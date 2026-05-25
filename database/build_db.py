"""
Constrói o banco de dados SQLite de patologias bacterianas no Brasil.
Uso: python database/build_db.py
"""

import sqlite3
import os
import sys

# Garante que o diretório pai está no path
sys.path.insert(0, os.path.dirname(__file__))

from data_fontes_bacterias_antibioticos import (
    FONTES_OFICIAIS, FAMILIAS_BACTERIANAS, BACTERIAS,
    CLASSES_ANTIBIOTICOS, ANTIBIOTICOS,
)
from data_patologias import CATEGORIAS_PATOLOGIAS, PATOLOGIAS
from data_eficacia import EFICACIA
from data_posologia import POSOLOGIA
from data_interacoes import INTERACOES
from data_tratamento_padrao_ouro import TRATAMENTO_PADRAO_OURO
from data_virais_agentes import (
    FONTES_VIRAIS, FAMILIAS_VIRAIS, VIRUS,
    CLASSES_ANTIVIRAIS, ANTIVIRAIS,
)
from data_virais_patologias import CATEGORIAS_VIRAIS, PATOLOGIAS_VIRAIS
from data_virais_eficacia import EFICACIA_VIRAL
from data_virais_posologia import POSOLOGIA_VIRAL
from data_virais_interacoes import INTERACOES_VIRAIS
from data_virais_tratamento import TRATAMENTO_PADRAO_OURO_VIRAL
from data_fungicos_agentes import (
    FONTES_FUNGICAS, FAMILIAS_FUNGICAS, FUNGOS,
    CLASSES_ANTIFUNGICOS, ANTIFUNGICOS,
)
from data_fungicos_patologias import CATEGORIAS_FUNGICAS, PATOLOGIAS_FUNGICAS
from data_fungicos_eficacia import EFICACIA_FUNGICA
from data_fungicos_posologia import POSOLOGIA_FUNGICA
from data_fungicos_interacoes import INTERACOES_FUNGICAS
from data_fungicos_tratamento import TRATAMENTO_PADRAO_OURO_FUNGICO

DB_PATH = os.path.join(os.path.dirname(__file__), "patologias_bacterianas_br.sqlite")
SCHEMA_PATH = os.path.join(os.path.dirname(__file__), "schema.sql")


def connect():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    conn.execute("PRAGMA journal_mode = WAL")
    return conn


def apply_schema(conn):
    with open(SCHEMA_PATH, "r") as f:
        conn.executescript(f.read())


def insert_fontes(conn):
    conn.executemany(
        "INSERT OR IGNORE INTO fontes_oficiais (sigla,nome,orgao,tipo,url,ano,descricao) VALUES (?,?,?,?,?,?,?)",
        FONTES_OFICIAIS,
    )


def insert_familias(conn):
    conn.executemany(
        "INSERT OR IGNORE INTO familias_bacterianas (nome,filo) VALUES (?,?)",
        FAMILIAS_BACTERIANAS,
    )


def get_id(conn, table, col, val):
    row = conn.execute(f"SELECT id FROM {table} WHERE {col}=?", (val,)).fetchone()
    if row:
        return row[0]
    raise ValueError(f"Não encontrado em {table}.{col}: {val!r}")


def insert_bacterias(conn):
    for row in BACTERIAS:
        nome_cient, nome_com, gram, familia_nome, aerobiose, formato, resist, obs = row
        familia_id = get_id(conn, "familias_bacterianas", "nome", familia_nome)
        conn.execute(
            """INSERT OR IGNORE INTO bacterias
               (nome_cientifico,nome_comum,gram,familia_id,aerobiose,formato,resistencia_natural,observacoes)
               VALUES (?,?,?,?,?,?,?,?)""",
            (nome_cient, nome_com, gram, familia_id, aerobiose, formato, resist, obs),
        )


def insert_classes(conn):
    conn.executemany(
        "INSERT OR IGNORE INTO classes_antibioticos (nome,mecanismo_acao,alvo_celular) VALUES (?,?,?)",
        CLASSES_ANTIBIOTICOS,
    )


def insert_antibioticos(conn):
    for row in ANTIBIOTICOS:
        nome_gen, nome_com, classe_nome, via, sus, anvisa, obs = row
        classe_id = get_id(conn, "classes_antibioticos", "nome", classe_nome)
        conn.execute(
            """INSERT OR IGNORE INTO antibioticos
               (nome_generico,nome_comercial,classe_id,via_administracao,disponivel_sus,anvisa_registrado,observacoes)
               VALUES (?,?,?,?,?,?,?)""",
            (nome_gen, nome_com, classe_id, via, int(sus), int(anvisa), obs),
        )


def insert_categorias(conn):
    conn.executemany(
        "INSERT OR IGNORE INTO categorias_patologias (nome,sistema) VALUES (?,?)",
        CATEGORIAS_PATOLOGIAS,
    )


def insert_patologias(conn):
    for row in PATOLOGIAS:
        (nome, cid10, cat_nome, desc, notif, tipo_notif,
         prev, mort, pop_risco, fonte_sigla) = row
        cat_id = get_id(conn, "categorias_patologias", "nome", cat_nome)
        fonte_id = get_id(conn, "fontes_oficiais", "sigla", fonte_sigla)
        conn.execute(
            """INSERT OR IGNORE INTO patologias
               (nome,cid10,categoria_id,descricao,notificacao_compulsoria,tipo_notificacao,
                prevalencia_br,mortalidade_br,populacao_risco,fonte_epidemio_id)
               VALUES (?,?,?,?,?,?,?,?,?,?)""",
            (nome, cid10, cat_id, desc, int(bool(notif)), tipo_notif,
             prev, mort, pop_risco, fonte_id),
        )


def _get_patologia_id_by_substr(conn, substr):
    """Busca patologia por substring do nome (case-insensitive)."""
    if substr is None:
        return None
    row = conn.execute(
        "SELECT id FROM patologias WHERE nome LIKE ?", (f"%{substr}%",)
    ).fetchone()
    return row[0] if row else None


def insert_eficacia(conn):
    inserted = 0
    skipped = 0
    for bact_nome, registros in EFICACIA.items():
        try:
            bact_id = get_id(conn, "bacterias", "nome_cientifico", bact_nome)
        except ValueError:
            print(f"  [AVISO] Bactéria não encontrada: {bact_nome!r}")
            skipped += len(registros)
            continue

        for rec in registros:
            (atb_nome, pat_substr, efic, linha, evidencia,
             resist, fonte_sigla, ano, obs) = rec

            try:
                atb_id = get_id(conn, "antibioticos", "nome_generico", atb_nome)
            except ValueError:
                print(f"  [AVISO] Antibiótico não encontrado: {atb_nome!r}")
                skipped += 1
                continue

            try:
                fonte_id = get_id(conn, "fontes_oficiais", "sigla", fonte_sigla)
            except ValueError:
                print(f"  [AVISO] Fonte não encontrada: {fonte_sigla!r}")
                fonte_id = None

            pat_id = _get_patologia_id_by_substr(conn, pat_substr)

            conn.execute(
                """INSERT OR IGNORE INTO eficacia_antibiotico
                   (bacteria_id,antibiotico_id,patologia_id,eficacia_pct,linha_tratamento,
                    nivel_evidencia,resistencia_br_pct,fonte_id,ano_dado,consideracoes)
                   VALUES (?,?,?,?,?,?,?,?,?,?)""",
                (bact_id, atb_id, pat_id, efic, linha, evidencia, resist, fonte_id, ano, obs),
            )
            inserted += 1

    return inserted, skipped


def insert_patologia_bacteria_links(conn):
    """
    Vincula patologias ↔ bactérias com base nos dados de eficácia
    já inseridos (bacteria_id + patologia_id presentes na tabela de eficácia).
    Também adiciona vínculos manuais adicionais.
    """
    # Links automáticos a partir da tabela de eficácia
    conn.execute(
        """INSERT OR IGNORE INTO patologia_bacteria (patologia_id, bacteria_id, papel)
           SELECT DISTINCT patologia_id, bacteria_id, 'principal'
           FROM eficacia_antibiotico
           WHERE patologia_id IS NOT NULL"""
    )

    # Links manuais adicionais (bacteria, patologia_substr, papel, freq_pct)
    extras = [
        ("Streptococcus pneumoniae",  "Sinusite Bacteriana Aguda",             "principal", 35.0),
        ("Streptococcus pneumoniae",  "Otite Média Aguda Bacteriana",          "principal", 40.0),
        ("Haemophilus influenzae",    "Sinusite Bacteriana Aguda",             "principal", 25.0),
        ("Haemophilus influenzae",    "Otite Média Aguda Bacteriana",          "principal", 25.0),
        ("Haemophilus influenzae",    "Bronquite Bacteriana Aguda",            "principal", 30.0),
        ("Haemophilus influenzae",    "Epiglotite Bacteriana Aguda",          "principal", 70.0),
        ("Staphylococcus aureus",     "Abscesso Pulmonar Bacteriano",          "principal", 30.0),
        ("Staphylococcus aureus",     "Artrite Séptica Bacteriana",            "principal", 45.0),
        ("Staphylococcus aureus",     "Empiema Pleural Bacteriano",            "secundario", 20.0),
        ("Staphylococcus aureus",     "Síndrome do Choque Tóxico Estafilocócico", "principal", 100.0),
        ("Staphylococcus aureus",     "Parotidite Bacteriana Supurativa",     "principal", 60.0),
        ("Staphylococcus aureus",     "Infecção de Prótese Articular (PJI)",   "principal", 30.0),
        ("Staphylococcus epidermidis","Infecção Relacionada a Cateter Venoso Central (CRBSI)", "principal", 35.0),
        ("Staphylococcus epidermidis","Infecção de Prótese Articular (PJI)",   "principal", 40.0),
        ("Escherichia coli",          "Peritonite Bacteriana Primária (Espontânea)", "principal", 50.0),
        ("Escherichia coli",          "Apendicite Bacteriana Secundária",     "principal", 35.0),
        ("Escherichia coli",          "Colangite Bacteriana Aguda",           "principal", 35.0),
        ("Escherichia coli",          "Abscesso Hepático Bacteriano",         "principal", 40.0),
        ("Escherichia coli",          "ITU Associada a Cateter (CAUTI)",      "principal", 45.0),
        ("Klebsiella pneumoniae",     "Abscesso Hepático Bacteriano",         "principal", 30.0),
        ("Klebsiella pneumoniae",     "Colangite Bacteriana Aguda",           "secundario", 25.0),
        ("Klebsiella pneumoniae",     "ITU Associada a Cateter (CAUTI)",      "secundario", 20.0),
        ("Pseudomonas aeruginosa",    "Infecção de Sítio Cirúrgico (ISC)",    "oportunista", 10.0),
        ("Pseudomonas aeruginosa",    "ITU Associada a Cateter (CAUTI)",      "oportunista", 10.0),
        ("Bacteroides fragilis",      "Apendicite Bacteriana Secundária",     "principal", 30.0),
        ("Bacteroides fragilis",      "Gangrena Gasosa (Clostridium perfringens)", "secundario", 15.0),
        ("Clostridium perfringens",   "Gangrena Gasosa (Clostridium perfringens)", "principal", 100.0),
        ("Clostridium botulinum",     "Botulismo Alimentar (Clostridium botulinum)", "principal", 100.0),
        ("Neisseria gonorrhoeae",     "Artrite Séptica Bacteriana",           "principal", 20.0),
        ("Mycobacterium tuberculosis","Pericardite Bacteriana",               "secundario", 25.0),
        ("Mycobacterium tuberculosis","Espondilodiscite Bacteriana",          "secundario", 20.0),
        ("Streptococcus pyogenes",    "Fasciíte Necrotizante",                "principal", 50.0),
        ("Streptococcus pyogenes",    "Escarlatina (Streptococcus pyogenes)", "principal", 100.0),
        ("Staphylococcus aureus",     "Fasciíte Necrotizante",                "secundario", 20.0),
        ("Staphylococcus aureus",     "Infecção de Corrente Sanguínea por Enterococcus Vancomicina-Resistente (VRE)", "oportunista", 5.0),
        ("Chlamydia trachomatis",     "Infecção por Mycoplasma hominis / Ureaplasma urealyticum", "secundario", 30.0),
    ]

    for bact_nome, pat_substr, papel, freq in extras:
        try:
            bact_id = get_id(conn, "bacterias", "nome_cientifico", bact_nome)
        except ValueError:
            continue
        pat_id = _get_patologia_id_by_substr(conn, pat_substr)
        if pat_id is None:
            continue
        conn.execute(
            """INSERT OR IGNORE INTO patologia_bacteria
               (patologia_id, bacteria_id, papel, frequencia_pct)
               VALUES (?,?,?,?)""",
            (pat_id, bact_id, papel, freq),
        )


def insert_posologia(conn):
    inserted = skipped = 0
    for rec in POSOLOGIA:
        (atb_nome, pat_substr, pop, dose, freq, via,
         dur_min, dur_max, dur_txt, aj_renal, aj_hep, obs, fonte_sigla) = rec
        try:
            atb_id = get_id(conn, "antibioticos", "nome_generico", atb_nome)
        except ValueError:
            skipped += 1
            continue
        pat_id = _get_patologia_id_by_substr(conn, pat_substr)
        try:
            fonte_id = get_id(conn, "fontes_oficiais", "sigla", fonte_sigla)
        except ValueError:
            fonte_id = None
        conn.execute(
            """INSERT INTO posologia
               (antibiotico_id,patologia_id,populacao,dose_unitaria,frequencia,via,
                duracao_min_dias,duracao_max_dias,duracao_texto,
                ajuste_renal,ajuste_hepatico,observacoes,fonte_id)
               VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)""",
            (atb_id, pat_id, pop, dose, freq, via,
             dur_min, dur_max, dur_txt,
             int(aj_renal), int(aj_hep), obs, fonte_id),
        )
        inserted += 1
    return inserted, skipped


def insert_interacoes(conn):
    inserted = skipped = 0
    for rec in INTERACOES:
        (atb_nome, med_inter, classe_inter,
         mecanismo, gravidade, efeito, conduta, fonte_sigla) = rec
        try:
            atb_id = get_id(conn, "antibioticos", "nome_generico", atb_nome)
        except ValueError:
            skipped += 1
            continue
        try:
            fonte_id = get_id(conn, "fontes_oficiais", "sigla", fonte_sigla)
        except ValueError:
            fonte_id = None
        conn.execute(
            """INSERT INTO interacoes_medicamentosas
               (antibiotico_id,medicamento_interagente,classe_interagente,
                mecanismo,gravidade,efeito_clinico,conduta,fonte_id)
               VALUES (?,?,?,?,?,?,?,?)""",
            (atb_id, med_inter, classe_inter,
             mecanismo, gravidade, efeito, conduta, fonte_id),
        )
        inserted += 1
    return inserted, skipped


def insert_fontes_virais(conn):
    conn.executemany(
        "INSERT OR IGNORE INTO fontes_oficiais (sigla,nome,orgao,tipo,url,ano,descricao) VALUES (?,?,?,?,?,?,?)",
        FONTES_VIRAIS,
    )


def insert_familias_virais(conn):
    conn.executemany(
        "INSERT OR IGNORE INTO familias_virais (nome,grupo) VALUES (?,?)",
        FAMILIAS_VIRAIS,
    )


def insert_virus(conn):
    for row in VIRUS:
        nome_cient, nome_com, familia_nome, tipo_an, envelope, transmissao, reservatorio = row
        familia_id = get_id(conn, "familias_virais", "nome", familia_nome)
        conn.execute(
            """INSERT OR IGNORE INTO virus
               (nome_cientifico,nome_comum,familia_id,tipo_acido_nucleico,envelope,transmissao_principal,reservatorio)
               VALUES (?,?,?,?,?,?,?)""",
            (nome_cient, nome_com, familia_id, tipo_an, envelope, transmissao, reservatorio),
        )


def insert_classes_antivirais(conn):
    conn.executemany(
        "INSERT OR IGNORE INTO classes_antivirais (nome,mecanismo_acao,alvo_celular) VALUES (?,?,?)",
        CLASSES_ANTIVIRAIS,
    )


def insert_antivirais(conn):
    for row in ANTIVIRAIS:
        nome_gen, nome_com, classe_nome, via, sus, anvisa, obs = row
        classe_id = get_id(conn, "classes_antivirais", "nome", classe_nome)
        conn.execute(
            """INSERT OR IGNORE INTO antivirais
               (nome_generico,nome_comercial,classe_id,via_administracao,disponivel_sus,anvisa_registrado,observacoes)
               VALUES (?,?,?,?,?,?,?)""",
            (nome_gen, nome_com, classe_id, via, int(sus), int(anvisa), obs),
        )


def insert_categorias_virais(conn):
    conn.executemany(
        "INSERT OR IGNORE INTO categorias_patologias (nome,sistema) VALUES (?,?)",
        CATEGORIAS_VIRAIS,
    )


def insert_patologias_virais(conn):
    for row in PATOLOGIAS_VIRAIS:
        (nome, cid10, cat_nome, desc, notif, tipo_notif,
         prev, mort, pop_risco, fonte_sigla) = row
        cat_id = get_id(conn, "categorias_patologias", "nome", cat_nome)
        fonte_id = get_id(conn, "fontes_oficiais", "sigla", fonte_sigla)
        conn.execute(
            """INSERT OR IGNORE INTO patologias
               (nome,cid10,categoria_id,descricao,notificacao_compulsoria,tipo_notificacao,
                prevalencia_br,mortalidade_br,populacao_risco,fonte_epidemio_id)
               VALUES (?,?,?,?,?,?,?,?,?,?)""",
            (nome, cid10, cat_id, desc, int(bool(notif)), tipo_notif,
             prev, mort, pop_risco, fonte_id),
        )


def insert_eficacia_viral(conn):
    inserted = skipped = 0
    for virus_nome, registros in EFICACIA_VIRAL.items():
        try:
            virus_id = get_id(conn, "virus", "nome_cientifico", virus_nome)
        except ValueError:
            print(f"  [AVISO] Vírus não encontrado: {virus_nome!r}")
            skipped += len(registros)
            continue

        for rec in registros:
            (atv_nome, pat_substr, efic, linha, evidencia,
             resist, fonte_sigla, ano, obs) = rec

            try:
                atv_id = get_id(conn, "antivirais", "nome_generico", atv_nome)
            except ValueError:
                print(f"  [AVISO] Antiviral não encontrado: {atv_nome!r}")
                skipped += 1
                continue

            try:
                fonte_id = get_id(conn, "fontes_oficiais", "sigla", fonte_sigla)
            except ValueError:
                fonte_id = None

            pat_id = _get_patologia_id_by_substr(conn, pat_substr)

            conn.execute(
                """INSERT OR IGNORE INTO eficacia_antiviral
                   (virus_id,antiviral_id,patologia_id,eficacia_pct,linha_tratamento,
                    nivel_evidencia,resistencia_br_pct,fonte_id,ano_dado,consideracoes)
                   VALUES (?,?,?,?,?,?,?,?,?,?)""",
                (virus_id, atv_id, pat_id, efic, linha, evidencia, resist, fonte_id, ano, obs),
            )

            if pat_id:
                conn.execute(
                    """INSERT OR IGNORE INTO patologia_virus (patologia_id, virus_id, papel)
                       VALUES (?, ?, 'principal')""",
                    (pat_id, virus_id),
                )
            inserted += 1

    return inserted, skipped


def insert_posologia_viral(conn):
    inserted = skipped = 0
    for rec in POSOLOGIA_VIRAL:
        (atv_nome, pat_substr, pop, dose, freq, via,
         dur_min, dur_max, dur_txt, aj_renal, aj_hep, obs, fonte_sigla) = rec
        try:
            atv_id = get_id(conn, "antivirais", "nome_generico", atv_nome)
        except ValueError:
            skipped += 1
            continue
        pat_id = _get_patologia_id_by_substr(conn, pat_substr)
        try:
            fonte_id = get_id(conn, "fontes_oficiais", "sigla", fonte_sigla)
        except ValueError:
            fonte_id = None
        conn.execute(
            """INSERT INTO posologia_viral
               (antiviral_id,patologia_id,populacao,dose_unitaria,frequencia,via,
                duracao_min_dias,duracao_max_dias,duracao_texto,
                ajuste_renal,ajuste_hepatico,observacoes,fonte_id)
               VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)""",
            (atv_id, pat_id, pop, dose, freq, via,
             dur_min, dur_max, dur_txt,
             int(aj_renal), int(aj_hep), obs, fonte_id),
        )
        inserted += 1
    return inserted, skipped


def insert_interacoes_virais(conn):
    inserted = skipped = 0
    for rec in INTERACOES_VIRAIS:
        (atv_nome, med_inter, classe_inter,
         mecanismo, gravidade, efeito, conduta, fonte_sigla) = rec
        try:
            atv_id = get_id(conn, "antivirais", "nome_generico", atv_nome)
        except ValueError:
            skipped += 1
            continue
        try:
            fonte_id = get_id(conn, "fontes_oficiais", "sigla", fonte_sigla)
        except ValueError:
            fonte_id = None
        conn.execute(
            """INSERT INTO interacoes_antivirais
               (antiviral_id,medicamento_interagente,classe_interagente,
                mecanismo,gravidade,efeito_clinico,conduta,fonte_id)
               VALUES (?,?,?,?,?,?,?,?)""",
            (atv_id, med_inter, classe_inter,
             mecanismo, gravidade, efeito, conduta, fonte_id),
        )
        inserted += 1
    return inserted, skipped


def insert_tratamento_padrao_ouro_viral(conn):
    inserted = skipped = 0
    for rec in TRATAMENTO_PADRAO_OURO_VIRAL:
        (pat_substr, atv_principal, combinacao, regime, duracao,
         justificativa, alt_alergia, alt_resistencia, obs,
         grau_rec, nivel_ev, fonte_sigla, ano_diretriz) = rec

        pat_id = _get_patologia_id_by_substr(conn, pat_substr)
        if pat_id is None:
            print(f"  [AVISO] Patologia viral não encontrada: {pat_substr!r}")
            skipped += 1
            continue

        try:
            fonte_id = get_id(conn, "fontes_oficiais", "sigla", fonte_sigla)
        except ValueError:
            fonte_id = None

        conn.execute(
            """INSERT OR IGNORE INTO tratamento_padrao_ouro_viral
               (patologia_id, antiviral_principal, combinacao, regime_resumido,
                duracao_resumida, justificativa, alternativa_alergia,
                alternativa_resistencia, obs_especiais, grau_recomendacao,
                nivel_evidencia, fonte_id, ano_diretriz)
               VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)""",
            (pat_id, atv_principal, combinacao, regime, duracao,
             justificativa, alt_alergia, alt_resistencia, obs,
             grau_rec, nivel_ev, fonte_id, ano_diretriz),
        )
        inserted += 1
    return inserted, skipped


def insert_fontes_fungicas(conn):
    conn.executemany(
        "INSERT OR IGNORE INTO fontes_oficiais (sigla,nome,orgao,tipo,url,ano,descricao) VALUES (?,?,?,?,?,?,?)",
        FONTES_FUNGICAS,
    )


def insert_familias_fungicas(conn):
    conn.executemany(
        "INSERT OR IGNORE INTO familias_fungicas (nome,grupo) VALUES (?,?)",
        FAMILIAS_FUNGICAS,
    )


def insert_fungos(conn):
    for row in FUNGOS:
        nome_cient, nome_com, familia_nome, tipo, transmissao, reservatorio, distribuicao = row
        familia_id = get_id(conn, "familias_fungicas", "nome", familia_nome)
        conn.execute(
            """INSERT OR IGNORE INTO fungos
               (nome_cientifico,nome_comum,familia_id,tipo,transmissao_principal,reservatorio,distribuicao_br)
               VALUES (?,?,?,?,?,?,?)""",
            (nome_cient, nome_com, familia_id, tipo, transmissao, reservatorio, distribuicao),
        )


def insert_classes_antifungicos(conn):
    conn.executemany(
        "INSERT OR IGNORE INTO classes_antifungicos (nome,mecanismo_acao,alvo_celular) VALUES (?,?,?)",
        CLASSES_ANTIFUNGICOS,
    )


def insert_antifungicos(conn):
    for row in ANTIFUNGICOS:
        nome_gen, nome_com, classe_nome, via, sus, anvisa, obs = row
        classe_id = get_id(conn, "classes_antifungicos", "nome", classe_nome)
        conn.execute(
            """INSERT OR IGNORE INTO antifungicos
               (nome_generico,nome_comercial,classe_id,via_administracao,disponivel_sus,anvisa_registrado,observacoes)
               VALUES (?,?,?,?,?,?,?)""",
            (nome_gen, nome_com, classe_id, via, int(sus), int(anvisa), obs),
        )


def insert_categorias_fungicas(conn):
    conn.executemany(
        "INSERT OR IGNORE INTO categorias_patologias (nome,sistema) VALUES (?,?)",
        CATEGORIAS_FUNGICAS,
    )


def insert_patologias_fungicas(conn):
    for row in PATOLOGIAS_FUNGICAS:
        (nome, cid10, cat_nome, desc, notif, tipo_notif,
         prev, mort, pop_risco, fonte_sigla) = row
        cat_id = get_id(conn, "categorias_patologias", "nome", cat_nome)
        fonte_id = get_id(conn, "fontes_oficiais", "sigla", fonte_sigla)
        conn.execute(
            """INSERT OR IGNORE INTO patologias
               (nome,cid10,categoria_id,descricao,notificacao_compulsoria,tipo_notificacao,
                prevalencia_br,mortalidade_br,populacao_risco,fonte_epidemio_id)
               VALUES (?,?,?,?,?,?,?,?,?,?)""",
            (nome, cid10, cat_id, desc, int(bool(notif)), tipo_notif,
             prev, mort, pop_risco, fonte_id),
        )


def insert_eficacia_fungica(conn):
    inserted = skipped = 0
    for fungo_nome, registros in EFICACIA_FUNGICA.items():
        try:
            fungo_id = get_id(conn, "fungos", "nome_cientifico", fungo_nome)
        except ValueError:
            print(f"  [AVISO] Fungo não encontrado: {fungo_nome!r}")
            skipped += len(registros)
            continue
        for rec in registros:
            (atf_nome, pat_substr, efic, linha, evidencia,
             resist, fonte_sigla, ano, obs) = rec
            try:
                atf_id = get_id(conn, "antifungicos", "nome_generico", atf_nome)
            except ValueError:
                print(f"  [AVISO] Antifúngico não encontrado: {atf_nome!r}")
                skipped += 1
                continue
            try:
                fonte_id = get_id(conn, "fontes_oficiais", "sigla", fonte_sigla)
            except ValueError:
                fonte_id = None
            pat_id = _get_patologia_id_by_substr(conn, pat_substr)
            conn.execute(
                """INSERT OR IGNORE INTO eficacia_antifungico
                   (fungo_id,antifungico_id,patologia_id,eficacia_pct,linha_tratamento,
                    nivel_evidencia,resistencia_br_pct,fonte_id,ano_dado,consideracoes)
                   VALUES (?,?,?,?,?,?,?,?,?,?)""",
                (fungo_id, atf_id, pat_id, efic, linha, evidencia, resist, fonte_id, ano, obs),
            )
            if pat_id:
                conn.execute(
                    """INSERT OR IGNORE INTO patologia_fungo (patologia_id, fungo_id, papel)
                       VALUES (?, ?, 'principal')""",
                    (pat_id, fungo_id),
                )
            inserted += 1
    return inserted, skipped


def insert_posologia_fungica(conn):
    inserted = skipped = 0
    for rec in POSOLOGIA_FUNGICA:
        (atf_nome, pat_substr, pop, dose, freq, via,
         dur_min, dur_max, dur_txt, aj_renal, aj_hep, obs, fonte_sigla) = rec
        try:
            atf_id = get_id(conn, "antifungicos", "nome_generico", atf_nome)
        except ValueError:
            skipped += 1
            continue
        pat_id = _get_patologia_id_by_substr(conn, pat_substr)
        try:
            fonte_id = get_id(conn, "fontes_oficiais", "sigla", fonte_sigla)
        except ValueError:
            fonte_id = None
        conn.execute(
            """INSERT INTO posologia_fungica
               (antifungico_id,patologia_id,populacao,dose_unitaria,frequencia,via,
                duracao_min_dias,duracao_max_dias,duracao_texto,
                ajuste_renal,ajuste_hepatico,observacoes,fonte_id)
               VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)""",
            (atf_id, pat_id, pop, dose, freq, via,
             dur_min, dur_max, dur_txt, int(aj_renal), int(aj_hep), obs, fonte_id),
        )
        inserted += 1
    return inserted, skipped


def insert_interacoes_fungicas(conn):
    inserted = skipped = 0
    for rec in INTERACOES_FUNGICAS:
        (atf_nome, med_inter, classe_inter,
         mecanismo, gravidade, efeito, conduta, fonte_sigla) = rec
        try:
            atf_id = get_id(conn, "antifungicos", "nome_generico", atf_nome)
        except ValueError:
            skipped += 1
            continue
        try:
            fonte_id = get_id(conn, "fontes_oficiais", "sigla", fonte_sigla)
        except ValueError:
            fonte_id = None
        conn.execute(
            """INSERT INTO interacoes_antifungicos
               (antifungico_id,medicamento_interagente,classe_interagente,
                mecanismo,gravidade,efeito_clinico,conduta,fonte_id)
               VALUES (?,?,?,?,?,?,?,?)""",
            (atf_id, med_inter, classe_inter,
             mecanismo, gravidade, efeito, conduta, fonte_id),
        )
        inserted += 1
    return inserted, skipped


def insert_tratamento_padrao_ouro_fungico(conn):
    inserted = skipped = 0
    for rec in TRATAMENTO_PADRAO_OURO_FUNGICO:
        (pat_substr, atf_principal, combinacao, regime, duracao,
         justificativa, alt_alergia, alt_resistencia, obs,
         grau_rec, nivel_ev, fonte_sigla, ano_diretriz) = rec
        pat_id = _get_patologia_id_by_substr(conn, pat_substr)
        if pat_id is None:
            print(f"  [AVISO] Patologia fúngica não encontrada: {pat_substr!r}")
            skipped += 1
            continue
        try:
            fonte_id = get_id(conn, "fontes_oficiais", "sigla", fonte_sigla)
        except ValueError:
            fonte_id = None
        conn.execute(
            """INSERT OR IGNORE INTO tratamento_padrao_ouro_fungico
               (patologia_id, antifungico_principal, combinacao, regime_resumido,
                duracao_resumida, justificativa, alternativa_alergia,
                alternativa_resistencia, obs_especiais, grau_recomendacao,
                nivel_evidencia, fonte_id, ano_diretriz)
               VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)""",
            (pat_id, atf_principal, combinacao, regime, duracao,
             justificativa, alt_alergia, alt_resistencia, obs,
             grau_rec, nivel_ev, fonte_id, ano_diretriz),
        )
        inserted += 1
    return inserted, skipped


def insert_tratamento_padrao_ouro(conn):
    inserted = skipped = 0
    for rec in TRATAMENTO_PADRAO_OURO:
        (pat_substr, atb_principal, combinacao, regime, duracao,
         justificativa, alt_alergia, alt_resistencia, obs,
         grau_rec, nivel_ev, fonte_sigla, ano_diretriz) = rec

        pat_id = _get_patologia_id_by_substr(conn, pat_substr)
        if pat_id is None:
            print(f"  [AVISO] Patologia não encontrada: {pat_substr!r}")
            skipped += 1
            continue

        try:
            fonte_id = get_id(conn, "fontes_oficiais", "sigla", fonte_sigla)
        except ValueError:
            fonte_id = None

        conn.execute(
            """INSERT OR IGNORE INTO tratamento_padrao_ouro
               (patologia_id, antibiotico_principal, combinacao, regime_resumido,
                duracao_resumida, justificativa, alternativa_alergia,
                alternativa_resistencia, obs_especiais, grau_recomendacao,
                nivel_evidencia, fonte_id, ano_diretriz)
               VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)""",
            (pat_id, atb_principal, combinacao, regime, duracao,
             justificativa, alt_alergia, alt_resistencia, obs,
             grau_rec, nivel_ev, fonte_id, ano_diretriz),
        )
        inserted += 1
    return inserted, skipped


def print_summary(conn):
    tables = [
        "fontes_oficiais", "familias_bacterianas", "bacterias",
        "classes_antibioticos", "antibioticos",
        "categorias_patologias", "patologias",
        "patologia_bacteria", "eficacia_antibiotico",
        "posologia", "interacoes_medicamentosas",
        "tratamento_padrao_ouro",
        "virus", "antivirais",
        "patologia_virus", "eficacia_antiviral",
        "posologia_viral", "interacoes_antivirais",
        "tratamento_padrao_ouro_viral",
        "fungos", "antifungicos",
        "patologia_fungo", "eficacia_antifungico",
        "posologia_fungica", "interacoes_antifungicos",
        "tratamento_padrao_ouro_fungico",
    ]
    print("\n── Resumo do banco de dados ──────────────────────")
    for t in tables:
        n = conn.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0]
        print(f"  {t:<40} {n:>5} registros")
    print("──────────────────────────────────────────────────\n")


def build():
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
        print(f"Banco anterior removido: {DB_PATH}")

    conn = connect()
    print("Aplicando schema...")
    apply_schema(conn)

    print("Inserindo fontes oficiais...")
    insert_fontes(conn)
    conn.commit()

    print("Inserindo famílias bacterianas...")
    insert_familias(conn)
    conn.commit()

    print("Inserindo bactérias...")
    insert_bacterias(conn)
    conn.commit()

    print("Inserindo classes de antibióticos...")
    insert_classes(conn)
    conn.commit()

    print("Inserindo antibióticos...")
    insert_antibioticos(conn)
    conn.commit()

    print("Inserindo categorias de patologias...")
    insert_categorias(conn)
    conn.commit()

    print("Inserindo patologias...")
    insert_patologias(conn)
    conn.commit()

    print("Inserindo dados de eficácia de antibióticos...")
    inserted, skipped = insert_eficacia(conn)
    conn.commit()
    print(f"  → {inserted} inseridos, {skipped} ignorados")

    print("Criando vínculos patologia ↔ bactéria...")
    insert_patologia_bacteria_links(conn)
    conn.commit()

    print("Inserindo posologia...")
    inserted, skipped = insert_posologia(conn)
    conn.commit()
    print(f"  → {inserted} inseridos, {skipped} ignorados")

    print("Inserindo interações medicamentosas...")
    inserted, skipped = insert_interacoes(conn)
    conn.commit()
    print(f"  → {inserted} inseridas, {skipped} ignoradas")

    print("Inserindo tratamento padrão-ouro...")
    inserted, skipped = insert_tratamento_padrao_ouro(conn)
    conn.commit()
    print(f"  → {inserted} inseridos, {skipped} ignorados")

    print("Inserindo fontes virais...")
    insert_fontes_virais(conn)
    conn.commit()

    print("Inserindo famílias virais...")
    insert_familias_virais(conn)
    conn.commit()

    print("Inserindo vírus...")
    insert_virus(conn)
    conn.commit()

    print("Inserindo classes de antivirais...")
    insert_classes_antivirais(conn)
    conn.commit()

    print("Inserindo antivirais...")
    insert_antivirais(conn)
    conn.commit()

    print("Inserindo categorias virais...")
    insert_categorias_virais(conn)
    conn.commit()

    print("Inserindo patologias virais...")
    insert_patologias_virais(conn)
    conn.commit()

    print("Inserindo eficácia de antivirais...")
    inserted, skipped = insert_eficacia_viral(conn)
    conn.commit()
    print(f"  → {inserted} inseridos, {skipped} ignorados")

    print("Inserindo posologia viral...")
    inserted, skipped = insert_posologia_viral(conn)
    conn.commit()
    print(f"  → {inserted} inseridos, {skipped} ignorados")

    print("Inserindo interações antivirais...")
    inserted, skipped = insert_interacoes_virais(conn)
    conn.commit()
    print(f"  → {inserted} inseridas, {skipped} ignoradas")

    print("Inserindo tratamento padrão-ouro viral...")
    inserted, skipped = insert_tratamento_padrao_ouro_viral(conn)
    conn.commit()
    print(f"  → {inserted} inseridos, {skipped} ignorados")

    print("Inserindo fontes fúngicas...")
    insert_fontes_fungicas(conn)
    conn.commit()

    print("Inserindo famílias fúngicas...")
    insert_familias_fungicas(conn)
    conn.commit()

    print("Inserindo fungos...")
    insert_fungos(conn)
    conn.commit()

    print("Inserindo classes de antifúngicos...")
    insert_classes_antifungicos(conn)
    conn.commit()

    print("Inserindo antifúngicos...")
    insert_antifungicos(conn)
    conn.commit()

    print("Inserindo categorias fúngicas...")
    insert_categorias_fungicas(conn)
    conn.commit()

    print("Inserindo patologias fúngicas...")
    insert_patologias_fungicas(conn)
    conn.commit()

    print("Inserindo eficácia de antifúngicos...")
    inserted, skipped = insert_eficacia_fungica(conn)
    conn.commit()
    print(f"  → {inserted} inseridos, {skipped} ignorados")

    print("Inserindo posologia fúngica...")
    inserted, skipped = insert_posologia_fungica(conn)
    conn.commit()
    print(f"  → {inserted} inseridos, {skipped} ignorados")

    print("Inserindo interações antifúngicos...")
    inserted, skipped = insert_interacoes_fungicas(conn)
    conn.commit()
    print(f"  → {inserted} inseridas, {skipped} ignoradas")

    print("Inserindo tratamento padrão-ouro fúngico...")
    inserted, skipped = insert_tratamento_padrao_ouro_fungico(conn)
    conn.commit()
    print(f"  → {inserted} inseridos, {skipped} ignorados")

    print_summary(conn)
    conn.close()
    print(f"Banco criado em: {DB_PATH}")
    return DB_PATH


if __name__ == "__main__":
    build()

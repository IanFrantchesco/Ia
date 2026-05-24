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


def print_summary(conn):
    tables = [
        "fontes_oficiais", "familias_bacterianas", "bacterias",
        "classes_antibioticos", "antibioticos",
        "categorias_patologias", "patologias",
        "patologia_bacteria", "eficacia_antibiotico",
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
    print(f"  → {inserted} registros inseridos, {skipped} ignorados")

    print("Criando vínculos patologia ↔ bactéria...")
    insert_patologia_bacteria_links(conn)
    conn.commit()

    print_summary(conn)
    conn.close()
    print(f"Banco criado em: {DB_PATH}")
    return DB_PATH


if __name__ == "__main__":
    build()

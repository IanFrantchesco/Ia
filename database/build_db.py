"""
Constrói o banco de dados SQLite de patologias bacterianas no Brasil.
Uso: python database/build_db.py
"""

import json
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
from data_parasitos_agentes import (
    FONTES_PARASITARIAS, FAMILIAS_PARASITARIAS, PARASITOS,
    CLASSES_ANTIPARASITARIOS, ANTIPARASITARIOS,
)
from data_parasitos_patologias import CATEGORIAS_PARASITOSES, PATOLOGIAS_PARASITOSES
from data_parasitos_eficacia import EFICACIA_PARASITARIA
from data_parasitos_posologia import POSOLOGIA_PARASITARIA
from data_parasitos_interacoes import INTERACOES_ANTIPARASITARIOS
from data_parasitos_tratamento import TRATAMENTO_PADRAO_OURO_PARASITARIO
from data_cronicas_fontes_medicamentos import (
    FONTES_CRONICAS, CLASSES_MEDICAMENTOS, MEDICAMENTOS,
)
from data_cronicas_patologias import CATEGORIAS_CRONICAS, PATOLOGIAS_CRONICAS
from data_cronicas_tratamento import TRATAMENTO_PADRAO_OURO_CRONICO
from data_cronicas_posologia_interacoes import (
    POSOLOGIA_CRONICA, INTERACOES_MEDICAMENTOS_CRONICOS,
)
from data_sintomas_bacterianas import SINTOMAS_BACTERIANAS
from data_sintomas_virais import SINTOMAS_VIRAIS
from data_sintomas_fungicas import SINTOMAS_FUNGICAS
from data_sintomas_parasitarias import SINTOMAS_PARASITARIAS
from data_sintomas_cronicas import SINTOMAS_CRONICAS
from data_criterios_bacterianas import CRITERIOS_BACTERIANAS
from data_criterios_virais import CRITERIOS_VIRAIS
from data_criterios_fungicas import CRITERIOS_FUNGICAS
from data_criterios_parasitarias import CRITERIOS_PARASITARIAS
from data_criterios_cronicas import CRITERIOS_CRONICAS

DB_PATH = os.path.join(os.path.dirname(__file__), "patologias_bacterianas_br.sqlite")
SCHEMA_PATH = os.path.join(os.path.dirname(__file__), "schema.sql")
# Baseline versionado das referências que o build hoje NÃO resolve (nomes de
# fármaco/medicamento/patologia que não casam) — 3c. Aceitas como dívida
# conhecida; o build FALHA só se surgir uma referência NOVA (ratchet).
KNOWN_UNRESOLVED = os.path.join(os.path.dirname(__file__), "known_unresolved.json")


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


# Substrings de patologia que casariam >1 patologia por LIKE e, sem correção,
# grudariam o dado numa doença ARBITRÁRIA. Mapeiam para o nome EXATO da
# patologia PRETENDIDA — decidido caso a caso pela droga do registro e
# confirmado em fonte oficial brasileira (PCDT/MS, SBC, SBPT). Ver o PR do S40.
# ('Influenza' e 'Imunocomprometidos' estavam ATIVAMENTE errados: gripe caía em
# PAC-Haemophilus (bacteriana) e a toxoplasmose caía em Listeriose.)
_PATOLOGIA_ALIAS = {
    'Influenza': 'Influenza (gripe sazonal e pandêmica)',
    'Imunocomprometidos': 'Toxoplasmose em Imunocomprometidos (HIV/AIDS)',
    'Hepatite B': 'Hepatite B (aguda e crônica)',
    'Bipolar Tipo I': 'Transtorno Bipolar Tipo I',
    'Visceral': 'Leishmaniose Visceral (Calazar)',
    'Compensada': 'Cirrose Hepática Compensada (Child-Pugh A)',
    'HIV/AIDS': 'HIV/AIDS (infecção aguda, crônica e AIDS estabelecida)',
    'Idiopática': 'Hipertensão Pulmonar Arterial Idiopática',
    'Alto Risco Cardiovascular': 'Diabetes Mellitus Tipo 2 com Complicações / Alto Risco Cardiovascular',
    'Luminal': 'Câncer de Mama — Luminal (Hormônio-Positivo, HER2-Negativo)',
    'Ressecável': 'Câncer Colorretal — Estágios I-III (Ressecável)',
    'Anticoagulação': 'Fibrilação Atrial — Anticoagulação / Controle de Ritmo',
    # Posologias crônicas gerais → variante BASE da doença (a droga deixa claro:
    # Metformina/anti-hipertensivos/Levotiroxina são o tratamento base, não a
    # sub-variante Gestação/Resistente/com Complicações).
    'Diabetes mellitus tipo 2': 'Diabetes Mellitus Tipo 2 (Sem Complicações)',
    'Hipertensão Arterial': 'Hipertensão Arterial Sistêmica — Estágio 1',
    'Hipotireoidismo': 'Hipotireoidismo Primário (Adulto)',
    # Normalização de nome (S42): a patologia existe sob outro nome.
    'Pneumocistose': 'Pneumonia por Pneumocystis jirovecii (PCP)',
}


# Normalização de NOME de medicamento crônico (S42): o fármaco JÁ existe na
# tabela ``medicamentos``, o dado-fonte só usa uma variante (abreviação, caixa,
# acento) que não casava no match exato. Alvo = nome exato do formulário
# (verificado contra o banco). NÃO é "dado faltando" — é o mesmo fármaco.
_MEDICAMENTO_ALIAS = {
    'AAS': 'Ácido Acetilsalicílico (antiagregante)',
    'Alendronato sódico': 'Alendronato',
    'Isossorbida mononitrato': 'Isossorbida Mononitrato',
    'Lítio': 'Lítio (carbonato)',
    'Lítio carbonato': 'Lítio (carbonato)',
    'Metoprolol succinato': 'Metoprolol Succinato',
    'Metotrexato': 'Metotrexato (reumatológico)',  # contexto crônico = AR/psoríase
    'Semaglutida': 'Semaglutida SC',               # dose SC/semana no registro
    'Sulfato ferroso': 'Sulfato Ferroso',
    # S43 — mais variantes que já existem em `medicamentos` (nome alternativo/
    # sal/grafia); alvo verificado contra o banco.
    'Cianocobalamina (Vitamina B12)': 'Cianocobalamina',
    'Levodopa / Carbidopa': 'Levodopa/Carbidopa',
    'Levodopa + Carbidopa': 'Levodopa/Carbidopa',
    'Mesalazina (5-ASA)': 'Mesalazina',
    'Salbutamol (Albuterol)': 'Salbutamol',
    'Ácido valproico / Valproato': 'Ácido Valproico',
    'Ácido valproico / Valproato de sódio': 'Ácido Valproico',
}


def _get_medicamento_cronico_id(conn, nome):
    """Resolve um medicamento crônico por nome exato, aplicando antes o
    ``_MEDICAMENTO_ALIAS`` (normalização de variantes). Retorna id ou None."""
    if not nome:
        return None
    nome = _MEDICAMENTO_ALIAS.get(nome, nome)
    row = conn.execute(
        "SELECT id FROM medicamentos WHERE nome_generico=?", (nome,)
    ).fetchone()
    return row[0] if row else None


# Fan-out de interações ancoradas em CLASSE (S45). A fonte (SBC etc.) agrupou
# algumas interações sob um rótulo de classe ("Beta-bloqueadores (atenolol,
# metoprolol, propranolol)"). O schema arquiva cada interação sob UM medicamento
# específico (``medicamento_id``), então um rótulo-de-classe não resolvia e a
# linha inteira era descartada — a interação sumia da API. Aqui cada âncora-classe
# é EXPANDIDA para os fármacos específicos que a fonte nomeia: uma linha vira N,
# uma por fármaco real. A especificidade fica explícita e revisável.
#
# Regra clínica que este dict codifica (por isso NÃO é um script cego):
#   • Efeito farmacodinâmico de CLASSE (ex.: β-bloq + verapamil → bloqueio AV) →
#     vale para todos os membros; expande para todos os nomeados.
#   • Efeito de MEMBRO específico (ex.: inibidores fortes de CYP2D6 × tamoxifeno)
#     → expande SÓ para os fármacos nomeados; jamais alargar para a classe toda.
# Alvos = nome_generico EXATO do catálogo (validado no teste e no build).
_INTERACAO_FANOUT = {
    # Farmacodinâmico de classe — todos os membros nomeados pela fonte.
    "Beta-bloqueadores (atenolol, metoprolol, propranolol)":
        ["Atenolol", "Metoprolol Succinato", "Propranolol"],
    "Estatinas (sinvastatina, atorvastatina)": ["Sinvastatina", "Atorvastatina"],
    "Estatinas (sinvastatina)": ["Sinvastatina"],
    "IECA (enalapril, ramipril)": ["Enalapril", "Ramipril"],
    "IECA (enalapril) / BRA (losartana)": ["Enalapril", "Losartana"],
    "Corticosteroide (prednisona)": ["Prednisona"],
    "ISRS (sertralina, fluoxetina, escitalopram)":
        ["Sertralina", "Fluoxetina", "Escitalopram"],
    # Sangramento com AINEs é efeito serotonérgico de classe (sem membros
    # nomeados na fonte) → todos os ISRS/IRSN do catálogo.
    "ISRS / IRSN":
        ["Sertralina", "Fluoxetina", "Escitalopram", "Paroxetina",
         "Venlafaxina", "Duloxetina"],
    # MEMBRO-específico: só inibidores fortes de CYP2D6 (NÃO alargar p/ ISRS).
    "Fluoxetina / Paroxetina (inibidores CYP2D6)": ["Fluoxetina", "Paroxetina"],
    "Sertralina / Fluoxetina (ISRS)": ["Sertralina", "Fluoxetina"],
    "Antipsicóticos (haloperidol, quetiapina, risperidona)":
        ["Haloperidol", "Quetiapina", "Risperidona"],
    "SGLT-2 (empagliflozina, dapagliflozina)": ["Empagliflozina", "Dapagliflozina"],
    "GLP-1 agonistas (semaglutida, liraglutida)": ["Semaglutida SC", "Liraglutida"],
    "Tofacitinibe / Baricitinibe (JAK inibidores)": ["Tofacitinibe", "Baricitinibe"],
    "AAS + Clopidogrel":
        ["Ácido Acetilsalicílico (antiagregante)", "Clopidogrel"],
    # Membro ausente do catálogo é OMITIDO (documentado): a linha resolve para os
    # que existem; o membro faltante fica como dívida menor até eventual cadastro.
    "Sulfonilureias (glibenclamida, glipizida)": ["Glibenclamida"],  # glipizida ausente
    "Darbepoetina alfa / Eritropoetina": ["Darbepoetina alfa"],       # eritropoetina ausente
}


def _fanout_interacao_ids(conn, anchor):
    """Se ``anchor`` é uma âncora-classe conhecida, retorna a lista de ids dos
    fármacos específicos para os quais a interação deve ser replicada. Cada nome
    do mapa DEVE resolver (senão é erro de digitação no mapa → ValueError, guard).
    Retorna None quando ``anchor`` não é fan-out (caller usa resolução simples)."""
    membros = _INTERACAO_FANOUT.get(anchor)
    if membros is None:
        return None
    ids = []
    for nome in membros:
        mid = _get_medicamento_cronico_id(conn, nome)
        if mid is None:
            raise ValueError(
                f"FANOUT: '{nome}' (de '{anchor}') não existe em medicamentos"
            )
        ids.append(mid)
    return ids


def _get_patologia_id_by_substr(conn, substr):
    """Resolve uma patologia por nome: alias conhecido → match exato → LIKE único.

    3f (risco clínico): antes o fallback LIKE usava ``.fetchone()`` SEM
    ``ORDER BY``/``LIMIT`` — se a substring casasse >1 patologia, escolhia uma
    ARBITRÁRIA, grudando tratamento/eficácia na doença errada, silenciosamente.
    Agora: (1) substrings ambíguas conhecidas são remapeadas para o nome exato
    (``_PATOLOGIA_ALIAS``); (2) se o LIKE ainda casar >1, o build FALHA com a
    lista de candidatos, forçando o dado-fonte a ser específico.
    """
    if substr is None:
        return None
    substr = _PATOLOGIA_ALIAS.get(substr, substr)
    row = conn.execute("SELECT id FROM patologias WHERE nome = ?", (substr,)).fetchone()
    if row:
        return row[0]
    rows = conn.execute(
        "SELECT id, nome FROM patologias WHERE nome LIKE ?", (f"%{substr}%",)
    ).fetchall()
    if len(rows) > 1:
        candidatos = [r[1] for r in rows]
        raise ValueError(
            f"Substring de patologia AMBÍGUA: {substr!r} casa {len(rows)} "
            f"patologias {candidatos} — torne o nome no dado-fonte específico "
            f"ou adicione um _PATOLOGIA_ALIAS."
        )
    return rows[0][0] if rows else None


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
        # Links extras — patologias bacterianas sem agente vinculado
        ("Streptococcus viridans (grupo)", "Endocardite Infecciosa por Streptococcus viridans",  "principal", 40.0),
        ("Staphylococcus aureus",     "Endoftalmite Bacteriana Pós-operatória",             "principal", 30.0),
        ("Staphylococcus epidermidis","Endoftalmite Bacteriana Pós-operatória",             "secundario", 25.0),
        ("Haemophilus influenzae",    "Pneumonia Adquirida na Comunidade (PAC) – Haemophilus", "principal", 80.0),
        ("Haemophilus influenzae",    "Meningite Bacteriana por Haemophilus",               "principal", 90.0),
        ("Streptococcus pneumoniae",  "Conjuntivite Bacteriana Aguda",                      "principal", 30.0),
        ("Haemophilus influenzae",    "Conjuntivite Bacteriana Aguda",                      "principal", 25.0),
        ("Staphylococcus aureus",     "Conjuntivite Bacteriana Aguda",                      "secundario", 20.0),
        ("Streptococcus viridans",    "Abscesso Dentário / Infecção Odontogênica",          "principal", 45.0),
        ("Staphylococcus aureus",     "Abscesso Dentário / Infecção Odontogênica",          "secundario", 15.0),
        ("Escherichia coli",          "Prostatite Bacteriana Aguda",                        "principal", 50.0),
        ("Klebsiella pneumoniae",     "Prostatite Bacteriana Aguda",                        "secundario", 15.0),
        ("Escherichia coli",          "ITU Gestacional / Bacteriúria Assintomática",        "principal", 70.0),
        ("Klebsiella pneumoniae",     "ITU Gestacional / Bacteriúria Assintomática",        "secundario", 15.0),
        ("Proteus mirabilis",         "ITU por Proteus mirabilis",                          "principal", 100.0),
        ("Mycobacterium ulcerans",    "Úlcera de Buruli – Mycobacterium ulcerans",          "principal", 100.0),
        ("Escherichia coli",          "Sepse Neonatal por Escherichia coli",                "principal", 100.0),
        ("Escherichia coli",          "Infecção por Escherichia coli Enteropatogênica",     "principal", 100.0),
        ("Shigella spp.",              "Shigelose (Disenteria Bacilar)",                     "principal", 100.0),
        ("Staphylococcus aureus",     "Difteria Cutânea",                                   "oportunista", 10.0),
        ("Corynebacterium diphtheriae","Difteria Cutânea",                                  "principal", 90.0),
        ("Streptococcus agalactiae",  "Sepse Neonatal por Escherichia coli",               "secundario", 15.0),
        # Links para patologias bacterianas ainda sem agente
        ("Streptococcus viridans (grupo)", "Abscesso Cerebral Bacteriano",               "principal", 35.0),
        ("Staphylococcus aureus",          "Abscesso Cerebral Bacteriano",               "secundario", 20.0),
        ("Borrelia spp.",                  "Febre Relapsante",                            "principal", 100.0),
        ("Burkholderia pseudomallei",      "Melioidose",                                  "principal", 100.0),
        ("Francisella tularensis",         "Tularemia",                                   "principal", 100.0),
        ("Streptococcus viridans (grupo)", "Abscesso Dentário",                           "principal", 45.0),
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


def insert_patologia_virus_links(conn):
    extras = [
        ("Dengue virus (DENV 1-4)",                      "Dengue",                           "principal", 100.0),
        ("Zika virus (ZIKV)",                            "Zika (infecção aguda",             "principal", 100.0),
        ("Zika virus (ZIKV)",                            "Síndrome Congênita do Zika",       "principal", 100.0),
        ("Chikungunya virus (CHIKV)",                    "Chikungunya",                      "principal", 100.0),
        ("Yellow fever virus (YFV)",                     "Febre Amarela",                    "principal", 100.0),
        ("West Nile virus (WNV)",                        "Febre do Nilo Ocidental",          "principal", 100.0),
        ("Hepatitis A virus (HAV)",                      "Hepatite A",                       "principal", 100.0),
        ("Hepatitis E virus (HEV)",                      "Hepatite E",                       "principal", 100.0),
        ("Human T-lymphotropic virus 1 (HTLV-1)",        "Infecção pelo HTLV-1",             "principal", 100.0),
        ("Human T-lymphotropic virus 1 (HTLV-1)",        "HTLV — Leucemia",                  "principal", 100.0),
        ("Human T-lymphotropic virus 1 (HTLV-1)",        "HTLV — Mielopatia",                "principal", 100.0),
        ("Epstein-Barr virus (EBV)",                     "Mononucleose Infecciosa",          "principal", 100.0),
        ("Human respiratory syncytial virus (RSV)",      "Infecção pelo Vírus Sincicial",    "principal", 100.0),
        ("Human adenovirus (HAdV)",                      "Infecção por Adenovírus",          "principal", 100.0),
        ("Measles morbillivirus",                        "Sarampo",                          "principal", 100.0),
        ("Rubella virus",                                "Rubéola",                          "principal", 100.0),
        ("Mumps orthorubulavirus",                       "Caxumba",                          "principal", 100.0),
        ("Enterovirus 71 (EV-A71)",                      "Doença Mão-Pé-Boca",              "principal", 60.0),
        ("Coxsackievirus A16 (CVA16)",                   "Doença Mão-Pé-Boca",              "principal", 40.0),
        ("Rotavirus A",                                  "Rotavirose",                       "principal", 100.0),
        ("Norovirus (GI/GII)",                           "Norovirose",                       "principal", 100.0),
        ("Rabies lyssavirus",                            "Raiva",                            "principal", 100.0),
        ("Enterovirus 71 (EV-A71)",                      "Meningite Viral",                  "principal", 40.0),
        ("Human papillomavirus (HPV)",                   "Infecção pelo HPV",                "principal", 100.0),
        ("Hantavirus (Araraquara, Juquitiba, Laguna Negra)", "Hantavirose",                  "principal", 100.0),
        ("Poliovirus (PV 1, 2, 3)",                      "Poliomielite",                     "principal", 100.0),
        ("Cytomegalovirus (CMV)",                        "CMV Congênito",                    "principal", 100.0),
        ("Hepatitis B virus (HBV)",                      "Hepatite B Perinatal",             "principal", 100.0),
        ("Herpes simplex virus 1 (HSV-1)",               "Herpes Neonatal",                  "principal", 50.0),
        ("Herpes simplex virus 2 (HSV-2)",               "Herpes Neonatal",                  "principal", 50.0),
        # Links a partir da eficácia viral — HIV, HCV, HBV, influenza, varicela, COVID
        ("Human immunodeficiency virus 1/2 (HIV-1/2)",  "HIV/AIDS",                         "principal", 100.0),
        ("Hepatitis C virus (HCV)",                      "Hepatite C",                       "principal", 100.0),
        ("Hepatitis B virus (HBV)",                      "Hepatite B",                       "principal", 100.0),
        ("Influenza virus A/B/C",                        "Influenza",                        "principal", 100.0),
        ("Varicella-zoster virus (VZV)",                 "Varicela",                         "principal", 100.0),
        ("Varicella-zoster virus (VZV)",                 "Herpes-Zóster",                    "principal", 100.0),
        ("SARS-CoV-2",                                   "COVID-19",                         "principal", 100.0),
        ("Herpes simplex virus 1 (HSV-1)",               "Herpes Labial / Genital",          "principal", 60.0),
        ("Herpes simplex virus 2 (HSV-2)",               "Herpes Labial / Genital",          "principal", 40.0),
        ("Cytomegalovirus (CMV)",                        "Doença por CMV em Imunocomprometi", "principal", 100.0),
        ("Epstein-Barr virus (EBV)",                     "Linfoma de Burkitt",               "secundario", 90.0),
        ("Human herpesvirus 8 (HHV-8)",                  "Sarcoma de Kaposi",                "principal", 100.0),
        ("Hepatitis D virus (HDV)",                      "Hepatite D",                       "principal", 100.0),
    ]
    for virus_nome, pat_substr, papel, freq in extras:
        try:
            virus_id = get_id(conn, "virus", "nome_cientifico", virus_nome)
        except ValueError:
            continue
        pat_id = _get_patologia_id_by_substr(conn, pat_substr)
        if pat_id is None:
            continue
        conn.execute(
            """INSERT OR IGNORE INTO patologia_virus
               (patologia_id, virus_id, papel, frequencia_pct)
               VALUES (?,?,?,?)""",
            (pat_id, virus_id, papel, freq),
        )


def insert_patologia_fungo_links(conn):
    extras = [
        ("Lacazia loboi",                    "Lobomicose",                       "principal", 100.0),
        ("Aspergillus fumigatus",            "Aspergiloma Pulmonar",             "principal", 70.0),
        ("Aspergillus fumigatus",            "Aspergilose Broncopulmonar",       "principal", 80.0),
        ("Aspergillus fumigatus",            "Rinossinusite Fúngica",            "principal", 40.0),
        ("Aspergillus flavus",               "Rinossinusite Fúngica",            "secundario", 20.0),
        ("Trichophyton rubrum",              "Dermatofitose Ungueal",            "principal", 70.0),
        ("Trichophyton rubrum",              "Tinea Corporis",                   "principal", 50.0),
        ("Pneumocystis jirovecii",           "Pneumonia por Pneumocystis",       "principal", 100.0),
        ("Fusarium solani",                  "Micetoma Fúngico",                 "principal", 30.0),
        ("Exophiala jeanselmei",             "Feohifomicose",                    "principal", 30.0),
        ("Bipolaris spicifera",              "Rinossinusite Fúngica",            "secundario", 15.0),
    ]
    for fungo_nome, pat_substr, papel, freq in extras:
        try:
            fungo_id = get_id(conn, "fungos", "nome_cientifico", fungo_nome)
        except ValueError:
            continue
        pat_id = _get_patologia_id_by_substr(conn, pat_substr)
        if pat_id is None:
            continue
        conn.execute(
            """INSERT OR IGNORE INTO patologia_fungo
               (patologia_id, fungo_id, papel, frequencia_pct)
               VALUES (?,?,?,?)""",
            (pat_id, fungo_id, papel, freq),
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

            if atv_nome is None:
                skipped += 1
                continue
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


def insert_fontes_parasitarias(conn):
    conn.executemany(
        "INSERT OR IGNORE INTO fontes_oficiais (sigla,nome,orgao,tipo,url,ano,descricao) VALUES (?,?,?,?,?,?,?)",
        FONTES_PARASITARIAS,
    )


def insert_familias_parasitarias(conn):
    conn.executemany(
        "INSERT OR IGNORE INTO familias_parasitarias (nome,filo) VALUES (?,?)",
        [(r[0], r[1]) for r in FAMILIAS_PARASITARIAS],
    )


def insert_parasitos(conn):
    for row in PARASITOS:
        (nome_cient, nome_com, familia_nome, tipo,
         ciclo, habitat, dist_br) = row[:7]
        reservatorio = row[7] if len(row) > 7 else None
        vetor = row[8] if len(row) > 8 else None
        try:
            familia_id = get_id(conn, "familias_parasitarias", "nome", familia_nome)
        except ValueError:
            familia_id = None
        conn.execute(
            """INSERT OR IGNORE INTO parasitos
               (nome_cientifico,nome_comum,familia_id,tipo,ciclo_hospedeiro,
                habitat_principal,distribuicao_br,reservatorio,vetor)
               VALUES (?,?,?,?,?,?,?,?,?)""",
            (nome_cient, nome_com, familia_id, tipo, ciclo, habitat, dist_br, reservatorio, vetor),
        )


def insert_classes_antiparasitarios(conn):
    conn.executemany(
        "INSERT OR IGNORE INTO classes_antiparasitarios (nome,mecanismo_acao,alvo_celular) VALUES (?,?,?)",
        CLASSES_ANTIPARASITARIOS,
    )


def insert_antiparasitarios(conn):
    for row in ANTIPARASITARIOS:
        nome_gen, nome_com, classe_nome, via, sus, anvisa, obs = row
        classe_id = get_id(conn, "classes_antiparasitarios", "nome", classe_nome)
        conn.execute(
            """INSERT OR IGNORE INTO antiparasitarios
               (nome_generico,nome_comercial,classe_id,via_administracao,disponivel_sus,anvisa_registrado,observacoes)
               VALUES (?,?,?,?,?,?,?)""",
            (nome_gen, nome_com, classe_id, via, int(sus), int(anvisa), obs),
        )


def insert_categorias_parasitoses(conn):
    conn.executemany(
        "INSERT OR IGNORE INTO categorias_patologias (nome,sistema) VALUES (?,?)",
        CATEGORIAS_PARASITOSES,
    )


def _num_to_prevalencia(v):
    if isinstance(v, str):
        return v
    if v >= 50000:
        return "muito_alta"
    if v >= 5000:
        return "alta"
    if v >= 500:
        return "media"
    if v >= 50:
        return "baixa"
    return "rara"


def _num_to_mortalidade(v):
    if isinstance(v, str):
        return v
    if v >= 1.0:
        return "alta"
    if v >= 0.1:
        return "media"
    return "baixa"


def insert_patologias_parasitoses(conn):
    for row in PATOLOGIAS_PARASITOSES:
        (nome, cid10, cat_nome, desc, notif, tipo_notif,
         prev, mort, pop_risco, fonte_sigla) = row
        cat_id = get_id(conn, "categorias_patologias", "nome", cat_nome)
        try:
            fonte_id = get_id(conn, "fontes_oficiais", "sigla", fonte_sigla)
        except ValueError:
            fonte_id = None
        conn.execute(
            """INSERT OR IGNORE INTO patologias
               (nome,cid10,categoria_id,descricao,notificacao_compulsoria,tipo_notificacao,
                prevalencia_br,mortalidade_br,populacao_risco,fonte_epidemio_id)
               VALUES (?,?,?,?,?,?,?,?,?,?)""",
            (nome, cid10, cat_id, desc, int(bool(notif)), tipo_notif,
             _num_to_prevalencia(prev), _num_to_mortalidade(mort), pop_risco, fonte_id),
        )


def insert_eficacia_parasitaria(conn):
    inserted = skipped = 0
    for parasito_nome, registros in EFICACIA_PARASITARIA.items():
        try:
            parasito_id = get_id(conn, "parasitos", "nome_cientifico", parasito_nome)
        except ValueError:
            print(f"  [AVISO] Parasito não encontrado: {parasito_nome!r}")
            skipped += len(registros)
            continue
        for rec in registros:
            (atp_nome, pat_substr, efic, linha, evidencia,
             resist, fonte_sigla, ano, obs) = rec
            if atp_nome is None:
                skipped += 1
                continue
            try:
                atp_id = get_id(conn, "antiparasitarios", "nome_generico", atp_nome)
            except ValueError:
                print(f"  [AVISO] Antiparasitário não encontrado: {atp_nome!r}")
                skipped += 1
                continue
            try:
                fonte_id = get_id(conn, "fontes_oficiais", "sigla", fonte_sigla)
            except ValueError:
                fonte_id = None
            pat_id = _get_patologia_id_by_substr(conn, pat_substr)
            conn.execute(
                """INSERT OR IGNORE INTO eficacia_antiparasitario
                   (parasito_id,antiparasitario_id,patologia_id,eficacia_pct,linha_tratamento,
                    nivel_evidencia,resistencia_br_pct,fonte_id,ano_dado,consideracoes)
                   VALUES (?,?,?,?,?,?,?,?,?,?)""",
                (parasito_id, atp_id, pat_id, efic, linha, evidencia, resist, fonte_id, ano, obs),
            )
            if pat_id:
                conn.execute(
                    """INSERT OR IGNORE INTO patologia_parasito (patologia_id, parasito_id, papel)
                       VALUES (?, ?, 'principal')""",
                    (pat_id, parasito_id),
                )
            inserted += 1
    return inserted, skipped


def insert_posologia_parasitaria(conn):
    inserted = skipped = 0
    for rec in POSOLOGIA_PARASITARIA:
        (atp_nome, pat_substr, pop, dose, freq, via,
         dur_min, dur_max, dur_txt, aj_renal, aj_hep, obs, fonte_sigla) = rec
        try:
            atp_id = get_id(conn, "antiparasitarios", "nome_generico", atp_nome)
        except ValueError:
            skipped += 1
            continue
        pat_id = _get_patologia_id_by_substr(conn, pat_substr)
        try:
            fonte_id = get_id(conn, "fontes_oficiais", "sigla", fonte_sigla)
        except ValueError:
            fonte_id = None
        conn.execute(
            """INSERT INTO posologia_parasitaria
               (antiparasitario_id,patologia_id,populacao,dose_unitaria,frequencia,via,
                duracao_min_dias,duracao_max_dias,duracao_texto,
                ajuste_renal,ajuste_hepatico,observacoes,fonte_id)
               VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)""",
            (atp_id, pat_id, pop, dose, freq, via,
             dur_min, dur_max, dur_txt, int(aj_renal), int(aj_hep), obs, fonte_id),
        )
        inserted += 1
    return inserted, skipped


def insert_interacoes_parasitarias(conn):
    inserted = skipped = 0
    for rec in INTERACOES_ANTIPARASITARIOS:
        (atp_nome, med_inter, classe_inter,
         mecanismo, gravidade, efeito, conduta, fonte_sigla) = rec
        try:
            atp_id = get_id(conn, "antiparasitarios", "nome_generico", atp_nome)
        except ValueError:
            skipped += 1
            continue
        try:
            fonte_id = get_id(conn, "fontes_oficiais", "sigla", fonte_sigla)
        except ValueError:
            fonte_id = None
        conn.execute(
            """INSERT INTO interacoes_antiparasitarios
               (antiparasitario_id,medicamento_interagente,classe_interagente,
                mecanismo,gravidade,efeito_clinico,conduta,fonte_id)
               VALUES (?,?,?,?,?,?,?,?)""",
            (atp_id, med_inter, classe_inter,
             mecanismo, gravidade, efeito, conduta, fonte_id),
        )
        inserted += 1
    return inserted, skipped


def insert_tratamento_padrao_ouro_parasitario(conn):
    inserted = skipped = 0
    for rec in TRATAMENTO_PADRAO_OURO_PARASITARIO:
        (pat_substr, atp_principal, combinacao, regime, duracao,
         justificativa, alt_alergia, alt_resistencia, obs,
         grau_rec, nivel_ev, fonte_sigla, ano_diretriz) = rec
        pat_id = _get_patologia_id_by_substr(conn, pat_substr)
        if pat_id is None:
            print(f"  [AVISO] Patologia parasitária não encontrada: {pat_substr!r}")
            skipped += 1
            continue
        try:
            fonte_id = get_id(conn, "fontes_oficiais", "sigla", fonte_sigla)
        except ValueError:
            fonte_id = None
        conn.execute(
            """INSERT OR IGNORE INTO tratamento_padrao_ouro_parasitario
               (patologia_id, antiparasitario_principal, combinacao, regime_resumido,
                duracao_resumida, justificativa, alternativa_alergia,
                alternativa_resistencia, obs_especiais, grau_recomendacao,
                nivel_evidencia, fonte_id, ano_diretriz)
               VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)""",
            (pat_id, atp_principal, combinacao, regime, duracao,
             justificativa, alt_alergia, alt_resistencia, obs,
             grau_rec, nivel_ev, fonte_id, ano_diretriz),
        )
        inserted += 1
    return inserted, skipped


def insert_patologia_parasito_links(conn):
    extras = [
        # Malária
        ("Plasmodium falciparum",          "Malária por Plasmodium falciparum", "principal", 100.0),
        ("Plasmodium vivax",               "Malária por Plasmodium vivax",      "principal", 100.0),
        ("Plasmodium malariae",            "Malária por Plasmodium malariae",   "principal", 100.0),
        # Leishmanioses
        ("Leishmania braziliensis",        "Leishmaniose Tegumentar",           "principal", 70.0),
        ("Leishmania amazonensis",         "Leishmaniose Tegumentar",           "principal", 15.0),
        ("Leishmania infantum (chagasi)",  "Leishmaniose Visceral",             "principal", 100.0),
        # Chagas
        ("Trypanosoma cruzi",              "Doença de Chagas Aguda",            "principal", 100.0),
        ("Trypanosoma cruzi",              "Doença de Chagas Crônica",          "principal", 100.0),
        # Toxoplasmose
        ("Toxoplasma gondii",              "Toxoplasmose em Imunocompetentes",  "principal", 100.0),
        ("Toxoplasma gondii",              "Toxoplasmose em Imunocomprometidos","principal", 100.0),
        ("Toxoplasma gondii",              "Toxoplasmose Congênita",            "principal", 100.0),
        # Protozooses intestinais
        ("Entamoeba histolytica",          "Amebíase Intestinal",               "principal", 100.0),
        ("Entamoeba histolytica",          "Abscesso Hepático Amebiano",        "principal", 100.0),
        ("Giardia lamblia (intestinalis/duodenalis)", "Giardíase",              "principal", 100.0),
        ("Trichomonas vaginalis",          "Tricomoníase",                      "principal", 100.0),
        ("Cryptosporidium parvum",         "Criptosporidiose",                  "principal", 100.0),
        # Helmintoses intestinais
        ("Ascaris lumbricoides",           "Ascaridíase",                       "principal", 100.0),
        ("Necator americanus",             "Ancilostomíase",                    "principal", 70.0),
        ("Ancylostoma duodenale",          "Ancilostomíase",                    "secundario", 30.0),
        ("Trichuris trichiura",            "Tricuríase",                        "principal", 100.0),
        ("Strongyloides stercoralis",      "Estrongiloidíase",                  "principal", 100.0),
        ("Strongyloides stercoralis",      "Hiperinfecção",                     "principal", 100.0),
        ("Enterobius vermicularis",        "Enterobíase",                       "principal", 100.0),
        ("Taenia solium",                  "Teníase",                           "principal", 50.0),
        ("Taenia saginata",                "Teníase",                           "principal", 50.0),
        ("Taenia solium",                  "Neurocisticercose",                 "principal", 100.0),
        # Helmintoses teciduais
        ("Schistosoma mansoni",            "Esquistossomose Mansoni",           "principal", 100.0),
        ("Wuchereria bancrofti",           "Filariose Linfática",               "principal", 100.0),
        ("Toxocara canis",                 "Toxocaríase",                       "principal", 100.0),
        ("Ancylostoma braziliense",        "Larva Migrans Cutânea",             "principal", 100.0),
        ("Echinococcus granulosus",        "Hidatidose",                        "principal", 100.0),
        ("Onchocerca volvulus",            "Oncocercose",                       "principal", 100.0),
        # Hepatobiliares
        ("Fasciola hepatica",              "Fasciolíase",                       "principal", 100.0),
        # Ectoparasitoses
        ("Pediculus humanus capitis",      "Pediculose do Couro Cabeludo",      "principal", 100.0),
        ("Sarcoptes scabiei",              "Escabiose",                         "principal", 100.0),
        ("Cochliomyia hominivorax",        "Miiase",                            "principal", 100.0),
    ]
    for parasito_nome, pat_substr, papel, freq in extras:
        try:
            parasito_id = get_id(conn, "parasitos", "nome_cientifico", parasito_nome)
        except ValueError:
            continue
        pat_id = _get_patologia_id_by_substr(conn, pat_substr)
        if pat_id is None:
            continue
        conn.execute(
            """INSERT OR IGNORE INTO patologia_parasito
               (patologia_id, parasito_id, papel, frequencia_pct)
               VALUES (?,?,?,?)""",
            (pat_id, parasito_id, papel, freq),
        )


def insert_fontes_cronicas(conn):
    conn.executemany(
        "INSERT OR IGNORE INTO fontes_oficiais (sigla,nome,orgao,tipo,url,ano,descricao) VALUES (?,?,?,?,?,?,?)",
        FONTES_CRONICAS,
    )


def insert_classes_medicamentos(conn):
    conn.executemany(
        "INSERT OR IGNORE INTO classes_medicamentos (nome,mecanismo_acao,alvo_terapeutico,area_terapeutica) VALUES (?,?,?,?)",
        CLASSES_MEDICAMENTOS,
    )


def insert_medicamentos(conn):
    for row in MEDICAMENTOS:
        nome_gen, nome_com, classe_nome, via, sus, anvisa, obs = row
        row_id = conn.execute(
            "SELECT id FROM classes_medicamentos WHERE nome=?", (classe_nome,)
        ).fetchone()
        classe_id = row_id[0] if row_id else None
        conn.execute(
            """INSERT OR IGNORE INTO medicamentos
               (nome_generico,nome_comercial,classe_id,via_administracao,disponivel_sus,anvisa_registrado,observacoes)
               VALUES (?,?,?,?,?,?,?)""",
            (nome_gen, nome_com, classe_id, via, int(sus), int(anvisa), obs),
        )


def insert_categorias_cronicas(conn):
    conn.executemany(
        "INSERT OR IGNORE INTO categorias_patologias (nome,sistema) VALUES (?,?)",
        CATEGORIAS_CRONICAS,
    )


def insert_patologias_cronicas(conn):
    for row in PATOLOGIAS_CRONICAS:
        (nome, cid10, cat_nome, desc, notif, tipo_notif,
         prev, mort, pop_risco, fonte_sigla) = row
        cat_id = get_id(conn, "categorias_patologias", "nome", cat_nome)
        try:
            fonte_id = get_id(conn, "fontes_oficiais", "sigla", fonte_sigla)
        except ValueError:
            fonte_id = None
        conn.execute(
            """INSERT OR IGNORE INTO patologias
               (nome,cid10,categoria_id,descricao,notificacao_compulsoria,tipo_notificacao,
                prevalencia_br,mortalidade_br,populacao_risco,fonte_epidemio_id)
               VALUES (?,?,?,?,?,?,?,?,?,?)""",
            (nome, cid10, cat_id, desc, int(bool(notif)), tipo_notif,
             prev, mort, pop_risco, fonte_id),
        )


def insert_tratamento_padrao_ouro_cronico(conn):
    inserted = skipped = 0
    for rec in TRATAMENTO_PADRAO_OURO_CRONICO:
        (pat_substr, med_principal, combinacao, regime, duracao,
         justificativa, alt_alergia, alt_resistencia, obs,
         grau_rec, nivel_ev, fonte_sigla, ano_diretriz) = rec
        pat_id = _get_patologia_id_by_substr(conn, pat_substr)
        if pat_id is None:
            print(f"  [AVISO] Patologia crônica não encontrada: {pat_substr!r}")
            skipped += 1
            continue
        try:
            fonte_id = get_id(conn, "fontes_oficiais", "sigla", fonte_sigla)
        except ValueError:
            fonte_id = None
        conn.execute(
            """INSERT OR IGNORE INTO tratamento_padrao_ouro_cronico
               (patologia_id, medicamento_principal, combinacao, regime_resumido,
                duracao_resumida, justificativa, alternativa_alergia,
                alternativa_resistencia, obs_especiais, grau_recomendacao,
                nivel_evidencia, fonte_id, ano_diretriz)
               VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)""",
            (pat_id, med_principal, combinacao, regime, duracao,
             justificativa, alt_alergia, alt_resistencia, obs,
             grau_rec, nivel_ev, fonte_id, ano_diretriz),
        )
        inserted += 1
    return inserted, skipped


def insert_posologia_cronica(conn):
    inserted = skipped = 0
    for rec in POSOLOGIA_CRONICA:
        (med_nome, pat_substr, pop, dose, freq, via,
         dur_txt, aj_renal, aj_hep, meta, obs, fonte_sigla) = rec
        med_id = _get_medicamento_cronico_id(conn, med_nome)
        if med_id is None:
            skipped += 1
            continue
        pat_id = _get_patologia_id_by_substr(conn, pat_substr)
        try:
            fonte_id = get_id(conn, "fontes_oficiais", "sigla", fonte_sigla)
        except ValueError:
            fonte_id = None
        conn.execute(
            """INSERT INTO posologia_cronica
               (medicamento_id,patologia_id,populacao,dose_unitaria,frequencia,via,
                duracao_texto,ajuste_renal,ajuste_hepatico,meta_terapeutica,observacoes,fonte_id)
               VALUES (?,?,?,?,?,?,?,?,?,?,?,?)""",
            (med_id, pat_id, pop, dose, freq, via,
             dur_txt, int(bool(aj_renal)), int(bool(aj_hep)), meta, obs, fonte_id),
        )
        inserted += 1
    return inserted, skipped


def insert_interacoes_medicamentos_cronicos(conn):
    inserted = skipped = 0
    for rec in INTERACOES_MEDICAMENTOS_CRONICOS:
        (med_nome, med_inter, classe_inter,
         mecanismo, gravidade, efeito, conduta, fonte_sigla) = rec
        # S45: âncora-classe é expandida para 1 linha por fármaco específico;
        # senão, resolução simples (1 âncora → 1 linha).
        med_ids = _fanout_interacao_ids(conn, med_nome)
        if med_ids is None:
            single = _get_medicamento_cronico_id(conn, med_nome)
            med_ids = [single] if single is not None else []
        if not med_ids:
            skipped += 1
            continue
        try:
            fonte_id = get_id(conn, "fontes_oficiais", "sigla", fonte_sigla)
        except ValueError:
            fonte_id = None
        for med_id in med_ids:
            conn.execute(
                """INSERT INTO interacoes_medicamentos
                   (medicamento_id,medicamento_interagente,classe_interagente,
                    mecanismo,gravidade,efeito_clinico,conduta,fonte_id)
                   VALUES (?,?,?,?,?,?,?,?)""",
                (med_id, med_inter, classe_inter,
                 mecanismo, gravidade, efeito, conduta, fonte_id),
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
        "familias_parasitarias", "parasitos",
        "classes_antiparasitarios", "antiparasitarios",
        "patologia_parasito", "eficacia_antiparasitario",
        "posologia_parasitaria", "interacoes_antiparasitarios",
        "tratamento_padrao_ouro_parasitario",
        "classes_medicamentos", "medicamentos",
        "tratamento_padrao_ouro_cronico",
        "posologia_cronica", "interacoes_medicamentos",
    ]
    print("\n── Resumo do banco de dados ──────────────────────")
    for t in tables:
        n = conn.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0]
        print(f"  {t:<40} {n:>5} registros")
    print("──────────────────────────────────────────────────\n")


def collect_unresolved(conn):
    """Re-deriva os descartes por nome não resolvido, REUSANDO as próprias
    funções de resolução do build (get_id / _get_patologia_id_by_substr) — logo
    não pode divergir do que o build realmente descarta. Retorna um set de
    strings ``"<categoria>: <nome>"``.

    Só conta descarte REAL (nome não-None que não resolve). Nomes None são
    intencionais (ex.: 'não há antiviral') e não entram. Patologia não resolvida
    só é descarte nos TRATAMENTOS/sintomas/critérios (que dão ``continue``); na
    eficácia, o registro entra com patologia_id NULL, então não conta aqui.
    """
    def _ok(table, col, name):
        if not name:
            return True
        try:
            get_id(conn, table, col, name)
            return True
        except ValueError:
            return False

    drops = set()
    efic = [
        ("efic_atb", EFICACIA, "antibioticos", "bacterias"),
        ("efic_atv", EFICACIA_VIRAL, "antivirais", "virus"),
        ("efic_atf", EFICACIA_FUNGICA, "antifungicos", "fungos"),
        ("efic_atp", EFICACIA_PARASITARIA, "antiparasitarios", "parasitos"),
    ]
    for kind, data, drug_tab, ag_tab in efic:
        for agente, regs in data.items():
            if not _ok(ag_tab, "nome_cientifico", agente):
                drops.add(f"{kind}:AGENTE:{agente}")
                continue
            for r in regs:
                if r[0] is not None and not _ok(drug_tab, "nome_generico", r[0]):
                    drops.add(f"{kind}:{r[0]}")

    lista = [
        ("pos_atb", POSOLOGIA, "antibioticos"), ("pos_atv", POSOLOGIA_VIRAL, "antivirais"),
        ("pos_atf", POSOLOGIA_FUNGICA, "antifungicos"), ("pos_atp", POSOLOGIA_PARASITARIA, "antiparasitarios"),
        ("int_atb", INTERACOES, "antibioticos"), ("int_atv", INTERACOES_VIRAIS, "antivirais"),
        ("int_atf", INTERACOES_FUNGICAS, "antifungicos"), ("int_atp", INTERACOES_ANTIPARASITARIOS, "antiparasitarios"),
    ]
    for kind, data, drug_tab in lista:
        for r in data:
            if r[0] is not None and not _ok(drug_tab, "nome_generico", r[0]):
                drops.add(f"{kind}:{r[0]}")

    # crônico: mesma resolução do build (alias de nome + match exato).
    # Interações: uma âncora-classe do fan-out (S45) NÃO é drop — resolve para
    # os fármacos específicos que expande.
    for r in POSOLOGIA_CRONICA:
        if r[0] and _get_medicamento_cronico_id(conn, r[0]) is None:
            drops.add(f"pos_cron:{r[0]}")
    for r in INTERACOES_MEDICAMENTOS_CRONICOS:
        if not r[0]:
            continue
        if r[0] in _INTERACAO_FANOUT:
            continue
        if _get_medicamento_cronico_id(conn, r[0]) is None:
            drops.add(f"int_cron:{r[0]}")

    # tratamentos: patologia não resolvida = registro descartado
    trats = [
        ("trat_atb", TRATAMENTO_PADRAO_OURO), ("trat_atv", TRATAMENTO_PADRAO_OURO_VIRAL),
        ("trat_atf", TRATAMENTO_PADRAO_OURO_FUNGICO), ("trat_atp", TRATAMENTO_PADRAO_OURO_PARASITARIO),
        ("trat_cron", TRATAMENTO_PADRAO_OURO_CRONICO),
    ]
    for kind, data in trats:
        for r in data:
            if r[0] and _get_patologia_id_by_substr(conn, r[0]) is None:
                drops.add(f"{kind}:PATOLOGIA:{r[0]}")

    return drops


def report_and_ratchet_drops(conn):
    """Relatório categorizado dos descartes + RATCHET: falha se surgir um NOVO
    (3c). Baseline em known_unresolved.json — dívida conhecida, aceita
    conscientemente; regressões (referência nova que não resolve) barram o build.
    """
    atual = collect_unresolved(conn)
    with open(KNOWN_UNRESOLVED, encoding="utf-8") as f:
        baseline = set(json.load(f))
    novos = atual - baseline
    resolvidos = baseline - atual

    from collections import Counter
    por_cat = Counter(d.split(":")[0] for d in atual)
    print("\n── Referências não resolvidas (dado descartado no build) ──")
    print(f"   {len(atual)} distintas | baseline aceito: {len(baseline)} | "
          f"por categoria: {dict(por_cat)}")
    if resolvidos:
        print(f"   [OK] {len(resolvidos)} do baseline foram RESOLVIDAS — "
              f"atualize known_unresolved.json removendo:")
        for r in sorted(resolvidos):
            print(f"        - {r}")
    if novos:
        print(f"   [ERRO] {len(novos)} referência(s) NOVA(S) não resolvida(s) — "
              f"dado clínico seria descartado em silêncio:")
        for n in sorted(novos):
            print(f"        + {n}")
        print("   Corrija o nome no dado-fonte, adicione um alias, ou (se "
              "aceitável) inclua em known_unresolved.json.")
        sys.exit(1)


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

    print("Criando vínculos patologia ↔ vírus...")
    insert_patologia_virus_links(conn)
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

    print("Criando vínculos patologia ↔ fungo...")
    insert_patologia_fungo_links(conn)
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

    print("Inserindo fontes parasitárias...")
    insert_fontes_parasitarias(conn)
    conn.commit()

    print("Inserindo famílias parasitárias...")
    insert_familias_parasitarias(conn)
    conn.commit()

    print("Inserindo parasitos...")
    insert_parasitos(conn)
    conn.commit()

    print("Inserindo classes de antiparasitários...")
    insert_classes_antiparasitarios(conn)
    conn.commit()

    print("Inserindo antiparasitários...")
    insert_antiparasitarios(conn)
    conn.commit()

    print("Inserindo categorias de parasitoses...")
    insert_categorias_parasitoses(conn)
    conn.commit()

    print("Inserindo patologias parasitárias...")
    insert_patologias_parasitoses(conn)
    conn.commit()

    print("Criando vínculos patologia ↔ parasito...")
    insert_patologia_parasito_links(conn)
    conn.commit()

    print("Inserindo eficácia de antiparasitários...")
    inserted, skipped = insert_eficacia_parasitaria(conn)
    conn.commit()
    print(f"  → {inserted} inseridos, {skipped} ignorados")

    print("Inserindo posologia parasitária...")
    inserted, skipped = insert_posologia_parasitaria(conn)
    conn.commit()
    print(f"  → {inserted} inseridos, {skipped} ignorados")

    print("Inserindo interações antiparasitários...")
    inserted, skipped = insert_interacoes_parasitarias(conn)
    conn.commit()
    print(f"  → {inserted} inseridas, {skipped} ignoradas")

    print("Inserindo tratamento padrão-ouro parasitário...")
    inserted, skipped = insert_tratamento_padrao_ouro_parasitario(conn)
    conn.commit()
    print(f"  → {inserted} inseridos, {skipped} ignorados")

    print("Inserindo fontes de doenças crônicas...")
    insert_fontes_cronicas(conn)
    conn.commit()

    print("Inserindo classes de medicamentos crônicos...")
    insert_classes_medicamentos(conn)
    conn.commit()

    print("Inserindo medicamentos crônicos...")
    insert_medicamentos(conn)
    conn.commit()

    print("Inserindo categorias de doenças crônicas...")
    insert_categorias_cronicas(conn)
    conn.commit()

    print("Inserindo patologias crônicas/não-infecciosas...")
    insert_patologias_cronicas(conn)
    conn.commit()

    print("Inserindo tratamento padrão-ouro crônico...")
    inserted, skipped = insert_tratamento_padrao_ouro_cronico(conn)
    conn.commit()
    print(f"  → {inserted} inseridos, {skipped} ignorados")

    print("Inserindo posologia crônica...")
    inserted, skipped = insert_posologia_cronica(conn)
    conn.commit()
    print(f"  → {inserted} inseridos, {skipped} ignorados")

    print("Inserindo interações de medicamentos crônicos...")
    inserted, skipped = insert_interacoes_medicamentos_cronicos(conn)
    conn.commit()
    print(f"  → {inserted} inseridas, {skipped} ignoradas")

    print("Inserindo sintomas...")
    inserted, skipped = insert_sintomas(conn)
    conn.commit()
    print(f"  → {inserted} vínculos inseridos, {skipped} patologias não encontradas")

    print("Inserindo critérios diagnósticos...")
    inserted, skipped = insert_criterios(conn)
    conn.commit()
    print(f"  → {inserted} critérios inseridos, {skipped} patologias não encontradas")

    print_summary(conn)
    report_and_ratchet_drops(conn)
    # Checkpoint TRUNCATE: transfere todo o WAL de volta ao arquivo principal e
    # esvazia o -wal. Deixa o artefato auto-contido (todo o dado no .sqlite), o
    # que o torna mais limpo para embarcar e seguro caso um dia seja servido de
    # um filesystem read-only (onde o -wal pendente não poderia ser reconciliado).
    conn.execute("PRAGMA wal_checkpoint(TRUNCATE)")
    conn.close()
    print(f"Banco criado em: {DB_PATH}")
    return DB_PATH


def insert_sintomas(conn):
    all_data = (
        SINTOMAS_BACTERIANAS + SINTOMAS_VIRAIS +
        SINTOMAS_FUNGICAS + SINTOMAS_PARASITARIAS + SINTOMAS_CRONICAS
    )
    inserted = skipped = 0
    for entry in all_data:
        row = conn.execute(
            "SELECT id FROM patologias WHERE nome = ?", (entry["patologia_nome"],)
        ).fetchone()
        if not row:
            skipped += 1
            continue
        pat_id = row[0]
        for s in entry["sintomas"]:
            conn.execute(
                "INSERT OR IGNORE INTO sintomas (nome, sistema, tipo) VALUES (?,?,?)",
                (s["nome"], s.get("sistema"), s.get("tipo")),
            )
            sin_id = conn.execute(
                "SELECT id FROM sintomas WHERE nome = ?", (s["nome"],)
            ).fetchone()[0]
            conn.execute(
                """INSERT OR REPLACE INTO patologia_sintoma
                   (patologia_id, sintoma_id, frequencia, onset_texto, severidade, ordem)
                   VALUES (?,?,?,?,?,?)""",
                (pat_id, sin_id, s.get("frequencia"), s.get("onset_texto"),
                 s.get("severidade"), s.get("ordem", 0)),
            )
            inserted += 1
    return inserted, skipped


def insert_criterios(conn):
    all_data = (
        CRITERIOS_BACTERIANAS + CRITERIOS_VIRAIS +
        CRITERIOS_FUNGICAS + CRITERIOS_PARASITARIAS + CRITERIOS_CRONICAS
    )
    inserted = skipped = 0
    for entry in all_data:
        row = conn.execute(
            "SELECT id FROM patologias WHERE nome = ?", (entry["patologia_nome"],)
        ).fetchone()
        if not row:
            skipped += 1
            continue
        pat_id = row[0]
        for c in entry.get("criterios", []):
            conn.execute(
                """INSERT INTO criterios_diagnosticos
                   (patologia_id, nome, categoria, tipo, descricao, valor_referencia, fonte, ordem)
                   VALUES (?,?,?,?,?,?,?,?)""",
                (pat_id, c["nome"], c.get("categoria"), c.get("tipo"),
                 c.get("descricao"), c.get("valor_referencia"), c.get("fonte"), c.get("ordem", 0)),
            )
            inserted += 1
        for e in entry.get("escores", []):
            conn.execute(
                """INSERT INTO escores_diagnosticos
                   (patologia_id, nome_escore, descricao, interpretacao, fonte, ordem)
                   VALUES (?,?,?,?,?,?)""",
                (pat_id, e["nome_escore"], e.get("descricao"),
                 e.get("interpretacao"), e.get("fonte"), e.get("ordem", 0)),
            )
    return inserted, skipped


if __name__ == "__main__":
    build()

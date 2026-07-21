"""Sanidade estrutural do banco construído (roda após database/build_db.py).

Diferente de test_api.py (contrato da API), esta suíte valida invariantes
ESTRUTURAIS do DADO: faixas numéricas, domínios de enumeração e integridade
referencial. Um erro de dado que passe por aqui serviria informação clínica
corrompida em produção — pega antes do deploy, no CI, logo após o build.

NÃO valida correção clínica (se a dose/eficácia está clinicamente certa — isso
exige revisão médica). Só assevera que a ESTRUTURA do dado é coerente.
"""
import app as app_module
import pytest

# (tabela de eficácia, tabela de fármaco, FK do fármaco) — os 4 domínios por agente.
EFF_TABLES = [
    ("eficacia_antibiotico", "antibioticos", "antibiotico_id"),
    ("eficacia_antiviral", "antivirais", "antiviral_id"),
    ("eficacia_antifungico", "antifungicos", "antifungico_id"),
    ("eficacia_antiparasitario", "antiparasitarios", "antiparasitario_id"),
]


@pytest.fixture(scope="module")
def db():
    with app_module.conn_bact() as conn:
        yield conn


def _count(db, sql):
    return db.execute(sql).fetchone()[0]


@pytest.mark.parametrize("tabela,_drug,_fk", EFF_TABLES)
def test_eficacia_e_resistencia_em_0_100(db, tabela, _drug, _fk):
    # Percentuais devem estar em [0,100] ou serem None (dado desconhecido).
    assert _count(db, f"SELECT COUNT(*) FROM {tabela} "
                      f"WHERE eficacia_pct NOT BETWEEN 0 AND 100") == 0
    assert _count(db, f"SELECT COUNT(*) FROM {tabela} "
                      f"WHERE resistencia_br_pct IS NOT NULL "
                      f"AND resistencia_br_pct NOT BETWEEN 0 AND 100") == 0


@pytest.mark.parametrize("tabela,_drug,_fk", EFF_TABLES)
def test_nivel_evidencia_e_linha_validos(db, tabela, _drug, _fk):
    # nivel_evidencia ∈ {A,B,C,D}; linha_tratamento ∈ {1,2,3} (ou None).
    assert _count(db, f"SELECT COUNT(*) FROM {tabela} "
                      f"WHERE nivel_evidencia IS NOT NULL "
                      f"AND nivel_evidencia NOT IN ('A','B','C','D')") == 0
    assert _count(db, f"SELECT COUNT(*) FROM {tabela} "
                      f"WHERE linha_tratamento IS NOT NULL "
                      f"AND linha_tratamento NOT IN (1,2,3)") == 0


@pytest.mark.parametrize("tabela,drug,fk", EFF_TABLES)
def test_sem_fk_orfa_em_eficacia(db, tabela, drug, fk):
    # Todo fármaco referenciado em eficácia deve existir na tabela de fármacos.
    assert _count(db, f"SELECT COUNT(*) FROM {tabela} e "
                      f"LEFT JOIN {drug} a ON a.id = e.{fk} WHERE a.id IS NULL") == 0


@pytest.mark.parametrize("tabela", ["posologia_cronica", "interacoes_medicamentos"])
def test_sem_fk_orfa_em_medicamentos(db, tabela):
    # Posologia/interações crônicas devem referenciar medicamentos existentes.
    assert _count(db, f"SELECT COUNT(*) FROM {tabela} x "
                      f"LEFT JOIN medicamentos m ON m.id = x.medicamento_id "
                      f"WHERE m.id IS NULL") == 0


def test_toda_patologia_tem_categoria(db):
    # Nenhuma patologia órfã de categoria (a API faz JOIN por categoria).
    assert _count(db, "SELECT COUNT(*) FROM patologias p "
                      "LEFT JOIN categorias_patologias c ON c.id = p.categoria_id "
                      "WHERE c.id IS NULL") == 0


def test_banco_nao_esta_vazio(db):
    # Sanidade mínima: o build populou as tabelas centrais.
    assert _count(db, "SELECT COUNT(*) FROM patologias") > 0
    assert _count(db, "SELECT COUNT(*) FROM categorias_patologias") > 0


# Toda linha clínica (eficácia/posologia/tratamento/interação) DEVE ter fonte
# vinculada — rastreabilidade é requisito clínico. O build engole em silêncio uma
# sigla de fonte que não resolve (fonte_id vira NULL); este guard trava isso no
# CI. Sem ele, um typo de sigla serviria dado clínico sem proveniência.
_TABELAS_COM_FONTE = [
    "eficacia_antibiotico", "eficacia_antiviral", "eficacia_antifungico",
    "eficacia_antiparasitario",
    "posologia", "posologia_viral", "posologia_fungica",
    "posologia_parasitaria", "posologia_cronica",
    "tratamento_padrao_ouro", "tratamento_padrao_ouro_viral",
    "tratamento_padrao_ouro_fungico", "tratamento_padrao_ouro_parasitario",
    "tratamento_padrao_ouro_cronico",
    "interacoes_medicamentosas", "interacoes_antivirais",
    "interacoes_antifungicos", "interacoes_antiparasitarios",
    "interacoes_medicamentos",
]


@pytest.mark.parametrize("tabela", _TABELAS_COM_FONTE)
def test_toda_linha_clinica_tem_fonte(db, tabela):
    # fonte_id NULL = dado clínico sem proveniência (sigla não resolveu no build).
    orfas = _count(db, f"SELECT COUNT(*) FROM {tabela} WHERE fonte_id IS NULL")
    assert orfas == 0, f"{orfas} linha(s) em {tabela} sem fonte vinculada"

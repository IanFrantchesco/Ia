"""Testes do build_db — foco no guard de resolução de patologia (S40, 3f).

O build resolve nomes de patologia por match exato e, como fallback, por LIKE.
Antes, um LIKE que casava >1 patologia escolhia uma ARBITRÁRIA e grudava o dado
clínico (tratamento/eficácia) na doença errada. O guard agora FALHA nesse caso;
substrings ambíguas CONHECIDAS são remapeadas para o nome exato via alias.
"""
import sqlite3
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "database"))
import build_db  # noqa: E402


def _db_com(nomes):
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE patologias (id INTEGER PRIMARY KEY, nome TEXT)")
    conn.executemany("INSERT INTO patologias(nome) VALUES (?)", [(n,) for n in nomes])
    return conn


def test_guard_levanta_em_substring_ambigua():
    # LIKE casa 2 patologias, sem match exato -> deve FALHAR (não escolher uma).
    conn = _db_com(["Hepatite C (aguda)", "Hepatite C crônica"])
    with pytest.raises(ValueError, match="AMB"):
        build_db._get_patologia_id_by_substr(conn, "Hepatite C")


def test_match_exato_tem_prioridade_sobre_like():
    # Se existe match exato, ele resolve mesmo que a substring casasse outras.
    conn = _db_com(["Dengue", "Dengue Grave"])
    assert build_db._get_patologia_id_by_substr(conn, "Dengue") is not None
    # "Dengue" casa exato "Dengue" -> retorna esse id (1), não ambíguo
    assert build_db._get_patologia_id_by_substr(conn, "Dengue") == 1


def test_unico_match_e_sem_match():
    conn = _db_com(["Malária por Plasmodium falciparum"])
    assert build_db._get_patologia_id_by_substr(conn, "falciparum") == 1
    assert build_db._get_patologia_id_by_substr(conn, "inexistente") is None
    assert build_db._get_patologia_id_by_substr(conn, None) is None


def test_alias_remapeia_substring_ambigua_para_nome_exato():
    # Uma substring conhecida como ambígua ('Influenza' casava PAC-Haemophilus)
    # é remapeada para o nome exato antes de resolver.
    alvo = build_db._PATOLOGIA_ALIAS["Influenza"]
    conn = _db_com([alvo, "Meningite Bacteriana por Haemophilus influenzae"])
    # sem alias, 'Influenza' casaria as duas por LIKE; com alias, casa exato o alvo
    assert build_db._get_patologia_id_by_substr(conn, "Influenza") == 1


def test_alias_cobre_as_ambiguidades_conhecidas():
    # Sanidade: o alias não está vazio e aponta para strings não-triviais.
    assert len(build_db._PATOLOGIA_ALIAS) >= 12
    for origem, alvo in build_db._PATOLOGIA_ALIAS.items():
        assert isinstance(alvo, str) and len(alvo) > len(origem) - 5


# ── S41: ratchet de referências não resolvidas (drops) ──────────────────────

def _conn_banco():
    return sqlite3.connect(build_db.DB_PATH)


def test_drops_atuais_nao_excedem_o_baseline():
    # 3c/ratchet: o build descarta silenciosamente registros cujo nome de
    # fármaco/medicamento/patologia não resolve. O baseline versionado
    # (known_unresolved.json) é a dívida aceita; NENHUM drop novo pode surgir
    # sem passar por revisão (mesmo critério do build, que faz sys.exit(1)).
    import json
    conn = _conn_banco()
    atual = build_db.collect_unresolved(conn)
    with open(build_db.KNOWN_UNRESOLVED, encoding="utf-8") as f:
        baseline = set(json.load(f))
    novos = atual - baseline
    assert not novos, f"drops NOVOS não baselinados: {sorted(novos)}"


def test_ratchet_falha_em_drop_novo(monkeypatch, tmp_path):
    # Um baseline menor que o conjunto atual (simulando um drop novo) deve
    # fazer report_and_ratchet_drops chamar sys.exit(1).
    import json
    conn = _conn_banco()
    atual = sorted(build_db.collect_unresolved(conn))
    assert atual, "esperava ao menos um drop conhecido para o teste"
    baseline_menor = tmp_path / "baseline.json"
    baseline_menor.write_text(json.dumps(atual[1:]), encoding="utf-8")  # falta 1
    monkeypatch.setattr(build_db, "KNOWN_UNRESOLVED", str(baseline_menor))
    with pytest.raises(SystemExit) as exc:
        build_db.report_and_ratchet_drops(conn)
    assert exc.value.code == 1


# ── S45: fan-out de interações ancoradas em classe ──────────────────────────

def test_fanout_alvos_todos_existem_no_catalogo():
    # Cada fármaco listado no mapa de fan-out DEVE existir em `medicamentos`
    # (nome_generico exato, via alias). Um typo no mapa quebra aqui e no build.
    conn = _conn_banco()
    for anchor, membros in build_db._INTERACAO_FANOUT.items():
        assert membros, f"fan-out de '{anchor}' está vazio"
        for nome in membros:
            assert build_db._get_medicamento_cronico_id(conn, nome) is not None, \
                f"'{nome}' (de '{anchor}') não resolve em medicamentos"


def test_fanout_expande_para_todos_os_membros():
    # Uma âncora-classe farmacodinâmica expande para 1 id por membro nomeado.
    conn = _conn_banco()
    ids = build_db._fanout_interacao_ids(
        conn, "Beta-bloqueadores (atenolol, metoprolol, propranolol)")
    assert ids is not None and len(ids) == 3
    assert len(set(ids)) == 3  # três fármacos distintos


def test_fanout_membro_especifico_nao_alarga_para_a_classe():
    # CYP2D6 é efeito de MEMBRO: expande só p/ Fluoxetina e Paroxetina — nunca
    # p/ Sertralina/Escitalopram (que não são inibidores fortes de CYP2D6).
    alvo = build_db._INTERACAO_FANOUT["Fluoxetina / Paroxetina (inibidores CYP2D6)"]
    assert set(alvo) == {"Fluoxetina", "Paroxetina"}
    assert "Sertralina" not in alvo and "Escitalopram" not in alvo


def test_fanout_anchor_nao_e_drop():
    # Uma âncora do fan-out NÃO pode aparecer como drop (ela resolve p/ os
    # fármacos específicos que expande).
    conn = _conn_banco()
    drops = build_db.collect_unresolved(conn)
    for anchor in build_db._INTERACAO_FANOUT:
        assert f"int_cron:{anchor}" not in drops


# ── S46: antimicrobianos do domínio fúngico (PCP) ───────────────────────────

def test_pcp_antimicrobianos_registrados_em_antifungicos():
    # Os fármacos do tratamento da PCP (que não são antifúngicos clássicos) foram
    # registrados no catálogo do domínio fúngico para resolverem eficácia/
    # posologia/interação da PCP e a sulfa da paracoccidioidomicose.
    conn = _conn_banco()
    esperados = ["Sulfametoxazol + Trimetoprima", "Pentamidina (isetionato)",
                 "Clindamicina", "Atovaquona"]
    catalogados = {r[0] for r in conn.execute(
        "SELECT nome_generico FROM antifungicos").fetchall()}
    for nome in esperados:
        assert nome in catalogados, f"{nome!r} não registrado em antifungicos"


def test_pcp_bloco_nao_tem_mais_drops():
    # Nenhuma referência do bloco PCP/paraco (efic/pos/int antifúngico) segue
    # sendo descartada após o cadastro cross-domínio.
    conn = _conn_banco()
    drops = build_db.collect_unresolved(conn)
    for prefixo in ("efic_atf:Atovaquona", "efic_atf:Clindamicina",
                    "efic_atf:Pentamidina", "efic_atf:Sulfadiazina + Trimetoprima",
                    "int_atf:Pentamidina (isetionato)",
                    "int_atf:Sulfametoxazol + Trimetoprima",
                    "pos_atf:Pentamidina (isetionato)",
                    "pos_atf:Sulfametoxazol + Trimetoprima"):
        assert prefixo not in drops


def test_pcp_primeira_linha_e_smx_tmp_nao_fallback():
    # Regressão do bug clínico: a PCP tinha o fármaco de escolha (SMX-TMP)
    # descartado e caía em card sintético. Agora é dado real de 1ª linha.
    conn = _conn_banco()
    pid = conn.execute(
        "SELECT id FROM patologias WHERE nome LIKE '%Pneumocystis%'").fetchone()[0]
    row = conn.execute(
        """SELECT a.nome_generico, e.linha_tratamento, e.eficacia_pct
           FROM eficacia_antifungico e JOIN antifungicos a ON a.id = e.antifungico_id
           WHERE e.patologia_id = ? AND e.linha_tratamento = 1""", (pid,)).fetchone()
    assert row is not None, "PCP sem eficácia de 1ª linha"
    assert row[0] == "Sulfametoxazol + Trimetoprima"
    assert row[2] and row[2] > 0

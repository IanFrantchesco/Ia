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

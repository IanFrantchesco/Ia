"""
Gera dados de sintomatologia para todas as patologias do banco.
Fonte: Ministério da Saúde (PCDT/Protocolos Clínicos), CFM, SBC, SBI, SBPT, SBMFC.

Uso:
    python database/generate_sintomas.py --domain bacteriana
    python database/generate_sintomas.py --domain viral
    python database/generate_sintomas.py --domain fungica
    python database/generate_sintomas.py --domain parasitaria
    python database/generate_sintomas.py --domain cronica
    python database/generate_sintomas.py --all

Saída: database/sintomas_gerados_<domain>.json
"""

import argparse
import json
import os
import sqlite3
import sys
import time

import anthropic

DB_PATH  = os.path.join(os.path.dirname(__file__), "patologias_bacterianas_br.sqlite")
OUT_DIR  = os.path.dirname(__file__)

DOMAIN_QUERY = {
    "bacteriana":  """
        SELECT DISTINCT p.id, p.nome, p.cid10, p.descricao
        FROM patologias p
        JOIN patologia_bacteria pb ON pb.patologia_id = p.id
        ORDER BY p.nome
    """,
    "viral": """
        SELECT DISTINCT p.id, p.nome, p.cid10, p.descricao
        FROM patologias p
        JOIN patologia_virus pv ON pv.patologia_id = p.id
        ORDER BY p.nome
    """,
    "fungica": """
        SELECT DISTINCT p.id, p.nome, p.cid10, p.descricao
        FROM patologias p
        JOIN patologia_fungo pf ON pf.patologia_id = p.id
        ORDER BY p.nome
    """,
    "parasitaria": """
        SELECT DISTINCT p.id, p.nome, p.cid10, p.descricao
        FROM patologias p
        JOIN patologia_parasito pp ON pp.patologia_id = p.id
        ORDER BY p.nome
    """,
    "cronica": """
        SELECT DISTINCT p.id, p.nome, p.cid10, p.descricao
        FROM patologias p
        JOIN tratamento_padrao_ouro_cronico t ON t.patologia_id = p.id
        ORDER BY p.nome
    """,
}

SYSTEM_PROMPT = """Você é um médico especialista em semiologia clínica com profundo conhecimento das diretrizes
brasileiras do Ministério da Saúde (PCDT), CFM, SBC, SBI, SBPT e SBMFC.

Ao receber uma lista de patologias, retorne EXCLUSIVAMENTE um JSON válido com os sintomas
baseados nas diretrizes oficiais brasileiras. Não invente dados — use somente o que está
documentado em fontes oficiais públicas brasileiras.

Formato de resposta (JSON puro, sem markdown, sem explicações):
{
  "patologias": [
    {
      "patologia_id": 1,
      "sintomas": [
        {
          "nome": "Febre",
          "sistema": "sistemico",
          "tipo": "cardinal",
          "frequencia": "muito_comum",
          "onset_texto": "1-3 dias após exposição",
          "severidade": "moderada",
          "ordem": 1
        }
      ]
    }
  ]
}

Valores permitidos:
- sistema: respiratorio, cardiovascular, neurologico, digestivo, cutaneo, musculoesqueletico, urinario, ocular, otorrinolaringologico, hematologico, endocrino, sistemico, outro
- tipo: cardinal, prodromico, sistemico, local, complicacao
- frequencia: muito_comum (>50%), comum (25-50%), incomum (10-25%), raro (<10%)
- severidade: leve, moderada, grave
- ordem: inteiro começando em 1 (sintomas mais importantes primeiro)

Inclua 5 a 12 sintomas por patologia. Priorize sintomas cardinais e mais frequentes."""


def build_user_prompt(patologias_batch: list[dict]) -> str:
    lines = ["Gere os sintomas para as seguintes patologias, baseando-se nas diretrizes oficiais brasileiras:\n"]
    for p in patologias_batch:
        desc = (p["descricao"] or "")[:200]
        lines.append(f"- ID {p['id']}: {p['nome']} (CID-10: {p['cid10'] or 'N/A'}) — {desc}")
    return "\n".join(lines)


def generate_for_domain(domain: str, batch_size: int = 10) -> list[dict]:
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        print("ERRO: ANTHROPIC_API_KEY não configurada.")
        sys.exit(1)

    client = anthropic.Anthropic(api_key=api_key)

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    rows = conn.execute(DOMAIN_QUERY[domain]).fetchall()
    conn.close()

    patologias = [dict(r) for r in rows]
    print(f"Domínio {domain}: {len(patologias)} patologias encontradas")

    all_results = []
    total_batches = (len(patologias) + batch_size - 1) // batch_size

    for i in range(0, len(patologias), batch_size):
        batch = patologias[i : i + batch_size]
        batch_num = i // batch_size + 1
        print(f"  Lote {batch_num}/{total_batches}: {[p['nome'][:30] for p in batch]}")

        try:
            msg = client.messages.create(
                model="claude-sonnet-4-6",
                max_tokens=4096,
                system=SYSTEM_PROMPT,
                messages=[{"role": "user", "content": build_user_prompt(batch)}],
            )
            raw = msg.content[0].text.strip()

            # Remove markdown code fences if present
            if raw.startswith("```"):
                raw = raw.split("```")[1]
                if raw.startswith("json"):
                    raw = raw[4:]
            raw = raw.strip()

            data = json.loads(raw)
            all_results.extend(data.get("patologias", []))
            print(f"    ✓ {len(data.get('patologias', []))} patologias geradas")

        except json.JSONDecodeError as e:
            print(f"    ✗ Erro JSON no lote {batch_num}: {e}")
            print(f"    Resposta raw: {raw[:300]}")
        except Exception as e:
            print(f"    ✗ Erro no lote {batch_num}: {e}")

        # Respeita rate limit
        if batch_num < total_batches:
            time.sleep(1)

    return all_results


def save_results(domain: str, results: list[dict]) -> str:
    out_path = os.path.join(OUT_DIR, f"sintomas_gerados_{domain}.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"\nSalvo em: {out_path} ({len(results)} patologias)")
    return out_path


def main():
    parser = argparse.ArgumentParser(description="Gera sintomatologia via Claude API")
    parser.add_argument("--domain", choices=list(DOMAIN_QUERY.keys()), help="Domínio a processar")
    parser.add_argument("--all", action="store_true", help="Processar todos os domínios")
    parser.add_argument("--batch-size", type=int, default=10, help="Patologias por chamada API (padrão: 10)")
    args = parser.parse_args()

    if args.all:
        domains = list(DOMAIN_QUERY.keys())
    elif args.domain:
        domains = [args.domain]
    else:
        parser.print_help()
        sys.exit(1)

    for domain in domains:
        print(f"\n{'='*50}")
        print(f"Gerando sintomas: {domain.upper()}")
        print(f"{'='*50}")
        results = generate_for_domain(domain, args.batch_size)
        save_results(domain, results)


if __name__ == "__main__":
    main()

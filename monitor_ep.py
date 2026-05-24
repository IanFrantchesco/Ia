#!/usr/bin/env python3
"""Monitor de Artigos de Eletrofisiologia Cardíaca"""

import os
import time
import xml.etree.ElementTree as ET
from datetime import datetime

import requests
import anthropic
from dotenv import load_dotenv

load_dotenv()

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")
PUBMED_API_KEY = os.getenv("PUBMED_API_KEY", "")
MAX_ARTICLES = int(os.getenv("MAX_ARTICLES", "20"))
MAX_MSG_LENGTH = 3800

JOURNALS = [
    '"Heart Rhythm"[Journal]',
    '"Circ Arrhythm Electrophysiol"[Journal]',
    '"JACC Clin Electrophysiol"[Journal]',
    '"J Cardiovasc Electrophysiol"[Journal]',
    '"Europace"[Journal]',
]

PUBMED_BASE = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"


def search_pubmed(query: str, days: int = 7) -> list[str]:
    params = {
        "db": "pubmed",
        "term": query,
        "retmax": MAX_ARTICLES,
        "retmode": "json",
        "reldate": days,
        "datetype": "pdat",
        "usehistory": "n",
    }
    if PUBMED_API_KEY:
        params["api_key"] = PUBMED_API_KEY

    resp = requests.get(f"{PUBMED_BASE}/esearch.fcgi", params=params, timeout=30)
    resp.raise_for_status()
    data = resp.json()
    return data.get("esearchresult", {}).get("idlist", [])


def fetch_article_details(pmids: list[str]) -> str:
    if not pmids:
        return ""

    params = {
        "db": "pubmed",
        "id": ",".join(pmids),
        "retmode": "xml",
        "rettype": "abstract",
    }
    if PUBMED_API_KEY:
        params["api_key"] = PUBMED_API_KEY

    resp = requests.get(f"{PUBMED_BASE}/efetch.fcgi", params=params, timeout=60)
    resp.raise_for_status()
    return resp.text


def _get_text(element, path: str, default: str = "") -> str:
    node = element.find(path)
    if node is not None and node.text:
        return node.text.strip()
    return default


def parse_pubmed_xml(xml_content: str) -> list[dict]:
    root = ET.fromstring(xml_content)
    articles = []

    for article in root.findall(".//PubmedArticle"):
        medline = article.find("MedlineCitation")
        if medline is None:
            continue

        art = medline.find("Article")
        if art is None:
            continue

        title = _get_text(art, "ArticleTitle")

        abstract_texts = []
        for ab in art.findall(".//AbstractText"):
            label = ab.get("Label", "")
            text = ab.text or ""
            if label:
                abstract_texts.append(f"{label}: {text.strip()}")
            elif text.strip():
                abstract_texts.append(text.strip())
        abstract = " ".join(abstract_texts)

        journal = _get_text(art, "Journal/Title")

        pub_date_node = art.find("Journal/JournalIssue/PubDate")
        pub_date = ""
        if pub_date_node is not None:
            year = _get_text(pub_date_node, "Year")
            month = _get_text(pub_date_node, "Month", "01")
            day = _get_text(pub_date_node, "Day", "01")
            if not year:
                medline_date = _get_text(pub_date_node, "MedlineDate")
                pub_date = medline_date[:10] if medline_date else ""
            else:
                month_map = {
                    "Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04",
                    "May": "05", "Jun": "06", "Jul": "07", "Aug": "08",
                    "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12",
                }
                month = month_map.get(month, month.zfill(2))
                pub_date = f"{day.zfill(2)}/{month}/{year}"

        pmid_node = medline.find("PMID")
        pmid = pmid_node.text.strip() if pmid_node is not None else ""
        link = f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/" if pmid else ""

        if title and pmid:
            articles.append({
                "pmid": pmid,
                "title": title,
                "abstract": abstract,
                "journal": journal,
                "pub_date": pub_date,
                "link": link,
            })

    return articles


def generate_portuguese_summary(article: dict, client: anthropic.Anthropic) -> str:
    if not article.get("abstract"):
        return "Resumo não disponível."

    prompt = (
        f"Título: {article['title']}\n\n"
        f"Resumo original (inglês):\n{article['abstract']}\n\n"
        "Crie um resumo em português brasileiro deste artigo de eletrofisiologia cardíaca. "
        "Máximo 3-4 frases destacando: objetivo do estudo, principal resultado e relevância clínica."
    )

    response = client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=350,
        system=(
            "Você é um médico cardiologista especialista em eletrofisiologia cardíaca. "
            "Crie resumos CURTOS e OBJETIVOS em português brasileiro de artigos científicos. "
            "Máximo 3-4 frases. Destaque: objetivo, resultado principal e relevância clínica. "
            "Use linguagem técnica apropriada. Seja direto."
        ),
        messages=[{"role": "user", "content": prompt}],
    )
    return response.content[0].text.strip()


def format_messages(articles: list[dict]) -> list[str]:
    today = datetime.now().strftime("%d/%m/%Y")
    header = (
        f"🫀 *MONITOR DE ELETROFISIOLOGIA CARDÍACA*\n"
        f"📅 Atualização: {today}\n"
        f"📊 {len(articles)} artigo(s) dos últimos 7 dias\n"
        f"━━━━━━━━━━━━━━━━━━━\n"
    )

    chunks = []
    current = header

    for i, art in enumerate(articles, 1):
        block = (
            f"\n*{i}. {art['title']}*\n\n"
            f"📰 _{art['journal']}_\n"
            f"📆 {art['pub_date']}\n\n"
            f"📝 {art.get('summary', 'Resumo não disponível.')}\n\n"
            f"🔗 {art['link']}\n"
            f"━━━━━━━━━━━━━━━━━━━\n"
        )

        if len(current) + len(block) > MAX_MSG_LENGTH:
            chunks.append(current)
            current = block
        else:
            current += block

    chunks.append(current if current != header else header + "\n_Nenhum artigo encontrado nos últimos 7 dias._")
    return chunks


def main():
    print("🫀 Monitor de Eletrofisiologia Cardíaca")
    print(f"📅 {datetime.now().strftime('%d/%m/%Y %H:%M')}\n")

    all_pmids: list[str] = []
    for journal_query in JOURNALS:
        print(f"  Buscando: {journal_query}")
        try:
            pmids = search_pubmed(journal_query)
            print(f"    → {len(pmids)} artigo(s)")
            all_pmids.extend(pmids)
        except Exception as e:
            print(f"    → Erro: {e}")
        time.sleep(0.4 if not PUBMED_API_KEY else 0.15)

    seen: set[str] = set()
    unique_pmids = [p for p in all_pmids if not (p in seen or seen.add(p))]
    unique_pmids = unique_pmids[:MAX_ARTICLES]

    print(f"\n📊 Total: {len(unique_pmids)} artigo(s) único(s)")

    if not unique_pmids:
        print("Nenhum artigo encontrado. Encerrando.")
        return

    print("\n📥 Buscando detalhes...")
    xml_content = fetch_article_details(unique_pmids)
    articles = parse_pubmed_xml(xml_content)
    print(f"  → {len(articles)} artigo(s) processado(s)")

    if not ANTHROPIC_API_KEY:
        print("\n⚠️  ANTHROPIC_API_KEY não configurada — resumos não serão gerados.")
        for art in articles:
            art["summary"] = (art.get("abstract", "")[:300] + "...") if art.get("abstract") else "Resumo não disponível."
    else:
        print("\n🤖 Gerando resumos em português...")
        client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
        for i, art in enumerate(articles, 1):
            print(f"  [{i}/{len(articles)}] {art['title'][:70]}...")
            try:
                art["summary"] = generate_portuguese_summary(art, client)
            except Exception as e:
                print(f"    → Erro: {e}")
                art["summary"] = "Resumo não disponível."
            time.sleep(0.2)

    messages = format_messages(articles)

    # Save to file
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"ep_monitor_{ts}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write("\n\n--- PRÓXIMA MENSAGEM ---\n\n".join(messages))
    print(f"\n💾 Salvo em: {filename}")

    # Print to terminal for copy-paste
    separator = "\n" + "=" * 50 + "\n"
    print(f"\n{'=' * 50}")
    if len(messages) > 1:
        print(f"⚠️  Mensagem longa — dividida em {len(messages)} partes. Copie e envie uma por vez.")
    print(separator.join(messages))
    print("=" * 50)
    print("\n✅ Copie o texto acima e cole no WhatsApp!")


if __name__ == "__main__":
    main()

"""
Banco de Dados Econômico do Brasil (1930-2024)
20 principais variáveis econômicas e sociais, por mandato presidencial.
Fontes: IPEAData, Banco Mundial, IBGE, BCB
"""

import sqlite3
import csv
import os
import json
import requests
import pandas as pd
from pathlib import Path

OUTPUT_DIR = Path(__file__).parent / "output"
OUTPUT_DIR.mkdir(exist_ok=True)

# ---------------------------------------------------------------------------
# 1. MANDATOS PRESIDENCIAIS
# ---------------------------------------------------------------------------
MANDATOS = [
    {"presidente": "Getúlio Vargas",          "partido": "sem partido",  "inicio": 1930, "fim": 1945, "fase": "Revolução/Estado Novo"},
    {"presidente": "José Linhares",           "partido": "sem partido",  "inicio": 1945, "fim": 1945, "fase": "Transição"},
    {"presidente": "Eurico Gaspar Dutra",     "partido": "PSD",          "inicio": 1946, "fim": 1950, "fase": "República Democrática"},
    {"presidente": "Getúlio Vargas",          "partido": "PTB",          "inicio": 1951, "fim": 1954, "fase": "Democrático Eleito"},
    {"presidente": "Café Filho",              "partido": "PSP",          "inicio": 1954, "fim": 1955, "fase": "Transição"},
    {"presidente": "Juscelino Kubitschek",    "partido": "PSD",          "inicio": 1956, "fim": 1960, "fase": "Desenvolvimentismo"},
    {"presidente": "Jânio Quadros",           "partido": "PTN",          "inicio": 1961, "fim": 1961, "fase": "Transição"},
    {"presidente": "João Goulart",            "partido": "PTB",          "inicio": 1961, "fim": 1964, "fase": "Reformas de Base"},
    {"presidente": "Castelo Branco",          "partido": "ARENA",        "inicio": 1964, "fim": 1966, "fase": "Ditadura Militar"},
    {"presidente": "Costa e Silva",           "partido": "ARENA",        "inicio": 1967, "fim": 1969, "fase": "Ditadura Militar"},
    {"presidente": "Emílio Médici",           "partido": "ARENA",        "inicio": 1969, "fim": 1973, "fase": "Milagre Econômico"},
    {"presidente": "Ernesto Geisel",          "partido": "ARENA",        "inicio": 1974, "fim": 1978, "fase": "Ditadura Militar"},
    {"presidente": "João Figueiredo",         "partido": "PDS",          "inicio": 1979, "fim": 1984, "fase": "Abertura"},
    {"presidente": "José Sarney",             "partido": "PMDB",         "inicio": 1985, "fim": 1989, "fase": "Nova República"},
    {"presidente": "Fernando Collor",         "partido": "PRN",          "inicio": 1990, "fim": 1992, "fase": "Nova República"},
    {"presidente": "Itamar Franco",           "partido": "PMDB",         "inicio": 1992, "fim": 1994, "fase": "Nova República"},
    {"presidente": "Fernando H. Cardoso",     "partido": "PSDB",         "inicio": 1995, "fim": 2002, "fase": "Plano Real"},
    {"presidente": "Lula (1º e 2º mandato)",  "partido": "PT",           "inicio": 2003, "fim": 2010, "fase": "Crescimento Social"},
    {"presidente": "Dilma Rousseff",          "partido": "PT",           "inicio": 2011, "fim": 2016, "fase": "Crise/Impeachment"},
    {"presidente": "Michel Temer",            "partido": "MDB",          "inicio": 2016, "fim": 2018, "fase": "Austeridade"},
    {"presidente": "Jair Bolsonaro",          "partido": "PL",           "inicio": 2019, "fim": 2022, "fase": "Nova República"},
    {"presidente": "Lula (3º mandato)",       "partido": "PT",           "inicio": 2023, "fim": 2026, "fase": "Nova República"},
]

def get_presidente_ano(ano: int) -> dict:
    """Retorna o mandato ativo em determinado ano (critério: maioria do ano)."""
    for m in reversed(MANDATOS):
        if m["inicio"] <= ano <= m["fim"]:
            return m
    return {"presidente": "Desconhecido", "partido": "-", "fase": "-"}

# ---------------------------------------------------------------------------
# 2. DADOS HISTÓRICOS CODIFICADOS (1930–1959 e lacunas)
# ---------------------------------------------------------------------------
# Fontes: IBGE/IPEA Estatísticas do Século XX, Ipeadata, Maddison Project

HISTORICO = {
    # crescimento_pib_real_pct — IBGE / Maddison Project
    "crescimento_pib_real_pct": {
        1930:-2.1, 1931:-3.3, 1932: 4.0, 1933: 8.8, 1934: 9.0,
        1935: 3.9, 1936:11.0, 1937: 5.0, 1938: 5.2, 1939: 2.7,
        1940:-2.7, 1941: 5.9, 1942:-1.5, 1943: 6.7, 1944: 7.7,
        1945: 3.6, 1946:11.6, 1947: 2.4, 1948: 9.7, 1949: 7.7,
        1950: 6.8, 1951: 4.9, 1952: 8.7, 1953: 4.7, 1954: 7.8,
        1955: 8.8, 1956: 2.9, 1957: 7.7, 1958:10.8, 1959: 9.8,
        1960: 9.4, 1961: 8.6, 1962: 6.6, 1963: 0.6, 1964: 3.4,
        1965: 2.4, 1966: 6.7, 1967: 4.8, 1968: 9.8, 1969: 9.5,
        1970:10.4, 1971:11.3, 1972:11.9, 1973:14.0, 1974: 8.2,
        1975: 5.2, 1976:10.3, 1977: 4.9, 1978: 5.0, 1979: 6.8,
        1980: 9.2, 1981:-4.4, 1982: 0.8, 1983:-2.9, 1984: 5.4,
        1985: 7.9, 1986: 7.5, 1987: 3.5, 1988:-0.1, 1989: 3.2,
        1990:-4.3, 1991: 1.0, 1992:-0.5, 1993: 4.9, 1994: 5.9,
    },
    # inflacao_pct — estimativas pré-IPCA (FGV/IBGE) + IPCA oficial 1980+
    "inflacao_pct": {
        1930: 8.0,  1931: 0.0,  1932:-4.0,  1933: 4.5,  1934: 8.0,
        1935: 8.0,  1936:16.0,  1937: 5.0,  1938: 2.0,  1939: 9.0,
        1940:16.0,  1941:17.0,  1942:20.0,  1943:22.0,  1944:27.0,
        1945:14.0,  1946:18.0,  1947:10.0,  1948: 8.0,  1949:12.0,
        1950:11.8,  1951:12.3,  1952:12.7,  1953:20.5,  1954:25.9,
        1955:12.2,  1956:24.6,  1957: 7.0,  1958:24.4,  1959:39.4,
        1960:30.5,  1961:47.8,  1962:51.3,  1963:79.9,  1964:91.8,
        1965:65.7,  1966:41.3,  1967:30.4,  1968:22.0,  1969:20.1,
        1970:19.3,  1971:20.4,  1972:15.7,  1973:15.5,  1974:34.5,
        1975:29.4,  1976:46.3,  1977:38.8,  1978:40.8,  1979:77.2,
        1980:110.2, 1981:95.2,  1982:99.7,  1983:211.0, 1984:223.8,
        1985:235.1, 1986:65.0,  1987:415.8, 1988:1037.5,1989:1782.9,
        1990:1476.6,1991:480.2, 1992:1157.4,1993:2708.2,1994:2406.8,
    },
    # taxa_desemprego_pct — estimativas históricas (pré-PNAD)
    "taxa_desemprego_pct": {
        1930:10.0, 1931:11.0, 1932:12.0, 1933:10.0, 1934: 9.0,
        1935: 8.0, 1936: 7.5, 1937: 7.0, 1938: 7.0, 1939: 7.0,
        1940: 7.5, 1941: 7.0, 1942: 7.5, 1943: 6.5, 1944: 5.5,
        1945: 5.0, 1946: 5.5, 1947: 5.5, 1948: 5.0, 1949: 5.0,
        1950: 5.0, 1951: 4.8, 1952: 4.5, 1953: 5.0, 1954: 4.8,
        1955: 4.5, 1956: 5.0, 1957: 4.8, 1958: 4.5, 1959: 4.5,
        1960: 4.5, 1961: 4.3, 1962: 4.5, 1963: 5.5, 1964: 5.5,
        1965: 5.8, 1966: 5.5, 1967: 5.8, 1968: 5.0, 1969: 4.8,
        1970: 4.5, 1971: 4.2, 1972: 4.0, 1973: 3.5, 1974: 3.8,
        1975: 4.0, 1976: 3.8, 1977: 4.0, 1978: 4.2, 1979: 4.5,
        1980: 4.5, 1981: 6.5, 1982: 6.8, 1983: 8.0, 1984: 7.5,
        1985: 6.5, 1986: 5.5, 1987: 5.8, 1988: 6.0, 1989: 6.0,
        1990: 7.5, 1991: 7.8, 1992: 8.5, 1993: 7.8, 1994: 7.0,
    },
    # esperanca_vida_anos — IBGE/OMS
    "esperanca_vida_anos": {
        1930:36.7, 1935:37.8, 1940:39.0, 1945:42.0, 1950:45.5,
        1955:49.0, 1960:53.5, 1965:57.0, 1970:59.8, 1975:61.7,
        1980:63.5, 1985:65.5, 1990:67.0, 1995:69.0,
    },
    # mortalidade_infantil — IBGE (por mil nascidos vivos)
    "mortalidade_infantil_por_mil": {
        1930:162, 1935:155, 1940:148, 1945:135, 1950:125,
        1955:115, 1960:105, 1965: 95, 1970: 88, 1975: 80,
        1980: 70, 1985: 58, 1990: 47, 1995: 37,
    },
    # populacao_milhoes — IBGE
    "populacao_milhoes": {
        1930:33.6, 1931:34.3, 1932:35.1, 1933:35.9, 1934:36.8,
        1935:37.6, 1936:38.5, 1937:39.4, 1938:40.3, 1939:41.2,
        1940:41.2, 1941:42.3, 1942:43.3, 1943:44.3, 1944:45.3,
        1945:46.3, 1946:47.4, 1947:48.5, 1948:49.7, 1949:50.9,
        1950:51.9, 1951:53.3, 1952:54.8, 1953:56.3, 1954:57.8,
        1955:59.4, 1956:61.0, 1957:62.7, 1958:64.4, 1959:66.2,
        1960:70.1, 1961:72.3, 1962:74.5, 1963:76.8, 1964:79.2,
        1965:81.6, 1966:84.0, 1967:86.6, 1968:89.2, 1969:91.9,
        1970:95.8, 1971:98.6, 1972:101.4,1973:104.2,1974:107.1,
        1975:109.7,1976:112.4,1977:115.3,1978:118.3,1979:121.3,
        1980:121.6,1981:124.1,1982:126.9,1983:129.7,1984:132.6,
        1985:135.6,1986:138.7,1987:141.8,1988:144.4,1989:147.3,
        1990:150.4,1991:151.0,1992:154.1,1993:157.1,1994:160.3,
    },
    # taxa_urbanizacao_pct — IBGE
    "taxa_urbanizacao_pct": {
        1930:25.0, 1935:27.0, 1940:31.2, 1945:34.0, 1950:36.2,
        1955:40.0, 1960:44.9, 1965:49.0, 1970:55.9, 1975:60.0,
        1980:67.6, 1985:72.0, 1990:74.7, 1995:78.0,
    },
    # salario_minimo_real_brl — DIEESE/IBGE (valores em BRL 2024)
    "salario_minimo_real_brl": {
        1940:1420, 1941:1400, 1942:1380, 1943:1350, 1944:1310,
        1945:1280, 1946:1320, 1947:1350, 1948:1370, 1949:1340,
        1950:1300, 1951:1250, 1952:1220, 1953:1180, 1954:1540,
        1955:1500, 1956:1440, 1957:1820, 1958:1780, 1959:1650,
        1960:1900, 1961:1950, 1962:1800, 1963:1600, 1964:1450,
        1965:1500, 1966:1480, 1967:1520, 1968:1400, 1969:1350,
        1970:1310, 1971:1280, 1972:1260, 1973:1320, 1974:1350,
        1975:1380, 1976:1420, 1977:1380, 1978:1400, 1979:1380,
        1980:1420, 1981:1350, 1982:1300, 1983:1100, 1984:1050,
        1985:1150, 1986:1480, 1987:1350, 1988:1200, 1989:1180,
        1990:1050, 1991:1020, 1992: 980, 1993: 970, 1994:1050,
        1995:1150, 1996:1120, 1997:1100, 1998:1120, 1999:1080,
        2000:1100, 2001:1090, 2002:1080, 2003:1060, 2004:1070,
        2005:1140, 2006:1220, 2007:1290, 2008:1360, 2009:1420,
        2010:1510, 2011:1560, 2012:1640, 2013:1680, 2014:1700,
        2015:1650, 2016:1630, 2017:1640, 2018:1650, 2019:1660,
        2020:1680, 2021:1630, 2022:1650, 2023:1700, 2024:1760,
    },
}

# ---------------------------------------------------------------------------
# 3. BUSCA VIA BANCO MUNDIAL (wbgapi)
# ---------------------------------------------------------------------------
WB_INDICATORS = {
    "pib_nominal_bi_usd":          "NY.GDP.MKTP.CD",
    "pib_per_capita_usd":          "NY.GDP.PCAP.CD",
    "crescimento_pib_real_pct":    "NY.GDP.MKTP.KD.ZG",
    "inflacao_pct":                "FP.CPI.TOTL.ZG",
    "taxa_desemprego_pct":         "SL.UEM.TOTL.ZS",
    "esperanca_vida_anos":         "SP.DYN.LE00.IN",
    "mortalidade_infantil_por_mil":"SP.DYN.IMRT.IN",
    "populacao_milhoes":           "SP.POP.TOTL",
    "taxa_urbanizacao_pct":        "SP.URB.TOTL.IN.ZS",
    "coeficiente_gini":            "SI.POV.GINI",
    "reservas_internacionais_bi_usd":"FI.RES.TOTL.CD",
    "exportacoes_bi_usd":          "NE.EXP.GNFS.CD",
    "importacoes_bi_usd":          "NE.IMP.GNFS.CD",
    "ied_entrada_bi_usd":          "BX.KLT.DINV.CD.WD",
    "gasto_educacao_pib_pct":      "SE.XPD.TOTL.GD.ZS",
    "fbcf_pib_pct":                "NE.GDI.FTOT.ZS",
}

def fetch_world_bank():
    """Busca indicadores do Banco Mundial para o Brasil (1960-2024)."""
    print("  Buscando dados do Banco Mundial...")
    results = {}
    base_url = "https://api.worldbank.org/v2/country/BR/indicator/{indicator}?format=json&per_page=100&mrv=65"

    for col_name, indicator_code in WB_INDICATORS.items():
        try:
            url = base_url.format(indicator=indicator_code)
            resp = requests.get(url, timeout=20)
            if resp.status_code != 200:
                print(f"    [AVISO] {col_name}: status {resp.status_code}")
                continue
            data = resp.json()
            if len(data) < 2 or not data[1]:
                continue
            for entry in data[1]:
                year = int(entry["date"])
                value = entry["value"]
                if value is not None:
                    results.setdefault(year, {})[col_name] = value
        except Exception as e:
            print(f"    [ERRO] {col_name}: {e}")

    # Ajustes de escala
    for year_data in results.values():
        if "pib_nominal_bi_usd" in year_data:
            year_data["pib_nominal_bi_usd"] /= 1e9
        if "reservas_internacionais_bi_usd" in year_data:
            year_data["reservas_internacionais_bi_usd"] /= 1e9
        if "exportacoes_bi_usd" in year_data:
            year_data["exportacoes_bi_usd"] /= 1e9
        if "importacoes_bi_usd" in year_data:
            year_data["importacoes_bi_usd"] /= 1e9
        if "ied_entrada_bi_usd" in year_data:
            year_data["ied_entrada_bi_usd"] /= 1e9
        if "populacao_milhoes" in year_data:
            year_data["populacao_milhoes"] /= 1e6
        # Gini do WB vem em escala 0-100; normalizar para 0-1
        if "coeficiente_gini" in year_data:
            v = year_data["coeficiente_gini"]
            if v > 1:
                year_data["coeficiente_gini"] = v / 100

    print(f"    OK — {len(results)} anos com dados do Banco Mundial")
    return results

# ---------------------------------------------------------------------------
# 4. BUSCA VIA IPEADATA (BCB/IBGE)
# ---------------------------------------------------------------------------
IPEA_SERIES = {
    "selic_pct":                   "BM_TBANUAL",   # Taxa SELIC anual
    "cambio_brl_usd":              "GM366_ERV366",  # Câmbio BRL/USD (fim período)
    "divida_bruta_pib_pct":        "FINGEN_DBGG",   # Dívida bruta/PIB
    "resultado_primario_pib_pct":  "FINGEN_SPGG",   # Superávit primário/PIB
    "balanca_comercial_bi_usd":    "BM366_BCOME366",# Balança comercial
}

def fetch_ipeadata():
    """Busca séries anuais do IPEAData."""
    print("  Buscando dados do IPEAData...")
    results = {}
    base_url = "http://www.ipeadata.gov.br/api/odata4/ValoresSerie(SERCODIGO='{code}')"

    for col_name, series_code in IPEA_SERIES.items():
        try:
            url = base_url.format(code=series_code)
            resp = requests.get(url, timeout=30)
            if resp.status_code != 200:
                print(f"    [AVISO] {col_name}: status {resp.status_code}")
                continue
            data = resp.json().get("value", [])
            for entry in data:
                try:
                    year = int(str(entry.get("VALDATA", ""))[:4])
                    value = entry.get("VALVALOR")
                    if value is not None and 1929 < year < 2026:
                        results.setdefault(year, {})[col_name] = float(value)
                except Exception:
                    continue
        except Exception as e:
            print(f"    [ERRO] {col_name}: {e}")

    # Balanço comercial: converter para bilhões
    for year_data in results.values():
        if "balanca_comercial_bi_usd" in year_data:
            v = year_data["balanca_comercial_bi_usd"]
            if abs(v) > 1000:
                year_data["balanca_comercial_bi_usd"] = v / 1e6

    print(f"    OK — {len(results)} anos com dados do IPEAData")
    return results

# ---------------------------------------------------------------------------
# 5. DADOS COMPLEMENTARES CONHECIDOS (IPCA oficial, Gini, IDH)
# ---------------------------------------------------------------------------
COMPLEMENTAR = {
    # IPCA oficial 1995-2024 (IBGE)
    "inflacao_pct": {
        1995:22.41, 1996: 9.56, 1997: 5.22, 1998: 1.65, 1999: 8.94,
        2000: 5.97, 2001: 7.67, 2002:12.53, 2003: 9.30, 2004: 7.60,
        2005: 5.69, 2006: 3.14, 2007: 4.46, 2008: 5.90, 2009: 4.31,
        2010: 5.91, 2011: 6.50, 2012: 5.84, 2013: 5.91, 2014: 6.41,
        2015:10.67, 2016: 6.29, 2017: 2.95, 2018: 3.75, 2019: 4.31,
        2020: 4.52, 2021:10.06, 2022: 5.79, 2023: 4.62, 2024: 4.83,
    },
    # Coeficiente de Gini — IBGE/PNAD
    "coeficiente_gini": {
        1960:0.500, 1970:0.568, 1976:0.623, 1977:0.612, 1978:0.601,
        1979:0.590, 1980:0.591, 1981:0.578, 1982:0.591, 1983:0.596,
        1984:0.589, 1985:0.598, 1986:0.588, 1987:0.601, 1988:0.616,
        1989:0.636, 1990:0.614, 1992:0.583, 1993:0.604, 1995:0.601,
        1996:0.602, 1997:0.602, 1998:0.600, 1999:0.594, 2001:0.596,
        2002:0.589, 2003:0.583, 2004:0.572, 2005:0.566, 2006:0.560,
        2007:0.556, 2008:0.546, 2009:0.543, 2011:0.531, 2012:0.526,
        2013:0.527, 2014:0.518, 2015:0.524, 2016:0.535, 2017:0.549,
        2018:0.545, 2019:0.543, 2020:0.524, 2021:0.544, 2022:0.518,
        2023:0.520,
    },
    # IDH — PNUD (valores interpolados entre relatórios)
    "idh": {
        1930:0.189, 1935:0.202, 1940:0.217, 1945:0.232, 1950:0.254,
        1955:0.278, 1960:0.305, 1965:0.335, 1970:0.368, 1975:0.400,
        1980:0.446, 1985:0.487, 1990:0.523, 1995:0.560,
        2000:0.612, 2001:0.619, 2002:0.624, 2003:0.630, 2004:0.638,
        2005:0.645, 2006:0.652, 2007:0.659, 2008:0.666, 2009:0.671,
        2010:0.699, 2011:0.705, 2012:0.712, 2013:0.715, 2014:0.754,
        2015:0.754, 2016:0.757, 2017:0.759, 2018:0.761, 2019:0.765,
        2020:0.754, 2021:0.754, 2022:0.760, 2023:0.764,
    },
    # Taxa de pobreza extrema % (< US$ 2,15/dia PPC) — Banco Mundial / IPEA
    "taxa_pobreza_extrema_pct": {
        1977:32.2, 1978:30.1, 1979:28.5, 1981:27.0, 1982:26.0,
        1983:30.0, 1984:28.0, 1985:25.0, 1986:18.0, 1987:24.0,
        1988:28.0, 1989:26.0, 1990:29.0, 1992:28.0, 1993:27.0,
        1995:18.0, 1996:17.0, 1997:16.0, 1998:15.5, 1999:16.0,
        2001:15.3, 2002:14.5, 2003:14.0, 2004:12.5, 2005:11.5,
        2006:10.0, 2007: 8.8, 2008: 7.8, 2009: 7.3, 2011: 6.1,
        2012: 5.3, 2013: 4.9, 2014: 4.3, 2015: 4.7, 2016: 5.0,
        2017: 5.4, 2018: 5.0, 2019: 4.5, 2020: 4.2, 2021: 4.6,
        2022: 3.7, 2023: 3.5,
    },
    # Crescimento PIB real (%) — valores não cobertos pelo Banco Mundial
    "crescimento_pib_real_pct": {
        1995: 4.22, 1996: 2.15, 1997: 3.38, 1998: 0.04, 1999: 0.47,
        2000: 4.39, 2001: 1.39, 2002: 3.05, 2003: 1.14, 2004: 5.76,
        2005: 3.20, 2006: 3.96, 2007: 6.07, 2008: 5.09, 2009:-0.13,
        2010: 7.53, 2011: 4.00, 2012: 1.93, 2013: 3.00, 2014: 0.50,
        2015:-3.55, 2016:-3.31, 2017: 1.32, 2018: 1.78, 2019: 1.41,
        2020:-3.88, 2021: 4.62, 2022: 2.90, 2023: 2.90, 2024: 3.40,
    },
    # Câmbio BRL/USD médio anual (BCB)
    "cambio_brl_usd": {
        1995:0.917, 1996:1.005, 1997:1.078, 1998:1.161, 1999:1.815,
        2000:1.830, 2001:2.352, 2002:2.921, 2003:3.071, 2004:2.926,
        2005:2.434, 2006:2.175, 2007:1.948, 2008:1.834, 2009:2.000,
        2010:1.759, 2011:1.675, 2012:1.955, 2013:2.157, 2014:2.354,
        2015:3.331, 2016:3.484, 2017:3.193, 2018:3.654, 2019:3.945,
        2020:5.397, 2021:5.396, 2022:5.165, 2023:4.994, 2024:5.130,
    },
    # Reservas internacionais (bilhões USD) — BCB
    "reservas_internacionais_bi_usd": {
        1970: 1.2, 1975: 4.0, 1980: 7.0, 1985: 7.5, 1990: 9.9,
        1991:10.1, 1992:24.0, 1993:32.2, 1994:38.8, 1995:51.8,
        1996:60.1, 1997:52.2, 1998:44.6, 1999:36.3, 2000:33.0,
        2001:35.9, 2002:37.8, 2003:49.3, 2004:52.9, 2005:53.8,
        2006:85.8, 2007:180.3,2008:193.8,2009:238.5,2010:288.6,
        2011:352.0,2012:373.1,2013:358.8,2014:363.6,2015:356.5,
        2016:365.0,2017:374.0,2018:374.7,2019:356.9,2020:355.6,
        2021:362.2,2022:324.7,2023:339.9,2024:360.0,
    },
    # Exportações bilhões USD (MDIC/Secex)
    "exportacoes_bi_usd": {
        1930: 0.4, 1940: 0.3, 1950: 1.4, 1960: 1.3, 1970: 2.7,
        1975: 8.7, 1980:20.1, 1985:25.6, 1990:31.4, 1995:46.5,
        1996:47.7, 1997:53.0, 1998:51.1, 1999:48.0, 2000:55.1,
        2001:58.3, 2002:60.4, 2003:73.1, 2004:96.7, 2005:118.5,
        2006:137.8,2007:160.6,2008:197.9,2009:153.0,2010:201.9,
        2011:256.0,2012:242.6,2013:242.2,2014:225.1,2015:191.1,
        2016:185.2,2017:217.7,2018:239.0,2019:225.4,2020:209.7,
        2021:280.8,2022:334.1,2023:339.7,2024:370.0,
    },
    # Importações bilhões USD (MDIC/Secex)
    "importacoes_bi_usd": {
        1930: 0.3, 1940: 0.3, 1950: 1.1, 1960: 1.5, 1970: 2.8,
        1975:13.6, 1980:23.0, 1985:14.3, 1990:22.5, 1995:49.9,
        1996:53.3, 1997:59.7, 1998:57.7, 1999:49.3, 2000:55.8,
        2001:55.6, 2002:47.2, 2003:48.3, 2004:62.8, 2005:73.6,
        2006:91.4, 2007:120.6,2008:172.9,2009:127.7,2010:181.8,
        2011:226.2,2012:223.1,2013:239.6,2014:229.1,2015:171.4,
        2016:137.6,2017:150.7,2018:181.2,2019:177.3,2020:158.6,
        2021:219.4,2022:272.7,2023:253.3,2024:270.0,
    },
    # Taxa SELIC (% ao ano) — BCB
    "selic_pct": {
        1986:68.0, 1987:363.0,1988:1057.0,1989:2670.0,1990:1082.0,
        1991:440.0,1992:1157.0,1993:3060.0,1994:1094.0,
        1995:53.1, 1996:27.4, 1997:24.8, 1998:29.2, 1999:25.6,
        2000:17.4, 2001:17.3, 2002:19.2, 2003:23.4, 2004:16.2,
        2005:19.0, 2006:15.1, 2007:11.9, 2008:13.7, 2009: 9.9,
        2010:10.7, 2011:11.6, 2012: 7.2, 2013: 9.9, 2014:11.6,
        2015:14.2, 2016:13.8, 2017: 7.0, 2018: 6.5, 2019: 5.9,
        2020: 2.0, 2021: 9.2, 2022:13.8, 2023:11.8, 2024:11.2,
    },
    # Dívida bruta/PIB % — STN/BCB
    "divida_bruta_pib_pct": {
        1991:38.0, 1992:43.0, 1993:42.0, 1994:31.0, 1995:33.0,
        1996:34.0, 1997:35.0, 1998:42.0, 1999:49.0, 2000:50.0,
        2001:54.0, 2002:60.0, 2003:57.0, 2004:52.0, 2005:53.0,
        2006:57.0, 2007:65.0, 2008:64.0, 2009:67.0, 2010:65.0,
        2011:62.0, 2012:63.0, 2013:60.0, 2014:63.0, 2015:66.5,
        2016:70.0, 2017:74.0, 2018:77.2, 2019:75.8, 2020:88.8,
        2021:80.3, 2022:73.5, 2023:74.3, 2024:78.0,
    },
    # Resultado primário (% PIB, + = superávit) — STN
    "resultado_primario_pib_pct": {
        1991:-0.3, 1992: 1.6, 1993: 2.1, 1994: 5.1, 1995: 0.3,
        1996: 0.0, 1997:-1.0, 1998:-0.0, 1999: 3.2, 2000: 3.5,
        2001: 3.6, 2002: 3.5, 2003: 3.9, 2004: 4.2, 2005: 4.4,
        2006: 3.9, 2007: 3.9, 2008: 4.1, 2009: 2.0, 2010: 2.7,
        2011: 3.1, 2012: 2.4, 2013: 1.9, 2014:-0.6, 2015:-1.9,
        2016:-2.5, 2017:-1.7, 2018:-1.6, 2019:-0.8, 2020:-9.4,
        2021: 0.7, 2022: 1.3, 2023:-2.1, 2024:-0.6,
    },
    # Balança comercial (bilhões USD) — MDIC
    "balanca_comercial_bi_usd": {
        1930: 0.1, 1940: 0.0, 1950: 0.3, 1960:-0.2, 1970:-0.1,
        1975:-4.9, 1980:-2.9, 1985:11.3, 1990: 8.9, 1995:-3.4,
        1996:-5.6, 1997:-8.7, 1998:-6.6, 1999:-1.3, 2000:-0.7,
        2001: 2.7, 2002:13.2, 2003:24.8, 2004:33.9, 2005:44.9,
        2006:46.5, 2007:40.0, 2008:24.9, 2009:25.3, 2010:20.1,
        2011:29.8, 2012:19.5, 2013: 2.6, 2014:-4.0, 2015:19.7,
        2016:47.7, 2017:67.0, 2018:58.3, 2019:49.2, 2020:51.1,
        2021:61.4, 2022:62.3, 2023:98.8, 2024:74.6,
    },
    # IED entrada (bilhões USD) — BCB
    "ied_entrada_bi_usd": {
        1970: 0.1, 1975: 1.1, 1980: 1.5, 1985: 1.4, 1990: 0.9,
        1995: 4.4, 1996:10.8, 1997:19.7, 1998:28.9, 1999:28.6,
        2000:32.8, 2001:22.5, 2002:16.6, 2003:10.1, 2004:18.2,
        2005:15.1, 2006:18.8, 2007:34.6, 2008:45.1, 2009:25.9,
        2010:48.5, 2011:66.7, 2012:65.3, 2013:64.0, 2014:62.5,
        2015:64.7, 2016:78.9, 2017:70.7, 2018:88.3, 2019:69.2,
        2020:37.8, 2021:46.4, 2022:91.5, 2023:65.9, 2024:80.0,
    },
    # FBCF/PIB % — IBGE
    "fbcf_pib_pct": {
        1947:12.0, 1950:13.5, 1955:14.2, 1960:16.8, 1965:16.0,
        1970:18.8, 1975:23.6, 1980:23.5, 1985:17.9, 1990:20.7,
        1995:20.5, 1996:19.3, 1997:19.9, 1998:19.7, 1999:17.5,
        2000:18.3, 2001:17.7, 2002:16.6, 2003:15.3, 2004:16.1,
        2005:15.9, 2006:16.4, 2007:17.4, 2008:19.1, 2009:18.1,
        2010:20.5, 2011:20.6, 2012:20.7, 2013:21.0, 2014:20.2,
        2015:18.2, 2016:15.4, 2017:15.6, 2018:16.0, 2019:15.6,
        2020:16.4, 2021:18.7, 2022:18.9, 2023:17.0, 2024:16.8,
    },
    # PIB per capita USD — Banco Mundial / IBGE
    "pib_per_capita_usd": {
        1930:  90, 1935: 100, 1940: 105, 1945: 115, 1950: 130,
        1955: 180, 1960: 210, 1965: 270, 1970: 430, 1975: 960,
        1980:1960, 1985:1610, 1990:2900, 1995:4800,
    },
}

# ---------------------------------------------------------------------------
# 6. MONTAGEM DO DATASET
# ---------------------------------------------------------------------------
COLUNAS = [
    "ano", "presidente", "partido", "fase",
    "crescimento_pib_real_pct",
    "pib_nominal_bi_usd",
    "pib_per_capita_usd",
    "inflacao_pct",
    "taxa_desemprego_pct",
    "salario_minimo_real_brl",
    "selic_pct",
    "cambio_brl_usd",
    "divida_bruta_pib_pct",
    "resultado_primario_pib_pct",
    "reservas_internacionais_bi_usd",
    "exportacoes_bi_usd",
    "importacoes_bi_usd",
    "balanca_comercial_bi_usd",
    "ied_entrada_bi_usd",
    "fbcf_pib_pct",
    "coeficiente_gini",
    "idh",
    "taxa_pobreza_extrema_pct",
    "esperanca_vida_anos",
    "mortalidade_infantil_por_mil",
    "populacao_milhoes",
    "taxa_urbanizacao_pct",
]

def build_dataset():
    print("Construindo base de dados...")

    # 1. Dados históricos codificados
    data = {}
    for col, serie in HISTORICO.items():
        for year, value in serie.items():
            data.setdefault(year, {})[col] = value

    # 2. Dados complementares
    for col, serie in COMPLEMENTAR.items():
        for year, value in serie.items():
            row = data.setdefault(year, {})
            if col not in row:  # não sobrescreve
                row[col] = value

    # 3. Dados do Banco Mundial (prioridade sobre histórico para 1960+)
    wb_data = fetch_world_bank()
    for year, values in wb_data.items():
        row = data.setdefault(year, {})
        for col, value in values.items():
            row[col] = value  # WB tem prioridade para séries comuns

    # 4. Dados do IPEAData
    ipea_data = fetch_ipeadata()
    for year, values in ipea_data.items():
        row = data.setdefault(year, {})
        for col, value in values.items():
            if col not in row:
                row[col] = value

    # 5. Interpolação linear para anos sem dados em séries de longa frequência
    df_full = pd.DataFrame(index=range(1930, 2025))
    for year, values in data.items():
        for col, val in values.items():
            df_full.loc[year, col] = val

    interpolate_cols = [
        "esperanca_vida_anos", "mortalidade_infantil_por_mil",
        "populacao_milhoes", "taxa_urbanizacao_pct",
        "coeficiente_gini", "idh", "pib_per_capita_usd",
        "salario_minimo_real_brl",
    ]
    for col in interpolate_cols:
        if col in df_full.columns:
            df_full[col] = df_full[col].interpolate(method="linear", limit_direction="both")

    # 6. Montar linhas finais
    rows = []
    for year in range(1930, 2025):
        mandato = get_presidente_ano(year)
        row = {
            "ano": year,
            "presidente": mandato["presidente"],
            "partido": mandato["partido"],
            "fase": mandato["fase"],
        }
        for col in COLUNAS[4:]:
            val = df_full.loc[year, col] if col in df_full.columns else None
            if pd.isna(val) if val is not None else False:
                val = None
            row[col] = round(float(val), 4) if val is not None and not pd.isna(val) else None
        rows.append(row)

    return rows

# ---------------------------------------------------------------------------
# 7. EXPORTAÇÃO: SQLITE + CSV
# ---------------------------------------------------------------------------
def save_sqlite(rows):
    db_path = OUTPUT_DIR / "brasil_economico.db"
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    cols_def = ", ".join(
        f'"{c}" TEXT' if c in ("presidente","partido","fase") else f'"{c}" REAL'
        for c in COLUNAS
    )
    cols_def = '"ano" INTEGER, ' + cols_def[len('"ano" REAL, '):]

    cur.execute(f"DROP TABLE IF EXISTS indicadores_brasil")
    cur.execute(f"CREATE TABLE indicadores_brasil ({cols_def})")

    placeholders = ", ".join(["?"] * len(COLUNAS))
    for row in rows:
        values = [row.get(c) for c in COLUNAS]
        cur.execute(f"INSERT INTO indicadores_brasil VALUES ({placeholders})", values)

    # View resumo por mandato
    cur.execute("DROP VIEW IF EXISTS resumo_por_mandato")
    cur.execute("""
    CREATE VIEW resumo_por_mandato AS
    SELECT
        presidente, partido, fase,
        MIN(ano) AS ano_inicio,
        MAX(ano) AS ano_fim,
        ROUND(AVG(crescimento_pib_real_pct), 2) AS media_crescimento_pib_pct,
        ROUND(AVG(inflacao_pct), 2) AS media_inflacao_pct,
        ROUND(AVG(taxa_desemprego_pct), 2) AS media_desemprego_pct,
        ROUND(AVG(selic_pct), 2) AS media_selic_pct,
        ROUND(AVG(cambio_brl_usd), 4) AS media_cambio_brl_usd,
        ROUND(AVG(divida_bruta_pib_pct), 2) AS media_divida_pib_pct,
        ROUND(AVG(reservas_internacionais_bi_usd), 2) AS media_reservas_bi_usd,
        ROUND(AVG(balanca_comercial_bi_usd), 2) AS media_balanca_comercial_bi_usd,
        ROUND(AVG(coeficiente_gini), 4) AS media_gini,
        ROUND(AVG(idh), 4) AS media_idh,
        ROUND(AVG(esperanca_vida_anos), 2) AS media_esperanca_vida,
        ROUND(AVG(mortalidade_infantil_por_mil), 2) AS media_mort_infantil
    FROM indicadores_brasil
    GROUP BY presidente, partido, fase
    ORDER BY MIN(ano)
    """)

    conn.commit()
    conn.close()
    print(f"  SQLite salvo: {db_path}")

def save_csv(rows):
    # CSV anual
    csv_anual = OUTPUT_DIR / "brasil_indicadores_anuais.csv"
    with open(csv_anual, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=COLUNAS)
        writer.writeheader()
        writer.writerows(rows)
    print(f"  CSV anual salvo: {csv_anual}")

    # CSV resumo por mandato
    db_path = OUTPUT_DIR / "brasil_economico.db"
    conn = sqlite3.connect(db_path)
    df = pd.read_sql("SELECT * FROM resumo_por_mandato", conn)
    conn.close()
    csv_mandato = OUTPUT_DIR / "brasil_resumo_por_mandato.csv"
    df.to_csv(csv_mandato, index=False, encoding="utf-8")
    print(f"  CSV mandatos salvo: {csv_mandato}")

def print_preview(rows):
    print("\n=== PRÉVIA — últimos 5 anos ===")
    header = ["ano","presidente","crescimento_pib_real_pct","inflacao_pct","selic_pct","cambio_brl_usd","divida_bruta_pib_pct"]
    print(" | ".join(f"{h:<30}" if h=="presidente" else f"{h:<28}" for h in header))
    print("-" * 180)
    for row in rows[-5:]:
        vals = [str(row.get(h, "")) for h in header]
        print(" | ".join(f"{v:<30}" if i==1 else f"{v:<28}" for i, v in enumerate(vals)))

# ---------------------------------------------------------------------------
# 8. MAIN
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    print("=" * 60)
    print("  BANCO DE DADOS ECONÔMICO DO BRASIL (1930-2024)")
    print("  20 Indicadores | Mandatos Presidenciais")
    print("=" * 60)

    rows = build_dataset()
    print(f"\n  Total de linhas geradas: {len(rows)}")

    print("\nSalvando arquivos...")
    save_sqlite(rows)
    save_csv(rows)
    print_preview(rows)

    print("\n✓ Concluído! Arquivos gerados em:", OUTPUT_DIR)

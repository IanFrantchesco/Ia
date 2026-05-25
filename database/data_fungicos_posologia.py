"""
Dados de posologia de antifúngicos por população e patologia.
Fontes: PCDT-PARACOC MS 2022, SBD-MICOSES, SBMT-FUNGOS, SBI-CAND, SBI-ASPERG,
        SBI-CRIPTO, ANVISA-ANTIF, PCDT-HIV-FUNG, SVS-HISTOP, SVS-ESPORO, SVS-CRIPTO.

Formato: (antifungico_nome, patologia_substr_ou_None, populacao,
          dose_unitaria, frequencia, via,
          duracao_min_dias, duracao_max_dias, duracao_texto,
          ajuste_renal, ajuste_hepatico, observacoes, fonte_sigla)

Populações: 'adulto','pediatrico','gestante','idoso','insuf_renal','insuf_hepatica','neonato'
"""

POSOLOGIA_FUNGICA = [

    # ══════════════════════════════════════════════════════════════════
    # ITRACONAZOL
    # ══════════════════════════════════════════════════════════════════
    ("Itraconazol", "Paracoccidioidomicose",
     "adulto", "200 mg", "24/24h", "oral", 365, 548, "12–18 meses",
     False, True,
     "1ª linha para paracoccidioidomicose em todas as formas (leve, moderada e grave após indução). "
     "Tomar com alimento ácido (suco de laranja) para maximizar absorção da cápsula. "
     "Monitorar transaminases a cada 3 meses. Disponível no SUS (RENAME).",
     "PCDT-PARACOC"),

    ("Itraconazol", "Paracoccidioidomicose",
     "pediatrico", "5–10 mg/kg/dia (máx 400 mg/dia)", "24/24h", "oral", 365, 548, "12–18 meses",
     False, True,
     "Solução oral (10 mg/mL) preferida em < 12 anos por melhor biodisponibilidade. "
     "Monitorar função hepática. Ajustar dose conforme peso.",
     "PCDT-PARACOC"),

    ("Itraconazol", "Paracoccidioidomicose",
     "gestante", "200 mg", "24/24h", "oral", None, None, "evitar — usar Anfotericina B ou SMX-TMP",
     False, True,
     "CONTRAINDICADO no 1º trimestre (teratogênico — Categoria D). "
     "Usar Anfotericina B desoxicolato em gestantes com formas graves; "
     "SMX-TMP pode ser opção em formas leves após 1º trimestre.",
     "PCDT-PARACOC"),

    ("Itraconazol", "Paracoccidioidomicose",
     "idoso", "200 mg", "24/24h", "oral", 365, 548, "12–18 meses",
     False, True,
     "Monitorar função hepática e interações medicamentosas (polifarmácia). "
     "Risco de insuficiência cardíaca em doses altas — evitar dose > 200 mg/dia em cardiopatas.",
     "PCDT-PARACOC"),

    ("Itraconazol", "Paracoccidioidomicose",
     "insuf_renal", "200 mg", "24/24h", "oral", 365, 548, "12–18 meses",
     False, True,
     "Não requer ajuste de dose renal — eliminação predominantemente hepática. "
     "Em diálise: sem ajuste adicional necessário.",
     "PCDT-PARACOC"),

    ("Itraconazol", "Paracoccidioidomicose",
     "insuf_hepatica", "Usar com cautela extrema", "24/24h", "oral", None, None, "individualizar",
     False, True,
     "Hepatotóxico — contraindicado em insuficiência hepática grave (Child-Pugh C). "
     "Em Child-Pugh A/B: monitorar TGO/TGP semanalmente nas primeiras 4 semanas.",
     "PCDT-PARACOC"),

    ("Itraconazol", "Histoplasmose",
     "adulto", "200 mg", "12/12h (indução) / 200 mg 24/24h (manutenção)", "oral",
     84, 365, "Indução 12 semanas; manutenção total 12 meses em imunossuprimidos",
     False, True,
     "1ª linha para histoplasmose moderada-grave e manutenção pós-anfotericina. "
     "Monitorar níveis séricos (meta: > 1,0 µg/mL) se disponível. "
     "IDSA 2020: 200 mg 3×/dia × 3 dias (ataque), depois 200 mg 2×/dia.",
     "SVS-HISTOP"),

    ("Itraconazol", "Histoplasmose",
     "pediatrico", "5–10 mg/kg/dia (máx 400 mg/dia)", "12/12h", "oral", 84, 365,
     "12 semanas indução; manutenção em imunossuprimidos",
     False, True,
     "Solução oral preferida. Monitorar função hepática. "
     "Em HIV/AIDS pediátrico: manutenção por pelo menos 12 meses ou até reconstituição imune.",
     "SVS-HISTOP"),

    ("Itraconazol", "Histoplasmose",
     "insuf_renal", "200 mg", "12/12h ou 24/24h", "oral", 84, 365, "conforme evolução",
     False, True,
     "Sem ajuste de dose renal. Evitar formulação IV (veículo ciclodextrina acumula em ClCr < 30).",
     "SVS-HISTOP"),

    ("Itraconazol", "Esporotricose",
     "adulto", "100–200 mg", "24/24h", "oral", 90, 180, "3–6 meses (cutânea); até 12 meses (sistêmica)",
     False, True,
     "1ª linha para esporotricose cutânea e linfocutânea. "
     "Para formas sistêmicas: 200 mg/dia após indução com anfotericina B. "
     "Endemia de Sporothrix brasiliensis no Rio de Janeiro: mesma sensibilidade ao itraconazol.",
     "SVS-ESPORO"),

    ("Itraconazol", "Esporotricose",
     "gestante", "Contraindicado", "—", "oral", None, None, "contraindicado",
     False, True,
     "CONTRAINDICADO na gestação (teratogênico). Usar Anfotericina B desoxicolato nas formas graves. "
     "Em formas leves cutâneas: calor local (termoterapia) como medida adjuvante até o pós-parto.",
     "SVS-ESPORO"),

    ("Itraconazol", "Esporotricose",
     "pediatrico", "5–10 mg/kg/dia (máx 400 mg)", "24/24h", "oral", 90, 180, "3–6 meses",
     False, True,
     "Solução oral (10 mg/mL) preferida. Monitorar função hepática mensalmente.",
     "SVS-ESPORO"),

    ("Itraconazol", "Cromoblastomicose",
     "adulto", "200 mg", "12/12h", "oral", 365, 730, "12–24 meses",
     False, True,
     "Associar com 5-fluorocitosina (5-FC) 150 mg/kg/dia nas formas extensas se disponível. "
     "Monoterapia por tempo prolongado; taxa de cura ~15–30% nas formas graves.",
     "SBD-MICOSES"),

    ("Itraconazol", "Dermatofitose",
     "adulto", "200 mg", "12/12h (Tinea unguium: pulso) / 100 mg 24/24h (Tinea corporis)", "oral",
     7, 90, "Tinea corporis: 15 dias; Tinea unguium: 3–4 pulsos mensais",
     False, True,
     "Tinea unguium (onicomicose): pulso 200 mg 2×/dia × 7 dias/mês × 3–4 meses (pé) ou 2 meses (mão). "
     "Tinea capitis: 5 mg/kg/dia × 4–6 semanas.",
     "SBD-MICOSES"),

    # ══════════════════════════════════════════════════════════════════
    # FLUCONAZOL
    # ══════════════════════════════════════════════════════════════════
    ("Fluconazol", "Candidíase orofaríngea",
     "adulto", "100–200 mg", "24/24h", "oral", 7, 14, "7–14 dias",
     True, True,
     "1ª linha para candidíase orofaríngea não complicada. "
     "Em HIV/AIDS: 200 mg/dia; manutenção 100–200 mg/dia em imunossuprimidos graves. "
     "Disponível no SUS.",
     "SBI-CAND"),

    ("Fluconazol", "Candidíase orofaríngea",
     "pediatrico", "3–6 mg/kg/dia (máx 400 mg)", "24/24h", "oral", 7, 14, "7–14 dias",
     True, True,
     "Em neonatos: 3 mg/kg/dose a cada 48–72h conforme IG. "
     "Suspensão oral 10 mg/mL ou 40 mg/mL disponível.",
     "SBI-CAND"),

    ("Fluconazol", "Candidíase orofaríngea",
     "gestante", "150 mg", "dose única (leve) / 150 mg 24/24h × 3–7 dias (grave)", "oral",
     1, 7, "dose única a 7 dias",
     True, True,
     "Dose única 150 mg: evitar no 1º trimestre (risco teratogênico em doses altas e prolongadas). "
     "Preferir miconazol tópico no 1º trimestre. Fluconazol sistêmico após 12 semanas se necessário.",
     "SBI-CAND"),

    ("Fluconazol", "Candidíase vaginal",
     "adulto", "150 mg", "dose única", "oral", 1, 1, "dose única",
     True, True,
     "1ª linha para candidíase vaginal não complicada. "
     "Recorrente (≥ 4 episódios/ano): 150 mg/semana × 6 meses de manutenção. "
     "C. glabrata e C. krusei: resistentes — usar nistatina tópica ou ácido bórico vaginal.",
     "SBI-CAND"),

    ("Fluconazol", "Candidíase vaginal",
     "gestante", "Evitar — usar nistatina tópica", "—", "tópico", None, None,
     "contraindicado sistêmico em gestantes — uso tópico preferido",
     False, False,
     "Fluconazol oral: evitar na gestação (Categoria D). "
     "Nistatina vaginal 100.000 UI/aplicação à noite × 14 dias: segura na gestação.",
     "SBI-CAND"),

    ("Fluconazol", "Candidíase esofágica",
     "adulto", "200–400 mg", "24/24h", "oral ou IV", 14, 21, "14–21 dias",
     True, True,
     "1ª linha para candidíase esofágica. Iniciar com 400 mg/dia nas formas graves ou imunossuprimidos. "
     "Step-down para oral assim que tolerado. Em refratários: anidulafungina ou caspofungina IV.",
     "SBI-CAND"),

    ("Fluconazol", "Candidíase esofágica",
     "insuf_renal", "400 mg dose de ataque; depois 50% da dose se ClCr < 50 mL/min", "24/24h",
     "oral ou IV", 14, 21, "14–21 dias",
     True, True,
     "Ajuste obrigatório: ClCr 11–50 mL/min → 50% da dose habitual; < 11 mL/min → 25% da dose; "
     "hemodiálise: dose completa após cada sessão.",
     "SBI-CAND"),

    ("Fluconazol", "Candidíase esofágica",
     "insuf_hepatica", "Usar com cautela", "24/24h", "oral ou IV", 14, 21, "14–21 dias",
     True, True,
     "Sem ajuste formal; monitorar toxicidade hepática. Evitar em Child-Pugh C.",
     "SBI-CAND"),

    ("Fluconazol", "Criptococose",
     "adulto", "400–800 mg (indução) / 200–400 mg (consolidação) / 200 mg (manutenção)",
     "24/24h", "oral ou IV",
     14, 730,
     "Indução 14 dias; consolidação 8 semanas; manutenção ≥ 12 meses em HIV",
     True, True,
     "Em HIV/AIDS: indução com Anfotericina B + Flucitosina × 14 dias; consolidação fluconazol 400 mg/dia "
     "× 8 semanas; manutenção 200 mg/dia × ≥ 12 meses ou até CD4 > 100 células/µL × 3–6 meses. "
     "PCDT-HIV-FUNG 2022.",
     "SBI-CRIPTO"),

    ("Fluconazol", "Criptococose",
     "pediatrico", "12 mg/kg/dia (máx 800 mg)", "24/24h", "oral ou IV",
     14, 730, "conforme protocolo HIV pediátrico",
     True, True,
     "Indução com anfotericina B ± flucitosina × 14 dias; consolidação fluconazol 12 mg/kg/dia × 8 semanas; "
     "manutenção 6 mg/kg/dia × ≥ 12 meses.",
     "PCDT-HIV-FUNG"),

    ("Fluconazol", "Criptococose",
     "insuf_renal", "800 mg ataque; depois ajuste por ClCr", "24/24h", "oral ou IV",
     14, 730, "conforme protocolo",
     True, True,
     "ClCr < 50 mL/min: 50% da dose; hemodiálise: dose completa pós-diálise.",
     "SBI-CRIPTO"),

    ("Fluconazol", "Histoplasmose",
     "adulto", "400–800 mg", "24/24h", "oral", 365, 365, "12 meses total",
     True, True,
     "Alternativa ao itraconazol quando indisponível ou intolerante; "
     "eficácia inferior ao itraconazol — usar apenas se necessário. "
     "Em HIV/AIDS: manutenção secundária fluconazol 200–400 mg/dia.",
     "SVS-HISTOP"),

    ("Fluconazol", "Pitiríase versicolor",
     "adulto", "300 mg", "dose única semanal × 2 semanas", "oral", 7, 14, "2 semanas",
     True, True,
     "Alternativa ao cetoconazol tópico para casos extensos ou recorrentes. "
     "Tomar em jejum e não banhar por 12h após (aumenta concentração na pele).",
     "SBD-MICOSES"),

    # ══════════════════════════════════════════════════════════════════
    # ANFOTERICINA B DESOXICOLATO
    # ══════════════════════════════════════════════════════════════════
    ("Anfotericina B desoxicolato", "Criptococose",
     "adulto", "0,7–1,0 mg/kg/dia", "24/24h", "IV",
     14, 14, "14 dias (indução)",
     True, False,
     "Indução clássica para criptococose meníngea (protocolo HIV/AIDS). "
     "Infundir em SG 5% em 4–6h com pré-medicação (paracetamol + difenidramina). "
     "Monitorar creatinina e eletrólitos diariamente — hipopotassemia e hipomagnesemia frequentes. "
     "Repor K+ e Mg2+ profilaticamente. Associar flucitosina 25 mg/kg 6/6h se disponível.",
     "SBI-CRIPTO"),

    ("Anfotericina B desoxicolato", "Criptococose",
     "pediatrico", "1,0 mg/kg/dia", "24/24h", "IV", 14, 14, "14 dias (indução)",
     True, False,
     "Dose pediátrica: 1 mg/kg/dia IV. Iniciar com dose-teste 0,1 mg/kg (máx 1 mg) em 1h. "
     "Monitorar função renal, eletrólitos e hemograma 2–3×/semana.",
     "PCDT-HIV-FUNG"),

    ("Anfotericina B desoxicolato", "Criptococose",
     "gestante", "0,7–1,0 mg/kg/dia", "24/24h", "IV", 14, 14, "14 dias",
     True, False,
     "Droga de escolha na gestação para criptococose grave — benefício supera risco. "
     "Monitorar função renal fetal. Flucitosina: evitar (embriotóxica).",
     "SBI-CRIPTO"),

    ("Anfotericina B desoxicolato", "Criptococose",
     "insuf_renal", "0,7 mg/kg/dia (reduzir se Cr > 2,5×basal)", "24/24h", "IV",
     14, 14, "14 dias",
     True, False,
     "Nefrotóxica — se creatinina duplicar do basal: suspender 24–48h e reidratar. "
     "Em insuficiência renal grave pré-existente: considerar anfotericina B lipossomal (se disponível). "
     "Reposição salina (500 mL SF 0,9% antes da infusão) reduz nefrotoxicidade.",
     "SBI-CRIPTO"),

    ("Anfotericina B desoxicolato", "Histoplasmose",
     "adulto", "0,7–1,0 mg/kg/dia", "24/24h", "IV", 14, 14, "14 dias (formas graves)",
     True, False,
     "Indução para histoplasmose disseminada grave ou meníngea. "
     "Dose cumulativa não exceder 35 mg/kg para reduzir nefrotoxicidade. "
     "Seguir com itraconazol 200 mg/dia após estabilização.",
     "SVS-HISTOP"),

    ("Anfotericina B desoxicolato", "Histoplasmose",
     "pediatrico", "1,0 mg/kg/dia", "24/24h", "IV", 14, 14, "14 dias",
     True, False,
     "Dose pediátrica: 1 mg/kg/dia IV. Monitorar função renal, hepática e eletrólitos.",
     "SVS-HISTOP"),

    ("Anfotericina B desoxicolato", "Paracoccidioidomicose",
     "adulto", "0,7–1,0 mg/kg/dia", "24/24h", "IV", 14, 28, "2–4 semanas (formas graves)",
     True, False,
     "Formas graves, disseminadas ou com acometimento de SNC. "
     "Transição para itraconazol oral assim que estabilização clínica.",
     "PCDT-PARACOC"),

    ("Anfotericina B desoxicolato", "Candidemia",
     "adulto", "0,6–1,0 mg/kg/dia", "24/24h", "IV", 14, 21, "≥ 14 dias após última hemocultura negativa",
     True, False,
     "Alternativa às equinocandinas quando não disponíveis. Retirar cateter venoso central se possível. "
     "Fluconazol preferido para step-down em pacientes estáveis e C. albicans sensível.",
     "SBI-CAND"),

    ("Anfotericina B desoxicolato", "Candidemia",
     "neonato", "0,5–1,0 mg/kg/dia", "24/24h", "IV", 14, 21, "≥ 14 dias após hemocultura negativa",
     True, False,
     "Candidemia neonatal: anfotericina B desoxicolato ainda é 1ª linha em muitos serviços brasileiros "
     "pela disponibilidade. Monitorar função renal rigorosamente. "
     "Fluconazol (6–12 mg/kg/dia) é alternativa em neonatos estáveis sem exposição prévia ao fluconazol.",
     "SBI-CAND"),

    ("Anfotericina B desoxicolato", "Mucormicose",
     "adulto", "1,0–1,5 mg/kg/dia", "24/24h", "IV", 14, 42, "mínimo 4–6 semanas",
     True, False,
     "Tratamento de escolha para mucormicose quando anfotericina lipossomal indisponível. "
     "Dose máxima 1,5 mg/kg/dia. Associar cirurgia desbridante precoce (fundamental). "
     "Monitorar nefrotoxicidade diariamente — hipopotassemia grave frequente.",
     "SBMT-FUNGOS"),

    ("Anfotericina B desoxicolato", "Mucormicose",
     "insuf_renal", "1,0 mg/kg/dia (reduzir para 0,5–0,7 se Cr > 2×basal)", "24/24h", "IV",
     14, 42, "individualizar",
     True, False,
     "Mucormicose é fatal sem tratamento — manter anfotericina B mesmo com toxicidade renal. "
     "Hemodiálise pode ser necessária. Hidratação vigorosa com SF 0,9% pré-infusão.",
     "SBMT-FUNGOS"),

    ("Anfotericina B desoxicolato", "Esporotricose",
     "adulto", "0,5–1,0 mg/kg/dia", "24/24h", "IV", 14, 28, "formas sistêmicas e disseminadas",
     True, False,
     "Formas disseminadas, meníngeas ou em imunossuprimidos graves. "
     "Seguir com itraconazol oral após estabilização. "
     "Endemia Rio de Janeiro: S. brasiliensis mantém sensibilidade.",
     "SVS-ESPORO"),

    ("Anfotericina B desoxicolato", "Aspergilose invasiva",
     "adulto", "1,0–1,5 mg/kg/dia", "24/24h", "IV", 14, 84, "individualizar",
     True, False,
     "Alternativa ao voriconazol quando indisponível. Eficácia inferior ao voriconazol. "
     "Usar apenas quando voriconazol contraindicado ou indisponível. "
     "Monitorar função renal diariamente.",
     "SBI-ASPERG"),

    # ══════════════════════════════════════════════════════════════════
    # ANFOTERICINA B LIPOSSOMAL
    # ══════════════════════════════════════════════════════════════════
    ("Anfotericina B lipossomal", "Aspergilose invasiva",
     "adulto", "3–5 mg/kg/dia", "24/24h", "IV", 14, 84, "individualizar conforme resposta",
     False, False,
     "Alternativa ao voriconazol em pacientes com insuficiência renal, transplantados renais ou toxicidade. "
     "Disponibilidade limitada no SUS — acesso via CEAF (componente especializado). "
     "Menor nefrotoxicidade que desoxicolato.",
     "SBI-ASPERG"),

    ("Anfotericina B lipossomal", "Mucormicose",
     "adulto", "5–10 mg/kg/dia", "24/24h", "IV", 28, 84, "4–12 semanas",
     False, False,
     "1ª linha preferencial para mucormicose quando disponível (menor toxicidade). "
     "Dose 5 mg/kg/dia padrão; alguns protocolos usam até 10 mg/kg/dia na rhinocerebral. "
     "ECIL/ESCMID 2022.",
     "SBMT-FUNGOS"),

    ("Anfotericina B lipossomal", "Criptococose",
     "adulto", "3–4 mg/kg/dia", "24/24h", "IV", 14, 14, "14 dias (indução)",
     False, False,
     "Alternativa ao desoxicolato em pacientes com toxicidade renal ou em UTI. "
     "Mesma eficácia antifúngica com menor nefrotoxicidade. "
     "Acesso via componente especializado CEAF quando disponível.",
     "SBI-CRIPTO"),

    ("Anfotericina B lipossomal", "Candidemia",
     "adulto", "3 mg/kg/dia", "24/24h", "IV", 14, 21, "≥ 14 dias após hemocultura negativa",
     False, False,
     "Alternativa para C. auris ou em pacientes com toxicidade renal ao desoxicolato. "
     "C. auris pode ter CIM elevada — checar sensibilidade.",
     "SBI-CAND"),

    ("Anfotericina B lipossomal", "Histoplasmose",
     "adulto", "3 mg/kg/dia", "24/24h", "IV", 14, 14, "14 dias",
     False, False,
     "Preferida em pacientes com insuficiência renal ou intolerância ao desoxicolato. "
     "IDSA 2020: AmB lipossomal 3 mg/kg/dia × 14 dias para histoplasmose moderada-grave.",
     "SVS-HISTOP"),

    # ══════════════════════════════════════════════════════════════════
    # VORICONAZOL
    # ══════════════════════════════════════════════════════════════════
    ("Voriconazol", "Aspergilose invasiva",
     "adulto", "6 mg/kg 12/12h × 2 doses (ataque); 4 mg/kg 12/12h (manutenção)", "12/12h", "IV ou oral",
     42, 84, "mínimo 6–12 semanas",
     False, True,
     "1ª linha para aspergilose invasiva (IDSA 2016, ECIL 2022). "
     "Step-down para oral (200 mg 12/12h) assim que estável. "
     "Monitorar níveis séricos (vale: 1–5,5 µg/mL). "
     "Polimorfismos CYP2C19 afetam metabolismo. Disponibilidade limitada no SUS.",
     "SBI-ASPERG"),

    ("Voriconazol", "Aspergilose invasiva",
     "pediatrico", "9 mg/kg 12/12h IV (ataque e manutenção)", "12/12h", "IV ou oral",
     42, 84, "6–12 semanas",
     False, True,
     "Crianças < 2 anos: não recomendado. 2–12 anos: 9 mg/kg 12/12h IV (máx 350 mg). "
     "Monitorar nível sérico. Menor biodisponibilidade oral em crianças — preferir IV.",
     "SBI-ASPERG"),

    ("Voriconazol", "Aspergilose invasiva",
     "insuf_renal", "200 mg", "12/12h (oral preferido)", "oral", 42, 84, "6–12 semanas",
     False, True,
     "IV: veículo ciclodextrina acumula em ClCr < 50 mL/min — preferir formulação oral. "
     "Sem ajuste de dose renal para formulação oral.",
     "SBI-ASPERG"),

    ("Voriconazol", "Aspergilose invasiva",
     "insuf_hepatica", "Dose normal (ataque); manutenção 50% em Child-Pugh B/C", "12/12h",
     "IV ou oral", 42, 84, "individualizar",
     False, True,
     "Child-Pugh A–B: manter dose de ataque, reduzir manutenção pela metade. "
     "Child-Pugh C: dados insuficientes — usar com cautela extrema e monitorar nível sérico.",
     "SBI-ASPERG"),

    ("Voriconazol", "Fusariose",
     "adulto", "6 mg/kg 12/12h ataque; 4 mg/kg 12/12h manutenção", "12/12h", "IV",
     28, 84, "até reconstituição imune",
     False, True,
     "1ª linha para fusariose invasiva em neutropênicos. Associar fator estimulante G-CSF. "
     "Reduzir imunossupressão se possível. Monitorar nível sérico.",
     "SBI-ASPERG"),

    ("Voriconazol", "Candidemia",
     "adulto", "6 mg/kg 12/12h ataque; 4 mg/kg 12/12h manutenção", "12/12h", "IV",
     14, 21, "≥ 14 dias após hemocultura negativa",
     False, True,
     "Alternativa para candidemia por Candida auris com sensibilidade preservada. "
     "C. krusei: intrinsecamente resistente. Monitorar QT.",
     "SBI-CAND"),

    # ══════════════════════════════════════════════════════════════════
    # CASPOFUNGINA
    # ══════════════════════════════════════════════════════════════════
    ("Caspofungina", "Candidemia",
     "adulto", "70 mg (ataque); 50 mg (manutenção)", "24/24h", "IV",
     14, 21, "≥ 14 dias após hemocultura negativa",
     False, True,
     "1ª linha para candidemia em adultos (IDSA 2016). "
     "Retirar CVC se possível. Step-down para fluconazol oral em pacientes estáveis e C. albicans/parapsilosis. "
     "Disponibilidade limitada no SUS — acesso via CEAF.",
     "SBI-CAND"),

    ("Caspofungina", "Candidemia",
     "pediatrico", "70 mg/m² (ataque); 50 mg/m² (manutenção); máx 70 mg/dia",
     "24/24h", "IV", 14, 21, "≥ 14 dias após hemocultura negativa",
     False, True,
     "Para crianças ≥ 3 meses. Neonatos: dados limitados; anfotericina B preferida. "
     "Monitorar função hepática.",
     "SBI-CAND"),

    ("Caspofungina", "Candidemia",
     "insuf_renal", "70 mg (ataque); 50 mg (manutenção)", "24/24h", "IV",
     14, 21, "≥ 14 dias após hemocultura negativa",
     False, True,
     "Sem ajuste de dose renal — segura em qualquer grau de insuficiência renal.",
     "SBI-CAND"),

    ("Caspofungina", "Candidemia",
     "insuf_hepatica", "70 mg (ataque); 35 mg (manutenção em Child-Pugh B/C)", "24/24h", "IV",
     14, 21, "≥ 14 dias após hemocultura negativa",
     False, True,
     "Child-Pugh B: manutenção 35 mg/dia. Child-Pugh C: dados insuficientes.",
     "SBI-CAND"),

    ("Caspofungina", "Aspergilose invasiva",
     "adulto", "70 mg (ataque); 50 mg (manutenção)", "24/24h", "IV", 14, 84, "individualizar",
     False, True,
     "2ª linha para aspergilose invasiva refratária ou intolerância ao voriconazol. "
     "Combinação com voriconazol pode ser usada em casos refratários graves.",
     "SBI-ASPERG"),

    ("Caspofungina", "Candidemia",
     "neonato", "25 mg/m²/dia", "24/24h", "IV", 14, 21, "≥ 14 dias pós hemocultura negativa",
     False, True,
     "Dados farmacocinéticos limitados em neonatos. Anfotericina B desoxicolato ainda preferida. "
     "Usar caspofungina em resistência documentada ou toxicidade ao desoxicolato.",
     "SBI-CAND"),

    # ══════════════════════════════════════════════════════════════════
    # MICAFUNGINA
    # ══════════════════════════════════════════════════════════════════
    ("Micafungina", "Candidemia",
     "adulto", "100 mg", "24/24h", "IV", 14, 21, "≥ 14 dias após hemocultura negativa",
     False, True,
     "1ª linha para candidemia (equivalente à caspofungina). "
     "Sem ajuste renal. Hepatotóxico: monitorar transaminases.",
     "SBI-CAND"),

    ("Micafungina", "Candidemia",
     "neonato", "10 mg/kg/dia (< 1 kg); 7 mg/kg/dia (1–6 kg)", "24/24h", "IV",
     14, 21, "≥ 14 dias após hemocultura negativa",
     False, True,
     "Melhor perfil farmacocinético que caspofungina em neonatos prematuros. "
     "ESPID 2016 recomenda micafungina como alternativa preferida em neonatos.",
     "SBI-CAND"),

    # ══════════════════════════════════════════════════════════════════
    # ANIDULAFUNGINA
    # ══════════════════════════════════════════════════════════════════
    ("Anidulafungina", "Candidemia",
     "adulto", "200 mg (ataque); 100 mg (manutenção)", "24/24h", "IV",
     14, 21, "≥ 14 dias após hemocultura negativa",
     False, False,
     "1ª linha para candidemia (IDSA 2016). "
     "Sem ajuste renal ou hepático — eliminação por degradação química, não hepática.",
     "SBI-CAND"),

    # ══════════════════════════════════════════════════════════════════
    # POSACONAZOL
    # ══════════════════════════════════════════════════════════════════
    ("Posaconazol", "Aspergilose invasiva",
     "adulto", "300 mg", "24/24h (após 300 mg 12/12h × 1 dia de ataque)", "oral ou IV",
     42, 84, "6–12 semanas",
     False, True,
     "Alternativa ao voriconazol ou quando voriconazol falha. "
     "Profilaxia: 200 mg 8/8h (suspensão) ou 300 mg/dia (comprimido gastrorresistente). "
     "Tomar comprimido com alimento. Disponibilidade restrita no SUS.",
     "SBI-ASPERG"),

    ("Posaconazol", "Mucormicose",
     "adulto", "300 mg", "24/24h", "oral", 28, 84, "manutenção e step-down",
     False, True,
     "Step-down após estabilização com anfotericina B. "
     "Ativo contra Mucorales — único azólico com atividade relevante. "
     "Comprimido gastrorresistente 300 mg/dia mais eficaz que suspensão.",
     "SBMT-FUNGOS"),

    # ══════════════════════════════════════════════════════════════════
    # TERBINAFINA
    # ══════════════════════════════════════════════════════════════════
    ("Terbinafina", "Dermatofitose",
     "adulto", "250 mg", "24/24h", "oral", 42, 90, "Tinea unguium pé: 3 meses; mão: 6 semanas",
     True, True,
     "1ª linha para onicomicose dermatofítica e tinea pedis grave. "
     "Tinea corporis/cruris: 250 mg/dia × 2–4 semanas. "
     "Tinea capitis: 250 mg/dia × 4–8 semanas (adultos). "
     "Disponível no SUS.",
     "SBD-MICOSES"),

    ("Terbinafina", "Dermatofitose",
     "pediatrico", "< 20 kg: 62,5 mg/dia; 20–40 kg: 125 mg/dia; > 40 kg: 250 mg/dia",
     "24/24h", "oral", 28, 90, "Tinea capitis: 4–8 semanas",
     True, True,
     "1ª linha para tinea capitis por Trichophyton (especialmente T. tonsurans). "
     "Granulos (pó oral) disponíveis em alguns países — no Brasil usar comprimido amassado.",
     "SBD-MICOSES"),

    ("Terbinafina", "Dermatofitose",
     "idoso", "250 mg", "24/24h", "oral", 42, 90, "conforme patologia",
     True, True,
     "Monitorar função hepática antes de iniciar e a cada 4–6 semanas. "
     "Em ClCr < 50 mL/min: reduzir dose 50% (dados limitados — alguns especialistas contraindicam).",
     "SBD-MICOSES"),

    ("Terbinafina", "Dermatofitose",
     "insuf_hepatica", "Contraindicada", "—", "oral", None, None, "contraindicado",
     False, True,
     "Contraindicada em insuficiência hepática crônica (hepatotóxica). "
     "Usar alternativas tópicas ou griseofulvina com monitoramento.",
     "SBD-MICOSES"),

    ("Terbinafina", "Esporotricose",
     "adulto", "250–500 mg", "24/24h", "oral", 90, 180, "3–6 meses",
     True, True,
     "Alternativa ao itraconazol para esporotricose cutânea. "
     "Evidência menos robusta que itraconazol mas tolerância geralmente boa.",
     "SVS-ESPORO"),

    # ══════════════════════════════════════════════════════════════════
    # GRISEOFULVINA
    # ══════════════════════════════════════════════════════════════════
    ("Griseofulvina", "Tinea capitis",
     "adulto", "500–1000 mg", "24/24h", "oral", 42, 56, "6–8 semanas",
     True, False,
     "Ainda disponível no SUS. Tomar com refeição gordurosa para melhorar absorção. "
     "Menor eficácia que terbinafina para Trichophyton, mas superior para Microsporum. "
     "Suspensão oral útil em crianças.",
     "SBD-MICOSES"),

    ("Griseofulvina", "Tinea capitis",
     "pediatrico", "10–20 mg/kg/dia (microparticulada); máx 1 g/dia", "24/24h", "oral",
     42, 56, "6–8 semanas",
     True, False,
     "1ª linha histórica para tinea capitis em crianças no Brasil. "
     "Suspensão oral 125 mg/5 mL. Tomar com leite ou alimento gorduroso.",
     "SBD-MICOSES"),

    ("Griseofulvina", "Tinea capitis",
     "gestante", "Contraindicada", "—", "oral", None, None, "contraindicado",
     False, False,
     "Contraindicada na gestação (teratogênica em animais — Categoria X). "
     "Usar tratamento tópico ou aguardar pós-parto para tratamento sistêmico.",
     "SBD-MICOSES"),

    # ══════════════════════════════════════════════════════════════════
    # NISTATINA
    # ══════════════════════════════════════════════════════════════════
    ("Nistatina", "Candidíase orofaríngea",
     "adulto", "400.000–600.000 UI (4–6 mL suspensão)", "6/6h", "oral (bochecho e deglutição)",
     7, 14, "7–14 dias",
     False, False,
     "Suspensão oral 100.000 UI/mL. Bochechar por 2 minutos antes de engolir. "
     "Sem absorção sistêmica — segura em insuficiência renal e hepática. "
     "Disponível no SUS.",
     "SBI-CAND"),

    ("Nistatina", "Candidíase orofaríngea",
     "pediatrico", "200.000 UI (2 mL)", "6/6h", "oral", 7, 14, "7–14 dias",
     False, False,
     "Neonatos e lactentes: 1 mL em cada lado da boca após mamadas. "
     "Em prematuros: 1 mL cada lado 6/6h × 7 dias para profilaxia se IG < 32 semanas.",
     "SBI-CAND"),

    ("Nistatina", "Candidíase orofaríngea",
     "gestante", "400.000 UI (4 mL)", "6/6h", "oral", 7, 14, "7–14 dias",
     False, False,
     "Segura na gestação — sem absorção sistêmica. 1ª linha para candidíase oral em gestantes.",
     "SBI-CAND"),

    ("Nistatina", "Candidíase vaginal",
     "gestante", "100.000 UI / aplicação", "24/24h (à noite)", "vaginal", 14, 14, "14 dias",
     False, False,
     "Óvulos vaginais. 1ª linha para candidíase vaginal em gestantes (segura, sem absorção sistêmica). "
     "Aplicar profundamente com aplicador.",
     "SBI-CAND"),

    ("Nistatina", "Candidíase orofaríngea",
     "neonato", "100.000 UI (1 mL cada lado)", "6/6h", "oral", 7, 14, "7–14 dias",
     False, False,
     "Uso seguro em neonatos a termo e prematuros. Aplicar após mamada.",
     "SBI-CAND"),

    # ══════════════════════════════════════════════════════════════════
    # CLOTRIMAZOL (TÓPICO)
    # ══════════════════════════════════════════════════════════════════
    ("Clotrimazol", "Candidíase vaginal",
     "adulto", "500 mg", "dose única", "vaginal", 1, 1, "dose única",
     False, False,
     "Creme 1% ou 2% à noite × 7–14 dias; óvulo 500 mg dose única. "
     "Disponível no SUS. Alternativa segura e eficaz.",
     "SBI-CAND"),

    ("Clotrimazol", "Candidíase vaginal",
     "gestante", "100 mg / aplicação", "24/24h (à noite)", "vaginal", 7, 14, "7–14 dias",
     False, False,
     "Seguro na gestação. Creme 1% × 7–14 noites. Evitar óvulo com aplicador interno no 1º trimestre.",
     "SBI-CAND"),

    ("Clotrimazol", "Dermatofitose",
     "adulto", "Aplicação fina", "12/12h", "tópico", 14, 28, "2–4 semanas",
     False, False,
     "Creme 1% — tinea corporis, tinea cruris, tinea pedis. "
     "Continuar 1–2 semanas após resolução clínica para prevenir recorrência.",
     "SBD-MICOSES"),

    # ══════════════════════════════════════════════════════════════════
    # CETOCONAZOL (TÓPICO — sistêmico não mais recomendado)
    # ══════════════════════════════════════════════════════════════════
    ("Cetoconazol", "Pitiríase versicolor",
     "adulto", "Aplicação fina (xampu 2%) / creme 2%", "24/24h", "tópico",
     14, 28, "2–4 semanas",
     False, False,
     "Xampu cetoconazol 2%: aplicar no tronco × 3–5 minutos, enxaguar, diariamente × 2 semanas. "
     "Ou creme 2% × 2–4 semanas. Disponível no SUS. "
     "Oral: NÃO usar (hepatotóxico — ANVISA restringiu uso sistêmico em 2013).",
     "SBD-MICOSES"),

    ("Cetoconazol", "Dermatofitose",
     "adulto", "Creme 2% — aplicação fina", "12/12h", "tópico", 14, 28, "2–4 semanas",
     False, False,
     "Tinea corporis e tinea cruris não complicadas. "
     "Oral: contraindicado por hepatotoxicidade (restrição ANVISA/FDA). Usar apenas tópico.",
     "SBD-MICOSES"),

    # ══════════════════════════════════════════════════════════════════
    # IODETO DE POTÁSSIO (KI)
    # ══════════════════════════════════════════════════════════════════
    ("Iodeto de Potássio (KI)", "Esporotricose",
     "adulto", "1 g (iniciar com 0,5 g) e aumentar gradualmente até 6–12 g/dia",
     "8/8h", "oral (em suco de fruta)", 90, 180, "3–6 meses ou até 4 semanas pós-cura",
     False, False,
     "Alternativa histórica para esporotricose cutânea linfangítica — ainda usada no Brasil. "
     "Iniciar com 5 gotas (saturação: 1 g/mL) 3×/dia e aumentar 5 gotas/dose a cada semana. "
     "Efeitos adversos: iodismo (metálico, tosse, acne iododerma). Contraindicado: gestantes, tireoide.",
     "SVS-ESPORO"),

    ("Iodeto de Potássio (KI)", "Esporotricose",
     "pediatrico", "5–10 mg/kg 8/8h (máx 1–2 g 3×/dia)", "8/8h", "oral", 90, 180, "3–6 meses",
     False, False,
     "Diluir em suco de fruta para mascarar sabor. Iniciar com dose menor e aumentar gradualmente. "
     "Monitorar função tireoidiana em crianças.",
     "SVS-ESPORO"),

    ("Iodeto de Potássio (KI)", "Esporotricose",
     "gestante", "Contraindicado", "—", "oral", None, None, "contraindicado",
     False, False,
     "Contraindicado na gestação — pode causar hipotireoidismo e bócio fetal. "
     "Usar anfotericina B desoxicolato nas formas sistêmicas.",
     "SVS-ESPORO"),

    # ══════════════════════════════════════════════════════════════════
    # SULFAMETOXAZOL + TRIMETOPRIMA (SMX-TMP) — Pneumocistose e Paracoccidioidomicose
    # ══════════════════════════════════════════════════════════════════
    ("Sulfametoxazol + Trimetoprima", "Pneumocistose",
     "adulto", "SMX 75–100 mg/kg/dia + TMP 15–20 mg/kg/dia dividido em 3–4 doses",
     "6/6h ou 8/8h", "oral ou IV", 21, 21, "21 dias",
     True, False,
     "1ª linha para pneumocistose (PCP) — PCDT-HIV-FUNG 2022. "
     "Oral se SpO2 > 92% em ar ambiente; IV se hipoxemia grave. "
     "Adjuvante corticosteroide: prednisona 40 mg 12/12h × 5 dias + 40 mg/dia × 5 dias + 20 mg/dia × 11 dias "
     "se PaO2 < 70 mmHg. Disponível no SUS.",
     "PCDT-HIV-FUNG"),

    ("Sulfametoxazol + Trimetoprima", "Pneumocistose",
     "pediatrico", "SMX 75 mg/kg/dia + TMP 15 mg/kg/dia dividido em 3–4 doses",
     "6/6h ou 8/8h", "oral ou IV", 21, 21, "21 dias",
     True, False,
     "Dose pediátrica idêntica em mg/kg. Formulação pediátrica suspensão 200/40 mg/5 mL. "
     "Monitorar neutropenia e plaquetopenia.",
     "PCDT-HIV-FUNG"),

    ("Sulfametoxazol + Trimetoprima", "Pneumocistose",
     "insuf_renal", "Ajuste por ClCr: 50% da dose se ClCr 15–30 mL/min; evitar se < 15 mL/min",
     "12/12h", "oral ou IV", 21, 21, "21 dias",
     True, False,
     "ClCr 15–30: reduzir 50% dose; ClCr < 15: contraindicado (acúmulo de sulfametoxazol). "
     "Pentamidina IV como alternativa em insuficiência renal grave.",
     "PCDT-HIV-FUNG"),

    ("Sulfametoxazol + Trimetoprima", "Paracoccidioidomicose",
     "adulto", "SMX 800 mg + TMP 160 mg (1 cp forte)", "12/12h", "oral",
     365, 730, "12–24 meses",
     True, False,
     "2ª linha para paracoccidioidomicose (alternativa quando itraconazol indisponível ou intolerante). "
     "Menor eficácia que itraconazol — maior taxa de recidiva. "
     "Monitorar função renal, hemograma.",
     "PCDT-PARACOC"),

    ("Sulfametoxazol + Trimetoprima", "Paracoccidioidomicose",
     "pediatrico", "SMX 25 mg/kg/dia + TMP 5 mg/kg/dia", "12/12h", "oral",
     365, 730, "12–24 meses",
     True, False,
     "Suspensão pediátrica 200/40 mg/5 mL. Monitorar hemograma e função renal mensalmente.",
     "PCDT-PARACOC"),

    ("Sulfametoxazol + Trimetoprima", "Pneumocistose",
     "gestante", "SMX 75 mg/kg/dia + TMP 15 mg/kg/dia", "6/6h", "IV ou oral", 21, 21, "21 dias",
     True, False,
     "Usar se risco de vida — benefício supera risco. Evitar próximo ao parto (risco de kernicterus neonatal). "
     "Suplementar ácido folínico (leucovorin) 15 mg/dia durante tratamento.",
     "PCDT-HIV-FUNG"),

    # ══════════════════════════════════════════════════════════════════
    # PENTAMIDINA — alternativa para PCP
    # ══════════════════════════════════════════════════════════════════
    ("Pentamidina (isetionato)", "Pneumocistose",
     "adulto", "4 mg/kg/dia", "24/24h", "IV (infusão em 60–120 min)",
     21, 21, "21 dias",
     True, False,
     "Alternativa ao SMX-TMP em alergia grave ou intolerância. "
     "Toxicidade elevada: hipoglicemia (monitorar glicemia 2×/dia), nefrotoxicidade, pancreatite, hipotensão. "
     "Infusão lenta em 60–120 minutos com monitoramento de PA. Disponível no SUS.",
     "PCDT-HIV-FUNG"),

    ("Pentamidina (isetionato)", "Pneumocistose",
     "pediatrico", "4 mg/kg/dia", "24/24h", "IV", 21, 21, "21 dias",
     True, False,
     "Mesma dose em mg/kg. Monitorar glicemia rigorosamente (risco de hipoglicemia grave). "
     "Monitorar função renal, hepática e pancreática.",
     "PCDT-HIV-FUNG"),

    # ══════════════════════════════════════════════════════════════════
    # FLUCITOSINA (5-FC) — combinação para criptococose
    # ══════════════════════════════════════════════════════════════════
    ("Flucitosina (5-FC)", "Criptococose",
     "adulto", "25 mg/kg", "6/6h", "oral ou IV", 14, 14, "14 dias (fase de indução)",
     True, False,
     "Combinada com Anfotericina B na indução da criptococose meníngea (protocolo OMS/PCDT-HIV-FUNG 2022). "
     "Reduz mortalidade significativamente quando associada. "
     "Monitorar hemograma (mielotoxicidade), função renal e nível sérico (meta: 25–100 µg/mL). "
     "Disponibilidade muito limitada no Brasil — acesso por demanda judicial frequente.",
     "SBI-CRIPTO"),

    ("Flucitosina (5-FC)", "Criptococose",
     "insuf_renal", "25 mg/kg a cada 12–48h conforme ClCr", "ajustar intervalo", "oral ou IV",
     14, 14, "14 dias",
     True, False,
     "ClCr 25–50: 25 mg/kg 12/12h; ClCr 10–25: 25 mg/kg 24/24h; < 10 / hemodiálise: 25 mg/kg pós-diálise. "
     "Monitorar nível sérico para evitar toxicidade hematológica.",
     "SBI-CRIPTO"),

    # ══════════════════════════════════════════════════════════════════
    # CICLOPIROX OLAMINA (TÓPICO)
    # ══════════════════════════════════════════════════════════════════
    ("Ciclopirox olamina", "Dermatofitose",
     "adulto", "Aplicação fina", "12/12h", "tópico", 28, 56, "4–8 semanas",
     False, False,
     "Esmalte 8% para onicomicose leve-moderada (alternativa tópica). "
     "Creme 1% para tinea pedis e corporis. "
     "Aplicar esmalte 1×/dia × 12 meses — menor eficácia que sistêmicos.",
     "SBD-MICOSES"),

    # ══════════════════════════════════════════════════════════════════
    # AMOROLFINA (TÓPICO)
    # ══════════════════════════════════════════════════════════════════
    ("Amorolfina", "Dermatofitose",
     "adulto", "Esmalte 5% — 1 aplicação", "1–2×/semana", "tópico (esmalte ungueal)",
     180, 365, "6–12 meses (unhas pé) / 3–6 meses (unhas mão)",
     False, False,
     "Onicomicose superficial e lateral leve-moderada. "
     "Lixar superfície ungueal antes de cada aplicação. "
     "Pode ser combinado com terbinafina oral para formas extensas.",
     "SBD-MICOSES"),

    # ══════════════════════════════════════════════════════════════════
    # MICONAZOL (TÓPICO E ORAL)
    # ══════════════════════════════════════════════════════════════════
    ("Miconazol", "Candidíase orofaríngea",
     "pediatrico", "Gel oral 20 mg/g — aplicar 5 mL (100 mg)", "6/6h", "oral (tópico mucoso)",
     7, 14, "7–14 dias",
     False, False,
     "Gel oral 2% — usado em lactentes e crianças para candidíase oral. "
     "Aplicar na mucosa com dedo limpo. Risco de asfixia em < 4 meses — usar com cuidado.",
     "SBI-CAND"),

    ("Miconazol", "Candidíase vaginal",
     "adulto", "Creme 2% ou óvulo 400 mg", "24/24h", "vaginal", 3, 7, "3–7 dias",
     False, False,
     "Creme 2%: 5 g/noite × 7 dias. Óvulo 400 mg × 3 noites. "
     "Creme também pode ser aplicado externamente para alívio do prurido.",
     "SBI-CAND"),

]

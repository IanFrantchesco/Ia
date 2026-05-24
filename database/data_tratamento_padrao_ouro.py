"""
Tratamento padrão-ouro para cada patologia bacteriana.
Fontes: PCDTs Ministério da Saúde, GVS 5ª ed., SBI/SBPT diretrizes,
        ANVISA notas técnicas, IDSA guidelines adaptadas ao Brasil.

Formato por entrada:
(patologia_nome_substr, antibiotico_principal, combinacao_ou_None,
 regime_resumido, duracao_resumida, justificativa,
 alternativa_alergia, alternativa_resistencia, obs_especiais,
 grau_recomendacao, nivel_evidencia, fonte_sigla, ano_diretriz)
"""

TRATAMENTO_PADRAO_OURO = [

    # ══════════════════════════════════════════════════════════════
    # RESPIRATÓRIAS
    # ══════════════════════════════════════════════════════════════
    (
        "Pneumonia Adquirida na Comunidade (PAC) – Streptococcus",
        "Amoxicilina",
        None,
        "Amoxicilina 500 mg VO 8/8h (ambulatorial) ou Ceftriaxona 1–2 g IV 24/24h (hospitalizado)",
        "5–7 dias",
        "Cobertura de S. pneumoniae sensível com menor espectro. Amoxicilina 1g 8/8h em áreas de resistência intermediária. Ceftriaxona para internados.",
        "Levofloxacino 750 mg VO/IV 24/24h × 5 dias — alergia grave à penicilina",
        "Levofloxacino ou Moxifloxacino se pneumococo com alta CIM à penicilina",
        "Associar macrólido se suspeita de co-infecção atípica.",
        "A", "I", "SBI-PNEUM", 2018
    ),
    (
        "Pneumonia Adquirida na Comunidade (PAC) – Haemophilus",
        "Amoxicilina-clavulanato",
        None,
        "Amoxicilina-clavulanato 875/125 mg VO 12/12h ou Ceftriaxona 1–2 g IV 24/24h",
        "5–7 dias",
        "H. influenzae produz beta-lactamase em ~30% dos isolados; clavulanato garante cobertura.",
        "Levofloxacino 750 mg VO 24/24h × 5 dias",
        "Cefuroxima IV se produção de beta-lactamase confirmada e amoxicilina falhar",
        "DPOC e tabagistas são os principais afetados.",
        "A", "I", "SBI-PNEUM", 2018
    ),
    (
        "Pneumonia Atípica – Mycoplasma",
        "Azitromicina",
        None,
        "Azitromicina 500 mg VO D1, depois 250 mg VO D2–D5",
        "5 dias",
        "Macrólido é a única classe eficaz contra Mycoplasma (sem parede celular). Azitromicina tem a melhor adesão.",
        "Doxiciclina 100 mg VO 12/12h × 10–14 dias",
        "Levofloxacino 750 mg VO 24/24h × 5 dias se macrólido-resistente",
        "Resistência a macrólidos emergindo; se falha em 72h, trocar por doxiciclina.",
        "A", "I", "SBI-PNEUM", 2018
    ),
    (
        "Pneumonia Atípica – Chlamydophila",
        "Azitromicina",
        None,
        "Azitromicina 500 mg VO D1, depois 250 mg VO D2–D5",
        "5 dias",
        "Intracelular obrigatória — betalactâmicos ineficazes. Macrólido de 1ª escolha.",
        "Doxiciclina 100 mg VO 12/12h × 10–14 dias",
        "Levofloxacino 750 mg VO 24/24h × 5 dias",
        None,
        "A", "I", "SBI-PNEUM", 2018
    ),
    (
        "Pneumonia Hospitalar / Associada à Ventilação Mecânica",
        "Piperacilina-tazobactam",
        None,
        "Piperacilina-tazobactam 4,5 g IV 6/6h (infusão estendida 4h) ou Cefepima 2 g IV 8/8h",
        "7–14 dias",
        "Cobertura antipseudomonas de 1ª linha; infusão estendida otimiza eficácia farmacodinâmica. Escalar para Meropenem se MDR confirmado.",
        "Aztreonam + Vancomicina (alergia grave a betalactâmicos)",
        "Meropenem 2 g IV 8/8h (infusão estendida 3h) em MDR/XDR",
        "Coletar culturas antes de iniciar. Desescalonar em 48–72h com antibiograma.",
        "A", "I", "ANVISA-IRAS", 2023
    ),
    (
        "Tuberculose Pulmonar",
        "Isoniazida (INH)",
        "+ Rifampicina + Pirazinamida + Etambutol",
        "Esquema RHZE: 2 meses de RHZE (fase intensiva) + 4 meses de RH (fase manutenção)",
        "6 meses",
        "Esquema 2RHZE/4RH é o padrão OMS/MS desde 1979; taxa de cura >95% em sensíveis. Rifampicina é o componente esterilizante central.",
        "Esquema alternativo sem rifampicina em hepatopatia grave: consultar especialista",
        "Ver protocolo MDR-TB se resistência a INH ou rifampicina",
        "Associar piridoxina 25–50 mg/dia para prevenir neuropatia periférica pela INH.",
        "A", "I", "PCDT-TB", 2022
    ),
    (
        "Coqueluche",
        "Azitromicina",
        None,
        "Azitromicina 500 mg VO D1, depois 250 mg VO D2–D5 (adultos); 10 mg/kg/dia D1–D5 (lactentes)",
        "5 dias",
        "Macrólido encurta a duração da tosse e reduz transmissão. Iniciar na fase catarral para maior eficácia; ainda indicado na fase paroxística para reduzir contagiosidade.",
        "SMX-TMP 800/160 mg VO 12/12h × 14 dias — alergia a macrólidos",
        None,
        "Lactentes < 1 mês: eritromicina contraindicada (estenose pilórica); usar azitromicina.",
        "A", "I", "PCDT-COQUELUCHE", 2023
    ),
    (
        "Difteria",
        "Eritromicina",
        None,
        "Eritromicina 500 mg VO/IV 6/6h × 14 dias + Soro Antidiftérico (SAD) IV conforme extensão da membrana",
        "14 dias",
        "O SAD neutraliza a toxina circulante — é o elemento terapêutico decisivo. O antibiótico erradica o bacilo e prevém transmissão. Penicilina G cristalina é alternativa equivalente.",
        "Penicilina G cristalina 100.000–150.000 UI/kg/dia IV × 14 dias",
        None,
        "SAD disponível no CRIE (Centro de Referência para Imunobiológicos Especiais) — solicitar imediatamente ao confirmar suspeita.",
        "A", "II", "PCDT-DIFTERIA", 2022
    ),
    (
        "Faringite / Amigdalite Estreptocócica",
        "Penicilina G benzatina",
        None,
        "Penicilina G benzatina 1.200.000 UI IM dose única (adultos); 600.000 UI se < 27 kg",
        "Dose única",
        "Erradica S. pyogenes em >95% dos casos com uma única injeção, garantindo adesão total. Previne febre reumática aguda.",
        "Amoxicilina 500 mg VO 12/12h × 10 dias — recusa de injetável",
        "Azitromicina 500 mg D1 + 250 mg D2–D5 — resistência ou alergia a penicilina",
        "Tratamento obrigatório 10 dias se oral, para erradicar o estreptococo e prevenir febre reumática.",
        "A", "I", "GVS-MS", 2022
    ),
    (
        "Otite Média Aguda Bacteriana",
        "Amoxicilina",
        None,
        "Amoxicilina 40–45 mg/kg/dia VO 12/12h (crianças); 500 mg VO 8/8h (adultos)",
        "5–10 dias",
        "S. pneumoniae e H. influenzae são os agentes mais frequentes; amoxicilina em dose adequada cobre ambos. Alta dose (80–90 mg/kg/dia) em áreas de resistência ao pneumococo.",
        "Amoxicilina-clavulanato — falha em 72h ou suspeita de H. influenzae beta-lactamase+",
        "Ceftriaxona 50 mg/kg IM × 3 dias — resistência múltipla ou impossibilidade oral",
        "Vigilância ativa por 48–72h é razoável em > 2 anos com quadro leve. Antibiótico obrigatório em < 2 anos, otalgia intensa ou febre alta.",
        "A", "I", "GVS-MS", 2022
    ),
    (
        "Sinusite Bacteriana Aguda",
        "Amoxicilina",
        None,
        "Amoxicilina 500 mg VO 8/8h (adulto) ou 45 mg/kg/dia VO 12/12h (criança)",
        "5–7 dias",
        "S. pneumoniae e H. influenzae respondem à amoxicilina na maioria dos casos. Antibiótico indicado apenas quando critérios bacterianos estão presentes (≥ 10 dias sem melhora, piora bifásica ou sintomas graves).",
        "Amoxicilina-clavulanato 875/125 mg VO 12/12h — falha em 72h",
        "Levofloxacino 750 mg VO 24/24h × 5 dias — alergia grave à penicilina",
        "80–90% das sinusites agudas são virais; evitar antibiótico nos primeiros 10 dias sem critério bacteriano.",
        "A", "I", "GVS-MS", 2022
    ),
    (
        "Bronquite Bacteriana Aguda",
        "Amoxicilina",
        None,
        "Amoxicilina 500 mg VO 8/8h × 5–7 dias — apenas em exacerbação bacteriana de DPOC documentada",
        "5–7 dias",
        "Antibiótico reservado para exacerbação de DPOC com aumento de purulência + dispneia + volume. Na maioria das bronquites agudas sem DPOC, antibiótico não é recomendado.",
        "Doxiciclina 100 mg VO 12/12h × 5 dias",
        "Levofloxacino 750 mg VO × 5 dias em exacerbações graves de DPOC (Gold 3–4)",
        "DPOC grave/muito grave: Amoxicilina-clavulanato ou Levofloxacino são preferidos.",
        "B", "II", "GVS-MS", 2022
    ),
    (
        "Epiglotite Bacteriana Aguda",
        "Ceftriaxona",
        None,
        "Ceftriaxona 2 g IV 24/24h (adultos) ou 100 mg/kg/dia IV (crianças)",
        "7–10 dias",
        "H. influenzae tipo b (crianças não vacinadas) ou flora mista (adultos). Ceftriaxona cobre todos os agentes. URGÊNCIA: garantir via aérea antes do antibiótico.",
        "Ampicilina-sulbactam 3 g IV 6/6h — cobertura de flora oral mista em adultos",
        None,
        "PRIORIDADE: estabilização da via aérea (intubação ou traqueostomia de emergência). Corticoide IV controverso — não usar rotineiramente.",
        "A", "II", "GVS-MS", 2022
    ),
    (
        "Abscesso Pulmonar Bacteriano",
        "Clindamicina",
        None,
        "Clindamicina 600–900 mg IV 8/8h → transição para 300–450 mg VO 8/8h após melhora",
        "3–6 semanas",
        "Melhor cobertura de anaeróbios orais (agentes principais) e boa penetração pulmonar. Superior à penicilina G no único ECA disponível.",
        "Amoxicilina-clavulanato 875/125 mg VO 12/12h — tratamento oral alternativo",
        "Meropenem 1 g IV 8/8h — suspeita de Klebsiella pneumoniae (abscesso primário em imunodeprimido)",
        "Drenagem postural obrigatória. Broncoscopia ou drenagem percutânea se sem melhora em 7–10 dias.",
        "A", "II", "GVS-MS", 2022
    ),
    (
        "Empiema Pleural Bacteriano",
        "Ceftriaxona",
        "+ Metronidazol",
        "Ceftriaxona 2 g IV 24/24h + Metronidazol 500 mg IV 8/8h + drenagem pleural obrigatória",
        "2–4 semanas",
        "Cobertura de gram-positivos, gram-negativos e anaeróbios. Drenagem é o pilar do tratamento — sem ela, antibiótico isolado falha.",
        "Piperacilina-tazobactam 4,5 g IV 6/6h — monoterapia alternativa",
        "Meropenem IV — empiema hospitalar ou gram-negativo resistente",
        "Indicar fibrinolítico intrapleural (alteplase + DNase) se empiema septado sem resolução em 48h de drenagem.",
        "A", "I", "GVS-MS", 2022
    ),

    # ══════════════════════════════════════════════════════════════
    # URINÁRIAS
    # ══════════════════════════════════════════════════════════════
    (
        "Cistite Não Complicada – Escherichia coli",
        "Nitrofurantoína",
        None,
        "Nitrofurantoína 100 mg VO 12/12h × 5–7 dias ou Fosfomicina 3 g VO dose única",
        "5–7 dias (Nitrofurantoína) / Dose única (Fosfomicina)",
        "Menor pressão seletiva por resistência e eficácia equivalente às fluoroquinolonas em ITU não complicada. Preservar quinolonas para indicações mais críticas.",
        "Cefalexina 500 mg VO 6/6h × 3–7 dias — contraindicação à nitrofurantoína",
        "Fosfomicina 3 g VO dose única — se resistência confirmada a nitrofurantoína",
        "NÃO usar nitrofurantoína em ClCr < 45 mL/min nem para pielonefrite (sem penetração renal adequada).",
        "A", "I", "SBI-ITU", 2020
    ),
    (
        "Pielonefrite Aguda – Escherichia coli",
        "Ciprofloxacino",
        None,
        "Ciprofloxacino 500 mg VO 12/12h (leve–moderada) ou Ceftriaxona 1–2 g IV 24/24h (hospitalizada)",
        "7–14 dias",
        "Fluoroquinolona VO tem eficácia equivalente ao IV e permite tratamento ambulatorial. IV reservado para: vômitos, sepse, imunossupressão ou resistência suspeita.",
        "Ceftriaxona IV → Cefalexina VO de transição — resistência à quinolona ou gestante",
        "Ertapenem 1 g IV/IM 24/24h — ESBL confirmado",
        "Gestantes: Cefalexina ou Amoxicilina-clavulanato (quinolona contraindicada na gravidez).",
        "A", "I", "SBI-ITU", 2020
    ),
    (
        "ITU Complicada – Klebsiella pneumoniae",
        "Ertapenem",
        None,
        "Ertapenem 1 g IV/IM 24/24h (ESBL confirmado) ou Nitrofurantoína 100 mg VO 12/12h (cepas sensíveis sem pielonefrite)",
        "7–14 dias",
        "ESBL é frequente em K. pneumoniae hospitalar brasileira; ertapenem garante cobertura com menor impacto ecológico que imipenem/meropenem.",
        "Meropenem IV — falha de ertapenem ou bacteremia",
        "Ceftazidima-avibactam — KPC confirmado",
        "Solicitar antibiograma com pesquisa de ESBL e KPC. Desescalar ao sensível mais estreito.",
        "A", "I", "SBI-ITU", 2020
    ),
    (
        "ITU por Enterococcus spp.",
        "Ampicilina",
        None,
        "Ampicilina 500 mg VO 6/6h (baixa não complicada) ou Ampicilina 2 g IV 6/6h (alta/sistêmica)",
        "5–7 dias (baixa) / 10–14 dias (alta)",
        "E. faecalis geralmente sensível à ampicilina. Linezolida e vancomicina reservados para VRE ou falha.",
        "Nitrofurantoína 100 mg VO 12/12h — ITU baixa por E. faecalis sensível, sem opção de ampicilina",
        "Linezolida 600 mg VO/IV 12/12h — VRE confirmado",
        "E. faecium é intrinsecamente resistente à ampicilina — confirmar espécie antes.",
        "A", "II", "SBI-ITU", 2020
    ),
    (
        "ITU por Proteus mirabilis",
        "Amoxicilina-clavulanato",
        None,
        "Amoxicilina-clavulanato 875/125 mg VO 12/12h (ambulatorial) ou Ceftriaxona IV (grave)",
        "7–14 dias",
        "P. mirabilis produz urease que eleva o pH urinário e precipita cálculos. Cobertura com beta-lactâmico + inibidor para produtores de beta-lactamase.",
        "Ciprofloxacino 500 mg VO 12/12h — resistência a amoxicilina-clavulanato",
        "Meropenem IV — ESBL ou KPC",
        "Investigar e tratar cálculos de estruvita associados — reservatório de recorrências.",
        "B", "II", "SBI-ITU", 2020
    ),
    (
        "ITU Associada a Cateter",
        "Nitrofurantoína",
        None,
        "REMOVER OU TROCAR o cateter + antibiótico guiado pelo antibiograma; empírico: Ceftriaxona 1 g IV 24/24h (grave) ou Nitrofurantoína VO (leve/sensível)",
        "7 dias (tratada) / 5 dias se alta resposta",
        "A remoção do cateter é a intervenção mais eficaz. Antibiótico sem remoção do cateter tem alta taxa de recorrência.",
        "Ciprofloxacino VO — gram-negativo sensível, tratamento oral",
        "Meropenem IV — gram-negativo MDR em bacteremia",
        "Bacteriúria assintomática em cateterizado NÃO deve ser tratada, exceto em gestantes ou pré-procedimento urológico.",
        "A", "I", "ANVISA-IRAS", 2023
    ),
    (
        "Prostatite Bacteriana Aguda",
        "Ciprofloxacino",
        None,
        "Ciprofloxacino 500 mg VO 12/12h × 4–6 semanas (forma aguda: iniciar IV 400 mg 12/12h nas primeiras 24–48h se febre alta)",
        "28–42 dias",
        "Fluoroquinolonas têm excelente penetração no tecido prostático (razão tecido:plasma > 1). Duração mínima de 4 semanas para erradicação e prevenção de cronicidade.",
        "SMX-TMP 800/160 mg VO 12/12h × 4–6 semanas — resistência à quinolona com sensibilidade confirmada",
        "Ceftriaxona IV → transição oral guiada por antibiograma — infecção grave ou resistente",
        "Forma aguda grave: internação, Ceftriaxona + Gentamicina IV até estabilização, depois oral.",
        "A", "II", "SBI-ITU", 2020
    ),
    (
        "ITU Gestacional / Bacteriúria Assintomática",
        "Cefalexina",
        None,
        "Cefalexina 500 mg VO 6/6h × 7 dias ou Amoxicilina-clavulanato 875/125 mg VO 12/12h × 7 dias",
        "7 dias",
        "Tratar obrigatoriamente toda bacteriúria em gestante — risco de pielonefrite (20–40%) e parto prematuro. Cefalexina é segura em todas as fases.",
        "Amoxicilina 500 mg VO 8/8h × 7 dias — cepa sensível documentada",
        "Ceftriaxona IV — pielonefrite em gestante com indicação de internação",
        "Nitrofurantoína: evitar no 3º trimestre. Fluoroquinolonas: contraindicadas na gravidez. SMX-TMP: evitar no 1º e 3º trimestres.",
        "A", "I", "GVS-MS", 2022
    ),
    (
        "Staphylococcus saprophyticus – ITU",
        "Nitrofurantoína",
        None,
        "Nitrofurantoína 100 mg VO 12/12h × 5–7 dias",
        "5–7 dias",
        "S. saprophyticus é intrinsecamente sensível à nitrofurantoína; excelente eficácia em cistite não complicada de mulheres jovens.",
        "Cefalexina 500 mg VO 6/6h × 7 dias",
        None,
        "Segunda causa mais comum de cistite em mulheres jovens sexualmente ativas. Não necessita antibiograma na primeira apresentação típica.",
        "A", "II", "SBI-ITU", 2020
    ),

    # ══════════════════════════════════════════════════════════════
    # GASTROINTESTINAIS
    # ══════════════════════════════════════════════════════════════
    (
        "Gastroenterite por Salmonella não-tífica",
        "Ciprofloxacino",
        None,
        "NÃO tratar gastrenterite leve/moderada em imunocompetentes. Ciprofloxacino 500 mg VO 12/12h × 5–7 dias nas formas invasivas",
        "5–7 dias (apenas formas invasivas)",
        "Antibiótico prolonga o estado de portador e não reduz duração dos sintomas em imunocompetentes. Indicar apenas: bacteremia, imunossupressão, < 3 meses, > 65 anos com comorbidades.",
        "Azitromicina 500 mg VO 24/24h × 3 dias — resistência à quinolona",
        "Ceftriaxona IV — bacteremia ou resistência a quinolonas",
        "Reidratação é o pilar do tratamento em todos os casos.",
        "A", "I", "GVS-MS", 2022
    ),
    (
        "Febre Tifoide",
        "Ceftriaxona",
        None,
        "Ceftriaxona 2 g IV 24/24h × 10–14 dias (formas graves) ou Azitromicina 1 g VO D1, depois 500 mg VO D2–D7 (formas não complicadas)",
        "10–14 dias (IV) / 7 dias (VO)",
        "Ceftriaxona é superior para formas graves e neurológicas. Azitromicina tem alta concentração intracelular e intramacrófagos — tratamento oral de eleição para não complicados.",
        "Azitromicina VO — intolerância oral resolvida e forma não complicada",
        "Levofloxacino 750 mg VO × 7 dias — cepas sensíveis à quinolona (confirmar antibiograma)",
        "Cloranfenicol e ampicilina: eficácia reduzida por resistência adquirida no Brasil. Fluoroquinolonas: resistência crescente em cepas importadas da Ásia.",
        "A", "I", "PCDT-FEBRETIFO", 2022
    ),
    (
        "Gastroenterite por Campylobacter",
        "Azitromicina",
        None,
        "Azitromicina 500 mg VO 24/24h × 3 dias — apenas formas moderadas-graves ou imunossuprimidos",
        "3–5 dias",
        "Resistência a fluoroquinolonas > 40% no Brasil. Azitromicina tem sensibilidade preservada em > 85% dos isolados nacionais.",
        "Eritromicina 500 mg VO 6/6h × 5 dias",
        "Imipenem IV — formas invasivas raras ou pan-resistência",
        "Maioria dos casos autolimitada em 5–7 dias sem antibiótico. Tratar: grave, prolongada (> 7 dias), bacteremia, imunossupressão.",
        "A", "I", "GVS-MS", 2022
    ),
    (
        "Shigelose",
        "Ciprofloxacino",
        None,
        "Ciprofloxacino 500 mg VO 12/12h × 3 dias (adultos) ou Azitromicina 20 mg/kg D1, depois 10 mg/kg D2–D5 (crianças)",
        "3–5 dias",
        "Quinolona encurta duração dos sintomas e elimina portação. Em crianças, azitromicina é preferida pela resistência crescente às quinolonas.",
        "Azitromicina 500 mg VO D1, 250 mg D2–D5 — adultos com quinolona-resistência",
        "Ceftriaxona 50 mg/kg IV 24/24h — formas graves ou pan-resistência",
        "S. dysenteriae tipo 1 (Shiga) pode causar SHU — monitorar função renal em crianças.",
        "A", "I", "GVS-MS", 2022
    ),
    (
        "Infecção por Escherichia coli Enteropatogênica",
        "Azitromicina",
        None,
        "Azitromicina 500 mg VO D1, 250 mg D2–D5 (adultos) ou 10 mg/kg/dia (crianças) + reidratação",
        "5 dias",
        "Reidratação é o pilar. ATB indicado em: viajante com sintomas moderados-graves, imunossuprimidos, < 3 meses.",
        "SMX-TMP 800/160 mg VO 12/12h × 3–5 dias — resistência confirmada a azitromicina",
        "Rifaximina 200 mg VO 8/8h × 3 dias — diarreia do viajante não invasiva",
        "EVITAR antibiótico e antiperistálticos em STEC (E. coli O157:H7) — risco de SHU.",
        "B", "II", "GVS-MS", 2022
    ),
    (
        "Cólera",
        "Doxiciclina",
        None,
        "Doxiciclina 300 mg VO dose única (adultos) + Reidratação oral/IV intensiva",
        "Dose única",
        "Reidratação é o tratamento principal e salva vidas. Antibiótico é adjuvante: reduz duração dos sintomas e eliminação do V. cholerae. Doxiciclina dose única garante máxima adesão.",
        "Azitromicina 1 g VO dose única — crianças, gestantes ou resistência à doxiciclina",
        "Ciprofloxacino 1 g VO dose única — alternativa adultos",
        "Reidratação oral (SRO OMS) em casos leves-moderados. Ringer Lactato IV em formas graves. Prioridade absoluta sobre antibiótico.",
        "A", "I", "PCDT-COLERA", 2022
    ),
    (
        "Infecção por Helicobacter pylori",
        "Amoxicilina",
        "+ Claritromicina + IBP",
        "IBP dose dupla + Amoxicilina 1 g 12/12h + Claritromicina 500 mg 12/12h × 14 dias (terapia tripla padrão). Se resistência a claritromicina > 15%: terapia quádrupla com bismuto (IBP + Bismuto + Tetraciclina + Metronidazol)",
        "14 dias",
        "Erradicação de H. pylori previne úlcera péptica recorrente e câncer gástrico. IBP potencializa a ação dos ATBs elevando o pH gástrico. 14 dias superiores a 7 ou 10 dias.",
        "Terapia quádrupla bismuto × 14 dias — alergia à penicilina ou falha prévia",
        "Levofloxacino + Amoxicilina + IBP × 14 dias — 2ª linha após falha da terapia padrão",
        "Idealmente confirmar susceptibilidade. No Brasil, resistência à claritromicina ~25% e ao metronidazol ~35%.",
        "A", "I", "GVS-MS", 2022
    ),
    (
        "Infecção por Clostridioides difficile",
        "Vancomicina",
        None,
        "Vancomicina 125 mg VO 6/6h × 10 dias (não grave) ou 500 mg VO 6/6h × 10–14 dias (grave/fulminante + Metronidazol IV)",
        "10–14 dias",
        "Vancomicina VO é superior ao metronidazol em todos os graus de gravidade. Não tem absorção sistêmica — ação local no cólon. Fidaxomicina superior para prevenção de recorrência (1ª escolha quando disponível).",
        "Fidaxomicina 200 mg VO 12/12h × 10 dias — risco de recorrência ou 1ª recorrência",
        "Bezlotoxumabe IV (anticorpo monoclonal) — adjuvante na prevenção de 2ª recorrência",
        "SUSPENDER ATB precipitante se possível. Metronidazol IV apenas como adjuvante na forma fulminante — NÃO usar metronidazol VO como 1ª linha.",
        "A", "I", "ANVISA-IRAS", 2023
    ),
    (
        "Peritonite Bacteriana Primária",
        "Ceftriaxona",
        None,
        "Ceftriaxona 2 g IV 24/24h × 5–7 dias",
        "5–7 dias",
        "E. coli e K. pneumoniae são os principais agentes. Ceftriaxona cobre ambos com boa concentração no líquido ascítico. Profilaxia primária com Norfloxacino 400 mg/dia em cirróticos com ascite proteína < 1,5 g/dL.",
        "Ciprofloxacino IV — indisponibilidade de ceftriaxona",
        "Piperacilina-tazobactam IV — suspeita de P. aeruginosa (hospitalizado, uso prévio de quinolona)",
        "Albumina IV 1,5 g/kg no D1 e 1 g/kg no D3 reduz mortalidade e síndrome hepatorrenal.",
        "A", "I", "GVS-MS", 2022
    ),
    (
        "Abscesso Hepático Bacteriano",
        "Ceftriaxona",
        "+ Metronidazol",
        "Ceftriaxona 2 g IV 24/24h + Metronidazol 500 mg IV 8/8h + drenagem percutânea",
        "4–6 semanas (IV inicialmente, depois VO)",
        "Cobertura de gram-negativos entéricos e anaeróbios. Drenagem percutânea guiada por imagem é obrigatória em abscessos > 3 cm.",
        "Meropenem IV — K. pneumoniae hipermucoviscosa ou suspeita de ESBL",
        "Amoxicilina-clavulanato VO — fase de manutenção oral após resposta clínica IV",
        "K. pneumoniae hipermucoviscosa (síndrome do abscesso hepático criptogênico) emergente no Brasil — investigar endoftalmite e meningite associadas.",
        "A", "II", "GVS-MS", 2022
    ),
    (
        "Colangite Bacteriana Aguda",
        "Piperacilina-tazobactam",
        None,
        "Piperacilina-tazobactam 4,5 g IV 6/6h + drenagem biliar obrigatória (CPRE ou PTD)",
        "7–10 dias",
        "Cobertura ampla de gram-negativos, incluindo anaeróbios, e enterococo. Drenagem biliar é o pilar do tratamento — sem ela, ATB isolado tem alta mortalidade na colangite grave.",
        "Meropenem + Vancomicina IV — colangite grave nosocomial com Enterococo resistente",
        "Ertapenem IV — ESBL confirmado em ambulatorial",
        "Colangite de Charcot (febre + icterícia + dor) = urgência. Pêntade de Reynolds (+ choque e confusão) = emergência cirúrgica.",
        "A", "I", "GVS-MS", 2022
    ),
    (
        "Apendicite Bacteriana Secundária",
        "Cefazolina",
        "+ Metronidazol",
        "Profilaxia: Cefazolina 2 g IV + Metronidazol 500 mg IV 30–60 min pré-operatório (dose única). Tratamento pós-op se perfurada: Piperacilina-tazobactam 4,5 g IV 6/6h × 3–5 dias",
        "Dose única profilática / 3–5 dias se perfurada",
        "Profilaxia com espectro dirigido à flora colônica. Piperacilina-tazobactam para apendicite perfurada ou com abscesso.",
        "Clindamicina + Gentamicina IV — alergia grave a betalactâmicos",
        "Meropenem IV — infecção hospitalar ou MDR",
        "Apendicite não complicada: antibiótico isolado é uma opção válida (sem cirurgia) em selecionados — estudos escandinavos.",
        "A", "I", "GVS-MS", 2022
    ),

    # ══════════════════════════════════════════════════════════════
    # CUTÂNEAS / TECIDOS MOLES
    # ══════════════════════════════════════════════════════════════
    (
        "Impetigo – Staphylococcus aureus / Streptococcus pyogenes",
        "Mupirocina",
        None,
        "Mupirocina 2% tópica 3x/dia × 5–7 dias (lesões localizadas) ou Cefalexina 500 mg VO 6/6h × 7 dias (disseminado)",
        "5–7 dias",
        "Impetigo localizado: tratamento tópico suficiente e com menor pressão seletiva de resistência. Sistêmico obrigatório em: lesões > 5, disseminadas, ou imunossuprimido.",
        "Amoxicilina-clavulanato VO × 7 dias — suspeita de S. aureus beta-lactamase positivo",
        "SMX-TMP VO — suspeita de CA-MRSA",
        "Higiene local rigorosa. Ácido fusídico tópico é alternativa à mupirocina.",
        "A", "I", "GVS-MS", 2022
    ),
    (
        "Celulite Bacteriana",
        "Cefalexina",
        None,
        "Cefalexina 500 mg VO 6/6h × 5–7 dias (não-purulenta/leve) ou Ceftriaxona 2 g IV 24/24h (grave/hospitalizado)",
        "5–7 dias",
        "S. pyogenes é o agente principal da celulite não-purulenta — betalactâmico é a primeira linha. Cefalexina tem excelente biodisponibilidade oral.",
        "Clindamicina 300 mg VO 8/8h × 5–7 dias — suspeita de CA-MRSA ou alergia à penicilina",
        "Vancomicina IV — celulite grave hospitalar com suspeita de MRSA",
        "Celulite purulenta: drenagem cirúrgica é a prioridade. Marcar a borda da lesão com caneta para monitorar progressão.",
        "A", "I", "GVS-MS", 2022
    ),
    (
        "Erisipela",
        "Penicilina G benzatina",
        None,
        "Penicilina G benzatina 1.200.000 UI IM dose única (leve) ou Penicilina G cristalina 2–4 M UI IV 6/6h × 7–10 dias (grave/hospitalizado)",
        "1 dose (leve) / 7–10 dias (grave)",
        "S. pyogenes é o único agente — penicilina nunca desenvolveu resistência. Benzatina garante nível sérico por 3 semanas e é o tratamento mais custo-efetivo para formas leves.",
        "Cefalexina 500 mg VO 6/6h × 7–10 dias — intolerância a injeção IM",
        "Clindamicina IV — suspeita de S. aureus co-infectante",
        "Tratar porta de entrada (tinea pedis, micose interdigital) para evitar recidivas.",
        "A", "I", "GVS-MS", 2022
    ),
    (
        "Furunculose / Carbúnculo",
        "Incisão e drenagem",
        None,
        "Incisão e drenagem (I&D) como tratamento primário. ATB sistêmico se: > 2 cm, celulite associada, imunossupressão ou CA-MRSA suspeito: SMX-TMP 800/160 mg VO 12/12h × 5–7 dias",
        "5–7 dias (se ATB indicado)",
        "I&D isolada é suficiente em furúnculos < 2 cm sem celulite. ATB reduz recorrência no CA-MRSA comunitário.",
        "Clindamicina 300–450 mg VO 8/8h × 5–7 dias — resistência ao SMX-TMP",
        "Vancomicina IV — MRSA grave ou bacteremia",
        "Descolonização nasal com mupirocina 2% + banhos de clorexidina 4% × 5 dias para portadores recorrentes de CA-MRSA.",
        "A", "I", "GVS-MS", 2022
    ),
    (
        "Fasciíte Necrotizante",
        "Penicilina G cristalina",
        "+ Clindamicina + Cirurgia",
        "DESBRIDAMENTO CIRÚRGICO IMEDIATO (tratamento principal) + Penicilina G cristalina 4 M UI IV 4/4h + Clindamicina 900 mg IV 8/8h ± Vancomicina IV se MRSA suspeito",
        "14–28 dias (ATB) + múltiplas revisões cirúrgicas",
        "Cirurgia é a única intervenção que salva vidas — atraso de horas aumenta mortalidade. Clindamicina inibe produção de toxinas estafilocócicas e estreptocócicas (efeito Eagle). Penicilina atua em fase de crescimento.",
        "Meropenem IV — tipo I polimicrobiana nosocomial",
        "Meropenem + Vancomicina + Clindamicina — polimicrobiana grave com MRSA suspeito",
        "IVIG pode ser considerado em choque tóxico estreptocócico associado. CTI obrigatória.",
        "A", "I", "GVS-MS", 2022
    ),
    (
        "Infecção por MRSA Comunitário",
        "Sulfametoxazol-trimetoprima (SMX-TMP)",
        None,
        "SMX-TMP 800/160 mg VO 12/12h × 5–7 dias (infecções cutâneas leves) + I&D de coleções",
        "5–7 dias",
        "CA-MRSA tem alta sensibilidade ao SMX-TMP (> 85% dos isolados no Brasil). Oral, de baixo custo, amplamente disponível.",
        "Clindamicina 300–450 mg VO 8/8h × 5–7 dias — resistência ao SMX-TMP",
        "Linezolida 600 mg VO 12/12h ou Vancomicina IV — infecção grave ou falha do tratamento oral",
        "Sempre checar sensibilidade local. Descolonização nasal reduz recorrências.",
        "A", "I", "ANVISA-SCIH", 2023
    ),
    (
        "Hanseníase",
        "Rifampicina",
        "+ Dapsona (PB) ou + Dapsona + Clofazimina (MB)",
        "PQT-PB: Rifampicina 600 mg/mês supervisionado + Dapsona 100 mg/dia × 6 meses. PQT-MB: Rifampicina 600 mg/mês + Clofazimina 300 mg/mês supervisionados + Dapsona 100 mg/dia + Clofazimina 50 mg/dia × 12 meses",
        "PB: 6 meses / MB: 12 meses",
        "PQT (poliquimioterapia) da OMS/MS elimina bacilos viáveis na 1ª dose e mantém supressão com doses autoadministradas. Taxa de cura > 98% com PQT completa.",
        "Esquema ROM dose única (Rifampicina + Ofloxacino + Minociclina) — lesão única (PB com 1 lesão)",
        "Ofloxacino + Minociclina substitui dapsona e/ou clofazimina em casos de intolerância",
        "Notificação e exame de contatos obrigatório. Reação hansênica tipo 1 e 2: corticoide e/ou talidomida (tipo 2) — não suspender PQT.",
        "A", "I", "PCDT-HANSENR", 2022
    ),

    # ══════════════════════════════════════════════════════════════
    # ISTs
    # ══════════════════════════════════════════════════════════════
    (
        "Sífilis (adquirida, primária a terciária)",
        "Penicilina G benzatina",
        None,
        "Primária/Secundária: Penicilina G benzatina 1.200.000 UI IM dose única × 1. Latente tardia/Terciária: 1.200.000 UI IM × 3 doses semanais. Neurossífilis: Penicilina G cristalina 3–4 M UI IV 4/4h × 14 dias",
        "1 dose / 3 semanas / 14 dias IV",
        "Treponema pallidum permanece 100% sensível à penicilina G após mais de 70 anos de uso. Nenhum outro antibiótico tem eficácia equivalente para neurossífilis.",
        "Doxiciclina 100 mg VO 12/12h × 14 dias — alergia leve à penicilina (exceto gestante)",
        None,
        "GESTANTE com alergia à penicilina: dessensibilização obrigatória. Nenhum outro ATB previne sífilis congênita com a mesma confiabilidade.",
        "A", "I", "PCDT-IST", 2022
    ),
    (
        "Sífilis Congênita",
        "Penicilina G cristalina",
        None,
        "Penicilina G cristalina 50.000 UI/kg IV 12/12h (primeiros 7 dias de vida) ou 8/8h (após 7 dias) × 10 dias",
        "10 dias IV",
        "Única opção eficaz para sífilis congênita. Penicilina G cristalina garante concentração treponemicida no SNC — fundamental pois 60% dos neonatos com sífilis congênita têm comprometimento neurológico silencioso.",
        None,
        None,
        "Mãe deve ser tratada durante pré-natal com penicilina G benzatina — isso previne a maioria dos casos. Notificação e seguimento obrigatórios até 18 meses.",
        "A", "I", "PCDT-IST", 2022
    ),
    (
        "Gonorreia",
        "Ceftriaxona",
        "+ Azitromicina",
        "Ceftriaxona 500 mg IM dose única + Azitromicina 1 g VO dose única (tratar co-infecção por Clamídia)",
        "Dose única",
        "Único regime com eficácia comprovada contra N. gonorrhoeae na era de resistência crescente a quinolonas (55% no Brasil). Azitromicina cobre simultaneamente Chlamydia, presente em 20–40% das uretrites gonocócicas.",
        "Cefixima 800 mg VO dose única + Azitromicina 1 g — impossibilidade de administração IM",
        "Gentamicina 240 mg IM + Azitromicina 2 g VO — cepa com CIM elevada a ceftriaxona (raro)",
        "NUNCA usar fluoroquinolonas como monoterapia no Brasil. Tratar parceiro(s) simultaneamente.",
        "A", "I", "PCDT-IST", 2022
    ),
    (
        "Infecção por Chlamydia trachomatis",
        "Azitromicina",
        None,
        "Azitromicina 1 g VO dose única (uretrite/cervicite) ou Doxiciclina 100 mg VO 12/12h × 7 dias",
        "Dose única / 7 dias",
        "Azitromicina dose única garante máxima adesão — crucial em IST onde o seguimento é incerto. Doxiciclina tem eficácia levemente superior para LGV e endometrite pélvica.",
        "Eritromicina 500 mg VO 6/6h × 7 dias — gestante (azitromicina alternativa mais tolerada)",
        None,
        "Tratar parceiro(s) simultaneamente. Doxiciclina 100 mg 12/12h × 21 dias para LGV.",
        "A", "I", "PCDT-IST", 2022
    ),
    (
        "Cancro Mole",
        "Azitromicina",
        None,
        "Azitromicina 1 g VO dose única ou Ceftriaxona 250 mg IM dose única",
        "Dose única",
        "Ambos os esquemas de dose única garantem alta adesão. Azitromicina oral é preferida pela facilidade de administração.",
        "Ciprofloxacino 500 mg VO 12/12h × 3 dias — alternativa com boa eficácia",
        None,
        "Aspirar bubão flutuante com agulha grossa — não incisar (risco de fístula). Tratar parceiros.",
        "A", "I", "PCDT-IST", 2022
    ),
    (
        "Linfogranuloma Venéreo",
        "Doxiciclina",
        None,
        "Doxiciclina 100 mg VO 12/12h × 21 dias",
        "21 dias",
        "Tratamento de longa duração necessário para erradicar C. trachomatis de linfonodos e prevenir fibrose linfática. Doxiciclina superior à azitromicina para LGV.",
        "Eritromicina 500 mg VO 6/6h × 21 dias — gestante",
        "Azitromicina 1 g VO × semana × 3 semanas — alternativa com menor evidência",
        "Aspiração de bubão pode ser necessária para alívio. Tratar parceiros com doxiciclina 7 dias.",
        "A", "II", "PCDT-IST", 2022
    ),

    # ══════════════════════════════════════════════════════════════
    # NEUROLÓGICAS / SNC
    # ══════════════════════════════════════════════════════════════
    (
        "Meningite Bacteriana por Neisseria meningitidis",
        "Ceftriaxona",
        None,
        "Ceftriaxona 2 g IV 12/12h × 7 dias + Dexametasona 0,15 mg/kg IV 6/6h × 4 dias (iniciar 15 min ANTES da 1ª dose de ATB)",
        "7 dias",
        "Ceftriaxona tem excelente penetração no LCR e cobre todos os sorogrupos com sensibilidade preservada. Dexametasona reduz sequelas neurológicas (principalmente surdez) em 50%.",
        "Penicilina G cristalina 4 M UI IV 4/4h — sensibilidade confirmada e disponibilidade",
        "Cloranfenicol IV — alergia grave a betalactâmicos",
        "Quimioprofilaxia de contatos íntimos: Rifampicina 600 mg VO 12/12h × 2 dias ou Ciprofloxacino 500 mg VO dose única.",
        "A", "I", "PCDT-MENIN", 2023
    ),
    (
        "Meningite Bacteriana por Streptococcus pneumoniae",
        "Ceftriaxona",
        "+ Vancomicina",
        "Ceftriaxona 2 g IV 12/12h + Vancomicina 15 mg/kg IV 6/6h + Dexametasona 0,15 mg/kg IV 6/6h × 4 dias (antes ou com 1ª dose de ATB)",
        "10–14 dias",
        "Combinação obrigatória por risco de pneumococo resistente à penicilina (CIM > 0,06 mg/L em ~18% no Brasil). Vancomicina cobre cepas DRSP. Dexametasona reduz surdez e sequelas.",
        "Moxifloxacino IV — alergia grave a betalactâmicos e vancomicina",
        "Linezolida + Rifampicina — resistência extrema",
        "Suspender vancomicina se cepa confirmada sensível à ceftriaxona (CIM ≤ 0,5 mg/L).",
        "A", "I", "PCDT-MENIN", 2023
    ),
    (
        "Meningite Bacteriana por Haemophilus influenzae",
        "Ceftriaxona",
        None,
        "Ceftriaxona 100 mg/kg/dia IV 12/12h (crianças) ou 2 g IV 12/12h (adultos) + Dexametasona",
        "7–10 dias",
        "Ceftriaxona cobre H. influenzae incluindo cepas produtoras de beta-lactamase. Dexametasona é especialmente importante nesta meningite para prevenir surdez.",
        "Ampicilina IV — cepa sensível confirmada",
        "Meropenem IV — cepa produtora de beta-lactamase de espectro estendido (raro)",
        "Quimioprofilaxia de contatos com Rifampicina 20 mg/kg/dia × 4 dias.",
        "A", "I", "PCDT-MENIN", 2023
    ),
    (
        "Meningite Neonatal por Streptococcus agalactiae",
        "Ampicilina",
        "+ Gentamicina",
        "Ampicilina 200–400 mg/kg/dia IV + Gentamicina 5 mg/kg/dia IV × 14–21 dias",
        "14–21 dias",
        "GBS permanece universalmente sensível à ampicilina. Gentamicina tem efeito sinérgico bactericida. Duração mínima de 14 dias para meningite e 21 dias se complicada.",
        "Penicilina G cristalina IV — alternativa à ampicilina",
        None,
        "Profilaxia intraparto com Ampicilina em mães GBS-positivas reduz a incidência da forma precoce em > 80%.",
        "A", "I", "PCDT-MENIN", 2023
    ),
    (
        "Meningite por Listeria monocytogenes",
        "Ampicilina",
        "+ Gentamicina",
        "Ampicilina 2 g IV 4/4h + Gentamicina 5 mg/kg/dia IV × 21 dias",
        "21 dias",
        "Listeria é intrinsecamente resistente a cefalosporinas — esquema empírico em meningite de imunocomprometido DEVE incluir ampicilina. Gentamicina confere sinergismo bactericida.",
        "SMX-TMP IV (20/100 mg/kg/dia) — alergia à penicilina",
        None,
        "Todo esquema empírico de meningite em > 50 anos, gestante ou imunossuprimido deve cobrir Listeria (adicionar ampicilina ao esquema padrão).",
        "A", "II", "PCDT-MENIN", 2023
    ),
    (
        "Abscesso Cerebral Bacteriano",
        "Ceftriaxona",
        "+ Metronidazol",
        "Ceftriaxona 2 g IV 12/12h + Metronidazol 500 mg IV 8/8h ± Vancomicina (se MRSA ou pós-neurocirurgia) × 6–8 semanas",
        "6–8 semanas",
        "Cobertura de estreptococos viridans (contiguidade), gram-negativos e anaeróbios. Vancomicina adicionar em pós-operatório de neurocirurgia (S. aureus / MRSA).",
        "Meropenem IV + Metronidazol — gram-negativo MDR ou flora mista hospitalar",
        None,
        "Drenagem cirúrgica obrigatória em abscessos > 2,5 cm ou com deterioração neurológica. Dexametasona controversa — usar apenas se edema com efeito de massa significativo.",
        "A", "II", "GVS-MS", 2022
    ),

    # ══════════════════════════════════════════════════════════════
    # CARDIOVASCULARES
    # ══════════════════════════════════════════════════════════════
    (
        "Endocardite Infecciosa por Staphylococcus aureus",
        "Oxacilina",
        None,
        "MSSA: Oxacilina 2 g IV 4/4h × 4–6 semanas. MRSA: Vancomicina 15–20 mg/kg IV 8/8h × 4–6 semanas ou Daptomicina 6–10 mg/kg IV 24/24h × 4–6 semanas",
        "4–6 semanas",
        "Oxacilina para MSSA tem resultados superiores à vancomicina. Daptomicina é igual à vancomicina para MRSA mas com melhor perfil toxicológico e preferida em bacteremia por MRSA.",
        "Cefazolina 2 g IV 8/8h — alergia leve à penicilina",
        "Ceftaroline + Daptomicina — MRSA com CIM elevada à vancomicina (hVISA/VISA)",
        "Ecocardiograma transesofágico obrigatório. Avaliar indicação cirúrgica: IC, vegetação > 10 mm, êmbolos sépticos, fúngica.",
        "A", "I", "GVS-MS", 2022
    ),
    (
        "Endocardite Infecciosa por Streptococcus viridans",
        "Penicilina G cristalina",
        None,
        "Penicilina G cristalina 12–18 M UI/dia IV contínuo ou 4/4h × 4 semanas ou + Gentamicina 3 mg/kg/dia × 2 semanas (esquema curto em baixo risco)",
        "4 semanas (/ 2 semanas regime curto)",
        "S. viridans com CIM ≤ 0,125 mg/L à penicilina cura com monoterapia de 4 semanas. Esquema de 2 semanas (penicilina + gentamicina) tem igual eficácia em endocardite de valva nativa não complicada.",
        "Ceftriaxona 2 g IV 24/24h × 4 semanas — alergia leve ou comodidade posológica",
        "Vancomicina IV × 4 semanas — alergia grave à penicilina",
        "Gengivite e procedimentos dentários como porta de entrada. Profilaxia com Amoxicilina 2 g VO pré-procedimento em valvopatias de alto risco.",
        "A", "I", "GVS-MS", 2022
    ),
    (
        "Endocardite por Enterococcus",
        "Ampicilina",
        "+ Ceftriaxona",
        "E. faecalis: Ampicilina 2 g IV 4/4h + Ceftriaxona 2 g IV 12/12h × 6 semanas (sinergismo sem toxicidade de aminoglicosídeo)",
        "6 semanas",
        "Combinação Ampicilina + Ceftriaxona tem eficácia equivalente a Ampicilina + Gentamicina para E. faecalis, sem nefrotoxicidade. Aprovada pelas diretrizes europeias e americanas.",
        "Vancomicina + Gentamicina — E. faecium ou E. faecalis com alta resistência à ampicilina",
        "Linezolida + Daptomicina — VRE endocardite",
        "E. faecalis representa 90% das endocardites enterocócicas. E. faecium: geralmente resistente à ampicilina.",
        "A", "I", "GVS-MS", 2022
    ),
    (
        "Febre Reumática Aguda",
        "Penicilina G benzatina",
        None,
        "FASE AGUDA — erradicação do estreptococo: Penicilina G benzatina 1.200.000 UI IM dose única. PROFILAXIA SECUNDÁRIA — prevenção de recorrências: Penicilina G benzatina 1.200.000 UI IM a cada 21 dias (por anos a décadas conforme cardite)",
        "Dose única (agudo) / Anos (profilaxia)",
        "A profilaxia secundária com benzatina cada 21 dias é a intervenção que previne cardiopatia reumática crônica — a principal causa de valvopatia adquirida em jovens no Brasil.",
        "Amoxicilina 500 mg VO 12/12h × 10 dias (agudo) + Amoxicilina 250 mg VO 12/12h (profilaxia)",
        "Eritromicina/Azitromicina — alergia à penicilina",
        "Duração da profilaxia: sem cardite = 5 anos ou até 18 anos. Com cardite sem valvopatia = 10 anos. Com valvopatia = 10 anos ou toda a vida.",
        "A", "I", "GVS-MS", 2022
    ),
    (
        "Pericardite Bacteriana",
        "Piperacilina-tazobactam",
        None,
        "Piperacilina-tazobactam 4,5 g IV 6/6h + drenagem pericárdica cirúrgica ou percutânea",
        "4–6 semanas",
        "Cobertura ampla necessária — flora mista frequente. Drenagem é obrigatória: tamponamento é fatal sem ela.",
        "Meropenem + Vancomicina IV — nosocomial ou pós-cirurgia cardíaca",
        None,
        "TB pericárdica no Brasil: tratar com esquema RHZE × 6 meses + Prednisona × 11 semanas (reduz pericardite constritiva).",
        "A", "II", "GVS-MS", 2022
    ),

    # ══════════════════════════════════════════════════════════════
    # SISTÊMICA / ZOONOSES
    # ══════════════════════════════════════════════════════════════
    (
        "Leptospirose",
        "Penicilina G cristalina",
        None,
        "Forma leve: Doxiciclina 100 mg VO 12/12h × 7 dias. Forma grave (Weil): Penicilina G cristalina 1,5 M UI IV 6/6h × 7 dias ou Ceftriaxona 1 g IV 24/24h × 7 dias",
        "7 dias",
        "Penicilina IV em formas graves (insuficiência renal, icterícia, hemorragia pulmonar) reduz mortalidade. Doxiciclina é suficiente e oral para formas leves e profilaxia pós-exposição (200 mg dose única).",
        "Ceftriaxona 1 g IV 24/24h × 7 dias — alternativa equivalente à penicilina IV",
        None,
        "Diálise é necessária em ~40% das formas graves. Oxigenação e suporte ventilatório na síndrome hemorrágica pulmonar (SHP).",
        "A", "I", "PCDT-LEPTO", 2019
    ),
    (
        "Febre Maculosa Brasileira",
        "Doxiciclina",
        None,
        "Doxiciclina 100 mg VO/IV 12/12h × 7 dias (mínimo até 3 dias afebril)",
        "7 dias (mínimo)",
        "INICIAR IMEDIATAMENTE na suspeita clínica epidemiológica — cada hora de atraso aumenta mortalidade (letalidade > 80% sem tratamento). Não aguardar confirmação laboratorial. A única alternativa aceitável é o cloranfenicol.",
        "Cloranfenicol 50–75 mg/kg/dia IV 6/6h — crianças < 8 anos ou gestantes (em casos graves, doxiciclina supera o risco do cloranfenicol mesmo em crianças)",
        None,
        "Crianças < 8 anos: o risco de morte pela febre maculosa supera o risco de manchas dentárias da doxiciclina — usar doxiciclina mesmo assim nas formas graves.",
        "A", "I", "PCDT-RICKETTSIA", 2022
    ),
    (
        "Rickettsioses (outras espécies)",
        "Doxiciclina",
        None,
        "Doxiciclina 100 mg VO 12/12h × 5–7 dias",
        "5–7 dias",
        "Todas as rickettsioses respondem à doxiciclina. Formas por R. parkeri e R. amblyommatis têm menor mortalidade que R. rickettsii.",
        "Cloranfenicol VO — alternativa em crianças pequenas",
        None,
        "Início precoce da doxiciclina correlaciona com excelente prognóstico mesmo nas formas graves.",
        "A", "I", "PCDT-RICKETTSIA", 2022
    ),
    (
        "Brucelose",
        "Doxiciclina",
        "+ Rifampicina",
        "Doxiciclina 100 mg VO 12/12h + Rifampicina 600–900 mg VO 24/24h × 6 semanas (esquema padrão OMS)",
        "6 semanas",
        "Combinação reduz recorrência vs. monoterapia. Rifampicina é o parceiro clássico pela boa penetração intracelular onde Brucella reside.",
        "Doxiciclina + Estreptomicina 1 g IM × 2–3 semanas — taxa de recorrência ligeiramente menor; padrão alternativo OMS",
        "SMX-TMP + Rifampicina × 6 semanas — crianças < 8 anos (doxiciclina contraindicada)",
        "Espondilodiscite brucélica: tratar por 3–6 meses. Endocardite brucélica: cirurgia geralmente necessária.",
        "A", "I", "PCDT-BRUCELOSE", 2022
    ),
    (
        "Bartonellose",
        "Azitromicina",
        None,
        "Linfadenopatia simples: Azitromicina 500 mg VO D1, 250 mg D2–D5. Angiomatose bacilar / Doença disseminada (HIV): Doxiciclina 100 mg VO 12/12h × 3–4 meses",
        "5 dias (simples) / 3–4 meses (disseminada)",
        "Azitromicina reduz a duração da linfadenopatia por doença da arranhadura do gato. Doxiciclina é preferida nas formas disseminadas em HIV pela ação anti-inflamatória adicional.",
        "Eritromicina 500 mg VO 6/6h — alternativa em imunocomprometidos",
        None,
        "Em HIV com contagem CD4 baixa: recidiva é frequente — considerar profilaxia com Azitromicina ou Doxiciclina.",
        "A", "II", "GVS-MS", 2022
    ),
    (
        "Peste Bubônica",
        "Estreptomicina",
        None,
        "Estreptomicina 1 g IM 12/12h × 10 dias ou Gentamicina 5 mg/kg IV 24/24h × 10 dias",
        "10 dias",
        "Estreptomicina é o padrão-ouro histórico com melhor evidência para peste bubônica. Gentamicina IV é alternativa equivalente com maior disponibilidade no Brasil.",
        "Doxiciclina 100 mg VO 12/12h × 10 dias — forma leve ou profilaxia de contatos",
        "Ciprofloxacino IV — resistência rara ou impossibilidade de aminoglicosídeo",
        "Isolamento por gotícula obrigatório na forma pneumônica. Notificação imediata à OMS.",
        "A", "II", "GVS-MS", 2022
    ),
    (
        "Febre Relapsante",
        "Doxiciclina",
        None,
        "Doxiciclina 100 mg VO dose única (forma epidêmica) ou 100 mg 12/12h × 7 dias (forma endêmica por carrapato)",
        "Dose única / 7 dias",
        "Doxiciclina é eficaz para todas as espécies de Borrelia. Iniciar ATB precipita reação de Jarisch-Herxheimer em 50–90% — monitorar.",
        "Eritromicina VO × 10 dias — gestantes (doxiciclina contraindicada)",
        "Penicilina G IV × 10 dias — formas graves com meningite",
        "Reação de Jarisch-Herxheimer: calafrios, febre e hipotensão nas primeiras 2h do ATB. Trate com suporte — não suspender antibiótico.",
        "A", "II", "GVS-MS", 2022
    ),
    (
        "Melioidose",
        "Ceftazidima",
        None,
        "Fase intensiva: Ceftazidima 2 g IV 8/8h ou Meropenem 1 g IV 8/8h × 10–14 dias. Fase erradicação: SMX-TMP 800/160 mg VO 12/12h × 3–6 meses",
        "10–14 dias IV + 3–6 meses VO",
        "Burkholderia pseudomallei é intrinsecamente resistente à maioria dos ATBs. Ceftazidima e meropenem são as únicas opções eficazes na fase aguda.",
        "Meropenem IV — formas graves ou bacteremia",
        None,
        "Alta taxa de recidiva sem fase de erradicação oral. Diabéticos têm risco elevado de melioidose grave — investigar ativamente no nordeste brasileiro.",
        "A", "II", "GVS-MS", 2022
    ),
    (
        "Tularemia",
        "Estreptomicina",
        None,
        "Estreptomicina 1 g IM 12/12h × 10 dias ou Gentamicina 5 mg/kg/dia IV × 10 dias",
        "10 dias",
        "Aminoglicosídeos têm maior índice de cura (< 1% de falha) comparados a doxiciclina em tularemia. Estreptomicina é o padrão clássico.",
        "Doxiciclina 100 mg VO 12/12h × 14–21 dias — forma leve ou indisponibilidade de aminoglicosídeo",
        "Ciprofloxacino IV — alternativa em bioterrorismo ou resistência",
        "Agente potencial de bioterrorismo (Categoria A CDC). Notificação imediata obrigatória.",
        "A", "II", "GVS-MS", 2022
    ),

    # ══════════════════════════════════════════════════════════════
    # ÓSSEA / ARTICULAR
    # ══════════════════════════════════════════════════════════════
    (
        "Osteomielite Hematogênica – Staphylococcus aureus",
        "Oxacilina",
        None,
        "MSSA: Oxacilina 2 g IV 4/4h × 4–6 semanas → Cefalexina VO 4–6 semanas. MRSA: Vancomicina IV × 4–6 semanas → Linezolida ou SMX-TMP VO",
        "4–6 semanas (total 6–12 semanas com oral)",
        "Oxacilina para MSSA tem penetração óssea superior à vancomicina. Transição para oral precoce (após 48h afebril) é segura e reduz complicações de cateter central.",
        "Cefazolina IV — alergia leve à penicilina",
        "Vancomicina IV + Rifampicina VO — MRSA com prótese",
        "Desbridamento cirúrgico obrigatório se: abscesso subperiosteal, artrite séptica associada, ou ausência de resposta em 48–72h.",
        "A", "I", "GVS-MS", 2022
    ),
    (
        "Artrite Séptica Bacteriana",
        "Oxacilina",
        None,
        "S. aureus (MSSA): Oxacilina 2 g IV 4/4h × 3–4 semanas. MRSA: Vancomicina IV. N. gonorrhoeae: Ceftriaxona 1 g IV 24/24h × 7 dias",
        "3–4 semanas (gram+) / 7 dias (gonocócica)",
        "Drenagem articular (artrocentese diária ou artroscopia) é o pilar do tratamento — antibiótico sem drenagem tem alta taxa de destruição articular.",
        "Cefazolina IV — MSSA, alergia leve à penicilina",
        "Vancomicina IV — MRSA confirmado",
        "Gonocócica em adulto jovem: excelente prognóstico com drenagem + ATB. Tratar parceiros.",
        "A", "I", "GVS-MS", 2022
    ),
    (
        "Espondilodiscite Bacteriana",
        "Oxacilina",
        None,
        "S. aureus MSSA: Oxacilina 2 g IV 6/6h × 6 semanas → Cefalexina VO. MRSA: Vancomicina IV × 6 semanas. TB: Esquema RHZE × 12 meses",
        "6 semanas ATB / 12 meses se TB",
        "Duração mínima de 6 semanas obrigatória. Guiar por hemoculturas e se possível biópsia percutânea pré-ATB para identificar agente.",
        "Ceftriaxona IV — gram-negativo (hemodialisado) ou diagnóstico presuntivo",
        "Meropenem + Vancomicina IV — polimicrobiana nosocomial",
        "Biopsia guiada por imagem antes do ATB é fundamental para diagnóstico microbiológico. Imobilização vertebral em ortese.",
        "A", "II", "GVS-MS", 2022
    ),
    (
        "Infecção de Prótese Articular",
        "Vancomicina",
        "+ Rifampicina",
        "Fase IV (4–6 semanas): Vancomicina IV + Rifampicina 450 mg VO 12/12h. Fase oral (3–6 meses): SMX-TMP 800/160 mg VO 12/12h + Rifampicina 450 mg VO 12/12h",
        "4–6 semanas IV + 3–6 meses VO",
        "Rifampicina é essencial para erradicar biofilme estafilocócico em prótese. Sem rifampicina, recidiva em > 60% dos casos. Retirada do implante melhora resultados.",
        "Ciprofloxacino + Rifampicina — gram-negativos em prótese",
        "Linezolida + Rifampicina — MRSA com intolerância a vancomicina",
        "Estratégias: DAIR (Debridement, Antibiotics, Implant Retention) para infecção aguda < 3 semanas; troca em 2 tempos para crônica.",
        "A", "I", "ANVISA-IRAS", 2023
    ),

    # ══════════════════════════════════════════════════════════════
    # NEONATAL / PERINATAL
    # ══════════════════════════════════════════════════════════════
    (
        "Sepse Neonatal Precoce por Streptococcus agalactiae",
        "Ampicilina",
        "+ Gentamicina",
        "Ampicilina 200 mg/kg/dia IV + Gentamicina 4–5 mg/kg/dia IV (sinérgico). Manter 10 dias (sepse) ou 14–21 dias (meningite)",
        "10–21 dias",
        "GBS permanece universalmente sensível à ampicilina. Gentamicina confere sinergismo bactericida e reduz mortalidade. Profilaxia intraparto com ampicilina IV reduz incidência em > 80%.",
        "Penicilina G cristalina IV + Gentamicina — alternativa equivalente",
        None,
        "Rastreamento materno (swab vaginal/retal 35–37 semanas) e profilaxia intraparto são as principais ferramentas preventivas no Brasil.",
        "A", "I", "GVS-MS", 2022
    ),
    (
        "Sepse Neonatal por Escherichia coli",
        "Ampicilina",
        "+ Gentamicina",
        "Ampicilina 200 mg/kg/dia IV + Gentamicina 4–5 mg/kg/dia IV × 10–14 dias (sepse) ou 21 dias (meningite)",
        "10–21 dias",
        "Cobertura empírica de neonatos com sepse precoce deve incluir gram-negativos. Risco de E. coli K1 com alta virulência neurológica.",
        "Ceftriaxona IV — resistência à ampicilina confirmada (ESBL)",
        "Meropenem IV — E. coli ESBL ou KPC",
        "Suspender ampicilina se cepa resistente. Ampicilina+gentamicina cobre > 80% das E. coli causadoras de sepse neonatal.",
        "A", "I", "GVS-MS", 2022
    ),
    (
        "Listeriose Neonatal",
        "Ampicilina",
        "+ Gentamicina",
        "Ampicilina 200–300 mg/kg/dia IV + Gentamicina 5 mg/kg/dia IV × 14–21 dias",
        "14–21 dias",
        "Listeria é intrinsecamente resistente a cefalosporinas — esquema empírico neonatal deve incluir ampicilina. Gentamicina tem efeito sinérgico comprovado.",
        "SMX-TMP IV — alternativa em alergia grave à penicilina",
        None,
        "Gestantes devem evitar alimentos de alto risco: carnes frias, queijos moles não pasteurizados, sushis.",
        "A", "II", "GVS-MS", 2022
    ),

    # ══════════════════════════════════════════════════════════════
    # HOSPITALAR / IRAS
    # ══════════════════════════════════════════════════════════════
    (
        "Sepse por Klebsiella pneumoniae KPC",
        "Ceftazidima-avibactam",
        None,
        "Ceftazidima-avibactam 2,5 g IV 8/8h (infusão 3h) ± Aztreonam (em KPC + MBL). Alternativa se indisponível: Polimixina B 2,5 mg/kg/dia IV + Meropenem 2 g IV 8/8h (infusão 4h)",
        "14 dias",
        "Ceftazidima-avibactam é superior à polimixina em mortalidade (estudo MERINO). Atua contra KPC, OXA-48 e ESBL. Não age contra metalobetalactamases (NDM) — nesses casos combinar aztreonam.",
        "Meropenem (dose alta, infusão estendida) + Polimixina B + Tigeciclina — se ceftazidima-avibactam indisponível",
        "Cefiderocol IV — KPC resistente a ceftazidima-avibactam (resistência emergente)",
        "Desescalonamento é possível após 72h com antibiograma completo. Controle da fonte (drenagem, remoção de cateter) é essencial.",
        "A", "I", "ANVISA-IRAS", 2023
    ),
    (
        "Infecção por Acinetobacter baumannii Resistente",
        "Polimixina B",
        "+ Ampicilina-sulbactam",
        "Polimixina B 2,5 mg/kg/dia IV + Ampicilina-sulbactam 9 g IV 8/8h (altas doses de sulbactam) ± Tigeciclina",
        "10–14 dias",
        "CRAB: opções terapêuticas extremamente limitadas. Sulbactam tem atividade intrínseca contra A. baumannii independente da ampicilina. Polimixina em combinação reduz emergência de resistência.",
        "Colistina IV + Rifampicina IV — alternativa a polimixina B",
        "Cefiderocol IV — carbapenem-resistente, quando disponível",
        "Controle de infecção hospitalar é mais eficaz que o tratamento. Isolamento em contato obrigatório.",
        "B", "II", "ANVISA-IRAS", 2023
    ),
    (
        "Infecção por Pseudomonas aeruginosa MDR",
        "Ceftolozano-tazobactam",
        None,
        "Ceftolozano-tazobactam 3 g IV 8/8h (infusão 1h) para PAC-MDR. XDR: Polimixina B + Cefepima (alta dose, infusão estendida)",
        "7–14 dias",
        "Ceftolozano-tazobactam tem a melhor atividade para Pseudomonas MDR (incluindo ESBL e AmpC), superior a carbapenens. Fibrose cística: doses mais altas.",
        "Aztreonam + Ceftazidima-avibactam — se MBL positivo (NDM, VIM, IMP)",
        "Cefiderocol IV — XDR-P. aeruginosa",
        "Antibiograma com testes de sensibilidade estendidos (ESBL, MBL) obrigatórios para otimização terapêutica.",
        "A", "I", "ANVISA-IRAS", 2023
    ),
    (
        "Bacteremia por S. aureus MRSA Hospitalar",
        "Vancomicina",
        None,
        "Vancomicina 25–30 mg/kg IV 8/8h (monitoramento AUC/CIM alvo 400–600) ou Daptomicina 6–10 mg/kg IV 24/24h × 14–42 dias conforme sítio",
        "14 dias (bacteremia não complicada) / 28–42 dias (endocardite/osteomielite)",
        "Daptomicina tem mortalidade equivalente à vancomicina em MRSA bacteremia com melhor tolerabilidade. Ambas são 1ª linha. Daptomicina CONTRAINDICADA em pneumonia (inativada pelo surfactante).",
        "Ceftaroline + Daptomicina — MRSA com hVISA/VISA (CIM vancomicina elevada)",
        "Linezolida + Rifampicina — intolerância a vancomicina e daptomicina",
        "Ecocardiograma transesofágico em toda bacteremia por S. aureus para descartar endocardite. Remover ou trocar cateter central.",
        "A", "I", "ANVISA-SCIH", 2023
    ),
    (
        "Infecção de Corrente Sanguínea por Enterococcus Vancomicina-Resistente",
        "Linezolida",
        None,
        "Linezolida 600 mg IV/VO 12/12h ou Daptomicina 6–10 mg/kg IV 24/24h × 14–28 dias",
        "14–28 dias",
        "VRE endocardite/bacteremia: daptomicina em doses altas é bactericida (preferida na endocardite). Linezolida bacteriostática, mas boa opção para bacteremia sem endocardite.",
        "Tigeciclina IV (adjuvante) — infecções intra-abdominais por VRE",
        None,
        "Remover cateter central. Controlar fonte. Transplantados e onco-hematológicos são os mais afetados no Brasil.",
        "A", "II", "ANVISA-IRAS", 2023
    ),
    (
        "Infecção Relacionada a Cateter Venoso Central",
        "Vancomicina",
        None,
        "Empírico: Vancomicina 25 mg/kg IV 8/8h. Gram-negativo suspeito: adicionar Cefepima ou Piperacilina-tazobactam. REMOVER OU TROCAR cateter central obrigatoriamente.",
        "7–14 dias após remoção do cateter",
        "Remoção do cateter é o pilar terapêutico — reduz recorrência e mortalidade independentemente do antibiótico. Coagulase-negativo e S. aureus são os principais agentes.",
        "Daptomicina IV — MRSA com CIM elevada à vancomicina",
        "Ceftazidima-avibactam — gram-negativo MDR/KPC",
        "Bundles de inserção e manutenção (máxima barreira, clorexidina, cobertura oclusiva) previnem > 60% das CRBSI.",
        "A", "I", "ANVISA-IRAS", 2023
    ),
    (
        "Infecção de Sítio Cirúrgico",
        "Cefazolina",
        None,
        "PROFILAXIA: Cefazolina 2 g IV 30–60 min pré-operatório (redosagem a cada 4h em cirurgias longas). TRATAMENTO pós-ISC superficial: Cefalexina 500 mg VO 6/6h × 5–7 dias. ISC profunda ou de órgão: Piperacilina-tazobactam IV + desbridamento",
        "Dose única (profilaxia) / 5–14 dias (tratamento)",
        "Profilaxia com cefazolina reduz ISC em 40–60% em cirurgias limpas e limpo-contaminadas. Tratamento guiado por cultura da ferida.",
        "Clindamicina + Gentamicina IV — alergia grave a betalactâmicos",
        "Vancomicina IV — suspeita de MRSA (histórico, colonização conhecida)",
        "Controle glicêmico intraoperatório e normotermia reduzem ISC independentemente do antibiótico.",
        "A", "I", "ANVISA-SCIH", 2023
    ),

    # ══════════════════════════════════════════════════════════════
    # OCULAR
    # ══════════════════════════════════════════════════════════════
    (
        "Conjuntivite Bacteriana Aguda",
        "Ciprofloxacino",
        None,
        "Ciprofloxacino 0,3% colírio 2 gotas 4x/dia × 5–7 dias ou Tobramicina 0,3% colírio 2 gotas 4x/dia",
        "5–7 dias",
        "Conjuntivite bacteriana é frequentemente autolimitada, mas ATB tópico acelera resolução e reduz contágio. Ciprofloxacino tem amplo espectro e baixa resistência local.",
        "Tobramicina colírio — alternativa equivalente",
        "Moxifloxacino colírio — amplo espectro para gram-positivos e negativos",
        "Conjuntivite neonatal gonocócica: Ceftriaxona 50 mg/kg IV dose única + colírio de eritromicina — URGÊNCIA OFTALMOLÓGICA.",
        "A", "II", "GVS-MS", 2022
    ),
    (
        "Tracoma",
        "Azitromicina",
        None,
        "Azitromicina 1 g VO dose única (adultos) ou 20 mg/kg (crianças). Alternativa: Tetraciclina 1% pomada oftálmica 2x/dia × 6 semanas",
        "Dose única (oral) / 6 semanas (tópico)",
        "Azitromicina oral dose única é superior à tetraciclina tópica em eficácia, adesão e cobertura da transmissão sistêmica. Estratégia SAFE da OMS (Surgery, Antibiotics, Facial cleanliness, Environmental change).",
        "Doxiciclina 100 mg VO 12/12h × 3 semanas — adultos com doença activa sem azitromicina",
        None,
        "Tratamento em massa da comunidade (MDA) é a estratégia de eliminação. Brasil tem metas de eliminação do tracoma como problema de saúde pública.",
        "A", "I", "GVS-MS", 2022
    ),
    (
        "Endoftalmite Bacteriana Pós-operatória",
        "Vancomicina",
        "+ Ceftazidima intravítrea",
        "Vancomicina 1 mg/0,1 mL intravítrea + Ceftazidima 2,25 mg/0,1 mL intravítrea (injeções simultâneas). Vitrectomia via pars plana se acuidade visual ≤ percepção de luz",
        "Injeção única (repetir em 48–72h se sem melhora) + Moxifloxacino colírio",
        "Injeção intravítrea de ATBs é o padrão-ouro — concentrações oculares inalcançáveis por via sistêmica. Vancomicina cobre gram-positivos (S. epidermidis principal agente). Ceftazidima cobre gram-negativos.",
        "Vancomicina + Amicacina intravítrea — alergia a cefalosporinas",
        None,
        "Endoftalmite pós-trauma: incluir cobertura antifúngica empírica. ATB sistêmico não melhora prognóstico visual.",
        "A", "I", "GVS-MS", 2022
    ),

    # ══════════════════════════════════════════════════════════════
    # ANAEROBIOSE / TOXIGÊNICAS
    # ══════════════════════════════════════════════════════════════
    (
        "Tétano Acidental",
        "Metronidazol",
        "+ IGTH + Desbridamento",
        "Metronidazol 500 mg IV 8/8h × 7–10 dias + Imunoglobulina Tetânica Humana (IGTH) 3.000–6.000 UI IM + desbridamento cirúrgico da ferida",
        "7–10 dias ATB",
        "IGTH neutraliza a toxina circulante (pilar principal). Metronidazol elimina C. tetani da ferida e é superior à penicilina G (penicilina pode antagonizar GABA). Desbridamento remove a fonte da toxina.",
        "Penicilina G cristalina 2 M UI IV 4/4h × 7–10 dias — alternativa",
        None,
        "Internação em CTI obrigatória. Controle de espasmos: benzodiazepínicos IV. Traqueostomia em formas graves. Vacinar APÓS recuperação (tétano não confere imunidade).",
        "A", "I", "PCDT-TETANO", 2022
    ),
    (
        "Tétano Neonatal",
        "Metronidazol",
        "+ IGTH neonatal",
        "Metronidazol 15 mg/kg IV ataque, depois 7,5 mg/kg IV 12/12h × 10 dias + IGTH 500 UI IM",
        "10 dias",
        "Mesmo mecanismo do tétano acidental. IGTH neonatal disponível nos CRIE do MS.",
        "Penicilina G cristalina 200.000 UI/kg/dia IV — alternativa",
        None,
        "PREVENÇÃO: vacinar mãe com dT em toda gestação. Higienizar coto umbilical com álcool 70%. Evitar práticas culturais nocivas (aplicar pó, esterco, etc.).",
        "A", "I", "PCDT-TETANO", 2022
    ),
    (
        "Botulismo Alimentar",
        "Soro Antibotulínico",
        None,
        "Soro Antibotulínico Trivalente (A, B, E) IV o mais precocemente possível + suporte ventilatório em UTI. ATB (Penicilina G ou Metronidazol IV) apenas se botulismo de ferida",
        "Dose única soro (repetir em 24h se progressão)",
        "O soro neutraliza a toxina circulante — deve ser administrado antes da confirmação laboratorial. Não reverte paralisia já instalada, apenas evita progressão.",
        None,
        None,
        "Soro Antibotulínico disponível no MS/CRIE. ATB NÃO é indicado no botulismo alimentar (sem bactéria viável a erradicar). Ventilação mecânica pode ser necessária por semanas a meses.",
        "A", "I", "GVS-MS", 2022
    ),
    (
        "Gangrena Gasosa",
        "Penicilina G cristalina",
        "+ Clindamicina + Cirurgia",
        "DESBRIDAMENTO CIRÚRGICO EMERGENCIAL + Penicilina G cristalina 4 M UI IV 4/4h + Clindamicina 900 mg IV 8/8h × 10–14 dias. Câmara hiperbárica adjuvante",
        "10–14 dias ATB",
        "Cirurgia de urgência (amputação frequente) é o único tratamento definitivo. Clindamicina inibe síntese de toxinas clostridianas (alfa-toxina). Hiperbárica reduz necrose tecidual.",
        "Meropenem + Clindamicina IV — infecção polimicrobiana hospitalar",
        None,
        "NÃO atrasar cirurgia para aguardar exames. Cada hora conta. Alta mortalidade sem desbridamento imediato.",
        "A", "I", "GVS-MS", 2022
    ),
    (
        "Síndrome do Choque Tóxico Estafilocócico",
        "Oxacilina",
        "+ Clindamicina + IVIG",
        "MSSA: Oxacilina 2 g IV 4/4h + Clindamicina 900 mg IV 8/8h × 10–14 dias. MRSA: Vancomicina IV + Clindamicina IV. IVIG 1–2 g/kg IV (neutraliza toxina TSST-1)",
        "10–14 dias",
        "Clindamicina inibe síntese de TSST-1 (inibição ribossômica mesmo em alta carga bacteriana). Oxacilina/Vancomicina erradica o bacilo. IVIG neutraliza toxina circulante.",
        "Vancomicina IV + Clindamicina IV — não diferenciação MSSA/MRSA ou MRSA confirmado",
        None,
        "Remover fonte (tampon, material cirúrgico, cateter). CTI obrigatória. Suporte vasopressor agressivo.",
        "A", "II", "GVS-MS", 2022
    ),
    (
        "Síndrome do Choque Tóxico Estreptocócico",
        "Penicilina G cristalina",
        "+ Clindamicina + Cirurgia",
        "Penicilina G cristalina 4 M UI IV 4/4h + Clindamicina 900 mg IV 8/8h × 10–14 dias. IVIG 2 g/kg IV em 24h (adjuvante). Desbridamento cirúrgico da porta de entrada",
        "10–14 dias",
        "Clindamicina inibe síntese de toxinas pirôgenicas estreptocócicas (SPE A, B, C) mesmo com alta densidade bacteriana (efeito Eagle). Penicilina mata o bacilo.",
        "Ceftriaxona IV + Clindamicina IV — alergia à penicilina",
        None,
        "IVIG melhora sobrevida em adultos com choque tóxico estreptocócico (NNT ~7). Desbridamento amplo é frequentemente necessário. CTI com vasopressor.",
        "A", "II", "GVS-MS", 2022
    ),

    # ══════════════════════════════════════════════════════════════
    # OUTRAS
    # ══════════════════════════════════════════════════════════════
    (
        "Escarlatina",
        "Amoxicilina",
        None,
        "Amoxicilina 500 mg VO 12/12h × 10 dias (adultos) ou 40–50 mg/kg/dia VO 12/12h × 10 dias (crianças)",
        "10 dias",
        "S. pyogenes permanece 100% sensível à amoxicilina. 10 dias obrigatórios para erradicação e prevenção de febre reumática. Amoxicilina tem maior adesão que penicilina V.",
        "Azitromicina 500 mg D1 + 250 mg D2–D5 — alergia à penicilina",
        None,
        "Contagiosa por gotícula até 24h após início do ATB. Afastar da escola por 24h após início do tratamento.",
        "A", "I", "GVS-MS", 2022
    ),
    (
        "Tuberculose Extra-pulmonar",
        "Isoniazida (INH)",
        "+ Rifampicina + Pirazinamida + Etambutol",
        "Esquema RHZE × 2 meses + RH × 4 meses (TB ganglionar, pleural, renal). TB meníngea: RHZE × 2 meses + RH × 10 meses (12 meses total). TB óssea: RHZE × 2 meses + RH × 10 meses",
        "6 meses (maioria) / 12 meses (TB SNC e óssea)",
        "Mesmo esquema da TB pulmonar com duração estendida para formas mais graves. Corticosteroides obrigatórios na TB meníngea e pericárdica.",
        "Mesmo esquema — sem alternativa eficaz comparável",
        "Esquema MDR — resistência primária a INH ou rifampicina",
        "TB meníngea: Dexametasona 0,4 mg/kg/dia IV decrescente × 6–8 semanas reduz mortalidade e sequelas.",
        "A", "I", "PCDT-TB", 2022
    ),
    (
        "Tuberculose Resistente (MDR",
        "Levofloxacino",
        "+ Linezolida + Bedaquilina",
        "Esquema MS para MDR-TB: Bedaquilina + Linezolida + Levofloxacino + Clofazimina × 6 meses (esquema BPaL ou BpaLM). Consultar CRPHF/PNCT obrigatoriamente",
        "6–18 meses (variável conforme extensão e resposta)",
        "Esquema BPaLM (Bedaquilina + Pretomanid + Linezolida + Moxifloxacino) por 6 meses mostrou 89% de cura em MDR/XDR-TB no estudo ZeNix. Eliminação de injetáveis melhora adesão.",
        "Bedaquilina + Pretomanid + Linezolida 6 meses (BpaL) — XDR-TB",
        None,
        "Notificação imediata e seguimento em serviço de referência OBRIGATÓRIO. DOTS supervisionado todo o tratamento. Parceiros HIV: consultar especialista sobre interações ARV.",
        "A", "I", "PCDT-TB", 2022
    ),
    (
        "Actinomicose",
        "Penicilina G cristalina",
        None,
        "Fase intensiva: Penicilina G cristalina 18–24 M UI/dia IV contínuo × 2–6 semanas. Fase manutenção: Amoxicilina 500 mg VO 8/8h × 6–12 meses",
        "6–12 meses (total)",
        "Actinomices é uniformemente sensível à penicilina. Tratamento prolongado obrigatório por boa penetração nos sulcos e filamentos — recidiva se curto. Drenagem cirúrgica das coleções.",
        "Doxiciclina 100 mg VO 12/12h × 6–12 meses — alergia à penicilina",
        None,
        "Exérese cirúrgica de lesões volumosas antes do ATB melhora resposta. Forma cervicofacial (> 50% dos casos) tem melhor prognóstico.",
        "A", "II", "GVS-MS", 2022
    ),
    (
        "Nocardiose",
        "Sulfametoxazol-trimetoprima (SMX-TMP)",
        None,
        "Forma leve-moderada: SMX-TMP 800/160 mg VO 8/8h × 6–12 meses. Forma grave/disseminada: SMX-TMP IV + Imipenem 500 mg IV 6/6h + Amicacina 15 mg/kg IV × 3–6 semanas, depois SMX-TMP oral",
        "6–12 meses",
        "SMX-TMP é a droga de escolha para nocardiose — excelente penetração tecidual incluindo SNC. Tratamento prolongado obrigatório em imunossuprimidos.",
        "Linezolida 600 mg VO/IV 12/12h — resistência ao SMX ou intolerância",
        "Amicacina + Imipenem IV — formas com disseminação do SNC",
        "Em HIV com CD4 < 100: profilaxia com SMX-TMP previne nocardiose além de toxoplasmose e PCP.",
        "A", "II", "GVS-MS", 2022
    ),
    (
        "Sepse por Gram-negativos",
        "Meropenem",
        None,
        "Empírico de alto risco: Meropenem 1–2 g IV 8/8h. Baixo risco/comunidade: Ceftriaxona 2 g IV 24/24h. DESESCALAR em 48–72h com antibiograma",
        "7–14 dias (controle de fonte + ATB)",
        "Meropenem empírico para sepse grave/choque séptico garante cobertura de ESBL, P. aeruginosa e Acinetobacter. Desescalonamento reduz pressão seletiva e custo.",
        "Piperacilina-tazobactam IV — sepse moderada sem risco de MDR",
        "Ceftazidima-avibactam IV — KPC suspeito ou confirmado",
        "Antibiótico dentro da 1ª hora em sepse/choque séptico. Controle da fonte (drenagem, cateter) é tão importante quanto o ATB.",
        "A", "I", "SBI-SEPSE", 2021
    ),
    (
        "Parotidite Bacteriana Supurativa",
        "Amoxicilina-clavulanato",
        None,
        "Amoxicilina-clavulanato 875/125 mg VO 12/12h × 10–14 dias (forma leve) ou Oxacilina + Metronidazol IV (forma grave)",
        "10–14 dias",
        "S. aureus é o principal agente. Clavulanato garante cobertura de cepas produtoras de beta-lactamase.",
        "Clindamicina 300 mg VO 8/8h × 10 dias — alergia ou suspeita de CA-MRSA",
        "Vancomicina IV — MRSA hospitalar confirmado",
        "Massagem da parótida, hidratação abundante e estimulação de salivação (balas ácidas) são medidas adjuvantes essenciais. Drenagem cirúrgica se flutuação.",
        "B", "III", "GVS-MS", 2022
    ),
    (
        "Abscesso Dentário / Infecção Odontogênica",
        "Amoxicilina",
        None,
        "Forma leve: Amoxicilina 500 mg VO 8/8h × 5–7 dias + DRENAGEM ODONTOLÓGICA obrigatória. Forma grave/celulite cervical: Amoxicilina-clavulanato IV ou Penicilina G + Metronidazol IV",
        "5–7 dias (leve) / 10–14 dias (grave)",
        "Drenagem da coleção é o tratamento primário — ATB sem drenagem tem alta taxa de falha. Flora mista (estreptococos orais + anaeróbios) responde a amoxicilina.",
        "Clindamicina 300 mg VO 8/8h × 5–7 dias — alergia à penicilina",
        "Meropenem + Vancomicina IV — celulite cervical profunda com MDR suspeito",
        "Angina de Ludwig (celulite do espaço submandibular) é emergência: Via aérea + cirurgia de urgência + ATB IV imediato.",
        "A", "II", "GVS-MS", 2022
    ),
    (
        "Difteria Cutânea",
        "Eritromicina",
        None,
        "Eritromicina 500 mg VO 6/6h × 7–10 dias + Soro Antidiftérico (SAD) se toxina confirmada",
        "7–10 dias",
        "Forma cutânea raramente produz toxina sistêmica em quantidade suficiente para complicações, mas tratar para erradicação do bacilo e prevenção de transmissão.",
        "Penicilina G benzatina IM × 1–2 doses — alternativa",
        None,
        "Cuidado com feridas em regiões tropicais sem vacinação atualizada — ulceração crônica indolente é a forma típica.",
        "A", "II", "PCDT-DIFTERIA", 2022
    ),
    (
        "Listeriose em Adultos Imunocomprometidos",
        "Ampicilina",
        "+ Gentamicina",
        "Ampicilina 2 g IV 4/4h + Gentamicina 5 mg/kg/dia IV × 3–6 semanas (bacteremia) ou 6 semanas (endocardite/meningite)",
        "3–6 semanas",
        "Listeria resistente a cefalosporinas — NUNCA usar como cobertura para Listeria. Ampicilina + gentamicina tem efeito sinérgico bactericida comprovado.",
        "SMX-TMP 15–20 mg/kg/dia IV (componente TMP) — alergia grave à penicilina",
        None,
        "Gestantes: tratar por 4–6 semanas. Prevenir reexposição: evitar carnes frias, patês, queijos moles, sushis.",
        "A", "II", "GVS-MS", 2022
    ),
    (
        "Infecção por Mycoplasma hominis / Ureaplasma",
        "Azitromicina",
        None,
        "Azitromicina 1 g VO dose única (Ureaplasma/uretrite NÃO gonocócica) ou Doxiciclina 100 mg VO 12/12h × 7 dias (formas recorrentes/persistentes)",
        "Dose única / 7 dias",
        "Ureaplasma urealyticum e M. hominis são intrinsecamente resistentes a betalactâmicos (sem parede celular). Azitromicina e doxiciclina são as únicas opções orais eficazes.",
        "Moxifloxacino 400 mg VO 24/24h × 14 dias — resistência a macrólidos e tetraciclinas (rara)",
        None,
        "Uretrite NÃO gonocócica: tratar também Chlamydia (mesmo esquema). Tratar parceiro(s) simultaneamente.",
        "B", "II", "PCDT-IST", 2022
    ),
    (
        "Úlcera de Buruli – Mycobacterium ulcerans",
        "Rifampicina",
        "+ Estreptomicina",
        "Rifampicina 10 mg/kg/dia VO + Estreptomicina 15 mg/kg/dia IM × 8 semanas. Alternativa oral: Rifampicina + Claritromicina × 8 semanas",
        "8 semanas",
        "Esquema OMS recomendado: antibióticos por 8 semanas + cirurgia conservadora quando necessário. Rifampicina + estreptomicina tem melhor evidência de cura.",
        "Rifampicina + Claritromicina VO × 8 semanas — impossibilidade de IM",
        "Rifampicina + Moxifloxacino VO × 8 semanas — alternativa oral equivalente",
        "Casos raros no Brasil — notificar ao MS. Centros de referência na Amazônia.",
        "A", "II", "GVS-MS", 2022
    ),
]

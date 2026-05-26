"""
Interações medicamentosas de antiparasitários — fontes oficiais brasileiras.
Fontes: PCDT-MS, SVS/GVS 5ª ed. 2022, SBMT, SBI, ANVISA.

Formato: lista de tuplas
(antip_nome, med_interagente, classe_interagente, mecanismo, gravidade, efeito_clinico, conduta, fonte_sigla)
"""

INTERACOES_ANTIPARASITARIOS = [
    # ── Antimaláricos ──────────────────────────────────────────────────────────
    ("Artemeter/Lumefantrina", "Rifampicina", "Rifamicinas",
     "Indução potente do CYP3A4 — reduz concentrações plasmáticas de lumefantrina em 68%",
     "grave",
     "Falha terapêutica antipalúdica com risco de malária grave e morte",
     "Evitar associação; se necessário, aumentar dose de artemeter/lumefantrina ou usar quinino + doxiciclina",
     "PCDT-MALARIA"),

    ("Artemeter/Lumefantrina", "Efavirenz (EFZ)", "INNTR (antirretrovirais)",
     "Indução moderada CYP3A4 pelo EFZ — reduz lumefantrina ~50%; EFZ prolonga QT",
     "grave",
     "Redução de eficácia antipalúdica; risco adicionado de prolongamento de QT",
     "Preferir regime de TARV alternativo (dolutegravir) durante tratamento da malária; monitorar ECG",
     "PCDT-MALARIA"),

    ("Quinino", "Halofantrina", "Antimaláricos",
     "Ambos prolongam intervalo QT por mecanismos distintos — efeito aditivo na repolarização ventricular",
     "contraindicada",
     "Risco de arritmia ventricular grave (torsades de pointes, fibrilação ventricular) e morte súbita",
     "Contraindicação absoluta — não coadministrar; monitorar ECG com quinino em combinação com qualquer droga que prolongue QT",
     "PCDT-MALARIA"),

    ("Quinino", "Mefloquina", "Antimaláricos",
     "Ambos têm efeitos cardiotóxicos com prolongamento de QT; mefloquina também inibe CYP2D6",
     "grave",
     "Prolongamento QT, arritmias; potenciação de toxicidade neurológica (tremores, convulsões)",
     "Evitar associação; intervalo mínimo de 12h entre o término da mefloquina e início do quinino",
     "PCDT-MALARIA"),

    ("Mefloquina", "Ácido valproico", "Anticonvulsivantes",
     "Mefloquina diminui concentrações plasmáticas do valproato por mecanismo não totalmente elucidado",
     "grave",
     "Redução do controle de convulsões — risco de crise epiléptica",
     "Evitar em pacientes epilépticos; preferir doxiciclina ou atovaquona/proguanil para profilaxia/tratamento; monitorar níveis de valproato",
     "PCDT-MALARIA"),

    ("Primaquina", "Cloroquina", "Antimaláricos — Aminoquinolonas",
     "Aditividade de efeitos na formação de metemoglobina em eritrócitos com deficiência de G6PD",
     "moderada",
     "Hemólise e metemoglobinemia acentuadas em pacientes G6PD-deficientes",
     "Triagem G6PD obrigatória antes do uso de primaquina; monitorar hemoglobina durante tratamento",
     "PCDT-MALARIA"),

    # ── Antileishmania ─────────────────────────────────────────────────────────
    ("Antimoniato de N-metilglucamina", "Amiodarona", "Antiarrítmicos classe III",
     "Ambos prolongam o intervalo QT por mecanismos independentes — efeito aditivo",
     "contraindicada",
     "Risco de torsades de pointes, fibrilação ventricular e morte súbita",
     "Contraindicação absoluta — não coadministrar; avaliar antecedentes cardiovasculares antes de iniciar Glucantime",
     "PCDT-LEISH-TEG"),

    ("Antimoniato de N-metilglucamina", "Digitálicos (digoxina)", "Glicosídeos cardíacos",
     "Antimoniato prolonga QT; digoxina reduz FC e condução AV — potenciação de efeitos cardíacos",
     "grave",
     "Bradiarritmias, bloqueio AV, prolongamento de QT e risco de arritmias graves",
     "Contraindicado em cardiopatias; se indispensável, monitorar ECG diariamente; considerar anfotericina B lipossomal como alternativa",
     "PCDT-LEISH-TEG"),

    ("Anfotericina B lipossomal", "Aminoglicosídeos (amicacina, gentamicina)", "Antibióticos aminoglicosídeos",
     "Ambos nefrotóxicos; sinergismo de nefrotoxicidade tubular renal — lesão tubular sinérgica",
     "grave",
     "Insuficiência renal aguda; hipopotassemia; hipomagnesemia grave",
     "Evitar associação quando possível; monitorar creatinina, ureia, eletrólitos (K+, Mg2+) diariamente; hidratação pré e pós infusão",
     "PCDT-LEISH-VIS"),

    ("Anfotericina B lipossomal", "Corticosteroides sistêmicos", "Corticosteroides",
     "Corticoides potencializam hipopotassemia induzida pela anfotericina por perda urinária de K+",
     "grave",
     "Hipopotassemia grave com risco de arritmias cardíacas, paralisia muscular",
     "Monitorar potássio sérico; reposição agressiva de KCl; reduzir dose de corticoide se possível",
     "PCDT-LEISH-VIS"),

    # ── Anti-Chagas ────────────────────────────────────────────────────────────
    ("Benznidazol", "Álcool etílico", "Substâncias com efeito dissulfiram-like",
     "Benznidazol inibe desidrogenase do acetaldeído — acúmulo de acetaldeído",
     "grave",
     "Reação dissulfiram-like: rubor, náusea intensa, vômitos, sudorese, palpitações, hipotensão",
     "Abstinência absoluta de álcool durante e por 48h após o tratamento; orientação explícita ao paciente",
     "PCDT-CHAGAS"),

    ("Benznidazol", "Fenitoína", "Anticonvulsivantes hidantoínicos",
     "Indução mútua de metabolismo hepático — benznidazol induz CYP2C9/CYP3A4 que metaboliza fenitoína",
     "moderada",
     "Variação imprevisível dos níveis de fenitoína — risco de toxicidade ou falha no controle de convulsões",
     "Monitorar níveis séricos de fenitoína; ajustar dose conforme necessário; preferir anticonvulsivantes não dependentes do CYP quando possível",
     "PCDT-CHAGAS"),

    ("Nifurtimox", "Fenobarbital", "Anticonvulsivantes barbitúricos",
     "Fenobarbital é indutor potente do CYP3A4 — pode reduzir concentrações plasmáticas de nifurtimox",
     "moderada",
     "Possível redução de eficácia antiparasitária do nifurtimox",
     "Monitorar resposta clínica e parasitológica; considerar ajuste de dose se necessário",
     "PCDT-CHAGAS"),

    # ── Antiprotozoários Nitroimidazóis ────────────────────────────────────────
    ("Metronidazol", "Álcool etílico", "Substâncias com efeito dissulfiram-like",
     "Metronidazol inibe desidrogenase do acetaldeído — acúmulo tóxico de acetaldeído",
     "grave",
     "Reação dissulfiram-like intensa: rubor, cefaleia, náusea, vômitos, taquicardia, hipotensão",
     "Abstinência absoluta de álcool durante e por 48h após término do metronidazol; orientação clara ao paciente",
     "SVS-PARASIT"),

    ("Metronidazol", "Varfarina", "Anticoagulantes cumarínicos",
     "Inibição do CYP2C9 pelo metronidazol — reduz metabolismo da varfarina, aumentando o INR",
     "grave",
     "Potenciação do efeito anticoagulante — risco de hemorragia grave",
     "Monitorar INR 2-3x por semana durante o tratamento; reduzir dose de varfarina em ~30-50%; retornar à dose usual após término do metronidazol",
     "SVS-PARASIT"),

    ("Metronidazol", "Lítio", "Estabilizadores de humor",
     "Metronidazol reduz excreção renal de lítio — elevação da litemia",
     "grave",
     "Toxicidade pelo lítio: tremores, ataxia, confusão, convulsões, insuficiência renal",
     "Monitorar litemias; reduzir dose de lítio durante o tratamento; hidratação adequada; consultar psiquiatra se possível",
     "SVS-PARASIT"),

    ("Tinidazol", "Álcool etílico", "Substâncias com efeito dissulfiram-like",
     "Mesmo mecanismo do metronidazol — inibição da desidrogenase do acetaldeído",
     "grave",
     "Reação dissulfiram-like: rubor, náusea, vômitos, taquicardia",
     "Abstinência absoluta de álcool durante e por 72h após o tinidazol (meia-vida maior que metronidazol)",
     "SVS-PARASIT"),

    # ── Antifolatos (pirimetamina/sulfadiazina) ────────────────────────────────
    ("Pirimetamina", "Ácido fólico", "Vitaminas do grupo B",
     "Ácido fólico compete diretamente com a pirimetamina pela DHFR — antagonismo de ação antiparasitária",
     "grave",
     "Reversão do efeito antiparasitário da pirimetamina — falha terapêutica na toxoplasmose",
     "NUNCA coadministrar ácido fólico com pirimetamina; usar EXCLUSIVAMENTE ácido folínico (leucovorin) para prevenir mielotoxicidade — não são intercambiáveis",
     "PCDT-TOXO"),

    ("Pirimetamina", "Zidovudina (AZT)", "ITRN (antirretrovirais)",
     "Mielotoxicidade aditiva — ambos causam anemia, leucopenia, plaquetopenia por supressão medular",
     "grave",
     "Pancitopenia grave; anemia, neutropenia, trombocitopenia — maior risco em pacientes com doença avançada",
     "Monitorar hemograma semanal; considerar substituição do AZT por TDF ou ABC durante tratamento com pirimetamina; garantir ácido folínico",
     "PCDT-TOXO"),

    ("Sulfadiazina", "Fenitoína", "Anticonvulsivantes hidantoínicos",
     "Sulfadiazina inibe CYP2C9 — reduz metabolismo da fenitoína, elevando sua concentração sérica",
     "moderada",
     "Toxicidade por fenitoína: nistagmo, ataxia, confusão, sedação excessiva",
     "Monitorar níveis séricos de fenitoína; reduzir dose se necessário; manter anticonvulsivante pois convulsões são comuns na toxoplasmose cerebral",
     "PCDT-TOXO"),

    ("Sulfadiazina", "Metotrexato", "Antimetabólitos (antineoplásicos/imunossupressores)",
     "Sulfonamidas competem com metotrexato pela ligação a proteínas plasmáticas e inibem sua excreção tubular renal",
     "grave",
     "Toxicidade severa por metotrexato: mucosite, pancitopenia, hepatotoxicidade, nefrotoxicidade",
     "Evitar associação; se necessária, monitorar níveis de metotrexato; ácido folínico em doses altas",
     "PCDT-TOXO"),

    # ── Anti-helmínticos ───────────────────────────────────────────────────────
    ("Albendazol", "Corticosteroides sistêmicos (dexametasona)", "Corticosteroides",
     "Dexametasona inibe o CYP3A4 hepático — aumenta concentrações plasmáticas de sulfóxido de albendazol (metabólito ativo) em 56%",
     "leve",
     "Aumento da concentração do metabólito ativo — potencialmente benéfico na NCC (maior penetração no SNC)",
     "Associação intencional no tratamento da NCC (dexametasona + albendazol); monitorar hepatotoxicidade (enzimas hepáticas)",
     "PCDT-NCC"),

    ("Albendazol", "Cimetidina", "Bloqueadores H2",
     "Cimetidina inibe CYP1A2 e CYP3A4 — pode aumentar níveis plasmáticos do sulfóxido de albendazol",
     "leve",
     "Potencial aumento de eficácia (maior concentração de metabólito ativo) mas também de toxicidade hepática",
     "Monitorar enzimas hepáticas; associação geralmente bem tolerada; raramente de relevância clínica",
     "PCDT-NCC"),

    ("Praziquantel", "Rifampicina", "Rifamicinas",
     "Rifampicina é indutor potente do CYP3A4 — reduz AUC do praziquantel em > 80%",
     "grave",
     "Falha terapêutica para esquistossomose ou teníase — concentrações subterapêuticas de praziquantel",
     "Suspender rifampicina 4 semanas antes do praziquantel quando possível; alternativa: oxamniquina para esquistossomose; triclabendazol não é afetado",
     "PCDT-ESQUIS"),

    ("Praziquantel", "Dexametasona", "Corticosteroides",
     "Dexametasona induz CYP3A4 — reduz concentrações plasmáticas de praziquantel em 50%",
     "moderada",
     "Potencial redução de eficácia na teníase (menos crítico na NCC onde doses mais altas são usadas)",
     "Na NCC: preferir albendazol que tem sua concentração aumentada pela dexametasona; na esquistossomose: evitar associação com dexametasona",
     "PCDT-NCC"),

    ("Ivermectina", "Varfarina", "Anticoagulantes cumarínicos",
     "Ivermectina pode inibir CYP3A4 — leve potenciação do efeito anticoagulante da varfarina",
     "moderada",
     "Aumento modesto do INR — risco hemorrágico em pacientes anticoagulados",
     "Monitorar INR 3-5 dias após ivermectina em pacientes anticoagulados; ajustar dose de varfarina se necessário",
     "SVS-PARASIT"),

    ("Ivermectina", "Benzodiazepínicos", "Ansiolíticos/Hipnóticos",
     "Ivermectina potencializa efeito inibitório GABA — sinergismo com benzodiazepínicos nos canais Cl-/GABA no SNC",
     "moderada",
     "Sedação excessiva, depressão respiratória em doses altas ou pacientes idosos/débeis",
     "Usar com cautela em pacientes em uso de benzodiazepínicos; reduzir dose de BZD se possível; monitorar nível de consciência",
     "SVS-PARASIT"),

    ("Dietilcarbamazina (DEC)", "Dietilcarbamazina (DEC) — na oncocercose", "Antifilarial",
     "DEC mata microfilárias de Onchocerca na pele e olhos — reação inflamatória intensa (Mazzotti) pode causar cegueira",
     "contraindicada",
     "Reação de Mazzotti ocular intensa por morte em massa das microfilárias: inflamação, lesão corneal, cegueira irreversível",
     "DEC é CONTRAINDICADA na oncocercose; usar EXCLUSIVAMENTE ivermectina para oncocercose; DEC só para filariose linfática",
     "PCDT-FILARIA"),

    # ── Ectoparasitoses ────────────────────────────────────────────────────────
    ("Permetrina", "Outros piretroides tópicos", "Antiparasitários — Piretroides",
     "Aditividade de neurotoxicidade por piretroides no SNC do hospedeiro em exposição excessiva (área extensa)",
     "leve",
     "Parestesias, tontura, irritação local em exposição excessiva ou em grandes áreas",
     "Não aplicar em mucosas, olhos ou em feridas abertas; seguir instruções de área de aplicação; lavar mãos após aplicação",
     "SVS-PARASIT"),

    ("Benzil benzoato 25%", "Outros irritantes cutâneos (álcool, acetona)", "Irritantes tópicos",
     "Irritação sinérgica da barreira cutânea — dano ao extrato córneo",
     "leve",
     "Dermatite de contato por irritação primária; eczema em pele sensível",
     "Não aplicar em pele com soluções alcoólicas; diluir a 12,5% em crianças; evitar áreas de dobras com pele macerada",
     "SVS-PARASIT"),
]

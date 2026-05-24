"""
Dados de eficácia de antibióticos por bactéria e patologia.
Baseado em: PCDTs do MS, ANVISA ANSIRE/WHONET-BR, SBI, SBPT diretrizes.

Formato por bloco:
bacteria_nome_cientifico -> lista de:
  (antibiotico_nome_generico, patologia_nome_parcial_ou_None,
   eficacia_pct, linha_tratamento, nivel_evidencia, resistencia_br_pct, fonte_sigla, ano, consideracoes)
"""

# Estrutura: dict { bacteria_nome_cientifico: [ (atb, patologia_substr, ef%, linha, evidencia, resist_br%, fonte, ano, obs) ] }

EFICACIA = {
    "Streptococcus pneumoniae": [
        ("Penicilina G cristalina",         "Meningite Bacteriana por Streptococcus pneumoniae", 85.0, 1, "A", 18.0, "PCDT-MENIN",  2023, "Usar apenas se CIM ≤0,06 mg/L; altas doses 4-6 M UI q4h IV"),
        ("Ceftriaxona",                      "Meningite Bacteriana por Streptococcus pneumoniae", 92.0, 1, "A",  8.0, "PCDT-MENIN",  2023, "Primeira linha atual para meningite pneumocócica"),
        ("Vancomicina",                      "Meningite Bacteriana por Streptococcus pneumoniae", 88.0, 1, "A",  1.0, "PCDT-MENIN",  2023, "Associar à ceftriaxona em suspeita de resistência"),
        ("Amoxicilina",                      "Pneumonia Adquirida na Comunidade (PAC) – Streptococcus pneumoniae", 91.0, 1, "A", 14.0, "SBI-PNEUM",   2018, "PAC leve-moderada ambulatorial"),
        ("Ceftriaxona",                      "Pneumonia Adquirida na Comunidade (PAC) – Streptococcus pneumoniae", 94.0, 1, "A",  8.0, "SBI-PNEUM",   2018, "PAC hospitalizada"),
        ("Levofloxacino",                    "Pneumonia Adquirida na Comunidade (PAC) – Streptococcus pneumoniae", 93.0, 2, "A",  2.5, "SBI-PNEUM",   2018, "Alternativa em alergia à penicilina ou pneumococo resistente"),
        ("Azitromicina",                     "Pneumonia Adquirida na Comunidade (PAC) – Streptococcus pneumoniae", 72.0, 2, "B", 25.0, "SBI-PNEUM",   2018, "Resistência de ~25% no Brasil; evitar como monoterapia"),
        ("Amoxicilina",                      "Otite Média Aguda Bacteriana",                       90.0, 1, "A", 14.0, "GVS-MS",      2022, "Primeira linha em OMA"),
        ("Amoxicilina-clavulanato",          "Otite Média Aguda Bacteriana",                       93.0, 2, "A", None, "GVS-MS",      2022, "Segunda linha ou falha de amoxicilina"),
    ],

    "Streptococcus pyogenes": [
        ("Penicilina G benzatina",           "Faringite / Amigdalite Estreptocócica",              96.0, 1, "A",  0.0, "GVS-MS",      2022, "Dose única IM 1,2M UI adultos; elimina portador"),
        ("Amoxicilina",                      "Faringite / Amigdalite Estreptocócica",              95.0, 1, "A",  0.0, "GVS-MS",      2022, "10 dias; superior à penicilina V em adesão"),
        ("Azitromicina",                     "Faringite / Amigdalite Estreptocócica",              85.0, 2, "A", 12.0, "GVS-MS",      2022, "Em alergia à penicilina; 5 dias"),
        ("Clindamicina",                     "Faringite / Amigdalite Estreptocócica",              88.0, 2, "B",  8.0, "GVS-MS",      2022, "Alternativa em alergia ou falha"),
        ("Penicilina G cristalina",          "Erisipela",                                          96.0, 1, "A",  0.0, "GVS-MS",      2022, "Formas moderadas-graves IV"),
        ("Amoxicilina",                      "Erisipela",                                          94.0, 1, "A",  0.0, "GVS-MS",      2022, "Erisipela leve oral"),
        ("Cefalexina",                       "Celulite Bacteriana",                                91.0, 1, "A",  0.0, "GVS-MS",      2022, "Celulite não-purulenta ambulatorial"),
        ("Penicilina G cristalina",          "Febre Reumática Aguda",                              98.0, 1, "A",  0.0, "GVS-MS",      2022, "Erradicação S. pyogenes; profilaxia secundária com BZT"),
        ("Penicilina G cristalina",          "Síndrome do Choque Tóxico Estreptocócico",           88.0, 1, "A",  0.0, "GVS-MS",      2022, "Associar clindamicina para inibição de toxina"),
        ("Clindamicina",                     "Síndrome do Choque Tóxico Estreptocócico",           92.0, 1, "A",  8.0, "GVS-MS",      2022, "Inibição da síntese de toxina; sempre em combinação"),
    ],

    "Streptococcus agalactiae": [
        ("Ampicilina",                       "Sepse Neonatal Precoce por Streptococcus agalactiae (GBS)", 96.0, 1, "A", 0.0, "GVS-MS", 2022, "Profilaxia intraparto e tratamento neonatal"),
        ("Penicilina G cristalina",          "Sepse Neonatal Precoce por Streptococcus agalactiae (GBS)", 97.0, 1, "A", 0.0, "GVS-MS", 2022, "Alternativa à ampicilina; preferida em infecções graves"),
        ("Ceftriaxona",                      "Meningite Neonatal por Streptococcus agalactiae (GBS)",     95.0, 1, "A", 0.0, "PCDT-MENIN", 2023, "Meningite neonatal por GBS"),
    ],

    "Staphylococcus aureus": [
        ("Oxacilina",                        "Endocardite Infecciosa por Staphylococcus aureus",   92.0, 1, "A",  0.0, "GVS-MS",      2022, "MSSA; 6 semanas IV para endocardite valva nativa"),
        ("Cefazolina",                       "Endocardite Infecciosa por Staphylococcus aureus",   90.0, 1, "A",  0.0, "GVS-MS",      2022, "Alternativa à oxacilina para MSSA"),
        ("Vancomicina",                      "Endocardite Infecciosa por Staphylococcus aureus",   78.0, 2, "A",  0.0, "GVS-MS",      2022, "MRSA ou alergia grave à penicilina"),
        ("Daptomicina",                      "Endocardite Infecciosa por Staphylococcus aureus",   84.0, 2, "A",  0.0, "GVS-MS",      2022, "MRSA; preferida em bacteremia por S. aureus"),
        ("Cefalexina",                       "Impetigo – Staphylococcus aureus / Streptococcus pyogenes", 89.0, 1, "A", 0.0, "GVS-MS", 2022, "Impetigo não-bolhoso leve"),
        ("Clindamicina",                     "Furunculose / Carbúnculo – Staphylococcus aureus",   82.0, 2, "B", 20.0, "GVS-MS",      2022, "CA-MRSA oral; checar resistência induzível"),
        ("Sulfametoxazol-trimetoprima (SMX-TMP)", "Furunculose / Carbúnculo – Staphylococcus aureus", 85.0, 2, "B", 10.0, "ANVISA-SCIH", 2023, "CA-MRSA oral; boa penetração cutânea"),
        ("Oxacilina",                        "Osteomielite Hematogênica – Staphylococcus aureus",  90.0, 1, "A",  0.0, "GVS-MS",      2022, "MSSA; 4-6 semanas"),
        ("Vancomicina",                      "Osteomielite Hematogênica – Staphylococcus aureus",  80.0, 2, "A",  0.0, "GVS-MS",      2022, "MRSA ou falha de oxacilina"),
        ("Cefazolina",                       "Infecção de Sítio Cirúrgico (ISC)",                  92.0, 1, "A",  0.0, "ANVISA-SCIH", 2023, "Profilaxia cirúrgica padrão em cirurgias limpas"),
    ],

    "Staphylococcus aureus resistente à meticilina (MRSA)": [
        ("Vancomicina",                      "Bacteremia por S. aureus MRSA Hospitalar (HA-MRSA)", 75.0, 1, "A",  0.0, "ANVISA-SCIH", 2023, "Alvo de AUC/MIC 400-600; monitoramento de nível sérico"),
        ("Daptomicina",                      "Bacteremia por S. aureus MRSA Hospitalar (HA-MRSA)", 83.0, 1, "A",  0.0, "ANVISA-SCIH", 2023, "Preferida em bacteremia e endocardite por MRSA"),
        ("Linezolida",                       "Bacteremia por S. aureus MRSA Hospitalar (HA-MRSA)", 80.0, 2, "A",  0.5, "ANVISA-SCIH", 2023, "Pneumonia por MRSA; inferior à vancomicina em bacteremia"),
        ("Ceftaroline",                      "Bacteremia por S. aureus MRSA Hospitalar (HA-MRSA)", 82.0, 2, "B",  0.0, "ANVISA-SCIH", 2023, "Alternativa emergente em MRSA com CIM elevada à vancomicina"),
        ("Sulfametoxazol-trimetoprima (SMX-TMP)", "Infecção por MRSA Comunitário (CA-MRSA)",      86.0, 1, "A", 10.0, "ANVISA-SCIH", 2023, "Infecções cutâneas CA-MRSA; oral"),
        ("Clindamicina",                     "Infecção por MRSA Comunitário (CA-MRSA)",            82.0, 1, "B", 20.0, "ANVISA-SCIH", 2023, "Testar resistência D-teste antes de usar"),
        ("Dalbavancina",                     None,                                                  88.0, 2, "A",  0.0, "ANVISA-SCIH", 2023, "Dose única semanal; alta adesão ambulatorial"),
        ("Tedizolida",                       None,                                                  85.0, 2, "B",  0.5, "ANVISA-SCIH", 2023, "Menor mielossupressão que linezolida"),
    ],

    "Escherichia coli": [
        ("Nitrofurantoína",                  "Cistite Não Complicada – Escherichia coli",          91.0, 1, "A",  5.0, "SBI-ITU",     2020, "ITU baixa não complicada; 5-7 dias"),
        ("Fosfomicina",                      "Cistite Não Complicada – Escherichia coli",          89.0, 1, "A",  8.0, "SBI-ITU",     2020, "Dose única 3g; ESBL sensível em muitos casos"),
        ("Sulfametoxazol-trimetoprima (SMX-TMP)", "Cistite Não Complicada – Escherichia coli",    78.0, 2, "A", 22.0, "SBI-ITU",     2020, "Usar somente com antibiograma; resistência 20-30% no Brasil"),
        ("Ciprofloxacino",                   "Cistite Não Complicada – Escherichia coli",          82.0, 2, "A", 18.0, "SBI-ITU",     2020, "Evitar 1ª linha para ITU não complicada – preservar para outras indicações"),
        ("Ceftriaxona",                      "Pielonefrite Aguda – Escherichia coli",              93.0, 1, "A",  8.0, "SBI-ITU",     2020, "Pielonefrite hospitalizada; aguardar antibiograma"),
        ("Ertapenem",                        "Pielonefrite Aguda – Escherichia coli",              97.0, 2, "A",  2.0, "SBI-ITU",     2020, "ESBL confirmado; ambulatorial com 1x/dia IM"),
        ("Meropenem",                        "Sepse por Gram-negativos (bacteremia primária)",     96.0, 1, "A",  4.0, "SBI-SEPSE",   2021, "Sepse grave por E. coli, especialmente ESBL"),
        ("Ampicilina",                       "Meningite Neonatal por Streptococcus agalactiae (GBS)", 88.0, 1, "A", 40.0, "PCDT-MENIN", 2023, "Sepse/meningite neonatal E. coli; atenção resistência ampicilina"),
    ],

    "Klebsiella pneumoniae": [
        ("Ertapenem",                        "ITU Complicada – Klebsiella pneumoniae",             94.0, 1, "A",  5.0, "SBI-ITU",     2020, "ESBL confirmado; boa opção ambulatorial"),
        ("Meropenem",                        "ITU Complicada – Klebsiella pneumoniae",             96.0, 1, "A",  5.0, "SBI-ITU",     2020, "Infecções graves por K. pneumoniae ESBL"),
        ("Ceftriaxona",                      "ITU Complicada – Klebsiella pneumoniae",             72.0, 2, "B", 28.0, "SBI-ITU",     2020, "Apenas com sensibilidade confirmada"),
        ("Polimixina B",                     "Sepse por Klebsiella pneumoniae KPC",                65.0, 1, "C",  0.0, "ANVISA-IRAS", 2023, "KPC; geralmente em combinação; nefrotoxicidade frequente"),
        ("Ceftazidima-avibactam",            "Sepse por Klebsiella pneumoniae KPC",                85.0, 1, "B",  5.0, "ANVISA-IRAS", 2023, "Preferida em KPC; melhor sobrevida que polimixina isolada"),
        ("Meropenem",                        "Sepse por Klebsiella pneumoniae KPC",                45.0, 2, "C",  0.0, "ANVISA-IRAS", 2023, "KPC: apenas em dose alta com AUC otimizado ou em combo"),
        ("Tigeciclina",                      "Sepse por Klebsiella pneumoniae KPC",                60.0, 2, "C",  5.0, "ANVISA-IRAS", 2023, "Combinação em KPC; monobacteremia tem baixa confiabilidade"),
    ],

    "Klebsiella pneumoniae produtora de carbapenemase (KPC)": [
        ("Ceftazidima-avibactam",            None, 83.0, 1, "B",  6.0, "ANVISA-IRAS", 2023, "Tratamento de escolha para KPC no Brasil"),
        ("Polimixina B",                     None, 62.0, 1, "C",  0.0, "ANVISA-IRAS", 2023, "Usar em combinação; monitorar função renal"),
        ("Meropenem",                        None, 40.0, 2, "C",  0.0, "ANVISA-IRAS", 2023, "Apenas doses estendidas + combinação; CIM ≤8 mg/L"),
        ("Tigeciclina",                      None, 58.0, 2, "C",  3.0, "ANVISA-IRAS", 2023, "Auxiliar em combo; não usar como monoterapia em bacteremia"),
        ("Ceftolozano-tazobactam",           None, 15.0, 3, "C",  0.0, "ANVISA-IRAS", 2023, "Sem atividade em KPC; mencionar apenas para pseudomonas"),
    ],

    "Pseudomonas aeruginosa": [
        ("Piperacilina-tazobactam",          "Pneumonia Hospitalar / Associada à Ventilação Mecânica (VAP)", 78.0, 1, "A", 20.0, "ANVISA-IRAS", 2023, "PAC-S Pseudomonas; infusão estendida melhora desfecho"),
        ("Cefepima",                         "Pneumonia Hospitalar / Associada à Ventilação Mecânica (VAP)", 80.0, 1, "A", 18.0, "ANVISA-IRAS", 2023, "Alternativa ao piperacilina-tazobactam"),
        ("Meropenem",                        "Pneumonia Hospitalar / Associada à Ventilação Mecânica (VAP)", 82.0, 1, "A", 15.0, "ANVISA-IRAS", 2023, "Preferido em suspeita de resistência"),
        ("Ciprofloxacino",                   None,                                                   74.0, 2, "A", 25.0, "ANVISA-IRAS", 2023, "Resistência crescente no Brasil (~25%)"),
        ("Ceftazidima",                      None,                                                   77.0, 1, "A", 20.0, "ANVISA-IRAS", 2023, "Boa atividade antipseudomonas"),
        ("Polimixina B",                     "Infecção por Pseudomonas aeruginosa MDR",              65.0, 1, "C",  5.0, "ANVISA-IRAS", 2023, "MDR/XDR Pseudomonas; sempre em combinação"),
        ("Ceftolozano-tazobactam",           "Infecção por Pseudomonas aeruginosa MDR",              80.0, 1, "B",  5.0, "ANVISA-IRAS", 2023, "MDR Pseudomonas; melhor opção atual para cepas MDR"),
        ("Aztreonam",                        None,                                                   72.0, 2, "B", 20.0, "ANVISA-IRAS", 2023, "Alternativa em alergia a carbapenens"),
    ],

    "Acinetobacter baumannii": [
        ("Polimixina B",                     "Infecção por Acinetobacter baumannii Resistente a Carbapenens (CRAB)", 60.0, 1, "C", 0.0, "ANVISA-IRAS", 2023, "CRAB; sempre em combinação"),
        ("Colistina (Polimixina E)",         "Infecção por Acinetobacter baumannii Resistente a Carbapenens (CRAB)", 58.0, 1, "C", 0.0, "ANVISA-IRAS", 2023, "Alternativa à polimixina B"),
        ("Ampicilina-sulbactam",             "Infecção por Acinetobacter baumannii Resistente a Carbapenens (CRAB)", 55.0, 2, "C", 0.0, "ANVISA-IRAS", 2023, "Apenas cepas sensíveis ao sulbactam; doses altas"),
        ("Tigeciclina",                      "Infecção por Acinetobacter baumannii Resistente a Carbapenens (CRAB)", 52.0, 2, "C", 5.0, "ANVISA-IRAS", 2023, "Auxiliar em combo; sem indicação como monoterapia"),
        ("Meropenem",                        "Infecção por Acinetobacter baumannii Resistente a Carbapenens (CRAB)", 35.0, 2, "C", 0.0, "ANVISA-IRAS", 2023, "Apenas com CIM ≤4 e doses altas estendidas"),
        ("Minociclina",                      None,                                                   58.0, 2, "C", 10.0, "ANVISA-IRAS", 2023, "Cepas sensíveis; combinar com polimixina"),
    ],

    "Neisseria meningitidis": [
        ("Penicilina G cristalina",          "Meningite Bacteriana por Neisseria meningitidis",    95.0, 1, "A",  5.0, "PCDT-MENIN",  2023, "Sensibilidade preservada na maioria dos isolados brasileiros"),
        ("Ceftriaxona",                      "Meningite Bacteriana por Neisseria meningitidis",    97.0, 1, "A",  1.0, "PCDT-MENIN",  2023, "Tratamento de escolha atual no Brasil"),
        ("Rifampicina",                      "Meningite Bacteriana por Neisseria meningitidis",    98.0, 1, "A",  0.0, "PCDT-MENIN",  2023, "Quimioprofilaxia de contatos; 2 dias"),
        ("Ciprofloxacino",                   "Meningite Bacteriana por Neisseria meningitidis",    98.0, 1, "A",  0.0, "PCDT-MENIN",  2023, "Quimioprofilaxia dose única adultos"),
        ("Cloranfenicol",                    "Meningite Bacteriana por Neisseria meningitidis",    88.0, 2, "A",  2.0, "PCDT-MENIN",  2023, "Alternativa histórica; preferido em crianças se alergia"),
    ],

    "Neisseria gonorrhoeae": [
        ("Ceftriaxona",                      "Gonorreia (Neisseria gonorrhoeae)",                  98.0, 1, "A",  3.0, "PCDT-IST",    2022, "500mg IM dose única; padrão atual no Brasil"),
        ("Azitromicina",                     "Gonorreia (Neisseria gonorrhoeae)",                  65.0, 2, "B", 35.0, "PCDT-IST",    2022, "Resistência crescente; usar apenas em combo com ceftriaxona"),
        ("Ciprofloxacino",                   "Gonorreia (Neisseria gonorrhoeae)",                  45.0, 3, "B", 55.0, "PCDT-IST",    2022, "Alta resistência no Brasil; NÃO usar como 1ª linha"),
        ("Cefixima",                         "Gonorreia (Neisseria gonorrhoeae)",                  90.0, 2, "A",  8.0, "PCDT-IST",    2022, "Opcao oral quando IM nao disponivel; 800mg dose unica"),
    ],

    "Salmonella Typhi": [
        ("Ceftriaxona",                      "Febre Tifoide",                                      95.0, 1, "A",  5.0, "PCDT-FEBRETIFO", 2022, "Formas graves; 7-14 dias"),
        ("Azitromicina",                     "Febre Tifoide",                                      92.0, 1, "A",  8.0, "PCDT-FEBRETIFO", 2022, "Formas não complicadas; 5-7 dias"),
        ("Ciprofloxacino",                   "Febre Tifoide",                                      75.0, 2, "A", 30.0, "PCDT-FEBRETIFO", 2022, "Resistência crescente às quinolonas; usar com antibiograma"),
        ("Cloranfenicol",                    "Febre Tifoide",                                      85.0, 2, "B", 10.0, "PCDT-FEBRETIFO", 2022, "Histórico; ainda usado em áreas com escassez de recursos"),
    ],

    "Salmonella spp. (não-tíficas)": [
        ("Ciprofloxacino",                   "Gastroenterite por Salmonella não-tífica",           85.0, 1, "A", 18.0, "GVS-MS",      2022, "Formas invasivas ou graves; não tratar gastroenterite leve"),
        ("Ceftriaxona",                      "Gastroenterite por Salmonella não-tífica",           92.0, 1, "A",  5.0, "GVS-MS",      2022, "Bacteremia / formas invasivas"),
        ("Azitromicina",                     "Gastroenterite por Salmonella não-tífica",           88.0, 2, "B",  8.0, "GVS-MS",      2022, "Alternativa oral para formas invasivas"),
    ],

    "Campylobacter jejuni": [
        ("Azitromicina",                     "Gastroenterite por Campylobacter jejuni",            90.0, 1, "A", 15.0, "GVS-MS",      2022, "Tratamento de escolha; 3-5 dias"),
        ("Eritromicina",                     "Gastroenterite por Campylobacter jejuni",            88.0, 1, "A", 15.0, "GVS-MS",      2022, "Alternativa à azitromicina; 5 dias"),
        ("Ciprofloxacino",                   "Gastroenterite por Campylobacter jejuni",            55.0, 2, "A", 45.0, "GVS-MS",      2022, "Resistência >40% no Brasil; evitar"),
        ("Doxiciclina",                      "Gastroenterite por Campylobacter jejuni",            80.0, 2, "B", 15.0, "GVS-MS",      2022, "Alternativa; adultos > 8 anos"),
    ],

    "Helicobacter pylori": [
        ("Amoxicilina",                      "Infecção por Helicobacter pylori / Gastrite Crônica Ativa", 92.0, 1, "A",  2.0, "GVS-MS", 2022, "Componente do esquema triplo; associar inibidor de bomba"),
        ("Claritromicina",                   "Infecção por Helicobacter pylori / Gastrite Crônica Ativa", 75.0, 1, "A", 25.0, "GVS-MS", 2022, "Resistência de ~25% no Brasil; teste de sensibilidade ideal"),
        ("Metronidazol",                     "Infecção por Helicobacter pylori / Gastrite Crônica Ativa", 68.0, 2, "A", 35.0, "GVS-MS", 2022, "Alta resistência; usar em terapia quádrupla bismuto"),
        ("Levofloxacino",                    "Infecção por Helicobacter pylori / Gastrite Crônica Ativa", 80.0, 2, "A", 20.0, "GVS-MS", 2022, "Esquema resgate com levofloxacino"),
        ("Rifampicina",                      "Infecção por Helicobacter pylori / Gastrite Crônica Ativa", 85.0, 3, "B",  5.0, "GVS-MS", 2022, "Rifabutina em esquemas de 3ª linha para cepas MDR"),
        ("Tetraciclina",                     "Infecção por Helicobacter pylori / Gastrite Crônica Ativa", 87.0, 2, "A",  5.0, "GVS-MS", 2022, "Terapia quádrupla com bismuto (Pylera ou PBMT)"),
    ],

    "Clostridioides difficile": [
        ("Vancomicina",                      "Infecção por Clostridioides difficile (CDI)",        91.0, 1, "A",  0.5, "ANVISA-IRAS", 2023, "Oral 125mg 4x/dia 10 dias; preferida sobre metronidazol"),
        ("Fidaxomicina",                     "Infecção por Clostridioides difficile (CDI)",        93.0, 1, "A",  0.5, "ANVISA-IRAS", 2023, "Superior em prevenir recorrência; custo elevado"),
        ("Metronidazol",                     "Infecção por Clostridioides difficile (CDI)",        78.0, 2, "A",  0.0, "ANVISA-IRAS", 2023, "Formas leves apenas; não usar para graves"),
    ],

    "Treponema pallidum": [
        ("Penicilina G benzatina",           "Sífilis (adquirida, primária a terciária)",          99.0, 1, "A",  0.0, "PCDT-IST",    2022, "Não há resistência documentada à penicilina"),
        ("Penicilina G benzatina",           "Sífilis Congênita",                                  98.0, 1, "A",  0.0, "PCDT-IST",    2022, "50.000 UI/kg IM 3 doses semanais (congênita tardia) ou IV (precoce)"),
        ("Penicilina G cristalina",          "Sífilis (adquirida, primária a terciária)",          99.0, 1, "A",  0.0, "PCDT-IST",    2022, "Neurossífilis: 18-24 M UI/dia IV por 14 dias"),
        ("Doxiciclina",                      "Sífilis (adquirida, primária a terciária)",          91.0, 2, "B",  0.0, "PCDT-IST",    2022, "Alergia à penicilina (exceto gestantes e crianças)"),
        ("Azitromicina",                     "Sífilis (adquirida, primária a terciária)",          70.0, 3, "C", 15.0, "PCDT-IST",    2022, "NÃO recomendada no Brasil; resistência documentada"),
    ],

    "Chlamydia trachomatis": [
        ("Azitromicina",                     "Infecção por Chlamydia trachomatis",                 96.0, 1, "A",  2.0, "PCDT-IST",    2022, "Dose única 1g oral; padrão no Brasil"),
        ("Doxiciclina",                      "Infecção por Chlamydia trachomatis",                 97.0, 1, "A",  2.0, "PCDT-IST",    2022, "100mg 2x/dia 7 dias; superior para LGV"),
        ("Doxiciclina",                      "Linfogranuloma Venéreo (Chlamydia trachomatis L1-L3)", 96.0, 1, "A", 2.0, "PCDT-IST", 2022, "21 dias para LGV"),
        ("Azitromicina",                     "Tracoma (Chlamydia trachomatis ocular)",             94.0, 1, "A",  2.0, "GVS-MS",      2022, "Dose única oral; estratégia SAFE da OMS"),
        ("Eritromicina",                     "Infecção por Chlamydia trachomatis",                 90.0, 2, "A",  2.0, "PCDT-IST",    2022, "Gestantes; alternativa à azitromicina"),
    ],

    "Chlamydophila pneumoniae": [
        ("Azitromicina",                     "Pneumonia Atípica – Chlamydophila pneumoniae",       91.0, 1, "A",  2.0, "SBI-PNEUM",   2018, "5 dias"),
        ("Doxiciclina",                      "Pneumonia Atípica – Chlamydophila pneumoniae",       90.0, 1, "A",  2.0, "SBI-PNEUM",   2018, "10-14 dias"),
        ("Levofloxacino",                    "Pneumonia Atípica – Chlamydophila pneumoniae",       93.0, 2, "A",  2.0, "SBI-PNEUM",   2018, "5 dias; PAC grave"),
    ],

    "Mycoplasma pneumoniae": [
        ("Azitromicina",                     "Pneumonia Atípica – Mycoplasma pneumoniae",          88.0, 1, "A",  5.0, "SBI-PNEUM",   2018, "Tratamento de escolha"),
        ("Doxiciclina",                      "Pneumonia Atípica – Mycoplasma pneumoniae",          87.0, 1, "A",  3.0, "SBI-PNEUM",   2018, "Alternativa; adultos"),
        ("Levofloxacino",                    "Pneumonia Atípica – Mycoplasma pneumoniae",          92.0, 2, "A",  2.0, "SBI-PNEUM",   2018, "PAC grave ou falha"),
    ],

    "Mycobacterium tuberculosis": [
        ("Isoniazida (INH)",                 "Tuberculose Pulmonar",                               98.0, 1, "A",  7.0, "PCDT-TB",     2022, "Esquema RHZE fase intensiva; monitorar hepatotoxicidade"),
        ("Rifampicina",                      "Tuberculose Pulmonar",                               98.0, 1, "A",  7.0, "PCDT-TB",     2022, "Componente central do esquema básico; interações medicamentosas"),
        ("Pirazinamida",                     "Tuberculose Pulmonar",                               96.0, 1, "A",  5.0, "PCDT-TB",     2022, "Fase intensiva 2 meses; esterilizante de bacilos em pH ácido"),
        ("Etambutol",                        "Tuberculose Pulmonar",                               95.0, 1, "A",  5.0, "PCDT-TB",     2022, "Previne resistência na fase intensiva"),
        ("Isoniazida (INH)",                 "Tuberculose Extra-pulmonar",                         97.0, 1, "A",  7.0, "PCDT-TB",     2022, "Mesmo esquema RHZE; duração varia conforme localização"),
        ("Rifampicina",                      "Tuberculose Extra-pulmonar",                         97.0, 1, "A",  7.0, "PCDT-TB",     2022, "TB meníngea: 12 meses total"),
        ("Levofloxacino",                    "Tuberculose Resistente (MDR/XDR-TB)",                80.0, 1, "A", None, "PCDT-TB",     2022, "Componente central do esquema MDR; preferir vs moxifloxacino"),
        ("Linezolida",                       "Tuberculose Resistente (MDR/XDR-TB)",                78.0, 1, "A", None, "PCDT-TB",     2022, "MDR/XDR-TB; mielossupressão limitante"),
        ("Amicacina",                        "Tuberculose Resistente (MDR/XDR-TB)",                75.0, 2, "A", None, "PCDT-TB",     2022, "TB MDR injetável; menos usado com novos agentes"),
    ],

    "Mycobacterium leprae": [
        ("Rifampicina",                      "Hanseníase (Lepra)",                                 99.0, 1, "A",  0.0, "PCDT-HANSENR", 2022, "Componente PQT mensal supervisionado"),
        ("Dapsona",                          "Hanseníase (Lepra)",                                 95.0, 1, "A",  5.0, "PCDT-HANSENR", 2022, "Diário autoadministrado no esquema PQT"),
        ("Clofazimina",                      "Hanseníase (Lepra)",                                 95.0, 1, "A",  0.0, "PCDT-HANSENR", 2022, "MB: mensal supervisionado + diário autoadmin; anti-inflamatório"),
        ("Ofloxacino",                       "Hanseníase (Lepra)",                                 85.0, 2, "B",  0.0, "PCDT-HANSENR", 2022, "Esquema ROM para PB dose unica"),
        ("Minociclina",                      "Hanseníase (Lepra)",                                 83.0, 2, "B",  0.0, "PCDT-HANSENR", 2022, "Esquema ROM para casos especiais"),
    ],

    "Rickettsia rickettsii": [
        ("Doxiciclina",                      "Febre Maculosa Brasileira (Rickettsia rickettsii)",  97.0, 1, "A",  0.0, "PCDT-RICKETTSIA", 2022, "Iniciar imediatamente na suspeita; não aguardar confirmação"),
        ("Cloranfenicol",                    "Febre Maculosa Brasileira (Rickettsia rickettsii)",  91.0, 2, "A",  0.0, "PCDT-RICKETTSIA", 2022, "Crianças < 8 anos ou gravidez quando doxiciclina contraindicada"),
    ],

    "Rickettsia spp.": [
        ("Doxiciclina",                      "Rickettsioses (outras espécies)",                    96.0, 1, "A",  0.0, "PCDT-RICKETTSIA", 2022, "Padrão para todas as rickettsioses"),
        ("Cloranfenicol",                    "Rickettsioses (outras espécies)",                    90.0, 2, "A",  0.0, "PCDT-RICKETTSIA", 2022, "Alternativa pediátrica"),
    ],

    "Leptospira interrogans": [
        ("Penicilina G cristalina",          "Leptospirose",                                       90.0, 1, "A",  0.0, "PCDT-LEPTO",  2019, "Formas graves (Weil); 7 dias IV"),
        ("Ampicilina",                       "Leptospirose",                                       88.0, 1, "A",  0.0, "PCDT-LEPTO",  2019, "Alternativa à penicilina nas formas graves"),
        ("Doxiciclina",                      "Leptospirose",                                       92.0, 1, "A",  0.0, "PCDT-LEPTO",  2019, "Formas leves-moderadas oral; quimioprofilaxia pós-exposição"),
        ("Ceftriaxona",                      "Leptospirose",                                       91.0, 2, "A",  0.0, "PCDT-LEPTO",  2019, "Alternativa para formas graves"),
    ],

    "Brucella spp.": [
        ("Doxiciclina",                      "Brucelose",                                          91.0, 1, "A",  0.0, "PCDT-BRUCELOSE", 2022, "Associar com rifampicina ou estreptomicina por 6 semanas"),
        ("Rifampicina",                      "Brucelose",                                          88.0, 1, "A",  0.0, "PCDT-BRUCELOSE", 2022, "Combinação com doxiciclina padrão OMS"),
        ("Estreptomicina",                   "Brucelose",                                          89.0, 1, "A",  0.0, "PCDT-BRUCELOSE", 2022, "Associar doxiciclina; preferida em formas graves"),
        ("Sulfametoxazol-trimetoprima (SMX-TMP)", "Brucelose",                                     82.0, 2, "B",  0.0, "PCDT-BRUCELOSE", 2022, "Crianças < 8 anos; combinação com rifampicina"),
    ],

    "Bordetella pertussis": [
        ("Azitromicina",                     "Coqueluche (Pertussis)",                             95.0, 1, "A",  0.0, "PCDT-COQUELUCHE", 2023, "Tratamento e quimioprofilaxia; 5 dias"),
        ("Claritromicina",                   "Coqueluche (Pertussis)",                             92.0, 2, "A",  0.0, "PCDT-COQUELUCHE", 2023, "Alternativa; 7 dias"),
        ("Eritromicina",                     "Coqueluche (Pertussis)",                             88.0, 2, "A",  0.0, "PCDT-COQUELUCHE", 2023, "Clássico; 14 dias; menos tolerado que azitromicina"),
        ("Sulfametoxazol-trimetoprima (SMX-TMP)", "Coqueluche (Pertussis)",                        85.0, 2, "B",  0.0, "PCDT-COQUELUCHE", 2023, "Alternativa em alergia a macrólidos"),
    ],

    "Corynebacterium diphtheriae": [
        ("Penicilina G cristalina",          "Difteria",                                           93.0, 1, "A",  0.0, "PCDT-DIFTERIA", 2022, "Erradicação do bacilo; soro antidiftérico é o principal"),
        ("Eritromicina",                     "Difteria",                                           91.0, 1, "A",  0.0, "PCDT-DIFTERIA", 2022, "Alternativa à penicilina; 14 dias"),
    ],

    "Clostridium tetani": [
        ("Metronidazol",                     "Tétano Acidental",                                   92.0, 1, "A",  0.0, "PCDT-TETANO", 2022, "Erradicação de C. tetani na ferida; desbridamento essencial"),
        ("Penicilina G cristalina",          "Tétano Acidental",                                   89.0, 2, "A",  0.0, "PCDT-TETANO", 2022, "Alternativa histórica ao metronidazol"),
        ("Metronidazol",                     "Tétano Neonatal",                                    90.0, 1, "A",  0.0, "PCDT-TETANO", 2022, "Tétano neonatal; cuidados de suporte são fundamentais"),
    ],

    "Vibrio cholerae": [
        ("Doxiciclina",                      "Cólera",                                             94.0, 1, "A",  5.0, "PCDT-COLERA", 2022, "Dose única 300mg adultos; reduz duração e carga bacteriana"),
        ("Azitromicina",                     "Cólera",                                             92.0, 1, "A",  5.0, "PCDT-COLERA", 2022, "Preferida em crianças e gestantes"),
        ("Ciprofloxacino",                   "Cólera",                                             90.0, 2, "A", 10.0, "PCDT-COLERA", 2022, "Alternativa adultos; resistência emergindo"),
        ("Sulfametoxazol-trimetoprima (SMX-TMP)", "Cólera",                                        75.0, 3, "B", 30.0, "PCDT-COLERA", 2022, "Alta resistência; evitar em surtos"),
    ],

    "Listeria monocytogenes": [
        ("Ampicilina",                       "Meningite por Listeria monocytogenes",               92.0, 1, "A",  0.0, "PCDT-MENIN",  2023, "Sempre associar gentamicina por sinergismo"),
        ("Ampicilina",                       "Listeriose em Adultos Imunocomprometidos",           91.0, 1, "A",  0.0, "GVS-MS",      2022, "Gentamicina em combinação por 2 semanas"),
        ("Ampicilina",                       "Listeriose Neonatal",                                93.0, 1, "A",  0.0, "GVS-MS",      2022, "Ampicilina + gentamicina em neonatos"),
        ("Sulfametoxazol-trimetoprima (SMX-TMP)", "Listeriose em Adultos Imunocomprometidos",     88.0, 2, "B",  0.0, "GVS-MS",      2022, "Alternativa em alergia à penicilina"),
    ],

    "Enterococcus faecalis": [
        ("Ampicilina",                       "ITU por Enterococcus spp.",                          88.0, 1, "A", 15.0, "SBI-ITU",     2020, "E. faecalis geralmente sensível à ampicilina"),
        ("Nitrofurantoína",                  "ITU por Enterococcus spp.",                          82.0, 1, "A",  5.0, "SBI-ITU",     2020, "ITU baixa por Enterococcus"),
        ("Vancomicina",                      "Endocardite por Enterococcus",                       80.0, 1, "A",  8.0, "GVS-MS",      2022, "Associar aminoglicosídeo se sensível"),
        ("Ampicilina",                       "Endocardite por Enterococcus",                       85.0, 1, "A", 15.0, "GVS-MS",      2022, "E. faecalis: ampicilina + ceftriaxona (sinergia, sem oto/nefrotoxicidade)"),
    ],

    "Enterococcus faecium": [
        ("Linezolida",                       "Infecção de Corrente Sanguínea por Enterococcus Vancomicina-Resistente (VRE)", 85.0, 1, "A", 0.0, "ANVISA-IRAS", 2023, "VRE; sem bactericida"),
        ("Daptomicina",                      "Infecção de Corrente Sanguínea por Enterococcus Vancomicina-Resistente (VRE)", 80.0, 1, "A", 5.0, "ANVISA-IRAS", 2023, "VRE endocardite/bacteremia; doses altas"),
        ("Tigeciclina",                      "Infecção de Corrente Sanguínea por Enterococcus Vancomicina-Resistente (VRE)", 70.0, 2, "C", 3.0, "ANVISA-IRAS", 2023, "Auxiliar em combo; não como monoterapia para bacteremia"),
    ],

    "Yersinia pestis": [
        ("Estreptomicina",                   "Peste Bubônica (Yersinia pestis)",                   97.0, 1, "A",  0.0, "GVS-MS",      2022, "Tratamento clássico da peste; 10 dias IM"),
        ("Doxiciclina",                      "Peste Bubônica (Yersinia pestis)",                   93.0, 1, "A",  0.0, "GVS-MS",      2022, "Alternativa oral; profilaxia de contatos"),
        ("Gentamicina",                      "Peste Bubônica (Yersinia pestis)",                   94.0, 1, "A",  0.0, "GVS-MS",      2022, "Alternativa à estreptomicina IV"),
        ("Ciprofloxacino",                   "Peste Bubônica (Yersinia pestis)",                   91.0, 2, "A",  0.0, "GVS-MS",      2022, "Opção oral alternativa"),
    ],

    "Bacteroides fragilis": [
        ("Metronidazol",                     "Peritonite Bacteriana Primária (Espontânea)",        94.0, 1, "A",  5.0, "GVS-MS",      2022, "Cobertura anaeróbia obrigatória; associar a gram-negativo"),
        ("Piperacilina-tazobactam",          "Apendicite Bacteriana Secundária",                   92.0, 1, "A",  5.0, "GVS-MS",      2022, "Cobertura mista gram-negativos e anaeróbios"),
        ("Meropenem",                        "Abscesso Hepático Bacteriano",                       95.0, 1, "A",  3.0, "GVS-MS",      2022, "Formas graves; cobertura ampla"),
        ("Clindamicina",                     "Abscesso Pulmonar Bacteriano",                       88.0, 1, "A", 10.0, "GVS-MS",      2022, "Cobertura anaeróbia; boa penetração pulmonar"),
    ],

    "Haemophilus ducreyi": [
        ("Azitromicina",                     "Cancro Mole (Haemophilus ducreyi)",                  96.0, 1, "A",  0.0, "PCDT-IST",    2022, "Dose única 1g oral; padrão BR"),
        ("Ceftriaxona",                      "Cancro Mole (Haemophilus ducreyi)",                  97.0, 1, "A",  0.0, "PCDT-IST",    2022, "Dose única 250mg IM"),
        ("Ciprofloxacino",                   "Cancro Mole (Haemophilus ducreyi)",                  90.0, 2, "A",  5.0, "PCDT-IST",    2022, "3 dias oral"),
        ("Eritromicina",                     "Cancro Mole (Haemophilus ducreyi)",                  88.0, 2, "A",  0.0, "PCDT-IST",    2022, "7 dias; maior esquema"),
    ],

    "Bartonella henselae": [
        ("Azitromicina",                     "Bartonellose (Doença da Arranhadura do Gato)",       87.0, 1, "A",  0.0, "GVS-MS",      2022, "Linfadenopatia simples; 5 dias"),
        ("Doxiciclina",                      "Bartonellose (Doença da Arranhadura do Gato)",       85.0, 2, "A",  0.0, "GVS-MS",      2022, "Formas sistêmicas; angiomatose bacilar em HIV"),
        ("Eritromicina",                     "Bartonellose (Doença da Arranhadura do Gato)",       82.0, 2, "B",  0.0, "GVS-MS",      2022, "Angiomatose bacilar"),
    ],

    "Staphylococcus saprophyticus": [
        ("Nitrofurantoína",                  "Staphylococcus saprophyticus – ITU em Mulheres Jovens", 93.0, 1, "A", 0.0, "SBI-ITU",  2020, "5 dias; excelente cobertura"),
        ("Cefalexina",                       "Staphylococcus saprophyticus – ITU em Mulheres Jovens", 91.0, 1, "A", 0.0, "SBI-ITU",  2020, "7 dias"),
        ("Sulfametoxazol-trimetoprima (SMX-TMP)", "Staphylococcus saprophyticus – ITU em Mulheres Jovens", 85.0, 2, "A", 5.0, "SBI-ITU", 2020, "Verificar sensibilidade local"),
    ],

    "Nocardia spp.": [
        ("Sulfametoxazol-trimetoprima (SMX-TMP)", "Nocardiose (Nocardia spp.)",                    87.0, 1, "A",  5.0, "GVS-MS",      2022, "Tratamento de escolha; longa duração (6-12 meses)"),
        ("Amicacina",                        "Nocardiose (Nocardia spp.)",                          80.0, 2, "B",  5.0, "GVS-MS",      2022, "Formas graves; combinar com SMX-TMP e imipenem"),
        ("Imipenem-cilastatina",             "Nocardiose (Nocardia spp.)",                          82.0, 2, "B",  3.0, "GVS-MS",      2022, "Terapia inicial formas disseminadas"),
        ("Linezolida",                       "Nocardiose (Nocardia spp.)",                          85.0, 2, "B",  2.0, "GVS-MS",      2022, "Boa atividade; alternativa em resistência ao SMX"),
    ],

    "Actinomyces israelii": [
        ("Penicilina G cristalina",          "Actinomicose (Actinomyces israelii)",                95.0, 1, "A",  0.0, "GVS-MS",      2022, "Fase inicial IV; transição oral amoxicilina 6-12 meses"),
        ("Amoxicilina",                      "Actinomicose (Actinomyces israelii)",                93.0, 1, "A",  0.0, "GVS-MS",      2022, "Tratamento prolongado oral após fase IV"),
        ("Doxiciclina",                      "Actinomicose (Actinomyces israelii)",                85.0, 2, "B",  0.0, "GVS-MS",      2022, "Alergia à penicilina"),
        ("Eritromicina",                     "Actinomicose (Actinomyces israelii)",                83.0, 2, "B",  0.0, "GVS-MS",      2022, "Alternativa em alergia"),
    ],
}

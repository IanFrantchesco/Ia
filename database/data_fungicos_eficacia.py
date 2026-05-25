"""
Dados de eficácia de antifúngicos por fungo e patologia.
Baseado em: PCDT-PARACOC MS 2022, SBD, SBMT, SBI, GVS/MS 5ª ed. 2022,
            PCDT-HIV-FUNG, ANVISA-ANTIF, SVS-HISTOP, SVS-ESPORO, SVS-CRIPTO.

Formato:
fungo_nome_cientifico -> lista de:
  (antifungico_nome_generico, patologia_nome_parcial_ou_None,
   eficacia_pct, linha_tratamento, nivel_evidencia, resistencia_br_pct, fonte_sigla, ano, consideracoes)
"""

EFICACIA_FUNGICA = {

    # ══════════════════════════════════════════════════════════════════
    # PARACOCCIDIOIDES
    # ══════════════════════════════════════════════════════════════════
    "Paracoccidioides brasiliensis": [
        ("Itraconazol", "Paracoccidioidomicose (Blastomicose Sul-Americana)", 92.0, 1, "A", 2.0,
         "PCDT-PARACOC", 2022,
         "1ª linha para todas as formas: leve, moderada e grave; 200 mg/dia VO × 12-18 meses; "
         "excelente resposta nas formas crônicas; menor toxicidade que anfotericina B; "
         "monitorar função hepática; disponível no SUS (RENAME)"),

        ("Anfotericina B desoxicolato", "Paracoccidioidomicose (Blastomicose Sul-Americana)", 88.0, 1, "A", 0.5,
         "PCDT-PARACOC", 2022,
         "Formas graves e disseminadas, meningoparacoccidioidomicose ou falha de itraconazol; "
         "0,7-1,0 mg/kg/dia IV × 2-4 semanas (indução), depois transição para itraconazol; "
         "nefrotoxicidade dose-limitante — monitorar creatinina diariamente"),

        ("Sulfadiazina + Trimetoprima", "Paracoccidioidomicose (Blastomicose Sul-Americana)", 78.0, 2, "B", 3.0,
         "PCDT-PARACOC", 2022,
         "Alternativa de baixo custo; formas leves e moderadas; sulfadiazina 500 mg + trimetoprima 80 mg "
         "VO 12/12h × 24 meses; maior taxa de recidiva que itraconazol; opção em ausência de itraconazol"),

        ("Voriconazol", "Paracoccidioidomicose (Blastomicose Sul-Americana)", 85.0, 2, "B", 0.0,
         "PCDT-PARACOC", 2022,
         "Dados limitados — estudos de menor escala; usado em refratários ao itraconazol; "
         "200 mg VO 12/12h; sem registro formal de indicação no PCDT; disponibilidade restrita"),
    ],

    "Paracoccidioides lutzii": [
        ("Itraconazol", "Paracoccidioidomicose (Blastomicose Sul-Americana)", 88.0, 1, "A", 3.0,
         "PCDT-PARACOC", 2022,
         "P. lutzii tem perfil de sensibilidade similar ao P. brasiliensis; "
         "200 mg/dia × 12-18 meses; principal agente na Amazônia; resposta clínica geralmente boa"),

        ("Anfotericina B desoxicolato", "Paracoccidioidomicose (Blastomicose Sul-Americana)", 85.0, 1, "A", 0.0,
         "PCDT-PARACOC", 2022,
         "Formas graves; mesma indicação que para P. brasiliensis; indução IV seguida de itraconazol VO"),
    ],

    # ══════════════════════════════════════════════════════════════════
    # HISTOPLASMA
    # ══════════════════════════════════════════════════════════════════
    "Histoplasma capsulatum": [
        ("Itraconazol", "Histoplasmose (Doença de Darling)", 90.0, 1, "A", 2.0,
         "SVS-HISTOP", 2022,
         "1ª linha para histoplasmose leve-moderada e consolidação após anfotericina B; "
         "200 mg VO 12/12h × 3 dias de ataque, depois 200 mg/dia × 12 meses para disseminada; "
         "manutenção em HIV com CD4 < 150: 200 mg/dia indefinidamente até reconstituição imune"),

        ("Anfotericina B desoxicolato", "Histoplasmose (Doença de Darling)", 87.0, 1, "A", 0.0,
         "SVS-HISTOP", 2022,
         "Histoplasmose disseminada grave, meningite fúngica, falha de itraconazol, imunossuprimidos graves; "
         "0,7-1,0 mg/kg/dia IV × 2-4 semanas (indução); transição para itraconazol após estabilização"),

        ("Anfotericina B lipossomal", "Histoplasmose (Doença de Darling)", 90.0, 1, "A", 0.0,
         "SVS-HISTOP", 2022,
         "Preferida em insuficiência renal ou intolerância à formulação convencional; "
         "3 mg/kg/dia IV × 2 semanas; menor nefrotoxicidade; acesso via RENAME excepcional"),

        ("Fluconazol", "Histoplasmose (Doença de Darling)", 60.0, 2, "B", 5.0,
         "SVS-HISTOP", 2022,
         "Menor eficácia que itraconazol — CIM de fluconazol para H. capsulatum é elevada; "
         "usado apenas quando itraconazol indisponível; 400-800 mg/dia; menor taxa de cura"),
    ],

    # ══════════════════════════════════════════════════════════════════
    # CRYPTOCOCCUS
    # ══════════════════════════════════════════════════════════════════
    "Cryptococcus neoformans": [
        ("Anfotericina B desoxicolato", "Criptococose (Meningite Criptocócica e Forma Pulmonar)", 85.0, 1, "A", 1.0,
         "SBI-CRIPTO", 2022,
         "FASE DE INDUÇÃO (2 semanas): anfotericina B 0,7-1,0 mg/kg/dia IV + flucitosina 100 mg/kg/dia VO "
         "(combinação padrão-ouro); ou anfotericina B isolada se flucitosina indisponível; "
         "punções lombares repetidas para controle da PIC (pressão intracraniana) são fundamentais"),

        ("Flucitosina (5-FC)", "Criptococose (Meningite Criptocócica e Forma Pulmonar)", 90.0, 1, "A", 2.0,
         "SBI-CRIPTO", 2022,
         "SEMPRE em combinação com anfotericina B na indução (nunca em monoterapia — resistência rápida); "
         "100 mg/kg/dia VO dividido em 4 doses × 2 semanas; "
         "disponibilidade muito limitada no Brasil — importação excepcional; monitorar hemograma"),

        ("Fluconazol", "Criptococose (Meningite Criptocócica e Forma Pulmonar)", 88.0, 1, "A", 2.0,
         "SBI-CRIPTO", 2022,
         "FASE DE CONSOLIDAÇÃO (semanas 3-10): fluconazol 400 mg/dia VO × 8 semanas; "
         "FASE DE MANUTENÇÃO (profilaxia secundária): fluconazol 200 mg/dia indefinidamente em HIV "
         "até CD4 > 200 por > 6 meses; bem tolerado; amplamente disponível no SUS"),

        ("Anfotericina B lipossomal", "Criptococose (Meningite Criptocócica e Forma Pulmonar)", 88.0, 1, "A", 0.0,
         "SBI-CRIPTO", 2022,
         "Preferida em insuficiência renal; 3-4 mg/kg/dia IV × 2 semanas (indução); "
         "menor nefrotoxicidade; disponível via RENAME excepcional"),
    ],

    "Cryptococcus gattii": [
        ("Anfotericina B desoxicolato", "Criptococose (Meningite Criptocócica e Forma Pulmonar)", 82.0, 1, "A", 0.5,
         "SBI-CRIPTO", 2022,
         "C. gattii geralmente requer cursos mais longos de indução (4 semanas) pela resposta mais lenta; "
         "pode formar criptococomas cerebrais volumosos; maior carga fúngica inicial; "
         "fluconazol consolidação e manutenção: mesma duração que C. neoformans mas com CIM frequentemente mais alta"),

        ("Fluconazol", "Criptococose (Meningite Criptocócica e Forma Pulmonar)", 82.0, 1, "A", 3.0,
         "SBI-CRIPTO", 2022,
         "Consolidação e manutenção: 400-800 mg/dia (pode necessitar dose maior que para C. neoformans); "
         "verificar CIM — C. gattii pode ter CIM mais elevada ao fluconazol"),
    ],

    # ══════════════════════════════════════════════════════════════════
    # CANDIDA
    # ══════════════════════════════════════════════════════════════════
    "Candida albicans": [
        ("Fluconazol", "Candidemia e Candidíase Invasiva", 87.0, 1, "A", 5.0,
         "SBI-CAND", 2022,
         "Candidemia em pacientes estáveis sem uso prévio de azólico: fluconazol 800 mg ataque → 400 mg/dia IV/VO; "
         "não usar em UTI de alto risco ou com exposição azólica prévia — preferir equinocandina; "
         "C. albicans raramente resistente ao fluconazol (5% no Brasil)"),

        ("Caspofungina", "Candidemia e Candidíase Invasiva", 91.0, 1, "A", 0.5,
         "SBI-CAND", 2022,
         "1ª linha em candidemia em UTI, neutropênicos, pacientes instáveis ou com exposição prévia a azólico; "
         "70 mg ataque IV D1, depois 50 mg/dia; eficácia superior ao fluconazol em pacientes críticos; "
         "cobre C. glabrata e C. tropicalis com reduzida sensibilidade ao fluconazol"),

        ("Fluconazol", "Candidíase Orofaríngea (Sapinho / Muguete)", 92.0, 1, "A", 5.0,
         "SBI-CAND", 2022,
         "Fluconazol 100-200 mg/dia VO × 7-14 dias; ou nistatina suspensão oral 400.000-600.000 UI 4x/dia × 7-14 dias; "
         "nistatina para formas leves; fluconazol para formas moderadas-graves ou HIV com CD4 muito baixo"),

        ("Fluconazol", "Candidíase Vaginal (Vulvovaginite por Candida)", 91.0, 1, "A", 5.0,
         "SBI-CAND", 2022,
         "Dose única fluconazol 150 mg VO; ou clotrimazol vaginal 100 mg × 7 dias; "
         "candidíase recorrente: fluconazol 150 mg VO a cada semana × 6 meses (supressão); "
         "C. glabrata com reduzida sensibilidade ao fluconazol — usar ácido bórico intravaginal"),

        ("Fluconazol", "Candidíase Esofágica", 90.0, 1, "A", 5.0,
         "SBI-CAND", 2022,
         "Fluconazol 200-400 mg/dia VO × 14-21 dias; candidíase esofágica é doença definidora de AIDS; "
         "resposta geralmente excelente; em falha: voriconazol ou caspofungina; "
         "HIV: iniciar TARV urgente para reconstituição imune"),
    ],

    "Candida tropicalis": [
        ("Caspofungina", "Candidemia e Candidíase Invasiva", 88.0, 1, "A", 3.0,
         "SBI-CAND", 2022,
         "Equinocandina é preferida para C. tropicalis — menor sensibilidade ao fluconazol (30-40% das cepas brasileiras); "
         "fluconazol 400 mg/dia apenas se CIM ≤ 2 µg/mL documentada; "
         "importante em neutropênicos e transplantados no Brasil"),

        ("Fluconazol", "Candidemia e Candidíase Invasiva", 72.0, 2, "B", 35.0,
         "SBI-CAND", 2022,
         "Usar somente com sensibilidade documentada (CIM ≤ 2 µg/mL); "
         "resistência ao fluconazol em C. tropicalis varia de 20-40% no Brasil — avaliar por antibiograma"),
    ],

    "Candida glabrata": [
        ("Caspofungina", "Candidemia e Candidíase Invasiva", 88.0, 1, "A", 2.0,
         "SBI-CAND", 2022,
         "Equinocandina é a 1ª linha absoluta para C. glabrata — sensibilidade reduzida intrínseca ao fluconazol; "
         "fluconazol NUNCA 1ª linha para C. glabrata candidemia; "
         "monitorar MIC de equinocandinas (mutações FKS crescentes no Brasil)"),

        ("Anfotericina B desoxicolato", "Candidemia e Candidíase Invasiva", 82.0, 2, "B", 1.0,
         "SBI-CAND", 2022,
         "Alternativa em falha de equinocandina ou resistência documentada; "
         "0,7 mg/kg/dia IV; nefrotoxicidade limitante"),
    ],

    "Candida parapsilosis": [
        ("Fluconazol", "Candidemia e Candidíase Invasiva", 85.0, 1, "A", 8.0,
         "SBI-CAND", 2022,
         "C. parapsilosis geralmente sensível ao fluconazol — pode ser usado se paciente estável; "
         "equinocandinas têm CIM elevada para C. parapsilosis (biologicamente menos sensível) — mas ainda eficazes; "
         "remover cateter venoso central é fundamental para cura"),

        ("Caspofungina", "Candidemia e Candidíase Invasiva", 82.0, 2, "A", 0.5,
         "SBI-CAND", 2022,
         "CIM de equinocandinas para C. parapsilosis é biologicamente mais elevada; "
         "eficaz clinicamente mas fluconazol preferido se sensível; "
         "usar equinocandina se instabilidade clínica ou exposição prévia a azólico"),
    ],

    "Candida auris": [
        ("Caspofungina", "Candidemia e Candidíase Invasiva", 85.0, 1, "A", 15.0,
         "SBI-CAND", 2022,
         "Equinocandina é o tratamento de escolha para C. auris (majoritariamente resistente a fluconazol); "
         "solicitar CIM para todas as classes — C. auris pode ser pan-resistente; "
         "isolamento de contato obrigatório; notificar vigilância epidemiológica"),

        ("Anfotericina B desoxicolato", "Candidemia e Candidíase Invasiva", 78.0, 2, "B", 20.0,
         "SBI-CAND", 2022,
         "Segunda opção se resistência a equinocandinas; verificar CIM — algumas cepas resistentes à anfotericina; "
         "C. auris pode ser resistente simultaneamente a azólicos, equinocandinas e anfotericina (pan-resistência)"),
    ],

    # ══════════════════════════════════════════════════════════════════
    # ASPERGILLUS
    # ══════════════════════════════════════════════════════════════════
    "Aspergillus fumigatus": [
        ("Voriconazol", "Aspergilose Invasiva (Pulmonar e Disseminada)", 53.0, 1, "A", 5.0,
         "SBI-ASPERG", 2021,
         "1ª linha para aspergilose invasiva (IDSA e SBI); 6 mg/kg IV 12/12h D1 (ataque), "
         "depois 4 mg/kg IV 12/12h ou 200-300 mg VO 12/12h × 6-12 semanas; "
         "resistência ao voriconazol emergente no Brasil (azol-resistência ambiental); "
         "monitorar nível sérico terapêutico (alvo 1-5,5 µg/mL); interações via CYP2C19"),

        ("Anfotericina B lipossomal", "Aspergilose Invasiva (Pulmonar e Disseminada)", 50.0, 1, "A", 0.0,
         "SBI-ASPERG", 2021,
         "Alternativa ao voriconazol (dose: 3-5 mg/kg/dia IV); preferida em: resistência ao voriconazol, "
         "insuficiência hepática, ou interações inaceitáveis; resgate e refratários ao voriconazol; "
         "acesso via RENAME excepcional"),

        ("Isavuconazol", "Aspergilose Invasiva (Pulmonar e Disseminada)", 51.0, 1, "A", 3.0,
         "SBI-ASPERG", 2021,
         "Não inferior ao voriconazol em ensaio SECURE; menor hepatotoxicidade e interações; "
         "aprovado ANVISA; disponibilidade muito limitada no Brasil; opção em pacientes com doença hepática"),

        ("Itraconazol", "Aspergilose Broncopulmonar Alérgica (ABPA)", 80.0, 1, "A", 2.0,
         "SBI-ASPERG", 2021,
         "ABPA: itraconazol 200 mg VO 12/12h × 16-32 semanas em combinação com corticoide; "
         "reduz eosinofilia, IgE e exacerbações; disponível no SUS; monitorar nível sérico ≥ 0,5 µg/mL"),

        ("Voriconazol", "Aspergilose Broncopulmonar Alérgica (ABPA)", 75.0, 2, "B", 2.0,
         "SBI-ASPERG", 2021,
         "Alternativa ao itraconazol para ABPA refratária ou intolerância; dados limitados; "
         "200 mg VO 12/12h × 16-32 semanas"),

        ("Caspofungina", "Aspergilose Invasiva (Pulmonar e Disseminada)", 45.0, 2, "B", 2.0,
         "SBI-ASPERG", 2021,
         "Terapia de resgate em falha ao voriconazol; 70 mg IV ataque → 50 mg/dia; "
         "combinação voriconazol + caspofungina em casos refratários (sem benefício em preemptiva)"),
    ],

    # ══════════════════════════════════════════════════════════════════
    # MUCORALES
    # ══════════════════════════════════════════════════════════════════
    "Rhizopus arrhizus": [
        ("Anfotericina B desoxicolato", "Mucormicose / Zigomicose (Rinocerebral, Pulmonar, Cutânea)", 50.0, 1, "B", 0.0,
         "SBI-ASPERG", 2021,
         "Primeiro antifúngico de escolha para mucormicose — 1,0-1,5 mg/kg/dia IV; "
         "voriconazol NÃO tem atividade contra Mucorales — contraindicado; "
         "cirurgia desbridante agressiva é obrigatória e mais importante que o antifúngico; "
         "corrigir fatores predisponentes (controle glicêmico, reduzir imunossupressão)"),

        ("Anfotericina B lipossomal", "Mucormicose / Zigomicose (Rinocerebral, Pulmonar, Cutânea)", 55.0, 1, "A", 0.0,
         "SBI-ASPERG", 2021,
         "Preferida para mucormicose rinocerebral (maior penetração no SNC) e em insuficiência renal; "
         "5-10 mg/kg/dia IV; menor nefrotoxicidade permite doses mais elevadas; "
         "disponibilidade limitada no Brasil"),

        ("Posaconazol", "Mucormicose / Zigomicose (Rinocerebral, Pulmonar, Cutânea)", 60.0, 2, "B", 0.0,
         "SBI-ASPERG", 2021,
         "Terapia de consolidação e manutenção oral após anfotericina B inicial; "
         "300 mg VO 12/12h D1, depois 300 mg/dia; cobertura de Mucorales diferente do voriconazol; "
         "dados de eficácia principalmente em casos de resgate"),

        ("Isavuconazol", "Mucormicose / Zigomicose (Rinocerebral, Pulmonar, Cutânea)", 55.0, 2, "B", 0.0,
         "SBI-ASPERG", 2021,
         "Ativo contra Mucorales (diferente do voriconazol); consolidação após anfotericina; "
         "aprovado FDA e ANVISA para mucormicose; dados de fase 3 limitados; disponibilidade restrita no BR"),
    ],

    # ══════════════════════════════════════════════════════════════════
    # SPOROTHRIX
    # ══════════════════════════════════════════════════════════════════
    "Sporothrix schenckii": [
        ("Itraconazol", "Esporotricose (Cutânea Linfangítica, Cutânea Fixa e Disseminada)", 90.0, 1, "A", 3.0,
         "SVS-ESPORO", 2022,
         "1ª linha para esporotricose cutânea linfangítica e cutânea fixa em imunocompetentes; "
         "200 mg/dia VO × 3-6 meses (cutânea) ou 200 mg 12/12h × 12-24 meses (disseminada); "
         "disponível no SUS; monitorar função hepática trimestralmente"),

        ("Iodeto de Potássio (KI)", "Esporotricose (Cutânea Linfangítica, Cutânea Fixa e Disseminada)", 82.0, 1, "B", 3.0,
         "SVS-ESPORO", 2022,
         "Alternativa de baixo custo para formas cutâneas leves em imunocompetentes; "
         "solução saturada 5-10 gotas 3x/dia com progressão até 40-50 gotas 3x/dia × 3-6 meses; "
         "disponível no SUS; pode ser usado como adjuvante ao itraconazol em formas resistentes"),

        ("Anfotericina B desoxicolato", "Esporotricose (Cutânea Linfangítica, Cutânea Fixa e Disseminada)", 85.0, 1, "A", 0.5,
         "SVS-ESPORO", 2022,
         "Formas disseminadas graves, meningoesporotricose, HIV com CD4 muito baixo; "
         "0,7-1,0 mg/kg/dia IV × 4-6 semanas (indução), depois transição para itraconazol oral; "
         "gravidez: anfotericina B é a única opção segura para formas graves"),
    ],

    "Sporothrix brasiliensis": [
        ("Itraconazol", "Esporotricose (Cutânea Linfangítica, Cutânea Fixa e Disseminada)", 82.0, 1, "A", 8.0,
         "SVS-ESPORO", 2022,
         "S. brasiliensis tem CIM mais elevada ao itraconazol que S. schenckii clássico; "
         "resposta mais lenta — tratar por períodos mais longos (6-18 meses); "
         "resistência ao itraconazol relatada no Rio de Janeiro — monitorar resposta clínica"),

        ("Anfotericina B desoxicolato", "Esporotricose (Cutânea Linfangítica, Cutânea Fixa e Disseminada)", 88.0, 1, "A", 0.0,
         "SVS-ESPORO", 2022,
         "Preferida em falha ao itraconazol (crescente para S. brasiliensis) e formas disseminadas; "
         "S. brasiliensis mantém boa sensibilidade à anfotericina B"),
    ],

    # ══════════════════════════════════════════════════════════════════
    # DERMATÓFITOS
    # ══════════════════════════════════════════════════════════════════
    "Trichophyton rubrum": [
        ("Terbinafina", "Tinea Pedis (Pé de Atleta) e Tinea Unguium (Onicomicose)", 83.0, 1, "A", 2.0,
         "SBD-MICOSES", 2022,
         "Melhor eficácia para onicomicose por T. rubrum (fungicida): 250 mg/dia VO × 6 semanas (unhas das mãos) "
         "ou × 12 semanas (unhas dos pés); taxa de cura micológica 70-80%; monitorar hepático a cada 6 semanas"),

        ("Itraconazol", "Tinea Pedis (Pé de Atleta) e Tinea Unguium (Onicomicose)", 72.0, 1, "A", 2.0,
         "SBD-MICOSES", 2022,
         "Alternativa à terbinafina para onicomicose: pulso 200 mg 12/12h × 7 dias por mês (× 2 meses mãos / × 3 meses pés); "
         "menor eficácia que terbinafina para dermatófitos; disponível no SUS"),

        ("Clotrimazol", "Tinea Corporis, Cruris e Faciei (Tinha do Corpo)", 89.0, 1, "A", 1.0,
         "SBD-MICOSES", 2022,
         "Tópico creme 1% 2x/dia × 2-4 semanas para tinea corporis e cruris não extensa; "
         "eficaz e de baixo custo; disponível no SUS"),
    ],

    "Trichophyton tonsurans": [
        ("Griseofulvina", "Tinea Capitis (Tinha do Couro Cabeludo)", 80.0, 1, "A", 1.0,
         "SBD-MICOSES", 2022,
         "Tratamento sistêmico obrigatório para tinea capitis; "
         "griseofulvina microsize 20-25 mg/kg/dia VO × 6-8 semanas; disponível no SUS; "
         "tomar com refeição gordurosa para melhorar absorção; tratamento por 4-8 semanas"),

        ("Terbinafina", "Tinea Capitis (Tinha do Couro Cabeludo)", 85.0, 1, "A", 1.0,
         "SBD-MICOSES", 2022,
         "Eficácia superior à griseofulvina para T. tonsurans em estudos comparativos; "
         "< 20 kg: 62,5 mg/dia; 20-40 kg: 125 mg/dia; > 40 kg: 250 mg/dia; VO × 4-6 semanas; "
         "custo maior que griseofulvina; não disponível no SUS para essa indicação na maioria dos serviços"),
    ],

    "Microsporum canis": [
        ("Griseofulvina", "Tinea Capitis (Tinha do Couro Cabeludo)", 85.0, 1, "A", 1.0,
         "SBD-MICOSES", 2022,
         "M. canis: griseofulvina é superior à terbinafina para este agente específico; "
         "20-25 mg/kg/dia VO × 8-12 semanas; shampu de cetoconazol ou sulfeto de selênio como adjuvante "
         "para reduzir transmissão; tratar animais domésticos infectados"),
    ],

    # ══════════════════════════════════════════════════════════════════
    # MALASSEZIA
    # ══════════════════════════════════════════════════════════════════
    "Malassezia furfur": [
        ("Cetoconazol", "Pitiríase Versicolor (Tinea Versicolor)", 92.0, 1, "A", 1.0,
         "SBD-MICOSES", 2022,
         "Xampu de cetoconazol 2% aplicado no corpo por 10 min antes do banho × 3-5 dias consecutivos; "
         "creme cetoconazol 2% 1x/dia × 2-4 semanas; ou itraconazol 200 mg/dia VO × 7 dias (formas extensas); "
         "despigmentação pós-inflamatória persiste após cura micológica — tranquilizar o paciente"),

        ("Fluconazol", "Pitiríase Versicolor (Tinea Versicolor)", 85.0, 1, "A", 1.0,
         "SBD-MICOSES", 2022,
         "Fluconazol 300-400 mg VO dose única (ou 150 mg/semana × 4 semanas); "
         "eficaz para formas extensas; profilaxia: fluconazol 300 mg mensal reduz recidivas; "
         "tomar e fazer exercício físico para suar — aumenta concentração do fluconazol na pele"),

        ("Itraconazol", "Pitiríase Versicolor (Tinea Versicolor)", 87.0, 1, "A", 1.0,
         "SBD-MICOSES", 2022,
         "200 mg/dia VO × 7 dias; alternativa oral quando fluconazol indisponível; "
         "profilaxia: 200 mg/dia × 1 dia/mês para recidivantes"),
    ],

    # ══════════════════════════════════════════════════════════════════
    # FONSECAEA / CROMOBLASTOMICOSE
    # ══════════════════════════════════════════════════════════════════
    "Fonsecaea pedrosoi": [
        ("Itraconazol", "Cromoblastomicose", 56.0, 1, "A", 5.0,
         "SBD-MICOSES", 2022,
         "1ª linha para cromoblastomicose; 200-400 mg/dia VO × 12-24 meses (ou mais); "
         "taxa de cura baixa especialmente em lesões extensas e antigas (30-50%); "
         "combinação com terbinafina ou criocirurgia pode melhorar resultados"),

        ("Terbinafina", "Cromoblastomicose", 50.0, 1, "B", 5.0,
         "SBD-MICOSES", 2022,
         "Alternativa ao itraconazol ou combinação com itraconazol em lesões extensas; "
         "500-1000 mg/dia VO × 12-24 meses; dados de eficácia limitados; "
         "combinação itraconazol 200 mg + terbinafina 250 mg/dia tem melhor taxa de cura que monoterapia"),

        ("Voriconazol", "Cromoblastomicose", 62.0, 2, "B", 3.0,
         "SBD-MICOSES", 2022,
         "Casos refratários ao itraconazol; dados principalmente de relatos de caso; "
         "200-300 mg VO 12/12h × 12-24 meses"),
    ],

    # ══════════════════════════════════════════════════════════════════
    # FUSARIUM
    # ══════════════════════════════════════════════════════════════════
    "Fusarium solani": [
        ("Voriconazol", "Fusariose (Hialohifomicose por Fusarium)", 47.0, 1, "B", 30.0,
         "SBI-ASPERG", 2021,
         "Fusarium solani tem alta resistência intrínseca a azólicos; voriconazol é a melhor opção disponível; "
         "6 mg/kg IV 12/12h D1 (ataque), depois 4 mg/kg IV 12/12h; longa duração; "
         "reconstituição imune (saída da neutropenia) é fundamental para resolução"),

        ("Anfotericina B lipossomal", "Fusariose (Hialohifomicose por Fusarium)", 45.0, 1, "B", 15.0,
         "SBI-ASPERG", 2021,
         "Combinação voriconazol + anfotericina B lipossomal em fusariose disseminada grave; "
         "F. solani tem CIM elevada para anfotericina comparado a F. oxysporum; "
         "3-5 mg/kg/dia IV; monitorar função renal rigorosamente"),
    ],

    # ══════════════════════════════════════════════════════════════════
    # PNEUMOCYSTIS JIROVECII
    # ══════════════════════════════════════════════════════════════════
    "Pneumocystis jirovecii": [
        ("Sulfadiazina + Trimetoprima", "Pneumonia por Pneumocystis jirovecii (PCP)", 85.0, 1, "A", 3.0,
         "PCDT-HIV-FUNG", 2022,
         "SMX-TMP é o TRATAMENTO DE ESCOLHA para PCP; 15-20 mg/kg/dia de TMP IV ou VO (em 4 doses) × 21 dias; "
         "SpO₂ < 70 mmHg de PaO₂: adicionar corticoide (prednisona 40 mg 2x/dia × 5 dias → desmame); "
         "profilaxia primária: SMX-TMP 1 cp dupla força/dia (ou 3x/semana) para CD4 < 200; "
         "profilaxia secundária: SMX-TMP 1 cp simples/dia indefinidamente até CD4 > 200 por 3 meses"),

        ("Pentamidina", "Pneumonia por Pneumocystis jirovecii (PCP)", 70.0, 2, "A", 1.0,
         "PCDT-HIV-FUNG", 2022,
         "Alternativa ao SMX-TMP em alergia grave não controlável; "
         "4 mg/kg/dia IV × 21 dias; toxicidade: hipoglicemia grave, hipotensão, nefrotoxicidade, arritmia; "
         "pentamidina inalatória: profilaxia apenas (não tratamento de PCP ativa)"),

        ("Clindamicina", "Pneumonia por Pneumocystis jirovecii (PCP)", 65.0, 2, "B", 2.0,
         "PCDT-HIV-FUNG", 2022,
         "Clindamicina 600 mg IV 8/8h + primaquina 30 mg/dia VO × 21 dias; "
         "alternativa de 2ª linha em intolerância ao SMX-TMP; "
         "primaquina contraindicada em deficiência de G6PD — testar antes de usar"),

        ("Atovaquona", "Pneumonia por Pneumocystis jirovecii (PCP)", 62.0, 2, "A", 1.0,
         "PCDT-HIV-FUNG", 2022,
         "Alternativa oral para formas leves-moderadas de PCP em intolerância ao SMX-TMP; "
         "750 mg VO 12/12h × 21 dias; tomar com refeição gordurosa; "
         "profilaxia: 1500 mg/dia; disponibilidade limitada no Brasil"),
    ],

    # ══════════════════════════════════════════════════════════════════
    # LACAZIA LOBOI
    # ══════════════════════════════════════════════════════════════════
    "Lacazia loboi": [
        (None, "Lobomicose (Lacaziose — Doença de Jorge Lobo)", None, None, "C", None,
         "SBMT-FUNGOS", 2022,
         "Lacazia loboi não pode ser cultivada in vitro — impossibilidade de teste de sensibilidade; "
         "NENHUM antifúngico sistêmico tem eficácia comprovada em ensaios clínicos controlados; "
         "relatos de casos com itraconazol, clofazimina e terbinafina sem resposta consistente; "
         "TRATAMENTO: CIRURGIA com exérese ampla das lesões é a única opção com evidência; "
         "recidiva frequente mesmo após cirurgia; novas lesões podem surgir em locais distantes"),
    ],
}

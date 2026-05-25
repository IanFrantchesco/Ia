"""
Patologias fúngicas mais importantes no Brasil com CID-10.
Fontes: PCDT-PARACOC MS 2022, SBD, SBMT, SBI, GVS/MS 5ª ed. 2022, PCDT-HIV, ANVISA.

Cada entrada:
(nome, cid10, categoria_nome, descricao, notificacao_compulsoria, tipo_notificacao,
 prevalencia_br, mortalidade_br, populacao_risco, fonte_sigla)
"""

CATEGORIAS_FUNGICAS = [
    # (nome, sistema)
    ("Micoses Sistêmicas Endêmicas", "Sistêmico / pulmão / múltiplos órgãos — fungos dimórficos endêmicos do Brasil"),
    ("Micoses Oportunistas Invasivas", "Sistêmico — infecções fúngicas em imunossuprimidos e hospitalizados"),
    ("Micoses Cutâneas e Subcutâneas", "Tegumento / derme / tecido subcutâneo"),
    ("Micoses Superficiais", "Camadas superficiais da pele, cabelo e unhas"),
    ("Pneumocistose", "Aparelho respiratório — oportunista em HIV e imunossuprimidos"),
]

PATOLOGIAS_FUNGICAS = [

    # ── MICOSES SISTÊMICAS ENDÊMICAS ──────────────────────────────────────────
    (
        "Paracoccidioidomicose (Blastomicose Sul-Americana)",
        "B41", "Micoses Sistêmicas Endêmicas",
        "Infecção causada por Paracoccidioides brasiliensis e P. lutzii; principal micose sistêmica endêmica da América Latina "
        "e a mais importante do Brasil; formas: aguda/subaguda (juvenil) e crônica (adultos); compromete pulmões, mucosas, pele, "
        "sistema linfático e suprarrenais; mortalidade sem tratamento é alta; Brasil responde por 80% dos casos mundiais.",
        True, "semanal",
        "alta", "media",
        "Trabalhadores rurais masculinos 30-60 anos; agricultores que mexem com solo úmido; estados de SP, MG, PR, MT, GO; "
        "fumantes têm risco aumentado de forma crônica grave",
        "PCDT-PARACOC"
    ),
    (
        "Histoplasmose (Doença de Darling)",
        "B39", "Micoses Sistêmicas Endêmicas",
        "Infecção por Histoplasma capsulatum; transmitida por inalação de microconídios em locais com excrementos de aves e morcegos; "
        "formas: pulmonar autolimitada (maioria), progressiva disseminada (imunossuprimidos), mediastínica; "
        "surtos ocorrem em demolições, espeleologistas e trabalhadores em galinheiros; endêmica no Brasil.",
        True, "semanal",
        "alta", "media",
        "Espeleólogos; trabalhadores em demolição de edifícios antigos; contato com excrementos de pombos e morcegos; "
        "HIV/AIDS com CD4 < 150 células/mm³ têm risco de histoplasmose disseminada grave",
        "SVS-HISTOP"
    ),
    (
        "Criptococose (Meningite Criptocócica e Forma Pulmonar)",
        "B45", "Micoses Sistêmicas Endêmicas",
        "Infecção por Cryptococcus neoformans (sorotipo A/D) e C. gattii; principal forma grave: meningoencefalite; "
        "C. neoformans predomina em HIV com CD4 < 100; C. gattii afeta imunocompetentes em determinadas regiões; "
        "alta mortalidade sem tratamento; segunda causa de meningite em HIV no Brasil após TB; "
        "exposição a excrementos de pombos é fator de risco.",
        True, "semanal",
        "media", "alta",
        "PVHIV com CD4 < 100 células/mm³ (principal grupo); transplantados de órgãos sólidos; corticoterapia crônica; "
        "cirróticos; imunocompetentes em regiões com C. gattii (Norte e Nordeste do Brasil)",
        "SBI-CRIPTO"
    ),
    (
        "Lobomicose (Lacaziose — Doença de Jorge Lobo)",
        "B48.0", "Micoses Sistêmicas Endêmicas",
        "Infecção crônica da pele e tecido subcutâneo por Lacazia loboi; exclusivamente cutânea e subcutânea; "
        "lesões queloides nodulares no dorso, membros e face; curso crônico progressivo por décadas; "
        "diagnóstico por biópsia com visualização das células leveduriformes em cadeia; "
        "sem antifúngico sistêmico comprovadamente eficaz — tratamento cirúrgico.",
        False, None,
        "baixa", "baixa",
        "Ribeirinhos e pescadores da Amazônia (AM, PA, RO, AC); homens adultos; indígenas amazônicos; "
        "rara zoonose em golfinhos Sotalia fluviatilis no Brasil",
        "SBMT-FUNGOS"
    ),

    # ── CANDIDÍASES ──────────────────────────────────────────────────────────
    (
        "Candidemia e Candidíase Invasiva",
        "B37.7", "Micoses Oportunistas Invasivas",
        "Infecção da corrente sanguínea por Candida spp. (principalmente C. albicans, C. tropicalis, C. glabrata, C. parapsilosis); "
        "principal infecção fúngica em UTI no Brasil; mortalidade de 30-50% em 30 dias; "
        "fator de risco: cateter venoso central, antibioticoterapia ampla, nutrição parenteral, cirurgia abdominal; "
        "C. auris emergente e multirresistente representa ameaça crescente.",
        False, None,
        "alta", "alta",
        "Pacientes de UTI; cirurgia gastrointestinal ou cardíaca; imunossuprimidos; "
        "grandes queimados; prematuros com cateter central; hemodialisados; transplantados",
        "SBI-CAND"
    ),
    (
        "Candidíase Orofaríngea (Sapinho / Muguete)",
        "B37.0", "Micoses Oportunistas Invasivas",
        "Infecção por Candida albicans da mucosa oral e orofaringe; placas brancas removíveis com eritema subjacente; "
        "muito frequente em HIV/AIDS, uso de corticoide inalatório, prótese dentária, xerostomia; "
        "pode indicar imunodeficiência subjacente não diagnosticada; tratamento tópico geralmente eficaz.",
        False, None,
        "muito_alta", "baixa",
        "PVHIV com CD4 < 200; uso de corticoides inalatórios sem higiene oral; prótese dentária mal higienizada; "
        "neonatos (muguet neonatal); antibioticoterapia de amplo espectro",
        "SBI-CAND"
    ),
    (
        "Candidíase Vaginal (Vulvovaginite por Candida)",
        "B37.3", "Micoses Oportunistas Invasivas",
        "Infecção por Candida albicans (80-90%) e outras espécies da vulva e vagina; corrimento branco grumoso, "
        "prurido intenso, eritema vulvar, dispareunia; extremamente prevalente — 75% das mulheres têm pelo menos um episódio; "
        "formas recorrentes (≥4 episódios/ano) em diabéticas, gravidez e imunossuprimidas.",
        False, None,
        "muito_alta", "baixa",
        "Mulheres em idade fértil; uso de antibióticos de amplo espectro; diabetes mellitus descompensada; "
        "gestantes; uso de anticoncepcionais orais; imunossuprimidas",
        "SBD-MICOSES"
    ),
    (
        "Candidíase Esofágica",
        "B37.81", "Micoses Oportunistas Invasivas",
        "Infecção por Candida do esôfago; disfagia e odinofagia; principal critério diagnóstico de AIDS (doença definidora); "
        "diagnóstico endoscópico; mais grave que candidíase oral; pode coexistir com candidíase oral; "
        "resposta ao fluconazol é geralmente boa em 1ª apresentação.",
        False, None,
        "alta", "media",
        "PVHIV com CD4 < 100 células/mm³; transplantados; imunossuprimidos em corticoterapia; "
        "pacientes oncológicos em quimioterapia",
        "PCDT-HIV-FUNG"
    ),

    # ── ASPERGILOSES ─────────────────────────────────────────────────────────
    (
        "Aspergilose Invasiva (Pulmonar e Disseminada)",
        "B44.1", "Micoses Oportunistas Invasivas",
        "Infecção por Aspergillus fumigatus (principal) em imunossuprimidos graves; neutropenia prolongada é o principal fator de risco; "
        "angioinfiltração vascular com necrose e disseminação hematogênica; TC pulmonar: sinal do halo e cavitação; "
        "galactomanana sérica e em LBA são biomarcadores diagnósticos; mortalidade > 50% mesmo com tratamento.",
        False, None,
        "media", "alta",
        "Neutropenia grave prolongada (> 10 dias); transplante de células-tronco hematopoéticas (TCTH); "
        "transplantados de pulmão; leucemia mieloide aguda; corticoterapia de alta dose; DPOC grave com internação",
        "SBI-ASPERG"
    ),
    (
        "Aspergilose Broncopulmonar Alérgica (ABPA)",
        "B44.81", "Micoses Oportunistas Invasivas",
        "Resposta hipersensibilidade (tipo I e III) a Aspergillus fumigatus em asma e fibrose cística; "
        "infiltrados pulmonares migratórios, bronquiectasias centrais, IgE total elevada (> 1000 UI/mL), "
        "IgE específica anti-Aspergillus positiva; deterioração da função pulmonar sem tratamento; "
        "tratamento com corticoide sistêmico e itraconazol.",
        False, None,
        "media", "baixa",
        "Asmáticos de difícil controle (5-10% têm ABPA); pacientes com fibrose cística; "
        "adultos jovens; imunocompetentes com resposta alérgica exacerbada",
        "SBI-ASPERG"
    ),
    (
        "Aspergiloma Pulmonar",
        "B44.0", "Micoses Oportunistas Invasivas",
        "Colonização de cavidade pulmonar pré-existente por Aspergillus (bola fúngica); "
        "principal complicação em sequelas de tuberculose com cavidades; hemoptise é a manifestação clínica mais grave; "
        "radiologicamente: imagem de massa dentro da cavidade (sinal do crescente de ar); "
        "tratamento cirúrgico quando indicado; itraconazol ou voriconazol para sintomáticos inoperáveis.",
        False, None,
        "media", "media",
        "Sequelas de tuberculose pulmonar com cavidades; sarcoidose; bronquiectasias; DPOC grave; "
        "imunocompetentes com doenças pulmonares estruturais",
        "SBI-ASPERG"
    ),

    # ── MUCORMICOSE ──────────────────────────────────────────────────────────
    (
        "Mucormicose / Zigomicose (Rinocerebral, Pulmonar, Cutânea)",
        "B46", "Micoses Oportunistas Invasivas",
        "Infecção por fungos da ordem Mucorales (Rhizopus, Mucor, Cunninghamella); angioinvasiva com trombose e necrose tecidual; "
        "formas: rinocerebral (principal em diabéticos), pulmonar (neutropênicos), cutânea (trauma), disseminada; "
        "progresso devastador — tecido necrótico preto na face; cirurgia desbridante agressiva é mandatória; "
        "alta mortalidade (> 50%); voriconazol NÃO tem atividade — usar anfotericina B.",
        False, None,
        "baixa", "alta",
        "Diabéticos descompensados com acidose metabólica (forma rinocerebral); neutropênicos; "
        "transplantados de TCTH; trauma com inoculação; uso de deferoxamina; ferro elevado",
        "SBI-ASPERG"
    ),

    # ── MICOSES CUTÂNEAS E SUBCUTÂNEAS ────────────────────────────────────────
    (
        "Esporotricose (Cutânea Linfangítica, Cutânea Fixa e Disseminada)",
        "B42", "Micoses Cutâneas e Subcutâneas",
        "Infecção por Sporothrix schenckii e S. brasiliensis; forma cutânea linfangítica é a mais comum: "
        "lesão ulcerada no sítio de inoculação seguida de nódulos ao longo do trajeto linfático (forma em colar de contas); "
        "endemia felina no Rio de Janeiro — principal foco mundial; S. brasiliensis é mais virulento e menos sensível ao itraconazol; "
        "disseminada ocorre em imunossuprimidos; tratamento: itraconazol ou SSKI.",
        True, "semanal",
        "alta", "baixa",
        "Trabalhadores rurais; jardineiros; floristas; manipuladores de material vegetal; "
        "proprietários de gatos no Rio de Janeiro, Minas Gerais e Rio Grande do Sul; "
        "imunossuprimidos têm risco de forma disseminada",
        "SVS-ESPORO"
    ),
    (
        "Cromoblastomicose",
        "B43", "Micoses Cutâneas e Subcutâneas",
        "Infecção crônica por fungos dematiáceos (Fonsecaea pedrosoi, Cladophialophora carrionii); "
        "inoculação traumática em solos tropicais; lesões verrucosas, papilomatosas e queloidianas de lento crescimento; "
        "membros inferiores são os mais afetados; células muriformes (fumagoides) na biópsia são patognomônicas; "
        "tratamento prolongado e de difícil erradicação; taxa de cura baixa.",
        False, None,
        "media", "baixa",
        "Trabalhadores rurais que caminham descalços (Norte e Nordeste do Brasil); agricultores; "
        "homens adultos em áreas tropicais; populações de baixa renda em regiões rurais",
        "SBD-MICOSES"
    ),
    (
        "Micetoma Fúngico (Eumicetoma)",
        "B47.0", "Micoses Cutâneas e Subcutâneas",
        "Infecção crônica progressiva do tecido subcutâneo, fáscia, músculo e osso por fungos (Madurella mycetomatis principal); "
        "tríade clínica: tumor (edema crônico), trajetos fistulosos e grãos (colônias fúngicas); pé de Madura; "
        "sem tratamento: amputação; diagnóstico por coloração dos grãos e cultura; "
        "itraconazol e voriconazol são os antifúngicos de escolha.",
        False, None,
        "baixa", "baixa",
        "Trabalhadores rurais do Nordeste brasileiro que caminham descalços; "
        "agricultores em regiões semiáridas; homens adultos",
        "SBD-MICOSES"
    ),
    (
        "Feohifomicose",
        "B43.8", "Micoses Cutâneas e Subcutâneas",
        "Infecção por fungos dematiáceos (melanizados) causando abscessos subcutâneos e cistos; "
        "Exophiala, Phialophora, Wangiella são os agentes mais comuns; localizadas em imunossuprimidos; "
        "diagnóstico por histopatologia (hifas marrons) e cultura; tratamento com itraconazol ou voriconazol; "
        "excisão cirúrgica é frequentemente necessária.",
        False, None,
        "baixa", "baixa",
        "Imunossuprimidos (transplantados, HIV); pacientes em corticoterapia crônica; "
        "trauma com material vegetal contaminado em qualquer população",
        "SBD-MICOSES"
    ),
    (
        "Fusariose (Hialohifomicose por Fusarium)",
        "B48.8", "Micoses Oportunistas Invasivas",
        "Infecção por Fusarium solani e F. oxysporum; forma localizada: onicomicose, ceratite, úlcera cutânea; "
        "forma disseminada em neutropênicos: febre refratária, lesões cutâneas disseminadas (nódulos eritematosos com escara central), "
        "fungemia; diagnóstico por hemocultura (cresce em hemocultura ao contrário de Aspergillus); "
        "alta resistência a antifúngicos — voriconazol e anfotericina B em combinação.",
        False, None,
        "media", "alta",
        "Neutropênicos graves (leucemia aguda, TCTH); portadores de onicomicose como porta de entrada; "
        "pacientes com queimaduras; imunocompetentes com trauma ocular (ceratite por Fusarium)",
        "SBI-ASPERG"
    ),
    (
        "Rinossinusite Fúngica (Invasiva e Alérgica)",
        "J33.0 / B44.8", "Micoses Oportunistas Invasivas",
        "Espectro de infecções fúngicas dos seios paranasais: forma alérgica (AFRS — em asmáticos), "
        "forma crônica não invasiva (bola fúngica sinusal) e forma invasiva (principalmente por Aspergillus e Mucor em imunossuprimidos); "
        "forma invasiva aguda é emergência otorrinolaringológica com prognóstico grave; "
        "Mucor: necrose do palato, tecido orbital e SNC; diagnóstico endoscópico e histopatológico.",
        False, None,
        "media", "media",
        "AFRS: pacientes com asma e rinossinusite recorrente; bola fúngica: adultos com tratamento endodôntico; "
        "invasiva: diabéticos, imunossuprimidos, transplantados; mucormicose rinocerebral: diabéticos com cetoacidose",
        "SBI-ASPERG"
    ),

    # ── MICOSES SUPERFICIAIS ──────────────────────────────────────────────────
    (
        "Tinea Capitis (Tinha do Couro Cabeludo)",
        "B35.0", "Micoses Superficiais",
        "Infecção dermatofítica do couro cabeludo por Trichophyton tonsurans (principal no Brasil) e Microsporum canis; "
        "alopecia com descamação; querion de Celso (forma inflamatória grave com abscessos) pode causar alopecia permanente; "
        "muito prevalente em crianças no Brasil, especialmente Norte e Nordeste; "
        "tratamento sistêmico obrigatório (griseofulvina ou terbinafina).",
        False, None,
        "muito_alta", "baixa",
        "Crianças 3-14 anos; compartilhamento de objetos de cabelo; creches e escolas; "
        "populações de baixa renda; crianças com contato com animais domésticos (M. canis)",
        "SBD-MICOSES"
    ),
    (
        "Tinea Corporis, Cruris e Faciei (Tinha do Corpo)",
        "B35.4", "Micoses Superficiais",
        "Infecção dermatofítica do corpo (T. rubrum, T. tonsurans, M. canis); lesões anulares com borda eritematosa ativa "
        "e centro mais claro (tinea em anel); pruriginosas; tinea cruris afeta região inguinal; "
        "extremamente prevalente no clima tropical brasileiro; tratamento tópico na maioria dos casos.",
        False, None,
        "muito_alta", "baixa",
        "Toda a população; maior prevalência em adolescentes e adultos; praticantes de esportes de contato; "
        "populações de clima quente e úmido",
        "SBD-MICOSES"
    ),
    (
        "Tinea Pedis (Pé de Atleta) e Tinea Unguium (Onicomicose)",
        "B35.3 / B35.1", "Micoses Superficiais",
        "Tinea pedis por T. rubrum e T. interdigitale: maceração e descamação interdigital, forma vesicular, "
        "forma moccasin (ceratose plantar crônica); onicomicose (tinea unguium): infecção ungueal por T. rubrum — "
        "principal causa de onicomicose no Brasil; afeta unhas dos pés em 80% dos casos; "
        "tratamento sistêmico (terbinafina oral) necessário para onicomicose; topico insuficiente para a maioria.",
        False, None,
        "muito_alta", "baixa",
        "Adultos; praticantes de esportes com uso de vestiários; idosos (onicomicose muito prevalente > 60 anos); "
        "diabéticos (risco aumentado de onicomicose e celulite secundária)",
        "SBD-MICOSES"
    ),
    (
        "Pitiríase Versicolor (Tinea Versicolor)",
        "B36.0", "Micoses Superficiais",
        "Infecção por Malassezia furfur e outras espécies de Malassezia da camada córnea da pele; "
        "manchas hipo ou hiperpigmentadas com fina descamação (sinal de Zireli positivo); tronco, ombros e pescoço; "
        "não contagiosa — fungo da microbiota normal com crescimento excessivo favorecido pelo calor; "
        "altíssima prevalência no Brasil pelo clima quente e úmido; recidiva frequente.",
        False, None,
        "muito_alta", "baixa",
        "Adolescentes e adultos jovens; climas quentes e úmidos (favorece Malassezia); "
        "pessoas que suam muito; uso de protetor solar oleoso; imunossuprimidos",
        "SBD-MICOSES"
    ),
    (
        "Dermatofitose Ungueal e Cutânea por Tricofíton (Tinea Manum e Tinea Barbae)",
        "B35.2 / B35.6", "Micoses Superficiais",
        "Tinea manum: infecção dermatofítica das mãos (T. rubrum); unilateral típica com hiperceratose; "
        "tinea barbae: infecção da barba por T. violaceum ou M. canis; frequente em homens adultos; "
        "síndrome uma-mão-dois-pés (tinea manum unilateral associada a tinea pedis bilateral); "
        "tratamento sistêmico necessário para formas extensas.",
        False, None,
        "alta", "baixa",
        "Adultos; trabalhadores rurais; tratadores de animais; adultos que compartilham fômites; "
        "homens com barba e contato com animais (tinea barbae)",
        "SBD-MICOSES"
    ),

    # ── PNEUMOCISTOSE ─────────────────────────────────────────────────────────
    (
        "Pneumonia por Pneumocystis jirovecii (PCP)",
        "B59", "Pneumocistose",
        "Pneumonia intersticial difusa por Pneumocystis jirovecii em imunossuprimidos; "
        "principal infecção oportunista em HIV/AIDS (CD4 < 200 células/mm³) no Brasil; "
        "tríade clínica: dispneia progressiva, febre e tosse seca; "
        "RX: infiltrado intersticial difuso bilateral (vidro fosco); LDH elevada; SpO₂ em queda com esforço; "
        "diagnóstico por PCR ou imunofluorescência em lavado broncoalveolar; SMX-TMP é o tratamento de escolha.",
        False, None,
        "alta", "alta",
        "PVHIV com CD4 < 200 células/mm³ sem profilaxia; transplantados de órgãos sólidos sem profilaxia; "
        "pacientes em corticoterapia prolongada (> 20 mg prednisona/dia > 1 mês); quimioterapia para leucemias linfoides",
        "PCDT-HIV-FUNG"
    ),
]

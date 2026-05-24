"""
100 patologias bacterianas mais comuns no Brasil com CID-10.
Fonte base: GVS-MS 5ª ed., SINAN, PCDT do Ministério da Saúde.

Cada entrada:
(nome, cid10, categoria_nome, descricao, notificacao_compulsoria, tipo_notificacao,
 prevalencia_br, mortalidade_br, populacao_risco, fonte_sigla)
"""

CATEGORIAS_PATOLOGIAS = [
    # (nome, sistema)
    ("Respiratória", "Aparelho respiratório"),
    ("Urinária", "Aparelho urinário"),
    ("Gastrointestinal", "Aparelho digestivo"),
    ("Cutânea / Tecidos moles", "Tegumento"),
    ("IST (Infecção Sexualmente Transmissível)", "Sistema reprodutor"),
    ("Neurológica / SNC", "Sistema nervoso central"),
    ("Cardiovascular", "Sistema cardiovascular"),
    ("Sistêmica / Zoonose", "Sistêmico / múltiplos órgãos"),
    ("Óssea / Articular", "Sistema musculoesquelético"),
    ("Neonatal / Perinatal", "Neonatal"),
    ("Hospitalar / IRAS", "Infecção relacionada à assistência à saúde"),
    ("Ocular", "Aparelho visual"),
    ("Micobacteriana", "Sistêmico / aparelho respiratório"),
    ("Anaerobiose / Toxigênica", "Sistêmico"),
    ("Outras", "Diversas"),
]

PATOLOGIAS = [
    # ── RESPIRATÓRIAS ──────────────────────────────────────────────────────────
    (
        "Pneumonia Adquirida na Comunidade (PAC) – Streptococcus pneumoniae",
        "J13", "Respiratória",
        "Infecção aguda do parênquima pulmonar por pneumococo; principal agente de PAC em adultos no Brasil.",
        False, None, "muito_alta", "alta", "Idosos, imunossuprimidos, sem vacinação", "SBI-PNEUM"
    ),
    (
        "Pneumonia Adquirida na Comunidade (PAC) – Haemophilus influenzae",
        "J14", "Respiratória",
        "PAC por H. influenzae não tipável; frequente em DPOC e tabagistas.",
        False, None, "alta", "media", "DPOC, tabagistas, idosos", "SBI-PNEUM"
    ),
    (
        "Pneumonia Atípica – Mycoplasma pneumoniae",
        "J15.7", "Respiratória",
        "Pneumonia atípica com tosse seca proeminente; epidemias em ciclos de 3-5 anos.",
        False, None, "alta", "baixa", "Crianças em idade escolar, adultos jovens", "SBI-PNEUM"
    ),
    (
        "Pneumonia Atípica – Chlamydophila pneumoniae",
        "J16.0", "Respiratória",
        "Pneumonia atípica; soroprevalência elevada na população brasileira adulta.",
        False, None, "alta", "baixa", "Adultos de todas as faixas etárias", "SBI-PNEUM"
    ),
    (
        "Pneumonia Hospitalar / Associada à Ventilação Mecânica (VAP)",
        "J95.851", "Hospitalar / IRAS",
        "Pneumonia após 48h de internação ou ventilação mecânica; agentes: P. aeruginosa, A. baumannii, K. pneumoniae.",
        False, None, "alta", "alta", "UTI, ventilação mecânica, imunossuprimidos", "ANVISA-IRAS"
    ),
    (
        "Tuberculose Pulmonar",
        "A15.0", "Micobacteriana",
        "Brasil entre os 30 países de alta carga; forma pulmonar responde por ~80% dos casos.",
        True, "semanal", "muito_alta", "media", "Pessoas em situação de rua, privados de liberdade, coinfectados pelo HIV", "PCDT-TB"
    ),
    (
        "Coqueluche (Pertussis)",
        "A37.0", "Respiratória",
        "Reemergência no Brasil desde 2011; lactentes < 6 meses têm maior mortalidade.",
        True, "imediata", "alta", "media", "Lactentes não vacinados, adultos sem reforço", "PCDT-COQUELUCHE"
    ),
    (
        "Difteria",
        "A36", "Respiratória",
        "Doença controlada pela vacinação no Brasil; surtos em populações não vacinadas.",
        True, "imediata", "baixa", "alta", "Crianças não vacinadas, comunidades rurais isoladas", "PCDT-DIFTERIA"
    ),
    (
        "Faringite / Amigdalite Estreptocócica",
        "J02.0", "Respiratória",
        "Infecção por S. pyogenes (grupo A); potencial para febre reumática se não tratada.",
        False, None, "muito_alta", "baixa", "Crianças 5-15 anos, adultos jovens", "GVS-MS"
    ),
    (
        "Otite Média Aguda Bacteriana",
        "H66.0", "Respiratória",
        "S. pneumoniae, H. influenzae e M. catarrhalis são os principais agentes.",
        False, None, "muito_alta", "baixa", "Crianças < 5 anos", "GVS-MS"
    ),
    (
        "Sinusite Bacteriana Aguda",
        "J01", "Respiratória",
        "Complicação de IVAS viral; S. pneumoniae e H. influenzae predominam.",
        False, None, "muito_alta", "baixa", "Adultos, crianças em idade escolar", "GVS-MS"
    ),
    (
        "Bronquite Bacteriana Aguda",
        "J20.9", "Respiratória",
        "Em geral secundária a infecção viral; agentes: H. influenzae, S. pneumoniae.",
        False, None, "muito_alta", "baixa", "DPOC, tabagistas, idosos", "GVS-MS"
    ),
    (
        "Epiglotite Bacteriana Aguda",
        "J05.1", "Respiratória",
        "H. influenzae tipo b (raro com vacinação); emergência respiratória.",
        False, None, "baixa", "alta", "Crianças não vacinadas, adultos imunossuprimidos", "GVS-MS"
    ),
    (
        "Abscesso Pulmonar Bacteriano",
        "J85.1", "Respiratória",
        "Infecção polimicrobiana com anaeróbios; S. aureus após pneumonia aspirativa.",
        False, None, "media", "media", "Alcoolistas, disfagia, imunossuprimidos", "GVS-MS"
    ),
    (
        "Empiema Pleural Bacteriano",
        "J86.9", "Respiratória",
        "Complicação de pneumonia; S. aureus, S. pneumoniae, Enterobacteriaceae.",
        False, None, "media", "media", "Pós-pneumonia, trauma torácico, cirurgia", "GVS-MS"
    ),

    # ── URINÁRIAS ──────────────────────────────────────────────────────────────
    (
        "Cistite Não Complicada – Escherichia coli",
        "N30.0", "Urinária",
        "E. coli responde por ~75-85% das ITU comunitárias; principal causa de ITU em mulheres.",
        False, None, "muito_alta", "baixa", "Mulheres em idade reprodutiva", "SBI-ITU"
    ),
    (
        "Pielonefrite Aguda – Escherichia coli",
        "N10", "Urinária",
        "Infecção do parênquima renal; pode evoluir para sepse.",
        False, None, "alta", "media", "Mulheres, gestantes, obstruções urinárias", "SBI-ITU"
    ),
    (
        "ITU Complicada – Klebsiella pneumoniae",
        "N39.0", "Urinária",
        "Frequente em hospitalizados e usuários de cateter; ESBL e KPC são desafios.",
        False, None, "alta", "media", "Hospitalizados, cateter vesical, imunossuprimidos", "SBI-ITU"
    ),
    (
        "ITU por Enterococcus spp.",
        "N39.0", "Urinária",
        "Frequente em idosos, hospitalizados e após uso de cefalosporinas.",
        False, None, "alta", "baixa", "Idosos, UTI, uso prévio de cefalosporinas", "SBI-ITU"
    ),
    (
        "ITU por Proteus mirabilis",
        "N39.0", "Urinária",
        "Associado a cálculos de estruvita; produz urease; alcaliniza urina.",
        False, None, "media", "baixa", "Homens, cateter vesical, cálculos renais", "SBI-ITU"
    ),
    (
        "ITU Associada a Cateter (CAUTI)",
        "T83.5", "Hospitalar / IRAS",
        "Principal IRAS no Brasil; E. coli, K. pneumoniae, Candida spp., Enterococcus.",
        False, None, "muito_alta", "media", "Pacientes com sonda vesical de demora", "ANVISA-IRAS"
    ),
    (
        "Prostatite Bacteriana Aguda",
        "N41.0", "Urinária",
        "E. coli em > 70% dos casos; febre alta, calafrios, dor perineal.",
        False, None, "media", "baixa", "Homens adultos, especialmente > 50 anos", "SBI-ITU"
    ),
    (
        "ITU Gestacional / Bacteriúria Assintomática na Gravidez",
        "O23.4", "Neonatal / Perinatal",
        "Rastreamento obrigatório; se não tratada, risco de pielonefrite e parto prematuro.",
        False, None, "alta", "baixa", "Gestantes", "GVS-MS"
    ),
    (
        "Staphylococcus saprophyticus – ITU em Mulheres Jovens",
        "N30.0", "Urinária",
        "Segunda causa de cistite em mulheres jovens sexualmente ativas.",
        False, None, "alta", "baixa", "Mulheres jovens sexualmente ativas", "SBI-ITU"
    ),

    # ── GASTROINTESTINAIS ──────────────────────────────────────────────────────
    (
        "Gastroenterite por Salmonella não-tífica",
        "A02.0", "Gastrointestinal",
        "Principal causa de surto alimentar bacteriano notificado no Brasil; aves e ovos são vetores.",
        False, None, "muito_alta", "baixa", "Toda a população; crianças e idosos mais graves", "GVS-MS"
    ),
    (
        "Febre Tifoide",
        "A01.0", "Gastrointestinal",
        "Salmonella Typhi; transmissão feco-oral; endêmica em áreas de saneamento precário.",
        True, "semanal", "media", "media", "Áreas sem saneamento, viajantes", "PCDT-FEBRETIFO"
    ),
    (
        "Gastroenterite por Campylobacter jejuni",
        "A04.5", "Gastrointestinal",
        "Principal causa bacteriana de diarreia aguda; transmissão por aves mal-cozidas.",
        False, None, "muito_alta", "baixa", "Crianças, adultos jovens", "GVS-MS"
    ),
    (
        "Shigelose (Disenteria Bacilar)",
        "A03", "Gastrointestinal",
        "S. sonnei predomina no Brasil urbano; S. dysenteriae causa formas mais graves.",
        False, None, "media", "media", "Crianças, áreas sem saneamento", "GVS-MS"
    ),
    (
        "Infecção por Escherichia coli Enteropatogênica (EPEC/ETEC)",
        "A04.0", "Gastrointestinal",
        "Diarreia do viajante; EPEC é importante em menores de 2 anos no Brasil.",
        False, None, "alta", "media", "Crianças < 2 anos, viajantes", "GVS-MS"
    ),
    (
        "Cólera",
        "A00", "Gastrointestinal",
        "Vibrio cholerae O1/O139; último grande surto no Brasil 1991-2005; vigilância ativa.",
        True, "imediata", "baixa", "alta", "Populações sem acesso a água potável e saneamento", "PCDT-COLERA"
    ),
    (
        "Infecção por Helicobacter pylori / Gastrite Crônica Ativa",
        "B96.81", "Gastrointestinal",
        "Prevalência ~60-70% em adultos brasileiros; principal fator de risco para úlcera péptica e câncer gástrico.",
        False, None, "muito_alta", "baixa", "Toda a população adulta; maior prevalência em baixo nível socioeconômico", "GVS-MS"
    ),
    (
        "Infecção por Clostridioides difficile (CDI)",
        "A04.7", "Gastrointestinal",
        "Crescente no Brasil associada ao uso de antibióticos; formas graves com colite pseudomembranosa.",
        False, None, "alta", "media", "Hospitalizados, uso de antibióticos, idosos", "ANVISA-IRAS"
    ),
    (
        "Peritonite Bacteriana Primária (Espontânea)",
        "K65.0", "Gastrointestinal",
        "Infecção do líquido ascítico em cirróticos; E. coli e Klebsiella predominam.",
        False, None, "media", "alta", "Cirróticos com ascite", "GVS-MS"
    ),
    (
        "Abscesso Hepático Bacteriano",
        "K75.0", "Gastrointestinal",
        "K. pneumoniae hipermucoviscosa emergindo no Brasil; E. coli e anaeróbios também frequentes.",
        False, None, "media", "media", "Adultos com comorbidades hepatobiliares", "GVS-MS"
    ),
    (
        "Colangite Bacteriana Aguda",
        "K83.0", "Gastrointestinal",
        "Tríade de Charcot: febre, icterícia, dor; E. coli, Klebsiella, Enterococcus.",
        False, None, "media", "alta", "Colelitíase, procedimentos biliares, idosos", "GVS-MS"
    ),
    (
        "Apendicite Bacteriana Secundária",
        "K37", "Gastrointestinal",
        "Flora mista colônica (E. coli, Bacteroides fragilis); antibióticos pré-cirúrgicos reduzem complicações.",
        False, None, "muito_alta", "baixa", "Adultos jovens, crianças", "GVS-MS"
    ),

    # ── CUTÂNEAS / TECIDOS MOLES ──────────────────────────────────────────────
    (
        "Impetigo – Staphylococcus aureus / Streptococcus pyogenes",
        "L01", "Cutânea / Tecidos moles",
        "Infecção cutânea superficial; muito frequente em crianças no Brasil tropical.",
        False, None, "muito_alta", "baixa", "Crianças em áreas tropicais, baixo nível socioeconômico", "GVS-MS"
    ),
    (
        "Celulite Bacteriana",
        "L03", "Cutânea / Tecidos moles",
        "S. pyogenes e S. aureus; porta de entrada frequente em picadas, micoses plantares.",
        False, None, "muito_alta", "baixa", "Adultos com linfedema, obesidade, diabetes", "GVS-MS"
    ),
    (
        "Erisipela",
        "A46", "Cutânea / Tecidos moles",
        "S. pyogenes; eritema demarcado com calafrio; membros inferiores são mais afetados no Brasil.",
        False, None, "muito_alta", "baixa", "Idosos, linfedema, insuficiência venosa", "GVS-MS"
    ),
    (
        "Furunculose / Carbúnculo – Staphylococcus aureus",
        "L02", "Cutânea / Tecidos moles",
        "Infecção de folículo piloso; MRSA comunitário (CA-MRSA) emergindo no Brasil.",
        False, None, "muito_alta", "baixa", "Toda a população; maior em diabetes, obesos", "GVS-MS"
    ),
    (
        "Fasciíte Necrotizante",
        "M72.6", "Cutânea / Tecidos moles",
        "Emergência cirúrgica; tipo I polimicrobiana ou tipo II por S. pyogenes.",
        False, None, "baixa", "alta", "Diabéticos, imunossuprimidos, pós-cirúrgico", "GVS-MS"
    ),
    (
        "Infecção por MRSA Comunitário (CA-MRSA)",
        "A49.0", "Cutânea / Tecidos moles",
        "Surgindo no Brasil; lesões cutâneas recorrentes em jovens saudáveis.",
        False, None, "media", "media", "Jovens, atletas, presidiários, militares", "ANVISA-SCIH"
    ),
    (
        "Hanseníase (Lepra)",
        "A30", "Micobacteriana",
        "Brasil é o 2º país em número de casos no mundo; norte e nordeste têm maior endemicidade.",
        True, "semanal", "alta", "baixa", "Populações em áreas endêmicas, baixo nível socioeconômico", "PCDT-HANSENR"
    ),
    (
        "Úlcera de Buruli – Mycobacterium ulcerans",
        "A31.1", "Cutânea / Tecidos moles",
        "Rara no Brasil; casos descritos na Amazônia; úlcera destrutiva indolor.",
        False, None, "rara", "baixa", "Populações ribeirinhas amazônicas", "GVS-MS"
    ),

    # ── IST ────────────────────────────────────────────────────────────────────
    (
        "Sífilis (adquirida, primária a terciária)",
        "A51–A53", "IST (Infecção Sexualmente Transmissível)",
        "Epidemia em curso no Brasil; crescimento em jovens 15-24 anos e gestantes.",
        True, "semanal", "muito_alta", "media", "Adultos jovens sexualmente ativos, gestantes", "PCDT-IST"
    ),
    (
        "Sífilis Congênita",
        "A50", "Neonatal / Perinatal",
        "Transmissão vertical; Brasil tem alta incidência apesar de ser prevenível com pré-natal.",
        True, "imediata", "muito_alta", "media", "Recém-nascidos de mães com sífilis não tratada", "PCDT-IST"
    ),
    (
        "Gonorreia (Neisseria gonorrhoeae)",
        "A54", "IST (Infecção Sexualmente Transmissível)",
        "Segunda IST bacteriana mais notificada; resistência crescente às quinolonas no Brasil.",
        True, "semanal", "muito_alta", "baixa", "Adultos jovens sexualmente ativos", "PCDT-IST"
    ),
    (
        "Infecção por Chlamydia trachomatis",
        "A56", "IST (Infecção Sexualmente Transmissível)",
        "IST bacteriana mais prevalente no Brasil; muitas vezes assintomática.",
        False, None, "muito_alta", "baixa", "Adultos jovens sexualmente ativos, adolescentes", "PCDT-IST"
    ),
    (
        "Cancro Mole (Haemophilus ducreyi)",
        "A57", "IST (Infecção Sexualmente Transmissível)",
        "Úlcera genital dolorosa; mais comum no Norte/Nordeste do Brasil.",
        True, "semanal", "media", "baixa", "Adultos sexualmente ativos, profissionais do sexo", "PCDT-IST"
    ),
    (
        "Linfogranuloma Venéreo (Chlamydia trachomatis L1-L3)",
        "A55", "IST (Infecção Sexualmente Transmissível)",
        "Reemergência no Brasil entre HSH; linfadenopatia inguinal e proctite.",
        True, "semanal", "media", "baixa", "HSH, adultos jovens", "PCDT-IST"
    ),

    # ── NEUROLÓGICAS / SNC ────────────────────────────────────────────────────
    (
        "Meningite Bacteriana por Neisseria meningitidis",
        "A39.0", "Neurológica / SNC",
        "Sorogrupos B e C predominam; alta mortalidade sem tratamento imediato.",
        True, "imediata", "alta", "alta", "Crianças < 5 anos, adolescentes, adultos jovens", "PCDT-MENIN"
    ),
    (
        "Meningite Bacteriana por Streptococcus pneumoniae",
        "G00.1", "Neurológica / SNC",
        "Maior mortalidade entre as meningites bacterianas; sequelas neurológicas frequentes.",
        True, "imediata", "alta", "alta", "Extremos de idade, asplênicos, imunossuprimidos", "PCDT-MENIN"
    ),
    (
        "Meningite Bacteriana por Haemophilus influenzae",
        "G00.0", "Neurológica / SNC",
        "Rara com vacinação Hib; predomina em não vacinados e adultos imunocomprometidos.",
        True, "imediata", "baixa", "alta", "Crianças não vacinadas, imunossuprimidos", "PCDT-MENIN"
    ),
    (
        "Meningite Neonatal por Streptococcus agalactiae (GBS)",
        "G00.2", "Neurológica / SNC",
        "Principal causa de meningite neonatal tardia; colonização materna = fator de risco.",
        True, "imediata", "media", "alta", "Recém-nascidos de mães GBS positivas", "PCDT-MENIN"
    ),
    (
        "Meningite por Listeria monocytogenes",
        "G00.7", "Neurológica / SNC",
        "Imunocomprometidos, idosos, gestantes; intrínseco a cefalosporinas.",
        True, "imediata", "baixa", "alta", "Gestantes, idosos, imunossuprimidos, HIV", "PCDT-MENIN"
    ),
    (
        "Abscesso Cerebral Bacteriano",
        "G06.0", "Neurológica / SNC",
        "Polimicrobiano; S. aureus pós-trauma, estreptococos orais por contiguidade.",
        False, None, "baixa", "alta", "Pós-neurocirurgia, trauma craniofacial, cardiopatia congênita", "GVS-MS"
    ),

    # ── CARDIOVASCULARES ─────────────────────────────────────────────────────
    (
        "Endocardite Infecciosa por Staphylococcus aureus",
        "I33.0", "Cardiovascular",
        "Principal causa de endocardite aguda; alta mortalidade; usuários de drogas IV em risco.",
        False, None, "media", "alta", "Usuários de drogas IV, dispositivos intravasculares, hemodiálise", "GVS-MS"
    ),
    (
        "Endocardite Infecciosa por Streptococcus viridans",
        "I33.0", "Cardiovascular",
        "Endocardite subaguda; valvopatia pré-existente é fator predisponente.",
        False, None, "media", "media", "Cardiopatias valvares, procedimentos odontológicos", "GVS-MS"
    ),
    (
        "Endocardite por Enterococcus",
        "I33.0", "Cardiovascular",
        "Terceira causa de endocardite; idosos, manipulação urológica ou gastrointestinal.",
        False, None, "media", "media", "Idosos, procedimentos gastrointestinais / urológicos", "GVS-MS"
    ),
    (
        "Febre Reumática Aguda",
        "I00", "Cardiovascular",
        "Sequela de faringite não tratada por S. pyogenes; cardite reumática causa valvopatia crônica.",
        False, None, "alta", "media", "Crianças e adolescentes em áreas de baixa renda", "GVS-MS"
    ),
    (
        "Pericardite Bacteriana",
        "I30.1", "Cardiovascular",
        "S. aureus, Mycobacterium tuberculosis, streptococos; tamponamento cardíaco é complicação.",
        False, None, "baixa", "alta", "Imunossuprimidos, pós-cirurgia cardíaca, TB ativa", "GVS-MS"
    ),

    # ── SISTÊMICA / ZOONOSES ─────────────────────────────────────────────────
    (
        "Leptospirose",
        "A27", "Sistêmica / Zoonose",
        "Endêmica no Brasil; pico em enchentes; formas graves com síndrome de Weil.",
        True, "imediata", "alta", "alta", "Trabalhadores em contato com água/solo, moradores de áreas alagadas", "PCDT-LEPTO"
    ),
    (
        "Febre Maculosa Brasileira (Rickettsia rickettsii)",
        "A77.0", "Sistêmica / Zoonose",
        "Alta letalidade (>80% sem tratamento); transmitida por carrapatos; foco principal: SP, MG, RJ.",
        True, "imediata", "media", "alta", "Exposição a carrapatos em área endêmica", "PCDT-RICKETTSIA"
    ),
    (
        "Rickettsioses (outras espécies)",
        "A77.9", "Sistêmica / Zoonose",
        "R. parkeri, R. amblyommatis; formas menos letais que R. rickettsii; transmissão por carrapatos.",
        True, "imediata", "media", "media", "Zona rural, exposição a carrapatos", "PCDT-RICKETTSIA"
    ),
    (
        "Brucelose",
        "A23", "Sistêmica / Zoonose",
        "Zoonose de bovinos e suínos; trabalhadores rurais e de frigoríficos são mais expostos no Brasil.",
        True, "semanal", "media", "baixa", "Veterinários, trabalhadores rurais, consumidores de laticínios não pasteurizados", "PCDT-BRUCELOSE"
    ),
    (
        "Bartonellose (Doença da Arranhadura do Gato)",
        "A28.1", "Sistêmica / Zoonose",
        "B. henselae; linfadenopatia regional; angiomatose bacilar em imunossuprimidos.",
        False, None, "media", "baixa", "Contato com gatos, imunossuprimidos (HIV)", "GVS-MS"
    ),
    (
        "Peste Bubônica (Yersinia pestis)",
        "A20.0", "Sistêmica / Zoonose",
        "Focos endêmicos residuais no semi-árido nordestino; transmissão por pulgas de roedores.",
        True, "imediata", "rara", "alta", "Populações rurais do semi-árido nordestino", "GVS-MS"
    ),
    (
        "Tularemia",
        "A21", "Sistêmica / Zoonose",
        "Rara no Brasil; casos esporádicos; transmissão por lagomorfos/roedores.",
        True, "imediata", "rara", "media", "Caçadores, trabalhadores rurais", "GVS-MS"
    ),
    (
        "Febre Relapsante (Borrelia spp.)",
        "A68", "Sistêmica / Zoonose",
        "Transmitida por carrapatos Ornithodoros; focos no Centro-Oeste e Norte do Brasil.",
        False, None, "baixa", "media", "Moradores e visitantes de zonas rurais", "GVS-MS"
    ),
    (
        "Melioidose (Burkholderia pseudomallei)",
        "A24.4", "Sistêmica / Zoonose",
        "Emergente no nordeste do Brasil (solo / água); formas graves em diabéticos.",
        True, "imediata", "baixa", "alta", "Diabéticos, áreas endêmicas do nordeste, trabalhadores rurais", "GVS-MS"
    ),

    # ── ÓSSEAS / ARTICULARES ─────────────────────────────────────────────────
    (
        "Osteomielite Hematogênica – Staphylococcus aureus",
        "M86.0", "Óssea / Articular",
        "S. aureus é o agente predominante em todas as faixas etárias.",
        False, None, "media", "media", "Crianças (hematogênica), adultos diabéticos (pé diabético)", "GVS-MS"
    ),
    (
        "Artrite Séptica Bacteriana",
        "M00", "Óssea / Articular",
        "S. aureus predomina; N. gonorrhoeae em jovens sexualmente ativos; destruição articular rápida.",
        False, None, "media", "media", "Próteses articulares, imunossuprimidos, usuários de drogas IV", "GVS-MS"
    ),
    (
        "Espondilodiscite Bacteriana",
        "M46.2", "Óssea / Articular",
        "S. aureus, Brucella, Mycobacterium tuberculosis; diagnóstico frequentemente tardio.",
        False, None, "media", "media", "Hemodialisados, usuários de drogas IV, idosos", "GVS-MS"
    ),
    (
        "Infecção de Prótese Articular (PJI)",
        "T84.5", "Hospitalar / IRAS",
        "Biofilme de S. epidermidis e S. aureus; tratamento requer retirada do implante em geral.",
        False, None, "media", "baixa", "Portadores de próteses articulares, imunossuprimidos", "ANVISA-IRAS"
    ),

    # ── NEONATAL / PERINATAL ─────────────────────────────────────────────────
    (
        "Sepse Neonatal Precoce por Streptococcus agalactiae (GBS)",
        "P36.0", "Neonatal / Perinatal",
        "Transmissão vertical; rastreamento materno e profilaxia intraparto reduzem incidência.",
        False, None, "alta", "alta", "Recém-nascidos de mães GBS+ sem profilaxia, prematuros", "GVS-MS"
    ),
    (
        "Sepse Neonatal por Escherichia coli",
        "P36.4", "Neonatal / Perinatal",
        "Segunda causa de sepse neonatal; cepas K1 com cápsula de ácido siálico são virulentas.",
        False, None, "alta", "alta", "Recém-nascidos prematuros, baixo peso", "GVS-MS"
    ),
    (
        "Listeriose Neonatal",
        "P37.2", "Neonatal / Perinatal",
        "Transmissão transplacentária ou intraparto; forma septicêmica precoce ou meningítica tardia.",
        True, "imediata", "baixa", "alta", "Recém-nascidos de mães infectadas, prematuros", "GVS-MS"
    ),

    # ── HOSPITALAR / IRAS ────────────────────────────────────────────────────
    (
        "Sepse por Klebsiella pneumoniae KPC",
        "A49.8", "Hospitalar / IRAS",
        "KPC = Klebsiella pneumoniae carbapenemase; alta mortalidade; opções terapêuticas limitadas.",
        False, None, "alta", "alta", "UTI, imunossuprimidos, transplantados, longa internação", "ANVISA-IRAS"
    ),
    (
        "Infecção por Acinetobacter baumannii Resistente a Carbapenens (CRAB)",
        "A49.8", "Hospitalar / IRAS",
        "CRAB é ameaça crítica; surtos em UTI; polimixinas são última linha no Brasil.",
        False, None, "alta", "alta", "UTI, ventilação mecânica, queimados, politrauma", "ANVISA-IRAS"
    ),
    (
        "Infecção por Pseudomonas aeruginosa MDR",
        "A49.8", "Hospitalar / IRAS",
        "MDR ou XDR; frequente em UTI; mucoviscosidade em fibrocísticos.",
        False, None, "alta", "alta", "UTI, fibrose cística, queimados, imunossuprimidos", "ANVISA-IRAS"
    ),
    (
        "Bacteremia por S. aureus MRSA Hospitalar (HA-MRSA)",
        "A49.0", "Hospitalar / IRAS",
        "Cateter venoso central como porta de entrada; endocardite como complicação.",
        False, None, "alta", "alta", "UTI, hemodiálise, cirurgias cardíacas", "ANVISA-SCIH"
    ),
    (
        "Infecção de Corrente Sanguínea por Enterococcus Vancomicina-Resistente (VRE)",
        "A49.8", "Hospitalar / IRAS",
        "VRE crescente no Brasil; transplantados e oncológicos são mais afetados.",
        False, None, "media", "alta", "UTI, transplantados, oncológicos, hematologia", "ANVISA-IRAS"
    ),
    (
        "Infecção Relacionada a Cateter Venoso Central (CRBSI)",
        "T80.2", "Hospitalar / IRAS",
        "Coagulase-negativos e S. aureus predominam; bundles de prevenção reduzem incidência.",
        False, None, "alta", "media", "UTI, onco-hematologia, hemodiálise", "ANVISA-IRAS"
    ),
    (
        "Infecção de Sítio Cirúrgico (ISC)",
        "T81.4", "Hospitalar / IRAS",
        "S. aureus, S. epidermidis, gram-negativos; profilaxia antimicrobiana perioperatória reduz risco.",
        False, None, "muito_alta", "media", "Pós-operatório de cirurgia limpa contaminada ou contaminada", "ANVISA-SCIH"
    ),

    # ── OCULAR ───────────────────────────────────────────────────────────────
    (
        "Conjuntivite Bacteriana Aguda",
        "H10.0", "Ocular",
        "S. aureus, H. influenzae, S. pneumoniae; muito frequente em crianças.",
        False, None, "muito_alta", "baixa", "Crianças, usuários de lentes de contato", "GVS-MS"
    ),
    (
        "Tracoma (Chlamydia trachomatis ocular)",
        "A71", "Ocular",
        "Principal causa infecciosa de cegueira no mundo; endêmico em regiões semi-áridas do Brasil.",
        True, "semanal", "media", "baixa", "Regiões semi-áridas nordestinas, baixo nível socioeconômico", "GVS-MS"
    ),
    (
        "Endoftalmite Bacteriana Pós-operatória",
        "H44.0", "Ocular",
        "S. epidermidis, S. aureus; complicação grave de cirurgia ocular; risco de cegueira.",
        False, None, "baixa", "baixa", "Pós-cirurgia ocular, trauma ocular", "GVS-MS"
    ),

    # ── ANAEROBIOSE / TOXIGÊNICAS ─────────────────────────────────────────────
    (
        "Tétano Acidental",
        "A35", "Anaerobiose / Toxigênica",
        "Clostridium tetani; ferimentos contaminados com solo em não vacinados.",
        True, "semanal", "media", "alta", "Adultos não vacinados, trabalhadores rurais", "PCDT-TETANO"
    ),
    (
        "Tétano Neonatal",
        "A33", "Anaerobiose / Toxigênica",
        "Corte do coto umbilical em condições não higiênicas; quase eliminado no Brasil.",
        True, "imediata", "baixa", "alta", "Recém-nascidos de mães não vacinadas, partos domiciliares", "PCDT-TETANO"
    ),
    (
        "Botulismo Alimentar (Clostridium botulinum)",
        "A05.1", "Anaerobiose / Toxigênica",
        "Surtos esporádicos no Brasil; conservas caseiras e palmito são veículos históricos.",
        True, "imediata", "baixa", "alta", "Consumidores de conservas artesanais", "GVS-MS"
    ),
    (
        "Gangrena Gasosa (Clostridium perfringens)",
        "A48.0", "Anaerobiose / Toxigênica",
        "Emergência cirúrgica; ferimentos profundos com isquemia.",
        False, None, "baixa", "alta", "Trauma grave, ferimentos profundos, pós-operatório vascular", "GVS-MS"
    ),
    (
        "Síndrome do Choque Tóxico Estafilocócico",
        "A48.3", "Anaerobiose / Toxigênica",
        "Toxina TSST-1 de S. aureus; febre, hipotensão, eritrodermia difusa.",
        False, None, "baixa", "alta", "Uso de tampões, ferimentos infectados, pós-operatório", "GVS-MS"
    ),
    (
        "Síndrome do Choque Tóxico Estreptocócico",
        "A48.3", "Anaerobiose / Toxigênica",
        "S. pyogenes; fasciíte necrotizante associada frequentemente; alta mortalidade.",
        False, None, "baixa", "alta", "Ferimentos cutâneos, pós-varicela", "GVS-MS"
    ),

    # ── OUTRAS ───────────────────────────────────────────────────────────────
    (
        "Escarlatina (Streptococcus pyogenes)",
        "A38", "Respiratória",
        "Exantema após faringite estreptocócica; tratamento previne febre reumática.",
        False, None, "alta", "baixa", "Crianças 5-15 anos", "GVS-MS"
    ),
    (
        "Tuberculose Extra-pulmonar",
        "A16–A19", "Micobacteriana",
        "Ganglionar, pleural, óssea, renal, meníngea; mais frequente em imunossuprimidos e HIV.",
        True, "semanal", "alta", "media", "HIV/AIDS, imunossuprimidos, desnutridos", "PCDT-TB"
    ),
    (
        "Tuberculose Resistente (MDR/XDR-TB)",
        "A15.0", "Micobacteriana",
        "MDR: resistência a INH + rifampicina; XDR: + fluoroquinolonas e injetáveis de 2ª linha.",
        True, "imediata", "media", "alta", "Contatos de casos MDR, tratamentos prévios incompletos, HIV", "PCDT-TB"
    ),
    (
        "Actinomicose (Actinomyces israelii)",
        "A42", "Outras",
        "Infecção crônica granulomatosa; forma cervicofacial é a mais comum; responde a penicilina prolongada.",
        False, None, "baixa", "baixa", "Adultos com má higiene oral, pós-extração dentária", "GVS-MS"
    ),
    (
        "Nocardiose (Nocardia spp.)",
        "A43", "Outras",
        "Infecção pulmonar, cutânea ou disseminada; exclusivamente em imunossuprimidos.",
        False, None, "baixa", "media", "HIV/AIDS, transplantados, corticoterapia crônica", "GVS-MS"
    ),
    (
        "Sepse por Gram-negativos (bacteremia primária)",
        "A41.5", "Hospitalar / IRAS",
        "E. coli, Klebsiella, Pseudomonas; porta de entrada frequentemente urinária ou biliar.",
        False, None, "muito_alta", "alta", "Imunossuprimidos, hospitalizados, idosos, cirróticos", "SBI-SEPSE"
    ),
    (
        "Parotidite Bacteriana Supurativa",
        "K11.3", "Outras",
        "S. aureus; idosos desidratados, xerostomia por medicamentos; pós-cirúrgico.",
        False, None, "baixa", "baixa", "Idosos, desidratados, pós-operatório", "GVS-MS"
    ),
    (
        "Abscesso Dentário / Infecção Odontogênica",
        "K04.7", "Outras",
        "Flora mista oral anaeróbia e estreptococos; pode evoluir para celulite cervical profunda.",
        False, None, "muito_alta", "baixa", "Toda a população com acesso precário à saúde bucal", "GVS-MS"
    ),
    (
        "Difteria Cutânea",
        "A36.3", "Cutânea / Tecidos moles",
        "C. diphtheriae; feridas em regiões tropicais; quadro mais brando que difteria faríngea.",
        True, "imediata", "baixa", "baixa", "Regiões tropicais com baixa cobertura vacinal", "PCDT-DIFTERIA"
    ),
    (
        "Listeriose em Adultos Imunocomprometidos",
        "A32.1", "Outras",
        "Bacteremia e meningite; alimentos refrigerados industrializados são veículos (frios, queijos).",
        True, "imediata", "baixa", "alta", "Idosos, gestantes, HIV/AIDS, transplantados, oncológicos", "GVS-MS"
    ),
    (
        "Infecção por Mycoplasma hominis / Ureaplasma urealyticum",
        "A49.3", "IST (Infecção Sexualmente Transmissível)",
        "Uretrite não gonocócica, vaginose; papel etiológico em infertilidade discutido.",
        False, None, "alta", "baixa", "Adultos jovens sexualmente ativos", "PCDT-IST"
    ),
]

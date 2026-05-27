"""
Sintomatologia das patologias fúngicas.
Fontes: MS/PCDT, SBI, SBMT, CFM.
"""

SINTOMAS_FUNGICAS = [
    {
        "patologia_nome": "Paracoccidioidomicose (Blastomicose Sul-Americana)",
        "sintomas": [
            {"nome": "Lesões mucosas orofaríngeas ulceradas (estomatite moriforme)", "sistema": "digestivo", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "semanas a meses", "severidade": "grave", "ordem": 1},
            {"nome": "Tosse crônica com expectoração", "sistema": "respiratorio", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "meses a anos", "severidade": "moderada", "ordem": 2},
            {"nome": "Dispneia progressiva", "sistema": "respiratorio", "tipo": "cardinal", "frequencia": "comum", "onset_texto": "meses a anos", "severidade": "grave", "ordem": 3},
            {"nome": "Linfadenopatia cervical e abdominal", "sistema": "hematologico", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "semanas a meses", "severidade": "moderada", "ordem": 4},
            {"nome": "Perda de peso e anorexia", "sistema": "sistemico", "tipo": "sistemico", "frequencia": "muito_comum", "onset_texto": "meses", "severidade": "moderada", "ordem": 5},
            {"nome": "Lesões cutâneas papuloulcerosas", "sistema": "cutaneo", "tipo": "local", "frequencia": "comum", "onset_texto": "meses", "severidade": "moderada", "ordem": 6},
            {"nome": "Febre baixa intermitente", "sistema": "sistemico", "tipo": "sistemico", "frequencia": "comum", "onset_texto": "meses", "severidade": "leve", "ordem": 7},
        ],
    },
    {
        "patologia_nome": "Histoplasmose (Doença de Darling)",
        "sintomas": [
            {"nome": "Febre e mal-estar (forma leve)", "sistema": "sistemico", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "3-17 dias após exposição", "severidade": "leve", "ordem": 1},
            {"nome": "Tosse não produtiva", "sistema": "respiratorio", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "dias a semanas", "severidade": "leve", "ordem": 2},
            {"nome": "Cefaleia e mialgia", "sistema": "musculoesqueletico", "tipo": "sistemico", "frequencia": "muito_comum", "onset_texto": "dias", "severidade": "leve", "ordem": 3},
            {"nome": "Linfadenopatia hiliar e mediastinal", "sistema": "hematologico", "tipo": "cardinal", "frequencia": "comum", "onset_texto": "semanas", "severidade": "moderada", "ordem": 4},
            {"nome": "Febre persistente + hepatoesplenomegalia (disseminada)", "sistema": "digestivo", "tipo": "complicacao", "frequencia": "comum", "onset_texto": "dias a semanas (imunocompr.)", "severidade": "grave", "ordem": 5},
            {"nome": "Eritema nodoso ou eritema multiforme", "sistema": "cutaneo", "tipo": "local", "frequencia": "incomum", "onset_texto": "semanas", "severidade": "leve", "ordem": 6},
        ],
    },
    {
        "patologia_nome": "Criptococose (Meningite Criptocócica e Forma Pulmonar)",
        "sintomas": [
            {"nome": "Cefaleia insidiosa e progressiva", "sistema": "neurologico", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "semanas a meses", "severidade": "grave", "ordem": 1},
            {"nome": "Febre baixa e mal-estar", "sistema": "sistemico", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "semanas", "severidade": "leve", "ordem": 2},
            {"nome": "Rigidez de nuca (meningite)", "sistema": "neurologico", "tipo": "cardinal", "frequencia": "comum", "onset_texto": "semanas", "severidade": "grave", "ordem": 3},
            {"nome": "Confusão mental e letargia", "sistema": "neurologico", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "semanas", "severidade": "grave", "ordem": 4},
            {"nome": "Hipertensão intracraniana (papiledema, vômitos)", "sistema": "neurologico", "tipo": "complicacao", "frequencia": "muito_comum", "onset_texto": "semanas", "severidade": "grave", "ordem": 5},
            {"nome": "Fotofobia", "sistema": "ocular", "tipo": "local", "frequencia": "comum", "onset_texto": "semanas", "severidade": "leve", "ordem": 6},
        ],
    },
    {
        "patologia_nome": "Lobomicose (Lacaziose — Doença de Jorge Lobo)",
        "sintomas": [
            {"nome": "Nódulos queloidianos cutâneos crônicos em expostos", "sistema": "cutaneo", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "meses a anos", "severidade": "leve", "ordem": 1},
            {"nome": "Plaques verrucosas coalescentes", "sistema": "cutaneo", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "meses a anos", "severidade": "leve", "ordem": 2},
            {"nome": "Ausência de dor (lesões indolentes)", "sistema": "cutaneo", "tipo": "sistemico", "frequencia": "muito_comum", "onset_texto": "sempre", "severidade": "leve", "ordem": 3},
            {"nome": "Prurido leve", "sistema": "cutaneo", "tipo": "local", "frequencia": "comum", "onset_texto": "meses", "severidade": "leve", "ordem": 4},
        ],
    },
    {
        "patologia_nome": "Candidemia e Candidíase Invasiva",
        "sintomas": [
            {"nome": "Febre persistente sem resposta a antibióticos de largo espectro", "sistema": "sistemico", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "dias de internação", "severidade": "grave", "ordem": 1},
            {"nome": "Calafrios", "sistema": "sistemico", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "dias", "severidade": "moderada", "ordem": 2},
            {"nome": "Lesões cutâneas por embolização (candidemia)", "sistema": "cutaneo", "tipo": "local", "frequencia": "incomum", "onset_texto": "dias", "severidade": "moderada", "ordem": 3},
            {"nome": "Endoftalmite por Candida (lesões brancas na retina)", "sistema": "ocular", "tipo": "complicacao", "frequencia": "incomum", "onset_texto": "dias", "severidade": "grave", "ordem": 4},
            {"nome": "Choque séptico refratário", "sistema": "cardiovascular", "tipo": "complicacao", "frequencia": "comum", "onset_texto": "dias", "severidade": "grave", "ordem": 5},
        ],
    },
    {
        "patologia_nome": "Candidíase Orofaríngea (Sapinho / Muguete)",
        "sintomas": [
            {"nome": "Placas brancas removíveis em mucosa oral", "sistema": "digestivo", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "dias", "severidade": "leve", "ordem": 1},
            {"nome": "Eritema e ardência na mucosa", "sistema": "digestivo", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "dias", "severidade": "leve", "ordem": 2},
            {"nome": "Dor ou desconforto ao engolir", "sistema": "digestivo", "tipo": "local", "frequencia": "comum", "onset_texto": "dias", "severidade": "leve", "ordem": 3},
            {"nome": "Alteração do paladar", "sistema": "neurologico", "tipo": "local", "frequencia": "comum", "onset_texto": "dias", "severidade": "leve", "ordem": 4},
            {"nome": "Queilite angular (rágades)", "sistema": "cutaneo", "tipo": "local", "frequencia": "comum", "onset_texto": "dias a semanas", "severidade": "leve", "ordem": 5},
        ],
    },
    {
        "patologia_nome": "Candidíase Vaginal (Vulvovaginite por Candida)",
        "sintomas": [
            {"nome": "Prurido vulvovaginal intenso", "sistema": "outro", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "dias", "severidade": "moderada", "ordem": 1},
            {"nome": "Corrimento branco grumoso (tipo queijo cottage)", "sistema": "outro", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "dias", "severidade": "leve", "ordem": 2},
            {"nome": "Eritema e edema vulvar", "sistema": "outro", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "dias", "severidade": "leve", "ordem": 3},
            {"nome": "Disúria externa", "sistema": "urinario", "tipo": "local", "frequencia": "comum", "onset_texto": "dias", "severidade": "leve", "ordem": 4},
            {"nome": "Dispareunia", "sistema": "outro", "tipo": "local", "frequencia": "comum", "onset_texto": "dias", "severidade": "moderada", "ordem": 5},
        ],
    },
    {
        "patologia_nome": "Candidíase Esofágica",
        "sintomas": [
            {"nome": "Odinofagia (dor ao deglutir)", "sistema": "digestivo", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "dias", "severidade": "grave", "ordem": 1},
            {"nome": "Disfagia progressiva", "sistema": "digestivo", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "dias", "severidade": "grave", "ordem": 2},
            {"nome": "Dor retroesternal", "sistema": "digestivo", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "dias", "severidade": "moderada", "ordem": 3},
            {"nome": "Náuseas", "sistema": "digestivo", "tipo": "sistemico", "frequencia": "comum", "onset_texto": "dias", "severidade": "leve", "ordem": 4},
            {"nome": "Candidíase oral associada (50-70%)", "sistema": "digestivo", "tipo": "local", "frequencia": "muito_comum", "onset_texto": "junto ao quadro esofágico", "severidade": "leve", "ordem": 5},
        ],
    },
    {
        "patologia_nome": "Aspergilose Invasiva (Pulmonar e Disseminada)",
        "sintomas": [
            {"nome": "Febre persistente refratária a antibióticos", "sistema": "sistemico", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "dias de neutropenia", "severidade": "grave", "ordem": 1},
            {"nome": "Tosse e hemoptise", "sistema": "respiratorio", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "dias", "severidade": "grave", "ordem": 2},
            {"nome": "Dor pleurítica e atrito pleural", "sistema": "respiratorio", "tipo": "cardinal", "frequencia": "comum", "onset_texto": "dias", "severidade": "grave", "ordem": 3},
            {"nome": "Infiltrado pulmonar nodular com sinal do halo (TC)", "sistema": "respiratorio", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "dias", "severidade": "grave", "ordem": 4},
            {"nome": "Sinusite invasiva com dor facial e edema", "sistema": "otorrinolaringologico", "tipo": "local", "frequencia": "incomum", "onset_texto": "dias", "severidade": "grave", "ordem": 5},
            {"nome": "Disseminação cerebral (convulsões, AVC)", "sistema": "neurologico", "tipo": "complicacao", "frequencia": "incomum", "onset_texto": "semanas", "severidade": "grave", "ordem": 6},
        ],
    },
    {
        "patologia_nome": "Aspergilose Broncopulmonar Alérgica (ABPA)",
        "sintomas": [
            {"nome": "Asma de difícil controle (exacerbações recorrentes)", "sistema": "respiratorio", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "meses a anos", "severidade": "grave", "ordem": 1},
            {"nome": "Rolhas de muco (tampões de muco marrom)", "sistema": "respiratorio", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "exacerbações", "severidade": "moderada", "ordem": 2},
            {"nome": "Bronquiectasias centrais", "sistema": "respiratorio", "tipo": "complicacao", "frequencia": "muito_comum", "onset_texto": "meses a anos", "severidade": "grave", "ordem": 3},
            {"nome": "Eosinofilia sanguínea e IgE elevada", "sistema": "hematologico", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "diagnóstico", "severidade": "leve", "ordem": 4},
            {"nome": "Dispneia e tosse produtiva crônica", "sistema": "respiratorio", "tipo": "sistemico", "frequencia": "muito_comum", "onset_texto": "crônico", "severidade": "moderada", "ordem": 5},
        ],
    },
    {
        "patologia_nome": "Aspergiloma Pulmonar",
        "sintomas": [
            {"nome": "Hemoptise (pode ser maciça)", "sistema": "respiratorio", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "meses", "severidade": "grave", "ordem": 1},
            {"nome": "Tosse crônica", "sistema": "respiratorio", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "meses", "severidade": "leve", "ordem": 2},
            {"nome": "Fadiga e perda de peso", "sistema": "sistemico", "tipo": "sistemico", "frequencia": "comum", "onset_texto": "meses", "severidade": "leve", "ordem": 3},
            {"nome": "Assintomático em muitos casos", "sistema": "sistemico", "tipo": "sistemico", "frequencia": "muito_comum", "onset_texto": "descoberta incidental", "severidade": "leve", "ordem": 4},
            {"nome": "Sinal do menisco (halo aéreo em TC)", "sistema": "respiratorio", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "diagnóstico por imagem", "severidade": "leve", "ordem": 5},
        ],
    },
    {
        "patologia_nome": "Mucormicose / Zigomicose (Rinocerebral, Pulmonar, Cutânea)",
        "sintomas": [
            {"nome": "Dor facial e edema periorbital (rinocerebral)", "sistema": "otorrinolaringologico", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "dias", "severidade": "grave", "ordem": 1},
            {"nome": "Necrose nasal com escara preta", "sistema": "otorrinolaringologico", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "dias", "severidade": "grave", "ordem": 2},
            {"nome": "Ptose, proptose e oftalmoplegia", "sistema": "ocular", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "dias", "severidade": "grave", "ordem": 3},
            {"nome": "Febre alta e toxemia sistêmica", "sistema": "sistemico", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "dias", "severidade": "grave", "ordem": 4},
            {"nome": "Cefaleia e sinais de extensão cerebral", "sistema": "neurologico", "tipo": "complicacao", "frequencia": "muito_comum", "onset_texto": "dias", "severidade": "grave", "ordem": 5},
            {"nome": "Hemoptise maciça (forma pulmonar)", "sistema": "respiratorio", "tipo": "local", "frequencia": "comum", "onset_texto": "dias", "severidade": "grave", "ordem": 6},
        ],
    },
    {
        "patologia_nome": "Esporotricose (Cutânea Linfangítica, Cutânea Fixa e Disseminada)",
        "sintomas": [
            {"nome": "Nódulo subcutâneo firme no local de inoculação", "sistema": "cutaneo", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "1-12 semanas após trauma", "severidade": "leve", "ordem": 1},
            {"nome": "Úlcera indolente com bordas irregulares", "sistema": "cutaneo", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "semanas", "severidade": "leve", "ordem": 2},
            {"nome": "Linfangite nodular ascendente ('cordão linfático')", "sistema": "cutaneo", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "semanas", "severidade": "moderada", "ordem": 3},
            {"nome": "Ausência de dor significativa", "sistema": "cutaneo", "tipo": "sistemico", "frequencia": "muito_comum", "onset_texto": "variável", "severidade": "leve", "ordem": 4},
            {"nome": "Artrite fúngica (forma osteoarticular)", "sistema": "musculoesqueletico", "tipo": "complicacao", "frequencia": "incomum", "onset_texto": "meses", "severidade": "grave", "ordem": 5},
        ],
    },
    {
        "patologia_nome": "Cromoblastomicose",
        "sintomas": [
            {"nome": "Lesões verrucosas e nódulos cutâneos crônicos", "sistema": "cutaneo", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "meses a anos", "severidade": "moderada", "ordem": 1},
            {"nome": "Localização preferencial em membros inferiores", "sistema": "cutaneo", "tipo": "local", "frequencia": "muito_comum", "onset_texto": "meses a anos", "severidade": "leve", "ordem": 2},
            {"nome": "Prurido leve", "sistema": "cutaneo", "tipo": "local", "frequencia": "comum", "onset_texto": "meses", "severidade": "leve", "ordem": 3},
            {"nome": "Linfedema por obstrução", "sistema": "cutaneo", "tipo": "complicacao", "frequencia": "comum", "onset_texto": "meses a anos", "severidade": "moderada", "ordem": 4},
            {"nome": "Ausência de febre (forma localizada)", "sistema": "sistemico", "tipo": "sistemico", "frequencia": "muito_comum", "onset_texto": "tipicamente afebril", "severidade": "leve", "ordem": 5},
        ],
    },
    {
        "patologia_nome": "Micetoma Fúngico (Eumicetoma)",
        "sintomas": [
            {"nome": "Tumefação indolente no pé ou membro (tríade: nódulo + grãos + fístulas)", "sistema": "cutaneo", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "meses a anos", "severidade": "grave", "ordem": 1},
            {"nome": "Fístulas drenando grãos (pretos ou brancos)", "sistema": "cutaneo", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "meses a anos", "severidade": "grave", "ordem": 2},
            {"nome": "Destruição óssea progressiva", "sistema": "musculoesqueletico", "tipo": "complicacao", "frequencia": "muito_comum", "onset_texto": "meses a anos", "severidade": "grave", "ordem": 3},
            {"nome": "Ausência de dor intensa (dor leve)", "sistema": "cutaneo", "tipo": "sistemico", "frequencia": "muito_comum", "onset_texto": "variável", "severidade": "leve", "ordem": 4},
        ],
    },
    {
        "patologia_nome": "Feohifomicose",
        "sintomas": [
            {"nome": "Cisto subcutâneo único de parede escura", "sistema": "cutaneo", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "semanas a meses", "severidade": "leve", "ordem": 1},
            {"nome": "Abscesso cutâneo ou subcutâneo", "sistema": "cutaneo", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "semanas", "severidade": "leve", "ordem": 2},
            {"nome": "Sinusite crônica (forma rinossinusal)", "sistema": "otorrinolaringologico", "tipo": "local", "frequencia": "comum", "onset_texto": "semanas a meses", "severidade": "moderada", "ordem": 3},
            {"nome": "Encefalite (forma cerebral em imunocomprometidos)", "sistema": "neurologico", "tipo": "complicacao", "frequencia": "raro", "onset_texto": "semanas", "severidade": "grave", "ordem": 4},
        ],
    },
    {
        "patologia_nome": "Fusariose (Hialohifomicose por Fusarium)",
        "sintomas": [
            {"nome": "Febre persistente em neutropênico", "sistema": "sistemico", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "dias de neutropenia", "severidade": "grave", "ordem": 1},
            {"nome": "Lesões cutâneas dolorosas (nódulos necróticos)", "sistema": "cutaneo", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "dias", "severidade": "grave", "ordem": 2},
            {"nome": "Onicomicose ou paroníquia (porta de entrada)", "sistema": "cutaneo", "tipo": "prodromico", "frequencia": "comum", "onset_texto": "semanas antes", "severidade": "leve", "ordem": 3},
            {"nome": "Pneumonia em imunocomprometidos", "sistema": "respiratorio", "tipo": "complicacao", "frequencia": "comum", "onset_texto": "dias", "severidade": "grave", "ordem": 4},
        ],
    },
    {
        "patologia_nome": "Rinossinusite Fúngica (Invasiva e Alérgica)",
        "sintomas": [
            {"nome": "Dor facial intensa e progressiva", "sistema": "otorrinolaringologico", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "dias (invasiva)", "severidade": "grave", "ordem": 1},
            {"nome": "Obstrução nasal e epistaxe", "sistema": "otorrinolaringologico", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "dias", "severidade": "moderada", "ordem": 2},
            {"nome": "Edema periorbital e proptose (extensão orbitária)", "sistema": "ocular", "tipo": "complicacao", "frequencia": "comum", "onset_texto": "dias", "severidade": "grave", "ordem": 3},
            {"nome": "Febre (forma invasiva)", "sistema": "sistemico", "tipo": "sistemico", "frequencia": "muito_comum", "onset_texto": "dias", "severidade": "grave", "ordem": 4},
            {"nome": "Necrose do palato ou turbinados", "sistema": "otorrinolaringologico", "tipo": "cardinal", "frequencia": "comum", "onset_texto": "dias", "severidade": "grave", "ordem": 5},
        ],
    },
    {
        "patologia_nome": "Tinea Capitis (Tinha do Couro Cabeludo)",
        "sintomas": [
            {"nome": "Alopecia focal com escamas e eritema", "sistema": "cutaneo", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "dias a semanas", "severidade": "leve", "ordem": 1},
            {"nome": "Prurido do couro cabeludo", "sistema": "cutaneo", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "dias", "severidade": "leve", "ordem": 2},
            {"nome": "Querion (placa inflamatória supurativa)", "sistema": "cutaneo", "tipo": "cardinal", "frequencia": "comum", "onset_texto": "semanas", "severidade": "moderada", "ordem": 3},
            {"nome": "Linfadenopatia cervical posterior", "sistema": "hematologico", "tipo": "local", "frequencia": "comum", "onset_texto": "semanas", "severidade": "leve", "ordem": 4},
        ],
    },
    {
        "patologia_nome": "Tinea Corporis, Cruris e Faciei (Tinha do Corpo)",
        "sintomas": [
            {"nome": "Placa eritematosa com bordas elevadas e centro claro", "sistema": "cutaneo", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "dias a semanas", "severidade": "leve", "ordem": 1},
            {"nome": "Prurido intenso (especialmente com calor)", "sistema": "cutaneo", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "dias", "severidade": "leve", "ordem": 2},
            {"nome": "Expansão centrífuga da lesão", "sistema": "cutaneo", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "dias a semanas", "severidade": "leve", "ordem": 3},
            {"nome": "Eritema e descamação periférica", "sistema": "cutaneo", "tipo": "local", "frequencia": "muito_comum", "onset_texto": "dias", "severidade": "leve", "ordem": 4},
        ],
    },
    {
        "patologia_nome": "Tinea Pedis (Pé de Atleta) e Tinea Unguium (Onicomicose)",
        "sintomas": [
            {"nome": "Descamação e fissuras nos espaços interdigitais", "sistema": "cutaneo", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "semanas", "severidade": "leve", "ordem": 1},
            {"nome": "Prurido e ardência plantar", "sistema": "cutaneo", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "semanas", "severidade": "leve", "ordem": 2},
            {"nome": "Unhas espessadas, amareladas e quebradiças (onicomicose)", "sistema": "cutaneo", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "meses", "severidade": "leve", "ordem": 3},
            {"nome": "Odor fétido dos pés", "sistema": "cutaneo", "tipo": "local", "frequencia": "muito_comum", "onset_texto": "semanas", "severidade": "leve", "ordem": 4},
            {"nome": "Sobreinfecção bacteriana das fissuras", "sistema": "cutaneo", "tipo": "complicacao", "frequencia": "comum", "onset_texto": "semanas", "severidade": "moderada", "ordem": 5},
        ],
    },
    {
        "patologia_nome": "Pitiríase Versicolor (Tinea Versicolor)",
        "sintomas": [
            {"nome": "Máculas hipocrômicas ou hipercrômicas no tronco", "sistema": "cutaneo", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "semanas a meses", "severidade": "leve", "ordem": 1},
            {"nome": "Descamação furfurácea fina (ao raspar)", "sistema": "cutaneo", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "semanas", "severidade": "leve", "ordem": 2},
            {"nome": "Prurido leve ou ausente", "sistema": "cutaneo", "tipo": "local", "frequencia": "comum", "onset_texto": "variável", "severidade": "leve", "ordem": 3},
            {"nome": "Piora com calor e suor", "sistema": "cutaneo", "tipo": "sistemico", "frequencia": "muito_comum", "onset_texto": "variável sazonal", "severidade": "leve", "ordem": 4},
        ],
    },
    {
        "patologia_nome": "Dermatofitose Ungueal e Cutânea por Tricofíton (Tinea Manum e Tinea Barbae)",
        "sintomas": [
            {"nome": "Eritema e descamação inflamatória (tinea barbae folicular)", "sistema": "cutaneo", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "dias a semanas", "severidade": "moderada", "ordem": 1},
            {"nome": "Pústulas foliculares na barba", "sistema": "cutaneo", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "semanas", "severidade": "moderada", "ordem": 2},
            {"nome": "Espessamento e descamação das palmas (tinea manum)", "sistema": "cutaneo", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "semanas a meses", "severidade": "leve", "ordem": 3},
            {"nome": "Prurido local", "sistema": "cutaneo", "tipo": "local", "frequencia": "muito_comum", "onset_texto": "semanas", "severidade": "leve", "ordem": 4},
        ],
    },
    {
        "patologia_nome": "Pneumonia por Pneumocystis jirovecii (PCP)",
        "sintomas": [
            {"nome": "Dispneia progressiva de esforço a repouso", "sistema": "respiratorio", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "dias a semanas", "severidade": "grave", "ordem": 1},
            {"nome": "Tosse seca persistente", "sistema": "respiratorio", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "dias a semanas", "severidade": "moderada", "ordem": 2},
            {"nome": "Febre baixa e sudorese noturna", "sistema": "sistemico", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "dias a semanas", "severidade": "leve", "ordem": 3},
            {"nome": "Hipoxemia desproporcional à clínica", "sistema": "respiratorio", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "dias a semanas", "severidade": "grave", "ordem": 4},
            {"nome": "Fadiga e perda de peso", "sistema": "sistemico", "tipo": "sistemico", "frequencia": "muito_comum", "onset_texto": "semanas", "severidade": "moderada", "ordem": 5},
            {"nome": "Insuficiência respiratória grave", "sistema": "respiratorio", "tipo": "complicacao", "frequencia": "muito_comum", "onset_texto": "dias a semanas", "severidade": "grave", "ordem": 6},
        ],
    },
]

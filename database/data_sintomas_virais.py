"""
Sintomatologia das patologias virais.
Fontes: MS/SVS, PCDT, SBI, SBP, CFM.
"""

SINTOMAS_VIRAIS = [
    {
        "patologia_nome": "Dengue (formas leve, moderada e grave)",
        "sintomas": [
            {"nome": "Febre alta de início súbito (38,5–40°C)", "sistema": "sistemico", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "3-7 dias após picada", "severidade": "moderada", "ordem": 1},
            {"nome": "Cefaleia intensa retroorbitária", "sistema": "neurologico", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "1-3 dias", "severidade": "moderada", "ordem": 2},
            {"nome": "Mialgia e artralgia intensas ('quebra-ossos')", "sistema": "musculoesqueletico", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "1-3 dias", "severidade": "grave", "ordem": 3},
            {"nome": "Exantema maculopapular (ilhas de pele sã)", "sistema": "cutaneo", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "3-5 dias", "severidade": "leve", "ordem": 4},
            {"nome": "Plaquetopenia e leucopenia", "sistema": "hematologico", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "3-7 dias", "severidade": "moderada", "ordem": 5},
            {"nome": "Dor abdominal intensa (alarme)", "sistema": "digestivo", "tipo": "local", "frequencia": "comum", "onset_texto": "3-6 dias", "severidade": "grave", "ordem": 6},
            {"nome": "Sangramento (petéquias, epistaxe, gengivorragia)", "sistema": "hematologico", "tipo": "complicacao", "frequencia": "comum", "onset_texto": "3-7 dias", "severidade": "grave", "ordem": 7},
            {"nome": "Choque por dengue grave (hipotensão)", "sistema": "cardiovascular", "tipo": "complicacao", "frequencia": "incomum", "onset_texto": "3-7 dias", "severidade": "grave", "ordem": 8},
        ],
    },
    {
        "patologia_nome": "Zika (infecção aguda e síndrome congênita)",
        "sintomas": [
            {"nome": "Exantema maculopapular pruriginoso", "sistema": "cutaneo", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "3-12 dias após picada", "severidade": "leve", "ordem": 1},
            {"nome": "Febre baixa (37,5–38,5°C)", "sistema": "sistemico", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "3-7 dias", "severidade": "leve", "ordem": 2},
            {"nome": "Conjuntivite não purulenta", "sistema": "ocular", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "3-7 dias", "severidade": "leve", "ordem": 3},
            {"nome": "Artralgia e edema articular", "sistema": "musculoesqueletico", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "3-7 dias", "severidade": "leve", "ordem": 4},
            {"nome": "Síndrome de Guillain-Barré (complicação)", "sistema": "neurologico", "tipo": "complicacao", "frequencia": "incomum", "onset_texto": "1-4 semanas após", "severidade": "grave", "ordem": 5},
        ],
    },
    {
        "patologia_nome": "Chikungunya (aguda e crônica)",
        "sintomas": [
            {"nome": "Artralgia bilateral intensa (especialmente mãos e pés)", "sistema": "musculoesqueletico", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "2-12 dias após picada", "severidade": "grave", "ordem": 1},
            {"nome": "Febre alta súbita (≥39°C)", "sistema": "sistemico", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "2-4 dias", "severidade": "grave", "ordem": 2},
            {"nome": "Exantema maculopapular", "sistema": "cutaneo", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "2-5 dias", "severidade": "leve", "ordem": 3},
            {"nome": "Edema articular (poliartrite)", "sistema": "musculoesqueletico", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "2-5 dias", "severidade": "grave", "ordem": 4},
            {"nome": "Artropatia crônica (persistência >3 meses)", "sistema": "musculoesqueletico", "tipo": "complicacao", "frequencia": "muito_comum", "onset_texto": "meses", "severidade": "grave", "ordem": 5},
            {"nome": "Cefaleia e mialgia", "sistema": "musculoesqueletico", "tipo": "sistemico", "frequencia": "muito_comum", "onset_texto": "2-5 dias", "severidade": "leve", "ordem": 6},
        ],
    },
    {
        "patologia_nome": "Febre Amarela (silvestre e urbana)",
        "sintomas": [
            {"nome": "Febre alta, cefaleia e mialgia intensa (fase aguda)", "sistema": "sistemico", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "3-6 dias após picada", "severidade": "grave", "ordem": 1},
            {"nome": "Náuseas e vômitos", "sistema": "digestivo", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "3-6 dias", "severidade": "moderada", "ordem": 2},
            {"nome": "Bradicardia relativa (sinal de Faget)", "sistema": "cardiovascular", "tipo": "cardinal", "frequencia": "comum", "onset_texto": "fase aguda", "severidade": "leve", "ordem": 3},
            {"nome": "Icterícia intensa (fase tóxica)", "sistema": "digestivo", "tipo": "cardinal", "frequencia": "comum", "onset_texto": "3-6 dias fase tóxica", "severidade": "grave", "ordem": 4},
            {"nome": "Hemorragias (hematêmese, melena)", "sistema": "hematologico", "tipo": "complicacao", "frequencia": "comum", "onset_texto": "fase tóxica", "severidade": "grave", "ordem": 5},
            {"nome": "Insuficiência hepato-renal", "sistema": "digestivo", "tipo": "complicacao", "frequencia": "comum", "onset_texto": "fase tóxica", "severidade": "grave", "ordem": 6},
            {"nome": "Remissão transitória (entre fases)", "sistema": "sistemico", "tipo": "local", "frequencia": "muito_comum", "onset_texto": "12-24h entre fases", "severidade": "leve", "ordem": 7},
        ],
    },
    {
        "patologia_nome": "Febre do Nilo Ocidental (casos importados e autóctones)",
        "sintomas": [
            {"nome": "Febre, cefaleia e mialgia (forma leve)", "sistema": "sistemico", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "2-14 dias após picada", "severidade": "leve", "ordem": 1},
            {"nome": "Exantema maculopapular no tronco", "sistema": "cutaneo", "tipo": "local", "frequencia": "comum", "onset_texto": "3-7 dias", "severidade": "leve", "ordem": 2},
            {"nome": "Meningoencefalite (forma neuroinvasiva)", "sistema": "neurologico", "tipo": "complicacao", "frequencia": "incomum", "onset_texto": "dias a semanas", "severidade": "grave", "ordem": 3},
            {"nome": "Fraqueza muscular flácida", "sistema": "musculoesqueletico", "tipo": "complicacao", "frequencia": "raro", "onset_texto": "dias a semanas", "severidade": "grave", "ordem": 4},
        ],
    },
    {
        "patologia_nome": "Hepatite A",
        "sintomas": [
            {"nome": "Icterícia progressiva", "sistema": "digestivo", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "15-50 dias após exposição", "severidade": "moderada", "ordem": 1},
            {"nome": "Urina colúrica (cor de chá)", "sistema": "urinario", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "dias antes da icterícia", "severidade": "leve", "ordem": 2},
            {"nome": "Fezes acolúricas (claras)", "sistema": "digestivo", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "fase ictérica", "severidade": "leve", "ordem": 3},
            {"nome": "Náuseas, vômitos e anorexia (pródromo)", "sistema": "digestivo", "tipo": "prodromico", "frequencia": "muito_comum", "onset_texto": "1-2 semanas antes da icterícia", "severidade": "leve", "ordem": 4},
            {"nome": "Febre baixa (pródromo)", "sistema": "sistemico", "tipo": "prodromico", "frequencia": "muito_comum", "onset_texto": "1-2 semanas antes da icterícia", "severidade": "leve", "ordem": 5},
            {"nome": "Hepatomegalia dolorosa", "sistema": "digestivo", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "fase ictérica", "severidade": "leve", "ordem": 6},
        ],
    },
    {
        "patologia_nome": "Hepatite B (aguda e crônica)",
        "sintomas": [
            {"nome": "Icterícia (forma ictérica aguda)", "sistema": "digestivo", "tipo": "cardinal", "frequencia": "comum", "onset_texto": "45-180 dias após exposição", "severidade": "moderada", "ordem": 1},
            {"nome": "Fadiga e astenia (crônica)", "sistema": "sistemico", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "crônico", "severidade": "leve", "ordem": 2},
            {"nome": "Náuseas e dor no hipocôndrio direito", "sistema": "digestivo", "tipo": "cardinal", "frequencia": "comum", "onset_texto": "fase aguda", "severidade": "leve", "ordem": 3},
            {"nome": "Artralgia (fase prodromal)", "sistema": "musculoesqueletico", "tipo": "prodromico", "frequencia": "comum", "onset_texto": "semanas antes da icterícia", "severidade": "leve", "ordem": 4},
            {"nome": "Cirrose hepática (sequela crônica)", "sistema": "digestivo", "tipo": "complicacao", "frequencia": "comum", "onset_texto": "anos de infecção crônica", "severidade": "grave", "ordem": 5},
            {"nome": "Carcinoma hepatocelular (sequela)", "sistema": "digestivo", "tipo": "complicacao", "frequencia": "comum", "onset_texto": "décadas", "severidade": "grave", "ordem": 6},
        ],
    },
    {
        "patologia_nome": "Hepatite C (aguda e crônica)",
        "sintomas": [
            {"nome": "Maioria assintomática na fase aguda", "sistema": "sistemico", "tipo": "sistemico", "frequencia": "muito_comum", "onset_texto": "2-26 semanas", "severidade": "leve", "ordem": 1},
            {"nome": "Fadiga crônica", "sistema": "sistemico", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "fase crônica", "severidade": "moderada", "ordem": 2},
            {"nome": "Artralgia e mialgia", "sistema": "musculoesqueletico", "tipo": "sistemico", "frequencia": "comum", "onset_texto": "fase crônica", "severidade": "leve", "ordem": 3},
            {"nome": "Cirrose hepática (20–30% após 20 anos)", "sistema": "digestivo", "tipo": "complicacao", "frequencia": "muito_comum", "onset_texto": "após 20-30 anos", "severidade": "grave", "ordem": 4},
            {"nome": "Manifestações extra-hepáticas (crioglobulinemia, vasculite)", "sistema": "sistemico", "tipo": "complicacao", "frequencia": "incomum", "onset_texto": "fase crônica", "severidade": "moderada", "ordem": 5},
        ],
    },
    {
        "patologia_nome": "Hepatite D (Coinfecção e Superinfecção por HDV)",
        "sintomas": [
            {"nome": "Icterícia mais grave que hepatite B isolada", "sistema": "digestivo", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "coinfecção ou superinfecção", "severidade": "grave", "ordem": 1},
            {"nome": "Fadiga e anorexia intensas", "sistema": "sistemico", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "semanas", "severidade": "moderada", "ordem": 2},
            {"nome": "Hepatite fulminante (superinfecção)", "sistema": "digestivo", "tipo": "complicacao", "frequencia": "comum", "onset_texto": "dias a semanas", "severidade": "grave", "ordem": 3},
            {"nome": "Insuficiência hepática aguda grave", "sistema": "digestivo", "tipo": "complicacao", "frequencia": "comum", "onset_texto": "semanas", "severidade": "grave", "ordem": 4},
        ],
    },
    {
        "patologia_nome": "Hepatite E",
        "sintomas": [
            {"nome": "Icterícia", "sistema": "digestivo", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "15-60 dias após exposição", "severidade": "moderada", "ordem": 1},
            {"nome": "Náuseas, vômitos e dor abdominal", "sistema": "digestivo", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "pródromo 1-2 semanas antes", "severidade": "leve", "ordem": 2},
            {"nome": "Febre baixa", "sistema": "sistemico", "tipo": "prodromico", "frequencia": "muito_comum", "onset_texto": "pródromo", "severidade": "leve", "ordem": 3},
            {"nome": "Hepatite fulminante em gestantes", "sistema": "digestivo", "tipo": "complicacao", "frequencia": "comum", "onset_texto": "3º trimestre", "severidade": "grave", "ordem": 4},
            {"nome": "Prurido", "sistema": "cutaneo", "tipo": "local", "frequencia": "comum", "onset_texto": "fase ictérica", "severidade": "leve", "ordem": 5},
        ],
    },
    {
        "patologia_nome": "HIV/AIDS (infecção aguda, crônica e AIDS estabelecida)",
        "sintomas": [
            {"nome": "Síndrome retroviral aguda: febre, linfadenopatia, faringite", "sistema": "sistemico", "tipo": "prodromico", "frequencia": "muito_comum", "onset_texto": "2-4 semanas após exposição", "severidade": "moderada", "ordem": 1},
            {"nome": "Exantema maculopapular (fase aguda)", "sistema": "cutaneo", "tipo": "prodromico", "frequencia": "muito_comum", "onset_texto": "2-4 semanas", "severidade": "leve", "ordem": 2},
            {"nome": "Perda de peso >10% (AIDS)", "sistema": "sistemico", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "AIDS estabelecida", "severidade": "grave", "ordem": 3},
            {"nome": "Infecções oportunistas (pneumocistose, toxoplasmose, CMV)", "sistema": "sistemico", "tipo": "complicacao", "frequencia": "muito_comum", "onset_texto": "CD4 <200/mm³", "severidade": "grave", "ordem": 4},
            {"nome": "Candidíase oral (muguet)", "sistema": "digestivo", "tipo": "local", "frequencia": "muito_comum", "onset_texto": "imunodeficiência avançada", "severidade": "moderada", "ordem": 5},
            {"nome": "Diarreia crônica", "sistema": "digestivo", "tipo": "sistemico", "frequencia": "muito_comum", "onset_texto": "AIDS estabelecida", "severidade": "moderada", "ordem": 6},
            {"nome": "Demência associada ao HIV", "sistema": "neurologico", "tipo": "complicacao", "frequencia": "incomum", "onset_texto": "AIDS avançada", "severidade": "grave", "ordem": 7},
        ],
    },
    {
        "patologia_nome": "Infecção pelo HTLV-1 (portador e formas clínicas)",
        "sintomas": [
            {"nome": "Maioria portadora assintomática", "sistema": "sistemico", "tipo": "sistemico", "frequencia": "muito_comum", "onset_texto": "pode ser assintomático por décadas", "severidade": "leve", "ordem": 1},
            {"nome": "Paraparesia espástica progressiva (HAM/TSP)", "sistema": "neurologico", "tipo": "cardinal", "frequencia": "comum", "onset_texto": "anos a décadas", "severidade": "grave", "ordem": 2},
            {"nome": "Hipotonia de membros inferiores", "sistema": "neurologico", "tipo": "cardinal", "frequencia": "comum", "onset_texto": "anos", "severidade": "grave", "ordem": 3},
            {"nome": "Bexiga neurogênica e disfunção sexual", "sistema": "urinario", "tipo": "sistemico", "frequencia": "muito_comum", "onset_texto": "meses a anos após HAM", "severidade": "moderada", "ordem": 4},
            {"nome": "Linfoma/leucemia de células T (ATLL)", "sistema": "hematologico", "tipo": "complicacao", "frequencia": "incomum", "onset_texto": "décadas", "severidade": "grave", "ordem": 5},
        ],
    },
    {
        "patologia_nome": "Herpes Simples (orolabial, genital e neonatal)",
        "sintomas": [
            {"nome": "Vesículas dolorosas agrupadas sobre base eritematosa", "sistema": "cutaneo", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "2-12 dias após contato", "severidade": "moderada", "ordem": 1},
            {"nome": "Ardência, prurido e parestesia locais", "sistema": "cutaneo", "tipo": "prodromico", "frequencia": "muito_comum", "onset_texto": "12-24h antes das vesículas", "severidade": "leve", "ordem": 2},
            {"nome": "Linfadenopatia regional", "sistema": "hematologico", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "dias", "severidade": "leve", "ordem": 3},
            {"nome": "Febre (primoinfecção)", "sistema": "sistemico", "tipo": "sistemico", "frequencia": "muito_comum", "onset_texto": "primoinfecção", "severidade": "moderada", "ordem": 4},
            {"nome": "Úlceras confluentes (genital ou oral)", "sistema": "cutaneo", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "dias", "severidade": "moderada", "ordem": 5},
            {"nome": "Encefalite herpética (HSV-1)", "sistema": "neurologico", "tipo": "complicacao", "frequencia": "raro", "onset_texto": "semanas", "severidade": "grave", "ordem": 6},
        ],
    },
    {
        "patologia_nome": "Varicela (catapora)",
        "sintomas": [
            {"nome": "Exantema vesicular pruriginoso polimórfico", "sistema": "cutaneo", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "10-21 dias após exposição", "severidade": "leve", "ordem": 1},
            {"nome": "Febre baixa e mal-estar (pródromo)", "sistema": "sistemico", "tipo": "prodromico", "frequencia": "muito_comum", "onset_texto": "1-2 dias antes do exantema", "severidade": "leve", "ordem": 2},
            {"nome": "Prurido intenso", "sistema": "cutaneo", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "simultâneo ao exantema", "severidade": "leve", "ordem": 3},
            {"nome": "Lesões em diversos estágios simultâneos", "sistema": "cutaneo", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "2-7 dias", "severidade": "leve", "ordem": 4},
            {"nome": "Pneumonia varicelosa (adultos, gestantes)", "sistema": "respiratorio", "tipo": "complicacao", "frequencia": "incomum", "onset_texto": "3-7 dias após exantema", "severidade": "grave", "ordem": 5},
            {"nome": "Sobreinfecção bacteriana das lesões", "sistema": "cutaneo", "tipo": "complicacao", "frequencia": "comum", "onset_texto": "dias", "severidade": "moderada", "ordem": 6},
        ],
    },
    {
        "patologia_nome": "Herpes Zoster (cobreiro)",
        "sintomas": [
            {"nome": "Dor radicular unilateral (pródromo)", "sistema": "neurologico", "tipo": "prodromico", "frequencia": "muito_comum", "onset_texto": "1-5 dias antes do exantema", "severidade": "grave", "ordem": 1},
            {"nome": "Vesículas agrupadas em dermátomo unilateral", "sistema": "cutaneo", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "dias após pródromo", "severidade": "moderada", "ordem": 2},
            {"nome": "Ardência e alodinia no dermátomo", "sistema": "neurologico", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "junto ao exantema", "severidade": "grave", "ordem": 3},
            {"nome": "Neuralgia pós-herpética (dor >3 meses)", "sistema": "neurologico", "tipo": "complicacao", "frequencia": "muito_comum", "onset_texto": ">3 meses após cicatrização", "severidade": "grave", "ordem": 4},
            {"nome": "Zoster oftálmico (risco de ceratite)", "sistema": "ocular", "tipo": "complicacao", "frequencia": "comum", "onset_texto": "junto ao exantema V1", "severidade": "grave", "ordem": 5},
        ],
    },
    {
        "patologia_nome": "Citomegalovirose (CMV) em Imunocomprometidos",
        "sintomas": [
            {"nome": "Retinite (flashes, moscas volantes, perda visual)", "sistema": "ocular", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "CD4 <50/mm³", "severidade": "grave", "ordem": 1},
            {"nome": "Colite (dor abdominal, diarreia sanguinolenta)", "sistema": "digestivo", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "imunodeficiência grave", "severidade": "grave", "ordem": 2},
            {"nome": "Pneumonite intersticial", "sistema": "respiratorio", "tipo": "cardinal", "frequencia": "comum", "onset_texto": "pós-transplante ou AIDS avançada", "severidade": "grave", "ordem": 3},
            {"nome": "Febre e fadiga persistentes", "sistema": "sistemico", "tipo": "sistemico", "frequencia": "muito_comum", "onset_texto": "variável", "severidade": "moderada", "ordem": 4},
            {"nome": "Esofagite (disfagia, odinofagia)", "sistema": "digestivo", "tipo": "local", "frequencia": "comum", "onset_texto": "variável", "severidade": "moderada", "ordem": 5},
        ],
    },
    {
        "patologia_nome": "Mononucleose Infecciosa (EBV)",
        "sintomas": [
            {"nome": "Faringite exsudativa grave", "sistema": "otorrinolaringologico", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "30-50 dias após exposição", "severidade": "grave", "ordem": 1},
            {"nome": "Adenopatia cervical posterior", "sistema": "hematologico", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "dias", "severidade": "moderada", "ordem": 2},
            {"nome": "Esplenomegalia", "sistema": "digestivo", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "1-2 semanas", "severidade": "moderada", "ordem": 3},
            {"nome": "Febre prolongada", "sistema": "sistemico", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "dias a 2 semanas", "severidade": "moderada", "ordem": 4},
            {"nome": "Exantema após uso de amoxicilina", "sistema": "cutaneo", "tipo": "local", "frequencia": "muito_comum", "onset_texto": "após amoxicilina", "severidade": "leve", "ordem": 5},
            {"nome": "Linfocitose atípica", "sistema": "hematologico", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "dias", "severidade": "leve", "ordem": 6},
            {"nome": "Ruptura esplênica (esporte)", "sistema": "digestivo", "tipo": "complicacao", "frequencia": "raro", "onset_texto": "primeiras 3 semanas", "severidade": "grave", "ordem": 7},
        ],
    },
    {
        "patologia_nome": "Influenza (gripe sazonal e pandêmica)",
        "sintomas": [
            {"nome": "Febre alta de início súbito (≥38,5°C)", "sistema": "sistemico", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "1-4 dias após exposição", "severidade": "moderada", "ordem": 1},
            {"nome": "Mialgia intensa e generalizada", "sistema": "musculoesqueletico", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "1-3 dias", "severidade": "grave", "ordem": 2},
            {"nome": "Cefaleia", "sistema": "neurologico", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "1-3 dias", "severidade": "moderada", "ordem": 3},
            {"nome": "Tosse seca e irritativa", "sistema": "respiratorio", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "1-3 dias", "severidade": "leve", "ordem": 4},
            {"nome": "Calafrios e prostração", "sistema": "sistemico", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "1-3 dias", "severidade": "moderada", "ordem": 5},
            {"nome": "Rinorreia e congestão nasal", "sistema": "otorrinolaringologico", "tipo": "local", "frequencia": "comum", "onset_texto": "1-3 dias", "severidade": "leve", "ordem": 6},
            {"nome": "Pneumonia viral primária (complicação)", "sistema": "respiratorio", "tipo": "complicacao", "frequencia": "incomum", "onset_texto": "3-5 dias", "severidade": "grave", "ordem": 7},
        ],
    },
    {
        "patologia_nome": "COVID-19 (infecção aguda, grave e síndrome pós-COVID)",
        "sintomas": [
            {"nome": "Febre e calafrios", "sistema": "sistemico", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "2-14 dias após exposição", "severidade": "moderada", "ordem": 1},
            {"nome": "Tosse seca", "sistema": "respiratorio", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "2-5 dias", "severidade": "leve", "ordem": 2},
            {"nome": "Dispneia (formas moderada/grave)", "sistema": "respiratorio", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "5-10 dias", "severidade": "grave", "ordem": 3},
            {"nome": "Anosmia e ageusia (perda de olfato e paladar)", "sistema": "neurologico", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "2-5 dias", "severidade": "leve", "ordem": 4},
            {"nome": "Fadiga prolongada (pós-COVID)", "sistema": "sistemico", "tipo": "complicacao", "frequencia": "muito_comum", "onset_texto": ">4 semanas", "severidade": "moderada", "ordem": 5},
            {"nome": "Pneumonia intersticial bilateral", "sistema": "respiratorio", "tipo": "complicacao", "frequencia": "comum", "onset_texto": "5-10 dias", "severidade": "grave", "ordem": 6},
            {"nome": "Tromboembolismo venoso", "sistema": "cardiovascular", "tipo": "complicacao", "frequencia": "comum", "onset_texto": "fase aguda a pós-COVID", "severidade": "grave", "ordem": 7},
        ],
    },
    {
        "patologia_nome": "Infecção pelo Vírus Sincicial Respiratório (VSR/RSV)",
        "sintomas": [
            {"nome": "Bronquiolite (sibilância + dificuldade respiratória em lactentes)", "sistema": "respiratorio", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "2-8 dias após exposição", "severidade": "grave", "ordem": 1},
            {"nome": "Coriza e congestão nasal", "sistema": "otorrinolaringologico", "tipo": "prodromico", "frequencia": "muito_comum", "onset_texto": "1-3 dias", "severidade": "leve", "ordem": 2},
            {"nome": "Febre baixa", "sistema": "sistemico", "tipo": "sistemico", "frequencia": "muito_comum", "onset_texto": "1-3 dias", "severidade": "leve", "ordem": 3},
            {"nome": "Taquipneia e retração intercostal", "sistema": "respiratorio", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "3-7 dias", "severidade": "grave", "ordem": 4},
            {"nome": "Sibilância expiratória", "sistema": "respiratorio", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "3-7 dias", "severidade": "moderada", "ordem": 5},
            {"nome": "Apneia em prematuros e lactentes jovens", "sistema": "respiratorio", "tipo": "complicacao", "frequencia": "comum", "onset_texto": "primeiros dias", "severidade": "grave", "ordem": 6},
        ],
    },
    {
        "patologia_nome": "Infecção por Adenovírus Respiratório",
        "sintomas": [
            {"nome": "Faringoconjuntivite febril", "sistema": "otorrinolaringologico", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "2-14 dias após exposição", "severidade": "leve", "ordem": 1},
            {"nome": "Febre alta prolongada (até 7 dias)", "sistema": "sistemico", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "dias", "severidade": "moderada", "ordem": 2},
            {"nome": "Conjuntivite folicular bilateral", "sistema": "ocular", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "1-5 dias", "severidade": "leve", "ordem": 3},
            {"nome": "Tosse e dor de garganta", "sistema": "respiratorio", "tipo": "local", "frequencia": "muito_comum", "onset_texto": "1-5 dias", "severidade": "leve", "ordem": 4},
            {"nome": "Pneumonia adenoviral (imunodeprimidos)", "sistema": "respiratorio", "tipo": "complicacao", "frequencia": "incomum", "onset_texto": "dias", "severidade": "grave", "ordem": 5},
        ],
    },
    {
        "patologia_nome": "Sarampo",
        "sintomas": [
            {"nome": "Exantema maculopapular cefalocaudal", "sistema": "cutaneo", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "14-21 dias após exposição (dia 3-4 de febre)", "severidade": "moderada", "ordem": 1},
            {"nome": "Febre alta (≥39°C)", "sistema": "sistemico", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "10-14 dias após exposição", "severidade": "moderada", "ordem": 2},
            {"nome": "Tosse, coriza e conjuntivite (Tríade prodromal 3Cs)", "sistema": "otorrinolaringologico", "tipo": "prodromico", "frequencia": "muito_comum", "onset_texto": "2-4 dias antes do exantema", "severidade": "leve", "ordem": 3},
            {"nome": "Manchas de Koplik (enantema)", "sistema": "digestivo", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "1-2 dias antes do exantema", "severidade": "leve", "ordem": 4},
            {"nome": "Pneumonia por sarampo", "sistema": "respiratorio", "tipo": "complicacao", "frequencia": "comum", "onset_texto": "durante exantema", "severidade": "grave", "ordem": 5},
            {"nome": "Encefalite pós-sarampo", "sistema": "neurologico", "tipo": "complicacao", "frequencia": "incomum", "onset_texto": "1-2 semanas após exantema", "severidade": "grave", "ordem": 6},
        ],
    },
    {
        "patologia_nome": "Rubéola (adquirida e congênita)",
        "sintomas": [
            {"nome": "Exantema maculopapular cefalocaudal leve", "sistema": "cutaneo", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "14-23 dias após exposição", "severidade": "leve", "ordem": 1},
            {"nome": "Linfadenopatia retroauricular e suboccipital", "sistema": "hematologico", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "dias antes do exantema", "severidade": "leve", "ordem": 2},
            {"nome": "Febre baixa", "sistema": "sistemico", "tipo": "sistemico", "frequencia": "muito_comum", "onset_texto": "pródromo", "severidade": "leve", "ordem": 3},
            {"nome": "Artralgia (mulheres adultas)", "sistema": "musculoesqueletico", "tipo": "local", "frequencia": "muito_comum", "onset_texto": "junto ao exantema", "severidade": "leve", "ordem": 4},
            {"nome": "Síndrome da rubéola congênita (surdez, catarata, cardiopatia)", "sistema": "outro", "tipo": "complicacao", "frequencia": "muito_comum", "onset_texto": "1º trimestre da gestação", "severidade": "grave", "ordem": 5},
        ],
    },
    {
        "patologia_nome": "Caxumba / Parotidite Epidêmica",
        "sintomas": [
            {"nome": "Tumefação parotídea bilateral dolorosa", "sistema": "otorrinolaringologico", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "16-18 dias após exposição", "severidade": "moderada", "ordem": 1},
            {"nome": "Febre (38–39°C)", "sistema": "sistemico", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "dias", "severidade": "leve", "ordem": 2},
            {"nome": "Mal-estar e cefaleia", "sistema": "sistemico", "tipo": "prodromico", "frequencia": "muito_comum", "onset_texto": "1-2 dias antes da parotidite", "severidade": "leve", "ordem": 3},
            {"nome": "Orquite (adolescentes e adultos do sexo masculino)", "sistema": "urinario", "tipo": "complicacao", "frequencia": "comum", "onset_texto": "1 semana após parotidite", "severidade": "grave", "ordem": 4},
            {"nome": "Meningite asséptica", "sistema": "neurologico", "tipo": "complicacao", "frequencia": "comum", "onset_texto": "1-2 semanas", "severidade": "moderada", "ordem": 5},
            {"nome": "Surdez unilateral (complicação)", "sistema": "otorrinolaringologico", "tipo": "complicacao", "frequencia": "incomum", "onset_texto": "semanas", "severidade": "grave", "ordem": 6},
        ],
    },
    {
        "patologia_nome": "Doença Mão-Pé-Boca (Enterovírus 71 e Coxsackievírus A16)",
        "sintomas": [
            {"nome": "Vesículas palmoplantares e interdigitais", "sistema": "cutaneo", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "3-5 dias após exposição", "severidade": "leve", "ordem": 1},
            {"nome": "Úlceras orais dolorosas (enantema)", "sistema": "digestivo", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "3-5 dias", "severidade": "leve", "ordem": 2},
            {"nome": "Febre baixa", "sistema": "sistemico", "tipo": "prodromico", "frequencia": "muito_comum", "onset_texto": "1-2 dias antes das vesículas", "severidade": "leve", "ordem": 3},
            {"nome": "Irritabilidade em lactentes", "sistema": "neurologico", "tipo": "sistemico", "frequencia": "muito_comum", "onset_texto": "dias", "severidade": "leve", "ordem": 4},
            {"nome": "Encefalite (EV71 — forma grave)", "sistema": "neurologico", "tipo": "complicacao", "frequencia": "incomum", "onset_texto": "dias", "severidade": "grave", "ordem": 5},
        ],
    },
    {
        "patologia_nome": "Rotavirose (diarreia por Rotavírus)",
        "sintomas": [
            {"nome": "Diarreia aquosa profusa", "sistema": "digestivo", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "1-3 dias após exposição", "severidade": "moderada", "ordem": 1},
            {"nome": "Vômitos frequentes", "sistema": "digestivo", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "1-3 dias", "severidade": "moderada", "ordem": 2},
            {"nome": "Febre (38–39°C)", "sistema": "sistemico", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "1-3 dias", "severidade": "leve", "ordem": 3},
            {"nome": "Desidratação rápida em lactentes", "sistema": "sistemico", "tipo": "complicacao", "frequencia": "muito_comum", "onset_texto": "1-3 dias", "severidade": "grave", "ordem": 4},
            {"nome": "Dor abdominal", "sistema": "digestivo", "tipo": "local", "frequencia": "comum", "onset_texto": "1-3 dias", "severidade": "leve", "ordem": 5},
        ],
    },
    {
        "patologia_nome": "Norovirose (diarreia e vômito por Norovírus)",
        "sintomas": [
            {"nome": "Vômitos súbitos e profusos", "sistema": "digestivo", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "12-48h após exposição", "severidade": "moderada", "ordem": 1},
            {"nome": "Diarreia aquosa não sanguinolenta", "sistema": "digestivo", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "12-48h", "severidade": "moderada", "ordem": 2},
            {"nome": "Cólicas abdominais", "sistema": "digestivo", "tipo": "local", "frequencia": "muito_comum", "onset_texto": "12-48h", "severidade": "moderada", "ordem": 3},
            {"nome": "Náuseas intensas", "sistema": "digestivo", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "12-48h", "severidade": "leve", "ordem": 4},
            {"nome": "Febre baixa e mal-estar", "sistema": "sistemico", "tipo": "sistemico", "frequencia": "comum", "onset_texto": "12-48h", "severidade": "leve", "ordem": 5},
        ],
    },
    {
        "patologia_nome": "Raiva (raiva humana transmitida por cão, morcego ou animais silvestres)",
        "sintomas": [
            {"nome": "Parestesia no local da mordida (pródromo)", "sistema": "neurologico", "tipo": "prodromico", "frequencia": "muito_comum", "onset_texto": "30-90 dias após mordida (pródromo 2-10 dias antes)", "severidade": "leve", "ordem": 1},
            {"nome": "Hidrofobia (espasmo faríngeo ao ver água)", "sistema": "neurologico", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "fase neurológica", "severidade": "grave", "ordem": 2},
            {"nome": "Aerofobia", "sistema": "neurologico", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "fase neurológica", "severidade": "grave", "ordem": 3},
            {"nome": "Agitação, alucinações e agressividade", "sistema": "neurologico", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "fase neurológica", "severidade": "grave", "ordem": 4},
            {"nome": "Paralisia flácida ascendente (forma paralítica)", "sistema": "neurologico", "tipo": "cardinal", "frequencia": "comum", "onset_texto": "fase neurológica", "severidade": "grave", "ordem": 5},
            {"nome": "Coma e óbito (invariavelmente fatal sem tratamento)", "sistema": "neurologico", "tipo": "complicacao", "frequencia": "muito_comum", "onset_texto": "dias após início neurológico", "severidade": "grave", "ordem": 6},
        ],
    },
    {
        "patologia_nome": "Encefalite Herpética (HSV-1)",
        "sintomas": [
            {"nome": "Febre alta e cefaleia intensa", "sistema": "sistemico", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "dias", "severidade": "grave", "ordem": 1},
            {"nome": "Alteração comportamental e confusão mental", "sistema": "neurologico", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "dias", "severidade": "grave", "ordem": 2},
            {"nome": "Convulsões (focais temporais)", "sistema": "neurologico", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "dias", "severidade": "grave", "ordem": 3},
            {"nome": "Afasia", "sistema": "neurologico", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "dias", "severidade": "grave", "ordem": 4},
            {"nome": "Déficit neurológico focal", "sistema": "neurologico", "tipo": "complicacao", "frequencia": "muito_comum", "onset_texto": "dias", "severidade": "grave", "ordem": 5},
            {"nome": "Rebaixamento progressivo do nível de consciência", "sistema": "neurologico", "tipo": "complicacao", "frequencia": "muito_comum", "onset_texto": "dias", "severidade": "grave", "ordem": 6},
        ],
    },
    {
        "patologia_nome": "Meningite Viral (enterovírus e outros)",
        "sintomas": [
            {"nome": "Cefaleia intensa", "sistema": "neurologico", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "dias", "severidade": "grave", "ordem": 1},
            {"nome": "Febre", "sistema": "sistemico", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "dias", "severidade": "moderada", "ordem": 2},
            {"nome": "Rigidez de nuca (meningismo leve)", "sistema": "neurologico", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "dias", "severidade": "moderada", "ordem": 3},
            {"nome": "Fotofobia e fonofobia", "sistema": "neurologico", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "dias", "severidade": "moderada", "ordem": 4},
            {"nome": "Náuseas e vômitos", "sistema": "digestivo", "tipo": "sistemico", "frequencia": "comum", "onset_texto": "dias", "severidade": "leve", "ordem": 5},
            {"nome": "Exantema (meningite por enterovírus)", "sistema": "cutaneo", "tipo": "local", "frequencia": "comum", "onset_texto": "dias", "severidade": "leve", "ordem": 6},
        ],
    },
    {
        "patologia_nome": "Infecção pelo HPV (verrugas genitais e lesões precursoras)",
        "sintomas": [
            {"nome": "Condilomas acuminados genitais (verrugas)", "sistema": "cutaneo", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "semanas a meses após contato", "severidade": "leve", "ordem": 1},
            {"nome": "Prurido genital", "sistema": "cutaneo", "tipo": "local", "frequencia": "comum", "onset_texto": "semanas", "severidade": "leve", "ordem": 2},
            {"nome": "Neoplasia intraepitelial cervical (NIC)", "sistema": "outro", "tipo": "complicacao", "frequencia": "muito_comum", "onset_texto": "meses a anos", "severidade": "grave", "ordem": 3},
            {"nome": "Maioria das infecções são assintomáticas", "sistema": "sistemico", "tipo": "sistemico", "frequencia": "muito_comum", "onset_texto": "variável", "severidade": "leve", "ordem": 4},
            {"nome": "Câncer cervical (HPV 16/18)", "sistema": "outro", "tipo": "complicacao", "frequencia": "comum", "onset_texto": "anos a décadas", "severidade": "grave", "ordem": 5},
        ],
    },
    {
        "patologia_nome": "Hantavirose (Síndrome Cardiopulmonar por Hantavírus — SCPH)",
        "sintomas": [
            {"nome": "Febre, cefaleia e mialgia (fase prodromal)", "sistema": "sistemico", "tipo": "prodromico", "frequencia": "muito_comum", "onset_texto": "9-33 dias após exposição", "severidade": "moderada", "ordem": 1},
            {"nome": "Dispneia de rápida progressão", "sistema": "respiratorio", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "3-5 dias após pródromo", "severidade": "grave", "ordem": 2},
            {"nome": "Edema pulmonar não cardiogênico", "sistema": "respiratorio", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "fase cardiopulmonar", "severidade": "grave", "ordem": 3},
            {"nome": "Choque cardiogênico", "sistema": "cardiovascular", "tipo": "complicacao", "frequencia": "muito_comum", "onset_texto": "fase cardiopulmonar", "severidade": "grave", "ordem": 4},
            {"nome": "Insuficiência respiratória grave", "sistema": "respiratorio", "tipo": "complicacao", "frequencia": "muito_comum", "onset_texto": "fase cardiopulmonar", "severidade": "grave", "ordem": 5},
        ],
    },
    {
        "patologia_nome": "Síndrome Congênita do Zika Vírus",
        "sintomas": [
            {"nome": "Microcefalia (PC ≤2 DP abaixo da média)", "sistema": "neurologico", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "ao nascer / intraútero", "severidade": "grave", "ordem": 1},
            {"nome": "Calcificações intracranianas subgiro-corticais", "sistema": "neurologico", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "ao nascer", "severidade": "grave", "ordem": 2},
            {"nome": "Déficit visual e alterações oculares", "sistema": "ocular", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "ao nascer", "severidade": "grave", "ordem": 3},
            {"nome": "Hipertonia e espasticidade", "sistema": "neurologico", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "meses", "severidade": "grave", "ordem": 4},
            {"nome": "Epilepsia de difícil controle", "sistema": "neurologico", "tipo": "complicacao", "frequencia": "muito_comum", "onset_texto": "meses a anos", "severidade": "grave", "ordem": 5},
            {"nome": "Atraso grave do neurodesenvolvimento", "sistema": "neurologico", "tipo": "complicacao", "frequencia": "muito_comum", "onset_texto": "meses", "severidade": "grave", "ordem": 6},
        ],
    },
    {
        "patologia_nome": "CMV Congênito",
        "sintomas": [
            {"nome": "Maioria assintomática ao nascer", "sistema": "sistemico", "tipo": "sistemico", "frequencia": "muito_comum", "onset_texto": "ao nascer", "severidade": "leve", "ordem": 1},
            {"nome": "Petéquias e trombocitopenia (sintomático)", "sistema": "hematologico", "tipo": "cardinal", "frequencia": "comum", "onset_texto": "ao nascer", "severidade": "moderada", "ordem": 2},
            {"nome": "Hepatoesplenomegalia e icterícia", "sistema": "digestivo", "tipo": "cardinal", "frequencia": "comum", "onset_texto": "ao nascer", "severidade": "moderada", "ordem": 3},
            {"nome": "Surdez neurossensorial (bilateral)", "sistema": "otorrinolaringologico", "tipo": "complicacao", "frequencia": "muito_comum", "onset_texto": "meses a anos", "severidade": "grave", "ordem": 4},
            {"nome": "Déficit cognitivo e atraso do desenvolvimento", "sistema": "neurologico", "tipo": "complicacao", "frequencia": "comum", "onset_texto": "meses a anos", "severidade": "grave", "ordem": 5},
        ],
    },
    {
        "patologia_nome": "Hepatite B Perinatal (transmissão vertical)",
        "sintomas": [
            {"nome": "Maioria assintomática no período neonatal", "sistema": "sistemico", "tipo": "sistemico", "frequencia": "muito_comum", "onset_texto": "ao nascer", "severidade": "leve", "ordem": 1},
            {"nome": "Infecção crônica assintomática (portador)", "sistema": "digestivo", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "anos", "severidade": "leve", "ordem": 2},
            {"nome": "Cirrose e carcinoma hepatocelular (longo prazo)", "sistema": "digestivo", "tipo": "complicacao", "frequencia": "muito_comum", "onset_texto": "décadas", "severidade": "grave", "ordem": 3},
            {"nome": "Hepatite aguda (raro no neonato)", "sistema": "digestivo", "tipo": "local", "frequencia": "raro", "onset_texto": "primeiros meses", "severidade": "grave", "ordem": 4},
        ],
    },
    {
        "patologia_nome": "Herpes Neonatal (HSV)",
        "sintomas": [
            {"nome": "Vesículas cutâneas, oculares e orais", "sistema": "cutaneo", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "5-19 dias de vida", "severidade": "grave", "ordem": 1},
            {"nome": "Encefalite neonatal (convulsões, letargia)", "sistema": "neurologico", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "dias a semanas", "severidade": "grave", "ordem": 2},
            {"nome": "Doença disseminada (sepse-like)", "sistema": "sistemico", "tipo": "cardinal", "frequencia": "comum", "onset_texto": "primeiros 10-12 dias", "severidade": "grave", "ordem": 3},
            {"nome": "Instabilidade térmica", "sistema": "sistemico", "tipo": "sistemico", "frequencia": "muito_comum", "onset_texto": "primeiros dias", "severidade": "grave", "ordem": 4},
            {"nome": "Ceratoconjuntivite", "sistema": "ocular", "tipo": "local", "frequencia": "comum", "onset_texto": "primeiros dias", "severidade": "grave", "ordem": 5},
        ],
    },
    {
        "patologia_nome": "Poliomielite (pólio)",
        "sintomas": [
            {"nome": "Paralisia flácida aguda assimétrica", "sistema": "neurologico", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "3-35 dias após exposição", "severidade": "grave", "ordem": 1},
            {"nome": "Febre, cefaleia e dor muscular (fase não paralítica)", "sistema": "sistemico", "tipo": "prodromico", "frequencia": "muito_comum", "onset_texto": "1-2 semanas", "severidade": "moderada", "ordem": 2},
            {"nome": "Rigidez de nuca e costas", "sistema": "neurologico", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "fase paralítica", "severidade": "grave", "ordem": 3},
            {"nome": "Paralisia de nervos bulbares (forma bulbar)", "sistema": "neurologico", "tipo": "complicacao", "frequencia": "incomum", "onset_texto": "dias", "severidade": "grave", "ordem": 4},
            {"nome": "Sequela permanente: paralisia e atrofia muscular", "sistema": "musculoesqueletico", "tipo": "complicacao", "frequencia": "muito_comum", "onset_texto": "permanente", "severidade": "grave", "ordem": 5},
        ],
    },
    {
        "patologia_nome": "HTLV — Leucemia/Linfoma de Células T do Adulto (ATLL)",
        "sintomas": [
            {"nome": "Linfadenopatia generalizada", "sistema": "hematologico", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "décadas após infecção", "severidade": "grave", "ordem": 1},
            {"nome": "Hepatoesplenomegalia", "sistema": "digestivo", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "décadas", "severidade": "grave", "ordem": 2},
            {"nome": "Lesões cutâneas (ATLL cutânea)", "sistema": "cutaneo", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "décadas", "severidade": "grave", "ordem": 3},
            {"nome": "Hipercalcemia (fadiga, confusão)", "sistema": "endocrino", "tipo": "complicacao", "frequencia": "muito_comum", "onset_texto": "décadas", "severidade": "grave", "ordem": 4},
            {"nome": "Infecções oportunistas por imunossupressão", "sistema": "sistemico", "tipo": "complicacao", "frequencia": "muito_comum", "onset_texto": "fase estabelecida", "severidade": "grave", "ordem": 5},
        ],
    },
    {
        "patologia_nome": "HTLV — Mielopatia Associada ao HTLV / Paraparesia Espástica Tropical (HAM/TSP)",
        "sintomas": [
            {"nome": "Paraparesia espástica progressiva", "sistema": "neurologico", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "anos a décadas após infecção", "severidade": "grave", "ordem": 1},
            {"nome": "Dificuldade de marcha progressiva", "sistema": "neurologico", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "anos", "severidade": "grave", "ordem": 2},
            {"nome": "Bexiga neurogênica (urgência, incontinência)", "sistema": "urinario", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "anos", "severidade": "moderada", "ordem": 3},
            {"nome": "Dor lombar e em membros inferiores", "sistema": "musculoesqueletico", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "anos", "severidade": "moderada", "ordem": 4},
            {"nome": "Disfunção erétil e constipação", "sistema": "outro", "tipo": "sistemico", "frequencia": "comum", "onset_texto": "anos", "severidade": "moderada", "ordem": 5},
        ],
    },
]

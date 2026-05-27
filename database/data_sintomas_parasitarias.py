"""
Sintomatologia das patologias parasitárias.
Fontes: MS/SVS, PCDT, SBMT, SBP, CFM.
"""

SINTOMAS_PARASITARIAS = [
    {
        "patologia_nome": "Malária por Plasmodium falciparum",
        "sintomas": [
            {"nome": "Febre paroxística (frio → calor → sudorese)", "sistema": "sistemico", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "7-14 dias após picada", "severidade": "grave", "ordem": 1},
            {"nome": "Cefaleia intensa", "sistema": "neurologico", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "junto à febre", "severidade": "grave", "ordem": 2},
            {"nome": "Calafrios intensos", "sistema": "sistemico", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "fase inicial do paroxismo", "severidade": "grave", "ordem": 3},
            {"nome": "Mialgia e artralgia", "sistema": "musculoesqueletico", "tipo": "sistemico", "frequencia": "muito_comum", "onset_texto": "junto à febre", "severidade": "moderada", "ordem": 4},
            {"nome": "Anemia hemolítica e esplenomegalia", "sistema": "hematologico", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "dias", "severidade": "grave", "ordem": 5},
            {"nome": "Malária cerebral (convulsões, coma)", "sistema": "neurologico", "tipo": "complicacao", "frequencia": "comum", "onset_texto": "dias", "severidade": "grave", "ordem": 6},
            {"nome": "Insuficiência renal aguda ('blackwater fever')", "sistema": "urinario", "tipo": "complicacao", "frequencia": "comum", "onset_texto": "dias", "severidade": "grave", "ordem": 7},
            {"nome": "Icterícia e hepatomegalia", "sistema": "digestivo", "tipo": "sistemico", "frequencia": "muito_comum", "onset_texto": "dias", "severidade": "grave", "ordem": 8},
        ],
    },
    {
        "patologia_nome": "Malária por Plasmodium vivax",
        "sintomas": [
            {"nome": "Febre terçã benigna (ciclos de 48h)", "sistema": "sistemico", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "12-20 dias após picada", "severidade": "moderada", "ordem": 1},
            {"nome": "Calafrios, febre alta e sudorese", "sistema": "sistemico", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "ciclos de 48h", "severidade": "moderada", "ordem": 2},
            {"nome": "Cefaleia e mialgia", "sistema": "musculoesqueletico", "tipo": "sistemico", "frequencia": "muito_comum", "onset_texto": "junto ao paroxismo", "severidade": "moderada", "ordem": 3},
            {"nome": "Esplenomegalia", "sistema": "digestivo", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "semanas", "severidade": "moderada", "ordem": 4},
            {"nome": "Anemia hemolítica", "sistema": "hematologico", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "dias a semanas", "severidade": "moderada", "ordem": 5},
            {"nome": "Náuseas e prostração", "sistema": "digestivo", "tipo": "sistemico", "frequencia": "muito_comum", "onset_texto": "junto ao paroxismo", "severidade": "leve", "ordem": 6},
        ],
    },
    {
        "patologia_nome": "Malária por Plasmodium malariae",
        "sintomas": [
            {"nome": "Febre quartã (ciclos de 72h)", "sistema": "sistemico", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "18-40 dias após picada", "severidade": "leve", "ordem": 1},
            {"nome": "Calafrios e sudorese (ciclos de 72h)", "sistema": "sistemico", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "ciclos de 72h", "severidade": "leve", "ordem": 2},
            {"nome": "Esplenomegalia crônica", "sistema": "digestivo", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "semanas a meses", "severidade": "moderada", "ordem": 3},
            {"nome": "Síndrome nefrótica (complicação crônica)", "sistema": "urinario", "tipo": "complicacao", "frequencia": "incomum", "onset_texto": "meses a anos", "severidade": "grave", "ordem": 4},
            {"nome": "Anemia leve", "sistema": "hematologico", "tipo": "sistemico", "frequencia": "muito_comum", "onset_texto": "semanas", "severidade": "leve", "ordem": 5},
        ],
    },
    {
        "patologia_nome": "Leishmaniose Tegumentar Americana (LTA)",
        "sintomas": [
            {"nome": "Úlcera cutânea indolor com borda em moldura (forma cutânea)", "sistema": "cutaneo", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "2-8 semanas após picada", "severidade": "moderada", "ordem": 1},
            {"nome": "Lesão destrutiva do septo nasal (forma mucosa)", "sistema": "otorrinolaringologico", "tipo": "cardinal", "frequencia": "comum", "onset_texto": "meses a anos", "severidade": "grave", "ordem": 2},
            {"nome": "Perfuração do septo nasal ('sinal do trompeteiro')", "sistema": "otorrinolaringologico", "tipo": "complicacao", "frequencia": "comum", "onset_texto": "meses a anos", "severidade": "grave", "ordem": 3},
            {"nome": "Nódulo de inoculação (pré-úlcera)", "sistema": "cutaneo", "tipo": "prodromico", "frequencia": "muito_comum", "onset_texto": "semanas", "severidade": "leve", "ordem": 4},
            {"nome": "Destruição do palato e úvula (forma mucosa avançada)", "sistema": "otorrinolaringologico", "tipo": "complicacao", "frequencia": "incomum", "onset_texto": "meses a anos", "severidade": "grave", "ordem": 5},
        ],
    },
    {
        "patologia_nome": "Leishmaniose Visceral (Calazar)",
        "sintomas": [
            {"nome": "Febre prolongada e irregular", "sistema": "sistemico", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "meses após picada", "severidade": "grave", "ordem": 1},
            {"nome": "Hepatoesplenomegalia volumosa", "sistema": "digestivo", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "meses", "severidade": "grave", "ordem": 2},
            {"nome": "Perda de peso e caquexia", "sistema": "sistemico", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "meses", "severidade": "grave", "ordem": 3},
            {"nome": "Palidez por anemia intensa", "sistema": "hematologico", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "meses", "severidade": "grave", "ordem": 4},
            {"nome": "Hiperpigmentação cutânea (kala-azar)", "sistema": "cutaneo", "tipo": "cardinal", "frequencia": "comum", "onset_texto": "meses", "severidade": "leve", "ordem": 5},
            {"nome": "Epistaxe e sangramento por plaquetopenia", "sistema": "hematologico", "tipo": "complicacao", "frequencia": "comum", "onset_texto": "meses", "severidade": "grave", "ordem": 6},
            {"nome": "Edema de membros inferiores (hipoalbuminemia)", "sistema": "sistemico", "tipo": "complicacao", "frequencia": "comum", "onset_texto": "meses", "severidade": "moderada", "ordem": 7},
        ],
    },
    {
        "patologia_nome": "Doença de Chagas Aguda",
        "sintomas": [
            {"nome": "Sinal de Romaña (edema bipalpebral unilateral)", "sistema": "ocular", "tipo": "cardinal", "frequencia": "comum", "onset_texto": "4-10 dias após inoculação ocular", "severidade": "leve", "ordem": 1},
            {"nome": "Febre prolongada e mal-estar", "sistema": "sistemico", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "5-20 dias após exposição", "severidade": "moderada", "ordem": 2},
            {"nome": "Linfadenopatia e hepatoesplenomegalia", "sistema": "hematologico", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "semanas", "severidade": "moderada", "ordem": 3},
            {"nome": "Chagoma de inoculação cutânea", "sistema": "cutaneo", "tipo": "cardinal", "frequencia": "comum", "onset_texto": "dias após contato", "severidade": "leve", "ordem": 4},
            {"nome": "Cardite aguda (miocardite)", "sistema": "cardiovascular", "tipo": "complicacao", "frequencia": "comum", "onset_texto": "semanas", "severidade": "grave", "ordem": 5},
            {"nome": "Meningoencefalite (imunocomprometidos)", "sistema": "neurologico", "tipo": "complicacao", "frequencia": "incomum", "onset_texto": "semanas", "severidade": "grave", "ordem": 6},
        ],
    },
    {
        "patologia_nome": "Doença de Chagas Crônica",
        "sintomas": [
            {"nome": "Palpitações e arritmias (cardiopatia chagásica)", "sistema": "cardiovascular", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "anos após infecção", "severidade": "grave", "ordem": 1},
            {"nome": "Dispneia de esforço e ortopneia", "sistema": "cardiovascular", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "anos", "severidade": "grave", "ordem": 2},
            {"nome": "Síncope e pré-síncope", "sistema": "cardiovascular", "tipo": "cardinal", "frequencia": "comum", "onset_texto": "anos", "severidade": "grave", "ordem": 3},
            {"nome": "Megaesôfago (disfagia progressiva)", "sistema": "digestivo", "tipo": "cardinal", "frequencia": "comum", "onset_texto": "anos", "severidade": "grave", "ordem": 4},
            {"nome": "Megacólon (constipação intensa)", "sistema": "digestivo", "tipo": "cardinal", "frequencia": "comum", "onset_texto": "anos", "severidade": "moderada", "ordem": 5},
            {"nome": "Morte súbita por arritmia", "sistema": "cardiovascular", "tipo": "complicacao", "frequencia": "comum", "onset_texto": "anos", "severidade": "grave", "ordem": 6},
        ],
    },
    {
        "patologia_nome": "Toxoplasmose em Imunocompetentes",
        "sintomas": [
            {"nome": "Maioria assintomática (90%)", "sistema": "sistemico", "tipo": "sistemico", "frequencia": "muito_comum", "onset_texto": "variável", "severidade": "leve", "ordem": 1},
            {"nome": "Linfadenopatia cervical indolor (síndrome mononucleose-like)", "sistema": "hematologico", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "10-23 dias após exposição", "severidade": "leve", "ordem": 2},
            {"nome": "Febre baixa e mal-estar", "sistema": "sistemico", "tipo": "sistemico", "frequencia": "comum", "onset_texto": "semanas", "severidade": "leve", "ordem": 3},
            {"nome": "Mialgia", "sistema": "musculoesqueletico", "tipo": "sistemico", "frequencia": "comum", "onset_texto": "semanas", "severidade": "leve", "ordem": 4},
        ],
    },
    {
        "patologia_nome": "Toxoplasmose em Imunocomprometidos (HIV/AIDS)",
        "sintomas": [
            {"nome": "Encefalite: cefaleia, febre e déficit neurológico focal", "sistema": "neurologico", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "dias a semanas (CD4 <100)", "severidade": "grave", "ordem": 1},
            {"nome": "Convulsões", "sistema": "neurologico", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "dias a semanas", "severidade": "grave", "ordem": 2},
            {"nome": "Confusão mental e alteração do nível de consciência", "sistema": "neurologico", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "dias", "severidade": "grave", "ordem": 3},
            {"nome": "Febre", "sistema": "sistemico", "tipo": "sistemico", "frequencia": "muito_comum", "onset_texto": "dias", "severidade": "moderada", "ordem": 4},
            {"nome": "Coriorretiníte (lesão ocular)", "sistema": "ocular", "tipo": "local", "frequencia": "incomum", "onset_texto": "variável", "severidade": "grave", "ordem": 5},
        ],
    },
    {
        "patologia_nome": "Toxoplasmose Congênita",
        "sintomas": [
            {"nome": "Coriorretinite (lesão ocular típica)", "sistema": "ocular", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "ao nascer ou meses", "severidade": "grave", "ordem": 1},
            {"nome": "Calcificações cerebrais intracranianas", "sistema": "neurologico", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "ao nascer", "severidade": "grave", "ordem": 2},
            {"nome": "Hidrocefalia", "sistema": "neurologico", "tipo": "cardinal", "frequencia": "comum", "onset_texto": "ao nascer", "severidade": "grave", "ordem": 3},
            {"nome": "Microcefalia", "sistema": "neurologico", "tipo": "local", "frequencia": "comum", "onset_texto": "ao nascer", "severidade": "grave", "ordem": 4},
            {"nome": "Maioria assintomática ao nascer (risco de sequela tardia)", "sistema": "sistemico", "tipo": "sistemico", "frequencia": "muito_comum", "onset_texto": "ao nascer", "severidade": "leve", "ordem": 5},
            {"nome": "Surdez neurossensorial (tardia)", "sistema": "otorrinolaringologico", "tipo": "complicacao", "frequencia": "comum", "onset_texto": "meses a anos", "severidade": "grave", "ordem": 6},
        ],
    },
    {
        "patologia_nome": "Amebíase Intestinal",
        "sintomas": [
            {"nome": "Diarreia com muco e sangue (disenteria amebiana)", "sistema": "digestivo", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "1-4 semanas após ingestão", "severidade": "grave", "ordem": 1},
            {"nome": "Tenesmo e cólicas abdominais", "sistema": "digestivo", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "dias", "severidade": "moderada", "ordem": 2},
            {"nome": "Febre baixa", "sistema": "sistemico", "tipo": "sistemico", "frequencia": "comum", "onset_texto": "dias", "severidade": "leve", "ordem": 3},
            {"nome": "Diarreia intermitente (forma assintomática)", "sistema": "digestivo", "tipo": "sistemico", "frequencia": "muito_comum", "onset_texto": "variável", "severidade": "leve", "ordem": 4},
            {"nome": "Peritonite por perfuração (complicação grave)", "sistema": "digestivo", "tipo": "complicacao", "frequencia": "raro", "onset_texto": "semanas", "severidade": "grave", "ordem": 5},
        ],
    },
    {
        "patologia_nome": "Abscesso Hepático Amebiano",
        "sintomas": [
            {"nome": "Dor em hipocôndrio direito intensa", "sistema": "digestivo", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "dias a semanas", "severidade": "grave", "ordem": 1},
            {"nome": "Febre alta e calafrios", "sistema": "sistemico", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "dias", "severidade": "grave", "ordem": 2},
            {"nome": "Hepatomegalia dolorosa", "sistema": "digestivo", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "dias", "severidade": "moderada", "ordem": 3},
            {"nome": "Perda de peso e anorexia", "sistema": "sistemico", "tipo": "sistemico", "frequencia": "muito_comum", "onset_texto": "semanas", "severidade": "moderada", "ordem": 4},
            {"nome": "Ruptura com derrame pleural ou peritonite", "sistema": "respiratorio", "tipo": "complicacao", "frequencia": "incomum", "onset_texto": "semanas", "severidade": "grave", "ordem": 5},
        ],
    },
    {
        "patologia_nome": "Giardíase",
        "sintomas": [
            {"nome": "Diarreia fétida gordurosa (esteatorreia)", "sistema": "digestivo", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "1-3 semanas após ingestão", "severidade": "leve", "ordem": 1},
            {"nome": "Flatulência e distensão abdominal", "sistema": "digestivo", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "dias a semanas", "severidade": "leve", "ordem": 2},
            {"nome": "Náuseas e cólicas", "sistema": "digestivo", "tipo": "local", "frequencia": "muito_comum", "onset_texto": "dias", "severidade": "leve", "ordem": 3},
            {"nome": "Perda de peso (má absorção)", "sistema": "sistemico", "tipo": "sistemico", "frequencia": "comum", "onset_texto": "semanas", "severidade": "leve", "ordem": 4},
            {"nome": "Ausência de febre (típico)", "sistema": "sistemico", "tipo": "sistemico", "frequencia": "muito_comum", "onset_texto": "variável", "severidade": "leve", "ordem": 5},
        ],
    },
    {
        "patologia_nome": "Tricomoníase",
        "sintomas": [
            {"nome": "Corrimento vaginal espumoso, amarelo-esverdeado e fétido", "sistema": "outro", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "5-28 dias após contato", "severidade": "leve", "ordem": 1},
            {"nome": "Prurido e ardência vulvovaginal", "sistema": "outro", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "dias", "severidade": "leve", "ordem": 2},
            {"nome": "Disúria", "sistema": "urinario", "tipo": "local", "frequencia": "comum", "onset_texto": "dias", "severidade": "leve", "ordem": 3},
            {"nome": "Assintomático em homens (portador)", "sistema": "urinario", "tipo": "sistemico", "frequencia": "muito_comum", "onset_texto": "variável", "severidade": "leve", "ordem": 4},
            {"nome": "Colpite com 'colo em framboesa'", "sistema": "outro", "tipo": "cardinal", "frequencia": "comum", "onset_texto": "dias", "severidade": "leve", "ordem": 5},
        ],
    },
    {
        "patologia_nome": "Criptosporidiose",
        "sintomas": [
            {"nome": "Diarreia aquosa profusa (imunocomprometidos: prolongada)", "sistema": "digestivo", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "7-10 dias após ingestão", "severidade": "grave", "ordem": 1},
            {"nome": "Cólicas abdominais", "sistema": "digestivo", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "dias", "severidade": "moderada", "ordem": 2},
            {"nome": "Náuseas e vômitos", "sistema": "digestivo", "tipo": "sistemico", "frequencia": "muito_comum", "onset_texto": "dias", "severidade": "leve", "ordem": 3},
            {"nome": "Febre baixa", "sistema": "sistemico", "tipo": "sistemico", "frequencia": "comum", "onset_texto": "dias", "severidade": "leve", "ordem": 4},
            {"nome": "Desidratação grave (em AIDS)", "sistema": "sistemico", "tipo": "complicacao", "frequencia": "muito_comum", "onset_texto": "dias", "severidade": "grave", "ordem": 5},
        ],
    },
    {
        "patologia_nome": "Ascaridíase",
        "sintomas": [
            {"nome": "Maioria assintomática (carga baixa)", "sistema": "digestivo", "tipo": "sistemico", "frequencia": "muito_comum", "onset_texto": "variável", "severidade": "leve", "ordem": 1},
            {"nome": "Dor abdominal em cólica (carga alta)", "sistema": "digestivo", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "semanas após ingestão", "severidade": "moderada", "ordem": 2},
            {"nome": "Síndrome de Löffler (tosse, dispneia, eosinofilia)", "sistema": "respiratorio", "tipo": "prodromico", "frequencia": "comum", "onset_texto": "2-3 semanas (fase larval)", "severidade": "leve", "ordem": 3},
            {"nome": "Obstrução intestinal (carga muito alta)", "sistema": "digestivo", "tipo": "complicacao", "frequencia": "incomum", "onset_texto": "semanas", "severidade": "grave", "ordem": 4},
            {"nome": "Verme eliminado nas fezes ou vômito", "sistema": "digestivo", "tipo": "cardinal", "frequencia": "comum", "onset_texto": "semanas", "severidade": "leve", "ordem": 5},
        ],
    },
    {
        "patologia_nome": "Ancilostomíase / Necatoríase (Hookworm)",
        "sintomas": [
            {"nome": "Anemia ferropriva (causa principal)", "sistema": "hematologico", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "meses após infecção", "severidade": "grave", "ordem": 1},
            {"nome": "Fadiga e palidez", "sistema": "sistemico", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "meses", "severidade": "moderada", "ordem": 2},
            {"nome": "Prurido e erupção no local de penetração (larva migrans)", "sistema": "cutaneo", "tipo": "prodromico", "frequencia": "comum", "onset_texto": "dias após penetração", "severidade": "leve", "ordem": 3},
            {"nome": "Dor epigástrica e anorexia", "sistema": "digestivo", "tipo": "local", "frequencia": "comum", "onset_texto": "semanas", "severidade": "leve", "ordem": 4},
            {"nome": "Hipoalbuminemia e edema (infecção grave)", "sistema": "sistemico", "tipo": "complicacao", "frequencia": "incomum", "onset_texto": "meses", "severidade": "grave", "ordem": 5},
        ],
    },
    {
        "patologia_nome": "Tricuríase",
        "sintomas": [
            {"nome": "Diarreia intermitente (carga moderada)", "sistema": "digestivo", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "semanas após ingestão", "severidade": "leve", "ordem": 1},
            {"nome": "Dor abdominal leve", "sistema": "digestivo", "tipo": "local", "frequencia": "comum", "onset_texto": "semanas", "severidade": "leve", "ordem": 2},
            {"nome": "Prolapso retal (carga intensa em crianças)", "sistema": "digestivo", "tipo": "complicacao", "frequencia": "incomum", "onset_texto": "meses", "severidade": "grave", "ordem": 3},
            {"nome": "Anemia e hipoalbuminemia (carga intensa)", "sistema": "hematologico", "tipo": "complicacao", "frequencia": "incomum", "onset_texto": "meses", "severidade": "grave", "ordem": 4},
            {"nome": "Maioria assintomática (carga leve)", "sistema": "digestivo", "tipo": "sistemico", "frequencia": "muito_comum", "onset_texto": "variável", "severidade": "leve", "ordem": 5},
        ],
    },
    {
        "patologia_nome": "Estrongiloidíase",
        "sintomas": [
            {"nome": "Prurido perianal e cutâneo (larva currens)", "sistema": "cutaneo", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "semanas após infecção", "severidade": "leve", "ordem": 1},
            {"nome": "Dor epigástrica e diarreia intermitente", "sistema": "digestivo", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "semanas", "severidade": "leve", "ordem": 2},
            {"nome": "Síndrome de Löffler (tosse, eosinofilia)", "sistema": "respiratorio", "tipo": "prodromico", "frequencia": "comum", "onset_texto": "dias a semanas (fase pulmonar)", "severidade": "leve", "ordem": 3},
            {"nome": "Náuseas e vômitos", "sistema": "digestivo", "tipo": "sistemico", "frequencia": "comum", "onset_texto": "semanas", "severidade": "leve", "ordem": 4},
            {"nome": "Eosinofilia sanguínea", "sistema": "hematologico", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "semanas", "severidade": "leve", "ordem": 5},
        ],
    },
    {
        "patologia_nome": "Estrongiloidíase com Síndrome de Hiperinfecção",
        "sintomas": [
            {"nome": "Diarreia grave e sanguinolenta", "sistema": "digestivo", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "dias (imunocomprometido)", "severidade": "grave", "ordem": 1},
            {"nome": "Pneumonia intersticial e hemoptise", "sistema": "respiratorio", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "dias", "severidade": "grave", "ordem": 2},
            {"nome": "Sepse gram-negativa (pela larva carreando bactérias)", "sistema": "sistemico", "tipo": "complicacao", "frequencia": "muito_comum", "onset_texto": "dias", "severidade": "grave", "ordem": 3},
            {"nome": "Meningite bacteriana secundária", "sistema": "neurologico", "tipo": "complicacao", "frequencia": "comum", "onset_texto": "dias", "severidade": "grave", "ordem": 4},
            {"nome": "Larva currens extenso (rash serpiginoso)", "sistema": "cutaneo", "tipo": "cardinal", "frequencia": "comum", "onset_texto": "dias", "severidade": "leve", "ordem": 5},
        ],
    },
    {
        "patologia_nome": "Enterobíase (Oxiuríase)",
        "sintomas": [
            {"nome": "Prurido perianal noturno intenso", "sistema": "digestivo", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "semanas após ingestão", "severidade": "leve", "ordem": 1},
            {"nome": "Insônia e irritabilidade (especialmente em crianças)", "sistema": "neurologico", "tipo": "sistemico", "frequencia": "muito_comum", "onset_texto": "semanas", "severidade": "leve", "ordem": 2},
            {"nome": "Vermiculas visíveis na região perianal à noite", "sistema": "digestivo", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "semanas", "severidade": "leve", "ordem": 3},
            {"nome": "Vaginite por migração (meninas)", "sistema": "outro", "tipo": "complicacao", "frequencia": "incomum", "onset_texto": "semanas", "severidade": "leve", "ordem": 4},
        ],
    },
    {
        "patologia_nome": "Teníase",
        "sintomas": [
            {"nome": "Dor abdominal vaga e intermitente", "sistema": "digestivo", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "meses após ingestão", "severidade": "leve", "ordem": 1},
            {"nome": "Proglotes visíveis nas fezes ou roupa íntima", "sistema": "digestivo", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "meses", "severidade": "leve", "ordem": 2},
            {"nome": "Perda de peso e anorexia", "sistema": "sistemico", "tipo": "sistemico", "frequencia": "comum", "onset_texto": "meses", "severidade": "leve", "ordem": 3},
            {"nome": "Prurido perianal", "sistema": "digestivo", "tipo": "local", "frequencia": "comum", "onset_texto": "semanas a meses", "severidade": "leve", "ordem": 4},
            {"nome": "Maioria assintomática", "sistema": "digestivo", "tipo": "sistemico", "frequencia": "muito_comum", "onset_texto": "variável", "severidade": "leve", "ordem": 5},
        ],
    },
    {
        "patologia_nome": "Neurocisticercose",
        "sintomas": [
            {"nome": "Convulsões (forma mais comum de apresentação)", "sistema": "neurologico", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "meses a anos após ingestão", "severidade": "grave", "ordem": 1},
            {"nome": "Cefaleia crônica", "sistema": "neurologico", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "meses", "severidade": "moderada", "ordem": 2},
            {"nome": "Hipertensão intracraniana (hidrocefalia)", "sistema": "neurologico", "tipo": "complicacao", "frequencia": "muito_comum", "onset_texto": "meses", "severidade": "grave", "ordem": 3},
            {"nome": "Déficit neurológico focal", "sistema": "neurologico", "tipo": "complicacao", "frequencia": "comum", "onset_texto": "meses", "severidade": "grave", "ordem": 4},
            {"nome": "Meningite eosinofílica (cisticerco subaracnoide)", "sistema": "neurologico", "tipo": "complicacao", "frequencia": "incomum", "onset_texto": "meses", "severidade": "grave", "ordem": 5},
        ],
    },
    {
        "patologia_nome": "Esquistossomose Mansoni",
        "sintomas": [
            {"nome": "Dermatite cercariana ('coceira do nadador')", "sistema": "cutaneo", "tipo": "prodromico", "frequencia": "muito_comum", "onset_texto": "logo após exposição à água", "severidade": "leve", "ordem": 1},
            {"nome": "Febre de Katayama: febre, urticária, eosinofilia (fase aguda)", "sistema": "sistemico", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "4-8 semanas após exposição", "severidade": "moderada", "ordem": 2},
            {"nome": "Hepatomegalia e esplenomegalia (fase crônica)", "sistema": "digestivo", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "meses a anos", "severidade": "grave", "ordem": 3},
            {"nome": "Hipertensão portal e varizes esofágicas", "sistema": "digestivo", "tipo": "complicacao", "frequencia": "muito_comum", "onset_texto": "anos", "severidade": "grave", "ordem": 4},
            {"nome": "Diarreia crônica com muco ou sangue", "sistema": "digestivo", "tipo": "cardinal", "frequencia": "comum", "onset_texto": "meses", "severidade": "moderada", "ordem": 5},
            {"nome": "Hematúria (Schistosoma haematobium – fora do Brasil)", "sistema": "urinario", "tipo": "local", "frequencia": "raro", "onset_texto": "variável", "severidade": "leve", "ordem": 6},
        ],
    },
    {
        "patologia_nome": "Filariose Linfática (Bancroftose)",
        "sintomas": [
            {"nome": "Elefantíase (linfedema crônico de membros genitais)", "sistema": "cutaneo", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "anos após infecção", "severidade": "grave", "ordem": 1},
            {"nome": "Linfangite e linfadenite aguda recorrente", "sistema": "hematologico", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "meses", "severidade": "grave", "ordem": 2},
            {"nome": "Febre filariásica com calafrios", "sistema": "sistemico", "tipo": "sistemico", "frequencia": "muito_comum", "onset_texto": "meses", "severidade": "moderada", "ordem": 3},
            {"nome": "Hidrocele (em homens)", "sistema": "urinario", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "meses a anos", "severidade": "moderada", "ordem": 4},
            {"nome": "Microfilaremia assintomática", "sistema": "hematologico", "tipo": "sistemico", "frequencia": "muito_comum", "onset_texto": "meses", "severidade": "leve", "ordem": 5},
        ],
    },
    {
        "patologia_nome": "Toxocaríase (Larva Migrans Visceral)",
        "sintomas": [
            {"nome": "Eosinofilia elevada e hepatomegalia", "sistema": "hematologico", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "semanas a meses", "severidade": "moderada", "ordem": 1},
            {"nome": "Febre e mal-estar", "sistema": "sistemico", "tipo": "sistemico", "frequencia": "muito_comum", "onset_texto": "semanas", "severidade": "leve", "ordem": 2},
            {"nome": "Pneumonite com sibilância", "sistema": "respiratorio", "tipo": "local", "frequencia": "comum", "onset_texto": "semanas", "severidade": "leve", "ordem": 3},
            {"nome": "Endoftalmite por toxocara (granuloma ocular)", "sistema": "ocular", "tipo": "local", "frequencia": "incomum", "onset_texto": "meses", "severidade": "grave", "ordem": 4},
            {"nome": "Urticária recorrente", "sistema": "cutaneo", "tipo": "local", "frequencia": "comum", "onset_texto": "semanas", "severidade": "leve", "ordem": 5},
        ],
    },
    {
        "patologia_nome": "Larva Migrans Cutânea",
        "sintomas": [
            {"nome": "Trilha serpiginosa eritematosa e pruriginosa", "sistema": "cutaneo", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "dias após contato com solo contaminado", "severidade": "leve", "ordem": 1},
            {"nome": "Prurido intenso (especialmente noturno)", "sistema": "cutaneo", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "dias", "severidade": "leve", "ordem": 2},
            {"nome": "Vesículas ao longo da trilha", "sistema": "cutaneo", "tipo": "local", "frequencia": "comum", "onset_texto": "dias", "severidade": "leve", "ordem": 3},
            {"nome": "Localização preferencial em pés, nádegas e pernas", "sistema": "cutaneo", "tipo": "local", "frequencia": "muito_comum", "onset_texto": "dias", "severidade": "leve", "ordem": 4},
        ],
    },
    {
        "patologia_nome": "Hidatidose / Equinococose Cística",
        "sintomas": [
            {"nome": "Massa hepática assintomática (descoberta incidental)", "sistema": "digestivo", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "anos após ingestão", "severidade": "leve", "ordem": 1},
            {"nome": "Dor no hipocôndrio direito (cisto grande)", "sistema": "digestivo", "tipo": "cardinal", "frequencia": "comum", "onset_texto": "meses a anos", "severidade": "moderada", "ordem": 2},
            {"nome": "Icterícia obstrutiva (compressão biliar)", "sistema": "digestivo", "tipo": "complicacao", "frequencia": "incomum", "onset_texto": "meses a anos", "severidade": "grave", "ordem": 3},
            {"nome": "Anafilaxia por ruptura do cisto", "sistema": "sistemico", "tipo": "complicacao", "frequencia": "incomum", "onset_texto": "ruptura espontânea ou trauma", "severidade": "grave", "ordem": 4},
            {"nome": "Cisto pulmonar com hemoptise", "sistema": "respiratorio", "tipo": "local", "frequencia": "comum", "onset_texto": "meses a anos", "severidade": "grave", "ordem": 5},
        ],
    },
    {
        "patologia_nome": "Oncocercose",
        "sintomas": [
            {"nome": "Prurido intenso e crônico ('cegueira dos rios')", "sistema": "cutaneo", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "meses a anos após infecção", "severidade": "grave", "ordem": 1},
            {"nome": "Nódulos subcutâneos (oncocercomas)", "sistema": "cutaneo", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "meses a anos", "severidade": "leve", "ordem": 2},
            {"nome": "Ceratite esclerosante progressiva", "sistema": "ocular", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "meses a anos", "severidade": "grave", "ordem": 3},
            {"nome": "Cegueira (uveíte e atrofia óptica)", "sistema": "ocular", "tipo": "complicacao", "frequencia": "muito_comum", "onset_texto": "anos", "severidade": "grave", "ordem": 4},
            {"nome": "Despigmentação cutânea ('pele de leopardo')", "sistema": "cutaneo", "tipo": "cardinal", "frequencia": "comum", "onset_texto": "anos", "severidade": "leve", "ordem": 5},
        ],
    },
    {
        "patologia_nome": "Fasciolíase",
        "sintomas": [
            {"nome": "Dor em hipocôndrio direito (fase aguda: migração larval)", "sistema": "digestivo", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "3-6 semanas após ingestão", "severidade": "moderada", "ordem": 1},
            {"nome": "Febre e eosinofilia alta (fase aguda)", "sistema": "sistemico", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "3-6 semanas", "severidade": "moderada", "ordem": 2},
            {"nome": "Hepatomegalia dolorosa", "sistema": "digestivo", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "semanas", "severidade": "moderada", "ordem": 3},
            {"nome": "Colangite obstrutiva (fase crônica)", "sistema": "digestivo", "tipo": "complicacao", "frequencia": "comum", "onset_texto": "meses a anos", "severidade": "grave", "ordem": 4},
            {"nome": "Icterícia intermitente (fase crônica)", "sistema": "digestivo", "tipo": "complicacao", "frequencia": "comum", "onset_texto": "meses a anos", "severidade": "grave", "ordem": 5},
        ],
    },
    {
        "patologia_nome": "Pediculose do Couro Cabeludo",
        "sintomas": [
            {"nome": "Prurido intenso do couro cabeludo (especialmente occipital)", "sistema": "cutaneo", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "dias após infestação", "severidade": "leve", "ordem": 1},
            {"nome": "Visualização de lêndeas (ovos brancos aderidos ao cabelo)", "sistema": "cutaneo", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "dias a semanas", "severidade": "leve", "ordem": 2},
            {"nome": "Escoriações do couro cabeludo (pelo arranhado)", "sistema": "cutaneo", "tipo": "local", "frequencia": "muito_comum", "onset_texto": "dias", "severidade": "leve", "ordem": 3},
            {"nome": "Sobreinfecção bacteriana", "sistema": "cutaneo", "tipo": "complicacao", "frequencia": "comum", "onset_texto": "semanas", "severidade": "leve", "ordem": 4},
        ],
    },
    {
        "patologia_nome": "Escabiose (Sarna)",
        "sintomas": [
            {"nome": "Prurido noturno intenso e generalizado", "sistema": "cutaneo", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "2-6 semanas após infestação primária", "severidade": "grave", "ordem": 1},
            {"nome": "Túneis escabióticos (pápulas com canal linear)", "sistema": "cutaneo", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "semanas", "severidade": "leve", "ordem": 2},
            {"nome": "Pápulas eritematosas entre dedos, punhos e genitais", "sistema": "cutaneo", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "semanas", "severidade": "leve", "ordem": 3},
            {"nome": "Lesões por coceira e sobreinfecção bacteriana", "sistema": "cutaneo", "tipo": "complicacao", "frequencia": "muito_comum", "onset_texto": "semanas", "severidade": "moderada", "ordem": 4},
            {"nome": "Sarna norueguesa (hiperinfestaçao) em imunocomprometidos", "sistema": "cutaneo", "tipo": "complicacao", "frequencia": "incomum", "onset_texto": "semanas", "severidade": "grave", "ordem": 5},
        ],
    },
    {
        "patologia_nome": "Miiase",
        "sintomas": [
            {"nome": "Nódulo cutâneo com abertura e sensação de movimento", "sistema": "cutaneo", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "dias após postura", "severidade": "leve", "ordem": 1},
            {"nome": "Dor ou prurido local", "sistema": "cutaneo", "tipo": "cardinal", "frequencia": "muito_comum", "onset_texto": "dias", "severidade": "leve", "ordem": 2},
            {"nome": "Exsudato serossanguinolento", "sistema": "cutaneo", "tipo": "local", "frequencia": "muito_comum", "onset_texto": "dias", "severidade": "leve", "ordem": 3},
            {"nome": "Sobreinfecção bacteriana da lesão", "sistema": "cutaneo", "tipo": "complicacao", "frequencia": "comum", "onset_texto": "dias a semanas", "severidade": "moderada", "ordem": 4},
            {"nome": "Miiase cavitária (narina, ouvido — forma mais grave)", "sistema": "otorrinolaringologico", "tipo": "complicacao", "frequencia": "incomum", "onset_texto": "dias", "severidade": "grave", "ordem": 5},
        ],
    },
]

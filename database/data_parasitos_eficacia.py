"""
Dados de eficácia de antiparasitários — fontes oficiais brasileiras.
Fontes: PCDT-MS, SVS/GVS 5ª ed. 2022, SBMT, SBI, ANVISA.

Formato: dict {parasito_nome_cientifico: [(antip, pat_substr, efic_pct, linha, evidencia, resist_br, fonte_sigla, ano, obs)]}
"""

EFICACIA_PARASITARIA = {
    "Plasmodium falciparum": [
        ("Artemeter/Lumefantrina",     "falciparum", 95.0, 1, "A", 2.0,  "PCDT-MALARIA", 2022,
         "1ª linha P. falciparum não complicado no Brasil; 6 doses (0, 8, 24, 36, 48, 60h); eficácia > 95% com boa adesão; tomar com alimento gorduroso"),
        ("Artesunato",                 "Malária por Plasmodium falciparum", 97.0, 1, "A", 1.0, "PCDT-MALARIA", 2022,
         "Malária grave/complicada: artesunato IV superior à quinina (AQUAMAT/SEAQUAMAT); 2,4 mg/kg EV 0h, 12h, 24h, depois 1x/dia; disponível via SVS/FUNASA"),
        ("Quinino",                    "falciparum", 85.0, 2, "B", 5.0,  "PCDT-MALARIA", 2022,
         "Alternativa ao artesunato em malária grave quando indisponível; associar doxiciclina 7 dias; cinchonismo (zumbido, tontura, náusea); monitorar QT"),
        ("Doxiciclina (antipalúdica)", "falciparum", 90.0, 2, "B", 3.0,  "PCDT-MALARIA", 2022,
         "Associar ao artesunato ou quinino por 7 dias; não usar < 8 anos e na gestação; fotossensibilidade; profilaxia para viajantes"),
    ],

    "Plasmodium vivax": [
        ("Cloroquina",  "Malária por Plasmodium vivax", 97.0, 1, "A", 1.0, "PCDT-MALARIA", 2022,
         "1ª linha P. vivax no Brasil; esquema de 3 dias (25 mg base/kg total); P. vivax resistente à cloroquina reportado em casos isolados; associar primaquina para radical cure"),
        ("Primaquina",  "Malária por Plasmodium vivax", 92.0, 1, "A", 2.0, "PCDT-MALARIA", 2022,
         "Radical cure (eliminação de hipnozoítas): 0,5 mg/kg/dia por 7 dias (adultos) ou 0,25 mg/kg/dia por 14 dias; triagem G6PD obrigatória; contraindicada gestação, lactantes, G6PD grave"),
        ("Artemeter/Lumefantrina", "Malária por Plasmodium vivax", 95.0, 2, "B", 1.0, "PCDT-MALARIA", 2022,
         "Alternativa na suspeita de resistência à cloroquina; eficácia sobre formas sanguíneas; associar primaquina para radical cure; não elimina hipnozoítas"),
    ],

    "Plasmodium malariae": [
        ("Cloroquina", "Malária por Plasmodium malariae", 99.0, 1, "A", 0.0, "PCDT-MALARIA", 2022,
         "1ª linha P. malariae; não forma hipnozoítas — sem necessidade de primaquina para radical cure; mesmo esquema de P. vivax"),
    ],

    "Leishmania braziliensis": [
        ("Antimoniato de N-metilglucamina", "Tegumentar", 75.0, 1, "A", 15.0, "PCDT-LEISH-TEG", 2022,
         "Padrão-ouro LTA cutânea: 20 mg SbV/kg/dia IM por 20 dias; LTA mucosa: 30 dias; falha em 15-25% (L. braziliensis mais refratária que L. amazonensis); monitorar QT, enzimas pancreáticas, creatinina"),
        ("Anfotericina B lipossomal", "Tegumentar", 90.0, 1, "A", 2.0, "PCDT-LEISH-TEG", 2022,
         "1ª linha em gestantes, imunossuprimidos, forma mucosa grave, falha de antimoniato; 3 mg/kg/dia EV por 7-10 dias (LTA); alta eficácia com menor toxicidade que antimoniato"),
        ("Miltefosina",             "Tegumentar", 72.0, 2, "B", 5.0, "PCDT-LEISH-TEG", 2022,
         "2ª linha LTA por L. guyanensis e L. braziliensis; 2,5 mg/kg/dia por 28 dias; teratogênica — contraceptivo obrigatório; náusea/vômito em 30%; aprovada ANVISA"),
        ("Pentamidina isetionato",  "Tegumentar", 70.0, 2, "B", 8.0, "PCDT-LEISH-TEG", 2022,
         "2ª linha especialmente L. guyanensis (Amazônia); 4 mg/kg IM a cada 2 dias, 3-4 doses; hipoglicemia grave, nefrotoxicidade; monitorar glicemia antes e após cada dose"),
    ],

    "Leishmania amazonensis": [
        ("Antimoniato de N-metilglucamina", "Tegumentar", 80.0, 1, "A", 10.0, "PCDT-LEISH-TEG", 2022,
         "1ª linha LTA por L. amazonensis; melhor resposta que L. braziliensis; cutânea difusa (anérgica) responde mal — requerer associação ou Anf. B"),
        ("Anfotericina B lipossomal", "Tegumentar", 88.0, 2, "A", 2.0, "PCDT-LEISH-TEG", 2022,
         "Forma cutânea difusa (anérgica) por L. amazonensis: terapia de escolha pela refratariedade ao antimoniato; múltiplos ciclos frequentemente necessários"),
    ],

    "Leishmania infantum (chagasi)": [
        ("Antimoniato de N-metilglucamina", "Visceral", 80.0, 1, "A", 5.0, "PCDT-LEISH-VIS", 2022,
         "1ª linha LV em adultos imunocompetentes sem contraindicações cardíacas, renais ou hepáticas; 20 mg SbV/kg/dia EV por 30 dias; hospitalização obrigatória"),
        ("Anfotericina B lipossomal", "Visceral", 97.0, 1, "A", 0.5, "PCDT-LEISH-VIS", 2022,
         "1ª linha LV em gestantes, crianças < 1 ano, idosos > 50 anos, IRC, cardiopatias, insucesso de antimoniato; 3-5 mg/kg/dia EV por 7 dias (dose total 21-40 mg/kg); eficácia > 97%"),
        ("Miltefosina", "Visceral", 85.0, 2, "B", 3.0, "PCDT-LEISH-VIS", 2022,
         "2ª linha LV; alternativa oral para casos selecionados; 2,5 mg/kg/dia por 28 dias; eficácia inferior à Anf. B lipo; não disponível SUS rotina"),
    ],

    "Trypanosoma cruzi": [
        ("Benznidazol", "Chagas Aguda", 85.0, 1, "A", 5.0, "PCDT-CHAGAS", 2022,
         "1ª linha fase aguda: cura parasitológica > 80%; 5 mg/kg/dia em 2 doses por 60 dias; dermatose (rash) em 30%, neuropatia periférica, leucopenia — monitorar; iniciar o mais precocemente possível"),
        ("Benznidazol", "Chagas Crônica", 70.0, 1, "B", 5.0, "PCDT-CHAGAS", 2022,
         "Fase crônica indeterminada: 75-80% cura sorológica em jovens (ensaios BENEFIT e TRAENA); cardiopatia moderada: benefício discutível; contraindicado IRC grave, gravidez, hepatopatia grave"),
        # Nifurtimox 2ª linha aplica-se às DUAS fases onde o benznidazol é
        # usado (PCDT-CHAGAS/MS: alternativa em falha/intolerância) — duplicado
        # em Aguda e Crônica (S40, antes o substring genérico "Doença de Chagas"
        # casava ambas e grudava só numa arbitrária).
        ("Nifurtimox",  "Doença de Chagas Aguda", 75.0, 2, "B", 5.0, "PCDT-CHAGAS", 2022,
         "2ª linha: falha ou intolerância ao benznidazol; 8-10 mg/kg/dia adultos, 15-20 mg/kg/dia crianças por 60-90 dias; tolerância inferior; disponível via MS mediante solicitação"),
        ("Nifurtimox",  "Doença de Chagas Crônica", 75.0, 2, "B", 5.0, "PCDT-CHAGAS", 2022,
         "2ª linha: falha ou intolerância ao benznidazol; 8-10 mg/kg/dia adultos, 15-20 mg/kg/dia crianças por 60-90 dias; tolerância inferior; disponível via MS mediante solicitação"),
    ],

    "Toxoplasma gondii": [
        ("Sulfadiazina",   "Imunocomprometidos", 85.0, 1, "A", 0.5, "PCDT-TOXO", 2022,
         "Encefalite toxoplásmica (HIV/AIDS): associar SEMPRE com pirimetamina + ácido folínico; 1,5 g 6/6h; manter até resolução clínica/radiológica + CD4 > 200 por 6 meses; hidratação para prevenir cristalúria"),
        ("Pirimetamina",   "Imunocomprometidos", 85.0, 1, "A", 0.5, "PCDT-TOXO", 2022,
         "Encefalite toxoplásmica: 200 mg ataque, 50-75 mg/dia; associar SEMPRE ácido folínico 10-25 mg/dia; monitorar hemograma semanal; NUNCA usar sem ácido folínico"),
        ("Ácido folínico", "Imunocomprometidos", None, 1, "A", None, "PCDT-TOXO", 2022,
         "Adjuvante obrigatório com pirimetamina — previne depressão medular (anemia, leucopenia, plaquetopenia); 10-25 mg/dia; não usar ácido fólico (antagônico)"),
        ("Sulfadiazina",   "Toxoplasmose Congênita", 80.0, 1, "A", 0.5, "PCDT-TOXO", 2022,
         "Toxoplasmose congênita: neonatos por 12 meses; associar pirimetamina + ácido folínico; monitorar retina e SNC; tratamento precoce melhora prognóstico neurológico"),
        ("Sulfadiazina",   "Imunocompetentes", 75.0, 2, "B", 0.5, "SBI-PARASIT", 2022,
         "Toxoplasmose ocular em imunocompetente: indicada em lesões maiores, ameaçando mácula ou nervo óptico; associar pirimetamina; duração 4-6 semanas"),
    ],

    "Entamoeba histolytica": [
        ("Metronidazol", "Amebíase Intestinal", 92.0, 1, "A", 2.0, "SVS-PARASIT", 2022,
         "1ª linha amebíase intestinal: 750 mg 8/8h por 5-10 dias (adultos); 35-50 mg/kg/dia crianças; elimina formas trofozoítas mas não cistos luminais — associar amebicida luminal (paramomicina) após"),
        ("Metronidazol", "Abscesso Hepático Amebiano", 95.0, 1, "A", 1.0, "SVS-PARASIT", 2022,
         "Abscesso hepático amebiano: 750 mg 8/8h por 10 dias; resposta clínica rápida (24-72h); drenagem percutânea apenas em abscessos > 10 cm ou com risco de ruptura; associar amebicida luminal"),
        ("Tinidazol",    "Amebíase Intestinal", 90.0, 1, "A", 2.0, "SVS-PARASIT", 2022,
         "Alternativa ao metronidazol; 2 g/dia por 3 dias (intestinal) ou 5 dias (AHA); meia-vida mais longa; melhor tolerância GI; dose única possível para formas leves"),
    ],

    "Giardia lamblia (intestinalis/duodenalis)": [
        ("Metronidazol", "Giardíase", 85.0, 1, "A", 5.0, "SVS-PARASIT", 2022,
         "1ª linha giardíase: 250-500 mg 8/8h por 5-7 dias; falha em 10-20% (possível resistência ou reinfecção); repetir com tinidazol ou nitazoxanida em caso de falha"),
        ("Tinidazol",    "Giardíase", 90.0, 1, "A", 3.0, "SVS-PARASIT", 2022,
         "Alternativa superior ao metronidazol em dose única (2 g); maior taxa de cura; menor número de falhas; melhor tolerância; preferida em crianças pela facilidade posológica"),
        ("Nitazoxanida", "Giardíase", 80.0, 2, "B", 5.0, "SVS-PARASIT", 2022,
         "Alternativa em falha de nitroimidazóis; 500 mg 12/12h por 3 dias (adultos); 100-200 mg 12/12h crianças; moderada eficácia; útil em casos resistentes"),
    ],

    "Trichomonas vaginalis": [
        ("Metronidazol", "Tricomoníase", 88.0, 1, "A", 5.0, "SVS-PARASIT", 2022,
         "1ª linha tricomoníase: 2 g dose única (favorece adesão) ou 500 mg 12/12h por 7 dias; tratar parceiro simultaneamente; abstinência ou preservativo durante tratamento; resistência crescente"),
        ("Tinidazol",    "Tricomoníase", 92.0, 1, "A", 3.0, "SVS-PARASIT", 2022,
         "Alternativa superior para tricomoníase: 2 g dose única; maior taxa de cura que metronidazol dose única; preferida nas recorrências; tratar parceiro; segura na gestação > 1º trimestre"),
        ("Secnidazol",   "Tricomoníase", 85.0, 2, "B", 3.0, "SVS-PARASIT", 2022,
         "Dose única 2 g; boa tolerância; alternativa quando metronidazol/tinidazol não tolerados; não disponível SUS rotina"),
    ],

    "Cryptosporidium parvum": [
        ("Nitazoxanida", "Criptosporidiose", 60.0, 1, "B", None, "SBI-PARASIT", 2022,
         "Única droga com eficácia aprovada para criptosporidiose; moderada eficácia em imunossuprimidos; 500 mg 12/12h por 3-7 dias; em HIV/AIDS: reconstituição imune com TARV é essencial — sem ela, nitazoxanida tem eficácia limitada"),
    ],

    "Ascaris lumbricoides": [
        ("Albendazol",      "Ascaridíase", 98.0, 1, "A", 1.0, "SVS-PARASIT", 2022,
         "1ª linha ascaridíase: 400 mg dose única; eficácia > 95% na eliminação de vermes adultos; seguro em crianças > 1 ano; repetir em 2 semanas se necessário em infecções graves"),
        ("Mebendazol",      "Ascaridíase", 95.0, 1, "A", 1.0, "SVS-PARASIT", 2022,
         "Alternativa ao albendazol: 100 mg 12/12h por 3 dias ou 500 mg dose única; má absorção sistêmica; seguro em crianças > 2 anos"),
        ("Pirantel pamoato", "Ascaridíase", 90.0, 2, "B", 1.0, "SVS-PARASIT", 2022,
         "Alternativa segura em gestantes (> 1º trimestre); 11 mg/kg dose única (máx 1 g); paralisia neuromuscular do verme"),
    ],

    "Necator americanus": [
        ("Albendazol",      "Ancilostomíase", 75.0, 1, "A", 2.0, "SVS-PARASIT", 2022,
         "1ª linha ancilostomíase: 400 mg dose única; eficácia moderada para N. americanus (inferior a A. duodenale); 400 mg/dia por 3 dias para infecções intensas; associar ferro para anemia"),
        ("Mebendazol",      "Ancilostomíase", 70.0, 1, "A", 2.0, "SVS-PARASIT", 2022,
         "Alternativa: 100 mg 12/12h por 3 dias; eficácia similar ao albendazol; seguro em crianças; associar suplementação de ferro"),
    ],

    "Ancylostoma duodenale": [
        ("Albendazol", "Ancilostomíase", 88.0, 1, "A", 1.0, "SVS-PARASIT", 2022,
         "Mais eficaz que em N. americanus; 400 mg dose única suficiente; associar reposição de ferro em anemia"),
    ],

    "Trichuris trichiura": [
        ("Albendazol",  "Tricuríase", 50.0, 1, "B", 1.0, "SVS-PARASIT", 2022,
         "Eficácia inferior nesta espécie: 400 mg/dia por 3 dias; combinação albendazol + ivermectina aumenta eficácia; repetir ciclos em infecções intensas"),
        ("Mebendazol",  "Tricuríase", 60.0, 1, "A", 1.0, "SVS-PARASIT", 2022,
         "Ligeiramente superior ao albendazol para T. trichiura: 100 mg 12/12h por 3 dias; prolapso retal indica infecção intensa — múltiplos ciclos"),
        ("Ivermectina", "Tricuríase", 35.0, 2, "B", 1.0, "SVS-PARASIT", 2022,
         "Eficácia moderada isolada; sinergia comprovada com albendazol em combinação (aumenta para ~80%); 200 mcg/kg dose única"),
    ],

    "Strongyloides stercoralis": [
        ("Ivermectina",  "Estrongiloidíase", 95.0, 1, "A", 1.0, "SVS-PARASIT", 2022,
         "1ª linha estrongiloidíase não complicada: 200 mcg/kg/dia por 2 dias consecutivos; hiperinfecção: 200 mcg/kg/dia por ≥ 5 dias (até negativação de fezes); parasitemia alta — controlar com parasitológico de fezes"),
        ("Ivermectina",  "Hiperinfecção", 70.0, 1, "B", 2.0, "SVS-PARASIT", 2022,
         "Síndrome de hiperinfecção: 200 mcg/kg/dia subcutâneo ou oral até dois parasitológicos negativos consecutivos; associar antibioticoterapia para sepse gram-negativa; reconstituição imune quando possível"),
        ("Albendazol",   "Estrongiloidíase", 70.0, 2, "B", 2.0, "SVS-PARASIT", 2022,
         "2ª linha: 400 mg/dia por 3-7 dias; inferior à ivermectina; usar quando ivermectina não disponível; repetir ciclos conforme parasitológico"),
        ("Tiabendazol",  "Estrongiloidíase", 65.0, 3, "C", 2.0, "SVS-PARASIT", 2022,
         "3ª linha: tolerância inferior; 25 mg/kg 12/12h por 3 dias; em desuso no Brasil; hepatotoxicidade; manter como opção de resgate"),
    ],

    "Enterobius vermicularis": [
        ("Albendazol",       "Enterobíase", 98.0, 1, "A", 0.5, "SVS-PARASIT", 2022,
         "1ª linha enterobíase: 400 mg dose única; repetir em 2 semanas (elimina os ovos ingeridos antes da 1ª dose); tratar familiares simultaneamente; lavar roupas de cama em água quente"),
        ("Mebendazol",       "Enterobíase", 95.0, 1, "A", 0.5, "SVS-PARASIT", 2022,
         "Alternativa: 100 mg dose única; repetir em 2 semanas; mesma eficácia do albendazol; seguro em crianças > 2 anos"),
        ("Pirantel pamoato", "Enterobíase", 90.0, 2, "B", 0.5, "SVS-PARASIT", 2022,
         "Alternativa segura em gestantes: 11 mg/kg dose única; repetir em 2 semanas; não tratar no 1º trimestre"),
    ],

    "Wuchereria bancrofti": [
        ("Dietilcarbamazina (DEC)", "Filariose Linfática", 80.0, 1, "A", 1.0, "PCDT-FILARIA", 2022,
         "Microfilaricida + efeito macrofilaricida parcial; 6 mg/kg/dia por 12 dias (tratamento individual); MDA: dose única anual; reação de Mazzotti (febre, prurido, edema) por morte de microfilárias — paracetamol sintomático"),
        ("Ivermectina",            "Filariose Linfática", 75.0, 1, "A", 1.0, "PCDT-FILARIA", 2022,
         "Programa de eliminação (MDA): ivermectina + DEC + albendazol dose única anual; eficácia microfilaricida > 90%; redução carga ao longo de anos de MDA"),
        ("Albendazol",             "Filariose Linfática", 60.0, 2, "B", 1.0, "PCDT-FILARIA", 2022,
         "MDA: associado à DEC e ivermectina no programa de eliminação; sinérgico; macrofilaricida parcial"),
    ],

    "Toxocara canis": [
        ("Albendazol",  "Toxocaríase", 75.0, 1, "B", 1.0, "SVS-PARASIT", 2022,
         "Toxocaríase visceral e ocular: 400 mg 12/12h por 5-7 dias (adultos); 10-15 mg/kg/dia crianças; associar corticoide em formas oculares e pulmonares graves para reduzir inflamação pela morte das larvas"),
        ("Mebendazol",  "Toxocaríase", 65.0, 2, "B", 1.0, "SVS-PARASIT", 2022,
         "Alternativa ao albendazol; menor absorção sistêmica — desvantagem na toxocaríase tecidual; 100-200 mg 12/12h por 5 dias"),
    ],

    "Ancylostoma braziliense": [
        ("Albendazol",   "Larva Migrans Cutânea", 96.0, 1, "A", 0.5, "SVS-PARASIT", 2022,
         "1ª linha LMC: 400 mg/dia por 3 dias (oral); altamente eficaz; mata as larvas na epiderme; prurido alivia em 24-48h; superior ao tiabendazol tópico"),
        ("Ivermectina",  "Larva Migrans Cutânea", 95.0, 1, "A", 0.5, "SVS-PARASIT", 2022,
         "Alternativa: 200 mcg/kg dose única oral; eficácia similar ao albendazol; opção quando albendazol não disponível; resolução em 24-72h"),
        ("Tiabendazol",  "Larva Migrans Cutânea", 75.0, 2, "B", 0.5, "SVS-PARASIT", 2022,
         "Formulação tópica 10-15%: aplicar 3-5x/dia por 5-7 dias; útil para lesões localizadas; sem toxicidade sistêmica; inferior às opções orais para lesões múltiplas"),
    ],

    "Onchocerca volvulus": [
        ("Ivermectina", "Oncocercose", 95.0, 1, "A", 0.5, "SVS-PARASIT", 2022,
         "Programa de eliminação Yanomami: 150 mcg/kg dose única a cada 6-12 meses; microfilaricida; suprime microfilaremia por 6-12 meses; não mata vermes adultos (macrofilaricida mínimo); reação de Mazzotti possível"),
    ],

    "Schistosoma mansoni": [
        ("Praziquantel", "Esquistossomose Mansoni", 85.0, 1, "A", 3.0, "PCDT-ESQUIS", 2022,
         "Padrão-ouro esquistossomose mansoni no Brasil: 60 mg/kg dose única (adultos); 50 mg/kg crianças < 30 kg; taxa de cura 80-90%; retratamento se persistência de ovos; resistência emergindo em algumas áreas endêmicas"),
        ("Oxamniquina",  "Esquistossomose Mansoni", 75.0, 2, "B", 8.0, "PCDT-ESQUIS", 2022,
         "Alternativa ao praziquantel: 15 mg/kg dose única adultos; resistência documentada no NE; uso restrito a casos de falha ao praziquantel; não indicado em gestantes"),
    ],

    "Fasciola hepatica": [
        ("Triclabendazol",   "Fasciolíase", 90.0, 1, "A", 2.0, "SVS-PARASIT", 2022,
         "Único antiparasitário eficaz para F. hepatica (praziquantel NÃO funciona); 10 mg/kg dose única (repetir após 12h em infecções intensas); eficácia > 90%; solicitar via acesso especial ANVISA; ausência do fármaco na rede pública é obstáculo no Brasil"),
        ("Praziquantel",     "Fasciolíase", 10.0, 3, "D", None, "SVS-PARASIT", 2022,
         "Ineficaz para F. hepatica — resistência intrínseca da fasciola; NÃO utilizar; incluído apenas para documentar ineficácia"),
    ],

    "Taenia solium": [
        ("Praziquantel", "Teníase", 95.0, 1, "A", 1.0, "SVS-PARASIT", 2022,
         "1ª linha teníase por T. solium (SEM NCC); 5-10 mg/kg dose única; contraindicado se houver cisticercose ocular ou no SNC não tratada — pode causar inflamação grave com morte de cistos cerebrais; TC de crânio antes"),
        ("Albendazol",   "Teníase", 90.0, 1, "A", 1.0, "SVS-PARASIT", 2022,
         "Alternativa ao praziquantel; 400 mg/dia por 3 dias; também ativo contra cisticercos em NCC parenquimatosa (associar dexametasona)"),
        ("Niclosamida",  "Teníase", 88.0, 2, "B", 1.0, "SVS-PARASIT", 2022,
         "Alternativa sem risco de estimular inflamação cerebral (não absorvida): 2 g dose única mastigada; preferida quando há suspeita de NCC; não disponível SUS rotina"),
        ("Albendazol",   "Neurocisticercose", 70.0, 1, "A", 2.0, "PCDT-NCC", 2022,
         "NCC parenquimatosa viável: 15 mg/kg/dia em 2 doses por 8-30 dias; SEMPRE associar dexametasona 0,1-0,15 mg/kg/dia para prevenir edema por morte dos cistos; corticoterapia 2-3 dias antes"),
        ("Praziquantel",  "Neurocisticercose", 65.0, 2, "B", 2.0, "PCDT-NCC", 2022,
         "Alternativa para NCC parenquimatosa; 50 mg/kg/dia por 15-30 dias; menos utilizado que albendazol; contraindicado na NCC ocular e subaracnóidea basilar; sempre com corticoide"),
    ],

    "Taenia saginata": [
        ("Praziquantel", "Teníase", 98.0, 1, "A", 0.5, "SVS-PARASIT", 2022,
         "T. saginata: sem risco de cisticercose humana; praziquantel 5-10 mg/kg dose única; alta eficácia; não há necessidade de TC pré-tratamento (diferente de T. solium)"),
        ("Niclosamida",  "Teníase", 92.0, 2, "B", 0.5, "SVS-PARASIT", 2022,
         "Alternativa eficaz para T. saginata; 2 g dose única mastigada; não absorvida sistemicamente; não disponível SUS rotina"),
    ],

    "Echinococcus granulosus": [
        ("Albendazol", "Hidatidose", 60.0, 1, "B", 1.0, "SVS-PARASIT", 2022,
         "Tratamento adjuvante à cirurgia ou PAIR: 400 mg 12/12h em ciclos de 28 dias com intervalos de 14 dias; cirurgia definitiva permanece padrão-ouro; albendazol pré-PAIR reduz risco de anafilaxia e semeadura peritoneal"),
    ],

    "Pediculus humanus capitis": [
        ("Permetrina", "Pediculose", 90.0, 1, "A", 5.0, "SVS-PARASIT", 2022,
         "1ª linha pediculose: loção 1% aplicar no cabelo úmido 10 min, enxaguar; repetir em 7-10 dias para matar ninfas eclodidas; resistência crescente em algumas regiões do Brasil; pente fino remove lêndeas"),
        ("Ivermectina", "Pediculose", 85.0, 2, "B", 3.0, "SVS-PARASIT", 2022,
         "Alternativa oral quando permetrina tópica falha; 400 mcg/kg (200 mcg/kg em crianças) dose única, repetir em 7-10 dias; off-label para pediculose; eficaz em resistência ao permetrina"),
    ],

    "Sarcoptes scabiei": [
        ("Permetrina",        "Escabiose", 95.0, 1, "A", 3.0, "SVS-PARASIT", 2022,
         "Padrão-ouro escabiose: creme 5% aplicar do pescoço para baixo 8-12h; banho, trocar roupas; repetir em 7 dias; segura em gestantes, lactantes e crianças > 2 meses; tratar todos os contatos domiciliares simultaneamente"),
        ("Benzil benzoato 25%", "Escabiose", 88.0, 1, "A", 5.0, "SVS-PARASIT", 2022,
         "1ª linha SUS Brasil: aplicar do pescoço para baixo 12-24h, repetir em 3-5 dias consecutivos; irritante para pele e mucosas; não aplicar face e genitais de crianças pequenas; eficácia similar à permetrina"),
        ("Ivermectina",       "Escabiose", 92.0, 2, "A", 3.0, "SVS-PARASIT", 2022,
         "Alternativa oral ou para sarna crostosa: 200 mcg/kg dose única, repetir em 14 dias; sarna norueguesa: 200 mcg/kg/dia por 2 dias + repetir semanal por 2-3 semanas + permetrina tópica; facilita tratamento em coletividades"),
    ],

    "Cochliomyia hominivorax": [
        ("Ivermectina", "Miiase", 85.0, 1, "B", None, "SVS-PARASIT", 2022,
         "Miiase cavitária extensa: ivermectina oral 200 mcg/kg dose única facilita remoção das larvas; parafina líquida ou éter no orifício para matar/expulsar larvas antes da remoção mecânica; principal tratamento é mecânico (remoção manual)"),
    ],
}

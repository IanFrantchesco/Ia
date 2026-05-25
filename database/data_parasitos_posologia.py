"""
Posologia de antiparasitários — fontes oficiais brasileiras.
Fontes: PCDT-MS, SVS/GVS 5ª ed. 2022, SBMT, SBI, ANVISA.

Formato: lista de tuplas
(antip_nome, pat_substr, populacao, dose_unitaria, frequencia, via,
 dur_min, dur_max, duracao_texto, aj_renal:bool, aj_hepatico:bool, obs, fonte_sigla)
"""

POSOLOGIA_PARASITARIA = [
    # ── Antimaláricos ──────────────────────────────────────────────────────────
    ("Artemeter/Lumefantrina", "falciparum", "adultos",
     "80 mg/480 mg (4 comprimidos)", "0h, 8h, 24h, 36h, 48h, 60h — total 6 doses", "oral",
     3, 3, "3 dias (6 doses)", False, False,
     "Tomar com alimento gorduroso ou leite integral; comprimidos de 20 mg/120 mg (preferir formulação adulto); gestação 1º tri: quinino + clindamicina",
     "PCDT-MALARIA"),

    ("Artesunato", "Malária por Plasmodium falciparum", "adultos — malária grave",
     "2,4 mg/kg", "0h, 12h, 24h — depois 1x/dia", "iv/im",
     7, 7, "Mínimo 24h IV até poder tomar oral; completar com artemeter/lumefantrina oral", True, True,
     "Reconstituir com 1 mL de bicarbonato 5%, depois diluir em SG 5% 5 mL; infundir em 1-2 min IV ou IM na face anterior da coxa; disponível via SVS/FUNASA",
     "PCDT-MALARIA"),

    ("Cloroquina", "Malária por Plasmodium vivax", "adultos",
     "Dose total 25 mg base/kg: D1 10 mg/kg, D2 10 mg/kg, D3 5 mg/kg", "1x/dia por 3 dias", "oral",
     3, 3, "3 dias", False, False,
     "Comprimidos de 150 mg base; tomar após refeição para reduzir náusea; P. vivax: associar primaquina para radical cure",
     "PCDT-MALARIA"),

    ("Primaquina", "Malária por Plasmodium vivax", "adultos — G6PD normal",
     "0,5 mg/kg/dia (máx 30 mg/dia)", "1x/dia", "oral",
     7, 14, "7 dias (esquema curto) ou 14 dias (esquema padrão BR)", False, True,
     "Triagem G6PD obrigatória antes do uso; 0,25 mg/kg/dia por 14 dias se G6PD intermediária; comprimidos de 5 mg e 15 mg; gestação e lactantes: CONTRAINDICADO",
     "PCDT-MALARIA"),

    ("Quinino", "Malária por Plasmodium falciparum", "adultos — malária grave",
     "10 mg/kg (máx 600 mg)", "8/8h por 7 dias", "iv/oral",
     7, 7, "7 dias", True, True,
     "IV: diluir em SG 5% 250-500 mL, infundir em 4h; monitorar ECG (QT), glicemia; associar doxiciclina 100 mg 12/12h por 7 dias (adultos, exceto gestantes)",
     "PCDT-MALARIA"),

    # ── Antileishmania ─────────────────────────────────────────────────────────
    ("Antimoniato de N-metilglucamina", "Tegumentar", "adultos",
     "20 mg SbV/kg/dia (máx 3 ampolas/dia = 1215 mg SbV)", "1x/dia", "im/iv",
     20, 30, "20 dias LTA cutânea; 30 dias LTA mucosa", False, True,
     "Ampola de 5 mL = 405 mg SbV; IM: dividir doses > 3 mL em dois sítios; monitorar QTc (≥ 500ms: suspender), amilase, lipase, creatinina; contraindicado em cardiopatias e gestação",
     "PCDT-LEISH-TEG"),

    ("Antimoniato de N-metilglucamina", "Leishmaniose Visceral", "adultos",
     "20 mg SbV/kg/dia", "1x/dia IV lento (30 min)", "iv",
     30, 30, "30 dias", True, True,
     "Hospitalização obrigatória; monitorar ECG diário; interromper se QTc > 500ms; hemograma 2x/semana; contraindicado na gestação — usar Anf. B lipossomal",
     "PCDT-LEISH-VIS"),

    ("Anfotericina B lipossomal", "Leishmaniose Visceral", "adultos e crianças",
     "3 mg/kg/dia", "1x/dia IV em 30-60 min", "iv",
     7, 10, "7 dias (dose total mínima 21 mg/kg)", True, False,
     "Diluir em SG 5%; não misturar com SF; pré-medicar com paracetamol e anti-histamínico; monitorar creatinina, potássio, magnésio; proteger da luz; refrigerar",
     "PCDT-LEISH-VIS"),

    # ── Anti-Chagas ────────────────────────────────────────────────────────────
    ("Benznidazol", "Doença de Chagas Aguda", "adultos",
     "5-7 mg/kg/dia em 2 doses iguais", "12/12h", "oral",
     60, 60, "60 dias",  False, True,
     "Comprimidos de 100 mg; tomar após refeição; monitorar hemograma (leucopenia), enzimas hepáticas, função renal; exantema ocorre em 30% — anti-histamínico; suspender se leucócitos < 2.500/mm³",
     "PCDT-CHAGAS"),

    ("Benznidazol", "Doença de Chagas Crônica", "adultos",
     "5 mg/kg/dia em 2 doses", "12/12h", "oral",
     60, 60, "60 dias", False, True,
     "Fase crônica indeterminada — indicação em adultos jovens < 50 anos; cardiopatia leve-moderada (FEVE > 40%): benefício discutível; gerenciar efeitos adversos; ajustar dose em IRC",
     "PCDT-CHAGAS"),

    # ── Antiprotozoários Intestinais ───────────────────────────────────────────
    ("Metronidazol", "Amebíase Intestinal", "adultos",
     "750 mg", "8/8h", "oral",
     5, 10, "5-10 dias", False, True,
     "Evitar álcool durante e por 48h após tratamento; seguir com amebicida luminal (paramomicina 25-35 mg/kg/dia 8/8h por 7 dias) para eliminar cistos luminais",
     "SVS-PARASIT"),

    ("Metronidazol", "Abscesso Hepático Amebiano", "adultos",
     "750 mg", "8/8h", "oral/iv",
     10, 10, "10 dias", False, True,
     "IV se não tolerar oral; resposta clínica esperada em 24-72h; drenagem percutânea se > 10 cm, risco de ruptura ou falha em 72h; seguir com amebicida luminal",
     "SVS-PARASIT"),

    ("Metronidazol", "Giardíase", "adultos",
     "500 mg", "8/8h", "oral",
     7, 7, "7 dias", False, False,
     "Alternativa: 250 mg 8/8h por 5 dias; reproduzir com tinidazol em caso de falha; crianças: 15 mg/kg/dia 8/8h por 5 dias",
     "SVS-PARASIT"),

    ("Tinidazol", "Giardíase", "adultos",
     "2 g (dose única)", "dose única", "oral",
     1, 1, "Dose única", False, False,
     "Tomar com alimento; crianças > 3 anos: 50 mg/kg dose única (máx 2 g); repetir se necessário; superior ao metronidazol em dose única",
     "SVS-PARASIT"),

    ("Metronidazol", "Tricomoníase", "adultos",
     "2 g (dose única) OU 500 mg 12/12h por 7 dias", "dose única ou 12/12h", "oral",
     1, 7, "Dose única ou 7 dias", False, False,
     "Tratar parceiro/parceira simultaneamente; dose única favorece adesão; esquema de 7 dias se recorrência; gestação > 2º trimestre: seguro",
     "SVS-PARASIT"),

    ("Sulfadiazina", "Imunocomprometidos", "adultos — encefalite toxoplásmica",
     "1,5 g", "6/6h (4x/dia)", "oral",
     42, 180, "6 semanas (agudo) + profilaxia secundária indefinida até CD4 > 200 por 6 meses",
     True, False,
     "Sempre associar pirimetamina + ácido folínico; manter hidratação > 2 L/dia para prevenir cristalúria (urina alcalina — bicarbonato se necessário); monitorar creatinina",
     "PCDT-TOXO"),

    ("Pirimetamina", "Imunocomprometidos", "adultos — encefalite toxoplásmica",
     "200 mg ataque, depois 75 mg/dia", "dose de ataque 1x, depois 1x/dia", "oral",
     42, 180, "6 semanas fase aguda + profilaxia secundária", False, True,
     "SEMPRE associar ácido folínico 10-25 mg/dia; monitorar hemograma semanal nas primeiras 2 semanas; ajustar em hepatopatia; NUNCA usar sem ácido folínico",
     "PCDT-TOXO"),

    ("Sulfadiazina", "Toxoplasmose Congênita", "neonatos",
     "100 mg/kg/dia em 2 doses", "12/12h", "oral",
     365, 365, "12 meses", True, False,
     "Associar pirimetamina 1 mg/kg/dia + ácido folínico 10 mg/dia; monitorar retina trimestralmente; hemograma mensal; hidratação adequada",
     "PCDT-TOXO"),

    # ── Anti-helmintos ──────────────────────────────────────────────────────────
    ("Albendazol", "Ascaridíase", "adultos e crianças > 2 anos",
     "400 mg (adultos); 200 mg (< 2 anos)", "dose única", "oral",
     1, 1, "Dose única", False, False,
     "Tomar em jejum ou com alimento (sem diferença significativa); comprimidos mastigáveis; seguro a partir de 1 ano; gestação: evitar 1º trimestre",
     "SVS-PARASIT"),

    ("Albendazol", "Ancilostomíase", "adultos",
     "400 mg/dia", "1x/dia por 3 dias (infecção intensa)", "oral",
     1, 3, "1-3 dias conforme carga", False, False,
     "Dose única em infecções leves; 3 dias em infecções intensas com anemia; associar sulfato ferroso 60 mg/dia por 3-6 meses para anemia ferropriva",
     "SVS-PARASIT"),

    ("Albendazol", "Estrongiloidíase", "adultos",
     "400 mg/dia", "1x/dia", "oral",
     3, 7, "3-7 dias", False, False,
     "2ª linha; controlar com parasitológico de fezes 2-4 semanas após; repetir ciclos se necessário; monitorar enzimas hepáticas em cursos prolongados",
     "SVS-PARASIT"),

    ("Albendazol", "Enterobíase", "adultos e crianças > 2 anos",
     "400 mg (adultos); 200 mg (crianças)", "dose única, repetir em 14 dias", "oral",
     1, 1, "Dose única (repetir em 14 dias)", False, False,
     "Tratar familiares e contactantes simultaneamente; lavar roupas de cama e toalhas em água quente; cortar unhas; banho matinal antes do uso do banheiro elimina ovos perianais",
     "SVS-PARASIT"),

    ("Albendazol", "Teníase", "adultos",
     "400 mg/dia", "1x/dia", "oral",
     3, 3, "3 dias", False, False,
     "Alternativa ao praziquantel; TC de crânio antes para excluir NCC; confirmar expulsão da escólex nas fezes; repetir se necessário",
     "SVS-PARASIT"),

    ("Albendazol", "Neurocisticercose", "adultos",
     "15 mg/kg/dia em 2 doses (máx 400 mg 12/12h)", "12/12h", "oral",
     8, 30, "8-30 dias conforme forma e resposta", False, False,
     "SEMPRE com dexametasona 0,1-0,15 mg/kg/dia iniciada 2-3 dias antes; monitorar convulsões — anticonvulsivante se necessário; TC/RNM de controle em 3 meses; formas calcificadas não se beneficiam de antiparasitário",
     "PCDT-NCC"),

    ("Ivermectina", "Estrongiloidíase", "adultos",
     "200 mcg/kg/dia", "1x/dia por 2 dias", "oral",
     2, 14, "2 dias (simples); até negativação de fezes em hiperinfecção", False, False,
     "Tomar em jejum (2h antes e 2h após refeição para melhor absorção); disponível comprimidos 6 mg; controle com parasitológico 2-4 semanas após; hiperinfecção: cursos mais prolongados",
     "SVS-PARASIT"),

    ("Ivermectina", "Enterobíase", "adultos",
     "200 mcg/kg", "dose única, repetir em 14 dias", "oral",
     1, 1, "Dose única", False, False,
     "Alternativa quando albendazol/mebendazol não disponíveis; tratar contactantes; off-label para enterobíase — eficaz",
     "SVS-PARASIT"),

    ("Ivermectina", "Escabiose", "adultos",
     "200 mcg/kg", "dose única, repetir em 14 dias", "oral",
     1, 1, "1 dose (repetir em 14 dias)", False, False,
     "Sarna crostosa: 200 mcg/kg/dia por 2 dias, repetir semanal por 2-3 semanas + permetrina tópica simultânea; tratar todos contactantes simultaneamente; lavar roupas e lençóis",
     "SVS-PARASIT"),

    ("Ivermectina", "Larva Migrans Cutânea", "adultos",
     "200 mcg/kg", "dose única", "oral",
     1, 1, "Dose única", False, False,
     "Alternativa ao albendazol; eficaz em 24-72h; segura; preferida em lesões múltiplas ou em adultos com dificuldade de manter albendazol por 3 dias",
     "SVS-PARASIT"),

    ("Praziquantel", "Esquistossomose Mansoni", "adultos",
     "60 mg/kg", "dose única", "oral",
     1, 1, "Dose única", False, True,
     "Tomar com alimento para aumentar absorção e reduzir náusea; crianças < 30 kg: 50 mg/kg dose única; contraindicado na gestação (1º trimestre); controle parasitológico em 60-90 dias",
     "PCDT-ESQUIS"),

    ("Praziquantel", "Teníase", "adultos",
     "5-10 mg/kg", "dose única", "oral",
     1, 1, "Dose única", False, False,
     "T. solium: TC pré-tratamento obrigatório para excluir NCC; T. saginata: sem necessidade de TC; tomar em jejum ou com pouco alimento; seguir expulsão da escólex nas fezes",
     "SVS-PARASIT"),

    ("Dietilcarbamazina (DEC)", "Filariose Linfática", "adultos",
     "6 mg/kg/dia em 3 doses", "8/8h", "oral",
     12, 12, "12 dias (tratamento individual)", False, False,
     "Programa MDA: dose única anual; reação de Mazzotti nas primeiras 24-48h (febre, artralgia, prurido) — tratar sintomaticamente; NÃO usar em oncocercose (causa cegueira por reação de Mazzotti ocular)",
     "PCDT-FILARIA"),

    ("Triclabendazol", "Fasciolíase", "adultos",
     "10 mg/kg", "dose única (repetir após 12h em infecção intensa)", "oral",
     1, 1, "1-2 doses", False, True,
     "Tomar com refeição gordurosa (aumenta absorção); único fármaco eficaz para Fasciola; solicitar via acesso especial ANVISA; monitorar enzimas hepáticas; náusea frequente",
     "SVS-PARASIT"),

    # ── Ectoparasitoses ────────────────────────────────────────────────────────
    ("Permetrina", "Pediculose", "crianças e adultos",
     "Loção ou creme rinse 1% — quantidade suficiente para cobrir o couro cabeludo", "aplicação única, repetir em 7-10 dias", "tópico",
     1, 1, "Aplicação única (repetir em 7-10 dias)", False, False,
     "Aplicar no cabelo lavado e levemente seco; deixar 10 min; enxaguar; pente fino para remoção de lêndeas; lavar roupas de cama e acessórios em água > 60°C ou selar em saco plástico por 72h",
     "SVS-PARASIT"),

    ("Permetrina", "Escabiose", "adultos e crianças > 2 meses",
     "Creme 5% — quantidade suficiente do pescoço para baixo", "1 aplicação, repetir em 7 dias", "tópico",
     1, 1, "1 aplicação (repetir em 7 dias)", False, False,
     "Aplicar em toda a superfície corporal do pescoço para baixo (incluindo genitais, espaços interdigitais); manter 8-12h; banho; trocar roupas; tratar todos os contactantes simultaneamente no mesmo dia",
     "SVS-PARASIT"),

    ("Benzil benzoato 25%", "Escabiose", "adultos",
     "Solução 25% — aplicar do pescoço para baixo", "1x/dia por 3-5 dias consecutivos", "tópico",
     3, 5, "3-5 dias consecutivos", False, False,
     "1ª linha SUS Brasil; aplicar após banho, pele seca; manter 24h, banho; repetir aplicação; crianças < 2 anos: diluir a 12,5%; não aplicar no rosto; irritante ocular — evitar mucosas",
     "SVS-PARASIT"),
]

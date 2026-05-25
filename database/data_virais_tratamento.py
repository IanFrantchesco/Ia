"""
Tratamento padrão-ouro para cada patologia viral.
Fontes: PCDTs Ministério da Saúde (HIV 2022, Hepatite B 2022, Hepatite C 2022, Influenza, COVID-19),
        SVS/MS GVS 5ª ed. 2022, SBI, SBMT, ANVISA notas técnicas, OPAS/PAHO adaptado ao Brasil.

Formato por entrada:
(patologia_nome_substr, antiviral_principal, combinacao_ou_None,
 regime_resumido, duracao_resumida, justificativa,
 alternativa_alergia_ou_contraindicacao, alternativa_resistencia, obs_especiais,
 grau_recomendacao, nivel_evidencia, fonte_sigla, ano_diretriz)
"""

TRATAMENTO_PADRAO_OURO_VIRAL = [

    # ══════════════════════════════════════════════════════════════════
    # ARBOVIROSES
    # ══════════════════════════════════════════════════════════════════
    (
        "Dengue (formas leve, moderada e grave)",
        "Tratamento suportivo (sem antiviral específico)",
        None,
        "Grupo A (leve): repouso + hidratação oral + paracetamol. "
        "Grupo B (sinais de alarme): hidratação IV com SF 0,9% 10 mL/kg em 1h; repetir conforme resposta; "
        "monitoramento hematócrito 2/2h; reposição de plaquetas raramente indicada. "
        "Grupo C (dengue grave): reposição volêmica agressiva IV; suporte em UTI; transfusão se sangramento grave.",
        "Contínuo durante fase febril e 24-48h após",
        "Não existe antiviral específico aprovado para dengue. O manejo é definido pela classificação clínica e "
        "pelo hematócrito — hemoconcentração indica extravasamento plasmático, guia hidratação. "
        "AAS e AINEs são CONTRAINDICADOS por risco hemorrágico.",
        "Não há alternativa antiviral — manejo de suporte é o único tratamento",
        "Não se aplica — sem antivirais específicos aprovados",
        "SINAIS DE ALARME obrigatoriamente hospitalizados: dor abdominal intensa, vômitos persistentes, "
        "acúmulo de líquidos, sangramento de mucosas, letargia/irritabilidade, aumento do fígado > 2 cm, "
        "hematócrito subindo com queda de plaquetas.",
        "A", "I", "SVS-DENGUE", 2022
    ),
    (
        "Zika (infecção aguda e síndrome congênita)",
        "Tratamento suportivo (sem antiviral específico)",
        None,
        "Adultos: paracetamol (evitar AAS e AINEs), hidratação, repouso. "
        "Gestantes: monitoramento ultrassonográfico seriado a cada 3-4 semanas após infecção comprovada; "
        "RM fetal se micro/macrocefalia suspeita. "
        "Síndrome Congênita Zika: equipe multidisciplinar (neuropediatria, fisioterapia, fonoaudiologia, "
        "oftalmologia, cardiologia) desde o nascimento.",
        "Fase aguda: 5-7 dias",
        "Sem antiviral específico aprovado. Monitoramento rigoroso da gestação é fundamental — "
        "microcefalia pode ser detectada por ultrassom a partir da 20ª semana. "
        "A síndrome congênita requer suporte multiprofissional de longo prazo.",
        "Não há alternativa antiviral",
        "Não se aplica",
        "Gestante com Zika confirmada: notificação imediata ao SINAN. "
        "Transmissão sexual documentada: uso de preservativo por toda a gestação se parceiro infectado.",
        "A", "I", "SVS-DENGUE", 2022
    ),
    (
        "Chikungunya (aguda e crônica)",
        "Tratamento suportivo (sem antiviral específico)",
        None,
        "Fase aguda (primeiros 3-7 dias): paracetamol 500-1000 mg 6/6h; hidratação; repouso. "
        "Evitar AINEs nas primeiras 72h (máscara sintomas e risco hemorrágico). "
        "Fase subaguda/crônica (artrite > 3 meses): Ibuprofeno 600 mg 8/8h ou Naproxeno; "
        "Fisioterapia obrigatória. Artrite persistente refratária: Hidroxicloroquina 400 mg/dia VO (off-label); "
        "Metotrexato 10-15 mg/semana para poliartrite crônica grave.",
        "Fase aguda: 7-14 dias / Fase crônica: meses a anos",
        "Sem antiviral aprovado. Hidroxicloroquina foi estudada em CHIKV crônica com alguma evidência de redução "
        "da artralgia — amplamente usada no Brasil. Corticoides curtos (prednisona 0,5 mg/kg × 5-10 dias) "
        "usados em crises agudas refratárias, mas sem evidência robusta.",
        "Não há alternativa antiviral",
        "Não se aplica",
        "Formas graves atípicas (encefalite, miocardite, insuficiência hepática): internação em UTI, suporte "
        "de órgãos. Recém-nascidos de mães virêmicas no parto: encefalopatia grave — monitoramento intensivo.",
        "A", "I", "SVS-DENGUE", 2022
    ),
    (
        "Febre Amarela (silvestre e urbana)",
        "Tratamento suportivo intensivo (sem antiviral específico)",
        None,
        "UTI: suporte de função renal (diálise em IRA progressiva), transfusões de plaquetas e PFC em "
        "coagulopatia grave, ventilação mecânica em insuficiência respiratória, vasopressores em choque. "
        "Vitamina K IV em coagulopatia. Evitar heparinização.",
        "Fase tóxica: 7-14 dias de internação em UTI",
        "Sem antiviral específico eficaz. A vacina 17D é a medida preventiva mais eficaz do mundo "
        "(dose única, eficácia > 99%, proteção por > 10 anos ou vitalícia). "
        "A tríade insuficiência renal + hepática + hemorragia indica mau prognóstico.",
        "Não há alternativa antiviral",
        "Não se aplica",
        "VACINAÇÃO: dose única ao entrar em área de risco; disponível gratuitamente na rede SUS. "
        "Contraindicada em: imunodeprimidos graves, gestantes de 1º trimestre, < 9 meses, alergia a ovo. "
        "Reações pós-vacinais graves são raras (<1/100.000) mas existem (doença viscerotrópica e neurotrópica).",
        "A", "I", "SVS-FEBAMARELA", 2022
    ),

    # ══════════════════════════════════════════════════════════════════
    # HEPATITES VIRAIS
    # ══════════════════════════════════════════════════════════════════
    (
        "Hepatite A",
        "Tratamento suportivo (sem antiviral específico)",
        None,
        "Repouso relativo, dieta pobre em gorduras e rica em carboidratos, hidratação. "
        "Sintomáticos: antieméticos (ondansetrona), analgesia com paracetamol em dose baixa ≤ 2g/dia. "
        "Hepatite fulminante: internação em CTI, transplante hepático de emergência é a única opção curativa.",
        "Autolimitada: 2-4 semanas (maioria)",
        "HAV causa hepatite aguda autolimitada em > 99% dos casos. "
        "Vacinação anti-HAV disponível no SUS (2 doses; eficácia > 95%) é a melhor estratégia de prevenção. "
        "Não há indicação de antiviral.",
        "Não há alternativa antiviral",
        "Não se aplica",
        "Hepatopatas crônicos com HAV têm risco aumentado de hepatite fulminante — vacinação prioritária. "
        "Notificação compulsória obrigatória e investigação de fonte (água, alimentos).",
        "A", "I", "SVS-HEPAT-AE", 2022
    ),
    (
        "Hepatite B (aguda e crônica)",
        "Tenofovir disoproxila (TDF)",
        None,
        "HBV crônico com indicação de tratamento (HBV DNA > 2.000 UI/mL + atividade histológica OU "
        "cirrose OU coinfecção HIV): TDF 300 mg VO 24/24h indefinidamente OU "
        "Entecavir 0,5 mg VO 24/24h em jejum. "
        "HBV aguda: tratamento antiviral geralmente não indicado — autolimitada em adultos. "
        "Hepatite B fulminante: TDF imediato + avaliação para transplante hepático.",
        "Indefinido (crônico) — descontinuação apenas com soroconversão HBsAg sustentada",
        "TDF e ETV têm alta barreira genética — resistência rara (< 1% em 5 anos). "
        "TDF preferido em gestantes e co-infectados HIV/HBV por cobertura dupla. "
        "Interferon peguilado é alternativa com duração limitada (48 semanas) e potencial de soroconversão HBeAg/HBsAg.",
        "Entecavir 0,5 mg VO 24/24h — contraindicação ao TDF (insuficiência renal grave sem ajuste possível)",
        "Tenofovir alafenamida (TAF) — toxicidade renal ou óssea documentada ao TDF",
        "Gestante com HBV DNA > 200.000 UI/mL: TDF a partir da 28ª semana + imunoglobulina anti-HBs e vacina "
        "ao RN nas primeiras 12h de vida. Rastrear HBsAg em TODAS as gestantes no pré-natal.",
        "A", "I", "PCDT-HEPB", 2022
    ),
    (
        "Hepatite C (aguda e crônica)",
        "Sofosbuvir/Velpatasvir (SOF/VEL)",
        None,
        "Genótipo 1: SOF/LED (400/90 mg) 1 cp/dia × 8-12 semanas OU SOF/VEL (400/100 mg) 1 cp/dia × 12 semanas. "
        "Genótipos 2-6: SOF/VEL 1 cp/dia × 12 semanas (pangenotípico). "
        "GLE/PIB (300/120 mg) 3 cp/dia × 8 semanas (sem cirrose) ou × 12 semanas (com cirrose compensada). "
        "Com cirrose Child-Pugh B: SOF/VEL + RBV × 12 semanas.",
        "8-12 semanas (meta: RVS12 = cura)",
        "DAAs pangenotípicos atingem RVS (resposta virológica sustentada = cura) em > 95-98% dos casos. "
        "RVS = HCV RNA indetectável 12 semanas após o final do tratamento. "
        "Todos os portadores de HCV com indicação de tratamento devem ser tratados com DAAs no SUS.",
        "GLE/PIB — insuficiência renal grave/diálise (não requer ajuste renal; SOF contraindicado em ClCr < 30)",
        "Repetir esquema com DAA diferente após análise de resistência (RAS) — falha primária é rara",
        "Tratar TODOS os portadores de HCV: a cura elimina a transmissão e previne cirrose e CHC. "
        "Cirrose Child-Pugh C: encaminhar para avaliação de transplante. "
        "Coinfectados HIV/HCV: atenção às interações entre DAAs e ARVs.",
        "A", "I", "PCDT-HEPC", 2022
    ),
    (
        "Hepatite D (Coinfecção e Superinfecção por HDV)",
        "Interferon alfa-2a peguilado (Peg-IFN-α2a)",
        None,
        "Peg-IFN-α2a 180 mcg SC 1x/semana × 48-72 semanas. "
        "Associar TDF se HBV DNA > 2.000 UI/mL para controle do HBV. "
        "Bulev­irtidin (bulevirtide 2 mg SC/dia) — novo inibidor de entrada do HDV — aprovado na Europa; "
        "ainda não disponível no Brasil em 2024.",
        "48-72 semanas",
        "Peg-IFN é o único tratamento disponível no Brasil para HDV; supressão sustentada em ~25-30% dos casos. "
        "Vacinação contra HBV previne também o HDV — medida preventiva mais eficaz. "
        "Bulevirtide tem eficácia superior ao interferon e aguarda aprovação pela ANVISA.",
        "Não há alternativa aprovada no Brasil além do Peg-IFN",
        "Bulevirtide 2 mg SC/dia — investigacional / acesso via importação excepcional",
        "HDV é endêmico na Amazônia brasileira — rastrear anti-HDV em todos os HBsAg positivos da região. "
        "A coinfecção HBV/HDV tem pior prognóstico que HBV isolado — maior risco de cirrose rápida.",
        "A", "II", "PCDT-HEPB", 2022
    ),
    (
        "Hepatite E",
        "Tratamento suportivo (sem antiviral específico em imunocompetentes)",
        None,
        "Imunocompetentes: suporte — repouso, hidratação, dieta; autolimitada em 4-6 semanas. "
        "Gestantes com hepatite fulminante: internação em UTI, transplante hepático de emergência. "
        "Transplantados com HEV crônico: reduzir imunossupressão (1ª medida) + "
        "Ribavirina 600-1000 mg/dia VO × 3-6 meses (off-label; RVS ~78%).",
        "Aguda: 4-6 semanas (autolimitada) / Crônica em transplantados: 3-6 meses de RBV",
        "HEV é autolimitado em imunocompetentes sem indicação de antiviral. "
        "Em transplantados, a cronicidade (HEV RNA > 3 meses) requer intervenção. "
        "Ribavirina (off-label) é a única opção com evidência para HEV crônico.",
        "Não há alternativa para imunocompetentes — suportivo apenas",
        "Sofosbuvir: estudos in vitro promissores, sem evidência clínica suficiente para uso rotineiro",
        "Mortalidade em gestantes com HEV fulminante alcança 20-25% no 3º trimestre. "
        "Ribavirina é CONTRAINDICADA na gestação — dilema clínico em gestantes com HEV grave.",
        "A", "II", "SVS-HEPAT-AE", 2022
    ),

    # ══════════════════════════════════════════════════════════════════
    # RETROVIROSES
    # ══════════════════════════════════════════════════════════════════
    (
        "HIV/AIDS (infecção aguda, crônica e AIDS estabelecida)",
        "Dolutegravir (DTG)",
        "+ Tenofovir disoproxila (TDF) + Lamivudina (3TC)",
        "Esquema preferencial SUS (TLD): TDF 300 mg + 3TC 300 mg + DTG 50 mg — 1 comprimido ao dia. "
        "Alternativas: ABC/3TC + DTG (quando TDF contraindicado). "
        "Coinfecção TB/HIV: DTG 50 mg 12/12h (dose dupla) + TDF/3TC durante rifampicina. "
        "Gestante: TDF + 3TC + DTG (após aconselhamento sobre risco de defeito de tubo neural no 1º trimestre). "
        "PrEP: TDF/FTC 1 cp/dia.",
        "Indefinido (tratamento permanente)",
        "O esquema TLD (TDF+3TC+DTG) é o padrão-ouro mundial e do SUS brasileiro. "
        "DTG tem alta barreira genética (dificilmente seleciona resistências), excelente tolerabilidade e "
        "conveniente posologia de 1 cp/dia. Meta: carga viral indetectável (< 50 cópias/mL) em 6 meses. "
        "Indetectável = Intransmissível (I=I): carga viral indetectável em uso regular de ARV garante "
        "que não há transmissão sexual do HIV.",
        "ABC + 3TC + DTG — contraindicação ao TDF (insuficiência renal grave) ou toxicidade renal",
        "Darunavir/ritonavir (DRV/r) + TDF + 3TC — após falha virológica com resistência ao DTG",
        "Início imediato do TARV em TODOS os portadores de HIV, independente de CD4 (Universal Test and Treat). "
        "CD4 e carga viral a cada 6 meses. Profilaxias infecciosas em CD4 < 200: SMX-TMP (Pneumocystis, Toxoplasma). "
        "Vacinação: pneumocócica, influenza anual, hepatite A e B, HPV.",
        "A", "I", "PCDT-HIV", 2022
    ),
    (
        "Infecção pelo HTLV-1 (portador e formas clínicas)",
        "Tratamento suportivo e imunomodulador (sem antiviral específico eficaz)",
        None,
        "Portador assintomático: acompanhamento semestral (hemograma, neurológico). "
        "HAM/TSP: Pulsoterapia com Metilprednisolona 1 g IV × 5 dias em exacerbações agudas; "
        "Interferon alfa-2a SC 3x/semana (off-label) para manutenção; "
        "Baclofeno 10-80 mg/dia para espasticidade; fisioterapia intensiva. "
        "ATLL aguda/linfomatosa: VCAP-AMP-VECP (quimioterapia combinada); "
        "transplante alogênico de células-tronco em remissão (único potencial curativo).",
        "Indefinido (doença crônica sem cura)",
        "Não existe antiviral específico que altere o curso da infecção pelo HTLV-1. "
        "Zidovudina + interferon-alfa mostrou benefício no subtipo indolente da ATLL em estudos japoneses. "
        "Mogamulizumabe (anti-CCR4) aprovado no Japão e EUA para ATLL — não disponível no SUS.",
        "Não há alternativa antiviral curative aprovada no Brasil",
        "Mogamulizumabe (acesso investigacional) — ATLL refratária",
        "Brasil é o maior foco de HTLV-1 fora do Japão. Triagem em bancos de sangue é obrigatória. "
        "Lactente de mãe HTLV-1 positiva: suspender aleitamento materno (principal via de transmissão pediátrica). "
        "Rastrear contatos sexuais.",
        "A", "III", "SVS-HTLV", 2022
    ),

    # ══════════════════════════════════════════════════════════════════
    # HERPESVIROSES
    # ══════════════════════════════════════════════════════════════════
    (
        "Herpes Simples (orolabial, genital e neonatal)",
        "Aciclovir (ACV)",
        None,
        "Primo-infecção orolabial: aciclovir 200 mg VO 5x/dia × 5 dias. "
        "Primo-infecção genital: aciclovir 400 mg VO 3x/dia × 7-10 dias "
        "OU valaciclovir 1 g VO 2x/dia × 7-10 dias. "
        "Supressão crônica (≥ 6 recorrências/ano): aciclovir 400 mg 2x/dia indefinidamente "
        "OU valaciclovir 500 mg/dia (reduz transmissão ao parceiro em 48%). "
        "Herpes neonatal: aciclovir IV 20 mg/kg 8/8h × 14-21 dias (EMERGÊNCIA).",
        "5-10 dias (primo-infecção) / Indefinido (supressão)",
        "Aciclovir é o padrão mundial para HSV-1 e HSV-2. Foscarnet em HSV resistente ao aciclovir "
        "(mutação TK; principalmente em imunossuprimidos). "
        "Herpes neonatal sem aciclovir tem mortalidade > 85% nas formas disseminadas.",
        "Valaciclovir — melhor biodisponibilidade oral, posologia mais conveniente",
        "Foscarnet IV — HSV resistente ao aciclovir (imunossuprimidos/HIV)",
        "Gravidez: aciclovir é seguro em todos os trimestres. Suprimir herpes genital a partir da 36ª semana "
        "para reduzir risco de herpes neonatal. Cesárea se lesões ativas no parto.",
        "A", "I", "SBI-VIRAL", 2022
    ),
    (
        "Varicela (catapora)",
        "Aciclovir (ACV)",
        None,
        "Crianças imunocompetentes < 12 anos com varicela leve: tratamento opcional (início em ≤ 24h). "
        "Indicações obrigatórias de aciclovir oral: adultos, gestantes, ≥ 12 anos, imunossuprimidos leves. "
        "Aciclovir VO: 800 mg 5x/dia × 5-7 dias (adultos) ou 20 mg/kg 4x/dia × 5 dias (crianças). "
        "Formas graves / imunossuprimidos / varicela disseminada: aciclovir IV 10 mg/kg 8/8h × 7-10 dias.",
        "5-7 dias VO / 7-10 dias IV (graves)",
        "Aciclovir em ≤ 24h do exantema reduz número de lesões, duração da febre e complicações. "
        "Vacinação (SCRV/VarVax) previne 99% das formas graves e é o padrão de prevenção. "
        "Imunoglobulina varicela-zoster (IGVZ) disponível no CRIE para imunossuprimidos expostos.",
        "Valaciclovir 1 g 3x/dia × 7 dias — adultos; melhor biodisponibilidade",
        "Foscarnet IV — VZV resistente ao aciclovir (muito raro; apenas em imunossuprimidos graves)",
        "Varicela em gestante: risco de varicela congênita (1-2%) e pneumonite grave na mãe. "
        "Neonato nascido de mãe com varicela periparto: IGVZ IM nas primeiras 72-96h de vida + aciclovir IV se doença.",
        "A", "I", "SVS-VARICELA", 2022
    ),
    (
        "Herpes Zoster (cobreiro)",
        "Valaciclovir (VACV)",
        None,
        "Valaciclovir 1 g VO 3x/dia × 7 dias (PREFERIDO — melhor que aciclovir em nevralgia pós-herpética). "
        "Alternativa: aciclovir 800 mg VO 5x/dia × 7 dias. "
        "Zoster disseminado / imunossuprimidos / zoster oftálmico grave: aciclovir IV 10 mg/kg 8/8h × 7-10 dias. "
        "Dor aguda: analgesia em escada (paracetamol → tramadol → opioides); gabapentina/pregabalina "
        "para reduzir nevralgia pós-herpética.",
        "7 dias antivirais + analgesia por semanas a meses",
        "Antivirais iniciados em ≤ 72h do exantema reduzem duração, gravidade e frequência da nevralgia pós-herpética. "
        "Valaciclovir é superior ao aciclovir oral para esta indicação por concentrações plasmáticas mais sustentadas. "
        "Corticoides (prednisona × 3 semanas) podem reduzir dor aguda mas não previnem nevralgia pós-herpética.",
        "Aciclovir 800 mg 5x/dia × 7 dias — indisponibilidade de valaciclovir",
        "Foscarnet IV — VZV resistente ao aciclovir (raro, apenas em imunossuprimidos)",
        "Vacina contra herpes zoster (Shingrix/recombinante adjuvantada): 2 doses; eficácia 97% em > 50 anos; "
        "disponível no setor privado e SUS para imunossuprimidos > 50 anos. "
        "Zoster oftálmico: encaminhamento urgente à oftalmologia; aciclovir IV obrigatório.",
        "A", "I", "SVS-VARICELA", 2022
    ),
    (
        "Citomegalovirose (CMV) em Imunocomprometidos",
        "Ganciclovir (GCV)",
        None,
        "Indução: ganciclovir IV 5 mg/kg 12/12h × 14-21 dias. "
        "Manutenção: valganciclovir 900 mg VO 24/24h (bioequivalente ao ganciclovir IV). "
        "CMV Congênito sintomático: valganciclovir VO (16 mg/kg 12/12h neonatos) × 6 meses. "
        "Profilaxia em transplantados (D+/R-): valganciclovir 900 mg/dia × 100-200 dias.",
        "Indução 14-21 dias IV + manutenção até reconstituição imune",
        "Ganciclovir IV é o padrão-ouro para CMV ativo em imunossuprimidos. "
        "Valganciclovir oral é equivalente para manutenção e profilaxia. "
        "CMV congênito sintomático: valganciclovir por 6 meses melhora desfechos auditivos e neurológicos "
        "(estudo CASG 112).",
        "Foscarnet IV — resistência ao ganciclovir (mutação UL97 ou UL54)",
        "Foscarnet + Ganciclovir (combinação) — CMV com dupla resistência",
        "PVHIV com CD4 < 50 células/mm³: realizar fundoscopia para rastrear retinite por CMV. "
        "Retinite por CMV (emergência oftalmológica): ganciclovir intravítreo + sistêmico + TARV urgente. "
        "Reconstituição imune com TARV é o objetivo final em PVHIV.",
        "A", "I", "SBI-VIRAL", 2022
    ),
    (
        "Mononucleose Infecciosa (EBV)",
        "Tratamento suportivo (sem antiviral específico indicado)",
        None,
        "Repouso relativo, paracetamol para febre e dor, hidratação adequada. "
        "EVITAR AAS (Síndrome de Reye em < 18 anos). "
        "EVITAR esportes de contato por 3-4 semanas (risco de ruptura esplênica). "
        "Corticoide IV (metilprednisolona 1-2 mg/kg/dia × 5 dias) indicado em: obstrução de vias aéreas, "
        "trombocitopenia grave (< 20.000), anemia hemolítica autoimune. "
        "Amoxicilina/ampicilina: CONTRAINDICADAS — causam exantema maculopapular em > 80% dos casos.",
        "Autolimitada: 2-4 semanas",
        "Aciclovir e valaciclovir suprimem replicação do EBV durante o uso mas não alteram a evolução clínica "
        "— não são indicados na mononucleose típica. A imunidade celular do hospedeiro controla a infecção. "
        "Síndrome linfoproliferativa pós-transplante (EBV+): reduzir imunossupressão + rituximabe.",
        "Não há alternativa antiviral indicada",
        "Rituximabe — síndrome linfoproliferativa grave em transplantados (EBV+)",
        "Linfoma de Burkitt (EBV+) e linfoma de Hodgkin (EBV+): requerem quimioterapia específica. "
        "EBV em HIV: linfoma SNC primário — encaminhar oncologia. "
        "Evitar ampicilina/amoxicilina em suspeita de mononucleose.",
        "A", "I", "SBI-VIRAL", 2022
    ),

    # ══════════════════════════════════════════════════════════════════
    # INFECÇÕES RESPIRATÓRIAS VIRAIS
    # ══════════════════════════════════════════════════════════════════
    (
        "Influenza (gripe sazonal e pandêmica)",
        "Oseltamivir (OST)",
        None,
        "Grupos de risco: oseltamivir 75 mg VO 12/12h × 5 dias — iniciar em ≤ 48h dos sintomas. "
        "Hospitalizados / influenza grave: iniciar oseltamivir independente do tempo de início dos sintomas. "
        "Formas leves em imunocompetentes saudáveis: tratamento sintomático (paracetamol, hidratação, repouso) "
        "sem antiviral obrigatório.",
        "5 dias (tratamento) / 10 dias (profilaxia pós-exposição)",
        "Oseltamivir reduz duração dos sintomas em ~1,3 dias e complicações em grupos de risco. "
        "Início em ≤ 48h maximiza o benefício, mas hospitalização por influenza grave justifica início tardio. "
        "Vacinação anual gratuita no SUS é a medida preventiva mais eficaz.",
        "Zanamivir inalatório — resistência ao oseltamivir (H275Y em H1N1) ou impossibilidade oral",
        "Baloxavir marboxil 40-80 mg VO dose única — cepas resistentes ao oseltamivir",
        "Grupos prioritários para vacinação anual gratuita no SUS: gestantes, puérperas, crianças 6 meses-5 anos, "
        "idosos ≥ 60 anos, profissionais de saúde, portadores de doenças crônicas, indígenas, população privada de liberdade. "
        "Vigilância virológica (SIVEP-Gripe) permite monitorar cepas circulantes e resistência ao oseltamivir.",
        "A", "I", "PCDT-INFLUENZA", 2022
    ),
    (
        "COVID-19 (infecção aguda, grave e síndrome pós-COVID)",
        "Nirmatrelvir/Ritonavir (NMV/r)",
        None,
        "COVID-19 leve-moderado em alto risco de progressão: Paxlovid (NMV/r) 300/100 mg VO 12/12h × 5 dias — "
        "iniciar em ≤ 5 dias dos sintomas. "
        "Hospitalizado com necessidade de O₂: remdesivir IV 200 mg D1, 100 mg D2-D5 + dexametasona 6 mg/dia × 10 dias. "
        "UTI com VMI ou ECMO: dexametasona 6 mg/dia IV × 10 dias + baricitinibe 4 mg IV × 14 dias. "
        "COVID leve em baixo risco: sintomáticos.",
        "5 dias (Paxlovid) / 5-10 dias (remdesivir/dexametasona)",
        "Paxlovid reduz hospitalização/morte em 89% em não vacinados com fatores de risco. "
        "Dexametasona reduz mortalidade em 35% em pacientes com VMI (RECOVERY Trial). "
        "Vacinação é a principal medida preventiva — alta eficácia contra formas graves.",
        "Molnupiravir 800 mg VO 12/12h × 5 dias — contraindicação ao Paxlovid (interações insuperáveis)",
        "Remdesivir IV ambulatorial × 3 dias — alternativa ao Paxlovid para ambulatorial de alto risco",
        "Síndrome pós-COVID: não há tratamento antiviral específico — reabilitação multidisciplinar "
        "(fisioterapia, reabilitação cognitiva, suporte psicológico). "
        "VERIFICAR TODAS AS INTERAÇÕES MEDICAMENTOSAS antes de prescrever Paxlovid — mais de 100 interações relevantes.",
        "A", "I", "PCDT-COVID19", 2022
    ),
    (
        "Infecção pelo Vírus Sincicial Respiratório (VSR/RSV)",
        "Tratamento suportivo (sem antiviral específico em uso rotineiro)",
        None,
        "Bronquiolite em lactentes: oxigênio suplementar (SpO₂ > 92-94%), aspiração de vias aéreas, "
        "posicionamento elevado, hidratação adequada (VO ou SNG; evitar IV excessivo). "
        "Broncodilatadores (salbutamol): benefício limitado — usar apenas se resposta documentada. "
        "Adrenalina nebulizada: pode reduzir hospitalização em formas moderadas. "
        "EVITAR: corticoides de rotina (sem evidência), antibióticos (sem infecção bacteriana secundária).",
        "7-14 dias (bronquiolite)",
        "Ribavirina inalatória (disponível) tem evidência insuficiente e não é recomendada rotineiramente. "
        "Palivizumabe (anticorpo monoclonal) disponível no SUS para profilaxia em prematuros < 29 semanas "
        "e cardiopatas congênitas cianóticas. "
        "Nirsevimabe (eficácia > 74% em prevenção de hospitalização) em implantação no Brasil.",
        "Não há alternativa antiviral eficaz para uso rotineiro",
        "Nirsevimabe IM dose única — profilaxia universal de lactentes (em implantação)",
        "Prematuros < 29 semanas: palivizumabe IM 15 mg/kg mensalmente nos meses de epidemia (máximo 5 doses). "
        "CRITÉRIOS DE INTERNAÇÃO: SpO₂ < 92% em ar ambiente, desconforto respiratório moderado-grave, "
        "apneias, impossibilidade de alimentação oral.",
        "A", "I", "SBI-VIRAL", 2022
    ),

    # ══════════════════════════════════════════════════════════════════
    # EXANTEMAS VIRAIS
    # ══════════════════════════════════════════════════════════════════
    (
        "Sarampo",
        "Vitamina A + Tratamento suportivo (sem antiviral específico)",
        None,
        "Vitamina A VO: crianças < 6 meses: 50.000 UI/dia × 2 dias; "
        "6-12 meses: 100.000 UI × 2 dias; ≥ 1 ano: 200.000 UI × 2 dias. "
        "Antipirético (paracetamol), hidratação, isolamento respiratório por 4 dias após início do exantema. "
        "Pneumonite: suporte respiratório, O₂, ATB apenas se co-infecção bacteriana confirmada. "
        "Encefalite por sarampo: corticoides, anticonvulsivantes.",
        "Autolimitado: 7-10 dias",
        "Vitamina A reduz mortalidade em crianças desnutridas em até 50% (evidência A). "
        "Sem antiviral específico aprovado. Vacinação com SCR/SCRV (2 doses) previne > 97% dos casos. "
        "A cobertura vacinal mínima de 95% é necessária para eliminar o sarampo.",
        "Imunoglobulina IM — profilaxia pós-exposição em gestantes, imunossuprimidos e < 6 meses dentro de 6 dias",
        "Não se aplica — sem antivirais",
        "ISOLAMENTO OBRIGATÓRIO por gotícula E aerossol por 4 dias após exantema. "
        "Notificação imediata. Investigação de contatos e vacinação de bloqueio em ≤ 72h da exposição. "
        "Surtos em 2018-2020 no Brasil por queda da cobertura vacinal.",
        "A", "I", "SVS-SARAMPO", 2022
    ),
    (
        "Rubéola (adquirida e congênita)",
        "Tratamento suportivo (sem antiviral específico)",
        None,
        "Rubéola adquirida: sintomático (paracetamol, repouso). "
        "Isolamento por gotícula por 7 dias após início do exantema. "
        "Síndrome da Rubéola Congênita (SRC): sem tratamento específico — "
        "equipe multidisciplinar para surdez (AASI/implante coclear), catarata (cirurgia precoce), "
        "cardiopatia (correção cirúrgica), acompanhamento neurossensorial.",
        "Autolimitada: 3-5 dias / SRC: suporte por anos",
        "Não existe antiviral específico. A vacinação com SCR (2 doses) foi responsável pela eliminação "
        "da rubéola endêmica no Brasil (certificada em 2009). "
        "Rubéola em gestante < 12 semanas tem 90% de risco de SRC.",
        "Não há alternativa antiviral",
        "Não se aplica",
        "Rubéola em gestante: notificação imediata; aconselhamento sobre risco fetal; "
        "não há indicação de imunoglobulina após exposição (sem eficácia preventiva para SRC). "
        "Monitorar ultrassonografia e exame do RN ao nascimento.",
        "A", "I", "SVS-SARAMPO", 2022
    ),
    (
        "Caxumba / Parotidite Epidêmica",
        "Tratamento suportivo (sem antiviral específico)",
        None,
        "Analgesia: paracetamol ou ibuprofeno; compressas frias na parótida; dieta macia, líquidos. "
        "Orquite: repouso no leito, suporte escrotal, analgesia intensa (pode necessitar opioides); "
        "corticoides orais × 5 dias para reduzir edema (controversial). "
        "Meningite asséptica: analgesia, hidratação, autolimitada.",
        "Parotidite: 7-10 dias",
        "Sem antiviral específico. Vacinação com SCR (2 doses) tem eficácia de ~88% para caxumba. "
        "3ª dose em surtos em adolescentes/adultos jovens com 2 doses aumenta proteção.",
        "Não há alternativa antiviral",
        "Não se aplica",
        "Isolamento domiciliar por 5 dias após início da parotidite. "
        "Orquite bilateral pode causar infertilidade masculina — encaminhar andrologia para seguimento. "
        "Em surtos universitários: notificar e considerar 3ª dose de SCR.",
        "A", "I", "SVS-SARAMPO", 2022
    ),

    # ══════════════════════════════════════════════════════════════════
    # GASTRENTERITE VIRAL
    # ══════════════════════════════════════════════════════════════════
    (
        "Rotavirose (diarreia por Rotavírus)",
        "Reidratação oral (SRO) — sem antiviral específico",
        None,
        "SRO OMS (250 mL água + 20g glicose + 3,5g NaCl + 1,5g KCl + 2,9g citrato tri-sódico) "
        "OU soluções industrializadas. Desidratação grave: Ringer Lactato IV 100 mL/kg em 3-4h. "
        "Manutenção nutricional: continuar amamentação; não suspender dieta por mais de 4h. "
        "Zinco VO: crianças 6 meses-5 anos: 20 mg/dia × 10-14 dias (reduz duração e recorrência).",
        "Autolimitada: 3-8 dias",
        "Reidratação oral é o tratamento que salva vidas — reduz mortalidade em > 90%. "
        "Vacina oral Rotarix (2 doses: 2 e 4 meses) disponível no SUS desde 2006 reduz hospitalizações em ~80%. "
        "Sem antiviral específico.",
        "Não há alternativa antiviral",
        "Não se aplica",
        "Sinais de desidratação grave em lactentes: olhos encovados, choro sem lágrimas, mucosas secas, "
        "turgor cutâneo diminuído, fontanela deprimida — internar para hidratação IV. "
        "Antidiarreicos (loperamida) são CONTRAINDICADOS em crianças < 2 anos.",
        "A", "I", "SBI-VIRAL", 2022
    ),
    (
        "Norovirose (diarreia e vômito por Norovírus)",
        "Reidratação oral (SRO) — sem antiviral específico",
        None,
        "SRO VO para casos leves-moderados; IV se vômitos intratáveis ou desidratação grave. "
        "Ondansetrona 0,15 mg/kg (máx 8 mg) VO/IM para controle dos vômitos. "
        "Isolamento de contato (luvas + avental) obrigatório em ambiente hospitalar — altamente contagioso. "
        "Lavagem de mãos com água e sabão (álcool gel tem eficácia limitada contra Norovírus).",
        "Autolimitada: 12-72h (maioria)",
        "Sem antiviral específico. Norovírus é resistente à maioria dos desinfetantes comuns — "
        "hipoclorito de sódio > 1000 ppm é necessário para descontaminação ambiental. "
        "Nitazoxanida (off-label) mostrou algum benefício em estudos pequenos — sem uso rotineiro.",
        "Não há alternativa antiviral",
        "Não se aplica",
        "Controle de surtos hospitalares: coorte de pacientes infectados, uso de EPIs de contato, "
        "hipoclorito para descontaminação de superfícies, restricionar visitas. "
        "Idosos e imunossuprimidos: formas mais prolongadas e graves.",
        "A", "I", "SBI-VIRAL", 2022
    ),

    # ══════════════════════════════════════════════════════════════════
    # ZOONOSES VIRAIS
    # ══════════════════════════════════════════════════════════════════
    (
        "Raiva (raiva humana transmitida por cão, morcego ou animais silvestres)",
        "Profilaxia Pós-Exposição (PEP) — sem tratamento curativo estabelecido após início dos sintomas",
        None,
        "PEP (PREVENÇÃO — única intervenção eficaz): "
        "1) Limpeza imediata e exaustiva da ferida com água corrente + sabão + antisséptico por 15 min. "
        "2) Vacina antirrábica: 4 doses IM nos dias 0, 3, 7, 14 (esquema ESSEN) — via SUS (CRIE). "
        "3) Imunoglobulina antirrábica humana (IGHAB) 20 UI/kg: toda a dose na ferida; excesso IM — "
        "indicada em exposições graves (mordedura em cabeça/pescoço/mão, arranhadura profunda, mucosa). "
        "APÓS INÍCIO DOS SINTOMAS: suporte paliativo em UTI (sedação, analgesia, cuidados humanizados). "
        "Protocolo Milwaukee: sem eficácia comprovada — não recomendado fora de contexto experimental.",
        "PEP: 14 dias / Raiva estabelecida: paliativo",
        "Raiva é 100% fatal após início dos sintomas. A PEP iniciada imediatamente após a exposição "
        "tem eficácia próxima de 100%. No Brasil, morcegos hematófagos (Desmodus rotundus) são o principal "
        "reservatório — qualquer contato deve ser avaliado para PEP.",
        "Não há alternativa terapêutica curativa após início dos sintomas",
        "Não se aplica — prevenção é a única estratégia eficaz",
        "Notificação imediata de caso suspeito de raiva humana. "
        "Vacinação pré-exposição para profissionais de risco (veterinários, biólogos, espeleólogos, "
        "trabalhadores em laboratório): 3 doses e reforços conforme titulação. "
        "Captura e observação do animal agressor por 10 dias (cão/gato domésticos) — se saudável, não vacinar.",
        "A", "I", "SVS-RAIVA", 2022
    ),
    (
        "Hantavirose (Síndrome Cardiopulmonar por Hantavírus — SCPH)",
        "Tratamento suportivo intensivo em UTI (sem antiviral específico eficaz)",
        None,
        "UTI OBRIGATÓRIA: monitorização hemodinâmica invasiva, manejo cuidadoso de fluidos "
        "(evitar sobrecarga — agrava edema pulmonar), ventilação mecânica protetora (volume corrente 6 mL/kg, "
        "PEEP adequada) em IRA hipoxêmica. "
        "Choque refratário: ECMO veno-arterial (VA-ECMO) — técnica com maior sobrevida documentada no Brasil. "
        "Suporte renal se IRA: diálise contínua preferencialmente.",
        "UTI: 1-4 semanas (sobreviventes)",
        "ECMO tem melhores resultados para SCPH do que o suporte convencional — mortalidade reduzida de 50% para ~25% "
        "em centros experientes. Ribavirina IV foi usada sem evidência de benefício em SCPH (diferente de Hantavírus "
        "Pulmonar do Velho Mundo, onde pode ter algum papel). "
        "Reconhecimento e transferência precoce para centro com ECMO são fundamentais.",
        "Não há alternativa antiviral eficaz para SCPH",
        "Não se aplica",
        "FASE CARDIOPULMONAR: piora súbita em 24-48h — não aguardar intubação eletiva para transferir para CTI com ECMO. "
        "Prevenção: evitar contato com roedores e excretas; ventilar ambientes fechados; uso de máscara N95 ao "
        "limpar áreas com presença de roedores. "
        "Notificação imediata.",
        "A", "II", "SVS-HANTA", 2022
    ),

    # ══════════════════════════════════════════════════════════════════
    # IST VIRAIS
    # ══════════════════════════════════════════════════════════════════
    (
        "Infecção pelo HPV (verrugas genitais e lesões precursoras)",
        "Tratamento das lesões + Vacinação profilática (sem antiviral sistêmico)",
        None,
        "Condilomas acuminados (verrugas genitais): "
        "Podofilotoxina 0,5% solução: aplicar 2x/dia × 3 dias, intervalo 4 dias, até 4 ciclos (autoaplicar). "
        "Imiquimode 5% creme: aplicar 3x/semana × até 16 semanas (imunomodulador tópico). "
        "Ácido tricloroacético 80-90% (ATA): aplicado pelo médico 1x/semana × 6 semanas. "
        "Crioterapia, eletrocauterização ou laser CO₂: para lesões resistentes ou extensas. "
        "NIC 2/3 (lesões precursoras do colo): exérese do colo (LEEP) ou conização.",
        "Variável conforme modalidade de tratamento (semanas a meses)",
        "Sem antiviral sistêmico que cure a infecção pelo HPV. O sistema imune do hospedeiro elimina o vírus "
        "em 1-2 anos na maioria dos casos. "
        "Vacina HPV quadrivalente/nonavalente profilática (previne infecção nova — não trata infecção existente): "
        "meninas 9-14 anos e meninos 11-14 anos no calendário SUS. "
        "PVHIV: vacinação até 45 anos (risco aumentado de HPV persistente).",
        "Sinecatequinas 15% (Polyphenon E) — alternativa tópica para condilomas",
        "Não se aplica — sem antivirais sistêmicos eficazes",
        "Rastreamento de câncer cervical: Papanicolaou a partir dos 25 anos (a cada 3 anos se normal × 2). "
        "Teste molecular de HPV alto risco: a partir dos 25-30 anos em centros com acesso. "
        "PVHIV: Pap a partir da primeira relação sexual e a cada 6-12 meses.",
        "A", "I", "SVS-HPV", 2022
    ),

    # ══════════════════════════════════════════════════════════════════
    # INFECÇÕES NEUROLÓGICAS VIRAIS
    # ══════════════════════════════════════════════════════════════════
    (
        "Encefalite Herpética (HSV-1)",
        "Aciclovir (ACV)",
        None,
        "Aciclovir IV 10 mg/kg 8/8h × 14-21 dias — EMERGÊNCIA NEUROLÓGICA. "
        "INICIAR IMEDIATAMENTE na suspeita clínica — não aguardar PCR ou RNM. "
        "Suporte: anticonvulsivantes (levetiracetam ou fenitoína) se crises, corticoides controversos "
        "(usar apenas se edema cerebral significativo).",
        "14-21 dias IV",
        "Encefalite herpética sem aciclovir tem mortalidade de 70% e sequelas graves nos sobreviventes. "
        "Com aciclovir IV precoce: mortalidade reduzida para ~20% e melhores desfechos neurológicos. "
        "PCR para HSV no LCR: sensibilidade 98%, especificidade 94% — confirmatório, mas não atrasar início. "
        "RNM cranioencefálica: hipersinal em T2 no lobo temporal é clássico.",
        "Foscarnet IV — HSV resistente ao aciclovir (raro, apenas em imunossuprimidos)",
        "Não se aplica em imunocompetentes",
        "Após 21 dias IV: considerar manutenção com valaciclovir VO × 3-6 meses para prevenção de recorrência. "
        "LCR após tratamento: repetir PCR para HSV apenas se deterioração clínica. "
        "Reabilitação neurológica multidisciplinar para sequelas (memória, linguagem, comportamento).",
        "A", "I", "SBI-VIRAL", 2022
    ),
    (
        "Poliomielite (pólio)",
        "Tratamento suportivo e reabilitação (sem antiviral curativo)",
        None,
        "Fase aguda (meningite asséptica / paralítica): repouso, analgesia, monitoramento respiratório. "
        "Insuficiência respiratória (paralisia bulbar ou dos músculos respiratórios): "
        "ventilação mecânica imediata. "
        "Reabilitação: fisioterapia motora intensiva para preservar e recuperar função muscular; "
        "órteses e adaptações de acessibilidade; cirurgias ortopédicas em selecionados.",
        "Suporte agudo + reabilitação por anos",
        "Não existe antiviral específico para poliovírus. A paralisia flácida estabelecida é irreversível. "
        "Vacinação é a única intervenção eficaz — Brasil certificado livre de poliovírus selvagem desde 1994. "
        "Risco de reintrodução por importação de países não erradicados (Paquistão, Afeganistão).",
        "Não há alternativa antiviral",
        "Não se aplica",
        "VIGILÂNCIA ATIVA DA PARALISIA FLÁCIDA AGUDA (PFA) é obrigatória — toda criança < 15 anos com PFA "
        "deve ser notificada como caso suspeito de pólio até exclusão laboratorial. "
        "Cobertura vacinal mínima de 95% com VOP+VIP essencial para manutenção da erradicação.",
        "A", "I", "SVS-POLIO", 2022
    ),

    # ══════════════════════════════════════════════════════════════════
    # TRATAMENTOS SUPORTIVOS — SEM ANTIVIRAL ESPECÍFICO
    # ══════════════════════════════════════════════════════════════════
    (
        "Febre do Nilo Ocidental",
        "Tratamento suportivo",
        None,
        "Hidratação, analgesia (Dipirona 500–1000 mg VO/IV 6/6h ou Paracetamol 500–750 mg VO 6/6h), "
        "antieméticos se necessário. Forma neuroinvasiva: UTI com suporte respiratório e controle de edema cerebral.",
        "Até resolução clínica",
        "Não existe antiviral aprovado para WNV. O tratamento é exclusivamente suportivo. "
        "A maioria dos casos (80%) é assintomática; apenas 1% evolui para doença neuroinvasiva grave.",
        "Não se aplica",
        "Imunoglobulina hiperimune (uso compassivo em neuroinvasiva grave — sem evidência robusta)",
        "Doença de notificação compulsória no Brasil. Transmitida por Culex mosquitoes — "
        "casos importados e autóctones registrados nas regiões Sul e Sudeste.",
        "B", "III", "SVS-DENGUE", 2022
    ),
    (
        "Doença Mão-Pé-Boca",
        "Tratamento suportivo",
        None,
        "Hidratação oral rigorosa (risco de desidratação por odinofagia), analgesia com Paracetamol "
        "15 mg/kg VO 6/6h (crianças) ou Ibuprofeno 10 mg/kg VO 8/8h. Higiene oral com clorexidina tópica.",
        "7–10 dias (autolimitada)",
        "Enterovírus 71 e Coxsackievírus A16 não têm antiviral específico aprovado. "
        "A doença é autolimitada na maioria dos casos. EV71 tem maior risco de complicações neurológicas.",
        "Não se aplica",
        "Não há alternativa antiviral aprovada",
        "ATENÇÃO: EV71 pode causar encefalite, edema pulmonar neurogênico e miocardite — "
        "sinais de alarme: febre persistente > 3 dias, vômitos, letargia, convulsões → hospitalização imediata.",
        "A", "III", "SBI-VIRAL", 2022
    ),
    (
        "Meningite Viral",
        "Tratamento suportivo",
        None,
        "Hidratação IV (SF 0,9% ou SG5%), analgesia (Dipirona IV), repouso em quarto escurecido. "
        "Aciclovir 10 mg/kg IV 8/8h apenas se suspeita de HSV confirmada por PCR LCR.",
        "5–7 dias (autolimitada) / 14–21 dias se HSV",
        "Meningite viral por enterovírus é autolimitada — antibiótico e antiviral não indicados empiricamente. "
        "Aciclovir coberto apenas após confirmação de HSV no LCR por PCR.",
        "Aciclovir empírico se LCR atípico com suspeita de HSV antes do resultado de PCR",
        "Não se aplica para enterovírus",
        "Punção lombar essencial para diagnóstico diferencial com meningite bacteriana. "
        "Meningite viral: glicose normal, proteína moderada, pleocitose linfocitária.",
        "A", "II", "SBI-VIRAL", 2022
    ),
    (
        "Infecção por Adenovírus Respiratório",
        "Tratamento suportivo",
        None,
        "Hidratação, antitérmicos (Paracetamol 15 mg/kg/dose VO 6/6h), broncodilatadores se broncoespasmo. "
        "Cidofovir IV apenas em imunossuprimidos graves com adenovirose disseminada.",
        "7–14 dias (autolimitada na imunocompetente)",
        "Não há antiviral aprovado para adenovírus respiratório em imunocompetentes. "
        "Cidofovir tem uso compassivo em transplantados com adenovirose grave.",
        "Não se aplica para imunocompetentes",
        "Cidofovir 5 mg/kg IV semanal em imunossuprimidos graves (nefrotóxico — pré-hidratação obrigatória)",
        "Adenovírus é causa importante de pneumonia em lactentes e crianças < 5 anos. "
        "Epidemias em creches e quartéis militares são frequentes.",
        "B", "III", "SBI-VIRAL", 2022
    ),

    # ══════════════════════════════════════════════════════════════════
    # INFECÇÕES CONGÊNITAS E PERINATAIS
    # ══════════════════════════════════════════════════════════════════
    (
        "CMV Congênito",
        "Valganciclovir",
        None,
        "Valganciclovir 16 mg/kg VO 12/12h × 6 meses (neonatos sintomáticos com acometimento do SNC). "
        "Ganciclovir 6 mg/kg IV 12/12h × 6 semanas se via oral inviável.",
        "6 meses",
        "Único tratamento que melhora desfechos auditivos e neurodesenvolvimento em CMV congênito sintomático "
        "com acometimento do SNC. PCDT MS 2022 recomenda valganciclovir oral como padrão.",
        "Ganciclovir IV — impossibilidade de administração oral",
        "Não há alternativa estabelecida de eficácia equivalente",
        "TRIAGEM AUDITIVA OBRIGATÓRIA (BERA/ABR). Monitorar neutropenia (principal toxicidade). "
        "CMV congênito assintomático: acompanhamento audiológico sem tratamento antiviral imediato.",
        "A", "I", "PCDT-HIV", 2022
    ),
    (
        "Hepatite B Perinatal",
        "Tenofovir disoproxil fumarato (TDF)",
        None,
        "Gestante com carga viral HBV > 200.000 UI/mL no 3º trimestre: TDF 300 mg VO 24/24h até 4–12 semanas pós-parto. "
        "RN: Imunoglobulina anti-hepatite B (HBIG) 0,5 mL IM + Vacina HBV nas primeiras 12h de vida.",
        "Profilaxia gestante: 3º trim. até pós-parto / RN: dose única HBIG + esquema vacinal completo",
        "Profilaxia combinada HBIG + vacina reduz transmissão vertical para < 5% mesmo em mães HBeAg+. "
        "TDF no 3º trimestre reduz carga viral materna e risco de breakthrough no RN.",
        "Lamivudina 150 mg VO 24/24h (gestante com contraindicação a TDF — menos recomendado, risco de resistência)",
        "Não se aplica — profilaxia, não tratamento de infecção estabelecida",
        "Amamentação NÃO é contraindicada se RN recebeu HBIG + vacina. "
        "HBsAg do RN deve ser testado aos 9–18 meses para confirmar eficácia da profilaxia.",
        "A", "I", "PCDT-HEPB", 2022
    ),
    (
        "Herpes Neonatal",
        "Aciclovir",
        None,
        "Aciclovir 20 mg/kg IV 8/8h × 14 dias (doença localizada pele/olho/boca) ou "
        "× 21 dias (SNC/disseminada). Seguido por supressão oral: Aciclovir 300 mg/m² VO 8/8h × 6 meses.",
        "14–21 dias IV + 6 meses VO supressão",
        "Herpes neonatal tem mortalidade > 80% sem tratamento. Aciclovir IV em dose alta reduz mortalidade "
        "da doença disseminada para ~30% e melhora desfechos neurológicos.",
        "Não há alternativa — aciclovir é o único aprovado e eficaz para herpes neonatal",
        "Não se aplica",
        "EMERGÊNCIA NEONATAL. Colher culturas e PCR antes de iniciar mas NÃO atrasar tratamento. "
        "Cesárea indicada se lesões herpéticas ativas no momento do parto.",
        "A", "I", "PCDT-HIV", 2022
    ),
    (
        "Síndrome Congênita do Zika",
        "Tratamento suportivo e reabilitação",
        None,
        "Não há antiviral específico. Tratamento multidisciplinar: fisioterapia motora, fonoaudiologia, "
        "terapia ocupacional, neurologia pediátrica (anticonvulsivantes se epilepsia), oftalmologia.",
        "Acompanhamento longitudinal (anos)",
        "Não existe antiviral aprovado para Zika. O foco é reabilitação neuromotora precoce e controle "
        "de comorbidades (epilepsia, espasticidade, déficit visual e auditivo).",
        "Não se aplica",
        "Não se aplica",
        "PCDT MS 2016/2022 garante acesso gratuito à rede de reabilitação pelo SUS. "
        "Microcefalia grave associada a pior prognóstico neurológico. "
        "Benefício Prestação Continuada (BPC) pode ser solicitado para crianças afetadas.",
        "A", "III", "SVS-DENGUE", 2022
    ),

    # ══════════════════════════════════════════════════════════════════
    # RETROVIROSES — HTLV
    # ══════════════════════════════════════════════════════════════════
    (
        "HTLV — Leucemia/Linfoma de Células T do Adulto (ATLL)",
        "Zidovudina (AZT)",
        "+ Interferon-alfa",
        "Forma indolente/smoldering: AZT 600 mg/dia VO + IFN-alfa 3–5 MUI SC 3×/semana. "
        "Forma agressiva (aguda/linfomatosa): quimioterapia CHOP ou CHOP-like ± mogamulizumabe (anti-CCR4).",
        "Contínuo (formas indolentes) / 6–8 ciclos (quimioterapia)",
        "AZT + IFN-alfa melhora sobrevida nas formas indolentes do ATLL. Formas agressivas têm prognóstico "
        "reservado — mediana de sobrevida < 12 meses mesmo com quimioterapia.",
        "IFN-alfa isolado se intolerância a AZT",
        "Mogamulizumabe (anti-CCR4) — aprovado para ATLL refratário (disponibilidade limitada no Brasil)",
        "HTLV-1 é endêmico na Bahia, Pernambuco e Maranhão. Triagem em bancos de sangue obrigatória no Brasil. "
        "Transplante alogênico de medula pode ser curativo em casos selecionados.",
        "B", "II", "SVS-HTLV", 2022
    ),
    (
        "HTLV — Mielopatia Associada ao HTLV / Paraparesia Espástica Tropical (HAM/TSP)",
        "Metilprednisolona",
        None,
        "Fase aguda/surto: Metilprednisolona 1 g IV/dia × 3–5 dias. Manutenção: Prednisona 40–60 mg/dia VO "
        "com redução gradual. Fisioterapia motora intensiva contínua.",
        "Pulsoterapia × 3–5 dias + manutenção crônica com fisioterapia",
        "HAM/TSP é progressiva — não há cura. Corticosteroides reduzem inflamação medular e podem "
        "estabilizar a progressão. Fisioterapia é essencial para manutenção da função motora.",
        "Pentoxifilina 400 mg VO 8/8h — alternativa imunomoduladora com menor toxicidade",
        "Não há alternativa antiviral eficaz estabelecida",
        "Bexiga neurogênica é complicação frequente — urologia e cateterismo intermitente. "
        "Espasticidade: baclofeno 5–20 mg VO 8/8h. Suporte psicológico e social essenciais.",
        "B", "II", "SVS-HTLV", 2022
    ),
]

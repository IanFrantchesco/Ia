"""
Patologias virais mais importantes no Brasil com CID-10.
Fonte base: GVS-MS 5ª ed. 2022, PCDTs do Ministério da Saúde, SINAN, SBI, SBMT, OPAS/PAHO.

Cada entrada:
(nome, cid10, categoria_nome, descricao, notificacao_compulsoria, tipo_notificacao,
 prevalencia_br, mortalidade_br, populacao_risco, fonte_sigla)
"""

CATEGORIAS_VIRAIS = [
    # (nome, sistema)
    ("Arboviroses", "Sistêmico / múltiplos órgãos — transmitidas por artrópodes"),
    ("Hepatites Virais", "Fígado / aparelho digestivo"),
    ("Retroviroses", "Sistema imunológico / sistêmico"),
    ("Herpesviroses", "Tegumento / sistema nervoso / sistêmico"),
    ("Infecções Respiratórias Virais", "Aparelho respiratório"),
    ("Exantemas Virais", "Tegumento / sistêmico"),
    ("Gastrenterite Viral", "Aparelho digestivo"),
    ("Infecções Neurológicas Virais", "Sistema nervoso central"),
    ("Infecções Virais Sexualmente Transmissíveis (IST Virais)", "Sistema reprodutor / mucosas"),
    ("Zoonoses Virais", "Sistêmico — origem em reservatório animal"),
    ("Infecções Virais Congênitas e Perinatais", "Neonatal / materno-infantil"),
    ("Infecções Virais em Imunocomprometidos", "Sistêmico — oportunistas em imunossuprimidos"),
]

PATOLOGIAS_VIRAIS = [

    # ── ARBOVIROSES ───────────────────────────────────────────────────────────
    (
        "Dengue (formas leve, moderada e grave)",
        "A90 / A91", "Arboviroses",
        "Principal arbovirose do Brasil; transmitida pelo Aedes aegypti; 4 sorotipos (DENV 1-4); "
        "epidemias anuais com pico no verão; forma grave inclui dengue com sinais de alarme e dengue grave (choque, hemorragia).",
        True, "imediata",
        "muito_alta", "media",
        "Toda a população em áreas urbanas tropicais; crianças e idosos têm maior risco de forma grave; "
        "reinfecção por sorotipo diferente aumenta risco de dengue grave",
        "SVS-DENGUE"
    ),
    (
        "Zika (infecção aguda e síndrome congênita)",
        "A928", "Arboviroses",
        "Arbovirose pelo Aedes aegypti com epidemia no Brasil em 2015-2016; causa microcefalia e síndrome "
        "congênita do Zika em fetos; transmissão sexual documentada; curso clínico leve na maioria dos adultos.",
        True, "imediata",
        "alta", "baixa",
        "Gestantes (risco de síndrome congênita); adultos em áreas de circulação do Aedes aegypti; "
        "parceiros sexuais de viajantes provenientes de zonas endêmicas",
        "SVS-DENGUE"
    ),
    (
        "Chikungunya (aguda e crônica)",
        "A920", "Arboviroses",
        "Arbovirose pelo Aedes aegypti/albopictus com epidemias anuais no Brasil; artralgia severa e persistente "
        "é marca da doença; forma crônica incapacitante dura meses a anos; alta carga de morbidade.",
        True, "imediata",
        "muito_alta", "baixa",
        "Idosos com maior risco de forma crônica incapacitante; toda a população em zonas endêmicas; "
        "recém-nascidos de mães virêmicas podem ter forma grave",
        "SVS-DENGUE"
    ),
    (
        "Febre Amarela (silvestre e urbana)",
        "A95", "Arboviroses",
        "Arbovirose pelo Flavivirus transmitida por Haemagogus/Sabethes (silvestre) ou Aedes (urbana); "
        "endêmica no Brasil; surtos com alta letalidade (20-50% nas formas ictero-hemorrágicas graves); "
        "vacina de dose única altamente eficaz.",
        True, "imediata",
        "baixa", "alta",
        "Não vacinados em áreas endêmicas ou de expansão (Centro-Oeste, Norte, parte do Sudeste/Sul); "
        "trabalhadores rurais, ecoturistas, aventureiros",
        "SVS-FEBAMARELA"
    ),
    (
        "Febre do Nilo Ocidental (casos importados e autóctones)",
        "A922", "Arboviroses",
        "Flavivirose transmitida por Culex; casos importados crescentes no Brasil; vírus detectado em aves "
        "e mosquitos no território nacional; formas neurológicas graves (meningite, encefalite) em idosos e imunossuprimidos.",
        True, "imediata",
        "rara", "media",
        "Viajantes; idosos; imunossuprimidos; áreas com presença de aves e Culex confirmados",
        "OPAS-BR"
    ),

    # ── HEPATITES VIRAIS ──────────────────────────────────────────────────────
    (
        "Hepatite A",
        "B15", "Hepatites Virais",
        "Hepatite aguda autolimitada por HAV; transmissão fecal-oral; epidemia em áreas sem saneamento; "
        "vakina disponível no SUS; formas fulminantes raras mas graves; sem cronicidade.",
        True, "semanal",
        "alta", "baixa",
        "Crianças < 10 anos em áreas de saneamento precário; adultos não vacinados; "
        "hepatopatas crônicos têm risco de hepatite fulminante",
        "SVS-HEPAT-AE"
    ),
    (
        "Hepatite B (aguda e crônica)",
        "B16 / B18.1", "Hepatites Virais",
        "Infecção pelo HBV com potencial de cronificação (90% nos neonatos, 5% em adultos); "
        "3 milhões de portadores crônicos no Brasil; cirrose e hepatocarcinoma são complicações tardias; "
        "vacinação universal previne infecção.",
        True, "semanal",
        "alta", "media",
        "Profissionais de saúde; parceiros sexuais de portadores; usuários de drogas injetáveis; "
        "recém-nascidos de mães HBsAg positivas; populações com acesso limitado à vacinação",
        "PCDT-HEPB"
    ),
    (
        "Hepatite C (aguda e crônica)",
        "B17.1 / B18.2", "Hepatites Virais",
        "Infecção pelo HCV de transmissão predominantemente parenteral; ~1,5 milhões de portadores crônicos no Brasil; "
        "maioria assintomática por décadas; cirrose e CHC são desfechos sem tratamento; DAAs curam >97% dos casos.",
        True, "semanal",
        "alta", "media",
        "Ex-usuários de drogas injetáveis (principal no Brasil); transfusões antes de 1993; "
        "profissionais de saúde; prisioneiros; HSH; parceiros de portadores",
        "PCDT-HEPC"
    ),
    (
        "Hepatite D (Coinfecção e Superinfecção por HDV)",
        "B17.0", "Hepatites Virais",
        "Vírus defectivo que requer HBV para replicação; coinfecção (HBV+HDV simultâneos) ou superinfecção "
        "(HDV em portador de HBV) causam formas mais graves; prevalência concentrada na Amazônia brasileira.",
        True, "semanal",
        "media", "alta",
        "Portadores crônicos de HBV não vacinados contra Hepatite B (vacinação contra HBV previne HDV); "
        "usuários de drogas injetáveis; populações indígenas amazônicas",
        "PCDT-HEPB"
    ),
    (
        "Hepatite E",
        "B17.2", "Hepatites Virais",
        "Hepatite aguda autolimitada por HEV; transmissão fecal-oral e zoonótica (suínos/javalis); "
        "sem cronicidade em imunocompetentes; formas fulminantes em gestantes (mortalidade 20-25%); "
        "casos esporádicos no Brasil.",
        True, "semanal",
        "baixa", "media",
        "Gestantes (risco de forma fulminante); consumidores de carne de porco/javali malcozida; "
        "viajantes para Ásia e África; imunossuprimidos (cronicidade possível)",
        "SVS-HEPAT-AE"
    ),

    # ── RETROVIROSES ──────────────────────────────────────────────────────────
    (
        "HIV/AIDS (infecção aguda, crônica e AIDS estabelecida)",
        "B20–B24", "Retroviroses",
        "Infecção pelo HIV-1/2 com ~657.000 pessoas vivendo com HIV no Brasil (2022); "
        "ARV garante carga viral indetectável e qualidade de vida normal; AIDS = CD4 < 200 ou doença definidora; "
        "epidemia concentrada mas em expansão em jovens e regiões Norte/Nordeste.",
        True, "imediata",
        "alta", "media",
        "HSH, mulheres trans, profissionais do sexo, usuários de drogas, populações privadas de liberdade; "
        "adultos jovens 20-34 anos são o principal grupo de novas infecções no Brasil",
        "PCDT-HIV"
    ),
    (
        "Infecção pelo HTLV-1 (portador e formas clínicas)",
        "B33.3", "Retroviroses",
        "Brasil tem a maior coorte de portadores de HTLV-1 do mundo (~800.000); Bahia é o estado de maior prevalência; "
        "2-5% desenvolvem leucemia/linfoma de células T do adulto (ATLL) ou mielopatia/paraparesia espástica tropical (TSP/HAM); "
        "sem tratamento curativo; manejo das complicações.",
        True, "semanal",
        "media", "media",
        "Descendentes de africanos; populações da Bahia e Norte do Brasil; "
        "parceiros sexuais e filhos amamentados de portadores; usuários de drogas injetáveis; "
        "receptores de transfusão de sangue não triado",
        "SVS-HTLV"
    ),

    # ── HERPESVIROSES ─────────────────────────────────────────────────────────
    (
        "Herpes Simples (orolabial, genital e neonatal)",
        "B00", "Herpesviroses",
        "Infecção pelo HSV-1 (orolabial) e HSV-2 (genital principalmente); latência no gânglio nervoso com reativações; "
        "herpes neonatal tem alta mortalidade sem aciclovir; encefalite herpética é emergência neurológica; "
        "prevalência muito alta na população brasileira.",
        False, None,
        "muito_alta", "baixa",
        "Adultos sexualmente ativos (HSV-2); crianças e adultos (HSV-1); "
        "imunossuprimidos têm reativações graves; recém-nascidos de mães com herpes genital ativo no parto",
        "SBI-VIRAL"
    ),
    (
        "Varicela (catapora)",
        "B01", "Herpesviroses",
        "Primo-infecção pelo VZV; altamente contagiosa; benigna em crianças imunocompetentes; "
        "formas graves em adultos, gestantes e imunossuprimidos; pneumonite varicela é complicação grave; "
        "vacinação universal no calendário SUS desde 2013.",
        True, "semanal",
        "alta", "baixa",
        "Crianças não vacinadas; adultos sem imunidade (susceptíveis); "
        "gestantes (risco de varicela neonatal e síndrome varicela congênita); "
        "imunossuprimidos (formas graves e disseminadas)",
        "SVS-VARICELA"
    ),
    (
        "Herpes Zoster (cobreiro)",
        "B02", "Herpesviroses",
        "Reativação do VZV em gânglios nervosos; maior incidência em idosos e imunossuprimidos; "
        "nevralgia pós-herpética é complicação incapacitante frequente; vacina disponível para > 50 anos (SUS em imunossuprimidos); "
        "zoster oftálmico pode causar cegueira.",
        False, None,
        "alta", "baixa",
        "Idosos > 60 anos (principal grupo); imunossuprimidos; PVHIV com CD4 baixo; "
        "pacientes em corticoterapia crônica ou quimioterapia",
        "SVS-VARICELA"
    ),
    (
        "Citomegalovirose (CMV) em Imunocomprometidos",
        "B25", "Herpesviroses",
        "CMV causa infecção latente ubíqua (soroprevalência > 70% no Brasil); "
        "doença por CMV em imunossuprimidos: retinite, colite, pneumonite, encefalite; "
        "principal causa de cegueira infecciosa em PVHIV com CD4 < 50 células; "
        "complicação grave em transplantados.",
        False, None,
        "alta", "media",
        "PVHIV com CD4 < 50 células/mm³; transplantados de órgãos sólidos ou células tronco; "
        "recém-nascidos de mães primoinfeção durante gravidez (CMV congênito)",
        "SBI-VIRAL"
    ),
    (
        "Mononucleose Infecciosa (EBV)",
        "B27.0", "Herpesviroses",
        "Primo-infecção sintomática pelo EBV em adolescentes e adultos jovens; tríade febre-linfadenopatia-faringite exsudativa; "
        "linfocitose com linfócitos atípicos; esplenomegalia com risco de ruptura; "
        "associado a linfomas (Burkitt, Hodgkin) em contextos específicos.",
        False, None,
        "alta", "baixa",
        "Adolescentes e adultos jovens 15-25 anos; países em desenvolvimento têm infecção precoce geralmente assintomática; "
        "imunossuprimidos podem ter reativação grave com síndrome linfoproliferativa",
        "SBI-VIRAL"
    ),

    # ── INFECÇÕES RESPIRATÓRIAS VIRAIS ─────────────────────────────────────────
    (
        "Influenza (gripe sazonal e pandêmica)",
        "J10 / J11", "Infecções Respiratórias Virais",
        "Infecção pelo Influenza A/B; epidemias sazonais com pico entre abril e setembro no Brasil; "
        "principais complicações: pneumonia viral primária e pneumonia bacteriana secundária; "
        "grupos de risco têm vacinação anual gratuita no SUS.",
        True, "semanal",
        "muito_alta", "media",
        "Idosos > 60 anos; gestantes; crianças < 5 anos; portadores de doença crônica; "
        "profissionais de saúde; indígenas; populações privadas de liberdade",
        "PCDT-INFLUENZA"
    ),
    (
        "COVID-19 (infecção aguda, grave e síndrome pós-COVID)",
        "U07.1", "Infecções Respiratórias Virais",
        "Infecção pelo SARS-CoV-2; pandemia 2020-2023 com > 700.000 mortes no Brasil; "
        "espectro desde infecção assintomática até SDRA e morte; síndrome pós-COVID afeta 10-30% dos casos; "
        "vacinação com alta eficácia contra formas graves.",
        True, "imediata",
        "muito_alta", "alta",
        "Idosos > 60 anos; imunossuprimidos; diabéticos; obesos; cardiopatas; "
        "não vacinados têm risco muito maior de hospitalização e morte",
        "PCDT-COVID19"
    ),
    (
        "Infecção pelo Vírus Sincicial Respiratório (VSR/RSV)",
        "J21.0 / J12.1", "Infecções Respiratórias Virais",
        "Principal causa de bronquiolite e pneumonia viral em lactentes < 2 anos no Brasil; "
        "epidemias anuais outono-inverno; formas graves em prematuros e cardiopatas congênitos; "
        "anticorpo monoclonal (nirsevimabe) disponível para alto risco.",
        False, None,
        "muito_alta", "media",
        "Lactentes < 6 meses (maior gravidade); prematuros; cardiopatas congênitos com shunt; "
        "adultos imunossuprimidos e idosos com doença crônica também afetados",
        "SBI-VIRAL"
    ),
    (
        "Infecção por Adenovírus Respiratório",
        "J12.0 / B34.0", "Infecções Respiratórias Virais",
        "Adenovírus causam infecções do trato respiratório, conjuntivite e gastrenterite; "
        "surtos em ambientes fechados (quartéis, creches, escolas); tipos 4, 7 e 14 causam pneumonia grave; "
        "imunossuprimidos têm doença disseminada.",
        False, None,
        "alta", "baixa",
        "Crianças < 5 anos; recrutas militares; ambientes com aglomeração; "
        "transplantados de células tronco (alta morbidade e mortalidade)",
        "SBI-VIRAL"
    ),

    # ── EXANTEMAS VIRAIS ──────────────────────────────────────────────────────
    (
        "Sarampo",
        "B05", "Exantemas Virais",
        "Morbillivírus altamente contagioso; reemergência global e brasileira 2018-2020; "
        "pneumonia e encefalite são complicações graves; mortalidade elevada em desnutridos e < 5 anos; "
        "vacinação (SCR) altamente eficaz; cobertura vacinal abaixo de 95% favorece surtos.",
        True, "imediata",
        "baixa", "media",
        "Crianças não vacinadas ou com vacinação incompleta; adultos jovens sem segunda dose; "
        "comunidades com baixa cobertura vacinal; viajantes a áreas com circulação ativa",
        "SVS-SARAMPO"
    ),
    (
        "Rubéola (adquirida e congênita)",
        "B06 / P35.0", "Exantemas Virais",
        "Togavírus com exantema autolimitado; principal risco é a Síndrome da Rubéola Congênita (SRC): "
        "surdez, catarata, cardiopatia, microcefalia; Brasil alcançou eliminação da rubéola endêmica em 2009; "
        "vigilância ativa de casos suspeitos é essencial.",
        True, "imediata",
        "rara", "media",
        "Gestantes susceptíveis no 1º trimestre têm risco de SRC; "
        "criancas e adultos jovens não vacinados em surtos importados",
        "SVS-SARAMPO"
    ),
    (
        "Caxumba / Parotidite Epidêmica",
        "B26", "Exantemas Virais",
        "Paramixovírus causador de parotidite bilateral; complicações incluem orquite (20% nos adultos), "
        "ooforite, meningite asséptica e pancreatite; surtos em adolescentes e adultos jovens com 2 doses de vacina "
        "(eficácia da 3ª dose debatida).",
        True, "semanal",
        "media", "baixa",
        "Adolescentes e adultos jovens em ambientes fechados (universidades, quartéis); "
        "indivíduos vacinados com 2 doses ainda têm risco em surtos (eficácia ~88%)",
        "SVS-SARAMPO"
    ),
    (
        "Doença Mão-Pé-Boca (Enterovírus 71 e Coxsackievírus A16)",
        "B08.4", "Exantemas Virais",
        "Infecção por EV-A71 e CVA16 com vesículas na boca, mãos e pés em crianças; "
        "EV-A71 pode causar complicações neurológicas graves (encefalite de tronco cerebral, meningite, edema pulmonar); "
        "surtos anuais em creches e escolas brasileiras.",
        False, None,
        "muito_alta", "baixa",
        "Crianças < 5 anos em creches e escolas; adultos podem ter infecção leve; "
        "EV-A71 em crianças < 3 anos tem maior risco de forma grave neurológica",
        "SBI-VIRAL"
    ),

    # ── GASTRENTERITE VIRAL ───────────────────────────────────────────────────
    (
        "Rotavirose (diarreia por Rotavírus)",
        "A08.0", "Gastrenterite Viral",
        "Principal causa de hospitalização por diarreia em crianças < 5 anos no Brasil; "
        "vacina oral disponível no SUS (Rotarix) desde 2006 com impacto significativo na redução de hospitalizações; "
        "epidemias outono-inverno.",
        False, None,
        "muito_alta", "media",
        "Crianças < 2 anos (maior gravidade e mortalidade); lactentes < 3 meses podem ter formas graves; "
        "adultos imunossuprimidos e idosos também afetados",
        "SBI-VIRAL"
    ),
    (
        "Norovirose (diarreia e vômito por Norovírus)",
        "A08.1", "Gastrenterite Viral",
        "Norovírus causa a maioria dos surtos de gastroenterite alimentar em todas as faixas etárias no Brasil; "
        "transmissão fecal-oral e por aerossóis de vômito; altamente contagioso (dose infectante < 100 vírions); "
        "sem tratamento específico.",
        False, None,
        "muito_alta", "baixa",
        "Toda a população; surtos em cruzeiros, hotéis, restaurantes, hospitais e creches; "
        "idosos e imunossuprimidos têm formas mais prolongadas",
        "SBI-VIRAL"
    ),

    # ── INFECÇÕES NEUROLÓGICAS VIRAIS ─────────────────────────────────────────
    (
        "Raiva (raiva humana transmitida por cão, morcego ou animais silvestres)",
        "A82", "Zoonoses Virais",
        "Encefalite viral invariavelmente fatal após início dos sintomas; transmissão por mordida/arranhadura; "
        "no Brasil: morcegos hematófagos são principal reservatório atual; "
        "profilaxia pós-exposição (PEP) altamente eficaz se iniciada imediatamente.",
        True, "imediata",
        "rara", "alta",
        "Populações rurais em contato com morcegos hematófagos (Norte, Centro-Oeste, Nordeste); "
        "crianças que brincam em áreas com cães errantes; trabalhadores rurais; veterinários sem vacinação",
        "SVS-RAIVA"
    ),
    (
        "Encefalite Herpética (HSV-1)",
        "B00.4", "Infecções Neurológicas Virais",
        "Encefalite por HSV-1 é a encefalite viral esporádica mais grave e tratável; "
        "alta mortalidade (70%) sem aciclovir; sequelas neurológicas graves em sobreviventes não tratados; "
        "PCR em LCR é o gold-standard diagnóstico.",
        False, None,
        "baixa", "alta",
        "Adultos > 50 anos (primo-infecção) e adolescentes/adultos jovens (reativação); "
        "imunossuprimidos têm risco aumentado de HSV encefalite",
        "SBI-VIRAL"
    ),
    (
        "Meningite Viral (enterovírus e outros)",
        "A87", "Infecções Neurológicas Virais",
        "Enterovírus causam a maioria das meningites virais no Brasil; curso geralmente benigno e autolimitado; "
        "diagnóstico diferencial com meningite bacteriana é fundamental; "
        "EBV, CMV, HSV-2 e HIV também causam meningite.",
        False, None,
        "alta", "baixa",
        "Crianças e adultos jovens em surtos de enterovírus; "
        "imunossuprimidos têm risco de formas graves por CMV, HSV, HIV",
        "SBI-VIRAL"
    ),

    # ── IST VIRAIS ────────────────────────────────────────────────────────────
    (
        "Infecção pelo HPV (verrugas genitais e lesões precursoras)",
        "B97.7 / A63.0", "Infecções Virais Sexualmente Transmissíveis (IST Virais)",
        "HPV é a IST mais prevalente no Brasil e no mundo; genótipos 6/11 causam condilomas; "
        "16/18 causam 70% dos cânceres cervicais; vacinação quadrivalente/nonavalente no SUS para meninas e meninos; "
        "rastreamento por Papanicolaou e teste molecular.",
        False, None,
        "muito_alta", "media",
        "Adultos sexualmente ativos; jovens 15-25 anos são o principal grupo de infecção nova; "
        "imunossuprimidos (HIV+) têm maior persistência viral e maior risco de progressão neoplásica",
        "SVS-HPV"
    ),

    # ── ZOONOSES VIRAIS ───────────────────────────────────────────────────────
    (
        "Hantavirose (Síndrome Cardiopulmonar por Hantavírus — SCPH)",
        "B33.4", "Zoonoses Virais",
        "Hantavírus brasileiros (Araraquara, Juquitiba) causam SCPH com letalidade de 39-50%; "
        "inalação de aerossóis de excretas de roedores silvestres; sem transmissão humano-humano no Brasil; "
        "pico em trabalhadores rurais durante colheita.",
        True, "imediata",
        "baixa", "alta",
        "Trabalhadores rurais; agricultores; pessoas em contato com roedores silvestres; "
        "moradores de áreas rurais do Sul, Sudeste, Centro-Oeste e Nordeste do Brasil",
        "SVS-HANTA"
    ),

    # ── INFECÇÕES CONGÊNITAS ──────────────────────────────────────────────────
    (
        "Síndrome Congênita do Zika Vírus",
        "Q02 / A928", "Infecções Virais Congênitas e Perinatais",
        "Microcefalia e malformações neurológicas por infecção pelo Zika em gestantes; "
        "epidemia 2015-2016 deixou milhares de crianças afetadas no Brasil; "
        "síndrome inclui microcefalia, calcificações cerebrais, artrogripose e lesões oculares.",
        True, "imediata",
        "media", "media",
        "Fetos e recém-nascidos de mães infectadas pelo Zika durante gestação, especialmente 1º trimestre; "
        "maior incidência nas regiões Norte e Nordeste do Brasil",
        "SVS-DENGUE"
    ),
    (
        "CMV Congênito",
        "P35.1", "Infecções Virais Congênitas e Perinatais",
        "Principal causa infecciosa de surdez neurossensorial congênita no Brasil; "
        "primoinfeção materna durante gestação é mais grave; 10% dos neonatos infectados têm sintomas ao nascimento; "
        "valganciclovir melhora desfecho auditivo e neurológico quando iniciado cedo.",
        False, None,
        "alta", "media",
        "Recém-nascidos de mães com primoinfeção durante gestação; "
        "maior risco em filhos de mães soronegativas para CMV no início da gravidez",
        "SBI-VIRAL"
    ),
    (
        "Hepatite B Perinatal (transmissão vertical)",
        "P35.3", "Infecções Virais Congênitas e Perinatais",
        "Transmissão vertical do HBV no periparto; 90% das crianças infectadas cronificam sem profilaxia; "
        "imunoglobulina anti-HBs + vacina ao nascimento previne em > 95%; "
        "rastreamento de HBsAg em gestantes é mandatório no pré-natal do SUS.",
        True, "semanal",
        "media", "media",
        "Recém-nascidos de mães HBsAg positivas; especialmente mães com HBeAg positivo ou carga viral elevada",
        "PCDT-HEPB"
    ),
    (
        "Herpes Neonatal (HSV)",
        "P35.2", "Infecções Virais Congênitas e Perinatais",
        "Infecção pelo HSV no periparto ou pós-natal precoce; três formas clínicas: cutâneo-mucosa (mais leve), "
        "SNC e disseminada (mortalidade > 80% sem tratamento); aciclovir IV é o tratamento de emergência.",
        False, None,
        "baixa", "alta",
        "Recém-nascidos de mães com herpes genital ativo (primo-infecção materna tem maior risco); "
        "neonatos prematuros; parto vaginal com lesões herpéticas ativas",
        "SBI-VIRAL"
    ),

    # ── IMUNOCOMPROMETIDOS ────────────────────────────────────────────────────
    (
        "Poliomielite (pólio)",
        "A80", "Infecções Neurológicas Virais",
        "Enterovirose com paralisia flácida assimétrica; Brasil certificado como livre de pólio desde 1994; "
        "vírus da vacina oral (VDPV) pode raramente causar paralisia; vigilância da Paralisia Flácida Aguda (PFA) é essencial; "
        "risco de reintrodução pelo poliovírus selvagem de outros países.",
        True, "imediata",
        "rara", "media",
        "Crianças não vacinadas ou com vacinação incompleta; "
        "comunidades com cobertura vacinal < 95%; imunodeficientes podem eliminar VDPV por meses",
        "SVS-POLIO"
    ),
    (
        "HTLV — Leucemia/Linfoma de Células T do Adulto (ATLL)",
        "C91.5", "Retroviroses",
        "Complicação neoplásica maligna em 2-5% dos portadores de HTLV-1 após latência de décadas; "
        "prognóstico muito ruim nas formas aguda e linfomatosa; prevalente na Bahia e Norte do Brasil; "
        "quimioterapia convencional com resposta limitada.",
        True, "semanal",
        "baixa", "alta",
        "Portadores de HTLV-1 por décadas; maior risco nos que adquiriram via amamentação na infância; "
        "japoneses-brasileiros têm incidência elevada",
        "SVS-HTLV"
    ),
    (
        "HTLV — Mielopatia Associada ao HTLV / Paraparesia Espástica Tropical (HAM/TSP)",
        "G04.1", "Retroviroses",
        "Doença desmielinizante progressiva da medula espinal em portadores de HTLV-1; "
        "paraparesia espástica progressiva, bexiga neurogênica, disfunção sexual; "
        "sem tratamento curativo; corticoides e interferon usados para modular a doença.",
        True, "semanal",
        "baixa", "media",
        "Portadores de HTLV-1 com alta carga proviral; maior risco em mulheres e nos que adquiriram via sexual ou transfusional",
        "SVS-HTLV"
    ),
]

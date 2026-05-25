"""
150 patologias crônicas / não-infecciosas mais relevantes no Brasil com CID-10.
Fonte base: PCDTs do Ministério da Saúde, Sociedades Brasileiras de Especialidade,
DATASUS/SVS, INCA, CFM.

Cada entrada:
(nome, cid10, categoria_nome, descricao, notificacao_compulsoria, tipo_notificacao,
 prevalencia_br, mortalidade_br, populacao_risco, fonte_sigla)
"""

CATEGORIAS_CRONICAS = [
    # (nome, sistema)
    ("Cardiovascular",                      "Aparelho circulatório — doenças do coração e vasos"),
    ("Endócrino e Metabólico",              "Sistema endócrino e metabólico — disfunções hormonais e metabólicas"),
    ("Oncológico",                          "Neoplasias — tumores malignos"),
    ("Saúde Mental e Neurológico",          "Sistema nervoso central e saúde mental"),
    ("Respiratório Crônico",                "Aparelho respiratório — doenças obstrutivas e intersticiais"),
    ("Gastrointestinal e Hepático",         "Aparelho digestivo e fígado — doenças crônicas"),
    ("Renal e Urológico",                   "Aparelho geniturinário — doenças crônicas"),
    ("Musculoesquelético e Reumatológico",  "Sistema musculoesquelético — doenças inflamatórias e degenerativas"),
    ("Dermatológico Crônico",               "Tegumento — dermatoses crônicas inflamatórias"),
    ("Hematológico",                        "Sistema hematopoiético e coagulação"),
    ("Ginecológico e Obstétrico",           "Aparelho reprodutor feminino e gestação"),
]

PATOLOGIAS_CRONICAS = [

    # ── CARDIOVASCULAR (20) ────────────────────────────────────────────────────
    (
        "Hipertensão Arterial Sistêmica — Estágio 1",
        "I10", "Cardiovascular",
        "HAS com PA sistólica 140-159 mmHg e/ou diastólica 90-99 mmHg; afeta ~36% dos adultos brasileiros; "
        "principal fator de risco modificável para doença cardiovascular e renal no Brasil.",
        False, None, "muito_alta", "baixa",
        "Adultos acima de 40 anos, sedentários, obesos, história familiar, negros",
        "SBC-HAS"
    ),
    (
        "Hipertensão Arterial Sistêmica — Estágio 2-3 / Resistente",
        "I10", "Cardiovascular",
        "HAS com PA ≥ 160/100 mmHg ou refratária ao uso de ≥ 3 anti-hipertensivos em dose ótima incluindo "
        "diurético; associada a lesão de órgão-alvo e alto risco cardiovascular.",
        False, None, "alta", "media",
        "Hipertensos com controle inadequado, obesos, portadores de síndrome metabólica, DRC",
        "PCDT-HAS"
    ),
    (
        "Insuficiência Cardíaca com Fração de Ejeção Reduzida (ICFEr)",
        "I50.0", "Cardiovascular",
        "IC sistólica com FE < 40%; etiologias mais comuns no Brasil: doença de Chagas, cardiopatia isquêmica "
        "e hipertensiva; quadriplay farmacológico (IECA/BRA/ARNI + BB + ARM + SGLT2i) como pilar do tratamento.",
        False, None, "alta", "alta",
        "Cardiopatas chagásicos, pós-infarto, hipertensos descompensados, homens > 60 anos",
        "SBC-ICC"
    ),
    (
        "Insuficiência Cardíaca com Fração de Ejeção Preservada (ICFEp)",
        "I50.0", "Cardiovascular",
        "IC diastólica com FE ≥ 50%; predomina em mulheres idosas, hipertensas e obesas; diagnóstico exige "
        "critérios funcionais e biomarcadores (BNP/NT-proBNP); SGLT2i com evidência crescente.",
        False, None, "alta", "media",
        "Mulheres idosas, hipertensas, obesas, diabéticas, fibrilação atrial concomitante",
        "SBC-ICC"
    ),
    (
        "Fibrilação Atrial — Controle de Frequência",
        "I48", "Cardiovascular",
        "Arritmia sustentada mais comum no Brasil; estratégia de controle de frequência com betabloqueador "
        "ou digoxina; anticoagulação conforme escore CHA₂DS₂-VASc; rastreio de FA silenciosa em idosos.",
        False, None, "alta", "media",
        "Idosos > 65 anos, hipertensos, cardiopatas, portadores de valvopatia reumática",
        "SBC-HAS"
    ),
    (
        "Fibrilação Atrial — Anticoagulação / Controle de Ritmo",
        "I48", "Cardiovascular",
        "Estratégia de controle de ritmo com cardioversão elétrica ou farmacológica e/ou ablação por "
        "cateter; anticoagulação obrigatória antes e após cardioversão; NOACs preferidos sobre warfarina.",
        False, None, "alta", "media",
        "Pacientes jovens com FA de início recente, FA paroxística sintomática, sem valvopatia reumática",
        "SBC-SCA"
    ),
    (
        "Síndrome Coronariana Aguda — NSTEMI / Angina Instável",
        "I20.0", "Cardiovascular",
        "Ruptura de placa aterosclerótica com oclusão subtotal; estratificação por escore GRACE/TIMI; "
        "abordagem invasiva precoce em alto risco; dupla antiagregação por 12 meses.",
        False, None, "alta", "alta",
        "Homens > 45 anos, mulheres > 55 anos, tabagistas, diabéticos, hipertensos, dislipidêmicos",
        "SBC-SCA"
    ),
    (
        "Síndrome Coronariana Aguda — STEMI (Infarto Agudo do Miocárdio com Supradesnivelamento de ST)",
        "I21", "Cardiovascular",
        "Oclusão coronariana aguda total; tempo porta-balão ≤ 90 min; ICP primária como padrão-ouro; "
        "fibrinólise quando ICP indisponível em < 120 min; dupla antiagregação por 12 meses.",
        False, None, "media", "alta",
        "Tabagistas, diabéticos, hipertensos, dislipidêmicos, história familiar de DAC prematura",
        "SBC-SCA"
    ),
    (
        "Doença Arterial Coronariana Crônica (Angina Estável)",
        "I25.1", "Cardiovascular",
        "Aterosclerose coronariana obstrutiva com demanda isquêmica; tratamento clínico otimizado com "
        "betabloqueador, nitrato, IECA, estatina de alta intensidade e AAS; revascularização conforme anatomia.",
        False, None, "alta", "media",
        "Pós-IAM, diabéticos, hipertensos com lesão de órgão-alvo, dislipidêmicos",
        "SBC-SCA"
    ),
    (
        "Acidente Vascular Cerebral Isquêmico Agudo",
        "I63", "Cardiovascular",
        "Oclusão arterial cerebral; tratamento trombolítico (alteplase) até 4,5h ou trombectomia mecânica "
        "até 24h em casos selecionados; prevenção secundária com antiagregação/anticoagulação e estatina.",
        False, None, "alta", "alta",
        "Hipertensos, fibrilação atrial, diabéticos, idosos, fumantes, portadores de estenose carotídea",
        "SBC-HAS"
    ),
    (
        "Acidente Vascular Cerebral Hemorrágico Intracerebral",
        "I61", "Cardiovascular",
        "Hemorragia intraparenquimatosa; principal causa: HAS mal controlada; manejo do hematoma, "
        "controle pressórico intensivo (< 140 mmHg) e reversão de anticoagulação quando aplicável.",
        False, None, "media", "alta",
        "Hipertensos graves, usuários de anticoagulantes, angiopatia amiloide cerebral, idosos",
        "SBC-HAS"
    ),
    (
        "Ataque Isquêmico Transitório (AIT)",
        "G45.9", "Cardiovascular",
        "Déficit neurológico focal transitório sem infarto estabelecido; alto risco de AVC nos primeiros "
        "dias (escore ABCD²); investigação urgente com neuroimagem e ecocardiograma; prevenção secundária imediata.",
        False, None, "media", "baixa",
        "Idosos, hipertensos, fibrilação atrial não anticoagulada, estenose carotídea > 50%",
        "SBC-HAS"
    ),
    (
        "Trombose Venosa Profunda (TVP)",
        "I80.2", "Cardiovascular",
        "Trombose de veias profundas, predominantemente membros inferiores; diagnóstico por ultrassonografia "
        "Doppler; anticoagulação com HBPM ou NOAC por 3-6 meses; profilaxia em pacientes de risco.",
        False, None, "media", "media",
        "Pós-operatório, imobilização prolongada, neoplasias, trombofilias, gestantes, obesos",
        "SBC-SCA"
    ),
    (
        "Tromboembolia Pulmonar (TEP)",
        "I26", "Cardiovascular",
        "Obstrução da vasculatura pulmonar por trombo; estratificação por escores PESI/Genebra; "
        "anticoagulação imediata com HBPM ou NOAC; trombólise sistêmica em TEP maciço com choque.",
        False, None, "media", "alta",
        "TVP prévia, neoplasias, cirurgias ortopédicas, imobilização, FA, gestantes, obesidade",
        "SBC-SCA"
    ),
    (
        "Doença Arterial Periférica (DAP)",
        "I73.9", "Cardiovascular",
        "Aterosclerose obstrutiva de membros inferiores; claudicação intermitente até isquemia crítica; "
        "ITB < 0,9 confirma diagnóstico; antiagregação, estatina e revascularização conforme gravidade.",
        False, None, "media", "media",
        "Tabagistas, diabéticos, hipertensos, dislipidêmicos, doença renal crônica",
        "SBC-SCA"
    ),
    (
        "Hipertensão Pulmonar Arterial Idiopática",
        "I27.0", "Cardiovascular",
        "Doença vascular pulmonar progressiva com hipertensão pré-capilar (mPAP > 20 mmHg, RVP > 3 UW); "
        "tratamento específico com PDE5i, ERA e/ou prostaciclinas; candidatos a transplante pulmonar.",
        False, None, "rara", "alta",
        "Mulheres jovens (20-40 anos), portadores de doenças do tecido conjuntivo, HIV, esquistossomose",
        "SBC-ICC"
    ),
    (
        "Pericardite Aguda (Não Infecciosa / Autoimune)",
        "I30.9", "Cardiovascular",
        "Inflamação do pericárdio de etiologia autoimune ou idiopática; tratamento com AINE + colchicina "
        "por 3 meses; corticoide reservado para casos refratários; risco de pericardite recorrente.",
        False, None, "baixa", "baixa",
        "Adultos jovens, portadores de LES, artrite reumatoide, pós-infarto (síndrome de Dressler)",
        "SBC-ICC"
    ),
    (
        "Insuficiência Cardíaca — Descompensação Aguda (ICAD)",
        "I50.9", "Cardiovascular",
        "Piora aguda dos sintomas de IC exigindo hospitalização; diuréticos EV, vasodilatadores e "
        "inotrópicos conforme perfil hemodinâmico; otimização da terapia de base na alta.",
        False, None, "alta", "alta",
        "IC crônica com comorbidades (FA, pneumonia, não adesão ao tratamento, isquemia aguda)",
        "SBC-ICC"
    ),
    (
        "Síndrome Coronariana Crônica — Prevenção Secundária Pós-IAM",
        "I25.2", "Cardiovascular",
        "Manejo de longo prazo após IAM com AAS, IECA/BRA, betabloqueador e estatina de alta intensidade; "
        "dupla antiagregação conforme stent implantado; reabilitação cardíaca supervisionada.",
        False, None, "alta", "baixa",
        "Sobreviventes de IAM, pós-ICP ou CRM, pacientes com DAC multiarterial documentada",
        "SBC-SCA"
    ),
    (
        "Endocardite Não Bacteriana (Marântica / Libman-Sacks)",
        "I33.0", "Cardiovascular",
        "Vegetações estéreis associadas a neoplasias avançadas (marântica) ou LES/síndrome antifosfolípide "
        "(Libman-Sacks); risco alto de embolização sistêmica; anticoagulação e tratamento da doença de base.",
        False, None, "rara", "alta",
        "Neoplasias avançadas (mucossecretoras), LES ativo, síndrome antifosfolípide",
        "SBC-ICC"
    ),

    # ── ENDÓCRINO E METABÓLICO (15) ────────────────────────────────────────────
    (
        "Diabetes Mellitus Tipo 2 (Sem Complicações)",
        "E11.9", "Endócrino e Metabólico",
        "DM2 sem lesão de órgão-alvo; manejo com mudança de estilo de vida e metformina como fármaco "
        "inicial; metas de HbA1c individualizadas; rastreio anual de complicações microvasculares.",
        False, None, "muito_alta", "baixa",
        "Adultos > 45 anos, obesos, sedentários, história familiar, síndrome metabólica, GDM prévia",
        "SBD-DM2"
    ),
    (
        "Diabetes Mellitus Tipo 2 com Complicações / Alto Risco Cardiovascular",
        "E11.6", "Endócrino e Metabólico",
        "DM2 com DCV estabelecida, DRC ou insuficiência cardíaca; SGLT2i e/ou GLP-1 RA com benefício "
        "cardiovascular-renal demonstrado; controle intensivo de PA, lipídeos e microalbuminúria.",
        False, None, "muito_alta", "media",
        "DM2 com DAC, IC, DRC G3-G4, nefropatia, retinopatia, neuropatia periférica",
        "PCDT-DM2"
    ),
    (
        "Diabetes Mellitus Tipo 1",
        "E10.9", "Endócrino e Metabólico",
        "DM autoimune com destruição de células β; insulinoterapia basal-bolus obrigatória; monitorização "
        "contínua de glicose (MCG); risco de cetoacidose diabética; manejo multidisciplinar.",
        False, None, "media", "baixa",
        "Crianças, adolescentes e adultos jovens; pico de incidência entre 10-14 anos no Brasil",
        "PCDT-DM1"
    ),
    (
        "Obesidade Grau I-II (IMC 30-39,9 kg/m²)",
        "E66.0", "Endócrino e Metabólico",
        "Excesso de adiposidade com risco cardiometabólico aumentado; intervenção comportamental intensiva, "
        "farmacoterapia (orlistate, liraglutida, semaglutida) e rastreio de comorbidades.",
        False, None, "muito_alta", "baixa",
        "Adultos > 30 anos, sedentários, dieta hipercalórica, predisposição genética, uso de medicamentos",
        "PCDT-OBESIDADE"
    ),
    (
        "Obesidade Grau III / Obesidade Mórbida (IMC ≥ 40 kg/m²)",
        "E66.01", "Endócrino e Metabólico",
        "Obesidade grave com múltiplas comorbidades; elegibilidade para cirurgia bariátrica (bypass gástrico "
        "em Y de Roux ou sleeve gastrectomia); farmacoterapia de alta intensidade como ponte ou alternativa.",
        False, None, "alta", "media",
        "Adultos com IMC ≥ 40 ou ≥ 35 com comorbidades graves; histórico de fracasso no tratamento clínico",
        "PCDT-OBESIDADE"
    ),
    (
        "Dislipidemia — Hipercolesterolemia Familiar / Alto Risco Cardiovascular",
        "E78.0", "Endócrino e Metabólico",
        "LDL-c > 190 mg/dL (HF) ou risco cardiovascular alto/muito alto; estatina de alta intensidade "
        "(rosuvastatina/atorvastatina); ezetimiba e inibidores de PCSK9 em metas não atingidas.",
        False, None, "muito_alta", "media",
        "Adultos com DCV estabelecida, DM, HAS com LOA, HF heterozigótica ou homozigótica",
        "PCDT-DISLIPID"
    ),
    (
        "Hipertrigliceridemia Grave (≥ 500 mg/dL)",
        "E78.1", "Endócrino e Metabólico",
        "Triglicerídeos muito elevados com risco de pancreatite aguda; fibratos como tratamento de escolha; "
        "restrição severa de gorduras, álcool e carboidratos simples; tratar causas secundárias.",
        False, None, "media", "media",
        "DM2 descontrolado, alcoolismo, hipotireoidismo, insuficiência renal, uso de corticoide/estrogênio",
        "SBC-DISLIPID"
    ),
    (
        "Hipotireoidismo Primário (Adulto)",
        "E03.9", "Endócrino e Metabólico",
        "Deficiência de hormônios tireoidianos; causa mais comum no Brasil: tireoidite de Hashimoto; "
        "reposição com levotiroxina sódica em dose individualizável; TSH como marcador de controle.",
        False, None, "muito_alta", "baixa",
        "Mulheres > 40 anos, pós-tireoidectomia, pós-radioiodo, história familiar de doença tireoidiana",
        "PCDT-HIPOTIREOID"
    ),
    (
        "Hipertireoidismo / Doença de Graves",
        "E05.0", "Endócrino e Metabólico",
        "Hiperatividade tireoidiana autoimune com TSH suprimido; tratamento com metimazol ou propiltiouracil; "
        "radioiodoterapia ou cirurgia nos casos refratários ou com bócio volumoso.",
        False, None, "alta", "baixa",
        "Mulheres jovens (20-40 anos), história familiar de doença autoimune tireoidiana",
        "PCDT-HIPOTIREOID"
    ),
    (
        "Síndrome de Cushing (Hipercortisolismo Endógeno)",
        "E24.0", "Endócrino e Metabólico",
        "Exposição crônica excessiva ao cortisol; causa mais comum: adenoma hipofisário produtor de ACTH "
        "(Doença de Cushing); cirurgia transesfenoidal de escolha; adrenalectomia bilateral quando necessário.",
        False, None, "rara", "media",
        "Adultos jovens (20-40 anos), mulheres 3x mais afetadas, portadores de tumores adrenais ou hipofisários",
        "CFM-SM"
    ),
    (
        "Insuficiência Adrenal Primária (Doença de Addison)",
        "E27.1", "Endócrino e Metabólico",
        "Destruição autoimune das adrenais com deficiência de cortisol e aldosterona; reposição com "
        "hidrocortisona + fludrocortisona; crise adrenal é emergência com risco de vida.",
        False, None, "rara", "alta",
        "Adultos jovens, doenças autoimunes associadas (tireoidite, DM1), tuberculose adrenal",
        "CFM-SM"
    ),
    (
        "Gota — Hiperuricemia Sintomática",
        "M10.0", "Endócrino e Metabólico",
        "Deposição de cristais de urato monossódico em articulações; alopurinol como uricostático de "
        "primeira linha; febuxostato em intolerantes; tratamento anti-inflamatório das crises agudas.",
        False, None, "alta", "baixa",
        "Homens > 40 anos, obesos, hipertensos, uso de diuréticos tiazídicos, insuficiência renal, alcoolismo",
        "SBR-AR"
    ),
    (
        "Síndrome Metabólica",
        "E88.81", "Endócrino e Metabólico",
        "Conjunto de adiposidade abdominal, dislipidemia aterogênica, HAS e hiperglicemia de jejum; "
        "fator de risco independente para DM2 e DCV; abordagem global com mudança de estilo de vida.",
        False, None, "muito_alta", "media",
        "Adultos obesos, sedentários, história familiar de DM2, síndrome dos ovários policísticos",
        "SBD-DM2"
    ),
    (
        "Diabetes Gestacional",
        "O24.4", "Endócrino e Metabólico",
        "Hiperglicemia diagnosticada pela primeira vez na gestação; rastreio com TOTG entre 24-28 semanas; "
        "dieta e exercício como primeira linha; insulina NPH + regular quando metas glicêmicas não atingidas.",
        False, None, "alta", "baixa",
        "Gestantes > 35 anos, obesas, história familiar de DM, GDM prévia, SOP",
        "SBD-DM2"
    ),
    (
        "Hiperparatireoidismo Primário",
        "E21.0", "Endócrino e Metabólico",
        "Hipersecreção autônoma de PTH por adenoma paratireoidiano (85% casos); hipercalcemia assintomática "
        "em >80% dos diagnósticos hodiernos; paratireoidectomia para casos sintomáticos ou com osteoporose.",
        False, None, "baixa", "baixa",
        "Mulheres pós-menopáusicas, idosos, história de neoplasia endócrina múltipla (NEM1)",
        "CFM-SM"
    ),

    # ── ONCOLÓGICO (20) ────────────────────────────────────────────────────────
    (
        "Câncer de Mama — Luminal (Hormônio-Positivo, HER2-Negativo)",
        "C50", "Oncológico",
        "Subtipo molecular mais prevalente (70% dos casos); hormonioterapia adjuvante por 5-10 anos "
        "(tamoxifeno ou inibidores de aromatase); CDK4/6 em doença metastática; rastreio por mamografia.",
        False, None, "alta", "alta",
        "Mulheres > 50 anos, menarca precoce, menopausa tardia, nuliparidade, HF de primeiro grau",
        "INCA-ONCOL"
    ),
    (
        "Câncer de Mama — HER2-Positivo",
        "C50", "Oncológico",
        "Subtipo com superexpressão de HER2 (~20% dos casos); trastuzumabe + pertuzumabe na neoadjuvância "
        "e adjuvância; T-DM1 ou T-DXd em doença residual pós-neoadjuvância; prognóstico melhorado com biológicos.",
        False, None, "alta", "alta",
        "Mulheres em todas as faixas etárias; mutações BRCA1/2 aumentam risco em subtipos agressivos",
        "INCA-ONCOL"
    ),
    (
        "Câncer de Mama — Triplo-Negativo",
        "C50", "Oncológico",
        "Ausência de RE, RP e HER2; alta taxa de resposta patológica completa à quimioterapia neoadjuvante; "
        "pembrolizumabe + quimioterapia em PD-L1 positivo; olaparibe em BRCA1/2-mutado metastático.",
        False, None, "media", "alta",
        "Mulheres jovens, negras, portadoras de BRCA1, diagnóstico geralmente tardio",
        "INCA-ONCOL"
    ),
    (
        "Câncer de Próstata — Localizado (Baixo/Intermediário Risco)",
        "C61", "Oncológico",
        "Adenocarcinoma acinar localizado; vigilância ativa para baixo risco; prostatectomia radical ou "
        "radioterapia com intenção curativa para intermediário; PSA + biópsia guiada por RM paramétrica.",
        False, None, "alta", "media",
        "Homens > 50 anos, negros (risco 2x), HF de primeiro grau, mutações BRCA2",
        "INCA-ONCOL"
    ),
    (
        "Câncer de Próstata — Metastático Hormônio-Sensível",
        "C61", "Oncológico",
        "Disseminação a distância ainda responsiva à supressão androgênica; ADT + darolutamida, apalutamida "
        "ou enzalutamida aumentam sobrevida global; docetaxel em alta carga metastática.",
        False, None, "media", "alta",
        "Homens > 65 anos com diagnóstico tardio; doença oligometastática ou poliméstática",
        "INCA-ONCOL"
    ),
    (
        "Câncer de Pulmão Não Pequenas Células (CPNPC) — Adenocarcinoma Avançado",
        "C34.1", "Oncológico",
        "Subtipo mais frequente de câncer de pulmão no Brasil; pesquisa de EGFR, ALK, ROS1, KRAS; "
        "terapia-alvo em mutações driver; pembrolizumabe em PD-L1 ≥ 50%; quimioterapia de combinação.",
        False, None, "alta", "alta",
        "Tabagistas > 20 maços-ano, ex-tabagistas, exposição a asbesto, radônio, poluição ambiental",
        "INCA-ONCOL"
    ),
    (
        "Câncer de Pulmão de Pequenas Células (CPPC)",
        "C34.9", "Oncológico",
        "Carcinoma neuroendócrino de alto grau com disseminação precoce; quimioterapia com etoposídeo + "
        "platina + atezolizumabe; resposta inicial alta mas recidiva frequente; radioterapia craniana profilática.",
        False, None, "media", "alta",
        "Tabagistas pesados (> 30 maços-ano); raramente em não-tabagistas",
        "INCA-ONCOL"
    ),
    (
        "Câncer Colorretal — Estágios I-III (Ressecável)",
        "C18.9", "Oncológico",
        "Segunda causa de morte por câncer no Brasil; rastreio com colonoscopia e pesquisa de sangue oculto "
        "nas fezes; quimioterapia adjuvante (FOLFOX) no estágio III; ressecção cirúrgica com margem oncológica.",
        False, None, "alta", "alta",
        "Adultos > 50 anos, polipose adenomatosa familiar, síndrome de Lynch, DII de longa data, obesidade",
        "INCA-ONCOL"
    ),
    (
        "Câncer Colorretal — Metastático",
        "C18.9", "Oncológico",
        "Doença avançada com metástases hepáticas e/ou pulmonares; FOLFOX/FOLFIRI + bevacizumabe ou "
        "cetuximabe (RAS selvagem); pembrolizumabe em dMMR/MSI-H; ressecção de metástases hepáticas quando possível.",
        False, None, "media", "alta",
        "Portadores de CCR localizado sem seguimento adequado; diagnóstico tardio em populações de baixa renda",
        "INCA-ONCOL"
    ),
    (
        "Câncer do Colo do Útero — Localmente Avançado (IIB-IVA)",
        "C53", "Oncológico",
        "Predominantemente por HPV 16/18; quimiorradioterapia concomitante com cisplatina como padrão-ouro; "
        "pembrolizumabe + quimioterapia em PD-L1+ metastático; vacinação HPV como prevenção primária.",
        False, None, "alta", "alta",
        "Mulheres de baixa renda sem rastreio adequado, início precoce de atividade sexual, tabagismo, HIV",
        "INCA-ONCOL"
    ),
    (
        "Câncer de Endométrio",
        "C54.1", "Oncológico",
        "Carcinoma endometrioide (tipo I) relacionado ao excesso estrogênico; estadiamento cirúrgico com "
        "histerectomia total; carcinomas de alto grau (tipo II) com comportamento agressivo; pembrolizumabe em dMMR.",
        False, None, "media", "media",
        "Mulheres obesas pós-menopáusicas, uso de tamoxifeno, SOP, diabetes, nuliparidade",
        "INCA-ONCOL"
    ),
    (
        "Câncer Gástrico — Localmente Avançado e Metastático",
        "C16.9", "Oncológico",
        "Alta mortalidade no Brasil; ressecção D2 para doença ressecável; quimioterapia perioperatória "
        "(FLOT); trastuzumabe + quimioterapia em HER2-positivo metastático; nivolumabe como manutenção.",
        False, None, "alta", "alta",
        "Homens > 60 anos, tabagistas, H. pylori crônico, dieta rica em sal/defumados, baixa ingesta de frutas",
        "INCA-ONCOL"
    ),
    (
        "Hepatocarcinoma (CHC) — Child-Pugh A/B",
        "C22.0", "Oncológico",
        "Neoplasia hepática primária em contexto de cirrose (VHB, VHC, NASH, álcool); ablação por "
        "radiofrequência ou TACE para intermediário; atezolizumabe + bevacizumabe em avançado Child A.",
        False, None, "media", "alta",
        "Cirróticos por VHC/VHB, NASH avançado, alcoolismo, portadores de hemocromatose hereditária",
        "INCA-ONCOL"
    ),
    (
        "Câncer de Pâncreas — Ressecável e Irressecável",
        "C25.9", "Oncológico",
        "Adenocarcinoma ductal com diagnóstico tardio; pancreatoduodenectomia (Whipple) nos ~20% ressecáveis; "
        "FOLFIRINOX ou gemcitabina + nab-paclitaxel em metastático; BRCA1/2 e PALB2 orientam manutenção.",
        False, None, "baixa", "alta",
        "Tabagistas, diabéticos de início recente, pancreatite crônica, HF, mutações BRCA2/PALB2",
        "INCA-ONCOL"
    ),
    (
        "Linfoma de Hodgkin Clássico",
        "C81.9", "Oncológico",
        "Neoplasia linfoide com distribuição bimodal (20-35 e > 65 anos); R-ABVD ou BEACOPP intensificado; "
        "PET-CT para avaliação interim e estadiamento; alta taxa de cura mesmo em doença avançada.",
        False, None, "baixa", "media",
        "Adultos jovens (pico 20-30 anos), EBV positivo em alguns casos, HIV/AIDS",
        "INCA-ONCOL"
    ),
    (
        "Linfoma Difuso de Grandes Células B (DLBCL)",
        "C83.3", "Oncológico",
        "Linfoma não-Hodgkin mais comum no Brasil; R-CHOP como esquema padrão; polatuzumabe vedotina + "
        "R-CHP em alto risco; CAR-T cell em segunda linha; estratificação por IPI e biologia molecular.",
        False, None, "baixa", "alta",
        "Adultos > 60 anos, imunossuprimidos, HIV, doenças autoimunes em tratamento com imunossupressores",
        "INCA-ONCOL"
    ),
    (
        "Leucemia Mieloide Aguda (LMA)",
        "C92.0", "Oncológico",
        "Leucemia aguda de pior prognóstico; quimioterapia de indução 7+3 (citarabina + daunorrubicina); "
        "venetoclax + azacitidina em idosos não aptos; transplante alogênico em risco intermediário/alto.",
        False, None, "baixa", "alta",
        "Adultos > 60 anos, síndrome mielodisplásica prévia, exposição a benzeno, quimioterapia prévia",
        "INCA-ONCOL"
    ),
    (
        "Leucemia Linfoide Crônica (LLC) — Com Indicação de Tratamento",
        "C91.1", "Oncológico",
        "LLC sintomática (Binet B-C / Rai III-IV); ibrutinibe ou venetoclax + obinutuzumabe como primeira "
        "linha preferencial; fludarabina + ciclofosfamida + rituximabe em jovens com mutação IGHV.",
        False, None, "baixa", "media",
        "Adultos > 65 anos, sexo masculino, HF de LLC, exposição a herbicidas/pesticidas",
        "INCA-ONCOL"
    ),
    (
        "Leucemia Mieloide Crônica (LMC) — Fase Crônica",
        "C92.1", "Oncológico",
        "Definida pela fusão BCR-ABL1 (cromossomo Philadelphia); imatinibe, dasatinibe ou nilotinibe como "
        "inibidores de tirosina-quinase de primeira geração; resposta molecular profunda possibilita descontinuação.",
        False, None, "baixa", "media",
        "Adultos de meia-idade (30-60 anos), discreto predomínio masculino, sem fator causal definido na maioria",
        "INCA-ONCOL"
    ),
    (
        "Melanoma — Metastático / Alto Risco (Estágios III-IV)",
        "C43.9", "Oncológico",
        "Neoplasia de melanócitos com alta taxa de mutação; BRAF V600E em ~50% (vemurafenibe + cobimetinibe); "
        "imunoterapia com nivolumabe + ipilimumabe em BRAF selvagem; adjuvância no estágio III ressecado.",
        False, None, "baixa", "alta",
        "Fotótipos I-II, exposição solar intensa na infância, nevos displásicos múltiplos, HF de melanoma",
        "INCA-ONCOL"
    ),

    # ── SAÚDE MENTAL E NEUROLÓGICO (20) ────────────────────────────────────────
    (
        "Depressão Maior (Episódio Moderado a Grave)",
        "F32.1", "Saúde Mental e Neurológico",
        "Transtorno depressivo com humor deprimido, anedonia e comprometimento funcional por ≥ 2 semanas; "
        "ISRS/IRSN como primeira linha; psicoterapia (TCC); eletroconvulsoterapia em casos refratários graves.",
        False, None, "muito_alta", "media",
        "Mulheres 2x mais afetadas, adultos jovens (18-45 anos), desempregados, comorbidades médicas crônicas",
        "CFM-SM"
    ),
    (
        "Transtorno Depressivo Persistente (Distimia)",
        "F34.1", "Saúde Mental e Neurológico",
        "Depressão de baixa intensidade e longa duração (≥ 2 anos); ISRS como primeira linha combinado "
        "com psicoterapia cognitivo-comportamental; risco de depressão dupla com episódios maiores sobrepostos.",
        False, None, "alta", "baixa",
        "Adultos jovens, mulheres, pacientes com história de adversidade na infância",
        "CFM-SM"
    ),
    (
        "Transtorno de Ansiedade Generalizada (TAG)",
        "F41.1", "Saúde Mental e Neurológico",
        "Preocupação excessiva persistente com múltiplos domínios da vida por ≥ 6 meses; ISRS/IRSN + "
        "TCC; buspirona como alternativa; benzodiazepínicos apenas no curto prazo devido à dependência.",
        False, None, "muito_alta", "baixa",
        "Mulheres (2:1), adultos de 30-50 anos, comorbidades com depressão e fobia social",
        "CFM-SM"
    ),
    (
        "Transtorno do Pânico",
        "F41.0", "Saúde Mental e Neurológico",
        "Crises recorrentes de ansiedade intensa com sintomas autonômicos; ISRS + TCC com técnicas de "
        "exposição interoceptiva; clomipramina como alternativa; benzodiazepínico no início como ponte.",
        False, None, "alta", "baixa",
        "Adultos jovens (20-35 anos), mulheres, história de transtorno de ansiedade na infância",
        "CFM-SM"
    ),
    (
        "Transtorno Obsessivo-Compulsivo (TOC)",
        "F42", "Saúde Mental e Neurológico",
        "Obsessões e compulsões que consomem > 1h/dia e causam sofrimento; ISRS em doses altas + TCC "
        "com exposição e prevenção de resposta (EPR); clomipramina em refratários; TMS/neuroestimulação.",
        False, None, "media", "baixa",
        "Início na infância ou adolescência; adultos jovens; HF de TOC; síndrome de Tourette associada",
        "CFM-SM"
    ),
    (
        "Transtorno de Estresse Pós-Traumático (TEPT)",
        "F43.1", "Saúde Mental e Neurológico",
        "Reexperiência, evitação e hipervigilância após evento traumático; ISRS (sertralina/paroxetina) + "
        "psicoterapia focada no trauma (EMDR, CPT); prazosin para pesadelos; risco de cronificação.",
        False, None, "media", "baixa",
        "Sobreviventes de violência doméstica, acidentes graves, desastres, combatentes, vítimas de abuso",
        "CFM-SM"
    ),
    (
        "Transtorno Bipolar Tipo I",
        "F31.1", "Saúde Mental e Neurológico",
        "Episódios de mania franca com depressão; lítio ou valproato como estabilizadores de humor; "
        "olanzapina ou quetiapina na mania aguda; lamotrigina na manutenção anti-depressiva; alto risco de suicídio.",
        False, None, "media", "media",
        "Adultos jovens (início 20-30 anos), HF de transtorno bipolar, uso de substâncias psicoativas",
        "CFM-SM"
    ),
    (
        "Transtorno Bipolar Tipo II",
        "F31.8", "Saúde Mental e Neurológico",
        "Hipomania + depressão maior; lítio ou lamotrigina como primeira linha de manutenção; quetiapina "
        "em monoterapia eficaz para ambos os polos; maior risco de diagnóstico tardio como depressão unipolar.",
        False, None, "media", "baixa",
        "Adultos jovens, mulheres ligeiramente mais afetadas que o TB tipo I; comorbidade com ansiedade",
        "CFM-SM"
    ),
    (
        "Esquizofrenia — Fase Aguda e Manutenção",
        "F20.9", "Saúde Mental e Neurológico",
        "Psicose crônica com sintomas positivos, negativos e cognitivos; antipsicóticos de segunda geração "
        "como primeira linha; clozapina em esquizofrenia refratária; reabilitação psicossocial e suporte familiar.",
        False, None, "media", "media",
        "Adultos jovens (18-35 anos), HF de psicose, uso de cannabis na adolescência",
        "CFM-SM"
    ),
    (
        "TDAH — Transtorno do Déficit de Atenção e Hiperatividade (Adulto)",
        "F90.0", "Saúde Mental e Neurológico",
        "Desatenção e/ou hiperatividade-impulsividade prejudicando múltiplos domínios; metilfenidato ou "
        "lisdexanfetamina como primeira linha farmacológica; TCC voltada para habilidades de organização.",
        False, None, "alta", "baixa",
        "Crianças e adultos jovens; diagnóstico em adultos crescente; HF de TDAH, prematuridade",
        "CFM-SM"
    ),
    (
        "Transtorno por Uso de Álcool",
        "F10.2", "Saúde Mental e Neurológico",
        "Dependência de álcool com tolerância, abstinência e perda de controle; desintoxicação com "
        "diazepam em ambiente supervisionado; naltrexona ou acamprosato na manutenção da abstinência.",
        False, None, "muito_alta", "media",
        "Homens jovens, adultos de baixa renda, trabalhadores da construção civil, HF de alcoolismo",
        "CFM-SM"
    ),
    (
        "Dependência de Opioides",
        "F11.2", "Saúde Mental e Neurológico",
        "Dependência a opioides prescritos ou ilícitos; terapia de manutenção com metadona ou buprenorfina/naloxona "
        "(BUPNX); naloxona como antídoto na overdose; abordagem por redução de danos.",
        False, None, "media", "alta",
        "Adultos com dor crônica em uso prolongado de opioides, usuários de drogas ilícitas injetáveis",
        "CFM-SM"
    ),
    (
        "Demência de Alzheimer — Leve a Moderada",
        "G30.9", "Saúde Mental e Neurológico",
        "Demência neurodegenerativa progressiva; inibidores de colinesterase (donepezila, rivastigmina) "
        "para leve-moderada; memantina para moderada-grave; lecanemabe/donanemabe em estágios precoces.",
        False, None, "alta", "media",
        "Idosos > 65 anos, HF de Alzheimer, portadores de APOE-ε4, baixa escolaridade, HAS não controlada",
        "PCDT-ALZHEIMER"
    ),
    (
        "Demência Vascular",
        "F01.9", "Saúde Mental e Neurológico",
        "Declínio cognitivo por doença cerebrovascular; controle intensivo de HAS, DM e dislipidemia para "
        "prevenção de progressão; antiagregação em etiologia aterotrombótica; sem farmacoterapia específica aprovada.",
        False, None, "media", "media",
        "Idosos > 70 anos, hipertensos, diabéticos, fibrilação atrial, AVC prévio, fumantes",
        "PCDT-ALZHEIMER"
    ),
    (
        "Epilepsia Focal (Crise Parcial)",
        "G40.1", "Saúde Mental e Neurológico",
        "Crises com início focal (antes: parcial); carbamazepina ou lacosamida como primeira linha; "
        "cirurgia de epilepsia em farmacorresistente com foco ressecável; estimulação do nervo vago.",
        False, None, "alta", "baixa",
        "Crianças e adultos jovens, pós-encefalite, malformações corticais, TCE prévio, AVC",
        "PCDT-EPILEPSIA"
    ),
    (
        "Epilepsia Generalizada",
        "G40.3", "Saúde Mental e Neurológico",
        "Crises com início bilateral sincronizado; ácido valproico como fármaco de amplo espectro; "
        "lamotrigina ou levetiracetam como alternativas; restrições específicas na mulher em idade fértil.",
        False, None, "alta", "baixa",
        "Crianças (epilepsias idiopáticas), adultos jovens; HF de epilepsia generalizada",
        "PCDT-EPILEPSIA"
    ),
    (
        "Doença de Parkinson — Estágio Inicial a Moderado (H&Y 1-3)",
        "G20", "Saúde Mental e Neurológico",
        "Doença neurodegenerativa com tremor de repouso, rigidez e bradicinesia; levodopa/carbidopa como "
        "padrão-ouro; agonistas dopaminérgicos em jovens; deep brain stimulation em flutuações motoras.",
        False, None, "media", "media",
        "Adultos > 60 anos, exposição a pesticidas/herbicidas, HF de Parkinson, sexo masculino",
        "PCDT-PARKINSON"
    ),
    (
        "Migrânea Sem Aura (Profilaxia)",
        "G43.0", "Saúde Mental e Neurológico",
        "Cefaleia primária episódica intensa; profilaxia indicada em ≥ 4 crises/mês: topiramato, propranolol, "
        "amitriptilina; anticorpos anti-CGRP (fremanezumabe, galcanezumabe) em casos refratários.",
        False, None, "muito_alta", "baixa",
        "Mulheres (3:1), adultos de 20-50 anos, HF de migrânea, distúrbios do sono",
        "ABN-EPILEPSIA"
    ),
    (
        "Esclerose Múltipla — Forma Remitente-Recorrente (EMRR)",
        "G35", "Saúde Mental e Neurológico",
        "Doença autoimune desmielinizante do SNC; interferon-β, glatirâmer ou natalizumabe como primeiras "
        "linhas; ocrelizumabe, alemtuzumabe ou cladribina em alta atividade; RM cerebral como monitoramento.",
        False, None, "baixa", "media",
        "Adultos jovens (20-40 anos), mulheres (2:1), regiões de latitude maior, HF de doenças autoimunes",
        "ABN-PARKINSON"
    ),
    (
        "Miastenia Gravis Generalizada",
        "G70.0", "Saúde Mental e Neurológico",
        "Doença autoimune da junção neuromuscular com anticorpos anti-AChR ou anti-MuSK; piridostigmina "
        "para sintomas; imunossupressores (prednisona + azatioprina); timectomia em timoma.",
        False, None, "rara", "media",
        "Bimodal: mulheres jovens (20-30 anos) e homens idosos (> 60 anos); timoma em 10-15%",
        "ABN-PARKINSON"
    ),

    # ── RESPIRATÓRIO CRÔNICO (8) ────────────────────────────────────────────────
    (
        "Asma Persistente Leve a Moderada",
        "J45.1", "Respiratório Crônico",
        "Inflamação crônica das vias aéreas com reversibilidade ao broncodilatador; CI + LABA como "
        "tratamento degrau 3-4 do GINA; controle ambiental de alérgenos; imunoterapia em alérgicos.",
        False, None, "muito_alta", "baixa",
        "Crianças (principal causa de hospitalização pediátrica), adultos jovens, atópicos, fumantes",
        "PCDT-ASMA"
    ),
    (
        "Asma Grave Não Controlada / Asma de Difícil Controle",
        "J45.5", "Respiratório Crônico",
        "Asma persistindo não controlada apesar do tratamento máximo inalatório; biológicos com alvo em "
        "via T2 (mepolizumabe, benralizumabe, dupilumabe); triagem de fenótipo/endótipo para seleção.",
        False, None, "alta", "media",
        "Adultos com eosinofilia persistente, IgE elevada, exposição ocupacional, obesidade mórbida",
        "PCDT-ASMA"
    ),
    (
        "DPOC — Grupos A-B (GOLD) / Pouco Sintomático ou Pouco Agudizante",
        "J44.1", "Respiratório Crônico",
        "Obstrução irreversível ao fluxo aéreo; LAMA como monoterapia preferencial no GOLD A/B sem "
        "eosinofilia; reabilitação pulmonar; vacinação influenza e pneumocócica; cessação tabágica.",
        False, None, "alta", "media",
        "Tabagistas > 20 maços-ano, ex-tabagistas, exposição ocupacional a poeiras/gases, déficit de α1-AT",
        "PCDT-DPOC"
    ),
    (
        "DPOC — Grupo E (GOLD) / Muito Sintomático e Alto Risco de Agudizações",
        "J44.1", "Respiratório Crônico",
        "DPOC com ≥ 2 agudizações/ano ou ≥ 1 com hospitalização; LAMA + LABA + CI em eosinófilos ≥ 300; "
        "roflumilaste ou azitromicina como add-on; oxigenoterapia domiciliar se PaO₂ ≤ 55 mmHg.",
        False, None, "alta", "alta",
        "Tabagistas pesados, pacientes com múltiplas hospitalizações prévias, DPOC grave (VEF1 < 30%)",
        "PCDT-DPOC"
    ),
    (
        "Apneia Obstrutiva do Sono (SAOS) Moderada-Grave",
        "G47.3", "Respiratório Crônico",
        "IAH ≥ 15 eventos/hora; CPAP como tratamento de primeira linha; dispositivo intraoral em leve-moderada; "
        "cirurgia (uvulopalatofaringoplastia) em casos selecionados; controle do peso.",
        False, None, "muito_alta", "media",
        "Homens obesos de meia-idade (> 40 anos), mulheres pós-menopausa, hipotireoidismo, macroglossia",
        "CFM-SM"
    ),
    (
        "Fibrose Pulmonar Idiopática (FPI)",
        "J84.1", "Respiratório Crônico",
        "Pneumonia intersticial usual de causa desconhecida; nintedanibe ou pirfenidona retardam declínio "
        "funcional; transplante pulmonar único em candidatos adequados; prognóstico reservado (mediana 3-5 anos).",
        False, None, "rara", "alta",
        "Homens > 60 anos, tabagistas ou ex-tabagistas, exposição a poeira de madeira/metal, HF de FPI",
        "CFM-SM"
    ),
    (
        "Hipertensão Pulmonar Arterial (HAP) — Grupo 1",
        "I27.0", "Respiratório Crônico",
        "HAP idiopática, hereditária ou associada a CTD/cardiopatias congênitas/HIV; terapia de combinação "
        "com ERA + PDE5i ± prostaciclina; avaliação para transplante pulmonar bilateral em refratários.",
        False, None, "rara", "alta",
        "Mulheres jovens, portadores de esclerodermia, HIV, esquistossomose hepática, LES",
        "SBC-ICC"
    ),
    (
        "Sarcoidose Pulmonar — Estágio II-III",
        "D86.0", "Respiratório Crônico",
        "Doença granulomatosa sistêmica com infiltrado pulmonar bilateral e adenopatia hilar; corticoide "
        "sistêmico indicado em deterioração funcional; metotrexato como poupador de esteroide.",
        False, None, "rara", "baixa",
        "Adultos jovens (20-40 anos), negros (maior prevalência e gravidade), mulheres ligeiramente mais afetadas",
        "CFM-SM"
    ),

    # ── GASTROINTESTINAL E HEPÁTICO (12) ───────────────────────────────────────
    (
        "Doença do Refluxo Gastroesofágico (DRGE) — Erosiva",
        "K21.0", "Gastrointestinal e Hepático",
        "Esofagite erosiva grau A-D de Los Angeles por refluxo ácido; IBP (omeprazol/pantoprazol) como "
        "tratamento de primeira linha; terapia de manutenção em doença frequentemente recidivante.",
        False, None, "muito_alta", "baixa",
        "Adultos obesos, tabagistas, com hérnia de hiato, uso de AINEs, gestantes",
        "CFM-SM"
    ),
    (
        "Úlcera Péptica Gastroduodenal (H. pylori-Positiva)",
        "K27.9", "Gastrointestinal e Hepático",
        "Úlcera gástrica ou duodenal associada a H. pylori; erradicação com terapia quádrupla (IBP + "
        "claritromicina + amoxicilina + bismuto) por 14 dias; confirmação de erradicação com teste respiratório.",
        False, None, "muito_alta", "baixa",
        "Adultos em condições socioeconômicas desfavoráveis, uso de AINEs/aspirina, fumantes, alcoolistas",
        "CFM-SM"
    ),
    (
        "Doença de Crohn — Ileocólica, Luminal Moderada-Grave",
        "K50.1", "Gastrointestinal e Hepático",
        "DII transmural com acometimento ileocólico; indução com corticoide ou biológico; anti-TNF "
        "(infliximabe, adalimumabe) como pilares terapêuticos; vedolizumabe e ustekinumabe em falha.",
        False, None, "media", "media",
        "Adultos jovens (20-40 anos), fumantes (fator de risco único para DC), HF de DII",
        "PCDT-CROHN"
    ),
    (
        "Retocolite Ulcerativa (RCU) — Extensiva, Moderada-Grave",
        "K51.0", "Gastrointestinal e Hepático",
        "DII limitada à mucosa do cólon; aminossalicilatos para leve; corticoide + anti-TNF para "
        "moderada-grave; vedolizumabe, tofacitinibe ou ozanimode como segunda linha; colectomia em refratários.",
        False, None, "media", "media",
        "Adultos jovens (20-40 anos), não-fumantes e ex-fumantes, HF de DII, ascendência judaica",
        "PCDT-RCU"
    ),
    (
        "Síndrome do Intestino Irritável (SII) com Diarreia",
        "K58.0", "Gastrointestinal e Hepático",
        "Dor abdominal recorrente associada a alteração do hábito intestinal sem causa orgânica; dieta "
        "low-FODMAP; antiespasmódicos e antidiarreicos; rifaximina em SII-D; TCC e amitriptilina em refratários.",
        False, None, "muito_alta", "baixa",
        "Adultos jovens (20-45 anos), mulheres (2:1), ansiedade e depressão comórbidas, história de gastrenterite",
        "CFM-SM"
    ),
    (
        "Doença Hepática Gordurosa Não Alcoólica / NASH com Fibrose",
        "K76.0", "Gastrointestinal e Hepático",
        "Espectro de esteatose a esteato-hepatite com fibrose progressiva; mudança de estilo de vida e "
        "perda de peso como tratamento central; resmetirom aprovado para MASH com fibrose F2-F3; rastreio de CHC.",
        False, None, "muito_alta", "media",
        "Obesos, diabéticos tipo 2, dislipidêmicos, síndrome metabólica, adultos > 40 anos",
        "CFM-SM"
    ),
    (
        "Cirrose Hepática Compensada (Child-Pugh A)",
        "K74.6", "Gastrointestinal e Hepático",
        "Fibrose hepática avançada sem complicações; abstinência alcoólica e tratamento da causa base; "
        "rastreio semestral de CHC (USG + alfafetoproteína); betabloqueador não seletivo para prevenção de varizes.",
        False, None, "media", "media",
        "Alcoolistas crônicos, portadores de VHC/VHB, NASH com fibrose avançada, hemocromatose",
        "CFM-SM"
    ),
    (
        "Cirrose Hepática Descompensada — Ascite / Encefalopatia",
        "K74.6", "Gastrointestinal e Hepático",
        "Cirrose com complicações: ascite, encefalopatia hepática, sangramento varicoso ou PBE; paracentese "
        "de alívio + albumina; rifaximina para encefalopatia; TIPS ou transplante hepático em candidatos.",
        False, None, "media", "alta",
        "Cirróticos com função hepática deteriorada (Child B-C), etilistas sem abstinência, hepatite B reativada",
        "CFM-SM"
    ),
    (
        "Pancreatite Crônica",
        "K86.1", "Gastrointestinal e Hepático",
        "Inflamação pancreática progressiva com fibrose e perda funcional exócrina e endócrina; abstinência "
        "alcoólica obrigatória; enzimas pancreáticas em insuficiência exócrina; analgesia escalonada.",
        False, None, "baixa", "media",
        "Homens alcoolistas (50-70% dos casos), tabagistas, mutações CFTR, hipercalcemia, hipertrigliceridemia",
        "CFM-SM"
    ),
    (
        "Doença Celíaca",
        "K90.0", "Gastrointestinal e Hepático",
        "Enteropatia autoimune induzida por glúten em HLA-DQ2/DQ8; dieta isenta de glúten como único "
        "tratamento; sorologia (anti-tTG IgA) para rastreio; biópsia duodenal para confirmação.",
        False, None, "media", "baixa",
        "HF de doença celíaca, portadores de DM1, tireoidite de Hashimoto, síndrome de Down, trisomia 21",
        "CFM-SM"
    ),
    (
        "Hemorragia Digestiva por Varizes Esofágicas",
        "I85.0", "Gastrointestinal e Hepático",
        "Sangramento varicoso em cirróticos; ressuscitação volêmica criteriosa + terlipressina/somatostatina + "
        "ligadura elástica endoscópica; antibióticos profiláticos; betabloqueador na profilaxia secundária.",
        False, None, "media", "alta",
        "Cirróticos com hipertensão portal, Child B-C, presença de varizes de grosso calibre",
        "CFM-SM"
    ),
    (
        "Colestase / Colangite Biliar Primária (CBP)",
        "K83.0", "Gastrointestinal e Hepático",
        "Doença autoimune das vias biliares intra-hepáticas com anticorpos anti-mitocôndria (AMA); "
        "ácido ursodesoxicólico como primeira linha; obeticólico ou fibratos em resposta inadequada.",
        False, None, "rara", "media",
        "Mulheres de meia-idade (40-60 anos), HF de doenças autoimunes, síndrome de Sjögren associada",
        "CFM-SM"
    ),

    # ── RENAL E UROLÓGICO (8) ──────────────────────────────────────────────────
    (
        "Doença Renal Crônica — Estágios G1-G3 (Leve-Moderada)",
        "N18.3", "Renal e Urológico",
        "TFG 30-89 mL/min/1,73 m²; controle de HAS (< 130/80 mmHg), DM e proteinúria com IECA/BRA; "
        "SGLT2i com benefício nefroprotetor; restrição proteica moderada; evitar nefrotóxicos.",
        False, None, "muito_alta", "media",
        "Diabéticos, hipertensos, obesos, idosos > 65 anos, HF de DRC, uso crônico de AINEs",
        "PCDT-DRC"
    ),
    (
        "Doença Renal Crônica — Estágios G4-G5 (Pré-Diálise)",
        "N18.4", "Renal e Urológico",
        "TFG < 30 mL/min/1,73 m²; manejo multidisciplinar pré-dialítico; controle de complicações "
        "(anemia, hiperfosfatemia, acidose metabólica, hiperparatireoidismo secundário); acesso para diálise.",
        False, None, "alta", "alta",
        "DRC avançada por DM, HAS, GN; hipertensos com HVE; portadores de doença renal policística",
        "PCDT-DRC"
    ),
    (
        "Síndrome Nefrótica (por Glomerulopatia)",
        "N04.9", "Renal e Urológico",
        "Proteinúria > 3,5 g/dia, edema, hipoalbuminemia e dislipidemia; causa mais comum em adultos: "
        "glomeruloesclerose segmentar focal (GESF); nefrose membranosa; corticoide e imunossupressores.",
        False, None, "media", "media",
        "Adultos jovens a meia-idade; DM como causa mais frequente em idosos; neoplasias associadas",
        "PCDT-DRC"
    ),
    (
        "Nefrolitíase (Litíase Renal Recorrente)",
        "N20.0", "Renal e Urológico",
        "Cálculos renais recorrentes de oxalato de cálcio (80% dos casos); hidratação intensiva; "
        "citrato de potássio em hipocitratúria; alopurinol em litíase úrica; PCNL/LECO conforme tamanho.",
        False, None, "alta", "baixa",
        "Homens de 30-50 anos, baixa ingesta hídrica, hiperuricemia, hiperparatireoidismo, dieta hipercalórica",
        "PCDT-DRC"
    ),
    (
        "Hiperplasia Prostática Benigna (HPB) Sintomática",
        "N40", "Renal e Urológico",
        "Obstrução infravesical por aumento prostático benigno; alfa-bloqueadores (tansulosina) como "
        "primeira linha; inibidores da 5-alfa-redutase em próstata > 40 mL; RTUP em refratários.",
        False, None, "muito_alta", "baixa",
        "Homens > 50 anos (prevalência aumenta progressivamente com a idade)",
        "CFM-SM"
    ),
    (
        "Bexiga Hiperativa / Incontinência Urinária de Urgência",
        "N32.8", "Renal e Urológico",
        "Urgência miccional com ou sem escape urinário de urgência; antimuscarínicos (solifenacina, "
        "oxibutinina) ou mirabegrona como farmacoterapia; fisioterapia do assoalho pélvico; neuromodulação.",
        False, None, "alta", "baixa",
        "Mulheres pós-menopáusicas, idosos de ambos os sexos, obesos, neuropatia diabética",
        "CFM-SM"
    ),
    (
        "Anemia da DRC (Eritropoetina-Responsiva)",
        "N18.9", "Renal e Urológico",
        "Anemia normocrômica-normocítica por deficiência de eritropoetina; agentes estimuladores de "
        "eritropoese (epoetina alfa, darbepoetina); reposição de ferro antes e durante ESA; Hb-alvo 10-12 g/dL.",
        False, None, "alta", "media",
        "Pacientes em diálise, DRC estágios G4-G5, neoplasias hematológicas com insuficiência renal",
        "PCDT-DRC"
    ),
    (
        "Nefropatia Diabética (DRC por DM)",
        "N08.3", "Renal e Urológico",
        "Glomerulopatia diabética com microalbuminúria evoluindo para macroalbuminúria e declínio de TFG; "
        "IECA ou BRA obrigatório; SGLT2i (finerenona + canagliflozina) para nefroproteção adicional.",
        False, None, "alta", "alta",
        "DM1 com > 10 anos de doença, DM2 com controle glicêmico inadequado, HAS concomitante",
        "PCDT-DM2"
    ),

    # ── MUSCULOESQUELÉTICO E REUMATOLÓGICO (12) ────────────────────────────────
    (
        "Osteoartrite de Joelho e Quadril (Sintomática)",
        "M17.1", "Musculoesquelético e Reumatológico",
        "Degeneração da cartilagem articular com dor mecânica e limitação funcional; fisioterapia e "
        "exercício aeróbico como pilares; AINEs tópicos e sistêmicos; artroplastia total em doença grave.",
        False, None, "muito_alta", "baixa",
        "Mulheres > 50 anos, obesos, trabalhadores com sobrecarga articular, HF de osteoartrite",
        "SBR-AR"
    ),
    (
        "Artrite Reumatoide — Início / Atividade Baixa-Moderada",
        "M05.9", "Musculoesquelético e Reumatológico",
        "Artrite inflamatória simétrica de pequenas articulações; metotrexato como DMARD-ancoragem; "
        "HCQ e sulfassalazina como adjuvantes; meta treat-to-target com DAS28 < 2,6 como objetivo.",
        False, None, "alta", "media",
        "Mulheres de 40-60 anos (3:1), fumantes, HLA-DRB1 (*04), HF de AR",
        "PCDT-AR"
    ),
    (
        "Artrite Reumatoide — Atividade Alta / Com Erosões",
        "M05.9", "Musculoesquelético e Reumatológico",
        "AR com falha ao MTX convencional; biológicos anti-TNF (adalimumabe, etanercepte) ou abatacepte "
        "como segunda linha; JAK inibidores (tofacitinibe, baricitinibe) como alternativa; rastreio de tuberculose.",
        False, None, "alta", "media",
        "Pacientes com fator reumatoide e anti-CCP positivos em altos títulos, fumantes, doença de longa data",
        "PCDT-AR"
    ),
    (
        "Lúpus Eritematoso Sistêmico (LES) — Moderado",
        "M32.9", "Musculoesquelético e Reumatológico",
        "Doença autoimune sistêmica multifatorial; HCQ obrigatório em todos os pacientes; corticoide + "
        "azatioprina ou micofenolato para manifestações moderadas; belimumabe em atividade persistente.",
        False, None, "media", "media",
        "Mulheres jovens (20-40 anos, 9:1), negras com maior prevalência no Brasil, HF de doenças autoimunes",
        "PCDT-LES"
    ),
    (
        "Lúpus Eritematoso Sistêmico — Nefrite Lúpica Proliferativa",
        "M32.1", "Musculoesquelético e Reumatológico",
        "Nefrite classe III/IV com proteinúria nefrótica e hematúria; indução com micofenolato + "
        "corticoide + belimumabe ou voclosporino; azatioprina na manutenção; risco de DRC terminal.",
        False, None, "media", "alta",
        "LES com manifestações renais precoces, mulheres negras jovens, anti-dsDNA e hipocomplementemia",
        "PCDT-LES"
    ),
    (
        "Espondilite Anquilosante / Espondiloartrite Axial",
        "M45", "Musculoesquelético e Reumatológico",
        "Artrite inflamatória axial com sacroileíte; AINE como primeira linha; anti-TNF (etanercepte, "
        "adalimumabe) em falha; ixequizumabe/secuquinumabe em casos selecionados; fisioterapia respiratória.",
        False, None, "media", "media",
        "Homens jovens (20-40 anos, 3:1), HLA-B27 positivo (~90% dos casos), HF de espondiloartropatia",
        "SBR-AR"
    ),
    (
        "Artrite Psoriática (com Comprometimento Articular Periférico)",
        "L40.5", "Musculoesquelético e Reumatológico",
        "Artrite associada à psoríase cutânea ou ungueal; MTX para doença leve; anti-TNF ou anti-IL-17 "
        "(secuquinumabe) em atividade alta; ustekinumabe e inibidores de JAK como alternativas.",
        False, None, "media", "media",
        "Adultos com psoríase (20-30% desenvolvem artrite), HF de artrite psoriática, tabagistas",
        "SBR-AR"
    ),
    (
        "Osteoporose Pós-Menopausa (com ou sem Fratura Prévia)",
        "M81.0", "Musculoesquelético e Reumatológico",
        "DMO T-score ≤ -2,5 ou fratura por fragilidade; bisfosfonatos (alendronato, risedronato) como "
        "primeira linha; denosumabe em alto risco; teriparatida em osteoporose grave com múltiplas fraturas.",
        False, None, "muito_alta", "media",
        "Mulheres pós-menopausa, fumantes, etilistas, uso crônico de corticoide, baixo peso, sedentarismo",
        "PCDT-OSTEOPOROSE"
    ),
    (
        "Fibromialgia",
        "M79.3", "Musculoesquelético e Reumatológico",
        "Síndrome de dor musculoesquelética crônica difusa com fadiga, sono não reparador e disfunção "
        "cognitiva; exercício aeróbico como tratamento central; duloxetina, pregabalina ou amitriptilina.",
        False, None, "alta", "baixa",
        "Mulheres de 30-50 anos (7:1), comorbidades com ansiedade e depressão, síndrome do intestino irritável",
        "SBR-AR"
    ),
    (
        "Síndrome de Sjögren Primária",
        "M35.0", "Musculoesquelético e Reumatológico",
        "Exocrinopatia autoimune com xeroftalmia e xerostomia; pilocarpina para estimulação glandular; "
        "HCQ para manifestações sistêmicas; rituximabe em manifestações graves; rastreio de linfoma.",
        False, None, "media", "baixa",
        "Mulheres de meia-idade (40-60 anos, 9:1), HF de doenças autoimunes, anti-Ro/SSA positivo",
        "SBR-AR"
    ),
    (
        "Polimialgia Reumática / Arterite de Células Gigantes",
        "M35.3", "Musculoesquelético e Reumatológico",
        "Dor e rigidez de cintura escapular e pélvica; corticoide (prednisona 15-20 mg/d) com redução lenta; "
        "tocilizumabe como poupador de esteroide na arterite de células gigantes com risco de recaída.",
        False, None, "baixa", "media",
        "Idosos > 50 anos (pico 70-80 anos), mulheres (2:1), ascendência nórdica",
        "SBR-AR"
    ),
    (
        "Vasculite ANCA-Positiva (Granulomatose com Poliangiite)",
        "M31.3", "Musculoesquelético e Reumatológico",
        "Vasculite de pequenos vasos com comprometimento pulmonar e renal; rituximabe + ciclofosfamida + "
        "corticoide na indução; rituximabe na manutenção; plasmaférese em síndrome pulmão-rim.",
        False, None, "rara", "alta",
        "Adultos de meia-idade (40-60 anos), ligeiramente mais comum em homens, c-ANCA/PR3 positivo",
        "SBR-AR"
    ),

    # ── DERMATOLÓGICO CRÔNICO (7) ──────────────────────────────────────────────
    (
        "Psoríase em Placas — Moderada (BSA 3-10%)",
        "L40.0", "Dermatológico Crônico",
        "Dermatose inflamatória crônica com placas eritematoescamosas; terapia tópica (corticoide + "
        "análogo da vitamina D) insuficiente na moderada; metotrexato, acitretina ou ciclosporina oral.",
        False, None, "alta", "baixa",
        "Adultos de 20-50 anos, HF de psoríase (hereditariedade ~30%), tabagistas, obesos, etilistas",
        "PCDT-PSORIASE"
    ),
    (
        "Psoríase Grave / Eritrodérmica / Pustulosa",
        "L40.1", "Dermatológico Crônico",
        "Psoríase com BSA > 10% ou eritrodermia/pustulosa generalizada; biológicos anti-IL-17 "
        "(secuquinumabe, ixequizumabe) ou anti-IL-23 (riseankumabe, guselkumabe) como tratamento de escolha.",
        False, None, "media", "media",
        "Pacientes com psoríase instável, infecção como gatilho, retirada abrupta de corticoide sistêmico",
        "PCDT-PSORIASE"
    ),
    (
        "Dermatite Atópica — Moderada a Grave",
        "L20.9", "Dermatológico Crônico",
        "Eczema crônico pruriginoso com disfunção de barreira cutânea; emolientes intensivos; dupilumabe "
        "(anti-IL-4Rα) ou tralokinumabe (anti-IL-13) para moderada-grave; JAK inibidores (upadacitinibe).",
        False, None, "muito_alta", "baixa",
        "Crianças (início < 5 anos em 85%), atópicos com rinite e asma, HF de atopia",
        "CFM-SM"
    ),
    (
        "Acne Vulgaris Moderada a Grave (Nódulo-Cística)",
        "L70.0", "Dermatológico Crônico",
        "Acne com nódulos e cistos com risco de cicatrizes; isotretinoína oral como padrão para acne "
        "grave; antibióticos sistêmicos + adapaleno tópico para moderada; hormônioterapia nas mulheres.",
        False, None, "muito_alta", "baixa",
        "Adolescentes e adultos jovens (15-30 anos), ambos os sexos, hiperandrogenismo feminino",
        "CFM-SM"
    ),
    (
        "Urticária Crônica Espontânea (UCE)",
        "L50.1", "Dermatológico Crônico",
        "Urticária persistindo > 6 semanas sem causa identificável; anti-histamínico H1 de segunda "
        "geração como primeira linha; omalizumabe (anti-IgE) em refratários; ciclosporina em casos graves.",
        False, None, "alta", "baixa",
        "Adultos de 30-50 anos, mulheres (2:1), autoimunidade tireoidiana associada em 25% dos casos",
        "CFM-SM"
    ),
    (
        "Rosácea (Eritematotelangectásica e Papulopustulosa)",
        "L71.9", "Dermatológico Crônico",
        "Dermatose facial crônica com eritema central e telangiectasias; metronidazol ou ácido azelaico "
        "tópico; doxiciclina sub-antimicrobiana (40 mg) oral; laser para telangiectasias.",
        False, None, "alta", "baixa",
        "Adultos de pele clara (fotótipo I-II), mulheres de 30-50 anos, HF de rosácea, clima frio",
        "CFM-SM"
    ),
    (
        "Vitiligo Generalizado",
        "L80", "Dermatológico Crônico",
        "Despigmentação autoimune da pele por destruição de melanócitos; corticoide tópico ou inibidores "
        "de calcineurina; ruxolitinibe creme (JAK1/2) aprovado; PUVA ou NB-UVB para repigmentação.",
        False, None, "media", "baixa",
        "Adultos jovens (início 10-30 anos), HF de vitiligo, doenças autoimunes associadas (DM1, tireoidite)",
        "CFM-SM"
    ),

    # ── HEMATOLÓGICO (8) ───────────────────────────────────────────────────────
    (
        "Anemia Ferropriva (Adulto)",
        "D50.9", "Hematológico",
        "Deficiência de ferro com anemia microcítica hipocrômica; investigação obrigatória da causa "
        "(sangramento oculto, má absorção); sulfato ferroso oral por 3-6 meses; ferro EV em intolerância.",
        False, None, "muito_alta", "baixa",
        "Mulheres em idade reprodutiva, gestantes, crianças < 2 anos, vegetarianos, pacientes com DII",
        "CFM-SM"
    ),
    (
        "Anemia por Deficiência de B12 / Anemia Perniciosa",
        "D51.0", "Hematológico",
        "Anemia megaloblástica por deficiência de cobalamina; gastrite autoimune com anticorpos anti-FI "
        "em anemia perniciosa; cianocobalamina IM mensal ou reposição oral de alta dose; rastreio de CA gástrico.",
        False, None, "alta", "baixa",
        "Idosos > 65 anos, veganos, pós-gastrectomia, uso crônico de metformina/IBP, má absorção intestinal",
        "CFM-SM"
    ),
    (
        "Doença Falciforme (Anemia Falciforme — HbSS)",
        "D57.0", "Hematológico",
        "Hemoglobinopatia autossômica recessiva com hemólise crônica e vasoclusão; hidroxiureia para "
        "redução das crises; transfusão crônica em AVC e priapismo; transplante de células-tronco hematopoéticas.",
        False, None, "media", "alta",
        "Afrodescendentes (maior prevalência entre negros brasileiros), portadores do traço falciforme HbAS",
        "PCDT-ANEMIA-FALCIF"
    ),
    (
        "Púrpura Trombocitopênica Imune (PTI) Primária Crônica",
        "D69.3", "Hematológico",
        "Trombocitopenia autoimune sem causa secundária identificável; corticoide na crise aguda; "
        "eltrombopague ou romiplostim (TPO-RA) na PTI crônica refratária; rituximabe como segunda linha.",
        False, None, "media", "media",
        "Adultos de 20-50 anos, mulheres na forma crônica, crianças na forma aguda pós-infecção viral",
        "CFM-SM"
    ),
    (
        "Hemofilia A — Moderada a Grave",
        "D66", "Hematológico",
        "Deficiência de fator VIII com sangramento articular recorrente (hemartroses); profilaxia com "
        "fator VIII concentrado EV; emicizumabe SC como profilaxia em hemofilia A com e sem inibidores.",
        False, None, "rara", "alta",
        "Masculino (ligado ao X), filhos de portadoras; rara em mulheres (homozigose ou lyonização extrema)",
        "CFM-SM"
    ),
    (
        "Mieloma Múltiplo — Sintomático",
        "C90.0", "Hematológico",
        "Neoplasia de plasmócitos com hipercalcemia, insuficiência renal, anemia e lesões ósseas (CRAB); "
        "VRd (bortezomibe + lenalidomida + dexametasona) como indução; ASCT em elegíveis; daratumumabe.",
        False, None, "baixa", "alta",
        "Adultos > 65 anos, negros (2x maior risco), MGUS como precursor; HF de gamapatia monoclonal",
        "INCA-ONCOL"
    ),
    (
        "Policitemia Vera",
        "D45", "Hematológico",
        "Neoplasia mieloproliferativa com mutação JAK2 V617F e eritrocitose; flebotomia para Hct < 45%; "
        "hidroxiureia em alto risco; ruxolitinibe em refratários; AAS em baixa dose; risco de trombose.",
        False, None, "rara", "media",
        "Adultos > 60 anos, ligeiramente mais comum em homens, mutação JAK2 V617F em > 95% dos casos",
        "CFM-SM"
    ),
    (
        "Trombose Venosa Recorrente (Anticoagulação Prolongada)",
        "I82.9", "Hematológico",
        "TVP ou TEP recorrente com indicação de anticoagulação por tempo indefinido; NOAC (rivaroxabana, "
        "apixabana) preferidos ao warfarina; investigação de trombofilia hereditária e neoplasia oculta.",
        False, None, "media", "media",
        "Portadores de síndrome antifosfolípide, trombofilia hereditária (fator V Leiden, MTHFR), neoplasias",
        "SBC-SCA"
    ),

    # ── GINECOLÓGICO E OBSTÉTRICO (10) ─────────────────────────────────────────
    (
        "Síndrome dos Ovários Policísticos (SOP) com Infertilidade",
        "E28.2", "Ginecológico e Obstétrico",
        "Hiperandrogenismo, oligo-anovulação e morfologia policística ovariana; metformina para resistência "
        "insulínica; letrozol para indução ovulatória; anticoncepcionais hormonais para controle de ciclo.",
        False, None, "muito_alta", "baixa",
        "Mulheres em idade reprodutiva (18-35 anos), obesas, com HF de DM2 ou SOP, resistência insulínica",
        "SBD-DM2"
    ),
    (
        "Endometriose — Moderada a Grave",
        "N80.1", "Ginecológico e Obstétrico",
        "Implantes de tecido endometrial fora do útero com dismenorreia intensa e infertilidade; "
        "DIU de levonorgestrel ou progestágenos orais; laparoscopia diagnóstica e terapêutica; FIV.",
        False, None, "alta", "baixa",
        "Mulheres de 25-40 anos, menarca precoce, ciclos curtos, nuliparidade, HF de endometriose",
        "CFM-SM"
    ),
    (
        "Mioma Uterino Sintomático",
        "D25.9", "Ginecológico e Obstétrico",
        "Leiomiomas uterinos com sangramento uterino anormal e/ou dor pélvica; ulipristal ou análogos "
        "de GnRH para redução pré-cirúrgica; miomectomia em mulheres com desejo reprodutivo; histerectomia.",
        False, None, "alta", "baixa",
        "Mulheres de 35-50 anos, negras (3-4x maior risco), nuliparidade, obesidade, HF de mioma",
        "CFM-SM"
    ),
    (
        "Síndrome do Climatério / Menopausa (Sintomas Vasomotores)",
        "N95.1", "Ginecológico e Obstétrico",
        "Fogachos, sudorese noturna e atrofia vaginal na transição menopausal; terapia hormonal da menopausa "
        "(estrogênio ± progesterona) em mulheres sem contraindicações; tibolona; terapias não hormonais.",
        False, None, "muito_alta", "baixa",
        "Mulheres entre 45-55 anos, menopausa precoce iatrogênica, ooforectomia bilateral, fumantes",
        "CFM-SM"
    ),
    (
        "Pré-Eclâmpsia / Síndrome HELLP",
        "O14.1", "Ginecológico e Obstétrico",
        "HAS gestacional com proteinúria após 20 semanas; magnésio IV para profilaxia de convulsão; "
        "anti-hipertensivos parenterais (hidralazina) em PE grave; parto como único tratamento definitivo.",
        False, None, "media", "alta",
        "Gestantes nulíparas, obesas, hipertensas prévias, DM, idade > 35 anos, gestação múltipla",
        "PCDT-HAS"
    ),
    (
        "Eclâmpsia",
        "O15.0", "Ginecológico e Obstétrico",
        "Convulsões em contexto de pré-eclâmpsia; magnésio sulfato IV como anticonvulsivante de escolha; "
        "controle pressórico agressivo; resolução obstétrica imediata após estabilização materna.",
        False, None, "baixa", "alta",
        "Gestantes com pré-eclâmpsia não controlada, primigestas jovens, baixo acesso ao pré-natal",
        "PCDT-HAS"
    ),
    (
        "Diabetes Gestacional (Requer Insulina)",
        "O24.4", "Ginecológico e Obstétrico",
        "GDM sem controle com dieta e exercício; insulina NPH noturna + regular pré-prandial; monitorização "
        "domiciliar de glicemia; metformina como alternativa segura quando insulina recusada.",
        False, None, "alta", "baixa",
        "Gestantes obesas > 35 anos, GDM prévia, macrossomia em gestação anterior, HF de DM2",
        "SBD-DM2"
    ),
    (
        "Hiperemese Gravídica",
        "O21.1", "Ginecológico e Obstétrico",
        "Vômitos incoercíveis no primeiro trimestre com perda ponderal > 5% e cetose; reposição "
        "hidroeletrolítica IV; ondansetrona + metoclopramida; tiamina IV para prevenção de Wernicke.",
        False, None, "media", "baixa",
        "Primíparas, gestação gemelar, doença trofoblástica, HF ou gestação anterior com hiperemese",
        "CFM-SM"
    ),
    (
        "Hemorragia Pós-Parto (Atonia Uterina)",
        "O72.1", "Ginecológico e Obstétrico",
        "Perda sanguínea > 500 mL no parto vaginal ou > 1000 mL na cesariana; ocitocina como primeira "
        "linha para atonia; misoprostol, ergometrina e ácido tranexâmico no manejo escalonado.",
        False, None, "media", "alta",
        "Macrossomia fetal, polidrâmnio, parto prolongado, multiparidade, placenta prévia, coagulopatia",
        "CFM-SM"
    ),
    (
        "Hipotireoidismo na Gestação",
        "O99.2", "Ginecológico e Obstétrico",
        "Hipotireoidismo clínico ou subclínico na gravidez com risco de déficit cognitivo fetal; "
        "levotiroxina com ajuste de dose (30-50% acima da dose pré-gestacional); TSH-alvo < 2,5 mUI/L.",
        False, None, "alta", "baixa",
        "Gestantes com tireoidite de Hashimoto, pós-tireoidectomia, hipotireoidismo prévio não tratado",
        "PCDT-HIPOTIREOID"
    ),

    # ── CARDIOVASCULAR — complementar (3) ──────────────────────────────────────
    (
        "Valvopatia Reumática — Estenose Mitral",
        "I05.0", "Cardiovascular",
        "Sequela de febre reumática com fusão das cúspides mitrais; comissurotomia mitral percutânea a "
        "balão em estenose moderada-grave com anatomia favorável; troca valvar quando indicada; anticoagulação.",
        False, None, "media", "media",
        "Adultos jovens em regiões de baixa renda, histórico de febre reumática na infância, FA associada",
        "SBC-ICC"
    ),
    (
        "Insuficiência Aórtica Crônica",
        "I35.1", "Cardiovascular",
        "Regurgitação aórtica por dilatação de raiz aórtica ou lesão valvar; vasodilatadores (IECA, "
        "bloqueadores de canal de cálcio) em sintomáticos sem indicação cirúrgica imediata; troca valvar conforme critérios.",
        False, None, "media", "media",
        "Síndrome de Marfan, síndrome de Ehlers-Danlos vascular, HAS sistêmica grave, valva bicúspide",
        "SBC-ICC"
    ),
    (
        "Miocardiopatia Chagásica Crônica",
        "B57.2", "Cardiovascular",
        "Cardiopatia por Trypanosoma cruzi com disfunção sistólica e bloqueios de condução; cardiodesfibrilador "
        "implantável em TVNS; terapia de ressincronização cardíaca; benznidazol na fase crônica recente.",
        False, None, "media", "alta",
        "Adultos de regiões endêmicas (Norte, Nordeste e Centro-Oeste), migrantes de zonas rurais",
        "SBC-ICC"
    ),

    # ── ENDÓCRINO E METABÓLICO — complementar (2) ──────────────────────────────
    (
        "Deficiência de Vitamina D (Hipovitaminose D Crônica)",
        "E55.9", "Endócrino e Metabólico",
        "Nível sérico de 25(OH)D < 20 ng/mL com consequências musculoesqueléticas e imunológicas; "
        "reposição com colecalciferol oral 50 000 UI/semana por 8 semanas, depois manutenção; exposição solar.",
        False, None, "muito_alta", "baixa",
        "Idosos institucionalizados, obesos, pessoas com baixa exposição solar, DRC, má absorção intestinal",
        "CFM-SM"
    ),
    (
        "Acromegalia",
        "E22.0", "Endócrino e Metabólico",
        "Hipersecreção de GH por adenoma hipofisário com IGF-1 elevado; cirurgia transesfenoidal como "
        "primeira linha; análogos de somatostatina (octreotida, lanreotida) em doença residual; pegvisomanto.",
        False, None, "rara", "media",
        "Adultos de 30-50 anos, diagnóstico geralmente tardio (8-10 anos de atraso), comorbidades CV e DM",
        "CFM-SM"
    ),

    # ── SAÚDE MENTAL E NEUROLÓGICO — complementar (2) ──────────────────────────
    (
        "Esclerose Lateral Amiotrófica (ELA)",
        "G12.2", "Saúde Mental e Neurológico",
        "Doença neurodegenerativa de neurônio motor superior e inferior; riluzol e edaravona retardam "
        "progressão modestamente; cuidados paliativos; ventilação não invasiva prolonga sobrevida.",
        False, None, "rara", "alta",
        "Adultos de 50-70 anos, ligeiramente mais comum em homens, mutação SOD1 em formas familiares",
        "ABN-PARKINSON"
    ),
    (
        "Síndrome de Tourette / Tiques Crônicos",
        "F95.2", "Saúde Mental e Neurológico",
        "Tiques motores múltiplos e ao menos um tique fônico por > 1 ano; aripiprazol, clonidina ou "
        "haloperidol em tiques graves com comprometimento funcional; TCC com reversão de hábitos.",
        False, None, "baixa", "baixa",
        "Crianças e adolescentes do sexo masculino (3-4:1), TOC e TDAH comórbidos em >50% dos casos",
        "CFM-SM"
    ),

    # ── RENAL E UROLÓGICO — complementar (1) ───────────────────────────────────
    (
        "Doença Renal Policística Autossômica Dominante (DRPAD)",
        "Q61.2", "Renal e Urológico",
        "Cistos renais progressivos por mutação PKD1/PKD2; tolvaptano retarda crescimento renal e declínio "
        "de TFG em progressores rápidos; manejo de dor, HAS e infecção de cistos; diálise/transplante.",
        False, None, "baixa", "media",
        "HF de DRPAD (dominante), adultos de 30-50 anos no diagnóstico, hipertensão arterial precoce",
        "PCDT-DRC"
    ),

    # ── MUSCULOESQUELÉTICO — complementar (1) ──────────────────────────────────
    (
        "Síndrome de Hipermobilidade Articular / Ehlers-Danlos Hipermóvel",
        "M35.7", "Musculoesquelético e Reumatológico",
        "Hiperlassidão ligamentar com subluxações recorrentes, dor crônica e disautonomia; fisioterapia "
        "de estabilização articular como pilar; analgesia multimodal; tricíclicos para dor neuropática.",
        False, None, "media", "baixa",
        "Mulheres jovens (3:1), adolescentes com dor crônica difusa, comorbidade com POTS e SII",
        "SBR-AR"
    ),

    # ── HEMATOLÓGICO — complementar (1) ────────────────────────────────────────
    (
        "Trombocitose Essencial (TE)",
        "D47.3", "Hematológico",
        "Neoplasia mieloproliferativa com plaquetas persistentemente elevadas (> 450 000/μL) e mutação "
        "JAK2/CALR/MPL; AAS em baixo risco; hidroxiureia em alto risco; anagrelida como alternativa.",
        False, None, "rara", "baixa",
        "Adultos de 50-60 anos, ligeiramente mais prevalente em mulheres, mutação JAK2 V617F em ~60%",
        "CFM-SM"
    ),

]

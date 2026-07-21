"""
Protocolos de tratamento padrão-ouro para micoses.
Baseado em: PCDT-PARACOC MS 2022, PCDT-HIV-FUNG MS 2022, SBI-CAND 2022,
            SBI-ASPERG 2019, SBI-CRIPTO 2021, SVS-HISTOP, SVS-ESPORO,
            SBD-MICOSES 2021, SBMT-FUNGOS, ANVISA-ANTIF.

Formato: (patologia_substr, antifungico_principal, combinacao_ou_None,
          regime_resumido, duracao_resumida, justificativa,
          alternativa_alergia_ou_contraindicacao, alternativa_resistencia,
          obs_especiais, grau_recomendacao, nivel_evidencia,
          fonte_sigla, ano_diretriz)

Graus de recomendação: 'A', 'B', 'C'
Níveis de evidência: 'I', 'II', 'III'
"""

TRATAMENTO_PADRAO_OURO_FUNGICO = [

    # ══════════════════════════════════════════════════════════════════
    # PARACOCCIDIOIDOMICOSE
    # ══════════════════════════════════════════════════════════════════
    ("Paracoccidioidomicose",
     "Itraconazol",
     None,
     "Itraconazol 200 mg/dia VO em dose única (cápsula com alimento ácido) ou "
     "Itraconazol solução oral 200 mg/dia (em jejum)",
     "12–18 meses para forma crônica multifocal; "
     "≥ 18 meses para formas graves ou com acometimento de SNC",
     "1ª linha para todas as formas — paracoccidioidomicose leve, moderada e grave (após indução IV). "
     "Eficácia >90%; menor toxicidade que anfotericina B; disponível no SUS (RENAME). "
     "PCDT MS 2022 recomenda como tratamento de escolha.",
     "Sulfametoxazol+Trimetoprima 800/160 mg 12/12h VO (em hepatopatas ou intolerância ao itraconazol); "
     "manter por 24 meses — menor eficácia e maior recidiva que itraconazol",
     "Voriconazol 200 mg 12/12h VO (casos refratários com falha documentada); dados limitados",
     "Em gestantes: CONTRAINDICADO itraconazol — usar Anfotericina B desoxicolato IV nas formas graves, "
     "SMX-TMP nas formas leves (após 1º trimestre). "
     "Em formas graves/SNC: Anfotericina B desoxicolato 0,7-1,0 mg/kg/dia IV × 2-4 semanas como indução, "
     "seguida de itraconazol 200 mg/dia de manutenção. "
     "Critério de cura: exames micológicos negativos + normalização de sorologias (dupla difusão, CIE).",
     "A", "I", "PCDT-PARACOC", 2022),

    ("Paracoccidioidomicose",
     "Anfotericina B desoxicolato",
     None,
     "Anfotericina B desoxicolato 0,7-1,0 mg/kg/dia IV em SG 5% (4-6h) × 2-4 semanas (indução)",
     "2–4 semanas IV (indução); seguido de itraconazol 200 mg/dia VO × 12-18 meses",
     "Formas graves com comprometimento de SNC, insuficiência respiratória ou disseminação hematogênica. "
     "Dose cumulativa máxima recomendada ~35 mg/kg para limitar nefrotoxicidade.",
     "Anfotericina B lipossomal 3-5 mg/kg/dia IV (se nefrotoxicidade grave ou IRA prévia)",
     "Não se aplica — resistência à anfotericina B não documentada para Paracoccidioides spp.",
     "Pré-medicação: paracetamol 750 mg + difenidramina 25-50 mg VO 30 min antes de cada infusão. "
     "Reposição profilática de KCl (40-80 mEq/dia) e MgSO4 conforme nível sérico. "
     "Monitorar creatinina diariamente — suspender temporariamente se Cr dobrar do basal.",
     "A", "I", "PCDT-PARACOC", 2022),

    # ══════════════════════════════════════════════════════════════════
    # HISTOPLASMOSE
    # ══════════════════════════════════════════════════════════════════
    ("Histoplasmose",
     "Anfotericina B lipossomal",
     None,
     "Anfotericina B lipossomal 3 mg/kg/dia IV × 14 dias (moderada-grave); "
     "desoxicolato 0,7-1,0 mg/kg/dia IV se lipossomal indisponível",
     "14 dias IV (indução) → consolidação com itraconazol 200 mg 2x/dia VO × 12 semanas "
     "→ manutenção itraconazol 200 mg/dia × ≥12 meses (se HIV/AIDS CD4 < 150)",
     "1ª linha para histoplasmose disseminada moderada-grave (IDSA 2020). "
     "Anfotericina lipossomal preferida por menor nefrotoxicidade. "
     "Itraconazol é 1ª linha para formas leves (200 mg 3x/dia × 3 dias ataque → 200 mg 2x/dia).",
     "Fluconazol 400-800 mg/dia VO (alternativa quando itraconazol indisponível; "
     "eficácia inferior — taxa de resposta ~75% vs 95% do itraconazol)",
     "Não há resistência clinicamente relevante — mecanismo principal de falha é imunossupressão não controlada",
     "HIV/AIDS: iniciar TARV após 2 semanas de tratamento antifúngico para evitar síndrome inflamatória "
     "(IRIS — immune reconstitution inflammatory syndrome). "
     "Manutenção secundária: itraconazol 200 mg/dia até CD4 > 150 células/µL por ≥6 meses em TARV. "
     "Diagnóstico preferencial no Brasil: antigenúria Histoplasma (alta sensibilidade em imunossuprimidos).",
     "A", "I", "SVS-HISTOP", 2022),

    ("Histoplasmose",
     "Itraconazol",
     None,
     "Itraconazol 200 mg 3x/dia VO × 3 dias (ataque), depois 200 mg 2x/dia × 12 semanas (consolidação), "
     "depois 200 mg/dia × ≥ 12 meses (manutenção em HIV/AIDS)",
     "Total: 12 meses ou mais em imunossuprimidos",
     "1ª linha para histoplasmose leve-moderada e como terapia de consolidação/manutenção pós-anfotericina. "
     "IDSA 2020 e SVS Brasil. Monitorar nível sérico (meta: > 1,0 µg/mL).",
     "Fluconazol 400 mg/dia VO — alternativa se itraconazol indisponível (eficácia inferior)",
     "Não se aplica",
     "Tomar com suco de laranja ou cola (pH ácido melhora absorção da cápsula). "
     "Solução oral: tomar em jejum. Monitorar nível sérico quando disponível.",
     "A", "II", "SVS-HISTOP", 2022),

    # ══════════════════════════════════════════════════════════════════
    # CRIPTOCOCOSE
    # ══════════════════════════════════════════════════════════════════
    ("Criptococose",
     "Anfotericina B desoxicolato",
     "Flucitosina (5-FC)",
     "Anfotericina B desoxicolato 0,7-1,0 mg/kg/dia IV + Flucitosina 25 mg/kg 6/6h VO × 14 dias (indução) → "
     "Fluconazol 400 mg/dia VO × 8 semanas (consolidação) → Fluconazol 200 mg/dia × ≥12 meses (manutenção)",
     "Indução 14 dias IV; consolidação 8 semanas; manutenção ≥ 12 meses",
     "Protocolo padrão para criptococose meníngea em HIV/AIDS — PCDT-HIV-FUNG MS 2022. "
     "Combinação anfotericina B + 5-FC reduz mortalidade em 30% vs monoterapia (ensaio ACTA 2018). "
     "Fluconazol 400-800 mg/dia IV/VO disponível no SUS para indução se anfotericina indisponível "
     "(mas inferior à combinação). Manejo de hipertensão intracraniana é fundamental: "
     "PL terapêutica diária se pressão de abertura > 25 cmH2O.",
     "Anfotericina B lipossomal 3-4 mg/kg/dia IV + 5-FC (se disponível) × 14 dias "
     "(em nefrotoxicidade prévia ou IRA em uso de desoxicolato)",
     "Resistência ao fluconazol (CIM ≥ 16 µg/mL): usar voriconazol 200 mg 12/12h VO como consolidação/manutenção; "
     "dados limitados",
     "HIV/AIDS: não iniciar TARV nos primeiros 14 dias — risco de IRIS neurológica fatal. "
     "Iniciar TARV após 4-6 semanas. Meta de CD4 > 100 células/µL × 3-6 meses para descontinuar profilaxia secundária. "
     "5-FC: monitorar hemograma 2×/semana (mielotoxicidade). "
     "Não-HIV (transplantados): mesmo esquema ou anfotericina B lipossomal preferida.",
     "A", "I", "SBI-CRIPTO", 2021),

    ("Criptococose",
     "Fluconazol",
     None,
     "Fluconazol 800 mg/dia IV/VO × 14 dias (indução — se anfotericina B indisponível); "
     "400 mg/dia × 8 semanas (consolidação); 200 mg/dia × ≥12 meses (manutenção)",
     "≥ 12 meses total em HIV/AIDS",
     "Fluconazol em monoterapia para indução: inferior à anfotericina B — usar somente se anfotericina indisponível. "
     "Como consolidação e manutenção: padrão-ouro após indução parenteral.",
     "Itraconazol 200 mg 2x/dia como manutenção (alternativa ao fluconazol se indisponível; "
     "eficácia menor para SNC)",
     "Voriconazol para cepas com resistência ao fluconazol",
     "Suspender profilaxia secundária quando CD4 > 100 células/µL por ≥ 3-6 meses em TARV eficaz. "
     "Em pacientes sem HIV: duração conforme imunossupressão.",
     "A", "II", "SBI-CRIPTO", 2021),

    # ══════════════════════════════════════════════════════════════════
    # CANDIDEMIA / CANDIDOSE INVASIVA
    # ══════════════════════════════════════════════════════════════════
    ("Candidemia",
     "Caspofungina",
     None,
     "Caspofungina 70 mg IV (ataque) no D1; 50 mg/dia IV (manutenção) do D2 em diante. "
     "Step-down para fluconazol 400 mg/dia VO quando: paciente estável, sensível ao fluconazol, "
     "hemocultura negativa × 2",
     "≥ 14 dias após última hemocultura negativa",
     "1ª linha para candidemia em adultos (IDSA 2016, SBI-CAND 2022). "
     "Equinocandinas têm melhor perfil de eficácia/segurança vs fluconazol e anfotericina B. "
     "Retirar CVC se candidemia relacionada a cateter. "
     "Avaliar olhos (fundoscopia) e coração (ecocardiograma) em candidemia persistente.",
     "Anidulafungina 200 mg IV D1 → 100 mg/dia IV (alternativa de 1ª linha equivalente); "
     "Micafungina 100 mg/dia IV (1ª linha equivalente). "
     "Fluconazol 800 mg IV/VO D1 → 400 mg/dia (alternativa em pacientes estáveis sem exposição prévia, "
     "sem C. glabrata/krusei)",
     "C. auris: anfotericina B lipossomal 3-5 mg/kg/dia IV (se resistente a equinocandinas); "
     "isavuconazol (se disponível). Checar susceptibilidade obrigatória. "
     "C. glabrata fluconazol-resistente: manter equinocandina ou anfotericina B",
     "Candida auris: isolamento de contato obrigatório — risco de surto hospitalar. "
     "Notificar CCIH e ANVISA se C. auris identificada. "
     "Fundoscopia em todos os pacientes com candidemia — endoftalmite fúngica em ~1-2% dos casos. "
     "Ecocardiograma se bacteriemia > 5 dias ou válvula protética.",
     "A", "I", "SBI-CAND", 2022),

    ("Candidíase orofaríngea",
     "Fluconazol",
     None,
     "Fluconazol 100-200 mg/dia VO × 7-14 dias",
     "7–14 dias",
     "1ª linha para candidíase orofaríngea — superior à nistatina tópica em imunossuprimidos. "
     "Em HIV/AIDS com CD4 < 200 células/µL: 200 mg/dia × 14 dias. Disponível no SUS.",
     "Nistatina suspensão oral 400.000-600.000 UI 6/6h × 7-14 dias "
     "(para casos leves não imunossuprimidos ou gestantes no 1º trimestre)",
     "Itraconazol solução oral 200 mg/dia × 14 dias (em refratários ao fluconazol — "
     "C. albicans fluconazol-resistente em pacientes com longa exposição ao fluconazol)",
     "HIV/AIDS: manutenção secundária fluconazol 100-200 mg/dia — considerar em CD4 < 50 células/µL "
     "com episódios frequentes (>3/ano). Peso do risco de resistência × benefício.",
     "A", "I", "SBI-CAND", 2022),

    ("Candidíase esofágica",
     "Fluconazol",
     None,
     "Fluconazol 200-400 mg/dia IV ou VO × 14-21 dias",
     "14–21 dias",
     "1ª linha para candidíase esofágica — eficácia >85%. "
     "Iniciar IV se disfagia grave; step-down para oral quando tolerado. "
     "PCDT-HIV-FUNG 2022 recomenda como tratamento de escolha.",
     "Itraconazol solução oral 200 mg/dia × 14-21 dias (alternativa se fluconazol indisponível)",
     "Caspofungina 70 mg D1 → 50 mg/dia IV × 14-21 dias "
     "(refratários ao fluconazol ou C. albicans fluconazol-resistente)",
     "Diagnóstico endoscópico recomendado quando não-HIV ou atípico. "
     "Em HIV: não requer endoscopia se resposta ao fluconazol empírico em 3-5 dias. "
     "Manutenção secundária: considerar em CD4 < 100 e episódios recorrentes.",
     "A", "I", "SBI-CAND", 2022),

    ("Candidíase vaginal",
     "Fluconazol",
     None,
     "Fluconazol 150 mg VO dose única (não complicada); "
     "150 mg × 3 doses em dias alternados (grave ou recorrente)",
     "Dose única; ou 3 doses em dias alternados para recorrente",
     "1ª linha para candidíase vaginal não complicada — eficácia equivalente ao clotrimazol tópico "
     "com maior comodidade posológica. Disponível no SUS.",
     "Clotrimazol creme 2% vaginal × 7 noites ou óvulo 500 mg dose única "
     "(1ª escolha em gestantes — seguro, sem absorção sistêmica)",
     "Fluconazol 150 mg/semana × 6 meses (candidíase recorrente por C. albicans); "
     "ácido bórico vaginal 600 mg/dia × 14 dias (C. glabrata ou não-albicans refratária)",
     "C. glabrata: intrinsecamente menos sensível ao fluconazol — usar nistatina vaginal ou ácido bórico. "
     "Candidíase recorrente (≥4/ano): investigar diabetes, imunossupressão, uso de antibiótico. "
     "Gestantes: evitar fluconazol oral — nistatina ou clotrimazol vaginal × 7-14 dias.",
     "A", "I", "SBI-CAND", 2022),

    # ══════════════════════════════════════════════════════════════════
    # ASPERGILOSE INVASIVA
    # ══════════════════════════════════════════════════════════════════
    ("Aspergilose invasiva",
     "Voriconazol",
     None,
     "Voriconazol 6 mg/kg IV 12/12h × 2 doses (ataque D1); "
     "4 mg/kg IV 12/12h (manutenção D2 em diante). "
     "Step-down: voriconazol 200 mg VO 12/12h quando estável",
     "Mínimo 6–12 semanas; individualizar conforme resposta e imunossupressão",
     "1ª linha para aspergilose invasiva (AI) — IDSA 2016, ECIL 2022, SBI-ASPERG 2019. "
     "Superior à anfotericina B em ensaio randomizado (Herbrecht 2002). "
     "Monitorar nível sérico (vale trough: 1–5,5 µg/mL). "
     "TC de tórax: sinal do halo e sinal do crescente de ar são característicos.",
     "Anfotericina B lipossomal 3-5 mg/kg/dia IV (toxicidade ao voriconazol, hepatopatia grave, "
     "gestação ou polimorfismo CYP2C19 com metabolismo ultrarrápido). "
     "Isavuconazol 200 mg 8/8h × 2 dias (ataque) → 200 mg/dia (manutenção) — alternativa de 1ª linha "
     "com melhor perfil de interações (não disponível no SUS)",
     "Posaconazol 300 mg 12/12h D1 (ataque) → 300 mg/dia VO/IV × 6-12 semanas "
     "(falha ou intolerância ao voriconazol)",
     "Profilaxia em neutropênicos de alto risco e TMO: posaconazol 200 mg 8/8h VO (suspensão) "
     "ou 300 mg/dia (comprimido gastrorresistente). "
     "Diagnóstico: galactomanana sérica/BAL (sensível em neutropênicos); TC de alta resolução "
     "(sinal do halo é específico mas temporário — realizar precocemente). "
     "Aspergillus ABPA: prednisona 0,5-1 mg/kg/dia + itraconazol 200 mg 2x/dia × 4-6 meses.",
     "A", "I", "SBI-ASPERG", 2019),

    ("Aspergilose invasiva",
     "Anfotericina B desoxicolato",
     None,
     "Anfotericina B desoxicolato 1,0-1,5 mg/kg/dia IV × 4-12 semanas",
     "Individualizar — mínimo 4 semanas após controle da neutropenia",
     "Alternativa quando voriconazol indisponível ou contraindicado. "
     "Eficácia inferior ao voriconazol (~35% resposta vs 53%). "
     "Usar somente se voriconazol/lipossomal indisponíveis.",
     "Anfotericina B lipossomal 5 mg/kg/dia IV (menor toxicidade renal — preferida se disponível)",
     "Caspofungina 70 mg D1 → 50 mg/dia IV (falha ou intolerância à anfotericina)",
     "Monitorar função renal diariamente. Hidratação IV com SF 0,9% 500 mL pré-infusão. "
     "Reposição eletrolítica profilática.",
     "B", "II", "SBI-ASPERG", 2019),

    # ══════════════════════════════════════════════════════════════════
    # MUCORMICOSE
    # ══════════════════════════════════════════════════════════════════
    ("Mucormicose",
     "Anfotericina B lipossomal",
     None,
     "Anfotericina B lipossomal 5-10 mg/kg/dia IV + desbridamento cirúrgico precoce e agressivo",
     "Mínimo 4-6 semanas IV; step-down para posaconazol 300 mg/dia VO quando estável",
     "1ª linha — combinação de antifúngico e cirurgia é fundamental; mortalidade >50% sem cirurgia. "
     "Dose 5 mg/kg/dia padrão; alguns protocolos usam 10 mg/kg/dia na forma rhinocerebral. "
     "ESCMID-ECMM 2021.",
     "Anfotericina B desoxicolato 1,0-1,5 mg/kg/dia IV (quando lipossomal indisponível; "
     "nefrotoxicidade limita doses maiores — limitar a 1,5 mg/kg/dia)",
     "Isavuconazol 200 mg 8/8h × 2 dias ataque → 200 mg/dia manutenção (ativo contra Mucorales; "
     "não disponível SUS); Posaconazol 300 mg 12/12h D1 → 300 mg/dia (step-down após anfotericina B)",
     "Controle do fator predisponente é fundamental: controle glicêmico rigoroso em diabéticos "
     "(meta: glicemia < 200 mg/dL), redução de imunossupressão em transplantados, "
     "descontinuar desferroxamina (quelante de ferro — fator de risco). "
     "Desfericrase (catabolismo do ferro): pesquisa ativa em pacientes com cetoacidose diabética + "
     "sinusite necrotizante → biópsia/cultura urgente. "
     "Mucormicose pulmonar pós-COVID-19: descrita no Brasil — investigar em pacientes com "
     "corticoterapia prolongada + hiperglicemia.",
     "A", "II", "SBMT-FUNGOS", 2022),

    # ══════════════════════════════════════════════════════════════════
    # ESPOROTRICOSE
    # ══════════════════════════════════════════════════════════════════
    ("Esporotricose",
     "Itraconazol",
     None,
     "Itraconazol 100-200 mg/dia VO × 3-6 meses (cutânea linfangítica); "
     "200-400 mg/dia × 12-18 meses (osteoarticular); "
     "200 mg/dia pós-anfotericina (disseminada/meníngea)",
     "Cutânea: 3–6 meses; osteoarticular/sistêmica: 12–18 meses",
     "1ª linha para esporotricose cutânea linfangítica e fixada, e manutenção após anfotericina B. "
     "SVS-ESPORO 2020. Sporothrix brasiliensis (endemia RJ) mantém sensibilidade ao itraconazol. "
     "Critério de cura: cicatrização completa de lesões + 4 semanas adicionais.",
     "Iodeto de potássio (KI) solução saturada — 5 gotas 3x/dia (aumentar progressivamente até "
     "40-50 gotas 3x/dia) × 3-6 meses. Alternativa histórica, ainda usada em locais sem itraconazol. "
     "Contraindicado em gestantes, lactentes e tireoidianos",
     "Terbinafina 250-500 mg/dia VO × 3-6 meses (alternativa para refratários ao itraconazol; "
     "evidência de eficácia crescente para S. brasiliensis)",
     "Anfotericina B desoxicolato 0,7-1,0 mg/kg/dia IV × 2-4 semanas para formas disseminadas "
     "e meníngeas (e em HIV/AIDS com CD4 < 200). "
     "Endemia Rio de Janeiro (Sporothrix brasiliensis via gato doméstico): maior virulência — "
     "investigar contato com gatos. Notificação compulsória semanal no Brasil.",
     "A", "II", "SVS-ESPORO", 2020),

    # ══════════════════════════════════════════════════════════════════
    # DERMATOFITOSES — TINEA CAPITIS
    # ══════════════════════════════════════════════════════════════════
    ("Tinea capitis",
     "Terbinafina",
     None,
     "Terbinafina: < 20 kg: 62,5 mg/dia; 20-40 kg: 125 mg/dia; > 40 kg: 250 mg/dia VO × 4-8 semanas",
     "4–8 semanas (Trichophyton); 8–12 semanas (Microsporum)",
     "1ª linha para tinea capitis por Trichophyton (T. tonsurans, T. violaceum) — SBD 2021. "
     "Griseofulvina ainda usada para Microsporum canis (M. canis tem CIM mais baixa para griseofulvina). "
     "Terbinafina: menos eficaz contra Microsporum — considerar griseofulvina para este dermatófito.",
     "Griseofulvina 10-20 mg/kg/dia VO × 6-12 semanas com alimento gorduroso "
     "(preferida para M. canis; disponível no SUS; alternativa histórica eficaz). "
     "Itraconazol 5 mg/kg/dia × 4-6 semanas (alternativa a ambas)",
     "Sem resistência clinicamente relevante documentada no Brasil — falha geralmente por má adesão",
     "Shampoo antifúngico adjuvante (cetoconazol 2% ou sulfeto de selênio 2,5%) para reduzir "
     "transmissão — não substitui tratamento oral. Tratar contactantes assintomáticos com shampoo. "
     "Não é necessário rapar o cabelo. Tinea capitis é notificável em surtos escolares.",
     "A", "II", "SBD-MICOSES", 2021),

    # ══════════════════════════════════════════════════════════════════
    # TINEA UNGUIUM (ONICOMICOSE)
    # ══════════════════════════════════════════════════════════════════
    ("Tinea unguium",
     "Terbinafina",
     None,
     "Terbinafina 250 mg/dia VO × 12 semanas (unhas do pé); × 6 semanas (unhas da mão)",
     "6 semanas (mão); 12 semanas (pé)",
     "1ª linha para onicomicose dermatofítica — taxas de cura micológica ~70-80% para unhas do pé. "
     "Superior ao itraconazol em pulso para T. rubrum (principal dermatófito no Brasil). "
     "SBD 2021.",
     "Itraconazol pulso: 200 mg 12/12h × 7 dias/mês × 2 pulsos (mão) ou 3-4 pulsos (pé); "
     "eficácia semelhante com menor duração de tratamento",
     "Ciclopirox esmalte 8% × 12 meses (alternativa tópica para formas leves sem acometimento "
     "da lúnula — taxa de cura ~30-35%)",
     "Confirmar diagnóstico micológico (exame direto + cultura) antes de tratamento sistêmico "
     "prolongado. Condições simuladoras: psoríase ungueal, líquen plano, trauma repetitivo. "
     "Taxa de recidiva alta (25-40%) — prevenir com higiene dos pés e calçados abertos.",
     "A", "I", "SBD-MICOSES", 2021),

    # ══════════════════════════════════════════════════════════════════
    # TINEA PEDIS / CORPORIS / CRURIS
    # ══════════════════════════════════════════════════════════════════
    ("Tinea pedis",
     "Clotrimazol",
     None,
     "Clotrimazol creme 1% aplicação fina 12/12h × 2-4 semanas; "
     "continuar 1-2 semanas após resolução clínica",
     "2–4 semanas",
     "1ª linha para tinea pedis, tinea corporis e tinea cruris não complicadas — terapia tópica eficaz. "
     "Disponível no SUS. Cetoconazol 2% e miconazol 2% são alternativas equivalentes.",
     "Terbinafina creme 1% 1-2x/dia × 1-2 semanas (tinea pedis interespacial — alta eficácia)",
     "Terbinafina 250 mg/dia VO × 2-4 semanas (casos extensos, hiperceratóticos ou recorrentes)",
     "Tinea pedis vesicular aguda: cursos curtos de corticosteroide tópico de baixa potência podem "
     "aliviar prurido intenso (adjuvante nos primeiros 5 dias). "
     "Higiene dos pés, calçados respiráveis e pó antifúngico previnem recidiva.",
     "A", "I", "SBD-MICOSES", 2021),

    # ══════════════════════════════════════════════════════════════════
    # PITIRÍASE VERSICOLOR
    # ══════════════════════════════════════════════════════════════════
    ("Pitiríase versicolor",
     "Cetoconazol",
     None,
     "Cetoconazol xampu 2%: aplicar no tronco × 3-5 min, enxaguar, diariamente × 2 semanas; "
     "OU cetoconazol creme 2% × 2-4 semanas; "
     "OU fluconazol 300 mg/semana × 2 semanas VO (casos extensos/recorrentes)",
     "2–4 semanas tópico; 2 semanas oral",
     "Malassezia furfur/globosa. Cetoconazol tópico: 1ª linha por disponibilidade no SUS e eficácia. "
     "Hipopigmentação pós-infecção pode persistir por meses após cura micológica. "
     "SBD 2021.",
     "Selenium dissulfeto xampu 2,5% × 10 min antes do banho × 2 semanas (alternativa barata e eficaz)",
     "Fluconazol 400 mg dose única (alternativa oral para recorrência frequente — evidência moderada)",
     "Alta taxa de recidiva (60-80% em 2 anos) no Brasil (clima quente e úmido). "
     "Profilaxia com cetoconazol xampu 1×/semana durante verão em pacientes com recidivas frequentes. "
     "Orientar: exposição solar pós-tratamento acelera repigmentação.",
     "A", "II", "SBD-MICOSES", 2021),

    # ══════════════════════════════════════════════════════════════════
    # CROMOBLASTOMICOSE
    # ══════════════════════════════════════════════════════════════════
    ("Cromoblastomicose",
     "Itraconazol",
     "Flucitosina (5-FC)",
     "Itraconazol 200-400 mg/dia VO × 12-24 meses (formas leves-moderadas); "
     "Itraconazol 400 mg/dia + Flucitosina 150 mg/kg/dia × 12-18 meses (formas extensas)",
     "12–24 meses; formas extensas até resolução completa",
     "1ª linha para cromoblastomicose — tratamento longo e desafiador. "
     "Taxa de cura varia de 15-80% dependendo da extensão e agente. "
     "Fonsecaea pedrosoi é o agente mais comum no Brasil. SBD 2021.",
     "Terbinafina 500-1000 mg/dia VO × 12-24 meses (alternativa eficaz, especialmente para "
     "Rhinocladiella aquaspersa e algumas cepas de F. pedrosoi)",
     "Voriconazol 200 mg 12/12h VO (casos refratários — evidência crescente)",
     "Adjuvantes: termoterapia local (bolsa de água quente 42-45°C × 20-30 min/dia) — "
     "Fonsecaea não tolera temperatura > 40°C; criocirurgia, laser CO2 ou ressecção cirúrgica "
     "para lesões pequenas e isoladas. "
     "Notificar ao serviço de dermatologia de referência. Doença ocupacional (trabalhadores rurais — "
     "pés e pernas geralmente acometidos por espinhos e farpas de madeira).",
     "B", "III", "SBD-MICOSES", 2021),

    # ══════════════════════════════════════════════════════════════════
    # PNEUMOCISTOSE (PCP)
    # ══════════════════════════════════════════════════════════════════
    ("Pneumocistose",
     "Sulfametoxazol + Trimetoprima",
     None,
     "SMX 75-100 mg/kg/dia + TMP 15-20 mg/kg/dia IV ou VO dividido em 3-4 doses × 21 dias. "
     "Adjuvante: prednisona 40 mg 12/12h VO × 5 dias → 40 mg/dia × 5 dias → 20 mg/dia × 11 dias "
     "(se PaO2 < 70 mmHg ou gradiente A-a O2 > 35 mmHg)",
     "21 dias",
     "1ª linha para pneumocistose — PCDT-HIV-FUNG 2022. "
     "Corticosteroide adjuvante reduz mortalidade em hipoxemia grave (meta-análise). "
     "IV se PaO2 < 70 mmHg ou SpO2 < 92%; VO se leve-moderada. "
     "Pneumocystis jirovecii: não cultiva in vitro — diagnóstico por PCR, imunofluorescência no LBA.",
     "Pentamidina isetionato 4 mg/kg/dia IV × 21 dias "
     "(alergia grave ao SMX-TMP — síndrome de Stevens-Johnson, anafilaxia; ou falha terapêutica). "
     "Atovaquona 750 mg VO 12/12h × 21 dias (forma leve-moderada; indisponível no SUS)",
     "Não há resistência documentada ao SMX-TMP — falha geralmente por imunossupressão grave, "
     "dose inadequada ou diagnóstico tardio",
     "Profilaxia primária: SMX-TMP 800/160 mg 3×/semana (ou 1 cp/dia) — indicado em HIV com "
     "CD4 < 200 células/µL, transplantados em imunossupressão intensa, uso prolongado de "
     "corticosteroide (prednisona > 20 mg/dia × > 4 semanas). "
     "Suspender profilaxia quando CD4 > 200 células/µL × 3 meses em TARV. "
     "TARV: iniciar após 2 semanas de tratamento de PCP para evitar IRIS.",
     "A", "I", "PCDT-HIV-FUNG", 2022),

    # ══════════════════════════════════════════════════════════════════
    # FUSARIOSE
    # ══════════════════════════════════════════════════════════════════
    ("Fusariose",
     "Voriconazol",
     None,
     "Voriconazol 6 mg/kg IV 12/12h × 2 doses ataque → 4 mg/kg IV 12/12h manutenção. "
     "Step-down para VO 200 mg 12/12h quando estável",
     "Até reconstituição imune (neutropenia resolvida e imunossupressão reduzida)",
     "1ª linha para fusariose invasiva — ESCMID 2014. "
     "Fusarium solani complex: CIM mais elevada ao voriconazol. "
     "Associar G-CSF (fator estimulante de colônia) para acelerar recuperação da neutropenia. "
     "Reduzir imunossupressão o máximo possível.",
     "Anfotericina B lipossomal 5-10 mg/kg/dia IV (alternativa em insuficiência renal ou "
     "intolerância ao voriconazol; Fusarium solani tem CIM elevada para anfotericina B desoxicolato)",
     "Combinação voriconazol + anfotericina B lipossomal (casos refratários — evidência limitada)",
     "Prognóstico reservado — mortalidade >50% em neutropênicos. "
     "Diagnóstico: hemocultura positiva em ~50% (diferente de Aspergillus — hemoculturas sempre negativas). "
     "Lesões cutâneas equimóticas/necróticas características — biópsia diagnóstica. "
     "Tratamento local de lesões fúngicas oculares se endoftalmite.",
     "B", "II", "SBI-ASPERG", 2019),

    # ══════════════════════════════════════════════════════════════════
    # LOBOMICOSE (LACAZIOSE)
    # ══════════════════════════════════════════════════════════════════
    ("Lobomicose",
     "Nenhum antifúngico sistêmico estabelecido",
     None,
     "Ressecção cirúrgica ampla (principal tratamento) + criocirurgia para lesões menores",
     "Conforme extensão das lesões — tratamento cirúrgico múltiplo frequentemente necessário",
     "Lacazia loboi (= Loboa loboi): agente não cultivável — sem tratamento farmacológico estabelecido. "
     "Cirurgia com margem ampla é o único tratamento comprovado. "
     "Endemia Amazônica — trabalhadores rurais e pescadores. "
     "SBD 2021.",
     "Clofazimina 200 mg/dia VO + itraconazol 200 mg/dia VO × 12 meses "
     "(regime experimental com respostas parciais relatadas — não há evidência de alta qualidade)",
     "Não se aplica (ausência de tratamento farmacológico padrão)",
     "Doença de notificação compulsória no Brasil (MS 2020). "
     "CID-10: B48.0. Endemia em estados amazônicos: AM, PA, AC, RO, RR, AP. "
     "Verificar exposição a rios, igarapés e vegetação tropical. "
     "Lesões queloidiformes características — diagnóstico histopatológico com corpos de Medlar. "
     "Não há transmissão interhumana. Zoonose em botos (Inia geoffrensis).",
     "C", "III", "SBD-MICOSES", 2021),

    # ══════════════════════════════════════════════════════════════════
    # MICETOMA FÚNGICO (EUMICETOMA)
    # ══════════════════════════════════════════════════════════════════
    ("Micetoma fúngico",
     "Itraconazol",
     None,
     "Itraconazol 400 mg/dia VO × 12-24 meses (eumicetoma branco por Madurella, Acremonium); "
     "associado à excisão cirúrgica quando viável",
     "12–24 meses; casos extensos indefinidamente",
     "Eumicetoma (grãos negros/brancos): itraconazol é o antifúngico mais utilizado. "
     "Mycetoma branco: resposta moderada. Mycetoma negro (M. mycetomatis): resposta limitada. "
     "SBD/SBMT 2021.",
     "Voriconazol 200 mg 12/12h VO (alternativa para M. mycetomatis e casos refratários — "
     "evidência crescente)",
     "Combinação itraconazol + terbinafina (casos refratários — regime experimental)",
     "Diagnóstico: grãos na secreção (aspecto macroscópico orienta etiologia — grãos negros = "
     "eumicetoma por Madurella; grãos brancos/amarelos = actinomicetoma bacteriano). "
     "RX/RNM: destruição óssea guia extensão cirúrgica. "
     "Actinomicetoma (Nocardia, Actinomadura): tratamento com SMX-TMP ou amicacina (não antifúngico). "
     "Diagnóstico diferencial crítico entre ato eumicetoma e actinomicetoma.",
     "B", "III", "SBMT-FUNGOS", 2022),

    # ══════════════════════════════════════════════════════════════════
    # FEOHIFOMICOSE
    # ══════════════════════════════════════════════════════════════════
    ("Feohifomicose",
     "Voriconazol",
     None,
     "Voriconazol 200-300 mg VO/IV 12/12h × 6-12 meses + excisão cirúrgica quando possível",
     "6–12 meses ou até resolução clínica e radiológica",
     "Feohifomicose cerebral (Rhinocladiella mackenziei, Exophiala dermatitidis) e sistêmica: "
     "voriconazol é 1ª linha. Mortalidade elevada nas formas cerebrais. ESCMID 2014.",
     "Itraconazol 400 mg/dia VO × 12 meses (formas cutâneas e subcutâneas menos graves)",
     "Posaconazol 400 mg 12/12h VO (casos refratários ao voriconazol)",
     "Excisão cirúrgica ampla é componente essencial do tratamento nas formas nodulares subcutâneas. "
     "Formas cerebrais: prognóstico muito grave — drenagem neurocirúrgica + voriconazol. "
     "Reduzir imunossupressão quando possível.",
     "B", "III", "SBMT-FUNGOS", 2022),

    # ══════════════════════════════════════════════════════════════════
    # CANDIDOSE INVASIVA EM NEONATOS
    # ══════════════════════════════════════════════════════════════════
    ("Candidemia neonatal",
     "Anfotericina B desoxicolato",
     None,
     "Anfotericina B desoxicolato 0,5-1,0 mg/kg/dia IV × ≥14 dias após última hemocultura negativa",
     "≥ 14 dias após hemocultura negativa",
     "1ª linha para candidemia neonatal em muitos serviços brasileiros — ampla disponibilidade no SUS. "
     "Fluconazol 6-12 mg/kg/dia IV/VO como alternativa em neonatos estáveis sem exposição prévia.",
     "Fluconazol 12 mg/kg/dia IV × 14 dias após hemocultura negativa "
     "(alternativa em neonatos estáveis, CD sem profilaxia prévia com fluconazol, Candida sensível)",
     "Micafungina 10 mg/kg/dia IV (neonatos prematuros com peso < 1 kg ou candidemia persistente)",
     "Profilaxia com fluconazol 3-6 mg/kg/semana × 6 semanas em RNPT < 1000g ou < 28 semanas de IG "
     "em UTINs com incidência > 2% — reduz candidemia neonatal (ESCMID/ESPID 2016). "
     "Fundoscopia obrigatória. Ecocardiograma se candidemia persistente (Candida endocarditis). "
     "Retirar CVC e sonda urinária se possível.",
     "A", "II", "SBI-CAND", 2022),

    # ══════════════════════════════════════════════════════════════════
    # TRATAMENTOS FALTANTES
    # ══════════════════════════════════════════════════════════════════
    (
        "Aspergiloma Pulmonar",
        "Voriconazol",
        None,
        "Assintomático: observação clínica sem antifúngico. Sintomático (hemoptise leve-moderada): "
        "Voriconazol 6 mg/kg IV 12/12h D1 depois 4 mg/kg IV 12/12h ou 200 mg VO 12/12h × 3–6 meses. "
        "Hemoptise grave: embolização arterial brônquica ou ressecção cirúrgica.",
        "3–6 meses (médico) / definitivo (cirúrgico)",
        "Aspergiloma é 'bola fúngica' em cavidade pulmonar preexistente — Aspergillus não invade tecido. "
        "Cirurgia é o único tratamento curativo mas tem alta morbimortalidade em pacientes com doença pulmonar grave. "
        "Antifúngico reduz carga fúngica e sintomas mas raramente erradica.",
        "Itraconazol 200 mg VO 12/12h × 3–6 meses — alternativa oral de menor custo",
        "Anfotericina B inalatória (uso compassivo em hemoptise refratária sem condições cirúrgicas)",
        "Tuberculose prévia é o principal fator de risco no Brasil. "
        "Instilação intracavitária de anfotericina B guiada por TC pode ser tentada em casos selecionados.",
        "B", "II", "SBI-ASPERG", 2022
    ),
    (
        "Aspergilose Broncopulmonar Alérgica (ABPA)",
        "Itraconazol",
        "+ Prednisona",
        "Prednisona 0,5 mg/kg/dia VO × 2 semanas, depois 0,5 mg/kg em dias alternados × 8 semanas, "
        "redução gradual. Itraconazol 200 mg VO 12/12h × 16 semanas (reduz necessidade de corticoide).",
        "16 semanas (fase aguda) + manutenção conforme resposta",
        "ABPA é resposta imunológica exagerada a Aspergillus em asmáticos e fibrose cística — "
        "não é infecção invasiva. Combinação corticoide + antifúngico reduz exacerbações e preserva função pulmonar.",
        "Voriconazol 200 mg VO 12/12h × 16 semanas — intolerância ou falha ao itraconazol",
        "Posaconazol 300 mg VO 24/24h — ABPA refratária em fibrose cística",
        "Monitorar níveis séricos de itraconazol (alvo: > 1 mg/L). IgE total e IgE específica anti-Aspergillus "
        "são marcadores de atividade. Broncodilatadores e fisioterapia respiratória são coadjuvantes essenciais.",
        "A", "I", "SBI-ASPERG", 2022
    ),
    (
        "Rinossinusite Fúngica",
        "Anfotericina B lipossomal",
        None,
        "Invasiva aguda (mucormicose/aspergilose): Anfotericina B lipossomal 5–10 mg/kg/dia IV + "
        "DESBRIDAMENTO CIRÚRGICO AGRESSIVO imediato + controle do fator predisponente (DM, imunossupressão). "
        "Alérgica: Itraconazol 200 mg VO 12/12h × 3–6 meses + corticoide tópico nasal.",
        "Invasiva: mínimo 4–6 semanas IV / Alérgica: 3–6 meses",
        "Rinossinusite fúngica invasiva (especialmente mucormicose) tem mortalidade > 50% — "
        "cirurgia é o pilar terapêutico e deve preceder ou acompanhar antifúngico. "
        "Forma alérgica é não-invasiva e responde a antifúngico oral.",
        "Voriconazol 6 mg/kg IV 12/12h D1 depois 4 mg/kg IV 12/12h — invasiva por Aspergillus",
        "Posaconazol 300 mg IV/VO 24/24h — terapia de resgate em mucormicose refratária",
        "Mucormicose nasal-orbital-cerebral é emergência — mobilizar cirurgia em < 24h. "
        "Controle glicêmico rígido (DM) e redução de imunossupressão são fundamentais. "
        "Oxigenoterapia hiperbárica pode ser coadjuvante em centros especializados.",
        "A", "II", "SBI-ASPERG", 2022
    ),
    (
        "Dermatofitose Ungueal e Cutânea por Tricofíton",
        "Terbinafina",
        None,
        "Ungueal (onicomicose): Terbinafina 250 mg VO 24/24h × 6 semanas (mãos) ou 12 semanas (pés). "
        "Cutânea (tinea manum/barbae): Terbinafina 250 mg VO 24/24h × 2–4 semanas ou "
        "Terbinafina creme 1% tópico 12/12h × 2–4 semanas.",
        "6–12 semanas (ungueal) / 2–4 semanas (cutânea)",
        "Terbinafina é fungicida contra dermatófitos — taxas de cura micológica > 70% na onicomicose. "
        "Superior ao itraconazol em eficácia e custo-benefício para dermatofitoses.",
        "Itraconazol 200 mg VO 12/12h × 7 dias/mês (pulsoterapia) × 2 meses (mãos) ou 3 meses (pés)",
        "Fluconazol 150–300 mg VO 1×/semana × 3–6 meses — alternativa quando outros indisponíveis",
        "Confirmação micológica (cultura ou PCR) antes de tratar onicomicose. "
        "Evitar esmaltes e calçados fechados úmidos. Taxa de recidiva alta — higiene e prevenção essenciais. "
        "Amorolfina laca ungueal 5% pode ser associada ao tratamento sistêmico.",
        "A", "I", "SBD-MICOSES", 2022
    ),
    (
        "Tinea Corporis, Cruris e Faciei",
        "Clotrimazol",
        None,
        "Lesões localizadas: Clotrimazol creme 1% tópico 12/12h × 2–4 semanas ou "
        "Terbinafina creme 1% tópico 24/24h × 1–2 semanas. "
        "Lesões extensas/recidivantes: Terbinafina 250 mg VO 24/24h × 2–4 semanas.",
        "2–4 semanas (tópico) / 2–4 semanas (sistêmico)",
        "Tinea corporis/cruris são superficiais e respondem bem a antifúngicos tópicos azólicos ou alilaminas. "
        "Terbinafina tópica tem menor tempo de tratamento por ser fungicida. "
        "Tratamento sistêmico reservado para casos extensos ou refratários.",
        "Miconazol creme 2% tópico 12/12h × 2–4 semanas — alternativa de baixo custo",
        "Itraconazol 100 mg VO 24/24h × 2 semanas — refratário ao tópico",
        "Evitar corticosteroide tópico isolado — agrava o quadro (tinea incógnita). "
        "Tinea cruris: tratar tinea pedis associada para evitar reinfecção. "
        "Roupas largas e secas reduzem recidiva.",
        "A", "I", "SBD-MICOSES", 2022
    ),
    (
        "Pneumonia por Pneumocystis jirovecii (PCP)",
        "Sulfametoxazol-trimetoprima (SMX-TMP)",
        None,
        "SMX-TMP 15–20 mg/kg/dia (componente TMP) IV ou VO dividido em 3–4 doses × 21 dias. "
        "PaO2 < 70 mmHg ou gradiente A-a > 35 mmHg: associar Prednisona 40 mg VO 12/12h × 5 dias → "
        "40 mg/dia × 5 dias → 20 mg/dia × 11 dias.",
        "21 dias",
        "SMX-TMP é o tratamento padrão-ouro para PCP desde os anos 1980 — taxa de sucesso > 85%. "
        "Corticoide adjuvante reduz mortalidade em casos moderados-graves (PaO2 < 70 mmHg). "
        "PCP é infecção oportunista definidora de AIDS — investigar HIV em todo caso.",
        "Pentamidina 4 mg/kg/dia IV × 21 dias — intolerância grave a SMX-TMP (hipersensibilidade, "
        "citopenias graves, insuficiência renal grave)",
        "Atovaquona 750 mg VO 12/12h × 21 dias — forma leve-moderada com intolerância a SMX-TMP",
        "Profilaxia primária com SMX-TMP 400/80 mg VO 24/24h quando CD4 < 200/mm³ em PVHIV. "
        "Profilaxia secundária obrigatória após episódio até CD4 > 200/mm³ por > 3 meses com TARV.",
        "A", "I", "PCDT-HIV", 2022
    ),
]

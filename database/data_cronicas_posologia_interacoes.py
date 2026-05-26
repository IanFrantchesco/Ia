"""
Dados de posologia e interações medicamentosas para doenças crônicas.
Fontes: PCDTs MS, SBC, SBD, SBR, ABN, CFM, INCA — edições vigentes até 2025.

POSOLOGIA_CRONICA:
Formato: (medicamento_nome, pat_substr, populacao, dose_unitaria, frequencia, via,
          duracao_texto, aj_renal, aj_hep, meta_terapeutica, observacoes, fonte_sigla)

INTERACOES_MEDICAMENTOS_CRONICOS:
Formato: (medicamento_nome, medicamento_interagente, classe_interagente,
          mecanismo, gravidade, efeito_clinico, conduta, fonte_sigla)

Gravidade: 'contraindicada' | 'grave' | 'moderada' | 'leve'
"""

# =============================================================================
# POSOLOGIA_CRONICA
# =============================================================================
# Campos:
#  0  medicamento_nome
#  1  pat_substr           (patologia/indicação — substring de busca ou None)
#  2  populacao            ('adulto' | 'pediatrico' | 'gestante' | 'idoso' | 'adulto/idoso')
#  3  dose_unitaria
#  4  frequencia
#  5  via                  ('oral' | 'sc' | 'iv' | 'im' | 'inalatoria' | 'topica')
#  6  duracao_texto        (texto livre; 'uso_continuo' para crônicos indefinidos)
#  7  aj_renal             (True se necessário ajuste renal)
#  8  aj_hep               (True se necessário ajuste hepático)
#  9  meta_terapeutica
# 10  observacoes
# 11  fonte_sigla

POSOLOGIA_CRONICA = [

    # ══════════════════════════════════════════════════════════════════════
    # CARDIOVASCULAR — HAS / ICC / DISLIPIDEMIA / SCA / ANGINA
    # ══════════════════════════════════════════════════════════════════════

    ("Enalapril", "Hipertensão Arterial",
     "adulto",
     "5–20 mg",        "1–2x/dia",        "oral",
     "uso_continuo",
     True, False,
     "PA < 130/80 mmHg",
     "Dose máxima 40 mg/dia. Reduzir dose inicial para 2,5 mg se TFGe < 30 mL/min/1,73m². "
     "Monitorar K+ e creatinina nas primeiras 2–4 semanas. Tosse seca em ~15% dos casos.",
     "SBC-HAS"),

    ("Enalapril", "Insuficiência Cardíaca com FE reduzida",
     "adulto",
     "2,5–10 mg",       "2x/dia",          "oral",
     "uso_continuo",
     True, False,
     "Redução de mortalidade; dose-alvo 10 mg 2x/dia",
     "Iniciar com 2,5 mg 2x/dia; titular a cada 2 semanas conforme tolerância e PA. "
     "Suspender se K+ > 5,5 mEq/L ou creatinina aumentar > 30%.",
     "SBC-ICC"),

    ("Losartana", "Hipertensão Arterial",
     "adulto",
     "50–100 mg",       "1x/dia",          "oral",
     "uso_continuo",
     False, False,
     "PA < 130/80 mmHg",
     "Não requer ajuste renal, porém monitorar K+ em DRC. Alternativa para pacientes intolerantes "
     "ao IECA por tosse. Dose máxima 100 mg/dia. Efeito máximo em 3–6 semanas.",
     "SBC-HAS"),

    ("Losartana", "Nefropatia diabética / DRC",
     "adulto",
     "50–100 mg",       "1x/dia",          "oral",
     "uso_continuo",
     False, False,
     "Reduzir proteinúria; retardar progressão da DRC",
     "Meta proteinúria < 0,5 g/dia. Monitorar K+ e TFGe a cada 3 meses. "
     "Combinação IECA + BRA é contraindicada (risco de hipercalemia e IRA).",
     "SBC-HAS"),

    ("Metoprolol succinato", "Insuficiência Cardíaca com FE reduzida",
     "adulto",
     "12,5–200 mg",     "1x/dia",          "oral",
     "uso_continuo",
     False, True,
     "FC repouso 55–65 bpm; melhora FEVE",
     "Iniciar com 12,5–25 mg/dia; dobrar a dose a cada 2 semanas se tolerado. "
     "Dose-alvo 200 mg/dia. Não suspender abruptamente. Usar com cautela em broncoespasmo.",
     "SBC-ICC"),

    ("Metoprolol succinato", "Hipertensão Arterial",
     "adulto",
     "50–200 mg",       "1x/dia",          "oral",
     "uso_continuo",
     False, True,
     "PA < 130/80 mmHg; FC 55–70 bpm",
     "Comprimido de liberação prolongada — não partir nem mastigar. "
     "Broncoespasmo: usar com cautela; preferir betabloqueador cardioseletivo.",
     "SBC-HAS"),

    ("Carvedilol", "Insuficiência Cardíaca com FE reduzida",
     "adulto",
     "3,125–25 mg",     "2x/dia",          "oral",
     "uso_continuo",
     False, True,
     "Redução de mortalidade; dose-alvo 25 mg 2x/dia (50 mg se ≥ 85 kg)",
     "Iniciar 3,125 mg 2x/dia com alimento; dobrar a cada 2 semanas conforme tolerância. "
     "Tomar com refeição para reduzir hipotensão ortostática. Não é cardioseletivo.",
     "SBC-ICC"),

    ("Anlodipino", "Hipertensão Arterial",
     "adulto",
     "5–10 mg",         "1x/dia",          "oral",
     "uso_continuo",
     False, True,
     "PA < 130/80 mmHg",
     "Não requer ajuste renal. Ajuste hepático em insuficiência grave: iniciar 2,5 mg. "
     "Edema periférico dose-dependente (~10% com 10 mg). Meia-vida longa (~35–50h).",
     "SBC-HAS"),

    ("Anlodipino", "Angina estável crônica",
     "adulto",
     "5–10 mg",         "1x/dia",          "oral",
     "uso_continuo",
     False, True,
     "Redução de episódios anginosos",
     "Dose inicial 5 mg; aumentar para 10 mg conforme tolerância. "
     "Pode associar a betabloqueador. Contraindicado em choque cardiogênico.",
     "SBC-HAS"),

    ("Hidroclorotiazida", "Hipertensão Arterial",
     "adulto",
     "12,5–25 mg",      "1x/dia (manhã)",  "oral",
     "uso_continuo",
     True, False,
     "PA < 130/80 mmHg",
     "Evitar doses > 25 mg por efeitos metabólicos (hipocalemia, hiperglicemia, hiperuricemia). "
     "Ineficaz se TFGe < 30 mL/min/1,73m². Monitorar eletrólitos a cada 3–6 meses.",
     "SBC-HAS"),

    ("Espironolactona", "Insuficiência Cardíaca com FE reduzida",
     "adulto",
     "25–50 mg",        "1x/dia",          "oral",
     "uso_continuo",
     True, False,
     "Redução de mortalidade; K+ 4,0–5,0 mEq/L",
     "Iniciar 25 mg/dia; aumentar para 50 mg se tolerado. Contraindicada se K+ > 5,0 mEq/L "
     "ou TFGe < 30. Monitorar K+ e creatinina após 1 semana e mensalmente nos primeiros 3 meses.",
     "SBC-ICC"),

    ("Espironolactona", "Hiperaldosteronismo primário",
     "adulto",
     "100–400 mg",      "1–2x/dia",        "oral",
     "uso_continuo",
     True, False,
     "Normalização de K+ e PA",
     "Dose de manutenção individualizada após controle. Ginecomastia é efeito adverso frequente "
     "em homens; considerar eplerenona como alternativa.",
     "SBC-HAS"),

    ("Furosemida", "Insuficiência Cardíaca descompensada / congestão",
     "adulto",
     "20–80 mg",        "1–2x/dia",        "oral",
     "conforme resposta clínica",
     True, False,
     "Alívio de congestão; diurese adequada",
     "Em DRC doses maiores necessárias (até 200–400 mg/dia). IV: 40–120 mg/dose. "
     "Monitorar K+, Na+, função renal. Evitar depleção excessiva.",
     "SBC-ICC"),

    ("Atorvastatina", "Dislipidemia de alto risco / prevenção secundária",
     "adulto",
     "40–80 mg",        "1x/dia (noturna)", "oral",
     "uso_continuo",
     False, True,
     "LDL < 70 mg/dL (alto risco) / < 50 mg/dL (muito alto risco)",
     "Tomar preferencialmente à noite (maior síntese hepática do colesterol). "
     "Monitorar CPK se mialgia. TGO/TGP na introdução; repetir se sintomas hepáticos. "
     "Contraindicada em gestação.",
     "SBC-DISLIPID"),

    ("Atorvastatina", "Dislipidemia de risco moderado/baixo",
     "adulto",
     "10–20 mg",        "1x/dia (noturna)", "oral",
     "uso_continuo",
     False, True,
     "LDL < 130 mg/dL (risco moderado) / redução ≥ 30%",
     "Iniciar com dose baixa e titular conforme resposta lipídica em 4–8 semanas.",
     "SBC-DISLIPID"),

    ("Sinvastatina", "Dislipidemia",
     "adulto",
     "20–40 mg",        "1x/dia (noturna)", "oral",
     "uso_continuo",
     False, True,
     "LDL < 100 mg/dL (risco moderado)",
     "Dose máxima 40 mg/dia (doses maiores aumentam risco de miopatia). "
     "Metabolizada por CYP3A4; evitar com inibidores potentes (azólicos, amiodarona, ciclosporina). "
     "Contraindicada em gestação.",
     "SBC-DISLIPID"),

    ("AAS", "Prevenção secundária — DAC / AVC / Doença arterial periférica",
     "adulto",
     "100 mg",          "1x/dia",          "oral",
     "uso_continuo",
     False, False,
     "Prevenção de eventos aterotrombóticos",
     "Tomar com alimentos para reduzir irritação gástrica. Considerar IBP se alto risco de úlcera. "
     "Não suspender abruptamente em coronariopatas.",
     "SBC-SCA"),

    ("Clopidogrel", "Pós-SCA / Pós-intervenção coronária percutânea",
     "adulto",
     "75 mg",           "1x/dia",          "oral",
     "12 meses (pós-SCA); uso_continuo se intolerância ao AAS",
     False, True,
     "Prevenção de eventos aterotrombóticos",
     "Pós-SCA: manter 12 meses em terapia dupla com AAS. Metabolização via CYP2C19 "
     "(inibidores como omeprazol podem reduzir ativação — preferir pantoprazol). "
     "Teste genômico pode identificar metabolizadores lentos.",
     "SBC-SCA"),

    ("Rivaroxabana", "Fibrilação atrial não valvar (anticoagulação)",
     "adulto",
     "20 mg",           "1x/dia (com refeição noturna)", "oral",
     "uso_continuo",
     True, True,
     "Prevenção de AVC e embolismo sistêmico; escore CHA₂DS₂-VASc ≥ 2",
     "Tomar com a refeição principal do jantar (aumenta biodisponibilidade). "
     "Reduzir para 15 mg/dia se ClCr 15–49 mL/min. Contraindicado se ClCr < 15 mL/min. "
     "Não necessita monitoração rotineira de coagulação.",
     "SBC-SCA"),

    ("Rivaroxabana", "TVP / TEP (tratamento e profilaxia)",
     "adulto",
     "15 mg",           "2x/dia × 21 dias, depois 20 mg 1x/dia", "oral",
     "mínimo 3 meses; avaliar extensão e fator de risco",
     True, True,
     "Tratamento e prevenção de recorrência de TVEP",
     "Fase inicial (15 mg 2x/dia × 21d) deve ser tomada com alimentos. "
     "Profilaxia estendida: 10 mg/dia. Contraindicado em gestação.",
     "SBC-SCA"),

    ("Apixabana", "Fibrilação atrial não valvar (anticoagulação)",
     "adulto",
     "5 mg",            "2x/dia",          "oral",
     "uso_continuo",
     True, True,
     "Prevenção de AVC; escore CHA₂DS₂-VASc ≥ 2",
     "Reduzir para 2,5 mg 2x/dia se ≥ 2 dos critérios: idade ≥ 80 anos, peso ≤ 60 kg, "
     "creatinina ≥ 1,5 mg/dL. Contraindicado se ClCr < 25 mL/min. "
     "Menor taxa de sangramento GI versus rivaroxabana.",
     "SBC-SCA"),

    ("Warfarina", "Anticoagulação oral (FA valvar, prótese mecânica, TVP/TEP)",
     "adulto",
     "dose individualizada (média 5 mg)",  "1x/dia", "oral",
     "uso_continuo",
     True, True,
     "RNI 2,0–3,0 (FA, TVP); RNI 2,5–3,5 (prótese mecânica mitral)",
     "Iniciar 5 mg/dia; ajustar conforme INR. Monitorar INR semanalmente até estabilidade, "
     "depois mensal. Múltiplas interações alimentares (vitamina K) e medicamentosas. "
     "Contraindicada na gestação (1º e 3º trimestres).",
     "SBC-SCA"),

    ("Isossorbida mononitrato", "Angina estável crônica (profilaxia)",
     "adulto",
     "20–40 mg",        "2x/dia (8h e 14h — janela noturna livre)", "oral",
     "uso_continuo",
     False, True,
     "Redução de episódios anginosos",
     "Manter janela de 8–12h livre de nitrato para evitar tolerância. "
     "Hipotensão grave se combinado com inibidores de PDE-5 (sildenafila) — contraindicado.",
     "SBC-SCA"),

    # ══════════════════════════════════════════════════════════════════════
    # ENDÓCRINO / METABÓLICO — DM / TIREOIDE / GOTA / OSTEOPOROSE / OBESIDADE
    # ══════════════════════════════════════════════════════════════════════

    ("Metformina", "Diabetes mellitus tipo 2",
     "adulto",
     "500–850 mg",      "2–3x/dia com refeições", "oral",
     "uso_continuo",
     True, False,
     "HbA1c < 7%; glicemia jejum 80–130 mg/dL",
     "Iniciar 500 mg 1–2x/dia para reduzir efeitos GI; titular a cada 1–2 semanas até "
     "2000–2550 mg/dia. Suspender se TFGe < 30 mL/min/1,73m². Precaução com TFGe 30–45. "
     "Risco de deficiência de B12 com uso prolongado.",
     "SBD-DM2"),

    ("Empagliflozina", "Diabetes mellitus tipo 2 / DRC / Insuficiência Cardíaca",
     "adulto",
     "10–25 mg",        "1x/dia (manhã)",  "oral",
     "uso_continuo",
     True, False,
     "HbA1c < 7%; redução de desfechos cardiovasculares e renais",
     "DRC (EMPA-KIDNEY): 10 mg/dia se TFGe ≥ 20. ICC: 10 mg/dia independente de DM. "
     "Não usar se TFGe < 20 mL/min/1,73m² para DM2. Risco de cetoacidose euglicêmica "
     "(suspender 3–5 dias antes de cirurgia). Infecções genitais micóticas mais frequentes.",
     "SBD-DM2"),

    ("Dapagliflozina", "Diabetes mellitus tipo 2 / DRC / Insuficiência Cardíaca",
     "adulto",
     "10 mg",           "1x/dia",          "oral",
     "uso_continuo",
     True, False,
     "HbA1c < 7%; proteção renal e cardiovascular",
     "Para DM2: não usar se TFGe < 25 mL/min/1,73m². Para DRC/ICC: manter até TFGe ≥ 15. "
     "Suspender 3 dias antes de procedimento cirúrgico (risco de cetoacidose). "
     "Benefício renal independente do efeito glicêmico (DAPA-CKD).",
     "SBD-DM2"),

    ("Semaglutida", "Diabetes mellitus tipo 2 (controle glicêmico e cardiovascular)",
     "adulto",
     "0,25 mg → 0,5 mg → 1 mg SC/semana", "1x/semana", "sc",
     "uso_continuo",
     False, False,
     "HbA1c < 7%; redução de peso; desfechos cardiovasculares",
     "Escalonar: 0,25 mg/semana × 4 semanas → 0,5 mg/semana × 4 semanas → 1 mg/semana. "
     "Anti-obesidade (Ozempic/Wegovy): escalonar até 2,4 mg/semana. "
     "Náusea e vômitos frequentes no início. Contraindicada em carcinoma medular de tireoide.",
     "SBD-DM2"),

    ("Insulina Glargina", "Diabetes mellitus tipo 1 e tipo 2 (insulina basal)",
     "adulto",
     "0,2–0,4 UI/kg",   "1x/dia (preferencialmente ao deitar)", "sc",
     "uso_continuo",
     True, False,
     "Glicemia em jejum 80–130 mg/dL",
     "Titular aumentando 2 UI a cada 3 dias até atingir meta de glicemia em jejum. "
     "Não misturar com outras insulinas. Rodízio de sítios de aplicação. "
     "Em DRC: risco aumentado de hipoglicemia — titular com cuidado.",
     "SBD-DM1"),

    ("Insulina NPH", "Diabetes mellitus tipo 1 e tipo 2 (insulina basal-intermediária)",
     "adulto",
     "0,1–0,3 UI/kg",   "2x/dia (manhã e 22h)",  "sc",
     "uso_continuo",
     True, False,
     "Glicemia pré-prandial 80–130 mg/dL",
     "Homogeneizar (girar frasco suavemente 20x antes de aspirar). Pico de ação 4–8h. "
     "Hipoglicemia noturna: ajustar dose das 22h. Pode ser misturada com insulina regular.",
     "SBD-DM1"),

    ("Levotiroxina", "Hipotireoidismo",
     "adulto",
     "1,6 μg/kg/dia",   "1x/dia em jejum (30 min antes do café)", "oral",
     "uso_continuo",
     False, False,
     "TSH 0,5–2,5 mUI/L (adultos < 60 anos); TSH 1–4 mUI/L (idosos)",
     "Idosos: iniciar com 25 μg/dia e titular a cada 4–6 semanas. "
     "Gestação: aumentar dose 25–30% assim que confirmada (meta TSH < 2,5 mUI/L). "
     "Medir TSH 6–8 semanas após mudança de dose.",
     "PCDT-HIPOTIREOID"),

    ("Levotiroxina", "Hipotireoidismo",
     "idoso",
     "25–75 μg/dia (titular)", "1x/dia em jejum", "oral",
     "uso_continuo",
     False, False,
     "TSH 1,0–4,0 mUI/L",
     "Iniciar com doses baixas (25 μg/dia) em idosos e cardiopatas, aumentando 12,5–25 μg "
     "a cada 4–6 semanas para evitar precipitar angina ou fibrilação atrial.",
     "PCDT-HIPOTIREOID"),

    ("Metimazol", "Hipertireoidismo (Doença de Graves / nódulo tóxico)",
     "adulto",
     "10–30 mg",        "1–3x/dia",        "oral",
     "12–18 meses (Graves); até tratamento definitivo",
     False, True,
     "TSH 0,5–2,5 mUI/L; T4L normal",
     "Iniciar com dose alta; reduzir progressivamente após eutiroidismo (6–8 semanas). "
     "Dose de manutenção: 5–10 mg/dia. Suspender imediatamente se febre + dor de garganta "
     "(agranulocitose). Solicitar hemograma antes de iniciar.",
     "PCDT-HIPOTIREOID"),

    ("Alopurinol", "Gota crônica / Hiperuricemia sintomática",
     "adulto",
     "100 mg → titular",  "1x/dia",          "oral",
     "uso_continuo",
     True, False,
     "Ácido úrico sérico < 6 mg/dL (< 5 mg/dL em gota tofácea)",
     "Iniciar 100 mg/dia; aumentar 100 mg a cada 2–4 semanas até atingir meta. "
     "Máximo usual: 300 mg/dia (até 900 mg em casos refratários). "
     "Reduzir dose se TFGe < 30 mL/min. Reação de hipersensibilidade (DRESS): suspender. "
     "Não iniciar durante crise aguda.",
     "SBR-AR"),

    ("Alendronato sódico", "Osteoporose",
     "adulto",
     "70 mg",           "1x/semana em jejum rigoroso", "oral",
     "uso_continuo (mín. 3–5 anos)",
     True, False,
     "Redução de risco de fratura vertebral e não vertebral",
     "Tomar com copo cheio de água, em jejum, 30–60 minutos antes de qualquer alimento, "
     "bebida ou medicamento. Permanecer sentado/em pé por pelo menos 30 minutos. "
     "Contraindicado se TFGe < 35 mL/min e em esofagopatias. Suplementar Ca²⁺ e vitamina D.",
     "PCDT-OSTEOPOROSE"),

    ("Orlistate", "Obesidade (IMC ≥ 30 kg/m² ou ≥ 27 com comorbidades)",
     "adulto",
     "120 mg",          "3x/dia com refeições",  "oral",
     "uso_continuo (avaliar em 3 meses)",
     False, False,
     "Redução ≥ 5% do peso em 3 meses; melhora de comorbidades",
     "Inibidor de lipase pancreática/gástrica. Reduz absorção de gorduras em ~30%. "
     "Efeitos GI (esteatorreia, urgência fecal) frequentes; melhoram com dieta hipogordurosa. "
     "Suplementar vitaminas lipossolúveis (A, D, E, K) separadas 2h do orlistate.",
     "PCDT-OSTEOPOROSE"),

    # ══════════════════════════════════════════════════════════════════════
    # SAÚDE MENTAL / NEUROLÓGICO
    # ══════════════════════════════════════════════════════════════════════

    ("Escitalopram", "Depressão maior / Transtorno de ansiedade generalizada",
     "adulto",
     "10–20 mg",        "1x/dia",          "oral",
     "mínimo 6–12 meses (depressão); uso_continuo em recorrências",
     False, True,
     "Remissão dos sintomas depressivos; PHQ-9 < 5",
     "Iniciar 10 mg/dia; aumentar para 20 mg após 2–4 semanas se necessário. "
     "Efeito terapêutico em 2–4 semanas (ansiedade pode piorar inicialmente). "
     "Retirada gradual ao suspender (reduzir 50% a cada 2 semanas). "
     "Evitar em gestação no 3º trimestre (síndrome de abstinência neonatal).",
     "CFM-SM"),

    ("Sertralina", "Depressão maior / TOC / TEPT / Fobia social",
     "adulto",
     "50–200 mg",       "1x/dia (manhã ou noite)", "oral",
     "mínimo 6–12 meses",
     False, True,
     "Remissão dos sintomas; HAM-D ≤ 7",
     "Iniciar 50 mg/dia; titular 50 mg a cada 1–2 semanas até 200 mg/dia. "
     "Efeitos GI (náusea, diarreia) frequentes nas primeiras 2 semanas. "
     "Evitar com IMAOs (washout 14 dias).",
     "CFM-SM"),

    ("Fluoxetina", "Depressão maior / Bulimia / TOC",
     "adulto",
     "20–60 mg",        "1x/dia (manhã)",  "oral",
     "mínimo 6–12 meses",
     False, True,
     "Remissão dos sintomas depressivos",
     "Meia-vida muito longa (~4–6 dias; metabólito ativo norfluoxetina: ~4–16 dias). "
     "Suspensão abrupta geralmente bem tolerada pela meia-vida longa. "
     "Washout de 5 semanas antes de IMAO. Inibidor moderado de CYP2D6.",
     "CFM-SM"),

    ("Amitriptilina", "Depressão / Dor neuropática / Fibromialgia / Profilaxia de enxaqueca",
     "adulto",
     "25–150 mg",       "1x/dia (noturna)", "oral",
     "mínimo 6 meses; uso_continuo em dor neuropática",
     False, True,
     "Remissão de sintomas; EVA dor < 4",
     "Iniciar 10–25 mg à noite; titular gradualmente. Sedação intensa — tomar 1–2h antes de dormir. "
     "Monitorar QTc (ECG antes de doses > 100 mg). Evitar em idosos (risco de quedas, confusão). "
     "Contraindicado no IAM recente e no glaucoma de ângulo fechado.",
     "CFM-SM"),

    ("Venlafaxina", "Depressão maior / Ansiedade / Dor neuropática",
     "adulto",
     "75–225 mg",       "1x/dia com refeição (LP) ou 2–3x/dia (IR)", "oral",
     "mínimo 6–12 meses",
     True, True,
     "Remissão dos sintomas; HAM-A < 7",
     "Iniciar 37,5–75 mg/dia; aumentar gradualmente. Retirada gradual obrigatória "
     "(síndrome de descontinuação grave com vertigens, parestesias). "
     "Hipertensão dose-dependente — monitorar PA com doses ≥ 150 mg/dia.",
     "CFM-SM"),

    ("Duloxetina", "Depressão / Fibromialgia / Neuropatia diabética dolorosa",
     "adulto",
     "60–120 mg",       "1x/dia",          "oral",
     "mínimo 6 meses; uso_continuo em dor neuropática",
     True, True,
     "Remissão dos sintomas; redução de dor ≥ 50%",
     "Iniciar 30 mg/dia por 1–2 semanas; aumentar para 60 mg. Tomar com alimento. "
     "Hepatotoxicidade rara — evitar em hepatopatia grave e em uso excessivo de álcool. "
     "Contraindicada se TFGe < 30 mL/min.",
     "CFM-SM"),

    ("Lítio carbonato", "Transtorno afetivo bipolar (manutenção e episódios maníacos)",
     "adulto",
     "300 mg",          "2–3x/dia",        "oral",
     "uso_continuo",
     True, False,
     "Nível sérico terapêutico 0,6–1,2 mEq/L (manutenção); 0,8–1,2 (agudo)",
     "Monitorar nível sérico 12h após a última dose. Dosagem inicial mensal, depois a cada 3–6 meses. "
     "Monitorar TSH (hipotireoidismo), creatinina (nefropatia) e cálcio anualmente. "
     "Toxicidade: tremores grosseiros, ataxia, confusão — acima de 1,5 mEq/L.",
     "CFM-SM"),

    ("Ácido valproico / Valproato de sódio", "Epilepsia / Transtorno bipolar",
     "adulto",
     "15–30 mg/kg/dia", "2x/dia",          "oral",
     "uso_continuo",
     False, True,
     "Ausência de crises; nível sérico 50–100 μg/mL",
     "Comprimido de liberação prolongada preferível (tolerância GI). "
     "Monitorar ALT/AST, hemograma e nível sérico. ALTAMENTE TERATOGÊNICO — "
     "contraindicado em mulheres em idade fértil sem anticoncepção eficaz. "
     "Risco de hiperamonemia (monitorar amônia se encefalopatia).",
     "ABN-EPILEPSIA"),

    ("Carbamazepina", "Epilepsia focal / Neuralgia do trigêmeo / TAB",
     "adulto",
     "200–1600 mg",     "2–3x/dia",        "oral",
     "uso_continuo",
     False, True,
     "Ausência de crises; nível sérico 4–12 μg/mL",
     "Iniciar com 200 mg/dia; titular gradualmente. Indutor potente de CYP3A4/CYP2C9 e P-gp. "
     "Hemograma de entrada (leucopenia, aplasia rara). Hiponatremia por SIADH. "
     "HLA-B*1502 (populações asiáticas): risco de Stevens-Johnson antes de iniciar.",
     "ABN-EPILEPSIA"),

    ("Levetiracetam", "Epilepsia focal e generalizada",
     "adulto",
     "500–3000 mg",     "2x/dia",          "oral",
     "uso_continuo",
     True, False,
     "Ausência ou redução ≥ 50% das crises",
     "Dose inicial 500 mg 2x/dia; aumentar 500 mg a cada 2 semanas. "
     "Ajuste renal: reduzir dose se TFGe < 50 mL/min/1,73m². "
     "Sem interações pelo sistema CYP (vantagem em politerapia). "
     "Irritabilidade e alterações comportamentais em ~15% dos pacientes.",
     "ABN-EPILEPSIA"),

    ("Levodopa + Carbidopa", "Doença de Parkinson",
     "adulto",
     "100/25 mg",       "3–4x/dia (a cada 4–6h)", "oral",
     "uso_continuo",
     False, False,
     "Melhora motora; redução de rigidez e bradicinesia",
     "Titulação lenta (início com metade do comprimido 3x/dia). "
     "Efeito on-off com tratamento prolongado. Tomar 30–60 min antes das refeições "
     "(proteínas reduzem absorção). Evitar interrupção abrupta (síndrome neuroléptica maligna like).",
     "ABN-PARKINSON"),

    ("Donepezila", "Doença de Alzheimer (demência leve a grave)",
     "adulto",
     "5–10 mg",         "1x/dia (noturna)", "oral",
     "uso_continuo enquanto houver benefício",
     False, False,
     "Estabilização ou melhora de cognição; MEEM",
     "Iniciar 5 mg/noite; aumentar para 10 mg após 4–6 semanas se tolerado. "
     "Efeitos colinérgicos: náusea, diarreia, bradicardia, insônia. "
     "Monitorar FC (risco de bradicardia em cardiopatas).",
     "PCDT-ALZHEIMER"),

    ("Risperidona", "Esquizofrenia / Transtorno bipolar (episódio maníaco)",
     "adulto",
     "2–8 mg",          "1–2x/dia",        "oral",
     "uso_continuo",
     True, True,
     "Controle dos sintomas psicóticos positivos e negativos",
     "Iniciar 1–2 mg/dia; titular gradualmente. Monitorar prolactina (ginecomastia, amenorreia), "
     "síndrome metabólica (peso, glicemia, lipídeos) e sintomas extrapiramidais. "
     "Reduzir dose em idosos (0,5–2 mg/dia). Ajuste em insuficiência renal/hepática.",
     "CFM-SM"),

    ("Metilfenidato LP", "TDAH (adulto e adolescente ≥ 6 anos)",
     "adulto",
     "18–54 mg",        "1x/dia (manhã)",  "oral",
     "uso_continuo (reavaliação periódica)",
     False, False,
     "Melhora de atenção, impulsividade e hiperatividade",
     "Medir PA e FC na 1ª consulta e a cada 6 meses. Contraindicado em glaucoma, "
     "tireotoxicose, arritmias graves e uso de IMAOs. Potencial de abuso — "
     "formulação LP preferível para diminuir desvio. Possível desaceleração do crescimento em crianças.",
     "CFM-SM"),

    ("Propranolol", "Profilaxia de enxaqueca / HAS / Taquicardia / Tremor essencial",
     "adulto",
     "40–240 mg",       "2–3x/dia",        "oral",
     "uso_continuo",
     False, True,
     "Redução de crises de enxaqueca ≥ 50%; FC e PA controladas",
     "Não cardioseletivo — contraindicado em asma, DPOC grave, bloqueio AV 2º–3º grau. "
     "Não suspender abruptamente (risco de angina rebote). "
     "Pode mascarar sintomas de hipoglicemia em diabéticos.",
     "SBC-HAS"),

    # ══════════════════════════════════════════════════════════════════════
    # RESPIRATÓRIO — ASMA / DPOC
    # ══════════════════════════════════════════════════════════════════════

    ("Budesonida inalatória", "Asma persistente (controle de longo prazo)",
     "adulto",
     "200–800 μg/dia",  "1–2x/dia",        "inalatoria",
     "uso_continuo",
     False, False,
     "Ausência de sintomas diurnos/noturnos; VEF₁ ≥ 80% do previsto",
     "Fazer bocochão com água após cada uso para prevenir candidíase orofaríngea. "
     "Dose depende da gravidade (leve: 200–400; moderada: 400–800; grave: > 800 μg). "
     "Não suspender abruptamente após uso prolongado em altas doses.",
     "PCDT-ASMA"),

    ("Formoterol", "Asma (LABA associado a ICS) / DPOC",
     "adulto",
     "12 μg",           "2x/dia (12/12h)", "inalatoria",
     "uso_continuo",
     False, False,
     "Controle de sintomas; redução de exacerbações",
     "LABA — nunca usar como monoterapia em asma (risco de morte por asma sem ICS). "
     "Em asma: sempre associado a corticoide inalatório (ICS). "
     "Início rápido de ação (3–5 min) — pode ser usado como SOS quando combinado com budesonida.",
     "PCDT-ASMA"),

    ("Tiotrópio", "DPOC (GOLD B, C, D)",
     "adulto",
     "18 μg",           "1x/dia",          "inalatoria",
     "uso_continuo",
     False, False,
     "Redução de exacerbações; melhora do VEF₁ e qualidade de vida",
     "Cápsula para inalação via HandiHaler — não engolir a cápsula. "
     "Não requer ajuste de dose. Anticolinérgico de longa ação (LAMA). "
     "Precaução em glaucoma de ângulo fechado e hipertrofia prostática.",
     "PCDT-DPOC"),

    ("Salbutamol (Albuterol)", "Asma / DPOC (broncodilatador de resgate)",
     "adulto",
     "100–200 μg (1–2 jatos)", "SOS (máx 10 inalações/dia)", "inalatoria",
     "conforme necessidade",
     False, False,
     "Alívio imediato do broncoespasmo",
     "SABA — uso frequente (> 2x/semana) indica asma não controlada: intensificar terapia. "
     "Nebulização: 2,5–5 mg diluído em SF 0,9%. "
     "Taquicardia e tremor são efeitos adversos comuns.",
     "PCDT-ASMA"),

    ("Montelucaste", "Asma alérgica / Rinite alérgica",
     "adulto",
     "10 mg",           "1x/dia (noturna)", "oral",
     "uso_continuo",
     False, False,
     "Redução de sintomas de asma e rinite",
     "Anti-leucotrieno. Efeitos neuropsiquiátricos: ansiedade, depressão, pesadelos, "
     "comportamento suicida (alerta FDA/ANVISA 2020) — avaliar relação risco-benefício. "
     "Alternativa ao ICS em asma leve ou como terapia add-on.",
     "PCDT-ASMA"),

    # ══════════════════════════════════════════════════════════════════════
    # GI / REUMATOLÓGICO / AUTOIMUNE
    # ══════════════════════════════════════════════════════════════════════

    ("Omeprazol", "DRGE / Úlcera péptica / Prevenção de úlcera por AINE",
     "adulto",
     "20–40 mg",        "1x/dia em jejum (30 min antes do café)", "oral",
     "4–8 semanas (úlcera); uso_continuo (DRGE erosiva)",
     False, True,
     "Ausência de sintomas; cicatrização de mucosa",
     "Uso prolongado (> 1 ano): monitorar vitamina B12, magnésio e potássio. "
     "Risco aumentado de fraturas, pneumonia, infecção por C. difficile. "
     "Inibidor moderado de CYP2C19 (reduz ativação do clopidogrel — preferir pantoprazol).",
     "PCDT-DPOC"),

    ("Mesalazina (5-ASA)", "Retocolite ulcerativa (manutenção e crise leve-moderada)",
     "adulto",
     "2–4 g/dia",       "1–2x/dia",        "oral",
     "indução 6–8 semanas; manutenção uso_continuo",
     True, False,
     "Remissão clínica; colonoscopia sem atividade inflamatória",
     "Granulado, comprimido gastrorresistente ou supositório (proctite). "
     "Dose de indução: 4 g/dia; manutenção: 2 g/dia. "
     "Nefrotoxicidade rara — monitorar creatinina anualmente.",
     "PCDT-RCU"),

    ("Azatioprina", "DII / LES / Transplante (imunossupressão de manutenção)",
     "adulto",
     "1,5–3 mg/kg/dia", "1–2x/dia",        "oral",
     "uso_continuo",
     True, True,
     "Manutenção da remissão; poupador de corticoide",
     "Hemograma mensal nos primeiros 3 meses, depois a cada 3 meses. "
     "Interação grave com alopurinol (reduzir dose em 75%). "
     "Risco aumentado de linfoma e infecções oportunistas. "
     "Testar atividade de TPMT antes de iniciar se disponível.",
     "PCDT-CROHN"),

    ("Infliximabe", "Artrite reumatoide / Doença de Crohn / RCU / Psoríase",
     "adulto",
     "5 mg/kg IV",      "S0, S2, S6 → a cada 8 semanas", "iv",
     "uso_continuo enquanto houver resposta",
     False, False,
     "Remissão ou baixa atividade de doença",
     "Rastrear TB (PPD ou IGRA) e hepatite B antes de iniciar. "
     "Pré-medicação com anti-histamínico e paracetamol para reduzir reações infusionais. "
     "Contraindicado em IC grave (classe NYHA III-IV) e sepse ativa. "
     "Reativação de TB: maior risco com anti-TNF.",
     "PCDT-CROHN"),

    ("Adalimumabe", "Artrite reumatoide / Psoríase / Doença de Crohn",
     "adulto",
     "40 mg",           "a cada 2 semanas (SC)",  "sc",
     "uso_continuo enquanto houver resposta",
     False, False,
     "Remissão ou baixa atividade de doença; DAS28 < 2,6",
     "Rastrear TB e hepatite B antes de iniciar. Auto-injetor disponível. "
     "Reações no local de injeção (eritema, prurido) são frequentes. "
     "Não combinar com outro biológico (risco infeccioso grave).",
     "PCDT-AR"),

    ("Metotrexato", "Artrite reumatoide / Psoríase / Artrite psoriásica",
     "adulto",
     "10–25 mg",        "1x/semana",       "oral",
     "uso_continuo",
     True, True,
     "Baixa atividade ou remissão; DAS28 < 2,6",
     "Sempre associar ácido fólico 5 mg/semana (no dia seguinte ao MTX) para reduzir toxicidade. "
     "Contraindicado em gestação (DROGA TERATOGÊNICA — categoria X). "
     "Monitorar hemograma, TGO, TGP e creatinina mensalmente nos primeiros 6 meses. "
     "Hepatotoxicidade e mielossupressão são as principais toxicidades.",
     "PCDT-AR"),

    ("Hidroxicloroquina", "Lúpus eritematoso sistêmico / Artrite reumatoide",
     "adulto",
     "400 mg/dia (ou 5 mg/kg/dia real)", "1x/dia",  "oral",
     "uso_continuo",
     False, False,
     "Controle de manifestações cutâneas e articulares; redução de flares",
     "Avaliação oftalmológica anual (retino toxicidade após 5 anos de uso ou dose > 5 mg/kg). "
     "Prolongamento do QTc — ECG basal em pacientes com risco cardíaco. "
     "Muito segura na gestação; manter durante a gravidez em LES.",
     "PCDT-LES"),

    ("Colchicina", "Gota aguda / Profilaxia de crises de gota / Pericardite",
     "adulto",
     "1 mg + 0,5 mg após 1h (aguda); 0,5 mg 1–2x/dia (profilaxia)", "conforme indicação", "oral",
     "crise aguda: 1–2 dias; profilaxia: 3–6 meses",
     True, True,
     "Controle da inflamação articular; prevenção de crises",
     "Gota aguda: 1 mg na crise + 0,5 mg 1h depois; dose máxima 1,5 mg/episódio. "
     "Toxicidade grave se combinada com inibidores CYP3A4/P-gp (claritromicina, ciclosporina). "
     "Ajuste de dose em insuficiência renal. Diarreia é o efeito adverso mais comum.",
     "SBR-AR"),

    ("Prednisona", "Anti-inflamatória / Imunossupressora (diversas doenças crônicas)",
     "adulto",
     "0,5–1 mg/kg/dia", "1x/dia (manhã)", "oral",
     "conforme resposta; desmame obrigatório se > 4 semanas",
     False, True,
     "Controle da inflamação; remissão de doenças autoimunes",
     "Tomar com alimento. Usar sempre a menor dose eficaz pelo menor tempo possível. "
     "Desmame gradual em tratamentos > 4 semanas (risco de insuficiência adrenal). "
     "Profilaxia de osteoporose: cálcio + vitamina D + considerar bifosfonato se uso > 3 meses. "
     "Monitorar glicemia, PA, peso e densidade mineral óssea.",
     "PCDT-AR"),

    # ══════════════════════════════════════════════════════════════════════
    # OUTROS — ANEMIA / ONCOLOGIA / SUPLEMENTAÇÃO
    # ══════════════════════════════════════════════════════════════════════

    ("Darbepoetina alfa", "Anemia da doença renal crônica",
     "adulto",
     "0,45 μg/kg",      "1x/semana SC ou IV", "sc",
     "uso_continuo enquanto em diálise ou TFGe < 30",
     True, False,
     "Hemoglobina 10–12 g/dL; redução de necessidade transfusional",
     "Ajustar dose para manter Hb 10–12 g/dL (evitar > 13 g/dL — risco cardiovascular). "
     "Monitorar depósitos de ferro (ferritina, IST) — suplementar se necessário para resposta ótima. "
     "Hipertensão e trombose são efeitos adversos importantes.",
     "PCDT-DRC"),

    ("Hidroxiureia", "Anemia falciforme (prevenção de crises vaso-oclusivas)",
     "adulto",
     "15–35 mg/kg/dia", "1x/dia",          "oral",
     "uso_continuo",
     True, False,
     "Redução de crises dolorosas; aumento de HbF ≥ 15%",
     "Iniciar 15 mg/kg/dia; aumentar 5 mg/kg a cada 8–12 semanas até resposta ou toxicidade. "
     "Suspender se neutrófilos < 2000/μL, plaquetas < 80.000/μL ou Hb < 5 g/dL. "
     "Teratogênica — anticoncepção obrigatória. Hemograma a cada 4–8 semanas.",
     "PCDT-ANEMIA-FALCIF"),

    ("Tamoxifeno", "Câncer de mama hormônio-receptor positivo (pré-menopausa)",
     "adulto",
     "20 mg",           "1x/dia",          "oral",
     "5–10 anos",
     False, True,
     "Redução de recorrência e mortalidade por câncer de mama",
     "Pré-menopausa. Risco de câncer de endométrio (monitorar sangramento vaginal anormal). "
     "Risco de TVP/TEP — mobilização e profilaxia em cirurgias. "
     "Evitar inibidores potentes de CYP2D6 (paroxetina, fluoxetina) que reduzem conversão "
     "para endoxifeno (metabólito ativo). Contraindicado na gestação.",
     "INCA-ONCOL"),

    ("Letrozol", "Câncer de mama hormônio-receptor positivo (pós-menopausa)",
     "adulto",
     "2,5 mg",          "1x/dia",          "oral",
     "5–10 anos",
     False, True,
     "Redução de recorrência e mortalidade por câncer de mama",
     "Inibidor de aromatase — indicado apenas em mulheres pós-menopáusicas. "
     "Osteoporose como efeito adverso principal: suplementar Ca²⁺ + vitamina D e monitorar DMO. "
     "Artralgias e calores comuns. Contraindicado na gestação.",
     "INCA-ONCOL"),

    ("Imatinibe", "LMC (fase crônica e acelerada) / GIST",
     "adulto",
     "400 mg",          "1x/dia com refeição", "oral",
     "uso_continuo",
     True, True,
     "Resposta citogenética completa; BCR-ABL ≤ 0,1% (RMM)",
     "LMC acelerada: 600 mg/dia. Náusea, edema periorbitário, retenção hídrica são frequentes. "
     "Monitorar hemograma, função hepática e renal. "
     "Metabolizado por CYP3A4 — múltiplas interações medicamentosas.",
     "INCA-ONCOL"),

    ("Sulfato ferroso", "Anemia ferropriva",
     "adulto",
     "300 mg",          "3x/dia em jejum (ou 2x com alimento se intolerância GI)", "oral",
     "3–6 meses pós-normalização de hemoglobina",
     False, False,
     "Hb normal para sexo e idade; ferritina > 50 ng/mL",
     "Tomar com suco de vitamina C (aumenta absorção). "
     "Evitar com antiácidos, carbonato de cálcio, chá e leite (quelação). "
     "Fezes escuras e constipação são efeitos adversos comuns. "
     "Controlar hemograma após 4 semanas de tratamento.",
     "PCDT-DRC"),

    ("Cianocobalamina (Vitamina B12)", "Deficiência de vitamina B12 / Anemia megaloblástica",
     "adulto",
     "1000 μg",         "1x/dia × 7 dias → 1x/semana × 4 sem → 1x/mês (manutenção)", "im",
     "manutenção: uso_continuo em déficit absortivo",
     False, False,
     "B12 sérica ≥ 300 pg/mL; resolução de anemia e neuropatia",
     "Reposição IM obrigatória em má absorção (gastrite atrófica, gastrectomia, anemia perniciosa). "
     "Via oral (1000–2000 μg/dia) eficaz em déficit por ingesta insuficiente. "
     "Monitorar K+ na fase inicial (hipocalemia por reticulocitose).",
     "PCDT-DRC"),

]


# =============================================================================
# INTERACOES_MEDICAMENTOS_CRONICOS
# =============================================================================
# Campos:
#  0  medicamento_nome
#  1  medicamento_interagente
#  2  classe_interagente
#  3  mecanismo
#  4  gravidade        ('contraindicada' | 'grave' | 'moderada' | 'leve')
#  5  efeito_clinico
#  6  conduta
#  7  fonte_sigla

INTERACOES_MEDICAMENTOS_CRONICOS = [

    # ══════════════════════════════════════════════════════════════════════
    # ANTICOAGULANTES / ANTIAGREGANTES
    # ══════════════════════════════════════════════════════════════════════

    ("Warfarina", "AINEs (ibuprofeno, naproxeno, diclofenaco)",
     "Anti-inflamatórios não esteroides",
     "Inibição plaquetária pelos AINEs somada ao efeito anticoagulante da warfarina; "
     "possível inibição de CYP2C9 (alguns AINEs) aumentando RNI",
     "grave",
     "Risco significativamente aumentado de sangramento GI e intracraniano",
     "Evitar uso concomitante sempre que possível. Se necessário, monitorar INR 2–3x/semana "
     "e usar IBP profilático. Paracetamol é a analgésica de escolha.",
     "SBC-SCA"),

    ("Warfarina", "Amiodarona",
     "Antiarrítmico classe III",
     "Inibição de CYP2C9 e CYP3A4 pela amiodarona → redução do metabolismo da warfarina; "
     "início de ação tardio (semanas) pela meia-vida longa da amiodarona",
     "grave",
     "Elevação progressiva do RNI com risco de sangramento grave",
     "Reduzir dose da warfarina em 30–50% ao iniciar amiodarona. "
     "Monitorar INR semanalmente por pelo menos 4–6 semanas e ajustar conforme resposta. "
     "O efeito persiste por meses após suspensão da amiodarona.",
     "SBC-SCA"),

    ("Warfarina", "Antifúngicos azólicos (fluconazol, voriconazol, cetoconazol)",
     "Antifúngicos sistêmicos",
     "Inibição potente de CYP2C9 (e CYP3A4 para alguns azólicos) → aumento dos níveis "
     "séricos de warfarina",
     "grave",
     "Elevação acentuada do RNI em 3–7 dias; risco de sangramento grave ou fatal",
     "Reduzir dose da warfarina em 25–50% ao iniciar azólicos. "
     "Monitorar INR diariamente nos primeiros 3–5 dias, depois 2–3x/semana.",
     "SBC-SCA"),

    ("Warfarina", "Antibióticos de amplo espectro (fluoroquinolonas, cefalosporinas, metronidazol)",
     "Antibióticos",
     "Redução da flora intestinal produtora de vitamina K; metronidazol inibe CYP2C9 "
     "adicionalmente",
     "grave",
     "Elevação do RNI com risco de sangramento",
     "Monitorar INR 2–3x/semana durante o antibiótico e por 1 semana após o término. "
     "Ajustar dose da warfarina conforme INR.",
     "SBC-SCA"),

    ("Warfarina", "Levotiroxina",
     "Hormônio tireoidiano",
     "Aumento do metabolismo dos fatores de coagulação dependentes de vitamina K "
     "em hipermetabolismo induzido pelo hormônio tireoidiano",
     "moderada",
     "Potencialização do efeito anticoagulante; RNI acima do alvo terapêutico",
     "Monitorar INR 2–4 semanas após iniciar ou ajustar levotiroxina. "
     "Ajustar dose da warfarina conforme necessário.",
     "SBC-SCA"),

    ("Rivaroxabana", "Antifúngicos azólicos (cetoconazol, voriconazol, itraconazol)",
     "Antifúngicos sistêmicos",
     "Inibição potente e dual de CYP3A4 e P-gp → aumento substancial dos níveis plasmáticos "
     "de rivaroxabana",
     "contraindicada",
     "Risco muito elevado de sangramento grave por superdosagem funcional do DOAC",
     "CONTRAINDICADA a combinação. Substituir o antifúngico ou o anticoagulante. "
     "Se inevitável, considerar warfarina com monitoração de INR.",
     "SBC-SCA"),

    ("Apixabana", "Antifúngicos azólicos (cetoconazol, itraconazol, voriconazol)",
     "Antifúngicos sistêmicos",
     "Inibição potente de CYP3A4 e P-gp → elevação marcada dos níveis de apixabana",
     "contraindicada",
     "Risco elevado de sangramento grave",
     "CONTRAINDICADA. Avaliar alternativa antifúngica (fluconazol = inibidor moderado: "
     "reduzir dose de apixabana para 2,5 mg 2x/dia se paciente já não usa dose reduzida).",
     "SBC-SCA"),

    ("AAS + Clopidogrel", "Anticoagulante oral (warfarina, DOAC) — terapia tripla",
     "Anticoagulantes",
     "Sinergismo farmacológico: inibição plaquetária dupla + anticoagulação → comprometimento "
     "de todos os mecanismos hemostáticos",
     "grave",
     "Sangramento major (GI, intracraniano) com risco de vida",
     "Restringir a situações de alto risco (pós-SCA + FA + stent). "
     "Limitar terapia tripla a ≤ 1 mês; preferir dupla terapia (DOAC + clopidogrel) "
     "após o período inicial. Usar IBP durante toda a terapia tripla.",
     "SBC-SCA"),

    # ══════════════════════════════════════════════════════════════════════
    # CARDIOVASCULAR — IECA / BRA / DIURÉTICOS / BETABLOQUEADORES
    # ══════════════════════════════════════════════════════════════════════

    ("IECA (enalapril, ramipril)", "Espironolactona",
     "Diurético poupador de potássio / Antagonista de aldosterona",
     "IECA reduz excreção de K+ (inibição de aldosterona) somado ao efeito poupador de K+ "
     "da espironolactona → acúmulo de potássio",
     "grave",
     "Hipercalemia grave (K+ > 6,0 mEq/L) com risco de arritmia fatal e parada cardíaca",
     "Monitorar K+ e creatinina após 1 semana do início ou de qualquer ajuste de dose. "
     "Manter K+ < 5,0 mEq/L. Contraindicada a combinação em DRC avançada (TFGe < 30).",
     "SBC-ICC"),

    ("IECA (enalapril) / BRA (losartana)", "AINEs (ibuprofeno, indometacina, naproxeno)",
     "Anti-inflamatórios não esteroides",
     "AINEs inibem síntese de prostaglandinas vasodilatadoras renais, antagonizando o efeito "
     "nefro e vasodilatador dos IECA/BRA; pode precipitar IRA em pacientes suscetíveis",
     "grave",
     "Redução da eficácia anti-hipertensiva e da nefroproteção; risco de IRA aguda "
     "especialmente em idosos, desidratados ou com DRC preexistente",
     "Evitar uso crônico de AINEs em pacientes com IECA/BRA. "
     "Se inevitável, monitorar PA, creatinina e K+ semanalmente. "
     "Preferir paracetamol como analgésico.",
     "SBC-HAS"),

    ("IECA / BRA / Espironolactona — combinação tripla", "Associação das três classes",
     "Bloqueio do sistema renina-angiotensina-aldosterona",
     "Bloqueio simultâneo do SRAA em três pontos distintos resulta em risco cumulativo "
     "de hipercalemia e IRA superiores à combinação dupla",
     "contraindicada",
     "Hipercalemia com risco de vida e IRA grave",
     "CONTRAINDICADA a combinação tripla IECA + BRA + poupador de K+. "
     "Utilizar no máximo dois agentes do SRAA com monitoração rigorosa.",
     "SBC-ICC"),

    ("Beta-bloqueadores (atenolol, metoprolol, propranolol)",
     "Verapamil / Diltiazem (via IV ou oral)",
     "Bloqueadores dos canais de cálcio não-dihidropiridínicos",
     "Efeitos cronotrópicos e dromotrópicos negativos aditivos sobre o nó SA e AV",
     "contraindicada",
     "Bradicardia grave, bloqueio AV de alto grau, hipotensão e parada cardíaca. "
     "Risco especialmente alto com administração IV",
     "CONTRAINDICADA a associação IV. Via oral: usar com extrema cautela em pacientes "
     "sem marca-passo; monitorar FC e ECG. Preferir associação com dihidropiridinas (anlodipino).",
     "SBC-ICC"),

    ("Digoxina", "Amiodarona",
     "Antiarrítmico classe III",
     "Amiodarona inibe a glicoproteína P (P-gp) → redução da excreção renal e intestinal "
     "de digoxina → elevação dos níveis séricos",
     "grave",
     "Toxicidade digitálica: náusea, bradicardia, bloqueio AV, arritmias ventriculares",
     "Reduzir dose da digoxina em 50% ao iniciar amiodarona. "
     "Monitorar nível sérico de digoxina (alvo 0,5–0,9 ng/mL para IC) e ECG.",
     "SBC-ICC"),

    ("Digoxina", "Diuréticos de alça (furosemida) / Tiazídicos",
     "Diuréticos",
     "Hipocalemia induzida pelos diuréticos aumenta a ligação da digoxina aos canais Na/K-ATPase "
     "no miocárdio → toxicidade mesmo com nível sérico dentro do alvo",
     "grave",
     "Toxicidade digitálica precipitada por hipocalemia: arritmias, náusea, distúrbios visuais",
     "Manter K+ > 4,0 mEq/L em pacientes usando digoxina + diurético. "
     "Suplementar KCl se necessário. Monitorar eletrólitos mensalmente.",
     "SBC-ICC"),

    # ══════════════════════════════════════════════════════════════════════
    # ESTATINAS / ANTILIPEMIANTES
    # ══════════════════════════════════════════════════════════════════════

    ("Estatinas (sinvastatina, atorvastatina)", "Genfibrozil",
     "Fibrato",
     "Genfibrozil inibe a glucuronidação das estatinas (principal via de metabolismo) e "
     "inibe CYP2C8 → aumento marcado dos níveis séricos das estatinas",
     "grave",
     "Miopatia e rabdomiólise com risco de IRA grave",
     "Combinação com genfibrozil é CONTRAINDICADA. "
     "Se fibrato necessário, preferir fenofibrato (menor interação). "
     "Monitorar CK se sintomas musculares.",
     "SBC-DISLIPID"),

    ("Sinvastatina", "Amiodarona",
     "Antiarrítmico classe III",
     "Amiodarona inibe CYP3A4 → aumento dos níveis de sinvastatina",
     "grave",
     "Miopatia e rabdomiólise",
     "Limitar sinvastatina a máximo 20 mg/dia quando associada à amiodarona. "
     "Considerar atorvastatina em doses menores ou rosuvastatina como alternativa.",
     "SBC-DISLIPID"),

    ("Estatinas (sinvastatina, atorvastatina)", "Ciclosporina",
     "Imunossupressor (inibidor de calcineurina)",
     "Ciclosporina inibe CYP3A4 e P-gp → aumento substancial dos níveis de estatinas",
     "grave",
     "Rabdomiólise com IRA grave",
     "Combinação de ciclosporina com sinvastatina ou atorvastatina em doses altas é contraindicada. "
     "Preferir rosuvastatina 5 mg/dia ou pravastatina (não CYP3A4) com monitoração de CK.",
     "SBC-DISLIPID"),

    ("Estatinas (sinvastatina)", "Fenofibrato",
     "Fibrato",
     "Inibição parcial do metabolismo das estatinas; risco menor que com genfibrozil",
     "moderada",
     "Risco aumentado de miopatia (menor que com genfibrozil)",
     "Combinação permitida com cautela. Usar doses moderadas de estatina. "
     "Monitorar CK antes e 4–8 semanas após início. Suspender se CK > 5× limite superior da normalidade.",
     "SBC-DISLIPID"),

    # ══════════════════════════════════════════════════════════════════════
    # ANTI-INFLAMATÓRIOS / REUMATOLÓGICOS
    # ══════════════════════════════════════════════════════════════════════

    ("Metotrexato", "AINEs (indometacina, naproxeno, ibuprofeno)",
     "Anti-inflamatórios não esteroides",
     "AINEs reduzem a excreção tubular renal do metotrexato (inibição de transportadores OAT) "
     "→ acúmulo de MTX",
     "grave",
     "Toxicidade do metotrexato: mielossupressão, mucosites severas, hepatotoxicidade",
     "Evitar AINEs de alta dose com MTX em doses intermediárias/altas (≥ 15 mg/semana). "
     "Doses baixas de AINEs em AR podem ser toleradas com vigilância. "
     "Monitorar hemograma e função renal se combinados.",
     "PCDT-AR"),

    ("Metotrexato", "Cotrimoxazol (Sulfametoxazol-Trimetoprima)",
     "Antibiótico sulfonamida + inibidor de dihidrofolato redutase",
     "Sinergismo antifolato: ambos inibem vias do folato → depleção grave do metabolismo "
     "de nucleotídeos em células de rápida divisão",
     "contraindicada",
     "Pancitopenia grave, mucosites severas, hepatotoxicidade",
     "CONTRAINDICADA a combinação. Substituir por outro antibiótico (amoxicilina, cefalexina). "
     "Se uso inadvertido: folinato de cálcio (leucovorin) + suporte hematológico.",
     "PCDT-AR"),

    ("Metotrexato", "Leflunomida",
     "Imunossupressor (inibidor de DHODH)",
     "Hepatotoxicidade aditiva por mecanismos distintos",
     "grave",
     "Hepatotoxicidade grave com risco de cirrose acelerada",
     "Monitorar TGO e TGP mensalmente. Combinação possível em AR refratária sob supervisão "
     "especializada. Biópsia hepática se TGO/TGP > 3× LSN persistente.",
     "PCDT-AR"),

    ("Corticosteroide (prednisona)", "AINEs",
     "Anti-inflamatórios não esteroides",
     "Sinergismo para dano da mucosa GI: corticoide reduz produção de muco e prostaglandinas "
     "protetoras; AINE inibe COX-1 e reduz prostaglandinas adicionalmente",
     "grave",
     "Úlcera péptica, sangramento GI e perfuração",
     "Usar IBP profilático (omeprazol 20 mg/dia) durante toda a combinação. "
     "Evitar associação crônica sem IBP. Preferir paracetamol como analgésico.",
     "PCDT-AR"),

    ("Colchicina", "Claritromicina / Inibidores potentes de CYP3A4 e P-gp",
     "Antibiótico macrolídeo / Inibidores enzimáticos",
     "Inibição de CYP3A4 e P-gp → acúmulo grave de colchicina (margem terapêutica estreita)",
     "contraindicada",
     "Toxicidade grave de colchicina: miopatia, neuropatia periférica, mielossupressão, "
     "insuficiência multorgânica",
     "CONTRAINDICADA em pacientes com insuficiência renal ou hepática. "
     "Em pacientes com função normal: reduzir dose de colchicina ao mínimo e monitorar. "
     "Preferir azitromicina como alternativa ao macrolídeo.",
     "SBR-AR"),

    ("Azatioprina", "Alopurinol",
     "Inibidor de xantina oxidase",
     "Alopurinol inibe a xantina oxidase → bloqueio da inativação da 6-mercaptopurina "
     "(metabólito ativo da azatioprina) → acúmulo de metabólitos tiopurínicos citotóxicos",
     "contraindicada",
     "Mielotoxicidade grave: pancitopenia com risco de infecções fatais",
     "CONTRAINDICADA a combinação em doses habituais. "
     "Se inevitável (gota refratária + IBD), reduzir azatioprina em 75% e monitorar CBC semanalmente. "
     "Considerar febuxostate como alternativa ao alopurinol (menor interação com azatioprina).",
     "PCDT-CROHN"),

    ("Adalimumabe", "Infliximabe / Outro biológico (anti-TNF, anti-IL)",
     "Imunobiológicos",
     "Imunossupressão aditiva por bloqueio de múltiplas vias imunológicas",
     "contraindicada",
     "Risco muito aumentado de infecções oportunistas graves (TB, aspergilose, CMV), "
     "reativação viral e malignidades",
     "CONTRAINDICADA a combinação de dois biológicos. "
     "Washout de pelo menos 5 meias-vidas antes de iniciar outro biológico.",
     "PCDT-AR"),

    ("Hidroxicloroquina", "Amiodarona / Moxifloxacino",
     "Antiarrítmico / Fluoroquinolona",
     "Efeito aditivo sobre prolongamento do intervalo QTc por mecanismos distintos "
     "(bloqueio de canais hERG potássio)",
     "grave",
     "Prolongamento do QTc com risco de Torsades de Pointes e morte súbita",
     "Monitorar ECG (QTc) antes e periodicamente durante a combinação. "
     "Evitar associação se QTc basal > 480 ms. Corrigir hipocalemia e hipomagnesemia.",
     "PCDT-LES"),

    # ══════════════════════════════════════════════════════════════════════
    # SAÚDE MENTAL / NEUROLÓGICO
    # ══════════════════════════════════════════════════════════════════════

    ("ISRS (sertralina, fluoxetina, escitalopram)", "Tramadol / Linezolida / Triptanos",
     "Opioides / Antibiótico oxazolidinona / Agonistas 5-HT",
     "Sinergismo serotoninérgico: aumento da disponibilidade de serotonina na fenda sináptica "
     "por diferentes mecanismos",
     "grave",
     "Síndrome serotoninérgica: agitação, hipertermia, tremores, rigidez muscular, "
     "taquicardia, pode evoluir para rabdomiólise e morte",
     "Monitorar rigorosamente. Evitar combinação sempre que possível. "
     "Se síndrome serotoninérgica suspeita: suspender todos os agentes, suporte clínico, "
     "ciproeptadina como antídoto.",
     "CFM-SM"),

    ("ISRS / IRSN", "AINEs (ibuprofeno, naproxeno, diclofenaco)",
     "Anti-inflamatórios não esteroides",
     "ISRS inibe recaptação de serotonina nas plaquetas → depleção de serotonina plaquetária "
     "+ AINE inibe COX-1 → sinergismo na inibição da agregação plaquetária",
     "moderada",
     "Aumento do risco de sangramento GI (2–3×) e possivelmente intracraniano",
     "Usar IBP profilático (omeprazol 20 mg/dia) se combinação necessária. "
     "Preferir paracetamol como analgésico.",
     "CFM-SM"),

    ("Fluoxetina / Paroxetina (inibidores CYP2D6)", "Tamoxifeno",
     "Antidepressivos ISRS",
     "Inibição potente de CYP2D6 → redução da conversão de tamoxifeno em endoxifeno "
     "(metabólito ativo responsável pelo efeito antiestrogênico)",
     "grave",
     "Redução da eficácia do tamoxifeno com aumento do risco de recorrência do câncer de mama",
     "EVITAR fluoxetina e paroxetina em pacientes usando tamoxifeno. "
     "Substituir por ISRS com menor inibição CYP2D6: sertralina, citalopram ou escitalopram.",
     "INCA-ONCOL"),

    ("Sertralina / Fluoxetina (ISRS)", "IMAOs (fenelzina, tranilcipromina, selegilina)",
     "Inibidores da monoamino oxidase",
     "IMAOs bloqueiam degradação de serotonina + ISRS aumentam disponibilidade sináptica → "
     "superdose funcional de serotonina",
     "contraindicada",
     "Síndrome serotoninérgica grave com risco de morte",
     "CONTRAINDICADA. Washout mínimo de 14 dias após suspender ISRS antes de iniciar IMAO "
     "(5 semanas para fluoxetina pela meia-vida longa do metabólito ativo). "
     "Washout de 14 dias após suspender IMAO antes de iniciar ISRS.",
     "CFM-SM"),

    ("Lítio", "Diuréticos tiazídicos (hidroclorotiazida) / AINEs / IECA",
     "Diuréticos / Anti-inflamatórios / IECA",
     "Tiazídicos e AINEs reduzem a excreção renal de lítio (depletam sódio, aumentando reabsorção "
     "renal de lítio); IECAs reduzem TFG → menor excreção de lítio",
     "grave",
     "Toxicidade por lítio: tremores grosseiros, ataxia, confusão, delirium, coma, "
     "arritmias e insuficiência renal",
     "Monitorar nível sérico de lítio semanalmente ao iniciar ou ajustar qualquer um desses agentes. "
     "Hidratação adequada é essencial. Considerar ajuste de dose do lítio.",
     "CFM-SM"),

    ("Carbamazepina", "Contraceptivos orais combinados / Progestágenos",
     "Hormônios anticoncepcionais",
     "Carbamazepina é indutor potente de CYP3A4 → acelera o metabolismo dos estrogênios "
     "e progestinas → redução dos níveis séricos dos contraceptivos",
     "grave",
     "Falha contraceptiva com gravidez não planejada",
     "Orientar a paciente sobre o risco. Utilizar método contraceptivo não hormonal (DIU de cobre, "
     "preservativo) ou DIU hormonal de alta dose. "
     "Não confiar em contraceptivo oral como único método.",
     "ABN-EPILEPSIA"),

    ("Carbamazepina", "Clozapina",
     "Antipsicótico atípico",
     "Ambos podem causar agranulocitose por mecanismos distintos; interação farmacodinâmica aditiva "
     "no risco de toxicidade hematológica",
     "contraindicada",
     "Risco aumentado de agranulocitose grave com risco de morte por infecção",
     "CONTRAINDICADA a combinação. Usar valproato ou lamotrigina se necessário antiepiléptico "
     "em paciente com clozapina.",
     "ABN-EPILEPSIA"),

    ("Ácido valproico / Valproato", "Carbamazepina / Fenitoína",
     "Anticonvulsivantes",
     "Interação complexa bidirecional: valproato inibe o metabolismo de carbamazepina (↑ metabólito "
     "epóxido tóxico); carbamazepina e fenitoína induzem metabolismo do valproato (↓ nível sérico)",
     "moderada",
     "Toxicidade de carbamazepina por acúmulo de epóxido (diplopia, ataxia, náusea) e/ou "
     "redução da eficácia do valproato",
     "Monitorar níveis séricos de ambos os anticonvulsivantes. "
     "Ajustar doses conforme monitoração clínica e laboratorial.",
     "ABN-EPILEPSIA"),

    ("Fenitoína", "Antifúngicos azólicos (fluconazol)",
     "Antifúngicos sistêmicos",
     "Fluconazol inibe CYP2C9 → redução do metabolismo da fenitoína → acúmulo",
     "grave",
     "Intoxicação por fenitoína: nistagmo, diplopia, ataxia, sonolência, arritmias",
     "Monitorar nível sérico de fenitoína 2–3x na primeira semana de combinação. "
     "Ajustar dose da fenitoína conforme necessário.",
     "ABN-EPILEPSIA"),

    ("Fenitoína", "Corticosteroides (prednisona, dexametasona)",
     "Corticosteroides",
     "Fenitoína induz CYP3A4 → aceleração do metabolismo dos corticosteroides",
     "moderada",
     "Redução da eficácia do corticoide; risco de falha terapêutica em doenças autoimunes "
     "e transplantados",
     "Aumentar dose do corticoide ao iniciar fenitoína. "
     "Monitorar resposta clínica e ajustar conforme necessário.",
     "ABN-EPILEPSIA"),

    ("Antipsicóticos (haloperidol, quetiapina, risperidona)",
     "Amiodarona / Azitromicina / Ciprofloxacino / Moxifloxacino",
     "Antiarrítmico / Antibióticos",
     "Prolongamento aditivo do intervalo QTc: todos esses agentes bloqueiam canais de potássio "
     "cardíacos (hERG) reduzindo a repolarização ventricular",
     "contraindicada",
     "Torsades de Pointes e morte súbita por fibrilação ventricular",
     "Evitar combinação sempre que possível. Se indispensável: monitorar QTc no ECG antes, "
     "24–48h após início e periodicamente. Suspender se QTc > 500 ms.",
     "CFM-SM"),

    ("Levodopa / Carbidopa", "Antipsicóticos típicos (haloperidol, clorpromazina)",
     "Antipsicóticos típicos",
     "Bloqueio dos receptores D2 dopaminérgicos pelo antipsicótico → antagonismo direto "
     "do efeito dopaminérgico da levodopa",
     "contraindicada",
     "Redução da eficácia da levodopa com piora grave do parkinsonismo; pode precipitar "
     "síndrome neuroléptica maligna",
     "CONTRAINDICADA. Se psicose no Parkinson, preferir quetiapina (< bloqueio D2) ou clozapina. "
     "Evitar haloperidol, risperidona, olanzapina.",
     "ABN-PARKINSON"),

    # ══════════════════════════════════════════════════════════════════════
    # ENDÓCRINO / METABÓLICO
    # ══════════════════════════════════════════════════════════════════════

    ("Metformina", "Contraste iodado IV (exames de imagem)",
     "Agente de contraste radiológico",
     "Contraste iodado pode causar IRA transitória → metformina acumula em ambiente de DRC → "
     "inibição da cadeia respiratória mitocondrial hepática → acidose láctica",
     "grave",
     "Acidose láctica grave com mortalidade elevada",
     "Suspender metformina 48h antes do contraste IV. "
     "Reintroduzir 48h após o procedimento, confirmando função renal estável.",
     "SBD-DM2"),

    ("Sulfonilureias (glibenclamida, glipizida)", "Fluconazol / Outros azólicos",
     "Antifúngicos sistêmicos",
     "Inibição de CYP2C9 → redução do metabolismo das sulfonilureias → aumento prolongado "
     "dos níveis séricos",
     "grave",
     "Hipoglicemia grave e prolongada",
     "Monitorar glicemia com frequência aumentada (4–6x/dia) ao iniciar azólico. "
     "Reduzir dose da sulfonilureia em 25–50% conforme necessário.",
     "SBD-DM2"),

    ("Levotiroxina", "Carbonato de cálcio / Hidróxido de alumínio / Sucralfato / Colestiramina",
     "Antiácidos / Quelantes / Resinas de troca iônica",
     "Quelação da levotiroxina no trato GI → redução da absorção oral",
     "moderada",
     "Hipotireoidismo por absorção insuficiente de levotiroxina; elevação do TSH",
     "Administrar levotiroxina pelo menos 4h antes ou 4h após esses medicamentos. "
     "Monitorar TSH 4–6 semanas após qualquer mudança na terapia concomitante.",
     "PCDT-HIPOTIREOID"),

    ("SGLT-2 (empagliflozina, dapagliflozina)", "Diuréticos de alça (furosemida)",
     "Diuréticos",
     "Efeito natriurético e diurético sinérgico: SGLT-2 promove glicosúria com perda osmótica "
     "de fluido + diurético de alça → depleção volumétrica acentuada",
     "moderada",
     "Hipotensão ortostática, depleção volumétrica, IRA pré-renal especialmente em idosos",
     "Iniciar SGLT-2 com dose reduzida do diurético quando possível. "
     "Orientar paciente sobre hidratação adequada. "
     "Monitorar pressão arterial, creatinina e eletrólitos nas primeiras 4 semanas.",
     "SBD-DM2"),

    ("GLP-1 agonistas (semaglutida, liraglutida)", "Insulina (NPH, glargina, lispro)",
     "Insulina",
     "GLP-1 aumenta a secreção de insulina glicose-dependente e retarda esvaziamento gástrico "
     "→ efeito hipoglicêmico aditivo à insulina exógena",
     "moderada",
     "Hipoglicemia, especialmente nas primeiras 4–8 semanas de associação",
     "Reduzir dose da insulina basal em 20% ao iniciar GLP-1 agonista. "
     "Monitorar glicemia em jejum diariamente na fase de ajuste. "
     "Titular insulina com cautela.",
     "SBD-DM2"),

    ("Alopurinol", "Azatioprina / 6-mercaptopurina",
     "Imunossupressores tiopurínicos",
     "Inibição da xantina oxidase pelo alopurinol bloqueia inativação de 6-MP/azatioprina "
     "→ acúmulo de metabólitos tiopurínicos ativos",
     "contraindicada",
     "Mielotoxicidade grave: leucopenia, trombocitopenia, anemia aplástica",
     "CONTRAINDICADA a combinação em doses habituais. "
     "Se indispensável: reduzir a dose de azatioprina em 75% e monitorar CBC semanalmente. "
     "Considerar febuxostate como alternativa.",
     "SBR-AR"),

    # ══════════════════════════════════════════════════════════════════════
    # RESPIRATÓRIO / GI / ONCOLÓGICO / OUTROS
    # ══════════════════════════════════════════════════════════════════════

    ("Tiotrópio", "Anticolinérgicos sistêmicos (oxibutinina, solifenacina, tricíclicos)",
     "Anticolinérgicos",
     "Efeitos anticolinérgicos aditivos: bloqueio de receptores muscarínicos em múltiplos órgãos",
     "moderada",
     "Retenção urinária, constipação, boca seca grave, confusão (idosos), "
     "taquicardia, glaucoma de ângulo fechado",
     "Avaliar carga anticolinérgica total (escala ACB). "
     "Monitorar função urinária e sintomas GI especialmente em idosos.",
     "PCDT-DPOC"),

    ("Omeprazol", "Clopidogrel",
     "Antiplaquetário (pró-fármaco)",
     "Omeprazol inibe CYP2C19 → redução da ativação do clopidogrel para seu metabólito ativo "
     "(tiol) responsável pelo efeito antiagregante",
     "moderada",
     "Redução de até 40% da inibição plaquetária pelo clopidogrel; possível aumento "
     "de eventos cardiovasculares em estudos observacionais",
     "Preferir pantoprazol (menor inibição de CYP2C19) quando IBP for necessário. "
     "Revisão da combinação em pacientes de alto risco cardiovascular.",
     "SBC-SCA"),

    ("Alendronato", "IBP (omeprazol, pantoprazol) / Antiácidos",
     "Inibidores de bomba de prótons / Antiácidos",
     "IBP alteram pH gástrico e podem aumentar risco de esofagite (aumento tempo de contato "
     "com mucosa); antiácidos quelam alendronato → redução de absorção",
     "moderada",
     "Esofagite (se IBP não tomado corretamente); redução de absorção do alendronato",
     "Orientar posologia correta do alendronato: 30–60 min antes de qualquer medicamento, "
     "com copo cheio de água, permanecendo ereto por 30 min. "
     "Separar antiácidos por pelo menos 2h.",
     "PCDT-OSTEOPOROSE"),

    ("Imatinibe", "Inibidores potentes de CYP3A4 (cetoconazol, claritromicina, ritonavir)",
     "Antifúngicos / Antibióticos / Antirretrovirais",
     "Inibição de CYP3A4 → redução do metabolismo do imatinibe → aumento dos níveis séricos",
     "moderada",
     "Toxicidade do imatinibe: edema, náusea, retenção hídrica, citopenia",
     "Monitorar toxicidade clínica e laboratorial. Considerar redução temporária de dose "
     "de imatinibe ou substituição do agente interagente.",
     "INCA-ONCOL"),

    ("Imatinibe", "Indutores potentes de CYP3A4 (rifampicina, carbamazepina, fenitoína)",
     "Antibióticos rifamicinas / Anticonvulsivantes",
     "Indução de CYP3A4 → aceleração do metabolismo do imatinibe → redução dos níveis séricos",
     "grave",
     "Redução da eficácia do imatinibe com risco de progressão da LMC ou GIST",
     "Evitar indutores potentes. Se necessário, aumentar dose do imatinibe em até 50% "
     "com monitoração de resposta molecular.",
     "INCA-ONCOL"),

    ("Metronidazol", "Álcool etílico / Dissulfiram",
     "Bebidas alcoólicas / Agente antialcoólico",
     "Metronidazol inibe acetaldeído desidrogenase → acúmulo de acetaldeído após ingestão "
     "de álcool; dissulfiram pode somar o efeito",
     "grave",
     "Reação dissulfiram-like: rubor facial intenso, cefaleia, taquicardia, náusea, "
     "vômitos, hipotensão",
     "Orientar paciente a evitar álcool durante o uso de metronidazol e por 48h após o término. "
     "Não associar com dissulfiram.",
     "CFM-SM"),

    ("Tofacitinibe / Baricitinibe (JAK inibidores)",
     "Biológicos (anti-TNF, anti-IL-6, anti-CD20)",
     "Imunobiológicos",
     "Imunossupressão aditiva profunda por bloqueio simultâneo de múltiplas vias inflamatórias",
     "contraindicada",
     "Infecções oportunistas graves (TB, aspergilose, pneumocistose), reativação de herpes zoster, "
     "herpes simplex e CMV",
     "CONTRAINDICADA a combinação de JAK inibidor com biológico. "
     "Usar um ou outro. Washout de pelo menos 5 meias-vidas antes da transição.",
     "PCDT-AR"),

    ("Darbepoetina alfa / Eritropoetina", "Ferro IV (sacarato/ferric carboxymaltose)",
     "Suplemento de ferro parenteral",
     "Interação sinérgica benéfica: ferro IV supre substrato necessário para eritropoiese "
     "estimulada por agentes estimuladores de eritropoiese (AEE)",
     "leve",
     "Sem efeito adverso; associação necessária para resposta eritropoiética ótima. "
     "Sem ferro adequado, há resistência ao AEE",
     "Administrar ferro IV conforme necessidade (ferritina < 200 ng/mL ou IST < 20%) "
     "para otimizar a resposta à darbepoetina. Monitorar parâmetros de ferro mensalmente.",
     "PCDT-DRC"),

]

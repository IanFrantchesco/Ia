"""
Interações medicamentosas clinicamente relevantes para antivirais.
Fontes: PCDT MS (HIV 2022, Hepatite B 2022, Hepatite C 2022), Bulário ANVISA,
        Micromedex Brasil, SBI, UpToDate adaptado ao formulário BR,
        Liverpool HIV Interactions / HEP Drug Interactions (referências globais).

Formato:
(antiviral_nome, medicamento_interagente, classe_interagente,
 mecanismo, gravidade, efeito_clinico, conduta, fonte_sigla)

Gravidade: 'contraindicada' | 'grave' | 'moderada' | 'leve'
"""

INTERACOES_VIRAIS = [

    # ══════════════════════════════════════════════════════════════════
    # DOLUTEGRAVIR (DTG) — INSTI
    # ══════════════════════════════════════════════════════════════════
    ("Dolutegravir (DTG)", "Rifampicina",
     "Rifamicina / antituberculose", "Indução potente de CYP3A4 e UGT1A1 — reduz AUC do DTG em ~57%",
     "grave", "Risco de falha virológica e seleção de mutações de resistência do HIV",
     "Dobrar dose do DTG para 50 mg 12/12h durante co-uso com rifampicina. Alternativa: substituir rifampicina por rifabutina (sem ajuste de DTG) se disponível.", "PCDT-HIV"),

    ("Dolutegravir (DTG)", "Antiácidos com cátions polivalentes (Al³⁺, Mg²⁺, Ca²⁺, Fe²⁺/Fe³⁺, Zn²⁺)",
     "Antiácidos / Suplementos minerais", "Quelação no trato gastrointestinal — reduz absorção oral do DTG em até 74%",
     "grave", "Concentração plasmática subterapêutica com risco de falha virológica",
     "Administrar DTG pelo menos 2h ANTES ou 6h APÓS antiácidos, suplementos de ferro ou zinco. Carbonato de cálcio com alimentos tem menor impacto.", "PCDT-HIV"),

    ("Dolutegravir (DTG)", "Metformina",
     "Antidiabético oral (biguanida)", "Inibição do transportador de cátions orgânicos OCT2/MATE1 — reduz excreção renal da metformina em ~79%",
     "moderada", "Aumento dos níveis séricos de metformina com risco de acidose lática e hipoglicemia",
     "Reduzir dose de metformina para máximo de 1g/dia ao iniciar DTG. Monitorar glicemia e lactato. Reavaliar ao suspender DTG.", "PCDT-HIV"),

    ("Dolutegravir (DTG)", "Carbamazepina / Fenitoína / Fenobarbital / Oxcarbamazepina",
     "Antiepilépticos indutores", "Indução de CYP3A4 e UGT1A1 — reduz concentrações do DTG significativamente",
     "grave", "Falha virológica por concentrações subterapêuticas de DTG",
     "Dobrar dose do DTG para 50 mg 12/12h. Considerar trocar antiepiléptico para levetiracetam ou lamotrigina (sem interação). Monitorar CV do HIV.", "PCDT-HIV"),

    # ══════════════════════════════════════════════════════════════════
    # LOPINAVIR/RITONAVIR (LPV/r) — IP
    # ══════════════════════════════════════════════════════════════════
    ("Lopinavir/ritonavir (LPV/r)", "Rifampicina",
     "Rifamicina / antituberculose", "Rifampicina é indutor potente do CYP3A4 — reduz níveis de LPV/r em 75-89%",
     "contraindicada", "Falha virológica garantida; não é possível compensar adequadamente com aumento de dose",
     "CONTRAINDICADA. Substituir o IP por raltegravir 400 mg 12/12h ou dolutegravir 50 mg 12/12h (com ajuste de dose) durante tratamento de TB.", "PCDT-HIV"),

    ("Lopinavir/ritonavir (LPV/r)", "Estatinas metabolizadas por CYP3A4 (sinvastatina, lovastatina)",
     "Hipolipemiantes", "Ritonavir inibe potentemente CYP3A4 — eleva concentrações da estatina em 20-50x",
     "contraindicada", "Rabdomiólise grave com insuficiência renal aguda",
     "CONTRAINDICADA com sinvastatina e lovastatina. Usar apenas pravastatina, rosuvastatina (cautela) ou pitavastatina com IPs.", "PCDT-HIV"),

    ("Lopinavir/ritonavir (LPV/r)", "Anticoncepcionais hormonais orais (etinilestradiol/noretisterona)",
     "Hormônios contraceptivos", "Ritonavir induz CYP3A4 — reduz concentrações de etinilestradiol em ~42%",
     "grave", "Risco de falha contraceptiva e gravidez não planejada",
     "Usar método contraceptivo de barreira (preservativo) durante toda a TAR com IP/ritonavir. Considerar DIU de cobre como alternativa altamente eficaz.", "PCDT-HIV"),

    ("Lopinavir/ritonavir (LPV/r)", "Sildenafila (para hipertensão pulmonar)",
     "Inibidor de PDE-5", "Ritonavir inibe CYP3A4 — eleva concentrações de sildenafila em 11x",
     "grave", "Hipotensão grave, priapismo, alterações visuais",
     "Sildenafila para disfunção erétil: reduzir para 25 mg a cada 48h. Para hipertensão pulmonar: iniciar com dose muito baixa e titular com cautela extrema.", "PCDT-HIV"),

    ("Lopinavir/ritonavir (LPV/r)", "Medicamentos que prolongam QT (amiodarona, sotalol, eritromicina IV, haloperidol)",
     "Agentes pró-arrítmicos", "Inibição de CYP3A4 + bloqueio hERG pelo ritonavir",
     "contraindicada", "Torsades de pointes e morte súbita cardíaca",
     "CONTRAINDICADA com amiodarona, dronedarona, flecainida, propafenona. ECG basal obrigatório antes de iniciar LPV/r.", "ANVISA-VIRAL"),

    # ══════════════════════════════════════════════════════════════════
    # NIRMATRELVIR/RITONAVIR (NMV/r — Paxlovid) — antiCOVID
    # ══════════════════════════════════════════════════════════════════
    ("Nirmatrelvir/Ritonavir (NMV/r)", "Imunossupressores (ciclosporina, tacrolimo, sirolimo, everolimo)",
     "Imunossupressores / antijeição", "Ritonavir inibe potentemente CYP3A4 e P-gp — eleva concentrações do imunossupressor em 2-10x",
     "contraindicada", "Nefrotoxicidade grave, toxicidade neurológica, rejeição paradoxal por superdosagem",
     "CONTRAINDICADO sem manejo especializado. Se uso obrigatório em transplantado: reduzir dose do imunossupressor drasticamente, monitorar nível sérico diariamente. Consultar centro de transplante.", "PCDT-COVID19"),

    ("Nirmatrelvir/Ritonavir (NMV/r)", "Anticoagulantes orais diretos (rivaroxabana, apixabana, dabigatrana)",
     "Anticoagulantes orais diretos", "Ritonavir inibe CYP3A4 e P-gp — eleva concentrações dos AODs em 2-5x",
     "contraindicada", "Hemorragia grave e potencialmente fatal",
     "CONTRAINDICADO com rivaroxabana e apixabana. Para dabigatrana: avaliar risco. Alternativa: substituir temporariamente por heparina de baixo peso molecular durante os 5 dias de Paxlovid.", "PCDT-COVID19"),

    ("Nirmatrelvir/Ritonavir (NMV/r)", "Estatinas metabolizadas por CYP3A4 (sinvastatina, atorvastatina, lovastatina)",
     "Hipolipemiantes", "Ritonavir inibe CYP3A4 — eleva concentrações da estatina",
     "grave", "Miopatia e rabdomiólise",
     "SUSPENDER sinvastatina e lovastatina durante os 5 dias de Paxlovid. Atorvastatina: suspender ou reduzir para dose mínima. Reiniciar 2-3 dias após última dose de Paxlovid.", "PCDT-COVID19"),

    ("Nirmatrelvir/Ritonavir (NMV/r)", "Antiepilépticos (carbamazepina, fenitoína, fenobarbital)",
     "Antiepilépticos indutores", "Indução de CYP3A4 — reduz concentrações de nirmatrelvir; e efeito recíproco",
     "contraindicada", "Falha terapêutica do Paxlovid (subdosagem de nirmatrelvir) E risco de toxicidade do antiepiléptico",
     "CONTRAINDICADA. Paxlovid não deve ser usado em pacientes em uso de antiepilépticos indutores sem supervisão especializada.", "PCDT-COVID19"),

    ("Nirmatrelvir/Ritonavir (NMV/r)", "Colchicina",
     "Antigotoso / anti-inflamatório", "Inibição CYP3A4 e P-gp pelo ritonavir — eleva concentrações de colchicina",
     "contraindicada", "Toxicidade grave por colchicina: miopatia, aplasia medular, insuficiência de múltiplos órgãos",
     "CONTRAINDICADA em insuficiência renal ou hepática. Em função preservada: suspender colchicina durante os 5 dias de Paxlovid.", "PCDT-COVID19"),

    # ══════════════════════════════════════════════════════════════════
    # SOFOSBUVIR / DAAs PARA HCV
    # ══════════════════════════════════════════════════════════════════
    ("Sofosbuvir/Ledipasvir (SOF/LED)", "Amiodarona",
     "Antiarrítmico", "Mecanismo incerto — possível inibição de canais cardíacos",
     "contraindicada", "Bradicardia sintomática grave, bloqueio cardíaco completo e morte — casos relatados",
     "CONTRAINDICADA com amiodarona. Pacientes que usaram amiodarona nos últimos 6 meses: monitorização cardíaca hospitalar por 48h se imprescindível. Aguardar eliminação da amiodarona antes de iniciar SOF-based DAA.", "PCDT-HEPC"),

    ("Sofosbuvir/Ledipasvir (SOF/LED)", "Antiácidos com Al³⁺/Mg²⁺, inibidores de bomba de próton",
     "Antiácidos / IBPs", "Aumento do pH gástrico — reduz solubilidade e absorção do ledipasvir em 35-71%",
     "moderada", "Concentrações subterapêuticas de ledipasvir com risco de falha virológica",
     "IBPs: tomar SOF/LED 4h antes do IBP com dose equivalente ≤ 20 mg omeprazol. Antiácidos: separar por 4h. SOF/VEL e GLE/PIB têm interações similares com IBPs — atenção.", "PCDT-HEPC"),

    ("Sofosbuvir/Velpatasvir (SOF/VEL)", "Rifampicina",
     "Rifamicina / antituberculose", "Indução de CYP2B6, CYP3A4 e P-gp — reduz AUC de SOF em 72% e VEL em 82%",
     "contraindicada", "Falha virológica garantida no tratamento do HCV",
     "CONTRAINDICADA. Tratar HCV e TB sequencialmente quando possível: completar TB primeiro ou iniciar HCV após fim da rifampicina. Alternativa: rifabutina (menor indução) com ajuste.", "PCDT-HEPC"),

    ("Glecaprevir/Pibrentasvir (GLE/PIB)", "Rifampicina e rifabutina",
     "Rifamicinas", "Indução de P-gp e OATP1B1/B3 — reduz glecaprevir drasticamente",
     "contraindicada", "Concentrações de GLE insuficientes para tratamento do HCV",
     "CONTRAINDICADA com rifampicina e rifabutina. Tratar TB e HCV sequencialmente.", "PCDT-HEPC"),

    ("Glecaprevir/Pibrentasvir (GLE/PIB)", "Estatinas (rosuvastatina, atorvastatina, sinvastatina, pravastatina)",
     "Hipolipemiantes", "Inibição de OATP1B1/B3 e P-gp pelo glecaprevir — eleva concentrações das estatinas",
     "grave", "Miopatia e rabdomiólise, especialmente com rosuvastatina (aumenta 5x)",
     "Contraindicada com lovastatina e sinvastatina. Rosuvastatina: suspender durante tratamento. Atorvastatina e fluvastatina: reduzir para metade da dose. Pravastatina: cautela (aumenta 35%).", "PCDT-HEPC"),

    ("Daclatasvir (DCV)", "Rifampicina",
     "Rifamicina / antituberculose", "Indução CYP3A4 e P-gp — reduz AUC do DCV em 79%",
     "contraindicada", "Falha virológica no tratamento do HCV",
     "CONTRAINDICADA com rifampicina. Com rifabutina: aumentar dose do DCV para 90 mg/dia.", "PCDT-HEPC"),

    ("Daclatasvir (DCV)", "Carbamazepina / Fenitoína / Fenobarbital",
     "Antiepilépticos indutores", "Indução CYP3A4 — reduz concentrações de DCV",
     "contraindicada", "Falha virológica no tratamento do HCV",
     "CONTRAINDICADA. Trocar antiepiléptico para levetiracetam ou lamotrigina (sem interação com DCV).", "PCDT-HEPC"),

    # ══════════════════════════════════════════════════════════════════
    # TENOFOVIR DISOPROXILA (TDF) — HIV e HBV
    # ══════════════════════════════════════════════════════════════════
    ("Tenofovir disoproxila (TDF)", "AINEs nefrotóxicos (ibuprofeno, diclofenaco) e aminoglicosídeos",
     "AINEs / Aminoglicosídeos", "Nefrotoxicidade aditiva — TDF causa disfunção tubular proximal (síndrome de Fanconi)",
     "grave", "Insuficiência renal aguda e toxicidade tubular (hipofosfatemia, acidose metabólica)",
     "Evitar uso prolongado de AINEs com TDF. Monitorar creatinina, fósforo e pH urinário mensalmente. Considerar substituição para TAF se insuficiência renal progressiva.", "PCDT-HIV"),

    ("Tenofovir disoproxila (TDF)", "Atazanavir (ATV)",
     "Inibidor de protease", "ATV aumenta concentrações de TDF em 24-37% por inibição de P-gp/MRP4",
     "moderada", "Maior risco de toxicidade renal pelo TDF",
     "Monitorar função renal mensalmente com ATV+TDF. Considerar substituição de TDF por TAF ou ABC.", "PCDT-HIV"),

    # ══════════════════════════════════════════════════════════════════
    # ACICLOVIR / VALACICLOVIR
    # ══════════════════════════════════════════════════════════════════
    ("Aciclovir (ACV)", "Probenecida e Cimetidina",
     "Uricosúrico / Antiulceroso H2", "Competição pela secreção tubular renal — aumenta AUC do aciclovir",
     "leve", "Aumento das concentrações de aciclovir — pode ser benéfico ou causar toxicidade em insuficiência renal",
     "Reduzir dose de aciclovir em pacientes com insuficiência renal que usam probenecida ou cimetidina. Monitorar sinais de toxicidade neurológica.", "SBI-VIRAL"),

    ("Aciclovir (ACV)", "Nefrotóxicos (aminoglicosídeos, cisplatina, ciclosporina, anfotericina B)",
     "Nefrotóxicos diversos", "Nefrotoxicidade aditiva — aciclovir pode precipitar em túbulos renais",
     "grave", "Insuficiência renal aguda, especialmente em altas doses IV",
     "Manter hidratação adequada durante aciclovir IV (pelo menos 500 mL antes da infusão). Monitorar creatinina 2x/dia em pacientes com outros nefrotóxicos.", "SBI-VIRAL"),

    ("Aciclovir (ACV)", "Metotrexato (MTX)",
     "Antineoplásico / imunossupressor", "Competição pelo transportador renal de folato e redução da excreção do MTX",
     "moderada", "Toxicidade aumentada do metotrexato: mucosite, pancitopenia, nefrotoxicidade",
     "Monitorar hemograma e creatinina. Reduzir dose de MTX se necessário. Preferir valaciclovir oral em vez de aciclovir IV quando possível.", "SBI-VIRAL"),

    # ══════════════════════════════════════════════════════════════════
    # GANCICLOVIR / VALGANCICLOVIR
    # ══════════════════════════════════════════════════════════════════
    ("Ganciclovir (GCV)", "Imipenem-cilastatina",
     "Carbapenem", "Mecanismo incerto — potencial convulsivo aditivo",
     "grave", "Convulsões generalizadas — casos relatados na literatura",
     "Evitar co-administração de ganciclovir IV com imipenem. Usar meropenem como alternativa ao imipenem em pacientes em uso de ganciclovir.", "SBI-VIRAL"),

    ("Ganciclovir (GCV)", "Zidovudina (AZT) e outros mielotóxicos",
     "Análogo nucleosídico / mielotóxico", "Mielossupressão aditiva — ambos suprimem proliferação de progenitores mieloides",
     "grave", "Anemia e neutropenia graves, potencialmente fatal",
     "Evitar co-administração. Se imprescindível (CMV + HIV com AZT): monitorar CBC semanalmente e considerar G-CSF profilático. Substituir AZT por outro ITRN quando possível.", "SBI-VIRAL"),

    ("Ganciclovir (GCV)", "Micofenolato mofetil (MMF)",
     "Imunossupressor antiproliferativo", "Competição pelo transportador tubular renal — pode elevar concentrações de ambos",
     "moderada", "Toxicidade hematológica aumentada (leucopenia, anemia)",
     "Monitorar CBC semanalmente. Considerar redução de dose de MMF. Risco maior em pacientes com insuficiência renal.", "SBI-VIRAL"),

    # ══════════════════════════════════════════════════════════════════
    # FOSCARNET
    # ══════════════════════════════════════════════════════════════════
    ("Foscarnet (PFA)", "Aminoglicosídeos / Anfotericina B / Ciclosporina",
     "Nefrotóxicos", "Nefrotoxicidade aditiva por dano tubular direto",
     "contraindicada", "Insuficiência renal aguda grave — incidência > 70% com combinação",
     "EVITAR combinação sempre que possível. Se imprescindível: hidratação IV agressiva (1L SF antes e depois de cada infusão), monitorar creatinina 2x/dia.", "SBI-VIRAL"),

    ("Foscarnet (PFA)", "Medicamentos que prolongam QT (pentamidina, eritromicina IV, antipsicóticos)",
     "Agentes pró-arrítmicos", "Hipocalcemia induzida pelo foscarnet + bloqueio de canais hERG pelos outros agentes",
     "grave", "Torsades de pointes — especialmente pelo efeito quelante do cálcio pelo foscarnet",
     "Monitorar Ca²⁺, Mg²⁺ e ECG antes e durante o tratamento. Corrigir distúrbios eletrolíticos antes de iniciar.", "SBI-VIRAL"),

    # ══════════════════════════════════════════════════════════════════
    # OSELTAMIVIR (influenza)
    # ══════════════════════════════════════════════════════════════════
    ("Oseltamivir (OST)", "Probenecida",
     "Uricosúrico", "Inibição da secreção tubular ativa — reduz excreção renal do oseltamivir carboxilato (metabólito ativo) em ~50%",
     "moderada", "Aumento da exposição ao oseltamivir — pode ser útil em resistência mas aumenta risco de toxicidade gastrointestinal",
     "Monitorar efeitos adversos (náuseas, vômitos). Em pacientes com insuficiência renal grave: risco de toxicidade neurológica; ajustar dose.", "PCDT-INFLUENZA"),

    ("Oseltamivir (OST)", "Vacina viva atenuada de influenza (FluMist/Fluenz)",
     "Vacina viral viva", "Inibição da replicação viral — pode reduzir eficácia da vacina intranasal viva",
     "moderada", "Redução da imunogenicidade da vacina intranasal viva",
     "Não administrar vacina intranasal viva nos 2 dias antes até 2 semanas após o uso de oseltamivir. Vacina inativada injectable não é afetada.", "PCDT-INFLUENZA"),

    # ══════════════════════════════════════════════════════════════════
    # REMDESIVIR (COVID-19)
    # ══════════════════════════════════════════════════════════════════
    ("Remdesivir (RDV)", "Cloroquina e Hidroxicloroquina",
     "Antimalárico / antirreumático", "Antagonismo farmacológico — cloroquina inibe a ativação intracelular do remdesivir",
     "contraindicada", "Redução significativa da atividade antiviral do remdesivir contra SARS-CoV-2 in vitro",
     "CONTRAINDICADA combinação. Não usar hidroxicloroquina/cloroquina com remdesivir.", "PCDT-COVID19"),

    ("Remdesivir (RDV)", "Indutores potentes de CYP3A4 (rifampicina, carbamazepina, fenitoína)",
     "Indutores enzimáticos", "Indução de CYP3A4 — pode reduzir concentrações do remdesivir",
     "moderada", "Possível redução da eficácia antiviral",
     "Evitar co-administração com indutores potentes. Monitorar resposta clínica.", "PCDT-COVID19"),

    # ══════════════════════════════════════════════════════════════════
    # ENTECAVIR (HBV)
    # ══════════════════════════════════════════════════════════════════
    ("Entecavir (ETV)", "Medicamentos nefrotóxicos (aminoglicosídeos, AINEs, ciclosporina, anfotericina B)",
     "Nefrotóxicos", "Nefrotoxicidade aditiva — entecavir é excretado por via renal",
     "moderada", "Acúmulo de entecavir e aumento do risco de acidose lática e toxicidade renal",
     "Monitorar função renal e ajustar dose de entecavir conforme ClCr. Evitar combinação com nefrotóxicos quando possível.", "PCDT-HEPB"),

    ("Entecavir (ETV)", "Lamivudina / Adefovir (em pacientes refratários)",
     "Análogos nucleosídicos / anti-HBV", "Resistência cruzada: mutação de resistência à lamivudina (M204I/V) reduz barreira genética ao entecavir",
     "grave", "Risco aumentado de falha virológica e desenvolvimento de resistência ao entecavir em pacientes previamente expostos à lamivudina",
     "Em pacientes lamivudina-refratários: usar entecavir 1 mg/dia (em vez de 0,5 mg) OU trocar para tenofovir. Preferir tenofovir como 1ª opção nesses casos.", "PCDT-HEPB"),

    # ══════════════════════════════════════════════════════════════════
    # INTERFERON PEGUILADO (HBV / HCV)
    # ══════════════════════════════════════════════════════════════════
    ("Interferon alfa-2a peguilado (Peg-IFN-α2a)", "Telbivudina (HBV)",
     "Análogo nucleosídico anti-HBV", "Neurotoxicidade aditiva — mecanismo incerto",
     "contraindicada", "Neuropatia periférica grave — casos relatados na combinação",
     "CONTRAINDICADA a combinação de Peg-IFN com telbivudina. Não usar telbivudina simultaneamente ao interferon.", "PCDT-HEPB"),

    ("Interferon alfa-2a peguilado (Peg-IFN-α2a)", "Antidiabéticos (insulina e antidiabéticos orais)",
     "Hipoglicemiantes", "Interferon pode causar hipo ou hiperglicemia por efeito em células beta pancreáticas",
     "moderada", "Desregulação glicêmica imprevisível — tanto hipoglicemia quanto diabetes mellitus autoimune",
     "Monitorar glicemia em jejum mensalmente. Ajustar dose de insulina ou hipoglicemiante conforme necessário. Atenção ao diabetes tipo 1 autoimune induzido por interferon.", "PCDT-HEPB"),

    ("Interferon alfa-2a peguilado (Peg-IFN-α2a)", "Anticoagulantes orais (varfarina)",
     "Anticoagulante", "Interferon reduz atividade de CYP1A2 e CYP2C9 — altera metabolismo da varfarina",
     "moderada", "Variação imprevisível do INR — tanto elevação quanto queda",
     "Monitorar INR 2x/semana no primeiro mês de interferon e ao suspendê-lo. Ajustar dose de varfarina conforme resposta.", "PCDT-HEPC"),

    ("Interferon alfa-2a peguilado (Peg-IFN-α2a)", "Zidovudina (AZT) em coinfectados HIV/HCV",
     "Análogo nucleosídico / mielotóxico", "Mielossupressão aditiva",
     "grave", "Anemia e neutropenia graves; síndrome de depleção mitocondrial",
     "Evitar AZT durante tratamento com interferon. Substituir AZT por tenofovir ou abacavir no esquema ARV.", "PCDT-HEPC"),
]

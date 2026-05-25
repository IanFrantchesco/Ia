"""
Dados de interações medicamentosas de antifúngicos.
Fontes: PCDT-PARACOC MS 2022, SBI-CAND, SBI-ASPERG, SBI-CRIPTO, ANVISA-ANTIF,
        PCDT-HIV-FUNG, SBD-MICOSES, SBMT-FUNGOS.

Formato: (antifungico_nome, medicamento_interagente, classe_interagente,
          mecanismo, gravidade, efeito_clinico, conduta, fonte_sigla)

Gravidades: 'contraindicada', 'grave', 'moderada', 'leve'
"""

INTERACOES_FUNGICAS = [

    # ══════════════════════════════════════════════════════════════════
    # FLUCONAZOL
    # ══════════════════════════════════════════════════════════════════
    ("Fluconazol", "Terfenadina", "Anti-histamínico (1ª geração)",
     "Inibição de CYP3A4 pelo fluconazol aumenta nível de terfenadina",
     "contraindicada",
     "Prolongamento grave do intervalo QT, risco de torsades de pointes e morte súbita",
     "CONTRAINDICADO — substituir por anti-histamínico de 2ª geração sem risco cardíaco (loratadina, cetirizina)",
     "ANVISA-ANTIF"),

    ("Fluconazol", "Astemizol", "Anti-histamínico (1ª geração)",
     "Inibição de CYP3A4 eleva nível de astemizol",
     "contraindicada",
     "Prolongamento do QT, torsades de pointes",
     "CONTRAINDICADO — não coadministrar. Substituir anti-histamínico",
     "ANVISA-ANTIF"),

    ("Fluconazol", "Cisaprida", "Pró-cinético",
     "Inibição CYP3A4 — elevação de cisaprida plasmática",
     "contraindicada",
     "Prolongamento QT grave, arritmias ventriculares",
     "CONTRAINDICADO — cisaprida retirada de vários mercados. Usar metoclopramida se necessário",
     "ANVISA-ANTIF"),

    ("Fluconazol", "Ergotamina / Ergometrina", "Alcalóide do ergot",
     "Inibição CYP3A4 aumenta nível de ergotamina",
     "contraindicada",
     "Vasoespasmo grave, ergotismo (isquemia de extremidades, gangrena)",
     "CONTRAINDICADO — suspender ergotamina antes de fluconazol. Usar sumatriptana como alternativa",
     "ANVISA-ANTIF"),

    ("Fluconazol", "Varfarina", "Anticoagulante (cumarínico)",
     "Inibição CYP2C9 reduz metabolismo da varfarina (S-varfarina)",
     "grave",
     "Aumento significativo do INR — risco de hemorragia grave (cerebral, digestiva)",
     "Monitorar INR a cada 2–3 dias na primeira semana; reduzir dose de varfarina em 25–50%. "
     "Ajuste de dose após estabilização",
     "ANVISA-ANTIF"),

    ("Fluconazol", "Fenitoína", "Antiepiléptico",
     "Inibição CYP2C9 reduz metabolismo da fenitoína",
     "grave",
     "Aumento dos níveis séricos de fenitoína — toxicidade: nistagmo, ataxia, confusão",
     "Monitorar nível sérico de fenitoína (meta: 10–20 µg/mL). Reduzir dose se necessário",
     "ANVISA-ANTIF"),

    ("Fluconazol", "Rifampicina", "Rifamicina (antimicobacteriano)",
     "Rifampicina é potente indutor de CYP3A4 — reduz nível de fluconazol",
     "grave",
     "Redução de até 25% da AUC do fluconazol — risco de falha terapêutica antifúngica",
     "Aumentar dose de fluconazol (considerar dobrar dose). Monitorar resposta clínica. "
     "Alternativa: voriconazol (mas também tem interação com rifampicina)",
     "PCDT-HIV-FUNG"),

    ("Fluconazol", "Sirolimo", "Imunossupressor (mTOR)",
     "Inibição CYP3A4 e P-gp aumenta nível de sirolimo",
     "grave",
     "Nefrotoxicidade, mielotoxicidade por superdosagem de sirolimo",
     "Reduzir dose de sirolimo em 75–90% e monitorar nível sérico diariamente na fase inicial",
     "SBI-CAND"),

    ("Fluconazol", "Tacrolimo", "Imunossupressor (inibidor calcineurina)",
     "Inibição CYP3A4 eleva nível de tacrolimo",
     "grave",
     "Nefrotoxicidade, neurotoxicidade por nível elevado de tacrolimo",
     "Reduzir dose de tacrolimo em 50–75%. Monitorar nível sérico 2–3×/semana",
     "SBI-CAND"),

    ("Fluconazol", "Ciclosporina", "Imunossupressor (inibidor calcineurina)",
     "Inibição CYP3A4 e P-gp eleva nível de ciclosporina",
     "grave",
     "Nefrotoxicidade e hepatotoxicidade por superdosagem de ciclosporina",
     "Reduzir dose de ciclosporina em 50%. Monitorar nível sérico frequentemente",
     "SBI-CAND"),

    ("Fluconazol", "Sulfonilureias (glibenclamida, glipizida)", "Antidiabético oral",
     "Inibição CYP2C9 reduz metabolismo de sulfonilureias",
     "grave",
     "Hipoglicemia grave, especialmente em idosos e com jejum",
     "Monitorar glicemia mais frequentemente. Reduzir dose de sulfonilureia ou trocar por metformina",
     "ANVISA-ANTIF"),

    ("Fluconazol", "Metadona", "Opioide (dependência química)",
     "Inibição CYP3A4 e CYP2C9 eleva nível de metadona",
     "grave",
     "Prolongamento QT, sedação excessiva, risco de arritmia e depressão respiratória",
     "Monitorar ECG (QTc) antes e durante tratamento. Considerar alternativa antifúngica ou reduzir metadona",
     "PCDT-HIV-FUNG"),

    ("Fluconazol", "Estatinas (sinvastatina, lovastatina)", "Hipolipemiante",
     "Inibição CYP3A4 eleva nível de estatinas",
     "moderada",
     "Rabdomiólise, miopatia por superdosagem de estatina",
     "Suspender sinvastatina/lovastatina durante tratamento com fluconazol. "
     "Rosuvastatina ou pravastatina são alternativas mais seguras",
     "ANVISA-ANTIF"),

    ("Fluconazol", "Midazolam / Triazolam", "Benzodiazepínico",
     "Inibição CYP3A4 eleva nível de benzodiazepínicos",
     "moderada",
     "Sedação prolongada, depressão respiratória",
     "Reduzir dose de benzodiazepínico em 50–75%. Midazolam IV para procedimentos: monitorar apneia",
     "ANVISA-ANTIF"),

    ("Fluconazol", "Haloperidol / Quetiapina", "Antipsicótico",
     "Inibição CYP3A4 eleva nível de antipsicótico; prolongamento QT aditivo",
     "moderada",
     "Prolongamento QT, sedação excessiva",
     "Monitorar ECG. Reduzir dose de antipsicótico se QTc > 470 ms (mulheres) ou 450 ms (homens)",
     "ANVISA-ANTIF"),

    ("Fluconazol", "Hidrocortisona / Prednisolona", "Corticosteroide",
     "Inibição CYP3A4 pode elevar nível de corticosteroide",
     "leve",
     "Potencialização de efeitos corticosteroides (hiperglicemia, imunossupressão)",
     "Monitorar glicemia. Geralmente não requer ajuste, mas atentar em diabéticos",
     "ANVISA-ANTIF"),

    # ══════════════════════════════════════════════════════════════════
    # ITRACONAZOL
    # ══════════════════════════════════════════════════════════════════
    ("Itraconazol", "Rifampicina", "Rifamicina (antimicobacteriano)",
     "Rifampicina induz CYP3A4 e P-gp — reduz drasticamente nível de itraconazol",
     "contraindicada",
     "Redução de até 90% da exposição ao itraconazol — falha terapêutica garantida",
     "CONTRAINDICADO — associação inviável. Em TB + paracoccidioidomicose: usar anfotericina B para a fase aguda, "
     "depois SMX-TMP ou voriconazol como alternativa. Discutir caso a caso com especialista",
     "PCDT-PARACOC"),

    ("Itraconazol", "Rifabutina", "Rifamicina (antimicobacteriano)",
     "Rifabutina induz CYP3A4 — reduz nível de itraconazol; itraconazol eleva nível de rifabutina",
     "contraindicada",
     "Falha terapêutica do itraconazol; uveíte e leucopenia por excesso de rifabutina",
     "CONTRAINDICADO — não coadministrar",
     "PCDT-HIV-FUNG"),

    ("Itraconazol", "Ergotamina", "Alcalóide do ergot",
     "Inibição CYP3A4 eleva nível de ergotamina",
     "contraindicada",
     "Ergotismo: vasoespasmo, isquemia de extremidades",
     "CONTRAINDICADO",
     "ANVISA-ANTIF"),

    ("Itraconazol", "Varfarina", "Anticoagulante (cumarínico)",
     "Inibição CYP2C9 e CYP3A4 eleva nível de varfarina",
     "grave",
     "Prolongamento de INR, sangramento grave",
     "Monitorar INR 2–3×/semana nas primeiras 2 semanas. Reduzir varfarina em 25–40%",
     "ANVISA-ANTIF"),

    ("Itraconazol", "Digoxina", "Glicosídeo cardíaco",
     "Inibição P-gp reduz excreção renal de digoxina",
     "grave",
     "Toxicidade digitálica: náusea, arritmias, bloqueio AV",
     "Monitorar nível sérico de digoxina. Considerar redução de dose em 30–50%",
     "ANVISA-ANTIF"),

    ("Itraconazol", "Tacrolimo", "Imunossupressor",
     "Inibição CYP3A4 eleva nível de tacrolimo",
     "grave",
     "Nefrotoxicidade, neurotoxicidade",
     "Reduzir dose de tacrolimo em 50–75%. Monitorar nível sérico frequentemente",
     "SBI-CAND"),

    ("Itraconazol", "Ciclosporina", "Imunossupressor",
     "Inibição CYP3A4 eleva nível de ciclosporina",
     "grave",
     "Nefrotoxicidade, hepatotoxicidade",
     "Reduzir ciclosporina em 50%. Monitorar nível sérico",
     "SBI-CAND"),

    ("Itraconazol", "Sirolimo", "Imunossupressor (mTOR)",
     "Inibição CYP3A4 eleva nível de sirolimo",
     "grave",
     "Toxicidade: nefrotoxicidade, trombocitopenia, pneumonite",
     "Reduzir dose de sirolimo em 75–90%. Monitorar nível sérico rigorosamente",
     "SBI-CAND"),

    ("Itraconazol", "Estatinas (sinvastatina, lovastatina, atorvastatina)", "Hipolipemiante",
     "Inibição CYP3A4 eleva nível de estatina",
     "grave",
     "Miopatia, rabdomiólise",
     "Suspender sinvastatina/lovastatina. Atorvastatina: reduzir dose máxima para 20 mg/dia. "
     "Pravastatina ou rosuvastatina são mais seguras",
     "ANVISA-ANTIF"),

    ("Itraconazol", "Antiácidos (IBP, bloqueadores H2, antiácidos com Al/Mg)",
     "Antiácido / antisecretor gástrico",
     "Redução do pH gástrico diminui absorção de cápsulas de itraconazol (requer pH ácido)",
     "moderada",
     "Redução de 50–70% da absorção de itraconazol — falha terapêutica",
     "Administrar itraconazol com suco ácido (laranja, cola). Evitar antiácidos 2h antes e após. "
     "A solução oral é menos afetada pelo pH gástrico",
     "PCDT-PARACOC"),

    ("Itraconazol", "Metformina", "Antidiabético oral (biguanida)",
     "Inibição transportadores renais (OCT2) pode reduzir eliminação de metformina",
     "leve",
     "Leve aumento de nível de metformina, risco de acidose lática (teórico, raro)",
     "Monitorar função renal. Geralmente sem necessidade de ajuste em pacientes com função renal normal",
     "ANVISA-ANTIF"),

    ("Itraconazol", "Fenitoína", "Antiepiléptico",
     "Fenitoína induz CYP3A4 — reduz nível de itraconazol; itraconazol pode inibir metabolismo de fenitoína",
     "moderada",
     "Falha antifúngica e/ou toxicidade de fenitoína (efeitos bidirecionais)",
     "Monitorar nível sérico de itraconazol e fenitoína. Considerar alternativa antifúngica",
     "ANVISA-ANTIF"),

    # ══════════════════════════════════════════════════════════════════
    # VORICONAZOL
    # ══════════════════════════════════════════════════════════════════
    ("Voriconazol", "Rifampicina", "Rifamicina (antimicobacteriano)",
     "Rifampicina induz CYP2C19, CYP3A4 e CYP2C9 — reduz AUC de voriconazol em ~96%",
     "contraindicada",
     "Falha terapêutica completa do voriconazol",
     "CONTRAINDICADO — coadministração inviável. Alternativa em TB + aspergilose: "
     "anfotericina B lipossomal ou ajuste da rifampicina (suspender rifampicina, usar rifabutina com cautela)",
     "SBI-ASPERG"),

    ("Voriconazol", "Rifabutina", "Rifamicina (antimicobacteriano)",
     "Rifabutina induz CYP3A4 — reduz voriconazol; voriconazol eleva rifabutina",
     "contraindicada",
     "Redução de ~79% da AUC de voriconazol; risco de toxicidade de rifabutina (uveíte)",
     "CONTRAINDICADO",
     "SBI-ASPERG"),

    ("Voriconazol", "Ergotamina", "Alcalóide do ergot",
     "Inibição CYP3A4 eleva nível de ergotamina",
     "contraindicada",
     "Ergotismo grave",
     "CONTRAINDICADO",
     "ANVISA-ANTIF"),

    ("Voriconazol", "Sirolimo", "Imunossupressor (mTOR)",
     "Inibição CYP3A4 eleva nível de sirolimo em ~11×",
     "contraindicada",
     "Toxicidade grave de sirolimo (nefrotoxicidade, trombocitopenia)",
     "CONTRAINDICADO — usar caspofungina ou micafungina como alternativa antifúngica em transplantados com sirolimo",
     "SBI-ASPERG"),

    ("Voriconazol", "Varfarina", "Anticoagulante",
     "Inibição CYP2C9 eleva S-varfarina",
     "grave",
     "INR elevado, sangramento grave",
     "Monitorar INR a cada 2 dias na primeira semana. Reduzir dose de varfarina em 25–50%",
     "ANVISA-ANTIF"),

    ("Voriconazol", "Tacrolimo", "Imunossupressor",
     "Inibição CYP3A4 eleva tacrolimo em ~3×",
     "grave",
     "Nefrotoxicidade, neurotoxicidade",
     "Reduzir tacrolimo em 66% (dose 1/3 da usual). Monitorar nível sérico 2–3×/semana",
     "SBI-ASPERG"),

    ("Voriconazol", "Ciclosporina", "Imunossupressor",
     "Inibição CYP3A4 eleva ciclosporina em ~1,7×",
     "grave",
     "Nefrotoxicidade",
     "Reduzir ciclosporina em 50%. Monitorar nível sérico diariamente na fase inicial",
     "SBI-ASPERG"),

    ("Voriconazol", "Fenitoína", "Antiepiléptico",
     "Fenitoína induz CYP2C19 — reduz voriconazol; voriconazol inibe CYP2C9 — eleva fenitoína",
     "grave",
     "Falha do voriconazol e toxicidade de fenitoína (efeitos bidirecionais)",
     "Se associação inevitável: dobrar dose de voriconazol (6 mg/kg 12/12h manutenção IV ou 400 mg 12/12h VO). "
     "Monitorar nível sérico de ambos",
     "SBI-ASPERG"),

    ("Voriconazol", "Carbamazepina / Fenobarbital", "Antiepiléptico (indutor CYP)",
     "Indução de CYP2C19 e CYP3A4 — reduz drasticamente nível de voriconazol",
     "contraindicada",
     "Falha antifúngica",
     "CONTRAINDICADO — substituir antiepiléptico por levetiracetam ou ácido valpróico (menor interação). "
     "Discutir com neurologista",
     "SBI-ASPERG"),

    ("Voriconazol", "Efavirenz", "Antirretroviral (NNRTI)",
     "Efavirenz induz CYP3A4/CYP2C19 — reduz voriconazol; voriconazol inibe metabolismo de efavirenz",
     "contraindicada",
     "Redução de ~77% de voriconazol; aumento de efavirenz — toxicidade neuropsiquiátrica",
     "CONTRAINDICADO com dose padrão de efavirenz. Alternativa ARV: substituir efavirenz por RAL ou DTG. "
     "Ou usar anfotericina B ou caspofungina como antifúngico alternativo",
     "PCDT-HIV-FUNG"),

    ("Voriconazol", "Lopinavir/ritonavir (LPV/r)", "Antirretroviral (IP/r)",
     "Ritonavir induz CYP2C19 — reduz voriconazol; voriconazol pode inibir metabolismo de LPV/r",
     "contraindicada",
     "Falha antifúngica; toxicidade imprevisível de LPV/r",
     "CONTRAINDICADO — usar caspofungina ou micafungina em pacientes com LPV/r",
     "PCDT-HIV-FUNG"),

    ("Voriconazol", "Metadona", "Opioide",
     "Inibição CYP3A4 e CYP2C19 eleva metadona",
     "grave",
     "Prolongamento QT, sedação, depressão respiratória",
     "Monitorar ECG (QTc). Reduzir metadona se necessário. Alternativa: caspofungina",
     "ANVISA-ANTIF"),

    ("Voriconazol", "Estatinas (sinvastatina, lovastatina)", "Hipolipemiante",
     "Inibição CYP3A4 eleva estatinas",
     "moderada",
     "Miopatia, rabdomiólise",
     "Suspender sinvastatina/lovastatina durante voriconazol. Usar pravastatina ou rosuvastatina",
     "ANVISA-ANTIF"),

    ("Voriconazol", "Omeprazol / esomeprazol", "IBP (antisecretor)",
     "Voriconazol inibe metabolismo de omeprazol por CYP2C19; omeprazol pode elevar voriconazol",
     "leve",
     "Aumento de ~4× no nível de omeprazol — risco de efeitos adversos do IBP",
     "Reduzir dose de omeprazol pela metade durante voriconazol. Monitorar sintomas GI",
     "ANVISA-ANTIF"),

    # ══════════════════════════════════════════════════════════════════
    # ANFOTERICINA B DESOXICOLATO
    # ══════════════════════════════════════════════════════════════════
    ("Anfotericina B desoxicolato", "Aminoglicosídeos (gentamicina, amicacina)",
     "Antibiótico (aminoglicosídeo)",
     "Toxicidade renal aditiva — ambos causam lesão tubular proximal",
     "contraindicada",
     "Nefrotoxicidade grave, insuficiência renal aguda oligúrica",
     "CONTRAINDICADO associar se possível. Se necessário: máxima hidratação IV (500 mL SF 0,9% pré-anfotericina), "
     "monitorar creatinina e ureia diariamente. Considerar aminoglicosídeo dose única diária",
     "ANVISA-ANTIF"),

    ("Anfotericina B desoxicolato", "Ciclosporina", "Imunossupressor",
     "Toxicidade renal aditiva (tubulotoxicidade)",
     "contraindicada",
     "Nefrotoxicidade grave, insuficiência renal aguda",
     "Evitar associação. Se necessário: usar anfotericina B lipossomal (menor nefrotoxicidade). "
     "Monitorar creatinina diariamente e nível de ciclosporina",
     "SBI-CAND"),

    ("Anfotericina B desoxicolato", "Tacrolimo", "Imunossupressor",
     "Toxicidade renal aditiva",
     "grave",
     "Nefrotoxicidade grave — IRA em transplantados",
     "Usar anfotericina B lipossomal se disponível. Monitorar nível de tacrolimo e função renal diariamente",
     "SBI-CAND"),

    ("Anfotericina B desoxicolato", "Furosemida / Hidroclorotiazida", "Diurético",
     "Diuréticos aumentam depleção de potássio e magnésio causada pela anfotericina B",
     "grave",
     "Hipopotassemia e hipomagnesemia graves — arritmias cardíacas, paralisia muscular",
     "Monitorar K+ e Mg2+ 2×/dia. Reposição profilática: KCl 40–80 mEq/dia + MgSO4 conforme nível sérico. "
     "Preferir diuréticos poupadores de K+ (espironolactona) se indicado",
     "ANVISA-ANTIF"),

    ("Anfotericina B desoxicolato", "Flucitosina (5-FC)", "Antifúngico (antimetabólito)",
     "Anfotericina B aumenta captação de 5-FC pelo fungo (sinergismo) e pode reduzir excreção renal de 5-FC",
     "moderada",
     "Mielotoxicidade (leucopenia, trombocitopenia) por acúmulo de 5-FC — mas associação é desejável clinicamente",
     "Associação BENÉFICA para criptococose (sinergismo). Monitorar hemograma e nível sérico de 5-FC "
     "(meta: pico < 100 µg/mL; vale > 25 µg/mL). Ajustar dose de 5-FC por função renal",
     "SBI-CRIPTO"),

    ("Anfotericina B desoxicolato", "Corticosteroides sistêmicos", "Corticosteroide",
     "Corticosteroides intensificam depleção de K+ causada por anfotericina B",
     "moderada",
     "Hipopotassemia grave, risco de arritmias",
     "Monitorar K+ diariamente. Reposição profilática agressiva de KCl",
     "ANVISA-ANTIF"),

    ("Anfotericina B desoxicolato", "Digoxina", "Glicosídeo cardíaco",
     "Hipopotassemia induzida por anfotericina B potencializa toxicidade digitálica",
     "grave",
     "Arritmias por toxicidade digitálica (bradiarritmias, bloqueios, TV)",
     "Monitorar K+ e nível sérico de digoxina frequentemente. Manter K+ > 4,0 mEq/L durante uso de anfotericina B",
     "ANVISA-ANTIF"),

    ("Anfotericina B desoxicolato", "Vancomicina", "Antibiótico (glicopeptídeo)",
     "Toxicidade renal aditiva",
     "moderada",
     "Nefrotoxicidade aumentada, especialmente em dose alta e uso prolongado de ambos",
     "Monitorar creatinina diariamente. Monitorar nível de vancomicina (AUC/CIM guiada). "
     "Hidratação IV vigorosa",
     "ANVISA-ANTIF"),

    ("Anfotericina B desoxicolato", "Colistina / Polimixina B", "Antibiótico (polimixina)",
     "Toxicidade renal aditiva grave",
     "grave",
     "Nefrotoxicidade grave — IRA com frequência elevada na associação",
     "Evitar associação quando possível. Se necessário: hidratação agressiva, monitorar Cr diariamente",
     "ANVISA-ANTIF"),

    # ══════════════════════════════════════════════════════════════════
    # CASPOFUNGINA
    # ══════════════════════════════════════════════════════════════════
    ("Caspofungina", "Rifampicina", "Rifamicina (antimicobacteriano)",
     "Indução de CYP3A4 reduz AUC de caspofungina",
     "moderada",
     "Redução de ~30% da exposição à caspofungina — possível falha terapêutica",
     "Aumentar dose de manutenção para 70 mg/dia (em vez de 50 mg). Monitorar resposta clínica",
     "SBI-ASPERG"),

    ("Caspofungina", "Efavirenz / Nevirapina", "Antirretroviral (NNRTI)",
     "Indução de CYP3A4 reduz exposição à caspofungina",
     "moderada",
     "Possível redução da eficácia antifúngica",
     "Aumentar dose de manutenção para 70 mg/dia",
     "PCDT-HIV-FUNG"),

    ("Caspofungina", "Dexametasona / Carbamazepina / Fenitoína", "Indutor enzimático",
     "Indução de enzimas hepáticas reduz nível de caspofungina",
     "moderada",
     "Redução da eficácia antifúngica",
     "Usar 70 mg/dia de manutenção em pacientes com indutores enzimáticos potentes",
     "SBI-ASPERG"),

    ("Caspofungina", "Tacrolimo", "Imunossupressor",
     "Caspofungina pode reduzir AUC de tacrolimo em ~20%",
     "leve",
     "Possível redução de nível de tacrolimo — risco de rejeição em transplantados",
     "Monitorar nível sérico de tacrolimo frequentemente durante coadministração",
     "SBI-CAND"),

    ("Caspofungina", "Ciclosporina", "Imunossupressor",
     "Coadministração eleva AUC de caspofungina em ~35%; elevação de transaminases relatada",
     "moderada",
     "Hepatotoxicidade — elevação de TGO/TGP",
     "Evitar combinação rotineira. Se necessária: monitorar função hepática 2×/semana",
     "SBI-CAND"),

    # ══════════════════════════════════════════════════════════════════
    # MICAFUNGINA
    # ══════════════════════════════════════════════════════════════════
    ("Micafungina", "Sirolimo", "Imunossupressor (mTOR)",
     "Micafungina inibe metabolismo de sirolimo",
     "moderada",
     "Aumento de ~21% no nível de sirolimo",
     "Monitorar nível de sirolimo. Ajustar dose se necessário",
     "SBI-CAND"),

    ("Micafungina", "Nifedipina", "Bloqueador de canal de cálcio",
     "Micafungina inibe CYP3A4 — eleva nível de nifedipina",
     "leve",
     "Hipotensão, edema de tornozelo, rubor facial por excesso de nifedipina",
     "Monitorar pressão arterial. Considerar redução de nifedipina se hipotensão sintomática",
     "ANVISA-ANTIF"),

    ("Micafungina", "Ciclosporina", "Imunossupressor",
     "Micafungina eleva nível de ciclosporina modestamente",
     "leve",
     "Leve aumento de nefrotoxicidade potencial",
     "Monitorar nível sérico de ciclosporina 2×/semana durante coadministração",
     "SBI-CAND"),

    # ══════════════════════════════════════════════════════════════════
    # TERBINAFINA
    # ══════════════════════════════════════════════════════════════════
    ("Terbinafina", "Rifampicina", "Rifamicina (antimicobacteriano)",
     "Rifampicina induz CYP3A4 — reduz nível de terbinafina em ~100%",
     "grave",
     "Falha terapêutica antifúngica (onicomicose, tinea)",
     "Aumentar dose de terbinafina para 500 mg/dia ou considerar alternativa",
     "SBD-MICOSES"),

    ("Terbinafina", "Cimetidina", "Anti-histamínico H2 / antiulceroso",
     "Cimetidina inibe metabolismo de terbinafina",
     "moderada",
     "Aumento de nível de terbinafina — risco de hepatotoxicidade",
     "Monitorar função hepática. Preferir omeprazol em vez de cimetidina",
     "SBD-MICOSES"),

    ("Terbinafina", "Antidepressivos tricíclicos (amitriptilina, nortriptilina)",
     "Antidepressivo (ADT)",
     "Terbinafina inibe CYP2D6 — eleva nível de ADT",
     "moderada",
     "Toxicidade anticolinérgica, sedação, prolongamento QT por excesso de ADT",
     "Monitorar ECG e nível sérico de ADT. Reduzir dose de ADT se necessário",
     "SBD-MICOSES"),

    ("Terbinafina", "ISRS (fluoxetina, paroxetina)", "Antidepressivo (ISRS)",
     "Terbinafina e ISRS são inibidores de CYP2D6 — efeito aditivo",
     "moderada",
     "Aumento de nível de ISRS; síndrome serotoninérgica (teórica); prolongamento QT",
     "Monitorar sintomas serotoninérgicos e ECG. Preferir ISRS com menor dependência de CYP2D6 (sertralina, escitalopram)",
     "SBD-MICOSES"),

    ("Terbinafina", "Varfarina", "Anticoagulante",
     "Mecanismo incerto — pode alterar metabolismo de varfarina via CYP2C9",
     "moderada",
     "Alteração de INR (elevação ou redução dependendo do contexto)",
     "Monitorar INR a cada 5–7 dias durante tratamento. Ajustar varfarina conforme INR",
     "SBD-MICOSES"),

    ("Terbinafina", "Beta-bloqueadores (metoprolol, carvedilol)", "Anti-hipertensivo / antiarrítmico",
     "Inibição CYP2D6 eleva nível de beta-bloqueadores metabolizados por essa via",
     "leve",
     "Bradicardia, hipotensão",
     "Monitorar FC e PA. Geralmente tolerado; ajustar beta-bloqueador se FC < 50 bpm ou hipotensão",
     "SBD-MICOSES"),

    # ══════════════════════════════════════════════════════════════════
    # GRISEOFULVINA
    # ══════════════════════════════════════════════════════════════════
    ("Griseofulvina", "Varfarina", "Anticoagulante",
     "Griseofulvina induz CYP2C9 — reduz nível de varfarina",
     "grave",
     "Redução do efeito anticoagulante — risco de eventos tromboembólicos",
     "Monitorar INR frequentemente. Aumentar dose de varfarina se INR subterapêutico",
     "SBD-MICOSES"),

    ("Griseofulvina", "Contraceptivos orais combinados", "Contraceptivo hormonal",
     "Indução de CYP — griseofulvina reduz nível de etinilestradiol e progestina",
     "grave",
     "Falha contraceptiva — gravidez indesejada",
     "Usar método contraceptivo de barreira (preservativo) durante e por 1 mês após griseofulvina. "
     "Informar a paciente sobre interação",
     "SBD-MICOSES"),

    ("Griseofulvina", "Álcool etílico", "Depressor do SNC",
     "Efeito sinérgico na depressão do SNC; griseofulvina pode inibir metabolismo do álcool",
     "moderada",
     "Efeito dissulfiram-like: rubor, taquicardia, náusea, mal-estar com ingestão de álcool",
     "Orientar abstinência alcoólica durante tratamento com griseofulvina",
     "SBD-MICOSES"),

    ("Griseofulvina", "Fenobarbital / Fenitoína", "Antiepiléptico",
     "Fenobarbital induz metabolismo da griseofulvina",
     "moderada",
     "Redução do nível de griseofulvina — falha antifúngica",
     "Considerar alternativa antifúngica (terbinafina) em epilépticos em uso de fenobarbital",
     "SBD-MICOSES"),

    # ══════════════════════════════════════════════════════════════════
    # SULFAMETOXAZOL + TRIMETOPRIMA (uso antifúngico — PCP e paracoccidioidomicose)
    # ══════════════════════════════════════════════════════════════════
    ("Sulfametoxazol + Trimetoprima", "Varfarina", "Anticoagulante",
     "SMX inibe CYP2C9 — eleva S-varfarina; TMP inibe CYP2C9 adicionalmente",
     "grave",
     "Aumento significativo de INR — sangramento grave",
     "Monitorar INR a cada 2–3 dias na primeira semana. Reduzir dose de varfarina em 25–50%",
     "PCDT-HIV-FUNG"),

    ("Sulfametoxazol + Trimetoprima", "Metotrexato", "Imunossupressor / quimioterápico",
     "TMP inibe DHFR como o metotrexato — efeito aditivo antifolato",
     "grave",
     "Mielotoxicidade grave (pancitopenia), mucosite, hepatotoxicidade",
     "EVITAR associação. Se necessário: reduzir dose de metotrexato. Suplementar leucovorin (ácido folínico)",
     "PCDT-HIV-FUNG"),

    ("Sulfametoxazol + Trimetoprima", "Azatioprina / 6-Mercaptopurina",
     "Imunossupressor (antimetabólito)",
     "Inibição de metabolismo por TMP — risco de toxicidade",
     "moderada",
     "Leucopenia grave",
     "Monitorar hemograma semanalmente. Reduzir dose de azatioprina",
     "PCDT-HIV-FUNG"),

    ("Sulfametoxazol + Trimetoprima", "Fenitoína", "Antiepiléptico",
     "SMX inibe CYP2C9 — eleva nível de fenitoína",
     "moderada",
     "Toxicidade de fenitoína (nistagmo, ataxia, confusão)",
     "Monitorar nível sérico de fenitoína. Reduzir dose se necessário",
     "PCDT-HIV-FUNG"),

    ("Sulfametoxazol + Trimetoprima", "Espironolactona / IECA / BRA",
     "Poupador de potássio / anti-hipertensivo",
     "TMP bloqueia canais de sódio no túbulo distal — retém K+ (efeito similar à amilorida); "
     "IECA/BRA/espironolactona também elevam K+",
     "grave",
     "Hiperpotassemia grave — risco de arritmia, parada cardíaca",
     "Monitorar K+ dentro de 5–7 dias após início do SMX-TMP. "
     "Evitar associação com IECA/BRA/espironolactona em alta dose. "
     "Interromper poupador de K+ se K+ > 5,5 mEq/L",
     "PCDT-HIV-FUNG"),

    ("Sulfametoxazol + Trimetoprima", "Dapsona", "Antilepromatoso / antiprotozoário",
     "Risco de metemoglobinemia aditiva",
     "grave",
     "Metemoglobinemia — cianose, dispneia, anemia hemolítica",
     "Evitar associação. Dapsona não é alternativa adequada para PCP em associação com SMX-TMP. "
     "Usar pentamidina como alternativa ao SMX-TMP se necessário",
     "PCDT-HIV-FUNG"),

    ("Sulfametoxazol + Trimetoprima", "Zidovudina (AZT)", "Antirretroviral (NRTI)",
     "Inibição de metabolismo — SMX-TMP pode elevar nível de AZT; ambos são mielotóxicos",
     "moderada",
     "Mielotoxicidade aditiva (neutropenia, anemia)",
     "Monitorar hemograma 2×/semana durante associação. "
     "Considerar suplementação de ácido folínico. Preferir TDF sobre AZT quando possível",
     "PCDT-HIV-FUNG"),

    # ══════════════════════════════════════════════════════════════════
    # PENTAMIDINA
    # ══════════════════════════════════════════════════════════════════
    ("Pentamidina (isetionato)", "Aminoglicosídeos", "Antibiótico",
     "Toxicidade renal aditiva",
     "grave",
     "Nefrotoxicidade grave, IRA",
     "Evitar associação. Se necessária: máxima hidratação IV e monitoramento diário de função renal",
     "PCDT-HIV-FUNG"),

    ("Pentamidina (isetionato)", "Anfotericina B desoxicolato", "Antifúngico (polieno)",
     "Nefrotoxicidade aditiva grave",
     "contraindicada",
     "IRA grave — toxicidade sinérgica tubular renal",
     "CONTRAINDICADO — usar SMX-TMP como 1ª linha para PCP. Se ambas necessárias: usar anfotericina B lipossomal",
     "PCDT-HIV-FUNG"),

    ("Pentamidina (isetionato)", "Antiarrítmicos (amiodarona, quinidina, sotalol)",
     "Antiarrítmico",
     "Prolongamento QT aditivo",
     "contraindicada",
     "Torsades de pointes, fibrilação ventricular, morte súbita",
     "CONTRAINDICADO — monitorar ECG antes de iniciar pentamidina. "
     "Se QTc > 450 ms (homens) ou 470 ms (mulheres): contraindicado",
     "PCDT-HIV-FUNG"),

    ("Pentamidina (isetionato)", "Sulfonilureias / Insulina", "Antidiabético",
     "Pentamidina causa disfunção de células beta — primeiro hipoglicemia, depois hiperglicemia",
     "grave",
     "Hipoglicemia grave (fase aguda); diabetes mellitus permanente (uso prolongado)",
     "Monitorar glicemia a cada 6h durante infusão. Ter glicose 50% disponível à beira do leito",
     "PCDT-HIV-FUNG"),

    # ══════════════════════════════════════════════════════════════════
    # FLUCITOSINA (5-FC)
    # ══════════════════════════════════════════════════════════════════
    ("Flucitosina (5-FC)", "Citarabina (ARA-C)", "Antineoplásico (antimetabólito)",
     "Citarabina inibe citidina desaminase — reduz metabolismo de 5-FC",
     "contraindicada",
     "Acúmulo de 5-FC e metabólitos tóxicos — mielotoxicidade grave",
     "CONTRAINDICADO — não usar 5-FC em pacientes em quimioterapia com citarabina",
     "SBI-CRIPTO"),

    ("Flucitosina (5-FC)", "Anfotericina B desoxicolato", "Antifúngico (polieno)",
     "Anfotericina B reduz ClCr — diminui excreção renal de 5-FC (acúmulo)",
     "moderada",
     "Toxicidade de 5-FC: leucopenia, trombocitopenia — mas combinação é SINÉRGICA e clinicamente desejável",
     "Associação BENÉFICA para criptococose. Ajustar 5-FC por função renal (ClCr). "
     "Monitorar hemograma 2×/semana e nível sérico de 5-FC",
     "SBI-CRIPTO"),

    ("Flucitosina (5-FC)", "Zidovudina (AZT)", "Antirretroviral (NRTI)",
     "Mielotoxicidade aditiva",
     "moderada",
     "Leucopenia, anemia, trombocitopenia",
     "Monitorar hemograma 2×/semana. Considerar substituição de AZT por TDF",
     "PCDT-HIV-FUNG"),

    # ══════════════════════════════════════════════════════════════════
    # POSACONAZOL
    # ══════════════════════════════════════════════════════════════════
    ("Posaconazol", "Sirolimo", "Imunossupressor (mTOR)",
     "Inibição CYP3A4 e P-gp eleva sirolimo",
     "contraindicada",
     "Toxicidade grave de sirolimo",
     "CONTRAINDICADO — usar micafungina ou caspofungina em pacientes com sirolimo",
     "SBI-ASPERG"),

    ("Posaconazol", "Rifampicina", "Rifamicina",
     "Rifampicina induz CYP3A4 e UGT — reduz posaconazol",
     "contraindicada",
     "Falha terapêutica",
     "CONTRAINDICADO — alternativa: anfotericina B lipossomal",
     "SBI-ASPERG"),

    ("Posaconazol", "Ergotamina", "Alcalóide do ergot",
     "Inibição CYP3A4",
     "contraindicada",
     "Ergotismo",
     "CONTRAINDICADO",
     "ANVISA-ANTIF"),

    ("Posaconazol", "Varfarina", "Anticoagulante",
     "Inibição CYP2C9 eleva varfarina",
     "grave",
     "Sangramento, INR elevado",
     "Monitorar INR frequentemente. Reduzir dose de varfarina",
     "ANVISA-ANTIF"),

    ("Posaconazol", "Ciclosporina", "Imunossupressor",
     "Inibição CYP3A4 eleva ciclosporina",
     "grave",
     "Nefrotoxicidade",
     "Reduzir ciclosporina em 25–50%. Monitorar nível sérico",
     "SBI-ASPERG"),

    ("Posaconazol", "Tacrolimo", "Imunossupressor",
     "Inibição CYP3A4 eleva tacrolimo",
     "grave",
     "Nefrotoxicidade, neurotoxicidade",
     "Reduzir tacrolimo em 50–66%. Monitorar nível sérico 2–3×/semana",
     "SBI-ASPERG"),

    ("Posaconazol", "Antiácidos / IBP / bloqueadores H2",
     "Antisecretor gástrico",
     "Redução do pH gástrico reduz absorção da suspensão oral de posaconazol",
     "moderada",
     "Redução da biodisponibilidade — possível falha antifúngica",
     "Usar comprimido gastrorresistente (menos afetado pelo pH). "
     "Administrar suspensão com alimento gorduroso e 2–4 horas após antiácido",
     "SBI-ASPERG"),

    # ══════════════════════════════════════════════════════════════════
    # NISTATINA (TÓPICA/ORAL — sem absorção sistêmica)
    # ══════════════════════════════════════════════════════════════════
    ("Nistatina", "Qualquer medicamento sistêmico", "Qualquer classe",
     "Nistatina não tem absorção sistêmica relevante — sem interações farmacocinéticas",
     "leve",
     "Sem interações sistêmicas conhecidas",
     "Sem restrições de interação medicamentosa sistêmica. "
     "Uso seguro em polifarmácia, transplantados e pacientes em HIV-TARV",
     "SBI-CAND"),

    # ══════════════════════════════════════════════════════════════════
    # IODETO DE POTÁSSIO (KI)
    # ══════════════════════════════════════════════════════════════════
    ("Iodeto de Potássio (KI)", "Carbonato de lítio", "Estabilizador de humor",
     "KI e lítio têm efeitos aditivos sobre a tireoide — hipotireoidismo",
     "grave",
     "Hipotireoidismo grave, bócio, hipocalcemia",
     "Monitorar TSH, T4 livre e função tireoidiana mensalmente. "
     "Considerar alternativa antifúngica (itraconazol) em pacientes em lítio",
     "SVS-ESPORO"),

    ("Iodeto de Potássio (KI)", "Diuréticos poupadores de potássio / IECA / BRA",
     "Anti-hipertensivo / cardiológico",
     "Hiperpotassemia aditiva — KI fornece K+; poupadores de K+ reduzem excreção renal de K+",
     "grave",
     "Hiperpotassemia grave — arritmias cardíacas",
     "Monitorar K+ seriadamente. Evitar associação em pacientes com risco de hiperpotassemia",
     "SVS-ESPORO"),

    ("Iodeto de Potássio (KI)", "Anticoagulantes (varfarina)", "Anticoagulante",
     "Interação teórica via alterações de proteínas de ligação",
     "leve",
     "Possível alteração de INR",
     "Monitorar INR durante tratamento com KI em pacientes anticoagulados",
     "SVS-ESPORO"),

]

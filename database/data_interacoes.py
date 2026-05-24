"""
Interações medicamentosas clinicamente relevantes para antibióticos.
Fontes: Micromedex Brasil, Bulário ANVISA, UpToDate adaptado ao formulário BR,
        PCDT MS, SBCM (Soc. Bras. Clínica Médica).

Formato:
(antibiotico_nome, medicamento_interagente, classe_interagente,
 mecanismo, gravidade, efeito_clinico, conduta, fonte_sigla)

Gravidade: 'contraindicada' | 'grave' | 'moderada' | 'leve'
"""

INTERACOES = [
    # ══════════════════════════════════════════════════════════════════
    # RIFAMPICINA — indutor enzimático potente CYP3A4/2C9/P-gp
    # ══════════════════════════════════════════════════════════════════
    ("Rifampicina", "Anticoagulantes orais (varfarina, rivaroxabana)",
     "Anticoagulantes", "Indução CYP2C9 e CYP3A4 — acelera metabolismo do anticoagulante",
     "grave", "Redução drástica do efeito anticoagulante; risco de tromboembolismo",
     "Aumentar dose do anticoagulante com monitoramento frequente de INR/anti-Xa. Reavaliar ao término da rifampicina.", "GVS-MS"),

    ("Rifampicina", "Anticoncepcionais hormonais orais",
     "Hormônios", "Indução CYP3A4 — reduz níveis de estrogênios e progestinas",
     "grave", "Falha contraceptiva com risco de gravidez não planejada",
     "Usar método contraceptivo de barreira durante e por 1 mês após término da rifampicina.", "PCDT-TB"),

    ("Rifampicina", "Antirretrovirais (inibidores de protease, INSTIs)",
     "Antirretrovirais", "Forte indução CYP3A4/P-gp — reduz exposição dos ARVs em 70-90%",
     "contraindicada", "Falha virológica e resistência aos antirretrovirais",
     "CONTRAINDICADA com IPs e maioria dos INSTIs. Substituir por rifabutina sempre que possível em PVHIV.", "PCDT-TB"),

    ("Rifampicina", "Corticosteroides (prednisona, dexametasona)",
     "Corticosteroides", "Indução CYP3A4 — reduz exposição do corticoide",
     "moderada", "Redução do efeito anti-inflamatório; risco de falha em transplantados e doenças autoimunes",
     "Dobrar dose do corticoide durante uso. Reavaliar ao suspender rifampicina.", "GVS-MS"),

    ("Rifampicina", "Ciclosporina / Tacrolimo",
     "Imunossupressores", "Potente indução CYP3A4 e P-gp — reduz nível sérico até 90%",
     "contraindicada", "Rejeição de órgão transplantado por nível subterapêutico do imunossupressor",
     "EVITAR combinação. Se indispensável, monitorar nível sérico 2x/dia e aumentar dose drasticamente.", "ANVISA-IRAS"),

    ("Rifampicina", "Metadona",
     "Opioide", "Indução CYP3A4 e CYP2C8 — reduz nível de metadona 30-60%",
     "grave", "Síndrome de abstinência com risco de recaída em pacientes em tratamento de dependência",
     "Aumentar dose de metadona com monitoramento cuidadoso. Informar equipe de saúde mental.", "PCDT-TB"),

    ("Rifampicina", "Fluconazol / Voriconazol",
     "Antifúngicos azólicos", "Indução CYP2C19/3A4 — reduz concentração do antifúngico",
     "grave", "Falha no tratamento de infecções fúngicas invasivas",
     "Evitar combinação. Se necessário, aumentar dose do azólico e monitorar. Voriconazol: considerar substituição.", "GVS-MS"),

    # ══════════════════════════════════════════════════════════════════
    # METRONIDAZOL
    # ══════════════════════════════════════════════════════════════════
    ("Metronidazol", "Álcool etílico",
     "Álcool", "Inibição da aldeído desidrogenase — acúmulo de acetaldeído",
     "grave", "Reação tipo dissulfiram: rubor facial, náuseas, vômitos, taquicardia, hipotensão",
     "Proibir consumo de álcool durante e por 48h após término do metronidazol. Orientar paciente.", "GVS-MS"),

    ("Metronidazol", "Varfarina",
     "Anticoagulante", "Inibição CYP2C9 — reduz metabolismo da varfarina",
     "grave", "Aumento do INR com risco de sangramento grave",
     "Reduzir dose de varfarina em 25-50%. Monitorar INR 2-3x/semana durante e após o antibiótico.", "GVS-MS"),

    ("Metronidazol", "Lítio",
     "Estabilizador de humor", "Reduz excreção renal de lítio",
     "moderada", "Toxicidade por lítio: tremores, confusão, arritmias",
     "Monitorar litemia e sinais de toxicidade. Considerar redução de dose de lítio.", "GVS-MS"),

    ("Metronidazol", "Dissulfiram",
     "Dependência química", "Efeito aditivo sobre aldeído desidrogenase",
     "contraindicada", "Reações psicóticas e estados confusionais graves",
     "CONTRAINDICADA. Não usar metronidazol em pacientes que usaram dissulfiram nas últimas 2 semanas.", "GVS-MS"),

    # ══════════════════════════════════════════════════════════════════
    # FLUOROQUINOLONAS (ciprofloxacino, levofloxacino, moxifloxacino)
    # ══════════════════════════════════════════════════════════════════
    ("Ciprofloxacino", "Antiácidos com alumínio/magnésio, suplementos de ferro/zinco",
     "Antiácidos / Minerais", "Quelação no trato gastrointestinal — reduz absorção da quinolona em até 90%",
     "grave", "Falha terapêutica por concentrações subterapêuticas",
     "Administrar ciprofloxacino 2h ANTES ou 4-6h APÓS antiácidos/ferro/zinco/cálcio.", "GVS-MS"),

    ("Ciprofloxacino", "Teofilina",
     "Broncodilatador xantínico", "Inibição CYP1A2 — reduz clearance da teofilina",
     "grave", "Toxicidade por teofilina: convulsões, arritmias, taquicardia",
     "Reduzir dose de teofilina em 50%. Monitorar nível sérico e sinais de toxicidade.", "GVS-MS"),

    ("Ciprofloxacino", "Varfarina",
     "Anticoagulante", "Inibição CYP1A2 — reduz metabolismo da varfarina",
     "moderada", "Elevação do INR com risco aumentado de sangramento",
     "Monitorar INR 2-3x/semana durante o curso. Reduzir dose de varfarina se necessário.", "GVS-MS"),

    ("Ciprofloxacino", "Medicamentos que prolongam QT (amiodarona, sotalol, haloperidol, antidepressivos tricíclicos)",
     "Agentes pró-arrítmicos", "Bloqueio de canais de potássio (hERG) — prolongamento do QTc aditivo",
     "grave", "Risco de arritmia grave tipo torsades de pointes e parada cardíaca",
     "Evitar combinação. Se indispensável, monitorar ECG e eletrólitos. Corrigir hipocalemia/hipomagnesemia.", "ANVISA-SCIH"),

    ("Levofloxacino", "Antidiabéticos orais (sulfoniluréias, insulina)",
     "Hipoglicemiantes", "Mecanismo misto: alteração de secreção insulínica",
     "moderada", "Hipo ou hiperglicemia imprevisível, especialmente em idosos",
     "Monitorar glicemia com mais frequência durante o tratamento. Ajustar dose do hipoglicemiante se necessário.", "GVS-MS"),

    ("Levofloxacino", "Medicamentos que prolongam QT",
     "Agentes pró-arrítmicos", "Bloqueio de canais hERG — aditivo ao prolongamento do QT",
     "grave", "Torsades de pointes e morte súbita",
     "Evitar combinação. ECG antes de iniciar em pacientes de risco (idosos, cardiopatas, QTc basal elevado).", "ANVISA-SCIH"),

    ("Moxifloxacino", "Medicamentos que prolongam QT",
     "Agentes pró-arrítmicos", "Bloqueio mais potente de canais hERG que outras quinolonas",
     "grave", "Maior risco de torsades de pointes entre as fluoroquinolonas",
     "EVITAR associação. Considerar outra quinolona ou antibiótico de classe diferente.", "ANVISA-SCIH"),

    # ══════════════════════════════════════════════════════════════════
    # CLARITROMICINA / ERITROMICINA
    # ══════════════════════════════════════════════════════════════════
    ("Claritromicina", "Estatinas (sinvastatina, atorvastatina, lovastatina)",
     "Hipolipemiantes", "Inibição CYP3A4 — aumenta nível sérico da estatina",
     "grave", "Rabdomiólise e insuficiência renal aguda",
     "SUSPENDER sinvastatina/lovastatina durante o curso. Atorvastatina: usar menor dose. Preferir estatinas não metabolizadas por CYP3A4 (pravastatina, rosuvastatina).", "GVS-MS"),

    ("Claritromicina", "Varfarina",
     "Anticoagulante", "Inibição CYP3A4 e CYP2C9 — aumenta efeito anticoagulante",
     "moderada", "Elevação significativa do INR; risco de sangramento",
     "Monitorar INR 2-3x/semana. Reduzir dose de varfarina conforme resposta.", "GVS-MS"),

    ("Claritromicina", "Colchicina",
     "Antigotoso / anti-inflamatório", "Inibição CYP3A4 e P-gp — aumenta exposição à colchicina",
     "grave", "Toxicidade grave por colchicina: miopatia, agranulocitose, falência de múltiplos órgãos",
     "CONTRAINDICADA em insuficiência renal ou hepática. Em pacientes normais: reduzir dose de colchicina e monitorar.", "GVS-MS"),

    ("Claritromicina", "Medicamentos que prolongam QT",
     "Agentes pró-arrítmicos", "Inibição CYP3A4 + bloqueio hERG direto",
     "grave", "Torsades de pointes, especialmente com cisaprida, terfenadina, astemizol",
     "CONTRAINDICADA com cisaprida, pimozida. Cautela com outros agentes pró-arrítmicos.", "GVS-MS"),

    ("Eritromicina", "Medicamentos que prolongam QT",
     "Agentes pró-arrítmicos", "Bloqueio de canais hERG e inibição de CYP3A4",
     "grave", "Risco elevado de torsades de pointes — maior que com claritromicina",
     "Evitar IV em pacientes com QTc prolongado. Monitorar ECG se uso obrigatório.", "GVS-MS"),

    # ══════════════════════════════════════════════════════════════════
    # VANCOMICINA
    # ══════════════════════════════════════════════════════════════════
    ("Vancomicina", "Aminoglicosídeos (gentamicina, amicacina)",
     "Aminoglicosídeos", "Nefrotoxicidade aditiva por dano tubular renal sinérgico",
     "grave", "Insuficiência renal aguda — risco 5-10x maior que com cada droga isolada",
     "Monitorar creatinina e ureia diariamente. Considerar alternativa terapêutica. Se indispensável, manter hidratação.", "ANVISA-IRAS"),

    ("Vancomicina", "Diuréticos de alça (furosemida)",
     "Diuréticos", "Nefrotoxicidade e ototoxicidade aditivas",
     "moderada", "Insuficiência renal aguda e ototoxicidade (perda auditiva)",
     "Monitorar função renal e nível sérico de vancomicina. Ajuste de dose em insuficiência renal.", "ANVISA-IRAS"),

    ("Vancomicina", "Piperacilina-tazobactam",
     "Betalactâmico + inibidor", "Possível nefrotoxicidade aditiva (mecanismo debatido)",
     "moderada", "Estudos sugerem maior incidência de nefrotoxicidade vs vancomicina + cefalosporina",
     "Monitorar creatinina diariamente. Considerar substituir pip-tazo por meropenem se risco renal elevado.", "ANVISA-IRAS"),

    # ══════════════════════════════════════════════════════════════════
    # LINEZOLIDA
    # ══════════════════════════════════════════════════════════════════
    ("Linezolida", "Inibidores seletivos de recaptação de serotonina (ISRS: sertralina, fluoxetina, escitalopram)",
     "Antidepressivos ISRS", "Inibição da MAO-A — acúmulo de serotonina (síndrome serotoninérgica)",
     "contraindicada", "Síndrome serotoninérgica: tremores, mioclonias, hipertermia, taquicardia, confusão, óbito",
     "CONTRAINDICADA. Suspender ISRS 2 semanas antes de iniciar linezolida (5 semanas para fluoxetina).", "ANVISA-SCIH"),

    ("Linezolida", "Inibidores da MAO (fenelzina, tranilcipromina)",
     "IMAOs", "Inibição dupla da MAO — hiperestimulação serotoninérgica e adrenérgica",
     "contraindicada", "Crise hipertensiva, síndrome serotoninérgica grave, óbito",
     "CONTRAINDICADA. Aguardar 14 dias após suspender IMAO antes de iniciar linezolida.", "ANVISA-SCIH"),

    ("Linezolida", "Tramadol",
     "Opioide / serotoninérgico", "Potencialização serotoninérgica e adrenérgica",
     "grave", "Síndrome serotoninérgica: agitação, hipertermia, convulsões",
     "Evitar combinação. Se dor intensa, usar opioide sem atividade serotoninérgica (morfina, fentanil).", "ANVISA-SCIH"),

    ("Linezolida", "Alimentos ricos em tiramina (queijos curados, vinho tinto, embutidos, cerveja)",
     "Alimentos com tiramina", "Inibição da MAO intestinal — absorção sistêmica da tiramina",
     "moderada", "Crise hipertensiva (reação do queijo): cefaleia, sudorese, taquicardia, AVC",
     "Orientar paciente a evitar alimentos ricos em tiramina durante todo o curso de linezolida.", "ANVISA-SCIH"),

    # ══════════════════════════════════════════════════════════════════
    # DAPTOMICINA
    # ══════════════════════════════════════════════════════════════════
    ("Daptomicina", "Estatinas (todos os tipos)",
     "Hipolipemiantes", "Toxicidade muscular aditiva (ambas causam miopatia)",
     "moderada", "Miopatia e rabdomiólise com elevação de CK",
     "Suspender estatina durante o curso de daptomicina. Monitorar CK semanal.", "ANVISA-SCIH"),

    ("Daptomicina", "Warfarina",
     "Anticoagulante", "Potencial alteração da coagulação não totalmente elucidada",
     "moderada", "Variação imprevisível do INR",
     "Monitorar INR na primeira semana de uso combinado.", "ANVISA-SCIH"),

    # ══════════════════════════════════════════════════════════════════
    # SULFAMETOXAZOL-TRIMETOPRIMA (SMX-TMP)
    # ══════════════════════════════════════════════════════════════════
    ("Sulfametoxazol-trimetoprima (SMX-TMP)", "Varfarina",
     "Anticoagulante", "Inibição CYP2C9 pelo sulfametoxazol",
     "grave", "Aumento pronunciado do INR; risco de hemorragia grave",
     "Monitorar INR em 2-3 dias após início. Reduzir dose de varfarina em ~25%. Vigilância rigorosa.", "GVS-MS"),

    ("Sulfametoxazol-trimetoprima (SMX-TMP)", "Metotrexato",
     "Antineoplásico / imunossupressor", "Inibição competitiva do DHFR e redução da excreção renal",
     "grave", "Toxicidade grave por metotrexato: pancitopenia, mucosite, nefrotoxicidade",
     "CONTRAINDICADA com metotrexato em altas doses. Em baixas doses (reumatológico): monitorar hemograma e função renal.", "GVS-MS"),

    ("Sulfametoxazol-trimetoprima (SMX-TMP)", "Inibidores de ECA e espironolactona",
     "Anti-hipertensivos", "Hipercalemia aditiva pela componente trimetoprima (bloqueia secreção tubular de potássio)",
     "moderada", "Hipercalemia potencialmente grave, especialmente em insuficiência renal e idosos",
     "Monitorar potássio sérico em 3-5 dias. Reduzir dose de diurético poupador de potássio se necessário.", "GVS-MS"),

    ("Sulfametoxazol-trimetoprima (SMX-TMP)", "Antidiabéticos orais (sulfonilureias)",
     "Hipoglicemiantes", "Inibição CYP2C9 + efeito hipoglicemiante direto da trimetoprima",
     "moderada", "Hipoglicemia, especialmente em idosos e insuficiência renal",
     "Monitorar glicemia. Reduzir dose do hipoglicemiante se necessário.", "GVS-MS"),

    # ══════════════════════════════════════════════════════════════════
    # AMINOGLICOSÍDEOS
    # ══════════════════════════════════════════════════════════════════
    ("Gentamicina", "Diuréticos de alça (furosemida, ácido etacrínico)",
     "Diuréticos", "Ototoxicidade e nefrotoxicidade aditivas",
     "grave", "Perda auditiva irreversível (coclear) e insuficiência renal",
     "Evitar uso simultâneo. Se indispensável, monitorar audiometria e creatinina. Manter hidratação.", "GVS-MS"),

    ("Gentamicina", "Cisplatina e outros quimioterápicos nefrotóxicos",
     "Quimioterápicos", "Nefrotoxicidade aditiva por lesão tubular sinérgica",
     "grave", "Insuficiência renal aguda e potencialização da ototoxicidade",
     "Evitar co-administração. Se necessário, intervalo de pelo menos 48h e monitoramento intensivo.", "GVS-MS"),

    ("Amicacina", "Bloqueadores neuromusculares (pancurônio, vecurônio)",
     "Agentes anestésicos", "Potencialização do bloqueio neuromuscular",
     "moderada", "Apneia prolongada ou bloqueio neuromuscular residual em pós-operatório",
     "Cautela no perioperatório. Monitorar função muscular e respiratória.", "GVS-MS"),

    # ══════════════════════════════════════════════════════════════════
    # DOXICICLINA
    # ══════════════════════════════════════════════════════════════════
    ("Doxiciclina", "Antiácidos com Al/Mg/Ca, leite, ferro",
     "Antiácidos / Minerais / Laticínios", "Quelação no trato gastrointestinal — reduz absorção oral",
     "moderada", "Níveis séricos subterapêuticos com risco de falha terapêutica",
     "Administrar doxiciclina 1-2h antes ou 2-3h após antiácidos, leite, ferro ou cálcio.", "GVS-MS"),

    ("Doxiciclina", "Anticonvulsivantes (fenitoína, carbamazepina, fenobarbital)",
     "Antiepilépticos", "Indução CYP3A4 — reduz meia-vida da doxiciclina em até 50%",
     "moderada", "Níveis subterapêuticos; risco de falha em infecções graves",
     "Considerar dobrar dose de doxiciclina ou substituir por outro antibiótico.", "GVS-MS"),

    ("Doxiciclina", "Anticoagulantes orais (varfarina)",
     "Anticoagulante", "Possível inibição da flora intestinal produtora de vitamina K",
     "leve", "Leve elevação do INR",
     "Monitorar INR após 3-5 dias de tratamento.", "GVS-MS"),

    # ══════════════════════════════════════════════════════════════════
    # ISONIAZIDA
    # ══════════════════════════════════════════════════════════════════
    ("Isoniazida (INH)", "Fenitoína",
     "Antiepiléptico", "Inibição CYP2C9 — reduz metabolismo da fenitoína",
     "grave", "Toxicidade por fenitoína: nistagmo, ataxia, confusão mental",
     "Monitorar nível sérico de fenitoína. Reduzir dose se necessário. Interação mais intensa em acetiladores lentos.", "PCDT-TB"),

    ("Isoniazida (INH)", "Paracetamol (acetaminofeno)",
     "Analgésico/antipirético", "Indução CYP2E1 — maior produção de metabólito hepatotóxico do paracetamol",
     "moderada", "Hepatotoxicidade potencializada, especialmente com doses > 2g/dia de paracetamol",
     "Limitar paracetamol a ≤ 2g/dia em pacientes em uso de isoniazida. Preferir AINEs se possível.", "PCDT-TB"),

    ("Isoniazida (INH)", "Carbamazepina",
     "Antiepiléptico", "Inibição do metabolismo da carbamazepina",
     "moderada", "Toxicidade por carbamazepina: diplopia, ataxia, sonolência",
     "Monitorar nível sérico de carbamazepina e reduzir dose se necessário.", "PCDT-TB"),

    ("Isoniazida (INH)", "Álcool etílico",
     "Álcool", "Indução enzimática mútua — maior produção de metabólitos hepatotóxicos",
     "grave", "Hepatite grave potencialmente fatal",
     "Orientar abstinência total de álcool durante todo o tratamento da tuberculose.", "PCDT-TB"),

    # ══════════════════════════════════════════════════════════════════
    # POLIMIXINA B / COLISTINA
    # ══════════════════════════════════════════════════════════════════
    ("Polimixina B", "Aminoglicosídeos",
     "Aminoglicosídeos", "Nefrotoxicidade e neurotoxicidade aditivas",
     "grave", "Insuficiência renal aguda frequente; neurotoxicidade (parestesias, apneia)",
     "Monitorar creatinina 2x/dia. Evitar associação se possível. Hidratação adequada.", "ANVISA-IRAS"),

    ("Polimixina B", "Bloqueadores neuromusculares",
     "Agentes anestésicos", "Efeito bloqueador neuromuscular direto da polimixina",
     "moderada", "Apneia e bloqueio neuromuscular prolongado",
     "Cautela extrema no perioperatório. Monitorar função respiratória.", "ANVISA-IRAS"),

    ("Colistina (Polimixina E)", "Aminoglicosídeos",
     "Aminoglicosídeos", "Nefrotoxicidade aditiva severa",
     "grave", "Insuficiência renal aguda — incidência > 50% com combinação",
     "Monitorar função renal 2x/dia. Considerar polimixina B (menos nefrotóxica para uso sistêmico) se possível.", "ANVISA-IRAS"),

    # ══════════════════════════════════════════════════════════════════
    # AZITROMICINA
    # ══════════════════════════════════════════════════════════════════
    ("Azitromicina", "Medicamentos que prolongam QT (amiodarona, sotalol, antipsicóticos)",
     "Agentes pró-arrítmicos", "Bloqueio de canais hERG — prolongamento do QTc",
     "grave", "Torsades de pointes — risco documentado em populações de risco",
     "Evitar em pacientes com QTc > 500ms, hipocalemia, hipomagnesemia ou cardiopatia. Checar ECG se risco.", "GVS-MS"),

    ("Azitromicina", "Varfarina",
     "Anticoagulante", "Mecanismo incerto — possível inibição do metabolismo",
     "moderada", "Elevação do INR",
     "Monitorar INR após 3-5 dias de tratamento com azitromicina.", "GVS-MS"),

    # ══════════════════════════════════════════════════════════════════
    # PENICILINAS + CEFALOSPORINAS (gerais)
    # ══════════════════════════════════════════════════════════════════
    ("Ampicilina", "Metotrexato",
     "Antineoplásico / imunossupressor", "Redução da excreção renal de metotrexato por competição tubular",
     "grave", "Toxicidade grave por metotrexato: mucosite, pancitopenia, nefrotoxicidade",
     "Evitar combinação durante metotrexato em altas doses. Em baixas doses: monitorar cuidadosamente.", "GVS-MS"),

    ("Amoxicilina", "Anticoagulantes orais",
     "Anticoagulante", "Redução de flora intestinal produtora de vitamina K",
     "leve", "Leve elevação do INR",
     "Monitorar INR se uso de anticoagulante oral durante amoxicilina.", "GVS-MS"),

    ("Ceftriaxona", "Soluções com cálcio (Ringer lactato, nutrição parenteral com cálcio)",
     "Soluções parenterais", "Precipitação de ceftriaxona cálcica na solução e tecidos",
     "contraindicada", "Precipitados no pulmão e rins — mortes em neonatos documentadas",
     "CONTRAINDICADO misturar ceftriaxona com soluções contendo cálcio, especialmente em neonatos. Em adultos, intervalo mínimo de 48h.", "PCDT-MENIN"),

    # ══════════════════════════════════════════════════════════════════
    # DAPSONA (hanseníase)
    # ══════════════════════════════════════════════════════════════════
    ("Dapsona", "Rifampicina",
     "Rifamicina", "Indução CYP2C9/3A4 — reduz nível sérico de dapsona em 7-10x",
     "moderada", "Possível redução de eficácia da dapsona; clinicamente manejável no esquema PQT",
     "Já previsto no esquema PQT MS. Monitorar resposta clínica. Não requer ajuste de dose no esquema padrão.", "PCDT-HANSENR"),

    ("Dapsona", "Primaquina",
     "Antimalárico", "Estresse oxidativo aditivo em eritrócitos",
     "moderada", "Hemólise em pacientes com deficiência de G6PD",
     "Testar G6PD antes de co-administrar. Evitar combinação em deficientes graves.", "GVS-MS"),
]

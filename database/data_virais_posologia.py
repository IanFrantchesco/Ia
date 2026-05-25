"""
Dados de posologia de antivirais por população.
Fontes: PCDTs MS (HIV 2022, Hepatite B 2022, Hepatite C 2022, Influenza, COVID-19),
        SVS/MS GVS 5ª ed. 2022, SBI, ANVISA bulas registradas.

Formato: (antiviral_nome, patologia_substr_ou_None, populacao,
          dose_unitaria, frequencia, via,
          duracao_min_dias, duracao_max_dias, duracao_texto,
          ajuste_renal, ajuste_hepatico, observacoes, fonte_sigla)
"""

POSOLOGIA_VIRAL = [

    # ══════════════════════════════════════════════════════════════════
    # HIV — ARVs (esquemas SUS)
    # ══════════════════════════════════════════════════════════════════
    ("Tenofovir disoproxila (TDF)", "HIV/AIDS",
     "adulto", "300 mg", "24/24h", "oral", None, None, "contínuo (indefinido)",
     True, False, "Esquema TLD: 1 cp/dia (TDF 300+3TC 300+DTG 50 mg). Ajuste em ClCr < 50: TDF 300 mg a cada 48h; < 30: evitar TDF — considerar TAF.", "PCDT-HIV"),

    ("Tenofovir disoproxila (TDF)", "HIV/AIDS",
     "pediatrico", "8 mg/kg (máx 300 mg)", "24/24h", "oral", None, None, "contínuo (indefinido)",
     True, False, "≥ 10 kg: comprimido dispersível 150 mg. Comprimido adulto (300 mg) apenas ≥ 35 kg.", "PCDT-HIV-PED"),

    ("Lamivudina (3TC)", "HIV/AIDS",
     "adulto", "300 mg", "24/24h", "oral", None, None, "contínuo (indefinido)",
     True, False, "Coformulada no TLD (TDF+3TC+DTG). Ajuste em ClCr < 50 mL/min se formulação isolada.", "PCDT-HIV"),

    ("Dolutegravir (DTG)", "HIV/AIDS",
     "adulto", "50 mg", "24/24h", "oral", None, None, "contínuo (indefinido)",
     False, False, "Tomar com refeição melhora absorção. Dose dupla (50 mg 12/12h) em co-uso com rifampicina, efavirenz, nevirapina ou carbamazepina.", "PCDT-HIV"),

    ("Dolutegravir (DTG)", "HIV/AIDS",
     "pediatrico", "Vide esquema por peso", "24/24h", "oral", None, None, "contínuo (indefinido)",
     False, False, "3-6 kg: 5 mg; 6-10 kg: 15 mg; 10-14 kg: 20 mg; 14-20 kg: 25 mg; ≥ 20 kg: 50 mg (comprimido dispersível disponível no SUS).", "PCDT-HIV-PED"),

    ("Efavirenz (EFZ)", "HIV/AIDS",
     "adulto", "600 mg", "24/24h (ao deitar)", "oral", None, None, "contínuo (indefinido)",
     False, True, "Tomar em jejum ao deitar para reduzir efeitos neuropsiquiátricos (sonhos vívidos, tontura). Metabolizado por CYP3A4/2B6 — múltiplas interações.", "PCDT-HIV"),

    ("Lopinavir/ritonavir (LPV/r)", "HIV/AIDS",
     "adulto", "400/100 mg (2 cp)", "12/12h", "oral", None, None, "contínuo (indefinido)",
     False, True, "Tomar com alimentos para melhorar absorção. Diarréia é efeito adverso frequente. Em TB com rifampicina: não usar — substituir por RAL ou DTG dose dupla.", "PCDT-HIV"),

    ("Lopinavir/ritonavir (LPV/r)", "HIV/AIDS",
     "pediatrico", "Vide tabela por peso e idade", "12/12h", "oral", None, None, "contínuo (indefinido)",
     False, True, "Solução oral 80/20 mg/mL — sabor amargo; pode ser misturada a alimentos. Comprimido apenas ≥ 40 kg.", "PCDT-HIV-PED"),

    ("Raltegravir (RAL)", "HIV/AIDS",
     "adulto", "400 mg", "12/12h", "oral", None, None, "contínuo (indefinido)",
     False, False, "Não requer ajuste renal ou hepático. Interações com antiácidos (quelação com Mg²⁺): separar 2h.", "PCDT-HIV"),

    ("Zidovudina (AZT)", "HIV/AIDS",
     "gestante", "300 mg", "12/12h", "oral", None, 180, "a partir da 14ª semana até o parto",
     True, True, "TARV completo com AZT em gestantes com carga viral elevada ou sem TARV prévia. Hemoglobina basal e mensal. AZT IV 2 mg/kg no parto.", "PCDT-HIV"),

    ("Zidovudina (AZT)", "HIV/AIDS",
     "neonato", "4 mg/kg", "12/12h", "oral", 28, 28, "28 dias (profilaxia neonatal)",
     True, False, "Profilaxia neonatal para prevenção da transmissão vertical. Sirupão 10 mg/mL.", "PCDT-HIV-PED"),

    # PrEP
    ("Tenofovir disoproxila (TDF)", "PrEP HIV",
     "adulto", "300 mg + Emtricitabina 200 mg", "24/24h", "oral", None, None, "contínuo (enquanto risco)",
     True, False, "TDF/FTC 1 cp/dia. ClCr < 60: não iniciar PrEP com TDF. PrEP 2-1-1 (on-demand) para HSH: 2 cp 2-24h antes + 1 cp 24h e 48h após relação.", "PCDT-HIV"),

    # ══════════════════════════════════════════════════════════════════
    # HEPATITE B
    # ══════════════════════════════════════════════════════════════════
    ("Entecavir (ETV)", "Hepatite B",
     "adulto", "0,5 mg", "24/24h", "oral", None, None, "indefinido (ou até soroconversão HBsAg)",
     True, False, "Em jejum (2h antes ou 2h após refeição). Pacientes refratários à lamivudina: 1 mg/dia. Ajuste em ClCr < 50 mL/min.", "PCDT-HEPB"),

    ("Tenofovir disoproxila (TDF)", "Hepatite B",
     "adulto", "300 mg", "24/24h", "oral", None, None, "indefinido (ou até soroconversão HBsAg)",
     True, False, "Pode ser tomado com alimentos. Monitorar creatinina e fósforo trimestralmente. Preferido em gestantes e co-infectados HIV/HBV.", "PCDT-HEPB"),

    ("Tenofovir disoproxila (TDF)", "Hepatite B Perinatal",
     "gestante", "300 mg", "24/24h", "oral", 84, None, "a partir da 28ª semana até 12 semanas pós-parto",
     True, False, "Gestantes com HBV DNA > 200.000 UI/mL ou HBeAg positivo com qualquer DNA. Associar IGHB + vacina ao RN nas primeiras 12h de vida.", "PCDT-HEPB"),

    ("Interferon alfa-2a peguilado (Peg-IFN-α2a)", "Hepatite B",
     "adulto", "180 mcg", "1x/semana", "sc", 168, 336, "24-48 semanas",
     True, True, "Contraindicado em cirrose descompensada, psicose, doenças autoimunes. Monitorar TSH, hemograma e aminotransferases mensalmente.", "PCDT-HEPB"),

    # ══════════════════════════════════════════════════════════════════
    # HEPATITE C — DAAs
    # ══════════════════════════════════════════════════════════════════
    ("Sofosbuvir/Ledipasvir (SOF/LED)", "Hepatite C",
     "adulto", "400/90 mg (1 cp)", "24/24h", "oral", 56, 84, "8 semanas (sem cirrose, CV < 6M UI) ou 12 semanas",
     True, True, "Genótipo 1 e 4. Tomar com ou sem alimentos. 8 semanas em não cirróticos com CV < 6 milhões UI/mL; 12 semanas nos demais. Ajuste em ClCr < 30: sem dados — usar GLE/PIB.", "PCDT-HEPC"),

    ("Sofosbuvir/Velpatasvir (SOF/VEL)", "Hepatite C",
     "adulto", "400/100 mg (1 cp)", "24/24h", "oral", 84, 84, "12 semanas",
     True, True, "Pangenotípico (1-6). 12 semanas. Sem cirrose ou com cirrose compensada (Child-Pugh A). Com cirrose Child-Pugh B: adicionar RBV. Evitar em Child-Pugh C.", "PCDT-HEPC"),

    ("Glecaprevir/Pibrentasvir (GLE/PIB)", "Hepatite C",
     "adulto", "300/120 mg (3 cp)", "24/24h", "oral", 56, 84, "8 semanas (sem cirrose) ou 12 semanas (com cirrose)",
     False, True, "Pangenotípico. Tomar com alimentos. Não requer ajuste renal (útil em insuficiência renal grave/diálise). Contraindicado em Child-Pugh B/C.", "PCDT-HEPC"),

    ("Daclatasvir (DCV)", "Hepatite C",
     "adulto", "60 mg", "24/24h", "oral", 84, 168, "12-24 semanas (com sofosbuvir)",
     True, True, "Sempre associar ao sofosbuvir. Genótipos 1 e 3. 24 semanas em genótipo 3 com cirrose. Interações: rifampicina reduz DCV 80% — usar 90 mg em co-uso.", "PCDT-HEPC"),

    ("Ribavirina (RBV)", "Hepatite C",
     "adulto", "< 75 kg: 1000 mg/dia; ≥ 75 kg: 1200 mg/dia", "12/12h", "oral", 84, 168, "12-24 semanas (adjuvante)",
     True, False, "Dividir em 2 doses com refeições. Anemia hemolítica é o principal efeito adverso — monitorar hemoglobina nas semanas 2 e 4. Contraindicada em gravidez.", "PCDT-HEPC"),

    # ══════════════════════════════════════════════════════════════════
    # INFLUENZA
    # ══════════════════════════════════════════════════════════════════
    ("Oseltamivir (OST)", "Influenza",
     "adulto", "75 mg", "12/12h", "oral", 5, 5, "5 dias (tratamento) / 10 dias (profilaxia pós-exposição)",
     True, False, "Iniciar em ≤ 48h dos sintomas para máxima eficácia; iniciar mesmo após 48h em hospitalizados ou graves. Náusea frequente — tomar com alimentos. Profilaxia: 75 mg 24/24h × 10 dias.", "PCDT-INFLUENZA"),

    ("Oseltamivir (OST)", "Influenza",
     "pediatrico", "Vide tabela por peso", "12/12h", "oral", 5, 5, "5 dias",
     True, False, "≤ 15 kg: 30 mg 12/12h; 15-23 kg: 45 mg 12/12h; 23-40 kg: 60 mg 12/12h; > 40 kg: 75 mg 12/12h. Suspensão 12 mg/mL disponível.", "PCDT-INFLUENZA"),

    ("Oseltamivir (OST)", "Influenza",
     "gestante", "75 mg", "12/12h", "oral", 5, 5, "5 dias",
     True, False, "SEGURO em todos os trimestres da gestação. Gestantes são grupo de risco para influenza grave — indicação prioritária para tratamento precoce.", "PCDT-INFLUENZA"),

    ("Zanamivir", "Influenza",
     "adulto", "2 inalações (10 mg)", "12/12h", "inalatória", 5, 5, "5 dias",
     False, False, "Contraindicado em asma ou DPOC grave (risco de broncoespasmo). Útil em resistência ao oseltamivir (mutação H275Y no H1N1). Profilaxia: 2 inalações/dia × 10 dias.", "PCDT-INFLUENZA"),

    # ══════════════════════════════════════════════════════════════════
    # COVID-19
    # ══════════════════════════════════════════════════════════════════
    ("Nirmatrelvir/Ritonavir (NMV/r)", "COVID-19",
     "adulto", "300/100 mg (2 cp NMV + 1 cp RTV)", "12/12h", "oral", 5, 5, "5 dias",
     True, True, "Iniciar em ≤ 5 dias dos sintomas. ClCr 30-59: dose reduzida (150/100 mg 12/12h). Contraindicado se ClCr < 30. NUMEROSAS interações via CYP3A4 (estatinas, anticoagulantes, imunossupressores). Verificar interações ANTES de prescrever.", "PCDT-COVID19"),

    ("Remdesivir (RDV)", "COVID-19",
     "adulto", "200 mg D1, depois 100 mg D2-D5", "24/24h", "iv", 3, 5, "3-5 dias",
     True, False, "Uso hospitalar. Infusão IV em 30-120 min. D1: 200 mg ataque; D2-D5: 100 mg manutenção. Contraindicado se ClCr < 30 mL/min (veículo sulfobutiléter β-ciclodextrina acumula). Monitorar enzimas hepáticas.", "PCDT-COVID19"),

    ("Molnupiravir", "COVID-19",
     "adulto", "800 mg (4 cp)", "12/12h", "oral", 5, 5, "5 dias",
     True, False, "Iniciar em ≤ 5 dias. Contraindicado na gravidez e aleitamento. Uso contraceptivo obrigatório durante e por 4 dias após (homens: 3 meses) pelo potencial mutagênico. Não usar em < 18 anos.", "PCDT-COVID19"),

    # ══════════════════════════════════════════════════════════════════
    # HERPES SIMPLES (HSV)
    # ══════════════════════════════════════════════════════════════════
    ("Aciclovir (ACV)", "Herpes Simples",
     "adulto", "200 mg (orolabial) ou 400 mg (genital)", "5x/dia", "oral", 5, 10, "5 dias (orolabial) / 7-10 dias (primo-infecção genital)",
     True, False, "Recorrência genital: 400 mg 3x/dia × 5 dias ou 800 mg 2x/dia × 5 dias. Supressão crônica (≥ 6 recorrências/ano): 400 mg 2x/dia indefinidamente.", "SBI-VIRAL"),

    ("Aciclovir (ACV)", "Encefalite Herpética",
     "adulto", "10 mg/kg", "8/8h", "iv", 14, 21, "14-21 dias",
     True, False, "URGÊNCIA NEUROLÓGICA: iniciar imediatamente na suspeita clínica — não aguardar PCR. Infundir em 60 min para evitar nefrotoxicidade. Ajuste obrigatório em insuficiência renal.", "SBI-VIRAL"),

    ("Aciclovir (ACV)", "Herpes Neonatal",
     "neonato", "20 mg/kg", "8/8h", "iv", 14, 21, "14 dias (cutâneo/SNC) / 21 dias (disseminado)",
     True, False, "Herpes neonatal é emergência. Manter hidratação adequada para evitar nefrotoxicidade. Manutenção oral com aciclovir × 6 meses após tratamento IV reduz recorrências e sequelas neurológicas.", "SBI-VIRAL"),

    ("Valaciclovir (VACV)", "Herpes Simples",
     "adulto", "1 g", "12/12h", "oral", 7, 10, "7-10 dias (primo-infecção genital)",
     True, False, "Recorrência: 500 mg 2x/dia × 3-5 dias. Supressão: 500 mg/dia. Reduz transmissão ao parceiro em 48%. Melhor opção oral disponível pelo SUS parcial.", "SBI-VIRAL"),

    # ══════════════════════════════════════════════════════════════════
    # VARICELA E HERPES ZOSTER
    # ══════════════════════════════════════════════════════════════════
    ("Aciclovir (ACV)", "Varicela",
     "adulto", "800 mg", "5x/dia", "oral", 7, 7, "7 dias",
     True, False, "Adultos não vacinados: iniciar em ≤ 24h do exantema. Formas graves/imunossuprimidos: aciclovir IV 10 mg/kg 8/8h × 7-10 dias.", "SVS-VARICELA"),

    ("Aciclovir (ACV)", "Varicela",
     "pediatrico", "20 mg/kg (máx 800 mg)", "4x/dia", "oral", 5, 5, "5 dias",
     True, False, "Crianças imunocompetentes: benefício moderado; indicar em: > 12 anos, doença cutânea/pulmonar prévia, salicilato crônico. Imunossuprimidos: IV obrigatório.", "SVS-VARICELA"),

    ("Aciclovir (ACV)", "Varicela",
     "gestante", "800 mg", "5x/dia", "oral", 7, 7, "7 dias",
     True, False, "Varicela na gestante tem risco aumentado de pneumonite grave (mortalidade 40% sem tratamento). Internar se pneumonite ou doença grave; aciclovir IV 10 mg/kg 8/8h.", "SVS-VARICELA"),

    ("Aciclovir (ACV)", "Herpes Zoster",
     "adulto", "800 mg", "5x/dia", "oral", 7, 7, "7 dias",
     True, False, "Iniciar em ≤ 72h do exantema. Indicações obrigatórias: > 50 anos, envolvimento oftálmico, imunossupressão, qualquer zoster > 50 vesículas. Zoster disseminado: IV 10 mg/kg 8/8h.", "SVS-VARICELA"),

    ("Valaciclovir (VACV)", "Herpes Zoster",
     "adulto", "1 g", "3x/dia", "oral", 7, 7, "7 dias",
     True, False, "Superior ao aciclovir oral em nevralgia pós-herpética (concentrações mais sustentadas). Ajuste em ClCr < 50 mL/min.", "SVS-VARICELA"),

    # ══════════════════════════════════════════════════════════════════
    # CMV
    # ══════════════════════════════════════════════════════════════════
    ("Ganciclovir (GCV)", "Citomegalovirose (CMV)",
     "adulto", "5 mg/kg", "12/12h", "iv", 14, 21, "14-21 dias (indução)",
     True, False, "Infusão em 1h. Ajuste obrigatório em insuficiência renal. Após indução: manutenção com valganciclovir 900 mg/dia VO. Monitorar leucócitos (risco de neutropenia).", "SBI-VIRAL"),

    ("Valganciclovir (VGCV)", "Citomegalovirose (CMV)",
     "adulto", "900 mg (tratamento) ou 450 mg (profilaxia)", "12/12h ou 24/24h", "oral", 14, None, "14-21 dias (tratamento) / 100-200 dias (profilaxia em transplante)",
     True, False, "Tomar com alimentos — aumenta biodisponibilidade em 30%. Ajuste em ClCr < 60 mL/min (tabela de ajuste obrigatória). Bioequivalente ao ganciclovir IV.", "SBI-VIRAL"),

    ("Valganciclovir (VGCV)", "CMV Congênito",
     "neonato", "16 mg/kg", "12/12h", "oral", 42, 180, "6 semanas a 6 meses conforme resposta",
     True, False, "Solução oral 50 mg/mL. Monitorar CBC semanalmente no 1º mês. 6 meses de tratamento superiores a 6 semanas em desfechos auditivos (estudo CASG 112).", "SBI-VIRAL"),

    ("Foscarnet (PFA)", "CMV ou HSV resistente",
     "adulto", "60 mg/kg", "8/8h (CMV) ou 40 mg/kg 8/8h (HSV)", "iv", 14, 21, "14-21 dias",
     True, False, "Altamente nefrotóxico — hidratação prévia com 1000 mL SF obrigatória. Quelante de cálcio: monitorar Ca²⁺, Mg²⁺, K⁺ e fósforo. Ulcerações genitais pelo mecanismo de quelação.", "SBI-VIRAL"),

    # ══════════════════════════════════════════════════════════════════
    # INTERFERON PEGUILADO (HBV/HCV histórico)
    # ══════════════════════════════════════════════════════════════════
    ("Interferon alfa-2a peguilado (Peg-IFN-α2a)", "Hepatite C",
     "adulto", "180 mcg", "1x/semana", "sc", 168, 336, "24-48 semanas (em desuso com DAAs disponíveis)",
     True, True, "Em desuso para HCV com disponibilidade de DAAs. Ainda usado para HBV. Efeitos adversos: síndrome gripal, depressão, leucopenia — pré-medicação com paracetamol antes das injeções.", "PCDT-HEPC"),

    ("Interferon alfa-2b peguilado (Peg-IFN-α2b)", "Hepatite C",
     "adulto", "1,5 mcg/kg", "1x/semana", "sc", 168, 336, "24-48 semanas (em desuso com DAAs disponíveis)",
     True, True, "Dose ajustada por peso. Semelhante ao Peg-IFN-α2a. Em desuso para HCV.", "PCDT-HEPC"),
]

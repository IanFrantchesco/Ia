"""
Dados de eficácia de antivirais por vírus e patologia.
Baseado em: PCDTs MS (HIV 2022, Hepatite B 2022, Hepatite C 2022, Influenza, COVID-19),
            SVS/MS GVS 5ª ed. 2022, SBI, SBMT, ANVISA bulas, OPAS/PAHO adaptado Brasil.

Formato:
virus_nome_cientifico -> lista de:
  (antiviral_nome_generico, patologia_nome_parcial_ou_None,
   eficacia_pct, linha_tratamento, nivel_evidencia, resistencia_br_pct, fonte_sigla, ano, consideracoes)

Nota: vírus sem antiviral específico aprovado têm eficácia = None e considições explicam tratamento suportivo.
"""

# Estrutura: dict { virus_nome_cientifico: [ (antiviral, patologia_substr, ef%, linha, evidencia, resist_br%, fonte, ano, obs) ] }

EFICACIA_VIRAL = {

    # ══════════════════════════════════════════════════════════════════
    # ARBOVIROSES — sem antiviral específico aprovado no Brasil
    # ══════════════════════════════════════════════════════════════════
    "Dengue virus (DENV 1-4)": [
        (None, "Dengue (formas leve, moderada e grave)", None, None, "A", None, "SVS-DENGUE", 2022,
         "Sem antiviral específico aprovado. Tratamento exclusivamente suportivo: hidratação, "
         "analgesia (paracetamol), repouso. AAS e AINEs contraindicados (risco hemorrágico). "
         "Monitoramento de sinais de alarme e hematócrito é o pilar do manejo clínico."),
    ],
    "Zika virus (ZIKV)": [
        (None, "Zika (infecção aguda e síndrome congênita)", None, None, "A", None, "SVS-DENGUE", 2022,
         "Sem antiviral específico aprovado. Tratamento suportivo: paracetamol, hidratação, repouso. "
         "Gestantes: acompanhamento fetal rigoroso com ultrassonografia seriada. "
         "Síndrome congênita: suporte multidisciplinar (fisioterapia, fonoaudiologia, neurodesenvolvimento)."),
    ],
    "Chikungunya virus (CHIKV)": [
        (None, "Chikungunya (aguda e crônica)", None, None, "A", None, "SVS-DENGUE", 2022,
         "Sem antiviral específico aprovado. Fase aguda: paracetamol e hidratação (evitar AINEs nas primeiras 72h). "
         "Fase pós-aguda/crônica: AINEs, corticoides em cursos curtos, fisioterapia. "
         "Artrite crônica refratária: hidroxicloroquina ou metotrexato podem ser considerados (off-label)."),
    ],
    "Yellow fever virus (YFV)": [
        (None, "Febre Amarela (silvestre e urbana)", None, None, "A", None, "SVS-FEBAMARELA", 2022,
         "Sem antiviral específico aprovado. Tratamento suportivo intensivo: reposição volêmica, "
         "suporte de função renal (diálise em IRA), transfusões em casos hemorrágicos, suporte respiratório. "
         "Ribavirina foi usada sem evidência robusta de benefício."),
    ],
    "West Nile virus (WNV)": [
        (None, "Febre do Nilo Ocidental (casos importados e autóctones)", None, None, "A", None, "OPAS-BR", 2022,
         "Sem antiviral específico aprovado globalmente. Tratamento suportivo. "
         "Encefalite pelo WNV: suporte em UTI, anticonvulsivantes se necessário. "
         "Imunoglobulina IV (IVIG) e interferon alfa usados off-label sem evidência consistente."),
    ],

    # ══════════════════════════════════════════════════════════════════
    # HEPATITES VIRAIS
    # ══════════════════════════════════════════════════════════════════
    "Hepatitis A virus (HAV)": [
        (None, "Hepatite A", None, None, "A", None, "SVS-HEPAT-AE", 2022,
         "Sem antiviral específico. Tratamento suportivo: repouso, hidratação, dieta adequada. "
         "Hepatite fulminante: transplante hepático é a única opção curativa. "
         "Vacinação é a medida preventiva mais eficaz (2 doses, eficácia > 95%)."),
    ],
    "Hepatitis B virus (HBV)": [
        ("Entecavir (ETV)",           "Hepatite B (aguda e crônica)",  97.0, 1, "A",  1.0, "PCDT-HEPB", 2022, "1ª linha SUS para HBV crônico com indicação de tratamento; alta barreira genética; HBV DNA indetectável em > 90% em 48 semanas"),
        ("Tenofovir disoproxila (TDF)", "Hepatite B (aguda e crônica)", 98.0, 1, "A",  0.0, "PCDT-HEPB", 2022, "1ª linha SUS; alta barreira genética; preferido em gestantes e co-infectados HIV/HBV; sem resistência documentada no Brasil"),
        ("Interferon alfa-2a peguilado (Peg-IFN-α2a)", "Hepatite B (aguda e crônica)", 30.0, 2, "A",  5.0, "PCDT-HEPB", 2022, "Soroconversão HBeAg em ~30% e HBsAg em < 10%; preferido em pacientes jovens com HBeAg+ e alta atividade inflamatória; 48 semanas SC"),
        ("Tenofovir alafenamida (TAF)", "Hepatite B (aguda e crônica)", 97.0, 2, "B",  0.0, "PCDT-HEPB", 2022, "Eficácia similar ao TDF com menor toxicidade renal e óssea; opção em insuficiência renal; ainda não disponível no SUS"),
        ("Tenofovir disoproxila (TDF)", "Hepatite B Perinatal (transmissão vertical)", 98.0, 1, "A",  0.0, "PCDT-HEPB", 2022, "Gestantes com HBV DNA elevado: TDF no 3º trimestre reduz transmissão vertical; imunoglobulina + vacina ao nascimento obrigatórias"),
    ],
    "Hepatitis C virus (HCV)": [
        ("Sofosbuvir/Ledipasvir (SOF/LED)", "Hepatite C (aguda e crônica)", 97.0, 1, "A",  1.0, "PCDT-HEPC", 2022, "Genótipo 1 (predominante no BR); 8-12 semanas; RVS > 97%; sem ribavirina na maioria dos casos não cirróticos"),
        ("Sofosbuvir/Velpatasvir (SOF/VEL)", "Hepatite C (aguda e crônica)", 98.0, 1, "A",  1.0, "PCDT-HEPC", 2022, "Pangenotípico (genótipos 1-6); 12 semanas; RVS > 97%; 1ª linha para genótipos 2, 3, 4, 5, 6 no SUS"),
        ("Glecaprevir/Pibrentasvir (GLE/PIB)", "Hepatite C (aguda e crônica)", 98.0, 1, "A",  1.0, "PCDT-HEPC", 2022, "Pangenotípico; 8 semanas sem cirrose, 12 com cirrose compensada; opção em co-infectados HIV/HCV"),
        ("Daclatasvir (DCV)", "Hepatite C (aguda e crônica)", 92.0, 1, "A",  2.0, "PCDT-HEPC", 2022, "Usado com sofosbuvir; genótipos 1 e 3; disponível SUS; 24 semanas em genótipo 3 com cirrose"),
        ("Ribavirina (RBV)", "Hepatite C (aguda e crônica)", 60.0, 2, "A", None, "PCDT-HEPC", 2022, "Adjuvante em situações especiais: genótipo 3 com cirrose, falha virológica prévia; anemia hemolítica é efeito adverso principal"),
    ],
    "Hepatitis D virus (HDV)": [
        ("Interferon alfa-2a peguilado (Peg-IFN-α2a)", "Hepatite D (Coinfecção e Superinfecção por HDV)", 25.0, 1, "B", 10.0, "PCDT-HEPB", 2022, "Único tratamento disponível no Brasil; supressão do HDV RNA em 25-30% após 48 semanas; benefício limitado e recidivas frequentes após suspensão"),
    ],
    "Hepatitis E virus (HEV)": [
        (None, "Hepatite E", None, None, "A", None, "SVS-HEPAT-AE", 2022,
         "Sem antiviral específico aprovado em imunocompetentes — autolimitada em 4-6 semanas. "
         "Imunossuprimidos com HEV crônico: redução da imunossupressão é a 1ª medida; "
         "ribavirina (off-label) em casos graves/crônicos em transplantados com boas taxas de resposta. "
         "Gestantes com hepatite fulminante: suporte intensivo e transplante hepático de emergência."),
    ],

    # ══════════════════════════════════════════════════════════════════
    # RETROVIROSES
    # ══════════════════════════════════════════════════════════════════
    "Human immunodeficiency virus 1/2 (HIV-1/2)": [
        # Esquemas de 1ª linha SUS
        ("Tenofovir disoproxila (TDF)",   "HIV/AIDS (infecção aguda, crônica e AIDS estabelecida)", 97.0, 1, "A",  3.0, "PCDT-HIV", 2022, "ITRN backbone do esquema preferencial TLD (TDF+3TC+DTG) — carga viral indetectável em > 90% em 48 semanas"),
        ("Lamivudina (3TC)",               "HIV/AIDS (infecção aguda, crônica e AIDS estabelecida)", 97.0, 1, "A",  3.0, "PCDT-HIV", 2022, "ITRN componente universal de todos os esquemas SUS; resistência M184V reduz eficácia"),
        ("Dolutegravir (DTG)",             "HIV/AIDS (infecção aguda, crônica e AIDS estabelecida)", 98.0, 1, "A",  0.5, "PCDT-HIV", 2022, "INSTI de 2ª geração; esquema preferencial TLD no SUS; alta barreira genética; atenção ao defeito do tubo neural se gestação no 1º trimestre"),
        ("Efavirenz (EFZ)",                "HIV/AIDS (infecção aguda, crônica e AIDS estabelecida)", 85.0, 2, "A",  8.0, "PCDT-HIV", 2022, "Substituído pelo DTG como 1ª linha; ainda usado em coinfecção TB/HIV com rifampicina (400 mg/dia; DTG dose dupla é alternativa)"),
        ("Lopinavir/ritonavir (LPV/r)",    "HIV/AIDS (infecção aguda, crônica e AIDS estabelecida)", 88.0, 2, "A",  5.0, "PCDT-HIV", 2022, "Esquema preferencial pediátrico SUS; 2ª linha em adultos após falha de DTG; IP de alta barreira genética"),
        ("Raltegravir (RAL)",              "HIV/AIDS (infecção aguda, crônica e AIDS estabelecida)", 90.0, 2, "A",  2.0, "PCDT-HIV", 2022, "Esquema pediátrico SUS alternativo; INSTI 1ª geração; 2 doses/dia"),
        ("Darunavir/ritonavir ou cobicistate (DRV/r ou DRV/c)", "HIV/AIDS (infecção aguda, crônica e AIDS estabelecida)", 92.0, 2, "A",  1.0, "PCDT-HIV", 2022, "Esquema de resgate em HIV multirresistente; alta barreira genética; requer genotipagem prévia"),
        ("Zidovudina (AZT)",               "HIV/AIDS (infecção aguda, crônica e AIDS estabelecida)", 85.0, 3, "A", 15.0, "PCDT-HIV", 2022, "Profilaxia de transmissão vertical e PEP; não é mais esquema de 1ª linha em adultos pela toxicidade"),
        # PrEP
        ("Tenofovir disoproxila (TDF)",   None, 99.0, 1, "A",  0.0, "PCDT-HIV", 2022, "PrEP diária: eficácia > 99% com boa adesão; disponível SUS para populações-chave; TDF/FTC é o esquema padrão"),
        ("Cabotegravir (CAB)",             None, 99.0, 1, "A",  0.0, "PCDT-HIV", 2022, "PrEP injetável (CAB IM a cada 2 meses): não inferior à PrEP oral; aprovado ANVISA; ainda não disponível SUS em 2024"),
    ],
    "Human T-lymphotropic virus 1 (HTLV-1)": [
        (None, "Infecção pelo HTLV-1 (portador e formas clínicas)", None, None, "B", None, "SVS-HTLV", 2022,
         "Sem antiviral específico que altere o curso da doença. Portadores assintomáticos: acompanhamento periódico. "
         "HAM/TSP: corticoides IV em pulsos, interferon alfa, metotrexato (imunomodulação) — evidência limitada. "
         "ATLL: quimioterapia convencional (CHOP-like), alentuzumabe, mogamulizumabe (não disponível SUS); "
         "transplante alogênico de células tronco em casos selecionados."),
        (None, "HTLV — Leucemia/Linfoma de Células T do Adulto (ATLL)", None, None, "C", None, "SVS-HTLV", 2022,
         "Quimioterapia convencional (VCAP-AMP-VECP) com resposta parcial; zidovudina + interferon para subtipo indolente. "
         "Transplante alogênico em remissão como único tratamento com potencial curativo."),
        (None, "HTLV — Mielopatia Associada ao HTLV / Paraparesia Espástica Tropical (HAM/TSP)", None, None, "C", None, "SVS-HTLV", 2022,
         "Sem tratamento modificador de doença comprovado. Corticoide e interferon alfa para exacerbações. "
         "Fisioterapia, manejo da bexiga neurogênica e espasticidade (baclofeno) são pilares do tratamento."),
    ],

    # ══════════════════════════════════════════════════════════════════
    # HERPESVIROSES
    # ══════════════════════════════════════════════════════════════════
    "Herpes simplex virus 1 (HSV-1)": [
        ("Aciclovir (ACV)",       "Herpes Simples (orolabial, genital e neonatal)", 90.0, 1, "A",  2.0, "SBI-VIRAL", 2022, "Orolabial: aciclovir tópico ou oral em primo-infecção; 5 dias. Encefalite: aciclovir IV 10 mg/kg 8/8h × 14-21 dias"),
        ("Valaciclovir (VACV)",   "Herpes Simples (orolabial, genital e neonatal)", 92.0, 1, "A",  2.0, "SBI-VIRAL", 2022, "Melhor biodisponibilidade oral que aciclovir; posologia mais conveniente (2x/dia vs 5x/dia)"),
        ("Foscarnet (PFA)",       "Herpes Simples (orolabial, genital e neonatal)", 80.0, 2, "B",  0.0, "SBI-VIRAL", 2022, "Reservado para HSV resistente ao aciclovir (principalmente em imunossuprimidos/HIV)"),
        ("Aciclovir (ACV)",       "Encefalite Herpética (HSV-1)",                  80.0, 1, "A",  2.0, "SBI-VIRAL", 2022, "Aciclovir IV 10 mg/kg 8/8h × 14-21 dias; iniciar na suspeita sem aguardar PCR confirmatório; reduz mortalidade de 70% para 20%"),
    ],
    "Herpes simplex virus 2 (HSV-2)": [
        ("Aciclovir (ACV)",       "Herpes Simples (orolabial, genital e neonatal)", 88.0, 1, "A",  2.0, "SBI-VIRAL", 2022, "Genital: 200 mg 5x/dia × 5-10 dias (primo-infecção) ou supressão 400 mg 2x/dia para recorrências frequentes"),
        ("Valaciclovir (VACV)",   "Herpes Simples (orolabial, genital e neonatal)", 91.0, 1, "A",  2.0, "SBI-VIRAL", 2022, "Posologia conveniente: 1 g 2x/dia × 7-10 dias; supressão 500 mg/dia — reduz transmissão ao parceiro em 48%"),
        ("Aciclovir (ACV)",       "Herpes Neonatal (HSV)",                          88.0, 1, "A",  1.0, "SBI-VIRAL", 2022, "Herpes neonatal: aciclovir IV 20 mg/kg 8/8h × 14-21 dias (cutâneo/SNC) ou × 21 dias (disseminado)"),
    ],
    "Varicella-zoster virus (VZV)": [
        ("Aciclovir (ACV)",       "Varicela (catapora)",                            85.0, 1, "A",  2.0, "SVS-VARICELA", 2022, "Indicado em: adultos, imunossuprimidos, gestantes, recém-nascidos; crianças saudáveis: benefício moderado — decisão individualizada"),
        ("Valaciclovir (VACV)",   "Varicela (catapora)",                            88.0, 1, "A",  2.0, "SVS-VARICELA", 2022, "Adultos: 1 g 3x/dia × 7 dias; melhor opção oral que aciclovir pela biodisponibilidade"),
        ("Aciclovir (ACV)",       "Herpes Zoster (cobreiro)",                       82.0, 1, "A",  2.0, "SVS-VARICELA", 2022, "Indicado se: > 50 anos, moderado-grave, envolvimento oftálmico, imunossuprimidos; iniciar em ≤ 72h do exantema"),
        ("Valaciclovir (VACV)",   "Herpes Zoster (cobreiro)",                       87.0, 1, "A",  2.0, "SVS-VARICELA", 2022, "Superior ao aciclovir oral em nevralgia pós-herpética; 1 g 3x/dia × 7 dias; preferido quando disponível"),
    ],
    "Cytomegalovirus (CMV)": [
        ("Ganciclovir (GCV)",     "Citomegalovirose (CMV) em Imunocomprometidos",  85.0, 1, "A",  5.0, "SBI-VIRAL", 2022, "Tratamento de indução: 5 mg/kg IV 12/12h × 14-21 dias; mielossupressão dose-limitante; monitorar hemograma"),
        ("Valganciclovir (VGCV)", "Citomegalovirose (CMV) em Imunocomprometidos",  87.0, 1, "A",  5.0, "SBI-VIRAL", 2022, "Oral com biodisponibilidade equivalente ao ganciclovir IV; tratamento e profilaxia em transplantados (SUS em transplante)"),
        ("Foscarnet (PFA)",       "Citomegalovirose (CMV) em Imunocomprometidos",  78.0, 2, "B",  0.0, "SBI-VIRAL", 2022, "CMV resistente ao ganciclovir (mutação UL97/UL54); alta nefrotoxicidade — hidratação rigorosa"),
        ("Cidofovir (CDV)",       "Citomegalovirose (CMV) em Imunocomprometidos",  75.0, 2, "B",  0.0, "SBI-VIRAL", 2022, "CMV multirresistente; 1x/semana por 2 semanas (indução) + probenecida; alta nefrotoxicidade"),
        ("Ganciclovir (GCV)",     "CMV Congênito",                                  80.0, 1, "B",  2.0, "SBI-VIRAL", 2022, "Recém-nascidos sintomáticos: aciclovir IV × 6 semanas; melhora desfecho auditivo e neurológico em formas moderadas-graves"),
        ("Valganciclovir (VGCV)", "CMV Congênito",                                  82.0, 1, "A",  2.0, "SBI-VIRAL", 2022, "Fase de manutenção oral após indução IV; 6 meses totais reduzem sequelas auditivas vs 6 semanas"),
    ],
    "Epstein-Barr virus (EBV)": [
        (None, "Mononucleose Infecciosa (EBV)", None, None, "A", None, "SBI-VIRAL", 2022,
         "Sem antiviral específico indicado na mononucleose típica — autolimitada em 2-4 semanas. "
         "Aciclovir e valaciclovir suprimem replicação mas não alteram sintomas clínicos — não recomendados na primo-infecção. "
         "Tratamento suportivo: repouso, analgesia/antipirética (paracetamol), evitar AAS. "
         "Corticoide IV em: obstrução de via aérea, trombocitopenia grave, anemia hemolítica."),
    ],

    # ══════════════════════════════════════════════════════════════════
    # INFLUENZA
    # ══════════════════════════════════════════════════════════════════
    "Influenza virus A/B/C": [
        ("Oseltamivir (OST)",     "Influenza (gripe sazonal e pandêmica)", 85.0, 1, "A",  2.0, "PCDT-INFLUENZA", 2022, "Reduz duração em ~1,3 dias; reduz complicações em grupos de risco; iniciar em ≤ 48h — mas iniciar mesmo tardio em graves/hospitalizados"),
        ("Zanamivir",             "Influenza (gripe sazonal e pandêmica)", 83.0, 2, "A",  0.5, "PCDT-INFLUENZA", 2022, "Alternativa ao oseltamivir; inalatória — contraindicada em asma/DPOC grave; útil em resistência ao oseltamivir (H275Y)"),
        ("Baloxavir marboxil",    "Influenza (gripe sazonal e pandêmica)", 88.0, 2, "A",  1.0, "PCDT-INFLUENZA", 2022, "Dose única; inibidor de endonuclease PA; eficaz em cepas resistentes ao oseltamivir; aprovado ANVISA 2023"),
    ],

    # ══════════════════════════════════════════════════════════════════
    # COVID-19
    # ══════════════════════════════════════════════════════════════════
    "SARS-CoV-2": [
        ("Nirmatrelvir/Ritonavir (NMV/r)", "COVID-19 (infecção aguda, grave e síndrome pós-COVID)", 89.0, 1, "A",  1.0, "PCDT-COVID19", 2022, "Redução de 89% em hospitalização/morte em não vacinados de alto risco; iniciar em ≤ 5 dias dos sintomas; numerosas interações medicamentosas via CYP3A4"),
        ("Remdesivir (RDV)",               "COVID-19 (infecção aguda, grave e síndrome pós-COVID)", 70.0, 1, "A",  0.5, "PCDT-COVID19", 2022, "Uso hospitalar: reduz tempo de hospitalização; 3-5 dias IV; menor evidência em pacientes em VMI"),
        ("Molnupiravir",                   "COVID-19 (infecção aguda, grave e síndrome pós-COVID)", 30.0, 2, "A",  0.5, "PCDT-COVID19", 2022, "Redução de ~30% em hospitalização em cepas Delta; menor eficácia em Ômicron; contraindicado na gravidez; mutagênico"),
    ],

    # ══════════════════════════════════════════════════════════════════
    # RAIVA
    # ══════════════════════════════════════════════════════════════════
    "Rabies lyssavirus": [
        (None, "Raiva (raiva humana transmitida por cão, morcego ou animais silvestres)", None, None, "A", None, "SVS-RAIVA", 2022,
         "Sem antiviral específico eficaz após início dos sintomas — raiva estabelecida é INVARIAVELMENTE FATAL. "
         "Protocolo Milwaukee (amantadina, ribavirina, cetamina, midazolam) teve resultados inconsistentes e NÃO é recomendado rotineiramente. "
         "ÚNICA intervenção eficaz: Profilaxia Pós-Exposição (PEP) = limpeza exaustiva da ferida + vacina antirrábica + "
         "imunoglobulina antirrábica humana (IGHAB) nas exposições de alto risco — disponível no SUS (CRIE)."),
    ],

    # ══════════════════════════════════════════════════════════════════
    # EXANTEMAS VIRAIS
    # ══════════════════════════════════════════════════════════════════
    "Measles morbillivirus": [
        (None, "Sarampo", None, None, "A", None, "SVS-SARAMPO", 2022,
         "Sem antiviral específico aprovado. Tratamento suportivo: isolamento respiratório, "
         "vitamina A (suplementação reduz mortalidade em desnutridos e crianças < 2 anos), antipirético. "
         "Vacinação com SCR/SCRV é a única medida preventiva eficaz (2 doses, eficácia > 97%)."),
    ],
    "Rubella virus": [
        (None, "Rubéola (adquirida e congênita)", None, None, "A", None, "SVS-SARAMPO", 2022,
         "Sem antiviral específico. Rubéola adquirida autolimitada — sintomático (paracetamol). "
         "Síndrome da Rubéola Congênita (SRC): sem tratamento curativo; suporte multidisciplinar para sequelas "
         "(surdez, catarata, cardiopatia). Vacinação com SCR é a única prevenção eficaz."),
    ],
    "Mumps orthorubulavirus": [
        (None, "Caxumba / Parotidite Epidêmica", None, None, "A", None, "SVS-SARAMPO", 2022,
         "Sem antiviral específico. Tratamento suportivo: analgesia (paracetamol/ibuprofeno), hidratação, dieta macia. "
         "Orquite: suporte escrotal, analgesia potente (podem ser necessários opioides); corticoides controversos. "
         "Meningite asséptica: analgesia e hidratação; autolimitada."),
    ],
    "Enterovirus 71 (EV-A71)": [
        (None, "Doença Mão-Pé-Boca (Enterovírus 71 e Coxsackievírus A16)", None, None, "A", None, "SBI-VIRAL", 2022,
         "Sem antiviral específico aprovado para EV-A71 ou CVA16. Tratamento suportivo. "
         "Formas neurológicas graves (EV-A71): milrinona IV (reduz edema pulmonar neurogênico), "
         "IVIG off-label, suporte em UTI. "
         "Vacina contra EV-A71 disponível na China — sem aprovação no Brasil até 2024."),
    ],

    # ══════════════════════════════════════════════════════════════════
    # GASTRENTERITE VIRAL
    # ══════════════════════════════════════════════════════════════════
    "Rotavirus A": [
        (None, "Rotavirose (diarreia por Rotavírus)", None, None, "A", None, "SBI-VIRAL", 2022,
         "Sem antiviral específico. Tratamento exclusivamente suportivo: "
         "reidratação oral (SRO OMS) é o pilar — reduz mortalidade; "
         "reidratação IV se desidratação grave. Vacina (Rotarix) disponível no SUS desde 2006 com impacto de ~80% na redução de hospitalizações."),
    ],
    "Norovirus (GI/GII)": [
        (None, "Norovirose (diarreia e vômito por Norovírus)", None, None, "A", None, "SBI-VIRAL", 2022,
         "Sem antiviral específico aprovado. Tratamento suportivo: reidratação oral ou IV, sintomáticos (ondansetrona para vômitos). "
         "Controle de infecção em ambientes coletivos: lavagem de mãos com água e sabão (álcool-gel é menos eficaz contra norovírus), "
         "hipoclorito para descontaminação de superfícies."),
    ],

    # ══════════════════════════════════════════════════════════════════
    # INFECÇÃO RESPIRATÓRIA — VSR
    # ══════════════════════════════════════════════════════════════════
    "Human respiratory syncytial virus (RSV)": [
        (None, "Infecção pelo Vírus Sincicial Respiratório (VSR/RSV)", None, None, "A", None, "SBI-VIRAL", 2022,
         "Sem antiviral específico rotineiramente indicado. Ribavirina inalatória: sem evidência robusta — não recomendada rotineiramente. "
         "Tratamento suportivo: oxigenioterapia, broncodilatadores (benefício limitado), aspiração de secreções. "
         "Profilaxia com palivizumabe (anticorpo monoclonal) disponível no SUS para prematuros < 29 semanas e cardiopatas congênitas cianóticas. "
         "Nirsevimabe (anticorpo de ação prolongada) em implantação para profilaxia universal de lactentes."),
    ],

    # ══════════════════════════════════════════════════════════════════
    # ADENOVÍRUS
    # ══════════════════════════════════════════════════════════════════
    "Human adenovirus (HAdV)": [
        (None, "Infecção por Adenovírus Respiratório", None, None, "A", None, "SBI-VIRAL", 2022,
         "Sem antiviral específico para uso rotineiro em imunocompetentes. "
         "Cidofovir IV off-label em imunossuprimidos com adenovirose grave/disseminada (transplantados); "
         "brincidofovir (oral) como alternativa com menos toxicidade — não disponível no Brasil. "
         "Tratamento de imunocompetentes: suportivo."),
    ],

    # ══════════════════════════════════════════════════════════════════
    # HPV
    # ══════════════════════════════════════════════════════════════════
    "Human papillomavirus (HPV)": [
        (None, "Infecção pelo HPV (verrugas genitais e lesões precursoras)", None, None, "A", None, "SVS-HPV", 2022,
         "Sem antiviral específico que elimine a infecção pelo HPV. "
         "Tratamento das verrugas genitais (condilomas): podofilotoxina tópica, ácido tricloroacético, crioterapia, eletrocauterização ou laser. "
         "Imiquimode (imunomodulador tópico) disponível para condilomas. "
         "Lesões precursoras cervicais (NIC 2/3): excisão (LEEP/conização) — não antiviral. "
         "PREVENÇÃO: vacinação profilática HPV quadrivalente/nonavalente no SUS para meninas 9-14 anos e meninos 11-14 anos."),
    ],

    # ══════════════════════════════════════════════════════════════════
    # HANTAVÍRUS
    # ══════════════════════════════════════════════════════════════════
    "Hantavirus (Araraquara, Juquitiba, Laguna Negra)": [
        (None, "Hantavirose (Síndrome Cardiopulmonar por Hantavírus — SCPH)", None, None, "A", None, "SVS-HANTA", 2022,
         "Sem antiviral específico aprovado para SCPH. Ribavirina IV foi testada sem benefício consistente em SCPH — não recomendada. "
         "Tratamento exclusivamente suportivo intensivo em UTI: suporte respiratório (VMI precoce), "
         "ECMO em choque refratário (uso crescente no Brasil), manejo cuidadoso de fluidos para evitar edema pulmonar. "
         "Mortalidade de 39-50% mesmo com suporte intensivo."),
    ],

    # ══════════════════════════════════════════════════════════════════
    # POLIOMIELITE
    # ══════════════════════════════════════════════════════════════════
    "Poliovirus (PV 1, 2, 3)": [
        (None, "Poliomielite (pólio)", None, None, "A", None, "SVS-POLIO", 2022,
         "Sem antiviral específico. A paralisia flácida é irreversível. "
         "Tratamento suportivo: fisioterapia respiratória e motora, ventilação mecânica em paralisia bulbar, "
         "reabilitação de longo prazo. "
         "PREVENÇÃO: vacinação (VOP oral + VIP inativada) é a única medida eficaz — "
         "Brasil livre de poliovírus selvagem desde 1994."),
    ],
}

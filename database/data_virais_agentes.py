"""
Dados de referência: fontes oficiais, vírus, antivirais e classes — dados virais.
Fontes: PCDT MS, SVS/MS GVS 5ª ed., SBI, SBMT, ANVISA, OPAS/PAHO adaptado ao Brasil.
"""

FONTES_VIRAIS = [
    # (sigla, nome, orgao, tipo, url, ano, descricao)
    # Apenas fontes que NÃO existem em data_fontes_bacterias_antibioticos.py
    ("PCDT-HIV", "Protocolo Clínico e Diretrizes Terapêuticas para Manejo da Infecção pelo HIV em Adultos", "Ministério da Saúde", "PCDT", "https://www.gov.br/saude/pt-br/centrais-de-conteudo/publicacoes/svsa/hiv-aids/pcdt-adultos-hiv-2022.pdf", 2022, "PCDT HIV/AIDS adultos MS 2022 — esquemas ARV, profilaxias, monitoramento"),
    ("PCDT-HIV-PED", "Protocolo Clínico e Diretrizes Terapêuticas para Manejo da Infecção pelo HIV em Crianças e Adolescentes", "Ministério da Saúde", "PCDT", "https://www.gov.br/saude/pt-br/centrais-de-conteudo/publicacoes/svsa/hiv-aids", 2022, "PCDT HIV/AIDS pediátrico e adolescentes MS 2022"),
    ("PCDT-HEPB", "Protocolo Clínico e Diretrizes Terapêuticas para Hepatite B e Coinfecções", "Ministério da Saúde", "PCDT", "https://www.gov.br/saude/pt-br/centrais-de-conteudo/publicacoes/svsa/hepatites-virais/pcdt-hepatite-b-2022.pdf", 2022, "PCDT Hepatite B MS 2022 — antivirais, critérios de tratamento, monitoramento"),
    ("PCDT-HEPC", "Protocolo Clínico e Diretrizes Terapêuticas para Hepatite C e Coinfecções", "Ministério da Saúde", "PCDT", "https://www.gov.br/saude/pt-br/centrais-de-conteudo/publicacoes/svsa/hepatites-virais/pcdt-hepatite-c-2022.pdf", 2022, "PCDT Hepatite C MS 2022 — DAAs pangenotípicos, critérios e metas"),
    ("SVS-DENGUE", "Guia de Vigilância em Saúde — Dengue, Zika e Chikungunya", "Ministério da Saúde / SVS", "Diretriz", "https://www.gov.br/saude/pt-br/centrais-de-conteudo/publicacoes/svsa/dengue", 2022, "GVS 5ª ed. capítulos Dengue, Zika e Chikungunya — manejo clínico e vigilância"),
    ("SVS-FEBAMARELA", "Guia de Vigilância em Saúde — Febre Amarela", "Ministério da Saúde / SVS", "Diretriz", "https://www.gov.br/saude/pt-br/centrais-de-conteudo/publicacoes/svsa/febre-amarela", 2022, "GVS 5ª ed. capítulo Febre Amarela — manejo, vacinação, vigilância entomológica"),
    ("SVS-RAIVA", "Guia de Vigilância em Saúde — Raiva", "Ministério da Saúde / SVS", "Diretriz", "https://www.gov.br/saude/pt-br/centrais-de-conteudo/publicacoes/svsa/raiva", 2022, "GVS 5ª ed. capítulo Raiva — profilaxia pós-exposição, esquemas vacinais"),
    ("SVS-HANTA", "Guia de Vigilância em Saúde — Hantavirose", "Ministério da Saúde / SVS", "Diretriz", "https://www.gov.br/saude/pt-br/centrais-de-conteudo/publicacoes/svsa/hantavirose", 2022, "GVS 5ª ed. capítulo Hantavirose — SCPH, manejo intensivo"),
    ("SVS-SARAMPO", "Guia de Vigilância em Saúde — Sarampo e Rubéola", "Ministério da Saúde / SVS", "Diretriz", "https://www.gov.br/saude/pt-br/centrais-de-conteudo/publicacoes/svsa/sarampo", 2022, "GVS 5ª ed. capítulos Sarampo e Rubéola — manejo, vacinação, controle de surtos"),
    ("SVS-VARICELA", "Guia de Vigilância em Saúde — Varicela e Herpes Zoster", "Ministério da Saúde / SVS", "Diretriz", "https://www.gov.br/saude/pt-br/centrais-de-conteudo/publicacoes/svsa/varicela", 2022, "GVS 5ª ed. capítulo Varicela/Herpes Zoster — aciclovir, imunoprofilaxia"),
    ("PCDT-INFLUENZA", "Protocolo de Tratamento da Influenza", "Ministério da Saúde / SVS", "PCDT", "https://www.gov.br/saude/pt-br/centrais-de-conteudo/publicacoes/svsa/influenza", 2022, "PCDT Influenza MS — oseltamivir, populações de risco, critérios de hospitalização"),
    ("PCDT-COVID19", "Protocolo de Manejo Clínico da COVID-19", "Ministério da Saúde", "PCDT", "https://www.gov.br/saude/pt-br/centrais-de-conteudo/publicacoes/svsa/covid-19", 2022, "PCDT COVID-19 MS — manejo ambulatorial e hospitalar, antivirais aprovados no Brasil"),
    ("SVS-HPV", "Guia de Vigilância em Saúde — HPV e Câncer do Colo do Útero", "Ministério da Saúde / SVS", "Diretriz", "https://www.gov.br/saude/pt-br/centrais-de-conteudo/publicacoes/svsa/hpv", 2022, "GVS 5ª ed. capítulo HPV — vacinação, rastreamento, manejo de lesões"),
    ("SBI-VIRAL", "Diretrizes de Infecções Virais — Sociedade Brasileira de Infectologia", "Sociedade Brasileira de Infectologia", "Diretriz", "https://www.infectologia.org.br", 2022, "Diretrizes SBI para infecções virais: HIV, hepatites, herpes, CMV, EBV"),
    ("SBMT-ARBOVIRUS", "Diretrizes de Arboviroses — Sociedade Brasileira de Medicina Tropical", "Sociedade Brasileira de Medicina Tropical", "Diretriz", "https://www.sbmt.org.br", 2022, "SBMT — dengue, zika, chikungunya, febre amarela: diagnóstico e manejo"),
    ("ANVISA-VIRAL", "Bulas e Notas Técnicas de Antivirais — ANVISA", "ANVISA", "Nota Técnica", "https://www.anvisa.gov.br/datavisa/fila_bula/index.asp", 2023, "Bulas ANVISA de antivirais registrados no Brasil e notas técnicas de segurança"),
    ("OPAS-BR", "Alertas Epidemiológicos e Guias Clínicos OPAS/OMS adaptados ao Brasil", "OPAS / OMS", "Diretriz", "https://www.paho.org/pt/brasil", 2022, "Guias OPAS para dengue, zika, febre amarela, sarampo e outras arboviroses — contexto Brasil"),
    ("SVS-HTLV", "Guia de Vigilância em Saúde — HTLV", "Ministério da Saúde / SVS", "Diretriz", "https://www.gov.br/saude/pt-br/centrais-de-conteudo/publicacoes/svsa/htlv", 2022, "GVS 5ª ed. capítulo HTLV — epidemiologia, diagnóstico, triagem bancos de sangue"),
    ("SVS-HEPAT-AE", "Guia de Vigilância em Saúde — Hepatites A e E", "Ministério da Saúde / SVS", "Diretriz", "https://www.gov.br/saude/pt-br/centrais-de-conteudo/publicacoes/svsa/hepatites-virais", 2022, "GVS 5ª ed. capítulos Hepatite A e E — manejo, vacinação, saneamento"),
    ("SVS-POLIO", "Guia de Vigilância em Saúde — Poliomielite", "Ministério da Saúde / SVS", "Diretriz", "https://www.gov.br/saude/pt-br/centrais-de-conteudo/publicacoes/svsa/poliomielite", 2022, "GVS 5ª ed. capítulo Poliomielite — vigilância, vacinação, resposta a surtos"),
]

FAMILIAS_VIRAIS = [
    # (nome, ordem_ou_grupo)
    ("Flaviviridae", "Amarilloviral"),
    ("Togaviridae", "Alphaviral"),
    ("Retroviridae", "Retroviral"),
    ("Herpesviridae", "Herpesviral"),
    ("Orthomyxoviridae", "Influenzaviral"),
    ("Coronaviridae", "Nidoviral"),
    ("Rhabdoviridae", "Mononegaviral"),
    ("Paramyxoviridae", "Mononegaviral"),
    ("Reoviridae", "Rotaviral"),
    ("Caliciviridae", "Caliciviral"),
    ("Adenoviridae", "Adenoviral"),
    ("Papillomaviridae", "Papilomaviral"),
    ("Hepadnaviridae", "Hepadnaviral"),
    ("Hantaviridae", "Hantaviral"),
    ("Deltavirus", "Subviral / satélite"),
    ("Hepeviridae", "Hepeviral"),
    ("Picornaviridae", "Picornaviral"),
    ("Pneumoviridae", "Pneumoviral"),
]

# (nome_cientifico, nome_comum, familia, tipo_acido_nucleico, envelope, transmissao_principal, reservatorio)
VIRUS = [
    # Arboviroses — Flaviviridae
    ("Dengue virus (DENV 1-4)", "Vírus da Dengue", "Flaviviridae", "RNA", "sim", "Picada de Aedes aegypti", "Humanos e primatas não humanos"),
    ("Zika virus (ZIKV)", "Vírus Zika", "Flaviviridae", "RNA", "sim", "Picada de Aedes aegypti; sexual; transplacentária", "Humanos e primatas não humanos"),
    ("Yellow fever virus (YFV)", "Vírus da Febre Amarela", "Flaviviridae", "RNA", "sim", "Picada de Aedes (urbana) ou Haemagogus/Sabethes (silvestre)", "Primatas não humanos (silvestre); humanos (urbano)"),
    ("West Nile virus (WNV)", "Vírus do Nilo Ocidental", "Flaviviridae", "RNA", "sim", "Picada de Culex spp.; transfusão; transplante", "Aves migratórias"),
    ("Hepatitis C virus (HCV)", "Vírus da Hepatite C", "Flaviviridae", "RNA", "sim", "Parenteral; sexual; vertical", "Humanos"),
    # Arboviroses — Togaviridae
    ("Chikungunya virus (CHIKV)", "Vírus Chikungunya", "Togaviridae", "RNA", "sim", "Picada de Aedes aegypti e Aedes albopictus", "Humanos e primatas"),
    # Retrovírus
    ("Human immunodeficiency virus 1/2 (HIV-1/2)", "Vírus da Imunodeficiência Humana", "Retroviridae", "RNA", "sim", "Sexual; parenteral; vertical (transplacentária/leite)", "Humanos"),
    ("Human T-lymphotropic virus 1 (HTLV-1)", "Vírus Linfotrópico de Células T Humanas tipo 1", "Retroviridae", "RNA", "sim", "Sexual; parenteral; vertical (leite materno)", "Humanos"),
    ("Human T-lymphotropic virus 2 (HTLV-2)", "Vírus Linfotrópico de Células T Humanas tipo 2", "Retroviridae", "RNA", "sim", "Sexual; parenteral; vertical", "Humanos e primatas"),
    # Herpesviridae
    ("Herpes simplex virus 1 (HSV-1)", "Herpes Simples tipo 1", "Herpesviridae", "DNA", "sim", "Contato direto com lesão ou saliva; vertical", "Humanos"),
    ("Herpes simplex virus 2 (HSV-2)", "Herpes Simples tipo 2", "Herpesviridae", "DNA", "sim", "Sexual; contato direto; vertical intraparto", "Humanos"),
    ("Varicella-zoster virus (VZV)", "Vírus Varicela-Zoster", "Herpesviridae", "DNA", "sim", "Respiratória; contato com lesões cutâneas; vertical", "Humanos"),
    ("Cytomegalovirus (CMV)", "Citomegalovírus", "Herpesviridae", "DNA", "sim", "Contato com saliva/urina/sangue; vertical; transplante; sexual", "Humanos"),
    ("Epstein-Barr virus (EBV)", "Vírus Epstein-Barr", "Herpesviridae", "DNA", "sim", "Contato com saliva (doença do beijo); transfusão; transplante", "Humanos"),
    ("Human herpesvirus 8 (HHV-8)", "Vírus do Sarcoma de Kaposi", "Herpesviridae", "DNA", "sim", "Sexual; saliva; transplante", "Humanos"),
    # Orthomyxoviridae
    ("Influenza virus A/B/C", "Vírus Influenza", "Orthomyxoviridae", "RNA", "sim", "Respiratória (gotículas e aerossóis); contato com fômites", "Humanos, aves, suínos"),
    # Coronaviridae
    ("SARS-CoV-2", "Coronavírus SARS-CoV-2 (COVID-19)", "Coronaviridae", "RNA", "sim", "Respiratória (aerossóis e gotículas); contato com superfícies contaminadas", "Humanos (morcegos como provável reservatório ancestral)"),
    # Rhabdoviridae
    ("Rabies lyssavirus", "Vírus da Raiva", "Rhabdoviridae", "RNA", "sim", "Mordedura/arranhadura de animal infectado; mucosa; transplante", "Cães (urbano); morcegos e raposas (silvestre)"),
    # Paramyxoviridae
    ("Measles morbillivirus", "Vírus do Sarampo", "Paramyxoviridae", "RNA", "sim", "Respiratória (aerossóis de longo alcance); contato direto", "Humanos"),
    ("Rubella virus", "Vírus da Rubéola", "Togaviridae", "RNA", "sim", "Respiratória; vertical (rubéola congênita)", "Humanos"),
    ("Mumps orthorubulavirus", "Vírus da Caxumba / Parotidite Epidêmica", "Paramyxoviridae", "RNA", "sim", "Respiratória; contato com saliva", "Humanos"),
    ("Human respiratory syncytial virus (RSV)", "Vírus Sincicial Respiratório", "Pneumoviridae", "RNA", "sim", "Respiratória (gotículas); contato com fômites", "Humanos"),
    ("Henipavirus spp.", "Henipaviridae respiratórios emergentes", "Paramyxoviridae", "RNA", "sim", "Contato com morcegos; transmissão humano-a-humano limitada", "Morcegos da ordem Chiroptera"),
    # Reoviridae
    ("Rotavirus A", "Rotavírus A", "Reoviridae", "RNA", "nao", "Fecal-oral; fômites", "Humanos"),
    # Caliciviridae
    ("Norovirus (GI/GII)", "Norovírus", "Caliciviridae", "RNA", "nao", "Fecal-oral; alimentos e água; aerossol de vômito", "Humanos"),
    # Adenoviridae
    ("Human adenovirus (HAdV)", "Adenovírus Humano", "Adenoviridae", "DNA", "nao", "Respiratória; fecal-oral; conjuntival; fômites", "Humanos"),
    # Papillomaviridae
    ("Human papillomavirus (HPV)", "Papilomavírus Humano", "Papillomaviridae", "DNA", "nao", "Sexual; contato com mucosas/pele; vertical intraparto", "Humanos"),
    # Hepadnaviridae
    ("Hepatitis B virus (HBV)", "Vírus da Hepatite B", "Hepadnaviridae", "DNA", "sim", "Parenteral; sexual; vertical (perinatal)", "Humanos"),
    # Hantaviridae
    ("Hantavirus (Araraquara, Juquitiba, Laguna Negra)", "Hantavírus brasileiro", "Hantaviridae", "RNA", "nao", "Inalação de aerossóis de excretas de roedores", "Roedores silvestres (Oligoryzomys nigripes, Necromys lasiurus)"),
    # Deltavirus
    ("Hepatitis D virus (HDV)", "Vírus da Hepatite D (Delta)", "Deltavirus", "RNA", "sim", "Parenteral; sexual; vertical — requer coinfecção ou superinfecção por HBV", "Humanos (satélite do HBV)"),
    # Hepeviridae
    ("Hepatitis E virus (HEV)", "Vírus da Hepatite E", "Hepeviridae", "RNA", "nao", "Fecal-oral; carne de porco/javali mal cozida; zoonótica", "Humanos, suínos, javalis"),
    # Picornaviridae
    ("Hepatitis A virus (HAV)", "Vírus da Hepatite A", "Picornaviridae", "RNA", "nao", "Fecal-oral; alimentos e água contaminados", "Humanos"),
    ("Poliovirus (PV 1, 2, 3)", "Poliovírus", "Picornaviridae", "RNA", "nao", "Fecal-oral; raramente respiratória", "Humanos"),
    ("Enterovirus 71 (EV-A71)", "Enterovírus 71 (Mão-Pé-Boca)", "Picornaviridae", "RNA", "nao", "Fecal-oral; contato com secreções; respiratória", "Humanos"),
    ("Coxsackievirus A16 (CVA16)", "Coxsackievírus A16 (Mão-Pé-Boca)", "Picornaviridae", "RNA", "nao", "Fecal-oral; contato com vesículas", "Humanos"),
]

CLASSES_ANTIVIRAIS = [
    # (nome, mecanismo_acao, alvo_viral)
    ("Inibidores de Nucleosídeo/Nucleotídeo (análogos)", "Inibição da polimerase viral por incorporação de análogos nucleotídicos terminadores de cadeia", "Polimerase viral (DNA ou RNA-dependente)"),
    ("Inibidores Não-Nucleosídicos de Polimerase (INNTR)", "Ligação alostérica à polimerase reversa — induz mudança conformacional e inibição", "Transcriptase reversa do HIV (sítio alostérico)"),
    ("Inibidores de Protease Viral (IP)", "Inibição competitiva da protease viral essencial para maturação dos vírions", "Protease viral (HIV, HCV, influenza)"),
    ("Inibidores de Integrase (INSTI)", "Bloqueio da integração do DNA viral proviral ao cromossomo do hospedeiro", "Integrase do HIV"),
    ("Inibidores de Entrada e Fusão", "Bloqueio da ligação ao receptor celular ou da fusão da membrana viral com a célula hospedeira", "Glicoproteína viral (gp120/gp41 do HIV; proteína S do SARS-CoV-2)"),
    ("Inibidores de Neuraminidase", "Inibição da neuraminidase viral — impede liberação de vírions e disseminação celular a celular", "Neuraminidase dos vírus Influenza A e B"),
    ("Inibidores da Cápside Viral", "Inibição da montagem ou desmontagem da cápside viral", "Proteína CA da cápside do HIV-1"),
    ("Antagonistas do Receptor CCR5", "Bloqueio do co-receptor CCR5 na célula hospedeira — impede entrada do HIV R5-trópico", "CCR5 (co-receptor do HIV no hospedeiro)"),
    ("Inibidores da RNA Polimerase Dependente de RNA (RdRp)", "Análogo nucleotídico que inibe a RdRp viral — interrompe replicação do RNA viral", "RdRp viral (Coronavírus, Influenza, VRS, HCV)"),
    ("Imunomoduladores Antivirais", "Estimulação da resposta imune inata (interferon) ou modulação de citocinas antivirais", "Sistema imune inato do hospedeiro (não alvo viral direto)"),
    ("Inibidores da Protease do HCV (NS3/4A)", "Inibição da protease NS3/4A do HCV essencial para clivagem da poliproteína viral", "Protease NS3/4A do vírus da Hepatite C"),
    ("Inibidores do NS5A do HCV", "Bloqueio da proteína NS5A — inibe montagem, replicação e secreção do HCV", "NS5A do vírus da Hepatite C"),
    ("Inibidores do NS5B do HCV (análogos nucleosídicos)", "Inibição da RNA polimerase NS5B do HCV por terminação de cadeia", "NS5B (RdRp) do vírus da Hepatite C"),
    ("Inibidores da Protease da Ribavirina", "Análogo de guanosina — inibição múltipla da síntese de RNA viral; mutagênico", "RNA polimerase viral (múltiplos vírus)"),
    ("Anticorpos Monoclonais Antivirais", "Neutralização direta de proteínas virais de superfície ou bloqueio de receptores do hospedeiro", "Proteínas de superfície viral específicas"),
    ("Inibidores de Hemaglutinina (Influenza)", "Bloqueio da hemaglutinina viral — impede ligação ao ácido siálico celular", "Hemaglutinina do Influenza A"),
]

# (nome_generico, nome_comercial_ou_None, classe_nome, via, disponivel_sus, anvisa_registrado, obs)
ANTIVIRAIS = [
    # ══════════════════════════════════════════════════════════════════
    # ANTIVIRAIS PARA HIV — ARVs
    # ══════════════════════════════════════════════════════════════════
    # Inibidores de Transcriptase Reversa Análogos de Nucleosídeo (ITRN)
    ("Tenofovir disoproxila (TDF)", "Viread", "Inibidores de Nucleosídeo/Nucleotídeo (análogos)", "oral", True, True, "ITRN; backbone do esquema preferencial de 1ª linha HIV/AIDS no Brasil; também ativo contra HBV"),
    ("Tenofovir alafenamida (TAF)", "Vemlidy", "Inibidores de Nucleosídeo/Nucleotídeo (análogos)", "oral", False, True, "ITRN; menor nefrotoxicidade e toxicidade óssea que TDF; aprovado HIV e HBV"),
    ("Lamivudina (3TC)", "Epivir", "Inibidores de Nucleosídeo/Nucleotídeo (análogos)", "oral", True, True, "ITRN; componente universal dos esquemas ARV no SUS; ativo contra HBV"),
    ("Emtricitabina (FTC)", "Emtriva", "Inibidores de Nucleosídeo/Nucleotídeo (análogos)", "oral", False, True, "ITRN; análogo da 3TC com maior meia-vida; usado em formulações coformuladas"),
    ("Abacavir (ABC)", "Ziagen", "Inibidores de Nucleosídeo/Nucleotídeo (análogos)", "oral", True, True, "ITRN; testar HLA-B*57:01 antes de usar — risco de hipersensibilidade grave"),
    ("Zidovudina (AZT)", "Retrovir", "Inibidores de Nucleosídeo/Nucleotídeo (análogos)", "oral/iv", True, True, "ITRN histórico; profilaxia de transmissão vertical e PEP; mielotoxicidade dose-limitante"),
    # INNTR
    ("Efavirenz (EFZ)", "Sustiva / Stocrin", "Inibidores Não-Nucleosídicos de Polimerase (INNTR)", "oral", True, True, "INNTR; esquema histórico 1ª linha no SUS até substituição pelo DTG; 600 mg/noite"),
    ("Nevirapina (NVP)", "Viramune", "Inibidores Não-Nucleosídicos de Polimerase (INNTR)", "oral", True, True, "INNTR; profilaxia vertical dose única; risco hepatotoxicidade em CD4 elevado"),
    ("Rilpivirina (RPV)", "Edurant", "Inibidores Não-Nucleosídicos de Polimerase (INNTR)", "oral", False, True, "INNTR de 2ª geração; carga viral < 100.000 cópias/mL; tomar com refeição"),
    ("Doravirina (DOR)", "Pifeltro", "Inibidores Não-Nucleosídicos de Polimerase (INNTR)", "oral", False, True, "INNTR de 3ª geração; sem restrição alimentar; menor interação com rifampicina"),
    # Inibidores de Protease (IP)
    ("Lopinavir/ritonavir (LPV/r)", "Kaletra", "Inibidores de Protease Viral (IP)", "oral", True, True, "IP; esquema preferencial pediátrico e 2ª linha adultos no SUS; ritonavir é potenciador"),
    ("Atazanavir/ritonavir (ATV/r)", "Reyataz", "Inibidores de Protease Viral (IP)", "oral", True, True, "IP; 1 cápsula/dia; hiperbilirrubinemia indireta benigna frequente"),
    ("Darunavir/ritonavir ou cobicistate (DRV/r ou DRV/c)", "Prezista", "Inibidores de Protease Viral (IP)", "oral", False, True, "IP de alta barreira genética; HIV multirresistente; alta eficácia com boosting"),
    # Inibidores de Integrase (INSTI)
    ("Dolutegravir (DTG)", "Tivicay", "Inibidores de Integrase (INSTI)", "oral", True, True, "INSTI de 2ª geração; esquema preferencial 1ª linha SUS (TLD = TDF+3TC+DTG); alta barreira"),
    ("Raltegravir (RAL)", "Isentress", "Inibidores de Integrase (INSTI)", "oral", True, True, "INSTI 1ª geração; esquema pediátrico SUS; 2 doses/dia"),
    ("Bictegravir (BIC)", "Biktarvy (coformulado BIC/TAF/FTC)", "Inibidores de Integrase (INSTI)", "oral", False, True, "INSTI de 2ª geração; coformulado com TAF/FTC; 1 cp/dia; excelente tolerabilidade"),
    ("Cabotegravir (CAB)", "Apretude (PrEP); Cabenuva (ARV)", "Inibidores de Integrase (INSTI)", "im", False, True, "INSTI injetável de ação prolongada; PrEP e tratamento; injeção mensal/bimestral"),
    # Inibidores de Entrada/Fusão
    ("Maraviroque (MVC)", "Selzentry", "Antagonistas do Receptor CCR5", "oral", False, True, "Bloqueador de CCR5; apenas cepas R5-trópicas (teste de tropismo obrigatório)"),
    ("Enfuvirtida (T-20)", "Fuzeon", "Inibidores de Entrada e Fusão", "sc", False, True, "Inibidor de fusão; HIV multirresistente; injeção SC 2x/dia; alto custo"),
    # Inibidores da Cápside
    ("Lenacapavir (LEN)", "Sunlenca", "Inibidores da Cápside Viral", "sc/oral", False, True, "Inibidor de cápside; injeção SC a cada 6 meses; HIV extensivamente resistente"),

    # ══════════════════════════════════════════════════════════════════
    # ANTIVIRAIS PARA HEPATITE B
    # ══════════════════════════════════════════════════════════════════
    ("Entecavir (ETV)", "Baraclude", "Inibidores de Nucleosídeo/Nucleotídeo (análogos)", "oral", True, True, "HBV — 1ª linha SUS; alta barreira genética; 0,5 mg/dia (1 mg/dia em refratários)"),
    ("Tenofovir disoproxila (TDF)", "Viread", "Inibidores de Nucleosídeo/Nucleotídeo (análogos)", "oral", True, True, "HBV — 1ª linha SUS; ativo contra HBV e HIV; também usado em coinfectados HIV/HBV"),
    ("Tenofovir alafenamida (TAF)", "Vemlidy", "Inibidores de Nucleosídeo/Nucleotídeo (análogos)", "oral", False, True, "HBV — menor toxicidade renal e óssea que TDF; opção em insuficiência renal leve"),
    ("Interferon alfa-2a peguilado (Peg-IFN-α2a)", "Pegasys", "Imunomoduladores Antivirais", "sc", True, True, "HBV e HCV — estímulo imune inato; soroconversão HBeAg/HBsAg; efeitos adversos limitam uso"),

    # ══════════════════════════════════════════════════════════════════
    # ANTIVIRAIS PARA HEPATITE C (DAAs)
    # ══════════════════════════════════════════════════════════════════
    ("Sofosbuvir (SOF)", "Sovaldi", "Inibidores do NS5B do HCV (análogos nucleosídicos)", "oral", True, True, "HCV — backbone pangenotípico; combinar com NS5A ou NS3 inibidor; 400 mg/dia"),
    ("Sofosbuvir/Velpatasvir (SOF/VEL)", "Epclusa", "Inibidores do NS5B do HCV (análogos nucleosídicos)", "oral", True, True, "HCV genótipos 1-6 — pangenotípico; 1ª linha SUS para genótipos não 1; 12 semanas"),
    ("Sofosbuvir/Ledipasvir (SOF/LED)", "Harvoni", "Inibidores do NS5B do HCV (análogos nucleosídicos)", "oral", True, True, "HCV genótipos 1 e 4 — padrão-ouro genótipo 1; 8-12 semanas; sem RBV na maioria"),
    ("Glecaprevir/Pibrentasvir (GLE/PIB)", "Maviret", "Inibidores da Protease do HCV (NS3/4A)", "oral", True, True, "HCV pangenotípico — 8 semanas sem cirrose; 12 semanas com cirrose compensada; alto índice de cura"),
    ("Daclatasvir (DCV)", "Daklinza", "Inibidores do NS5A do HCV", "oral", True, True, "HCV — inibidor NS5A; usado com sofosbuvir no esquema SUS (genótipos 1, 3); 60 mg/dia"),
    ("Ribavirina (RBV)", "Rebetol / Ribavirina genérica", "Inibidores da Protease da Ribavirina", "oral", True, True, "HCV — adjuvante em situações especiais (genótipo 3 com cirrose, falha prévia); anemia dose-limitante"),

    # ══════════════════════════════════════════════════════════════════
    # ANTIVIRAIS PARA INFLUENZA
    # ══════════════════════════════════════════════════════════════════
    ("Oseltamivir (OST)", "Tamiflu", "Inibidores de Neuraminidase", "oral", True, True, "Influenza A e B — 1ª linha SUS; iniciar em ≤ 48h dos sintomas; populações de risco"),
    ("Zanamivir", "Relenza", "Inibidores de Neuraminidase", "inalatória", False, True, "Influenza A e B — alternativa inalatória; usar em resistência ao oseltamivir (H275Y)"),
    ("Baloxavir marboxil", "Xofluza", "Inibidores de Hemaglutinina (Influenza)", "oral", False, True, "Influenza A e B — dose única; inibidor de endonuclease PA; aprovado ANVISA 2023"),

    # ══════════════════════════════════════════════════════════════════
    # ANTIVIRAIS PARA COVID-19
    # ══════════════════════════════════════════════════════════════════
    ("Nirmatrelvir/Ritonavir (NMV/r)", "Paxlovid", "Inibidores de Protease Viral (IP)", "oral", False, True, "SARS-CoV-2 — redução de 89% hospitalização/morte se iniciado ≤ 5 dias; alto risco de interações"),
    ("Remdesivir (RDV)", "Veklury", "Inibidores da RNA Polimerase Dependente de RNA (RdRp)", "iv", False, True, "SARS-CoV-2 — uso hospitalar; reduz tempo de hospitalização; inibidor de RdRp"),
    ("Molnupiravir", "Lagevrio", "Inibidores da RNA Polimerase Dependente de RNA (RdRp)", "oral", False, True, "SARS-CoV-2 — uso ambulatorial em alto risco; mutagênico — contraindicado na gravidez"),

    # ══════════════════════════════════════════════════════════════════
    # ANTIVIRAIS PARA HERPES / VZV / CMV / EBV
    # ══════════════════════════════════════════════════════════════════
    ("Aciclovir (ACV)", "Zovirax", "Inibidores de Nucleosídeo/Nucleotídeo (análogos)", "oral/iv/tópico", True, True, "HSV-1, HSV-2, VZV — 1ª linha SUS; herpes simples, varicela, herpes zoster, encefalite herpética"),
    ("Valaciclovir (VACV)", "Valtrex", "Inibidores de Nucleosídeo/Nucleotídeo (análogos)", "oral", False, True, "Pró-fármaco do aciclovir — maior biodisponibilidade oral; HSV e VZV; posologia mais conveniente"),
    ("Ganciclovir (GCV)", "Cymevene", "Inibidores de Nucleosídeo/Nucleotídeo (análogos)", "iv", True, True, "CMV — tratamento de doença por CMV em imunossuprimidos; requer monitoramento hematológico"),
    ("Valganciclovir (VGCV)", "Valcyte", "Inibidores de Nucleosídeo/Nucleotídeo (análogos)", "oral", True, True, "CMV — pró-fármaco do ganciclovir; profilaxia e tratamento de CMV em transplantados; SUS em transplante"),
    ("Foscarnet (PFA)", "Foscavir", "Inibidores de Nucleosídeo/Nucleotídeo (análogos)", "iv", True, True, "CMV e HSV resistente ao aciclovir/ganciclovir; nefrotoxicidade limitante; quelante de Ca²⁺"),
    ("Cidofovir (CDV)", "Vistide", "Inibidores de Nucleosídeo/Nucleotídeo (análogos)", "iv", False, True, "CMV resistente ao ganciclovir; administração 1x/semana; alta nefrotoxicidade"),

    # ══════════════════════════════════════════════════════════════════
    # ANTIVIRAIS PARA HEPATITES A e E — sem tratamento antiviral específico
    # ══════════════════════════════════════════════════════════════════
    # Não existem antivirais específicos aprovados para HAV e HEV — tratamento suportivo

    # ══════════════════════════════════════════════════════════════════
    # ANTIVIRAIS PARA DENGUE / ZIKA / CHIKUNGUNYA / FEBRE AMARELA
    # ══════════════════════════════════════════════════════════════════
    # Não existem antivirais específicos aprovados no Brasil para arboviroses
    # Tratamento é suportivo; pesquisas em andamento (dengue: JNJ-64281802; ivermectina sem evidência)

    # ══════════════════════════════════════════════════════════════════
    # IMUNOMODULADORES / INTERFERONS
    # ══════════════════════════════════════════════════════════════════
    ("Interferon alfa-2b peguilado (Peg-IFN-α2b)", "PegIntron", "Imunomoduladores Antivirais", "sc", True, True, "HCV genótipo 1 (em desuso com DAAs disponíveis); HBV; melanoma adjuvante"),
    ("Interferon beta-1a (IFN-β1a)", "Rebif / Avonex", "Imunomoduladores Antivirais", "sc/im", False, True, "Esclerose múltipla; uso off-label histórico em infecções virais graves — sem evidência robusta"),
]

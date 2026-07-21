"""
Dados de referência: fontes oficiais, fungos, antifúngicos e classes — dados fúngicos.
Fontes: PCDT MS (Paracoccidioidomicose 2022), SBD, SBMT, SBI, ANVISA notas técnicas antifúngicos,
        GVS/MS 5ª ed. 2022, PCDT-HIV (para PCP e criptococose em AIDS).

Nota: Siglas de fontes que NÃO existem em data_fontes_bacterias_antibioticos.py nem em data_virais_agentes.py.
"""

FONTES_FUNGICAS = [
    # (sigla, nome, orgao, tipo, url, ano, descricao)
    ("PCDT-PARACOC", "Protocolo Clínico e Diretrizes Terapêuticas da Paracoccidioidomicose",
     "Ministério da Saúde", "PCDT",
     "https://www.gov.br/saude/pt-br/centrais-de-conteudo/publicacoes/svsa/doencas-tropicais/paracoccidioidomicose",
     2022, "PCDT Paracoccidioidomicose MS 2022 — itraconazol, sulfadiazina, anfotericina B, duração do tratamento"),

    ("SBD-MICOSES", "Diretrizes Brasileiras para Diagnóstico e Tratamento das Micoses Cutâneas",
     "Sociedade Brasileira de Dermatologia", "Diretriz",
     "https://www.sbd.org.br/dermatologia/doencas-e-tratamentos/micoses/",
     2022, "SBD — dermatofitoses, onicomicose, pitiríase versicolor, esporotricose, cromoblastomicose, micetoma fúngico"),

    ("SBMT-FUNGOS", "Diretrizes para Micoses Sistêmicas e Tropicais — Sociedade Brasileira de Medicina Tropical",
     "Sociedade Brasileira de Medicina Tropical", "Diretriz",
     "https://www.sbmt.org.br",
     2022, "SBMT — paracoccidioidomicose, histoplasmose, lobomicose, esporotricose: diagnóstico e tratamento no Brasil"),

    ("SBI-CAND", "Diretrizes Brasileiras para Diagnóstico e Tratamento de Candidíase Invasiva",
     "Sociedade Brasileira de Infectologia", "Diretriz",
     "https://www.infectologia.org.br",
     2022, "SBI — candidemia, candidíase invasiva, Candida auris: antifúngicos, profilaxia, manejo em UTI"),

    ("SBI-ASPERG", "Diretrizes Brasileiras para Aspergilose Invasiva e ABPA",
     "Sociedade Brasileira de Infectologia", "Diretriz",
     "https://www.infectologia.org.br",
     2021, "SBI — aspergilose invasiva em imunossuprimidos, ABPA em asmaticos/fibrocísticos: diagnóstico e tratamento"),

    ("SBI-CRIPTO", "Diretrizes Brasileiras para Criptococose",
     "Sociedade Brasileira de Infectologia", "Diretriz",
     "https://www.infectologia.org.br",
     2022, "SBI — criptococose meníngea e pulmonar em HIV e não-HIV: indução, consolidação e manutenção"),

    ("ANVISA-ANTIF", "Notas Técnicas e Bulas de Antifúngicos — ANVISA",
     "ANVISA", "Nota Técnica",
     "https://www.anvisa.gov.br/datavisa/fila_bula/index.asp",
     2023, "ANVISA — bulas de antifúngicos registrados no Brasil: fluconazol, itraconazol, voriconazol, caspofungina, anfotericina B"),

    ("PCDT-HIV-FUNG", "Protocolo Clínico e Diretrizes Terapêuticas para Manejo das Infecções Fúngicas em PVHIV",
     "Ministério da Saúde", "PCDT",
     "https://www.gov.br/saude/pt-br/centrais-de-conteudo/publicacoes/svsa/hiv-aids",
     2022, "PCDT HIV/AIDS — seções de PCP (Pneumocystis jirovecii) e criptococose em PVHIV; profilaxias primária e secundária"),

    ("SVS-HISTOP", "Guia de Vigilância em Saúde — Histoplasmose",
     "Ministério da Saúde / SVS", "Diretriz",
     "https://www.gov.br/saude/pt-br/centrais-de-conteudo/publicacoes/svsa/vigilancia",
     2022, "GVS 5ª ed. — capítulo Histoplasmose: epidemiologia, diagnóstico, tratamento no Brasil"),

    ("SVS-ESPORO", "Guia de Vigilância em Saúde — Esporotricose",
     "Ministério da Saúde / SVS", "Diretriz",
     "https://www.gov.br/saude/pt-br/centrais-de-conteudo/publicacoes/svsa/vigilancia",
     2022, "GVS 5ª ed. — capítulo Esporotricose: endemia do Rio de Janeiro, Sporothrix brasiliensis, itraconazol"),

    ("SVS-CRIPTO", "Guia de Vigilância em Saúde — Criptococose",
     "Ministério da Saúde / SVS", "Diretriz",
     "https://www.gov.br/saude/pt-br/centrais-de-conteudo/publicacoes/svsa/vigilancia",
     2022, "GVS 5ª ed. — capítulo Criptococose: C. neoformans e C. gattii, manejo da meningite criptocócica"),
]

FAMILIAS_FUNGICAS = [
    # (nome, grupo)
    ("Ajellomycetaceae", "Ascomycota — Onygenales"),
    ("Nectriaceae", "Ascomycota — Hypocreales"),
    ("Phaffomycetaceae", "Ascomycota — Saccharomycetales"),
    ("Cryptococcaceae", "Basidiomycota — Tremellales"),
    ("Aspergillaceae", "Ascomycota — Eurotiales"),
    ("Mucoraceae", "Mucoromycota — Mucorales"),
    ("Cunninghamellaceae", "Mucoromycota — Mucorales"),
    ("Mortierellaceae", "Mucoromycota — Mucorales"),
    ("Rhizopodaceae", "Mucoromycota — Mucorales"),
    ("Scedosporiaceae", "Ascomycota — Microascales"),
    ("Sporothricaceae", "Ascomycota — Ophiostomatales"),
    ("Herpotrichiellaceae", "Ascomycota — Chaetothyriales"),
    ("Neodevriesiaceae", "Ascomycota — Chaetothyriales"),
    ("Phialophora-family", "Ascomycota — Chaetothyriales"),
    ("Trimorphomycetaceae", "Basidiomycota — Trichosporonales"),
    ("Debaryomycetaceae", "Ascomycota — Saccharomycetales"),
    ("Pneumocystidaceae", "Ascomycota — Pneumocystidales"),
    ("Lomentosporaceae", "Ascomycota — Microascales"),
    ("Cordycipitaceae", "Ascomycota — Hypocreales"),
]

# (nome_cientifico, nome_comum, familia_nome, tipo, transmissao_principal, reservatorio, distribuicao_br)
FUNGOS = [
    ("Paracoccidioides brasiliensis",
     "Fungo da paracoccidioidomicose",
     "Ajellomycetaceae", "dimórfico",
     "Inalação de conídios do solo",
     "Solo úmido de áreas rurais tropicais e subtropicais",
     "Endêmico; maior incidência em SP, MG, PR, MT, GO, MS; regiões Centro-Oeste, Sul e Sudeste"),

    ("Paracoccidioides lutzii",
     "Fungo da paracoccidioidomicose (forma Lutzii)",
     "Ajellomycetaceae", "dimórfico",
     "Inalação de conídios do solo",
     "Solo de áreas rurais da Amazônia e Centro-Oeste",
     "Predominante na região Amazônica e Centro-Oeste do Brasil"),

    ("Histoplasma capsulatum",
     "Fungo da histoplasmose",
     "Ajellomycetaceae", "dimórfico",
     "Inalação de microconídios em locais com excremento de aves e morcegos",
     "Solo enriquecido com excrementos de aves e morcegos (grutas, galinheiros, árvores ocas)",
     "Distribuição ampla no Brasil; surtos em grutas e demolições; endêmico em todo o território"),

    ("Cryptococcus neoformans",
     "Criptococo (sorotipo A/D)",
     "Cryptococcaceae", "levedura",
     "Inalação de células leveduriformes ou esporos do ambiente",
     "Excrementos de pombos e outras aves; solo; madeira apodrecida",
     "Distribuição nacional; principal causa de meningite fúngica em HIV no Brasil"),

    ("Cryptococcus gattii",
     "Criptococo gattii",
     "Cryptococcaceae", "levedura",
     "Inalação de esporos de árvores (principalmente eucalipto e oiti)",
     "Árvores: Eucalyptus spp., Schizolobium parahyba, Plumeria sp.",
     "Regiões Norte, Nordeste e Sul; casos em imunocompetentes; mais virulento que C. neoformans"),

    ("Candida albicans",
     "Cândida (espécie mais comum)",
     "Debaryomycetaceae", "levedura",
     "Endógena (microbiota normal); transmissão em neonatos durante o parto",
     "Microbiota normal de mucosas oral, gastrointestinal e vaginal de humanos",
     "Distribuição nacional; responsável por 40-60% das candidemias hospitalares no Brasil"),

    ("Candida tropicalis",
     "Cândida tropical",
     "Debaryomycetaceae", "levedura",
     "Endógena ou exógena hospitalar; transmissão por fômites e mãos de profissionais de saúde",
     "Microbiota de mucosas e trato gastrointestinal de humanos",
     "Segunda espécie mais frequente de candidemia no Brasil (20-30%); maior resistência ao fluconazol"),

    ("Candida glabrata",
     "Cândida glabrata",
     "Phaffomycetaceae", "levedura",
     "Endógena; maior prevalência em pacientes idosos e previamente expostos a azólicos",
     "Microbiota de mucosas de humanos",
     "Terceira causa de candidemia no Brasil; resistência intrínseca reduzida ao fluconazol"),

    ("Candida parapsilosis",
     "Cândida parapsilosis",
     "Debaryomycetaceae", "levedura",
     "Transmissão exógena por mãos de profissionais de saúde e superfícies",
     "Mãos de profissionais de saúde; cateteres vasculares; superfícies hospitalares",
     "Importante em neonatos e UTI pediátrica; frequente em candidemia relacionada a cateter"),

    ("Candida auris",
     "Cândida auris (emergente multirresistente)",
     "Debaryomycetaceae", "levedura",
     "Transmissão horizontal em ambiente hospitalar; persistência em superfícies",
     "Ambiente hospitalar; pele de pacientes colonizados",
     "Emergente no Brasil desde 2018; notificações em hospitais terciários de SP, RJ, RS"),

    ("Aspergillus fumigatus",
     "Aspergilho fumigado",
     "Aspergillaceae", "fungo_filamentoso",
     "Inalação de conídios ubíquos no ambiente",
     "Solo, compostagens, material vegetal em decomposição, sistemas de ar-condicionado",
     "Distribuição nacional; principal agente de aspergilose invasiva em imunossuprimidos no Brasil"),

    ("Aspergillus flavus",
     "Aspergilho flavus",
     "Aspergillaceae", "fungo_filamentoso",
     "Inalação de conídios; contaminação de alimentos",
     "Solo, grãos (milho, amendoim), material vegetal",
     "Segundo agente de aspergilose invasiva; produz aflatoxinas; trópicos e semitropicos"),

    ("Aspergillus niger",
     "Aspergilho niger",
     "Aspergillaceae", "fungo_filamentoso",
     "Inalação de conídios",
     "Solo, vegetais, grãos armazenados",
     "Aspergilose do ouvido externo (otomicose); aspergiloma pulmonar; distribuição nacional"),

    ("Rhizopus arrhizus",
     "Rizopus (agente de mucormicose)",
     "Mucoraceae", "fungo_filamentoso",
     "Inalação de esporos ou inoculação traumática; ingestão",
     "Solo, material vegetal em decomposição, frutas, pão velho",
     "Distribuição nacional; agente mais comum de mucormicose no Brasil"),

    ("Mucor irregularis",
     "Mucor (agente de mucormicose)",
     "Mucoraceae", "fungo_filamentoso",
     "Inalação de esporos ou inoculação traumática",
     "Solo, matéria orgânica em decomposição",
     "Mucormicose rinocerebral e pulmonar em diabéticos e imunossuprimidos"),

    ("Cunninghamella bertholletiae",
     "Cunninghamella",
     "Cunninghamellaceae", "fungo_filamentoso",
     "Inalação de esporos",
     "Solo, matéria orgânica",
     "Rara; mucormicose disseminada de alta mortalidade; imunossuprimidos graves"),

    ("Sporothrix schenckii",
     "Esporotrix (esporotricose clássica)",
     "Sporothricaceae", "dimórfico",
     "Inoculação traumática com espinhos, plantas, palha; transmissão zoonótica por gatos",
     "Solo, vegetação em decomposição, penas, palha; gatos domésticos (endemia felina RJ)",
     "Distribuição nacional; endemia no Rio de Janeiro (maior foco do mundo) e RS, MG"),

    ("Sporothrix brasiliensis",
     "Esporotrix brasiliensis (endêmico do Brasil)",
     "Sporothricaceae", "dimórfico",
     "Transmissão zoonótica por gatos (arranhadura, mordida); inoculação traumática",
     "Gatos domésticos e errantes no Brasil; solo",
     "Espécie endêmica do Brasil; principal agente da endemia felina do Rio de Janeiro; mais virulento que S. schenckii"),

    ("Fonsecaea pedrosoi",
     "Fonsecaea (cromoblastomicose)",
     "Herpotrichiellaceae", "dimórfico",
     "Inoculação traumática com material vegetal (farpas, espinhos, palha)",
     "Solo, madeira apodrecida, vegetação em decomposição",
     "Distribuição nacional; maior prevalência em regiões Norte e Nordeste; trabalhadores rurais"),

    ("Cladophialophora carrionii",
     "Cladofialofora (cromoblastomicose árida)",
     "Herpotrichiellaceae", "dimórfico",
     "Inoculação traumática com cactos, material vegetal seco",
     "Solo de regiões semiáridas; cactos",
     "Nordeste do Brasil; áreas semiáridas; segunda espécie mais comum de cromoblastomicose no BR"),

    ("Madurella mycetomatis",
     "Madurela (micetoma eumicético)",
     "Neodevriesiaceae", "fungo_filamentoso",
     "Inoculação traumática no solo (pés descalços)",
     "Solo tropical; material vegetal",
     "Nordeste do Brasil; trabalhadores rurais que caminham descalços"),

    ("Scedosporium apiospermum",
     "Scedospório",
     "Scedosporiaceae", "fungo_filamentoso",
     "Inalação de esporos; inoculação traumática; inalação em quase-afogamento",
     "Solo, esgoto, águas poluídas",
     "Distribuição nacional; infecções localizadas e disseminadas em imunossuprimidos"),

    ("Fusarium solani",
     "Fusário (fusariose)",
     "Nectriaceae", "fungo_filamentoso",
     "Inoculação traumática (unhas, pés); inalação; via cateter",
     "Solo, restos vegetais, plantas",
     "Distribuição nacional; onicomicose e ceratite; fusariose invasiva em neutropênicos"),

    ("Fusarium oxysporum",
     "Fusário oxysporum",
     "Nectriaceae", "fungo_filamentoso",
     "Inoculação traumática; inalação de esporos",
     "Solo, restos vegetais, parasita de plantas",
     "Infecções cutâneas e subcutâneas; fusariose invasiva em leucêmicos"),

    ("Trichophyton rubrum",
     "Tricofíton rubrum (dermatofitose)",
     "Ajellomycetaceae", "fungo_filamentoso",
     "Contato direto com pessoas infectadas, fômites, solos; autoinoculação",
     "Humanos (antropofílico); solos",
     "Principal agente de tinea pedis, onicomicose e tinea corporis no Brasil"),

    ("Trichophyton tonsurans",
     "Tricofíton tonsurans (tinea capitis)",
     "Ajellomycetaceae", "fungo_filamentoso",
     "Contato direto; fômites (pentes, chapéus); compartilhamento de itens de higiene",
     "Humanos (antropofílico)",
     "Principal agente de tinea capitis em crianças no Brasil; maior prevalência em Norte e Nordeste"),

    ("Microsporum canis",
     "Microsporino canis",
     "Ajellomycetaceae", "fungo_filamentoso",
     "Contato com animais infectados (cães, gatos); contato direto com humanos infectados",
     "Cães e gatos (zoofílico)",
     "Tinea capitis e tinea corporis; distribuição nacional; comum em crianças com animais de estimação"),

    ("Malassezia furfur",
     "Malassezia (pitiríase versicolor)",
     "Cordycipitaceae", "levedura",
     "Endógena (microbiota normal da pele); não contagiosa entre pessoas",
     "Microbiota cutânea normal de humanos; superfícies oleosas da pele",
     "Pitiríase versicolor extremamente prevalente no Brasil (clima quente e úmido); distribuição nacional"),

    ("Lacazia loboi",
     "Lacazia (lobomicose, doença de Jorge Lobo)",
     "Trimorphomycetaceae", "levedura",
     "Provável inoculação traumática; contato com água e solo de áreas endêmicas",
     "Solo e água de rios da Amazônia; golfinhos de rio (Sotalia fluviatilis)",
     "Endêmica na Amazônia brasileira; AM, PA, RO, AC; descrita por Jorge Lobo em 1931"),

    ("Pneumocystis jirovecii",
     "Pneumocistis (PCP — pneumonia por Pneumocystis)",
     "Pneumocystidaceae", "fungo_filamentoso",
     "Inalação de esporos; transmissão aérea de pessoa a pessoa (imunocomprometidos)",
     "Humanos (comensal em pulmões de pessoas imunocompetentes saudáveis)",
     "Distribuição nacional; principal causa de pneumonia oportunista em HIV/AIDS com CD4 < 200; imunossuprimidos"),

    ("Exophiala jeanselmei",
     "Exofíala (feohifomicose, micetoma fúngico negro)",
     "Herpotrichiellaceae", "fungo_filamentoso",
     "Inoculação traumática com material vegetal ou solo; inalação ocasional",
     "Solo, madeira em decomposição, plantas — ambiente tropical e subtropical",
     "Distribuição nacional; mais frequente em Nordeste e Norte do Brasil; associada a feohifomicose subcutânea e infecções de SNC em imunocomprometidos"),
]

CLASSES_ANTIFUNGICOS = [
    # (nome, mecanismo_acao, alvo_celular)
    ("Polienos", "Ligação ao ergosterol da membrana fúngica — formação de poros e lise osmótica",
     "Ergosterol da membrana citoplasmática fúngica"),
    ("Azólicos — Triazólicos", "Inibição da lanosterol 14α-desmetilase (CYP51) — bloqueia síntese de ergosterol",
     "CYP51 fúngico (enzima da via de síntese do ergosterol)"),
    ("Azólicos — Imidazólicos", "Inibição da lanosterol 14α-desmetilase — depleção de ergosterol e acúmulo de precursores tóxicos",
     "CYP51 fúngico"),
    ("Equinocandinas", "Inibição não competitiva da β-(1,3)-D-glucano sintase — disrupção da parede celular fúngica",
     "Subunidade Fks1/Fks2 da β-(1,3)-D-glucano sintase"),
    ("Alilaminas", "Inibição da esqualeno epoxidase — depleção de ergosterol e acúmulo de esqualeno tóxico",
     "Esqualeno epoxidase fúngica"),
    ("Antimetabólitos pirimídínicos", "Conversão intracelular em 5-fluorouracil — inibição da síntese de DNA e RNA fúngico",
     "Timidilato sintase e RNA polimerase fúngica"),
    ("Griseofulvina", "Ligação à tubulina fúngica — inibição da divisão celular (mitose)",
     "Microtúbulos fúngicos (tubulina)"),
    ("Iodeto de Potássio", "Mecanismo incerto — possível imunomodulação e atividade direta",
     "Incerto — possivelmente ergosterol e resposta imune do hospedeiro"),
    # ── Antimicrobianos usados no domínio fúngico (S46) ───────────────────────
    # Fármacos que NÃO são antifúngicos clássicos (azol/polieno/equinocandina),
    # mas são o tratamento de patologias do domínio fúngico — sobretudo a PCP
    # (Pneumocystis jirovecii, reclassificado como fungo) e a sulfa da
    # paracoccidioidomicose. Registrados aqui pelo mesmo motivo que o sistema
    # duplica fármacos entre catálogos de domínio (ex.: Metronidazol em
    # antibióticos e antiparasitários): cada domínio resolve seus próprios nomes.
    ("Sulfamídicos (Antifolato)",
     "Inibição sequencial da via do folato — sulfametoxazol bloqueia a di-hidropteroato sintase "
     "e a trimetoprima a di-hidrofolato redutase, colapsando a síntese de purinas do patógeno",
     "Enzimas da via do folato (DHPS e DHFR)"),
    ("Diamidinas Aromáticas",
     "Ligação ao DNA (sulco menor) e interferência no metabolismo do folato e na fosforilação "
     "oxidativa do patógeno",
     "DNA e enzimas do metabolismo energético do patógeno"),
    ("Lincosamidas",
     "Inibição da síntese proteica por ligação à subunidade ribossomal 50S (associada à primaquina "
     "na PCP)",
     "Subunidade ribossomal 50S"),
    ("Naftoquinonas",
     "Inibição do complexo citocromo bc1 (complexo III) da cadeia respiratória — colapso do "
     "potencial de membrana mitocondrial do patógeno",
     "Complexo III (citocromo bc1) da cadeia respiratória"),
]

# (nome_generico, nome_comercial_ou_None, classe_nome, via_administracao, disponivel_sus, anvisa_registrado, observacoes)
ANTIFUNGICOS = [
    # ══════════════════════════════════════════════════════════════════
    # POLIENOS
    # ══════════════════════════════════════════════════════════════════
    ("Anfotericina B desoxicolato", "Fungizone",
     "Polienos", "iv", True, True,
     "Formulação convencional; amplo espectro (Candida, Aspergillus, Cryptococcus, Mucor, Histoplasma, Paracoccidioides); "
     "nefrotoxicidade grave dose-limitante; disponível no SUS; padrão-ouro para infecções fúngicas graves"),

    ("Anfotericina B lipossomal", "AmBisome",
     "Polienos", "iv", False, True,
     "Formulação lipídica com menor nefrotoxicidade que desoxicolato; mesma eficácia antifúngica; "
     "disponível via RENAME excepcionalmente; indicada em insuficiência renal ou intolerância à formulação convencional"),

    ("Anfotericina B complexo lipídico (ABLC)", "Abelcet",
     "Polienos", "iv", False, True,
     "Complexo lipídico; menor nefrotoxicidade que desoxicolato; aprovada ANVISA; menor custo que lipossomal; "
     "indicada em pacientes com toxicidade renal à formulação convencional"),

    ("Nistatina", "Mycostatin / Nistatin",
     "Polienos", "oral/tópico", True, True,
     "Uso tópico e oral para candidíase oral e mucocutânea; absorção oral mínima — ação local; "
     "disponível no SUS para candidíase orofaríngea; sem indicação para infecções sistêmicas"),

    # ══════════════════════════════════════════════════════════════════
    # TRIAZÓLICOS
    # ══════════════════════════════════════════════════════════════════
    ("Fluconazol", "Diflucan / Zoltec / Flucovim",
     "Azólicos — Triazólicos", "oral/iv", True, True,
     "1ª linha para candidíase oral, vaginal e urinária; consolidação/manutenção de criptococose; "
     "não cobre Aspergillus, C. krusei, C. glabrata (reduzida sensibilidade); ampla disponibilidade no SUS"),

    ("Itraconazol", "Sporanox / Itranax",
     "Azólicos — Triazólicos", "oral", True, True,
     "1ª linha para paracoccidioidomicose, histoplasmose (formas leves-moderadas), esporotricose, "
     "dermatofitoses refratárias, onicomicose; cobre Aspergillus; biodisponibilidade variável — tomar com refeição gordurosa; "
     "disponível no SUS (RENAME)"),

    ("Voriconazol", "Vfend",
     "Azólicos — Triazólicos", "oral/iv", False, True,
     "1ª linha para aspergilose invasiva; cobertura de Scedosporium e Fusarium; "
     "não cobre Mucor/Rhizopus; disponibilidade limitada — via CEAF (componente especializado); "
     "múltiplas interações medicamentosas via CYP2C19 e CYP3A4; monitoramento de níveis séricos recomendado"),

    ("Posaconazol", "Noxafil",
     "Azólicos — Triazólicos", "oral/iv", False, True,
     "Amplo espectro: Aspergillus, Mucor, Fusarium, Candida resistente; profilaxia em neutropênicos "
     "e transplantados de células-tronco; disponível via CEAF ou importação excepcional; tomar com refeição gordurosa"),

    ("Isavuconazol", "Cresemba",
     "Azólicos — Triazólicos", "oral/iv", False, True,
     "Alternativa ao voriconazol para aspergilose invasiva; cobre também Mucor (diferente do voriconazol); "
     "melhor tolerabilidade hepática; aprovado ANVISA; disponibilidade muito limitada no Brasil"),

    ("Ravuconazol", None,
     "Azólicos — Triazólicos", "oral", False, False,
     "Investigacional no Brasil para doença de Chagas (ensaios clínicos); não aprovado como antifúngico no Brasil; "
     "longa meia-vida; mencionado por pesquisas nacionais"),

    # ══════════════════════════════════════════════════════════════════
    # IMIDAZÓLICOS — USO TÓPICO
    # ══════════════════════════════════════════════════════════════════
    ("Clotrimazol", "Canesten / Fungiderme",
     "Azólicos — Imidazólicos", "tópico/vaginal", True, True,
     "Uso tópico para dermatofitoses, candidíase vaginal e oral; disponível no SUS; "
     "cremes, óvulos vaginais, solução ótica; primeira linha para candidíase vaginal não complicada"),

    ("Miconazol", "Daktarin / Micostatin",
     "Azólicos — Imidazólicos", "tópico/oral", True, True,
     "Gel oral para candidíase oral; cremes para dermatofitoses; "
     "pó para prevenção de tinea pedis; disponível no SUS (formulação oral pediátrica)"),

    ("Cetoconazol", "Nizoral",
     "Azólicos — Imidazólicos", "oral/tópico", True, True,
     "Oral: uso restrito por hepatotoxicidade grave (FDA alerta 2013) — uso tópico preferido; "
     "xampu e creme para pitiríase versicolor, dermatite seborreica, candidíase cutânea; disponível no SUS"),

    ("Econazol", "Pevaryl",
     "Azólicos — Imidazólicos", "tópico", False, True,
     "Creme e pó tópico para dermatofitoses e candidíase cutânea; "
     "alternativa ao clotrimazol; não disponível no SUS"),

    ("Oxiconazol", "Oxistat",
     "Azólicos — Imidazólicos", "tópico", False, True,
     "Creme tópico para tinea corporis, tinea pedis, tinea cruris; uso limitado no Brasil"),

    ("Fenticonazol", "Lomexin",
     "Azólicos — Imidazólicos", "vaginal/tópico", False, True,
     "Óvulos e creme vaginal para candidíase vaginal; dermatofitoses superficiais"),

    # ══════════════════════════════════════════════════════════════════
    # EQUINOCANDINAS
    # ══════════════════════════════════════════════════════════════════
    ("Caspofungina", "Cancidas",
     "Equinocandinas", "iv", False, True,
     "1ª linha para candidemia em pacientes críticos (UTI) e aspergilose invasiva refratária; "
     "dose ataque 70 mg IV D1, depois 50 mg IV 24/24h; aprovada ANVISA; disponibilidade limitada — "
     "uso hospitalar restrito; sem atividade contra Cryptococcus e Mucor"),

    ("Micafungina", "Mycamine",
     "Equinocandinas", "iv", False, True,
     "Candidemia, candidíase esofágica, profilaxia em transplante de células-tronco; "
     "aprovada ANVISA; disponibilidade limitada no Brasil; sem atividade contra Cryptococcus e Mucor"),

    ("Anidulafungina", "Eraxis",
     "Equinocandinas", "iv", False, True,
     "Candidemia e candidíase invasiva; não metabolizada pelo CYP450 — menor risco de interações; "
     "aprovada ANVISA; disponibilidade muito limitada no Brasil"),

    # ══════════════════════════════════════════════════════════════════
    # ALILAMINAS
    # ══════════════════════════════════════════════════════════════════
    ("Terbinafina", "Lamisil / Terbinafil",
     "Alilaminas", "oral/tópico", True, True,
     "1ª linha para onicomicose por dermatófitos (oral); tinea pedis, tinea corporis, tinea capitis (sistêmica); "
     "maior eficácia que itraconazol oral para onicomicose dermatofítica; disponível no SUS; "
     "hepatotoxicidade rara — monitorar em tratamentos prolongados"),

    ("Naftifina", "Exoderil",
     "Alilaminas", "tópico", False, True,
     "Creme e gel tópico para dermatofitoses superficiais; alternativa ao clotrimazol; não disponível no SUS"),

    # ══════════════════════════════════════════════════════════════════
    # ANTIMETABÓLITOS
    # ══════════════════════════════════════════════════════════════════
    ("Flucitosina (5-FC)", "Ancotil",
     "Antimetabólitos pirimídínicos", "oral/iv", False, True,
     "Sinergismo com anfotericina B para criptococose meníngea grave (combinação padrão-ouro da indução); "
     "não usar em monoterapia (resistência rápida); disponibilidade muito limitada no Brasil — "
     "importação excepcional; monitorar hemograma e função renal"),

    # ══════════════════════════════════════════════════════════════════
    # OUTROS ANTIFÚNGICOS
    # ══════════════════════════════════════════════════════════════════
    ("Griseofulvina", "Fulcin / Grisovin",
     "Griseofulvina", "oral", True, True,
     "Tinea capitis em crianças (tratamento sistêmico obrigatório); dermatofitoses de cabelo e couro cabeludo; "
     "sem indicação para onicomicose (pouco eficaz); disponível no SUS; tomar com refeição gordurosa; "
     "longa duração: 4-8 semanas para tinea capitis"),

    ("Iodeto de Potássio (KI)", "Iodeto de Potássio",
     "Iodeto de Potássio", "oral", True, True,
     "Tratamento histórico e atual da esporotricose cutânea linfangítica (formas leves) — eficaz e de baixo custo; "
     "solução saturada (SSKI) 5-10 gotas 3x/dia com progressão gradual; disponível no SUS; "
     "alternativa ao itraconazol em gestantes com cautela; efeitos adversos: gosto metálico, acne iodada"),

    ("Ciclopirox olamina", "Batrafen / Loprox",
     "Azólicos — Imidazólicos", "tópico", False, True,
     "Esmalte e creme tópico para onicomicose superficial e dermatofitoses; "
     "mecanismo diferente dos azólicos — inibição de enzimas mitocondriais; "
     "alternativa tópica para onicomicose quando antifúngico oral contraindicado"),

    ("Amorolfina", "Loceryl",
     "Azólicos — Imidazólicos", "tópico", False, True,
     "Esmalte tópico para onicomicose superficial e distal leve-moderada; "
     "aplicação semanal; pode ser associada à terbinafina oral; não disponível no SUS"),

    # ── Antimicrobianos do domínio fúngico — PCP e sulfa da PCM (S46) ─────────
    ("Sulfametoxazol + Trimetoprima", "Bactrim / Cotrimoxazol",
     "Sulfamídicos (Antifolato)", "iv/oral", True, True,
     "Cotrimoxazol. TRATAMENTO DE ESCOLHA da PCP (15-20 mg/kg/dia de trimetoprima, IV ou VO em "
     "4 doses × 21 dias) e opção de baixo custo na paracoccidioidomicose leve-moderada. "
     "Monitorar função renal, K+ e hemograma. Disponível no SUS (RENAME)."),
    ("Pentamidina (isetionato)", "Pentacarinat",
     "Diamidinas Aromáticas", "iv", True, True,
     "Alternativa ao SMX-TMP na PCP em alergia grave não controlável (4 mg/kg/dia IV × 21 dias). "
     "Toxicidade: hipoglicemia grave, hipotensão, nefrotoxicidade, pancreatite, arritmia (QT). "
     "Forma inalatória: apenas profilaxia, não tratamento de PCP ativa."),
    ("Clindamicina", "Dalacin",
     "Lincosamidas", "iv/oral", True, True,
     "PCP de 2ª linha em associação com primaquina (clindamicina 600 mg IV 8/8h + primaquina "
     "30 mg/dia VO × 21 dias). Primaquina contraindicada em deficiência de G6PD — testar antes."),
    ("Atovaquona", "Mepron",
     "Naftoquinonas", "oral", False, False,
     "Alternativa oral para PCP leve-moderada em intolerância ao SMX-TMP (750 mg VO 12/12h × 21 "
     "dias, com refeição gordurosa). Disponibilidade limitada no Brasil (não incorporado ao SUS)."),
]

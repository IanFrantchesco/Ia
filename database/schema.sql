-- ============================================================
-- BANCO DE DADOS: PATOLOGIAS BACTERIANAS NO BRASIL
-- Fontes: Ministério da Saúde (PCDT), ANVISA, SBI, SINAN
-- ============================================================

PRAGMA foreign_keys = ON;

-- ------------------------------------------------------------
-- FONTES OFICIAIS
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS fontes_oficiais (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    sigla       TEXT NOT NULL,
    nome        TEXT NOT NULL,
    orgao       TEXT NOT NULL,
    tipo        TEXT NOT NULL, -- 'PCDT', 'Nota Técnica', 'Diretriz', 'Boletim', 'Portaria'
    url         TEXT,
    ano         INTEGER,
    descricao   TEXT
);

-- ------------------------------------------------------------
-- FAMÍLIAS / CLASSES TAXONÔMICAS
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS familias_bacterianas (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    nome        TEXT NOT NULL,
    filo        TEXT
);

-- ------------------------------------------------------------
-- FAMÍLIAS VIRAIS
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS familias_virais (
    id      INTEGER PRIMARY KEY AUTOINCREMENT,
    nome    TEXT NOT NULL UNIQUE,
    grupo   TEXT
);

-- ------------------------------------------------------------
-- VÍRUS
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS virus (
    id                      INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_cientifico         TEXT NOT NULL UNIQUE,
    nome_comum              TEXT,
    familia_id              INTEGER REFERENCES familias_virais(id),
    tipo_acido_nucleico     TEXT CHECK(tipo_acido_nucleico IN ('DNA', 'RNA', 'DNA/RNA')),
    envelope                TEXT CHECK(envelope IN ('sim', 'nao')),
    transmissao_principal   TEXT,
    reservatorio            TEXT
);

-- ------------------------------------------------------------
-- CLASSES DE ANTIVIRAIS
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS classes_antivirais (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    nome            TEXT NOT NULL UNIQUE,
    mecanismo_acao  TEXT,
    alvo_celular    TEXT
);

-- ------------------------------------------------------------
-- ANTIVIRAIS
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS antivirais (
    id                  INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_generico       TEXT NOT NULL UNIQUE,
    nome_comercial      TEXT,
    classe_id           INTEGER REFERENCES classes_antivirais(id),
    via_administracao   TEXT,
    disponivel_sus      BOOLEAN DEFAULT 0,
    anvisa_registrado   BOOLEAN DEFAULT 1,
    observacoes         TEXT
);

-- ------------------------------------------------------------
-- RELAÇÃO PATOLOGIA ↔ VÍRUS
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS patologia_virus (
    patologia_id    INTEGER NOT NULL REFERENCES patologias(id),
    virus_id        INTEGER NOT NULL REFERENCES virus(id),
    papel           TEXT CHECK(papel IN ('principal', 'secundario', 'oportunista')),
    frequencia_pct  REAL,
    observacoes     TEXT,
    PRIMARY KEY (patologia_id, virus_id)
);

-- ------------------------------------------------------------
-- EFICÁCIA DE ANTIVIRAIS
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS eficacia_antiviral (
    id                  INTEGER PRIMARY KEY AUTOINCREMENT,
    virus_id            INTEGER NOT NULL REFERENCES virus(id),
    antiviral_id        INTEGER NOT NULL REFERENCES antivirais(id),
    patologia_id        INTEGER REFERENCES patologias(id),
    eficacia_pct        REAL CHECK(eficacia_pct BETWEEN 0 AND 100),
    linha_tratamento    INTEGER CHECK(linha_tratamento IN (1, 2, 3)),
    nivel_evidencia     TEXT CHECK(nivel_evidencia IN ('A', 'B', 'C', 'D')),
    resistencia_br_pct  REAL,
    fonte_id            INTEGER REFERENCES fontes_oficiais(id),
    ano_dado            INTEGER,
    consideracoes       TEXT
);

-- ------------------------------------------------------------
-- POSOLOGIA ANTIVIRAIS
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS posologia_viral (
    id                  INTEGER PRIMARY KEY AUTOINCREMENT,
    antiviral_id        INTEGER NOT NULL REFERENCES antivirais(id),
    patologia_id        INTEGER REFERENCES patologias(id),
    populacao           TEXT NOT NULL CHECK(populacao IN
                            ('adulto','pediatrico','gestante','idoso','insuf_renal','insuf_hepatica','neonato')),
    dose_unitaria       TEXT NOT NULL,
    frequencia          TEXT NOT NULL,
    via                 TEXT NOT NULL,
    duracao_min_dias    INTEGER,
    duracao_max_dias    INTEGER,
    duracao_texto       TEXT,
    ajuste_renal        BOOLEAN DEFAULT 0,
    ajuste_hepatico     BOOLEAN DEFAULT 0,
    observacoes         TEXT,
    fonte_id            INTEGER REFERENCES fontes_oficiais(id)
);

-- ------------------------------------------------------------
-- INTERAÇÕES ANTIVIRAIS
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS interacoes_antivirais (
    id                      INTEGER PRIMARY KEY AUTOINCREMENT,
    antiviral_id            INTEGER NOT NULL REFERENCES antivirais(id),
    medicamento_interagente TEXT NOT NULL,
    classe_interagente      TEXT,
    mecanismo               TEXT,
    gravidade               TEXT CHECK(gravidade IN ('contraindicada','grave','moderada','leve')),
    efeito_clinico          TEXT,
    conduta                 TEXT,
    fonte_id                INTEGER REFERENCES fontes_oficiais(id)
);

-- ------------------------------------------------------------
-- TRATAMENTO PADRÃO-OURO VIRAL
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS tratamento_padrao_ouro_viral (
    id                      INTEGER PRIMARY KEY AUTOINCREMENT,
    patologia_id            INTEGER NOT NULL REFERENCES patologias(id),
    antiviral_principal     TEXT NOT NULL,
    combinacao              TEXT,
    regime_resumido         TEXT,
    duracao_resumida        TEXT,
    justificativa           TEXT,
    alternativa_alergia     TEXT,
    alternativa_resistencia TEXT,
    obs_especiais           TEXT,
    grau_recomendacao       TEXT CHECK(grau_recomendacao IN ('A', 'B', 'C', 'D')),
    nivel_evidencia         TEXT,
    fonte_id                INTEGER REFERENCES fontes_oficiais(id),
    ano_diretriz            INTEGER
);

-- Índices virais
CREATE INDEX IF NOT EXISTS idx_patologia_virus_pat  ON patologia_virus(patologia_id);
CREATE INDEX IF NOT EXISTS idx_patologia_virus_vir  ON patologia_virus(virus_id);
CREATE INDEX IF NOT EXISTS idx_eficacia_viral_virus  ON eficacia_antiviral(virus_id);
CREATE INDEX IF NOT EXISTS idx_eficacia_viral_atv    ON eficacia_antiviral(antiviral_id);
CREATE INDEX IF NOT EXISTS idx_eficacia_viral_pat    ON eficacia_antiviral(patologia_id);
CREATE INDEX IF NOT EXISTS idx_trat_padrao_viral_pat ON tratamento_padrao_ouro_viral(patologia_id);

-- ------------------------------------------------------------
-- BACTÉRIAS
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS bacterias (
    id                  INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_cientifico     TEXT NOT NULL UNIQUE,
    nome_comum          TEXT,
    gram                TEXT CHECK(gram IN ('positiva', 'negativa', 'indeterminada', 'nao_aplicavel')),
    familia_id          INTEGER REFERENCES familias_bacterianas(id),
    aerobiose           TEXT CHECK(aerobiose IN ('aerobio', 'anaerobio', 'facultativo', 'microaerofilo')),
    formato             TEXT, -- coco, bacilo, espirilo, etc.
    resistencia_natural TEXT,
    observacoes         TEXT
);

-- ------------------------------------------------------------
-- CLASSES DE ANTIBIÓTICOS
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS classes_antibioticos (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    nome            TEXT NOT NULL UNIQUE,
    mecanismo_acao  TEXT,
    alvo_celular    TEXT
);

-- ------------------------------------------------------------
-- ANTIBIÓTICOS
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS antibioticos (
    id                  INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_generico       TEXT NOT NULL UNIQUE,
    nome_comercial      TEXT,
    classe_id           INTEGER REFERENCES classes_antibioticos(id),
    via_administracao   TEXT, -- 'oral', 'iv', 'im', 'topica', 'oral/iv'
    disponivel_sus      BOOLEAN DEFAULT 0,
    anvisa_registrado   BOOLEAN DEFAULT 1,
    observacoes         TEXT
);

-- ------------------------------------------------------------
-- CATEGORIAS DE PATOLOGIAS
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS categorias_patologias (
    id      INTEGER PRIMARY KEY AUTOINCREMENT,
    nome    TEXT NOT NULL UNIQUE,
    sistema TEXT  -- sistema orgânico
);

-- ------------------------------------------------------------
-- PATOLOGIAS (100 entradas)
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS patologias (
    id                          INTEGER PRIMARY KEY AUTOINCREMENT,
    nome                        TEXT NOT NULL,
    cid10                       TEXT,
    categoria_id                INTEGER REFERENCES categorias_patologias(id),
    descricao                   TEXT,
    notificacao_compulsoria     BOOLEAN DEFAULT 0,
    tipo_notificacao            TEXT, -- 'imediata', 'semanal', NULL
    prevalencia_br              TEXT CHECK(prevalencia_br IN ('muito_alta', 'alta', 'media', 'baixa', 'rara')),
    mortalidade_br              TEXT CHECK(mortalidade_br IN ('alta', 'media', 'baixa')),
    populacao_risco             TEXT,
    fonte_epidemio_id           INTEGER REFERENCES fontes_oficiais(id)
);

-- ------------------------------------------------------------
-- RELAÇÃO PATOLOGIA ↔ BACTÉRIA
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS patologia_bacteria (
    patologia_id    INTEGER NOT NULL REFERENCES patologias(id),
    bacteria_id     INTEGER NOT NULL REFERENCES bacterias(id),
    papel           TEXT CHECK(papel IN ('principal', 'secundario', 'oportunista')),
    frequencia_pct  REAL,   -- % dos casos em que esta bactéria é o agente
    observacoes     TEXT,
    PRIMARY KEY (patologia_id, bacteria_id)
);

-- ------------------------------------------------------------
-- EFICÁCIA DE ANTIBIÓTICOS
-- Dados baseados em PCDTs, ANVISA e estudos epidemiológicos nacionais
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS eficacia_antibiotico (
    id                  INTEGER PRIMARY KEY AUTOINCREMENT,
    bacteria_id         INTEGER NOT NULL REFERENCES bacterias(id),
    antibiotico_id      INTEGER NOT NULL REFERENCES antibioticos(id),
    patologia_id        INTEGER REFERENCES patologias(id),   -- NULL = geral para a bactéria
    eficacia_pct        REAL CHECK(eficacia_pct BETWEEN 0 AND 100),
    linha_tratamento    INTEGER CHECK(linha_tratamento IN (1, 2, 3)), -- 1ª, 2ª, 3ª linha
    nivel_evidencia     TEXT CHECK(nivel_evidencia IN ('A', 'B', 'C', 'D')),
    -- A = ECA de alta qualidade; B = ECA de moderada qualidade / meta-análise;
    -- C = estudos observacionais; D = consenso de especialistas
    resistencia_br_pct  REAL,   -- % de resistência isolada no Brasil (dados ANSIRE/WHONET)
    fonte_id            INTEGER REFERENCES fontes_oficiais(id),
    ano_dado            INTEGER,
    consideracoes       TEXT
);

-- ------------------------------------------------------------
-- ÍNDICES PARA PERFORMANCE
-- ------------------------------------------------------------
CREATE INDEX IF NOT EXISTS idx_patologia_bacteria_pat  ON patologia_bacteria(patologia_id);
CREATE INDEX IF NOT EXISTS idx_patologia_bacteria_bac  ON patologia_bacteria(bacteria_id);
CREATE INDEX IF NOT EXISTS idx_eficacia_bacteria        ON eficacia_antibiotico(bacteria_id);
CREATE INDEX IF NOT EXISTS idx_eficacia_antibiotico     ON eficacia_antibiotico(antibiotico_id);
CREATE INDEX IF NOT EXISTS idx_eficacia_patologia       ON eficacia_antibiotico(patologia_id);
CREATE INDEX IF NOT EXISTS idx_patologias_cid10         ON patologias(cid10);

-- ------------------------------------------------------------
-- VIEWS ÚTEIS
-- ------------------------------------------------------------
-- ------------------------------------------------------------
-- POSOLOGIA
-- Fonte: PCDTs MS, bulas ANVISA, SBI/SBPT diretrizes
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS posologia (
    id                  INTEGER PRIMARY KEY AUTOINCREMENT,
    antibiotico_id      INTEGER NOT NULL REFERENCES antibioticos(id),
    patologia_id        INTEGER REFERENCES patologias(id),   -- NULL = posologia geral do ATB
    populacao           TEXT NOT NULL CHECK(populacao IN
                            ('adulto','pediatrico','gestante','idoso','insuf_renal','insuf_hepatica')),
    dose_unitaria       TEXT NOT NULL,   -- ex: "500 mg", "1 g", "25 mg/kg"
    frequencia          TEXT NOT NULL,   -- ex: "8/8h", "12/12h", "1x/dia"
    via                 TEXT NOT NULL,   -- ex: "oral", "iv", "im"
    duracao_min_dias    INTEGER,
    duracao_max_dias    INTEGER,
    duracao_texto       TEXT,            -- ex: "6 semanas", "14 dias", "dose única"
    ajuste_renal        BOOLEAN DEFAULT 0,
    ajuste_hepatico     BOOLEAN DEFAULT 0,
    observacoes         TEXT,
    fonte_id            INTEGER REFERENCES fontes_oficiais(id)
);

-- ------------------------------------------------------------
-- INTERAÇÕES MEDICAMENTOSAS
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS interacoes_medicamentosas (
    id                      INTEGER PRIMARY KEY AUTOINCREMENT,
    antibiotico_id          INTEGER NOT NULL REFERENCES antibioticos(id),
    medicamento_interagente TEXT NOT NULL,
    classe_interagente      TEXT,
    mecanismo               TEXT,
    gravidade               TEXT NOT NULL CHECK(gravidade IN
                                ('leve','moderada','grave','contraindicada')),
    efeito_clinico          TEXT NOT NULL,
    conduta                 TEXT NOT NULL,
    fonte_id                INTEGER REFERENCES fontes_oficiais(id)
);

CREATE INDEX IF NOT EXISTS idx_posologia_atb       ON posologia(antibiotico_id);
CREATE INDEX IF NOT EXISTS idx_posologia_pat       ON posologia(patologia_id);
CREATE INDEX IF NOT EXISTS idx_interacao_atb       ON interacoes_medicamentosas(antibiotico_id);

-- ------------------------------------------------------------
-- VIEW POSOLOGIA COMPLETA
-- ------------------------------------------------------------
CREATE VIEW IF NOT EXISTS v_posologia_completa AS
SELECT
    a.nome_generico         AS antibiotico,
    p2.nome                 AS patologia,
    po.populacao,
    po.dose_unitaria,
    po.frequencia,
    po.via,
    po.duracao_texto,
    po.duracao_min_dias,
    po.duracao_max_dias,
    po.ajuste_renal,
    po.ajuste_hepatico,
    po.observacoes,
    fo.sigla                AS fonte
FROM posologia po
JOIN antibioticos a  ON a.id  = po.antibiotico_id
LEFT JOIN patologias p2 ON p2.id = po.patologia_id
LEFT JOIN fontes_oficiais fo ON fo.id = po.fonte_id
ORDER BY a.nome_generico, po.populacao;

-- ------------------------------------------------------------
-- VIEW INTERAÇÕES
-- ------------------------------------------------------------
CREATE VIEW IF NOT EXISTS v_interacoes AS
SELECT
    a.nome_generico         AS antibiotico,
    i.medicamento_interagente,
    i.classe_interagente,
    i.gravidade,
    i.efeito_clinico,
    i.conduta,
    fo.sigla                AS fonte
FROM interacoes_medicamentosas i
JOIN antibioticos a ON a.id = i.antibiotico_id
LEFT JOIN fontes_oficiais fo ON fo.id = i.fonte_id
ORDER BY i.gravidade DESC, a.nome_generico;

-- ------------------------------------------------------------
CREATE VIEW IF NOT EXISTS v_tratamento_completo AS
SELECT
    p.nome                          AS patologia,
    p.cid10,
    p.prevalencia_br,
    b.nome_cientifico               AS bacteria,
    b.gram,
    pb.papel                        AS papel_bacteria,
    pb.frequencia_pct               AS frequencia_bacteria_pct,
    a.nome_generico                 AS antibiotico,
    ca.nome                         AS classe_antibiotico,
    a.via_administracao,
    a.disponivel_sus,
    e.eficacia_pct,
    e.linha_tratamento,
    e.nivel_evidencia,
    e.resistencia_br_pct,
    e.consideracoes,
    fo.sigla                        AS fonte,
    e.ano_dado
FROM patologias p
JOIN patologia_bacteria pb ON pb.patologia_id = p.id
JOIN bacterias b ON b.id = pb.bacteria_id
JOIN eficacia_antibiotico e ON e.bacteria_id = b.id
    AND (e.patologia_id = p.id OR e.patologia_id IS NULL)
JOIN antibioticos a ON a.id = e.antibiotico_id
JOIN classes_antibioticos ca ON ca.id = a.classe_id
LEFT JOIN fontes_oficiais fo ON fo.id = e.fonte_id
ORDER BY p.nome, e.linha_tratamento, e.eficacia_pct DESC;

CREATE VIEW IF NOT EXISTS v_resistencia_bacteriana AS
SELECT
    b.nome_cientifico               AS bacteria,
    b.gram,
    a.nome_generico                 AS antibiotico,
    ca.nome                         AS classe,
    e.resistencia_br_pct,
    e.ano_dado,
    fo.sigla                        AS fonte
FROM eficacia_antibiotico e
JOIN bacterias b ON b.id = e.bacteria_id
JOIN antibioticos a ON a.id = e.antibiotico_id
JOIN classes_antibioticos ca ON ca.id = a.classe_id
LEFT JOIN fontes_oficiais fo ON fo.id = e.fonte_id
WHERE e.resistencia_br_pct IS NOT NULL
ORDER BY e.resistencia_br_pct DESC;

-- ------------------------------------------------------------
-- TRATAMENTO PADRÃO-OURO POR PATOLOGIA
-- Fontes: PCDTs MS, GVS, SBI, ANVISA
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS tratamento_padrao_ouro (
    id                      INTEGER PRIMARY KEY AUTOINCREMENT,
    patologia_id            INTEGER NOT NULL REFERENCES patologias(id),
    antibiotico_principal   TEXT NOT NULL,
    combinacao              TEXT,
    regime_resumido         TEXT,
    duracao_resumida        TEXT,
    justificativa           TEXT,
    alternativa_alergia     TEXT,
    alternativa_resistencia TEXT,
    obs_especiais           TEXT,
    grau_recomendacao       TEXT CHECK(grau_recomendacao IN ('A', 'B', 'C', 'D')),
    nivel_evidencia         TEXT,
    fonte_id                INTEGER REFERENCES fontes_oficiais(id),
    ano_diretriz            INTEGER
);

CREATE INDEX IF NOT EXISTS idx_trat_padrao_patologia ON tratamento_padrao_ouro(patologia_id);

-- ------------------------------------------------------------
-- FAMÍLIAS FÚNGICAS
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS familias_fungicas (
    id      INTEGER PRIMARY KEY AUTOINCREMENT,
    nome    TEXT NOT NULL UNIQUE,
    grupo   TEXT
);

-- ------------------------------------------------------------
-- FUNGOS
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS fungos (
    id                  INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_cientifico     TEXT NOT NULL UNIQUE,
    nome_comum          TEXT,
    familia_id          INTEGER REFERENCES familias_fungicas(id),
    tipo                TEXT CHECK(tipo IN ('levedura','fungo_filamentoso','dimórfico')),
    transmissao_principal TEXT,
    reservatorio        TEXT,
    distribuicao_br     TEXT
);

-- ------------------------------------------------------------
-- CLASSES DE ANTIFÚNGICOS
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS classes_antifungicos (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    nome            TEXT NOT NULL UNIQUE,
    mecanismo_acao  TEXT,
    alvo_celular    TEXT
);

-- ------------------------------------------------------------
-- ANTIFÚNGICOS
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS antifungicos (
    id                  INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_generico       TEXT NOT NULL UNIQUE,
    nome_comercial      TEXT,
    classe_id           INTEGER REFERENCES classes_antifungicos(id),
    via_administracao   TEXT,
    disponivel_sus      BOOLEAN DEFAULT 0,
    anvisa_registrado   BOOLEAN DEFAULT 1,
    observacoes         TEXT
);

-- ------------------------------------------------------------
-- RELAÇÃO PATOLOGIA ↔ FUNGO
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS patologia_fungo (
    patologia_id    INTEGER NOT NULL REFERENCES patologias(id),
    fungo_id        INTEGER NOT NULL REFERENCES fungos(id),
    papel           TEXT CHECK(papel IN ('principal','secundario','oportunista')),
    frequencia_pct  REAL,
    observacoes     TEXT,
    PRIMARY KEY (patologia_id, fungo_id)
);

-- ------------------------------------------------------------
-- EFICÁCIA DE ANTIFÚNGICOS
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS eficacia_antifungico (
    id                  INTEGER PRIMARY KEY AUTOINCREMENT,
    fungo_id            INTEGER NOT NULL REFERENCES fungos(id),
    antifungico_id      INTEGER NOT NULL REFERENCES antifungicos(id),
    patologia_id        INTEGER REFERENCES patologias(id),
    eficacia_pct        REAL CHECK(eficacia_pct BETWEEN 0 AND 100),
    linha_tratamento    INTEGER CHECK(linha_tratamento IN (1,2,3)),
    nivel_evidencia     TEXT CHECK(nivel_evidencia IN ('A','B','C','D')),
    resistencia_br_pct  REAL,
    fonte_id            INTEGER REFERENCES fontes_oficiais(id),
    ano_dado            INTEGER,
    consideracoes       TEXT
);

-- ------------------------------------------------------------
-- POSOLOGIA ANTIFÚNGICOS
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS posologia_fungica (
    id                  INTEGER PRIMARY KEY AUTOINCREMENT,
    antifungico_id      INTEGER NOT NULL REFERENCES antifungicos(id),
    patologia_id        INTEGER REFERENCES patologias(id),
    populacao           TEXT NOT NULL CHECK(populacao IN
                            ('adulto','pediatrico','gestante','idoso','insuf_renal','insuf_hepatica','neonato')),
    dose_unitaria       TEXT NOT NULL,
    frequencia          TEXT NOT NULL,
    via                 TEXT NOT NULL,
    duracao_min_dias    INTEGER,
    duracao_max_dias    INTEGER,
    duracao_texto       TEXT,
    ajuste_renal        BOOLEAN DEFAULT 0,
    ajuste_hepatico     BOOLEAN DEFAULT 0,
    observacoes         TEXT,
    fonte_id            INTEGER REFERENCES fontes_oficiais(id)
);

-- ------------------------------------------------------------
-- INTERAÇÕES ANTIFÚNGICOS
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS interacoes_antifungicos (
    id                      INTEGER PRIMARY KEY AUTOINCREMENT,
    antifungico_id          INTEGER NOT NULL REFERENCES antifungicos(id),
    medicamento_interagente TEXT NOT NULL,
    classe_interagente      TEXT,
    mecanismo               TEXT,
    gravidade               TEXT CHECK(gravidade IN ('contraindicada','grave','moderada','leve')),
    efeito_clinico          TEXT,
    conduta                 TEXT,
    fonte_id                INTEGER REFERENCES fontes_oficiais(id)
);

-- ------------------------------------------------------------
-- TRATAMENTO PADRÃO-OURO FÚNGICO
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS tratamento_padrao_ouro_fungico (
    id                      INTEGER PRIMARY KEY AUTOINCREMENT,
    patologia_id            INTEGER NOT NULL REFERENCES patologias(id),
    antifungico_principal   TEXT NOT NULL,
    combinacao              TEXT,
    regime_resumido         TEXT,
    duracao_resumida        TEXT,
    justificativa           TEXT,
    alternativa_alergia     TEXT,
    alternativa_resistencia TEXT,
    obs_especiais           TEXT,
    grau_recomendacao       TEXT CHECK(grau_recomendacao IN ('A','B','C','D')),
    nivel_evidencia         TEXT,
    fonte_id                INTEGER REFERENCES fontes_oficiais(id),
    ano_diretriz            INTEGER
);

-- Índices fúngicos
CREATE INDEX IF NOT EXISTS idx_patologia_fungo_pat   ON patologia_fungo(patologia_id);
CREATE INDEX IF NOT EXISTS idx_patologia_fungo_fun   ON patologia_fungo(fungo_id);
CREATE INDEX IF NOT EXISTS idx_eficacia_fungica_fun  ON eficacia_antifungico(fungo_id);
CREATE INDEX IF NOT EXISTS idx_eficacia_fungica_atf  ON eficacia_antifungico(antifungico_id);
CREATE INDEX IF NOT EXISTS idx_eficacia_fungica_pat  ON eficacia_antifungico(patologia_id);
CREATE INDEX IF NOT EXISTS idx_trat_padrao_fungico   ON tratamento_padrao_ouro_fungico(patologia_id);

-- ============================================================
-- MÓDULO PARASITOSES
-- Fontes: PCDT-MS, SVS/GVS 5ª ed. 2022, SBMT, SBI, ANVISA
-- ============================================================

CREATE TABLE IF NOT EXISTS familias_parasitarias (
    id      INTEGER PRIMARY KEY AUTOINCREMENT,
    nome    TEXT NOT NULL UNIQUE,
    filo    TEXT
);

CREATE TABLE IF NOT EXISTS parasitos (
    id                  INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_cientifico     TEXT NOT NULL UNIQUE,
    nome_comum          TEXT,
    familia_id          INTEGER REFERENCES familias_parasitarias(id),
    tipo                TEXT CHECK(tipo IN ('protozoario','helminto_nematoda','helminto_trematoda','helminto_cestoda','ectoparasito')),
    ciclo_hospedeiro    TEXT,
    habitat_principal   TEXT,
    distribuicao_br     TEXT,
    reservatorio        TEXT,
    vetor               TEXT
);

CREATE TABLE IF NOT EXISTS classes_antiparasitarios (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    nome            TEXT NOT NULL UNIQUE,
    mecanismo_acao  TEXT,
    alvo_celular    TEXT
);

CREATE TABLE IF NOT EXISTS antiparasitarios (
    id                      INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_generico           TEXT NOT NULL UNIQUE,
    nome_comercial          TEXT,
    classe_id               INTEGER REFERENCES classes_antiparasitarios(id),
    via_administracao       TEXT,
    disponivel_sus          BOOLEAN DEFAULT 0,
    anvisa_registrado       BOOLEAN DEFAULT 1,
    observacoes             TEXT
);

CREATE TABLE IF NOT EXISTS patologia_parasito (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    patologia_id    INTEGER NOT NULL REFERENCES patologias(id),
    parasito_id     INTEGER NOT NULL REFERENCES parasitos(id),
    papel           TEXT CHECK(papel IN ('principal','secundario','oportunista','vetor')),
    frequencia_pct  REAL,
    UNIQUE(patologia_id, parasito_id)
);

CREATE TABLE IF NOT EXISTS eficacia_antiparasitario (
    id                  INTEGER PRIMARY KEY AUTOINCREMENT,
    parasito_id         INTEGER NOT NULL REFERENCES parasitos(id),
    antiparasitario_id  INTEGER NOT NULL REFERENCES antiparasitarios(id),
    patologia_id        INTEGER REFERENCES patologias(id),
    eficacia_pct        REAL,
    linha_tratamento    INTEGER DEFAULT 1,
    nivel_evidencia     TEXT,
    resistencia_br_pct  REAL,
    fonte_id            INTEGER REFERENCES fontes_oficiais(id),
    ano_dado            INTEGER,
    consideracoes       TEXT,
    UNIQUE(parasito_id, antiparasitario_id, patologia_id)
);

CREATE TABLE IF NOT EXISTS posologia_parasitaria (
    id                  INTEGER PRIMARY KEY AUTOINCREMENT,
    antiparasitario_id  INTEGER NOT NULL REFERENCES antiparasitarios(id),
    patologia_id        INTEGER REFERENCES patologias(id),
    populacao           TEXT,
    dose_unitaria       TEXT,
    frequencia          TEXT,
    via                 TEXT,
    duracao_min_dias    INTEGER,
    duracao_max_dias    INTEGER,
    duracao_texto       TEXT,
    ajuste_renal        BOOLEAN DEFAULT 0,
    ajuste_hepatico     BOOLEAN DEFAULT 0,
    observacoes         TEXT,
    fonte_id            INTEGER REFERENCES fontes_oficiais(id)
);

CREATE TABLE IF NOT EXISTS interacoes_antiparasitarios (
    id                      INTEGER PRIMARY KEY AUTOINCREMENT,
    antiparasitario_id      INTEGER NOT NULL REFERENCES antiparasitarios(id),
    medicamento_interagente TEXT NOT NULL,
    classe_interagente      TEXT,
    mecanismo               TEXT,
    gravidade               TEXT CHECK(gravidade IN ('grave','moderada','leve','contraindicada')),
    efeito_clinico          TEXT,
    conduta                 TEXT,
    fonte_id                INTEGER REFERENCES fontes_oficiais(id)
);

CREATE TABLE IF NOT EXISTS tratamento_padrao_ouro_parasitario (
    id                      INTEGER PRIMARY KEY AUTOINCREMENT,
    patologia_id            INTEGER NOT NULL UNIQUE REFERENCES patologias(id),
    antiparasitario_principal TEXT NOT NULL,
    combinacao              TEXT,
    regime_resumido         TEXT,
    duracao_resumida        TEXT,
    justificativa           TEXT,
    alternativa_alergia     TEXT,
    alternativa_resistencia TEXT,
    obs_especiais           TEXT,
    grau_recomendacao       TEXT CHECK(grau_recomendacao IN ('A','B','C','D')),
    nivel_evidencia         TEXT,
    fonte_id                INTEGER REFERENCES fontes_oficiais(id),
    ano_diretriz            INTEGER
);

-- Índices parasitoses
CREATE INDEX IF NOT EXISTS idx_patologia_parasito_pat  ON patologia_parasito(patologia_id);
CREATE INDEX IF NOT EXISTS idx_patologia_parasito_par  ON patologia_parasito(parasito_id);
CREATE INDEX IF NOT EXISTS idx_eficacia_parasit_par    ON eficacia_antiparasitario(parasito_id);
CREATE INDEX IF NOT EXISTS idx_eficacia_parasit_atp    ON eficacia_antiparasitario(antiparasitario_id);
CREATE INDEX IF NOT EXISTS idx_eficacia_parasit_pat    ON eficacia_antiparasitario(patologia_id);
CREATE INDEX IF NOT EXISTS idx_trat_padrao_parasit     ON tratamento_padrao_ouro_parasitario(patologia_id);

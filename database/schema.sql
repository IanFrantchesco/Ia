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

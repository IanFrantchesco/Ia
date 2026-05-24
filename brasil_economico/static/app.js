/* ═══════════════════════════════════════════════════
   Brasil Político — Frontend Logic
══════════════════════════════════════════════════ */

'use strict';

// ── Constants ──────────────────────────────────────────────────────────────

const COLORS = ['#00D4AA', '#FFB800', '#FF6B6B'];

// Radar chart metrics with normalization config
// score = 0-100, higher always means better performance
const RADAR_METRICS = [
  { key: 'media_crescimento_pib',  label: 'Crescimento\nPIB',     higherBetter: true,  min: -5,   max: 14,    log: false },
  { key: 'media_inflacao',         label: 'Estab.\nPreços',        higherBetter: false, min: 1,    max: 500,   log: true  },
  { key: 'media_desemprego',       label: 'Emprego',               higherBetter: false, min: 3,    max: 15,    log: false },
  { key: 'media_idh',              label: 'IDH',                   higherBetter: true,  min: 0.19, max: 0.77,  log: false },
  { key: 'media_gini',             label: 'Igualdade\nSocial',     higherBetter: false, min: 0.47, max: 0.65,  log: false },
  { key: 'media_pobreza',          label: 'Redução\nPobreza',      higherBetter: false, min: 3,    max: 32,    log: false },
  { key: 'media_esperanca_vida',   label: 'Longevidade',           higherBetter: true,  min: 36,   max: 76,    log: false },
  { key: 'media_fbcf',             label: 'Investimento\n/PIB',    higherBetter: true,  min: 12,   max: 24,    log: false },
];

// Bar chart categories — cada métrica tem uma explicação breve
const CHART_CATEGORIES = [
  {
    title: 'Crescimento Econômico', icon: '📈',
    metrics: [
      {
        key: 'media_crescimento_pib', label: 'Cresc. PIB real', unit: '%',
        info: 'Variação do PIB descontada a inflação. Mede o quanto a economia cresceu de verdade no período.',
      },
      {
        key: 'media_pib_per_capita', label: 'PIB per capita', unit: 'USD',
        info: 'Riqueza média por habitante em dólares. Indica o nível de desenvolvimento econômico do país.',
      },
      {
        key: 'media_fbcf', label: 'Invest. (FBCF/PIB)', unit: '%',
        info: 'Formação Bruta de Capital Fixo como % do PIB. Mede o quanto foi investido em máquinas, obras e equipamentos — base do crescimento futuro.',
      },
    ],
  },
  {
    title: 'Estabilidade de Preços', icon: '💰',
    metrics: [
      {
        key: 'media_inflacao', label: 'Inflação', unit: '%',
        info: 'Aumento geral dos preços ao consumidor (IPCA oficial pós-1995; estimativas históricas antes). Inflação alta corrói o poder de compra da população.',
      },
      {
        key: 'media_selic', label: 'SELIC', unit: '%',
        info: 'Taxa básica de juros definida pelo Banco Central. Influencia o custo do crédito, investimentos e o controle da inflação.',
      },
      {
        key: 'media_cambio', label: 'Câmbio BRL/USD', unit: '',
        info: 'Quantos reais são necessários para comprar 1 dólar (média do mandato). Câmbio alto encarece importações e pode estimular exportações.',
      },
    ],
  },
  {
    title: 'Emprego e Renda', icon: '👷',
    metrics: [
      {
        key: 'media_desemprego', label: 'Desemprego', unit: '%',
        info: 'Percentual da população economicamente ativa sem trabalho. Inclui estimativas históricas para períodos sem pesquisa formal (PNAD).',
      },
      {
        key: 'media_salario_min', label: 'Sal. mínimo real', unit: 'R$',
        info: 'Salário mínimo corrigido pela inflação em valores de hoje (R$ de 2024). Indica o poder de compra real do trabalhador ao longo do tempo.',
      },
    ],
  },
  {
    title: 'Equilíbrio Fiscal', icon: '⚖️',
    metrics: [
      {
        key: 'media_divida_pib', label: 'Dívida bruta/PIB', unit: '%',
        info: 'Total da dívida pública como proporção do PIB. Valores altos indicam maior vulnerabilidade fiscal e pressão sobre os juros.',
      },
      {
        key: 'media_resultado_primario', label: 'Resultado primário', unit: '% PIB',
        info: 'Diferença entre receitas e despesas do governo, excluindo juros da dívida. Positivo (superávit) = governo gasta menos do que arrecada.',
      },
    ],
  },
  {
    title: 'Setor Externo', icon: '🌍',
    metrics: [
      {
        key: 'media_balanca_comercial', label: 'Balança comercial', unit: 'bi USD',
        info: 'Diferença entre exportações e importações de bens. Positivo significa que o Brasil vendeu mais ao exterior do que comprou.',
      },
      {
        key: 'media_reservas', label: 'Reservas internacionais', unit: 'bi USD',
        info: 'Dólares e outros ativos guardados pelo Banco Central. Funcionam como colchão de segurança em crises cambiais.',
      },
      {
        key: 'media_ied', label: 'IED (Invest. Estrangeiro)', unit: 'bi USD',
        info: 'Capital estrangeiro investido diretamente em empresas e projetos no Brasil. Indica confiança do mercado externo na economia.',
      },
    ],
  },
  {
    title: 'Desenvolvimento Social', icon: '🤝',
    metrics: [
      {
        key: 'media_idh', label: 'IDH', unit: '',
        info: 'Índice de Desenvolvimento Humano do PNUD (0 a 1). Combina três dimensões: renda per capita, educação e expectativa de vida.',
      },
      {
        key: 'media_gini', label: 'Coeficiente de Gini', unit: '',
        info: 'Mede a desigualdade de renda (0 = igualdade total; 1 = desigualdade máxima). Quanto menor, mais equilibrada é a distribuição de renda.',
      },
      {
        key: 'media_pobreza', label: 'Pobreza extrema', unit: '%',
        info: 'Percentual da população vivendo com menos de US$ 2,15 por dia (linha de pobreza extrema do Banco Mundial).',
      },
      {
        key: 'media_esperanca_vida', label: 'Esperança de vida', unit: 'anos',
        info: 'Quantos anos, em média, uma pessoa nascida naquele período viverá. Reflete qualidade do sistema de saúde, saneamento e condições de vida.',
      },
      {
        key: 'media_mortalidade', label: 'Mortalidade infantil', unit: '/mil',
        info: 'Número de mortes de crianças menores de 1 ano para cada 1.000 nascidos vivos. Um dos indicadores sociais mais sensíveis ao desenvolvimento.',
      },
    ],
  },
];

// ── State ──────────────────────────────────────────────────────────────────

let presidentes = [];
let resumos     = [];
let chartInstances = {};

// ── Init ───────────────────────────────────────────────────────────────────

async function init() {
  presidentes = await apiFetch('/api/presidentes');
  const defaultOpt = '<option value="">— Selecione —</option>';
  const opts = presidentes.map(p =>
    `<option value="${esc(p.presidente)}">${esc(p.presidente)} (${p.ano_inicio}–${p.ano_fim})</option>`
  ).join('');

  for (let i = 0; i < 3; i++) {
    const sel = document.getElementById(`sel-${i}`);
    sel.innerHTML = (i === 2 ? '<option value="">— Opcional —</option>' : defaultOpt) + opts;
    sel.addEventListener('change', () => updateSelInfo(i));
  }

  document.getElementById('compare-btn').addEventListener('click', compare);

  Chart.defaults.color = '#8892A4';
  Chart.defaults.borderColor = 'rgba(255,255,255,0.06)';
}

// ── Selector info ──────────────────────────────────────────────────────────

function updateSelInfo(idx) {
  const val = document.getElementById(`sel-${idx}`).value;
  const info = document.getElementById(`info-${idx}`);
  if (!val) { info.innerHTML = ''; return; }
  const p = presidentes.find(x => x.presidente === val);
  if (!p) return;
  info.innerHTML = `<strong>${p.partido}</strong> · ${p.fase} · ${p.ano_inicio}–${p.ano_fim}`;
}

// ── Compare ────────────────────────────────────────────────────────────────

async function compare() {
  const selected = [0, 1, 2]
    .map(i => document.getElementById(`sel-${i}`).value)
    .filter(Boolean);

  if (selected.length < 2) {
    alert('Selecione pelo menos 2 presidentes para comparar.');
    return;
  }

  setLoading(true);

  try {
    resumos = await Promise.all(selected.map(nome =>
      apiFetch(`/api/resumo/${encodeURIComponent(nome)}`)
    ));
  } catch (e) {
    alert('Erro ao carregar dados. Verifique o servidor.');
    setLoading(false);
    return;
  }

  renderSummaryCards();
  renderRadarChart();
  renderBarCharts();

  document.getElementById('results').hidden = false;
  document.getElementById('results').scrollIntoView({ behavior: 'smooth', block: 'start' });
  setLoading(false);

  // Gera análise automaticamente
  generateAnalysis();
}

// ── Summary Cards ──────────────────────────────────────────────────────────

function renderSummaryCards() {
  const row = document.getElementById('summary-row');
  row.innerHTML = resumos.map((r, i) => {
    const color = COLORS[i];
    const pib    = fmtNum(r.media_crescimento_pib, 2, '%');
    const infl   = fmtNum(r.media_inflacao, 2, '%');
    const desemp = fmtNum(r.media_desemprego, 1, '%');
    const idh    = r.media_idh ? r.media_idh.toFixed(3) : 'N/D';
    const pibCl  = r.media_crescimento_pib > 0 ? 'positive' : 'negative';

    return `
    <div class="summary-card">
      <div class="summary-card-top">
        <div class="pres-dot" style="background:${color}"></div>
        <div>
          <div class="summary-card-name">${esc(r.presidente)}</div>
          <div class="summary-card-meta">${esc(r.partido)} · ${r.ano_inicio}–${r.ano_fim}</div>
        </div>
      </div>
      <div class="kpi-grid">
        <div class="kpi">
          <div class="kpi-label">Cresc. PIB</div>
          <div class="kpi-value ${pibCl}">${pib}</div>
        </div>
        <div class="kpi">
          <div class="kpi-label">Inflação</div>
          <div class="kpi-value neutral">${infl}</div>
        </div>
        <div class="kpi">
          <div class="kpi-label">Desemprego</div>
          <div class="kpi-value neutral">${desemp}</div>
        </div>
        <div class="kpi">
          <div class="kpi-label">IDH</div>
          <div class="kpi-value neutral">${idh}</div>
        </div>
      </div>
    </div>`;
  }).join('');
}

// ── Radar Chart ────────────────────────────────────────────────────────────

function normalizeScore(value, metric) {
  if (value == null || isNaN(value)) return null;

  let v = value;
  let min = metric.min;
  let max = metric.max;

  if (metric.log) {
    v   = Math.log(Math.max(v, 1));
    min = Math.log(Math.max(min, 1));
    max = Math.log(Math.max(max, 1));
  }

  let score = (v - min) / (max - min);
  score = Math.max(0, Math.min(1, score));

  if (!metric.higherBetter) score = 1 - score;
  return Math.round(score * 100);
}

function renderRadarChart() {
  const labels = RADAR_METRICS.map(m => m.label);

  const datasets = resumos.map((r, i) => ({
    label: r.presidente,
    data: RADAR_METRICS.map(m => normalizeScore(r[m.key], m)),
    borderColor: COLORS[i],
    backgroundColor: COLORS[i] + '22',
    borderWidth: 2,
    pointBackgroundColor: COLORS[i],
    pointRadius: 5,
    pointHoverRadius: 7,
  }));

  destroyChart('radar');
  const ctx = document.getElementById('chart-radar').getContext('2d');
  chartInstances['radar'] = new Chart(ctx, {
    type: 'radar',
    data: { labels, datasets },
    options: {
      responsive: true,
      animation: { duration: 800 },
      scales: {
        r: {
          min: 0, max: 100,
          ticks: {
            stepSize: 25,
            font: { size: 9 },
            color: '#4A5568',
            backdropColor: 'transparent',
          },
          grid:       { color: 'rgba(255,255,255,0.06)' },
          angleLines: { color: 'rgba(255,255,255,0.08)' },
          pointLabels: { font: { size: 10, weight: '500' }, color: '#8892A4' },
        },
      },
      plugins: {
        legend: { display: false },
        tooltip: {
          callbacks: {
            label: ctx => `${ctx.dataset.label}: ${ctx.raw ?? 'N/D'}/100`,
          },
        },
      },
    },
  });

  // Legend
  const leg = document.getElementById('radar-legend');
  leg.innerHTML = resumos.map((r, i) =>
    `<div class="legend-item">
       <div class="legend-dot" style="background:${COLORS[i]}"></div>
       <span>${esc(r.presidente)}</span>
     </div>`
  ).join('');
}

// ── Bar Charts ─────────────────────────────────────────────────────────────

function renderBarCharts() {
  const grid = document.getElementById('bar-grid');
  grid.innerHTML = '';
  destroyChart('chart-');

  CHART_CATEGORIES.forEach(cat => {
    cat.metrics.forEach(m => {
      const vals = resumos.map(r => r[m.key]);
      if (vals.every(v => v == null)) return;

      const id = `chart-${m.key}`;
      const card = document.createElement('div');
      card.className = 'bar-chart-card';
      card.innerHTML = `
        <div class="bar-chart-title">${cat.icon} <span>${esc(m.label)}</span></div>
        <div class="bar-chart-sub">${esc(cat.title)}${m.unit ? ' · ' + esc(m.unit) : ''}</div>
        ${m.info ? `<div class="bar-chart-info">${esc(m.info)}</div>` : ''}
        <div class="bar-chart-wrap"><canvas id="${id}"></canvas></div>
      `;
      grid.appendChild(card);

      const datasets = resumos.map((r, i) => ({
        label: r.presidente,
        data: [r[m.key] ?? null],
        backgroundColor: COLORS[i] + 'CC',
        borderColor: COLORS[i],
        borderWidth: 1.5,
        borderRadius: 8,
        barThickness: 40,
      }));

      const ctx = card.querySelector(`#${id}`).getContext('2d');
      chartInstances[id] = new Chart(ctx, {
        type: 'bar',
        data: { labels: ['Média do mandato'], datasets },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          animation: { duration: 600 },
          plugins: {
            legend: {
              position: 'bottom',
              labels: { font: { size: 10 }, boxWidth: 10, padding: 10 },
            },
            tooltip: {
              callbacks: {
                label: ctx => {
                  const v = ctx.parsed.y;
                  return v != null ? `${ctx.dataset.label}: ${fmtNum(v, 2, m.unit)}` : `${ctx.dataset.label}: N/D`;
                },
              },
            },
          },
          scales: {
            x: { display: false },
            y: {
              grid: { color: 'rgba(255,255,255,0.05)' },
              ticks: { font: { size: 10 }, maxTicksLimit: 5 },
            },
          },
        },
      });
    });
  });
}

// ── AI Analysis ────────────────────────────────────────────────────────────

async function generateAnalysis() {
  const btn     = document.getElementById('ai-btn');
  const result  = document.getElementById('ai-result');
  const content = document.getElementById('ai-content');

  btn.disabled = true;
  btn.innerHTML = `<div class="spinner" style="width:16px;height:16px;border-width:2px;margin:0"></div> Gerando análise…`;
  result.hidden = true;

  try {
    const data = await apiFetch('/api/analise', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ presidentes: resumos }),
    });
    content.innerHTML = marked.parse(data.analise);
    result.hidden = false;
  } catch (err) {
    const isKeyErr = (err.message || '').includes('ANTHROPIC_API_KEY');
    content.innerHTML = `
      <div class="ai-error">
        <strong>⚠ Análise por IA indisponível</strong><br><br>
        ${isKeyErr
          ? `Para ativar, adicione a variável de ambiente <code>ANTHROPIC_API_KEY</code> no Railway:<br>
             <strong>Settings → Variables → New Variable</strong><br>
             Nome: <code>ANTHROPIC_API_KEY</code> · Valor: sua chave de <a href="https://console.anthropic.com" target="_blank" style="color:var(--c1)">console.anthropic.com</a>`
          : esc(err.message || 'Erro ao gerar análise.')}
      </div>`;
    result.hidden = false;
  }

  btn.disabled = false;
  btn.innerHTML = `
    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
      <circle cx="12" cy="12" r="3"/>
      <path d="M12 1v4M12 19v4M4.22 4.22l2.83 2.83M16.95 16.95l2.83 2.83M1 12h4M19 12h4M4.22 19.78l2.83-2.83M16.95 7.05l2.83-2.83"/>
    </svg>
    Regerar Análise`;
}

// ── Helpers ────────────────────────────────────────────────────────────────

async function apiFetch(url, opts = {}) {
  const res = await fetch(url, opts);
  if (!res.ok) {
    const err = await res.json().catch(() => ({}));
    throw new Error(err.detail || `HTTP ${res.status}`);
  }
  return res.json();
}

function fmtNum(v, decimals = 2, unit = '') {
  if (v == null || isNaN(v)) return 'N/D';
  const n = Number(v).toFixed(decimals);
  return unit ? `${n} ${unit}` : n;
}

function esc(str) {
  return String(str ?? '')
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}

function setLoading(on) {
  document.getElementById('loading').hidden = !on;
  if (on) document.getElementById('results').hidden = true;
}

function destroyChart(prefix) {
  Object.keys(chartInstances).forEach(k => {
    if (k.startsWith(prefix)) {
      chartInstances[k].destroy();
      delete chartInstances[k];
    }
  });
}

// ── Boot ───────────────────────────────────────────────────────────────────
init();

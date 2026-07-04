# Template Padrão — Postagens @arritmia.update

## Contexto do projeto
Canal de curadoria científica semanal em cardiologia e arritmias para cardiologistas e eletrofisiologistas no Brasil. Instagram: @arritmia.update. Produto: assinatura WhatsApp R$50/mês.

---

## Formato dos slides
- **Plataforma:** Instagram Feed
- **Dimensões:** 1080×1080px (1:1)
- **Idioma do prompt:** inglês (melhor eficácia no DALL-E/ChatGPT)
- **Texto visível nos slides:** português
- **Gerador:** ChatGPT com DALL-E 3

---

## Paleta obrigatória
| Elemento | Cor | Hex |
|---|---|---|
| Fundo | Azul-marinho escuro | #010717 |
| Destaque principal | Azul ciano elétrico | #00BFFF |
| Texto | Branco | #FFFFFF |
| Alerta 1 | Laranja | #E07B00 |
| Alerta 2 | Vermelho | #C0001A |
| Mapa eletroanatômico | Gradiente laranja-vermelho-amarelo | — |

---

## Estilo visual geral
- Fundo com textura sutil de espaço/galáxia
- Iluminação cinematográfica dramática
- Elementos 3D fotorrealistas com glow ciano
- Imagem fantasma de mapa eletroanatômico ao fundo (15% opacidade) nos slides 2, 3 e 4
- Linha de ECG ciano decorativa
- Tipografia ultra-negrito (estilo Montserrat ExtraBold / Impact)

---

## Estrutura dos 5 slides

### SLIDE 1 — Capa (impacto visual máximo)
**Elementos:**
- Badge "1" círculo branco — canto superior esquerdo
- Tag da revista — cápsula ciano centro superior (ex: "Heart Rhythm", "JAMA Cardiology", "Circulation")
- Título 2 linhas: linha 1 branco + linha 2 ciano elétrico — ultra-negrito, grande
- Imagem 3D fotorrealista centralizada (coração, estrutura anatômica relevante ao tema)
- Labels com linhas finas apontando para elementos da imagem
- Elemento técnico à direita (imagem comparativa, gráfico, scan)
- 2 boxes de alerta (laranja + vermelho) com ícone e texto curto
- Linha de ECG horizontal decorativa
- Footer padrão

**Instrução:** Este slide deve ter o maior impacto visual da série — é a capa que para o scroll.

---

### SLIDE 2 — O Estudo
**Elementos:**
- Badge "2" círculo ciano — canto superior esquerdo
- Ícone 3D de livro brilhante + título "O ESTUDO"
- Linha separadora ciano
- Parágrafo descritivo do estudo (palavras-chave em ciano)
- 2 blocos com gradiente: ícone 3D à esquerda + texto à direita
- Seção "Fonte:" com journal e DOI em ciano
- Footer padrão

---

### SLIDE 3 — Por Que Isso Importa?
**Elementos:**
- Badge "3" — canto superior esquerdo
- Ícone 3D de lupa brilhante + título 2 linhas: "POR QUE ISSO" (branco) / "IMPORTA?" (ciano)
- 3 blocos com separador ciano tracejado: ícone 3D circular ciano + texto branco
- Footer padrão

---

### SLIDE 4 — O Que Foi Observado?
**Elementos:**
- Badge "4" — canto superior esquerdo
- Ícone 3D de lupa brilhante + título 2 linhas: "O QUE FOI" (branco) / "OBSERVADO?" (ciano)
- 3 blocos com separador ciano tracejado: ícone 3D circular ciano + texto branco
- Footer padrão

---

### SLIDE 5 — CTA (sem número)
**Elementos:**
- Sem badge de número
- Coração 3D fotorrealista dominando 60% superior — glow azul neon + destaque vermelho/laranja no centro
- Linha de ECG ciano atravessando horizontalmente
- 6 ícones hexagonais/circulares flutuando ao redor (ECG, molécula, monitor cardíaco, DNA, coração anatômico, mapa de mapeamento)
- Texto inferior: "Entre em contato" (branco negrito grande) + "e receba suas atualizações em cardiologia e arritmias." (ciano médio) + "Não fique de fora dessa revolução científica." (itálico branco)
- Footer padrão

---

## Footer padrão (todos os slides)
- Esquerda: logo "ARRITMIA UPDATE" — ícone de coração com linha de ECG integrada em ciano + "ARRITMIA" branco negrito + "UPDATE" ciano
- Direita: "ATUALIZAÇÕES SEMANAIS" + linha de ECG decorativa
- Linha separadora fina com brilho ciano acima

---

## Margem de segurança (pós-geração)
Após gerar e baixar os slides, solicitar ajuste de margem:
- Escalar para 93% do tamanho
- Centralizar em canvas 1080×1080 navy (#010717)
- Resultado: ~38px de margem em todos os lados
- Garante que badges e footer não sejam cortados pelo Instagram

---

## Exportação para anúncio (evitar erro de dimensionamento)
- **NUNCA subir o arquivo cru do DALL-E como anúncio.** O DALL-E gera em
  1024×1792 (≈9:16), mais alto que o limite do feed do Meta → erro de
  dimensionamento no upload.
- Sempre reformatar para o tamanho exato antes de anunciar:
  - **1:1 → 1080×1080** (padrão atual, universal em feed/stories/reels)
  - 4:5 → 1080×1350 também é aceito e recomendado pelo Meta (mais tela no
    feed, melhor engajamento), mas precisa de versão 9:16 separada p/ stories
- O passo de margem de segurança acima já entrega o tamanho exato aceito.

---

## Legenda padrão
- Gancho forte na primeira linha (sem hashtag, sem emoji excessivo)
- Corpo: contexto clínico → novidade do estudo → resultados em bullets (→)
- Journal + data + DOI
- CTA: "Quer receber toda semana o que realmente importa em arritmia e eletrofisiologia? Entre em contato 👇"
- Encerramento: "💾 Salve esse post para acessar o DOI quando precisar."
- Público-alvo: cardiologistas e eletrofisiologistas brasileiros
- Tom: técnico mas direto, sem linguagem de divulgação leiga

---

## Para gerar nova série de slides
Enviar ao assistente:
1. Título do artigo
2. Journal e data de publicação
3. DOI
4. Resumo ou achados principais
5. Solicitar: "Gere os 5 prompts no template padrão"

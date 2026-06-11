# Aprender Python do Zero 🐍

### Um curso completo para iniciantes, usando o seu próprio projeto

Este material foi feito para quem **nunca programou**. A cada passo você vê um
bloco de código pequeno, e logo abaixo a explicação **linha por linha**, na
linguagem mais simples possível. O conhecimento é construído aos poucos: cada
módulo usa o que você aprendeu no anterior — e nada aparece "do nada".

No final, você vai entender o código que faz o seu painel clínico de
patologias funcionar — porque vamos aprender olhando justamente para ele, com
trechos reais do `app.py` e do `static/patologias.html`.

Esta é a versão **estendida**: cada módulo tem mais exemplos, mais variações
"o que acontece se eu mudar isto?", e cinco módulos novos que não existiam na
primeira versão (tratamento de erros, conjuntos, JSON, testes automatizados e
git/deploy). Existe também um caderno separado, o `EXERCICIOS_PYTHON.md`, com
desafios práticos progressivos — use os dois lado a lado.

> **Como estudar:** vá devagar, **um módulo por vez**. Sempre que aparecer um
> bloco de código, **digite você mesmo** no computador e veja o resultado. Ler
> não basta — é digitando, errando e corrigindo que se aprende a programar.
> Se um módulo parecer difícil, releia o anterior antes de continuar: o curso
> é uma escada, não uma lista solta.

---

## Índice

**Parte 1 — Primeiros passos**
- Módulo 0 · O que é programar (e como rodar Python)
- Módulo 1 · Variáveis: guardando informação
- Módulo 2 · Os tipos básicos e conversão entre eles
- Módulo 3 · Texto (strings) em detalhe
- Módulo 4 · Números e contas
- Módulo 5 · Verdadeiro ou falso (booleanos)

**Parte 2 — Guardando muitas coisas**
- Módulo 6 · Listas
- Módulo 7 · Dicionários
- Módulo 8 · Tuplas e desempacotamento
- Módulo 9 · Conjuntos (sets)

**Parte 3 — Tomando decisões e repetindo**
- Módulo 10 · `if`, `elif`, `else` e o operador ternário
- Módulo 11 · Loops (`for`, `while`, `break`, `continue`)
- Módulo 12 · Compreensões de lista e de dicionário

**Parte 4 — Organizando o código**
- Módulo 13 · Funções em profundidade
- Módulo 14 · Módulos, pacotes e `import`
- Módulo 15 · Classes (uma introdução suave)
- Módulo 16 · Tratamento de erros (`try`/`except`)

**Parte 5 — O seu projeto de verdade**
- Módulo 17 · Banco de dados e SQL
- Módulo 18 · Ferramentas avançadas que seu projeto usa
- Módulo 19 · JSON: a língua da web
- Módulo 20 · Como funciona uma API (FastAPI)
- Módulo 21 · Lendo um endpoint inteiro, linha por linha
- Módulo 22 · Testes automatizados (garantindo que nada quebra)
- Módulo 23 · Git e deploy: do código ao site no ar

**Apêndices**
- A · Erros comuns e como resolver
- B · Gabarito dos exercícios deste material
- C · Glossário de bolso
- D · Mapa do projeto (onde fica cada coisa)

---
---

# PARTE 1 — Primeiros passos

## Módulo 0 · O que é programar (e como rodar Python)

**Programar** é dar instruções para o computador, uma de cada vez, na ordem
certa. O computador é obediente, mas burro: ele faz **exatamente** o que você
escreve — nem mais, nem menos. Python é só o idioma que usamos para escrever
essas instruções (e é um dos mais fáceis de ler, porque parece inglês simples).

### Duas formas de rodar Python

**1. Modo interativo** — bom para testar coisas rápidas. Abra o terminal,
digite `python3` e aperte Enter. Vai aparecer `>>>`:

```python
>>> print("Olá, mundo!")
Olá, mundo!
```

- `print(...)` é uma **ordem**: "mostre na tela o que está entre os parênteses".
- `"Olá, mundo!"` é um **texto** (note as aspas — todo texto fica entre aspas).
- A segunda linha, sem `>>>`, é a **resposta** do computador.

Para sair do modo interativo, digite `exit()` ou `Ctrl+D`.

**2. Arquivo `.py`** — é como programas de verdade são escritos, inclusive o
seu `app.py`. Você cria um arquivo de texto com extensão `.py`, escreve várias
linhas, salva, e depois manda o Python executar **o arquivo inteiro**:

```python
# arquivo: ola.py
print("Olá, mundo!")
print("Esta é a segunda linha")
```

No terminal:
```
python3 ola.py
```
Saída:
```
Olá, mundo!
Esta é a segunda linha
```

A diferença é importante: no modo interativo você vê o resultado **linha a
linha**; num arquivo, o Python lê **todas as linhas de cima para baixo** e só
depois mostra os resultados dos `print`.

### Comentários: anotações que o Python ignora

Qualquer coisa depois de `#` numa linha é um **comentário** — serve para
humanos lerem, o Python pula direto:

```python
# Isto é um comentário, o Python não executa esta linha
print("Isto sim é executado")  # comentário no fim da linha também funciona
```

Comentários bons explicam o **porquê**, não o **o quê** (o código já diz o
"quê"). No seu `app.py`, por exemplo, há comentários explicando *por que* o
SQL usa `?` em vez de colar o valor direto — isso não é óbvio só de olhar o
código, então vale a pena escrever.

### Não tenha medo de erros

Errar faz parte — é a forma normal de aprender a programar. Quando você
escreve algo errado, o Python avisa com uma **mensagem de erro**:

```python
>>> print("Olá)
  File "<stdin>", line 1
    print("Olá)
          ^
SyntaxError: unterminated string literal
```

Parece assustador, mas leia a **última linha**: `SyntaxError: unterminated
string literal` quer dizer "texto sem fechamento" — esquecemos a aspa final.
Quase todo erro tem uma dica na última linha. Ler erros é uma habilidade, não
um fracasso. Vamos voltar a isso com mais detalhes no Apêndice A e no Módulo 16.

> **Experimente:** digite `print(2 + 2)` e depois `print("2 + 2")`. Por que um
> mostra `4` e o outro mostra `2 + 2`? (Resposta: com aspas vira texto; sem
> aspas vira conta — veremos isso no Módulo 2.)

> **Experimente também:** digite só `2 + 2` (sem `print`) no modo interativo.
> Repare que ele mostra `4` mesmo sem `print`! Isso só acontece no modo
> interativo, como conveniência. Num arquivo `.py`, sem `print` **nada
> aparece** — é um erro comum de quem está começando.

**Exercício 0:** faça o computador se apresentar — imprima seu nome e a frase
"estou aprendendo Python", em duas linhas separadas, usando dois `print`.

---

## Módulo 1 · Variáveis: guardando informação

Uma **variável** é uma caixa com um nome, onde você guarda um valor para usar
depois. Criar é simples: `nome = valor`.

```python
medicamento = "Amoxicilina"
dose_mg = 500
print(medicamento)
print(dose_mg)
```

Linha por linha:
- `medicamento = "Amoxicilina"` → cria a caixa `medicamento` e coloca o texto dentro.
- `dose_mg = 500` → cria a caixa `dose_mg` com o número 500.
- `print(medicamento)` → mostra o que está na caixa: `Amoxicilina`.
- `print(dose_mg)` → mostra o que está na outra caixa: `500`.

O `=` aqui **não** é "igual" da matemática; ele significa "**guarde isto nesta
caixa**". Pense numa etiqueta colada numa caixa de remédios: a etiqueta
(`medicamento`) não é o remédio, ela só **aponta** para onde o remédio está.

### Você pode trocar o conteúdo

```python
contador = 1
print(contador)      # mostra 1
contador = contador + 1
print(contador)      # mostra 2
```

A linha `contador = contador + 1` lê assim: "pegue o valor atual da caixa, some
1, e guarde de volta na mesma caixa". Isso é tão comum que existe um atalho:

```python
contador = 1
contador += 1   # é o mesmo que: contador = contador + 1
print(contador) # 2
```

Existem atalhos parecidos: `-=` (subtrai e guarda), `*=` (multiplica e
guarda), `/=` (divide e guarda). Todos seguem o mesmo padrão: "faça a conta
com o valor atual e guarde de volta".

### Atribuição múltipla

Você pode criar várias variáveis numa linha só:

```python
nome, idade, febre = "Maria", 30, True
print(nome)    # Maria
print(idade)   # 30
print(febre)   # True
```

Cada valor à direita da vírgula vai para a variável correspondente à esquerda,
na mesma posição. É útil quando os valores estão relacionados (como veremos no
Módulo 8, com tuplas).

### Regras e boas práticas para nomes de variáveis

- Use nomes que **descrevem** o conteúdo: `dose_mg` é melhor que `x`.
- Sem espaços — use `_` para separar palavras: `nome_do_paciente`. Esse
  estilo, com letras minúsculas e `_`, chama-se **snake_case** e é o padrão em
  Python.
- Não pode começar com número: `2dose` ❌, `dose2` ✔️.
- Maiúsculas/minúsculas importam: `Dose` e `dose` são variáveis **diferentes**.
- Por convenção, valores que **nunca devem mudar** durante o programa são
  escritos **TUDO_MAIUSCULO**, para avisar quem lê: "isto é uma constante,
  não reatribua".

**No seu projeto** (`app.py`, perto do topo), há variáveis exatamente assim:
```python
EVIDENCIA_SCORE = {"A": 100, "B": 75, "C": 50, "D": 25}
LINHA_SCORE     = {1: 100, 2: 60, 3: 30}
```
São duas caixas chamadas `EVIDENCIA_SCORE` e `LINHA_SCORE`, escritas em
maiúsculas porque são **constantes** — valores fixos usados em vários lugares
do código, definidos uma única vez no topo. (O conteúdo é um "dicionário" —
chegaremos lá no Módulo 7.)

> **Experimente:** crie a variável `DB_PATH = "database/dados.sqlite"` e
> depois `print(DB_PATH)`. Agora tente `dB_path = "outro valor"` e imprima os
> dois — note que são caixas diferentes, mesmo com nomes parecidos.

**Exercício 1:** crie três variáveis — `nome` (texto), `idade` (número) e
`febre` (verdadeiro/falso) — e imprima as três, cada uma com seu próprio
`print`. Depois, usando `+=`, aumente `idade` em 1 e imprima de novo.

---

## Módulo 2 · Os tipos básicos e conversão entre eles

Todo valor em Python tem um **tipo**. Os quatro mais importantes para começar:

| Tipo | Nome em Python | Exemplo | Para quê |
|------|----------------|---------|----------|
| Texto | `str` | `"Febre"` | palavras, frases |
| Inteiro | `int` | `38` | contar, idade, quantidade |
| Decimal | `float` | `38.5` | medidas, temperatura |
| Lógico | `bool` | `True` / `False` | sim/não, ligado/desligado |

Você pode perguntar o tipo de qualquer valor com `type(...)`:

```python
print(type("Febre"))   # <class 'str'>
print(type(38))        # <class 'int'>
print(type(38.5))      # <class 'float'>
print(type(True))      # <class 'bool'>
```

`<class 'str'>` é só o jeito do Python dizer "isto é da classe/tipo `str`".
Vamos falar de "classe" de verdade no Módulo 15 — por enquanto, leia
`<class 'X'>` como "o tipo é X".

### Cuidado: número com aspas vira texto!

```python
a = 10
b = "10"
print(a + 5)    # 15  (conta de verdade)
print(b + "5")  # 105 (juntou os textos, não somou!)
```

Esse é um dos erros mais comuns de quem começa. `"10"` é o **texto** "um-zero",
não o número dez. O `+` entre dois textos **gruda** um no outro (veremos isso
melhor no Módulo 3).

> **Experimente:** rode `print("10" + 5)`. Vai dar erro, porque o Python não
> sabe somar texto com número. Leia a mensagem — ela diz exatamente
> `TypeError: can only concatenate str (not "int") to str`, ou seja "só posso
> grudar texto com texto, não com inteiro".

### Convertendo entre tipos

Quando você precisa de fato transformar um tipo no outro, existem três
"funções conversoras" que valem a pena memorizar:

```python
texto_numero = "10"
numero = int(texto_numero)        # "10" -> 10  (texto vira inteiro)
print(numero + 5)                 # 15

idade = 30
texto_idade = str(idade)          # 30 -> "30" (número vira texto)
print("Idade: " + texto_idade)    # Idade: 30

preco_texto = "4.50"
preco = float(preco_texto)        # "4.50" -> 4.5 (texto vira decimal)
print(preco * 2)                  # 9.0
```

- `int(...)` converte para inteiro (cuidado: `int("4.5")` dá erro — texto com
  ponto decimal precisa virar `float` primeiro).
- `float(...)` converte para decimal.
- `str(...)` converte qualquer coisa para texto — é o inverso de `int`/`float`
  e é a forma mais comum de "preparar" um número para grudar com `+` num
  texto (embora f-strings, no Módulo 3, sejam melhores para isso).

Essas conversões aparecem o tempo todo quando dados vêm de fora do programa —
por exemplo, de um formulário web ou da URL de uma API — porque **tudo que
chega de fora chega como texto**. O FastAPI do seu projeto faz boa parte dessa
conversão sozinho (veremos no Módulo 20), mas é importante entender o que
acontece por baixo dos panos.

**Exercício 2:** crie uma variável `temperatura_texto = "38.5"` (como se
tivesse vindo de um formulário). Converta para `float`, some `0.2` a ela
(simulando uma correção do termômetro) e imprima o resultado com
`type()` para confirmar que ainda é `float`.

---

## Módulo 3 · Texto (strings) em detalhe

Texto (`str`) é o tipo que você mais vai usar — nomes de pacientes,
medicamentos, mensagens de erro, trechos de SQL. Vamos explorá-lo a fundo.

### Juntando textos

```python
primeiro = "Strepto"
segundo = "coccus"
nome = primeiro + segundo
print(nome)    # Streptococcus
```
O `+` entre textos **gruda** um no outro (chamamos isso de "concatenar"). Note
que não há espaço automático — se você quiser um espaço, precisa colocar você
mesmo: `primeiro + " " + segundo`.

### f-strings: o jeito moderno de montar texto

Colocar um `f` antes das aspas permite inserir variáveis dentro do texto, usando
chaves `{ }`:

```python
medicamento = "Amoxicilina"
dose = 500
frase = f"{medicamento} {dose} mg de 8 em 8 horas"
print(frase)    # Amoxicilina 500 mg de 8 em 8 horas
```
Tudo que está dentro de `{ }` é **substituído pelo valor da variável**. É muito
mais limpo do que ficar usando `+` e `str(...)` em vários pedaços.

Você pode até colocar **contas** dentro das chaves:
```python
dose_unica = 250
vezes_por_dia = 3
print(f"Total no dia: {dose_unica * vezes_por_dia} mg")
# Total no dia: 750 mg
```

E pode formatar números — por exemplo, controlar quantas casas decimais
aparecem, com `:`:
```python
eficacia = 87.6543
print(f"Eficácia: {eficacia:.1f}%")   # Eficácia: 87.7%
print(f"Eficácia: {eficacia:.0f}%")   # Eficácia: 88%
```
`:.1f` significa "mostre como decimal (`f` de *float*) com **1** casa depois
da vírgula". É outra forma de fazer o que `round()` faz (Módulo 4), só que na
hora de exibir o texto.

**No seu projeto** (`app.py`, função `_categorias`):
```python
key = f"{cfg.route}:categorias"
```
Se `cfg.route` for `"bacterias"`, essa linha cria o texto `"bacterias:categorias"`,
usado como "etiqueta" no cache (`_cache`).

### Ferramentas embutidas no texto (métodos)

Todo texto sabe fazer algumas coisas sozinho — chamamos essas habilidades de
**métodos**, e você as usa com um ponto (`.`) depois da variável:

```python
nome = "ampicilina"
print(nome.upper())        # AMPICILINA (tudo maiúsculo)
print(nome.lower())         # ampicilina (tudo minúsculo)
print(nome.capitalize())   # Ampicilina (primeira maiúscula)
print(len(nome))           # 10 (quantas letras tem)
print("cilina" in nome)    # True ("cilina" está dentro de "ampicilina"?)
```

Mais alguns métodos muito úteis no dia a dia:

```python
frase = "  febre alta  "
print(frase.strip())              # "febre alta" (remove espaços das pontas)
print(frase.strip().split(" "))   # ['febre', 'alta'] (quebra em lista por espaço)

partes = ["Amoxicilina", "500mg", "8/8h"]
print(" - ".join(partes))         # Amoxicilina - 500mg - 8/8h (junta com separador)

texto = "Febre + Tosse + Calafrios"
print(texto.replace("Febre", "Cefaleia"))
# Cefaleia + Tosse + Calafrios
```

- `.strip()` tira espaços (ou quebras de linha) do começo e do fim — muito
  usado para "limpar" texto que veio de um formulário.
- `.split(separador)` quebra um texto **em uma lista**, dividindo onde
  encontra o separador.
- `separador.join(lista)` faz o **caminho inverso**: junta os itens de uma
  lista num texto só, com o separador entre eles.
- `.replace(antigo, novo)` troca todas as ocorrências de um trecho por outro.

**No seu projeto** (`static/patologias.html`, no JavaScript que monta a tela
de tratamento combinado), existe uma lógica equivalente para separar os nomes
dos medicamentos de uma combinação:
```javascript
const _combDrugs = _combStr.split(/\s*\+\s*/).map(d => d.trim());
```
Embora seja JavaScript (não Python), a ideia é **idêntica** ao `.split()` e
`.strip()` que você acabou de aprender: quebrar um texto como
`"Amoxicilina + Ácido clavulânico"` numa lista `["Amoxicilina", "Ácido clavulânico"]`,
removendo espaços extras de cada pedaço.

### Fatiamento (slicing): pegando "pedaços" de um texto

Cada caractere de um texto tem uma posição (índice), começando do **zero**.
Você pode pegar um pedaço com `texto[início:fim]`:

```python
cid = "A41.9"
print(cid[0])     # A   (primeiro caractere)
print(cid[0:3])   # A41 (do índice 0 até o 3, sem incluir o 3)
print(cid[-1])    # 9   (último caractere, contando de trás)
print(cid[:1])    # A   (do começo até o índice 1)
print(cid[1:])    # 41.9 (do índice 1 até o fim)
```

Pense no fatiamento como "corte aqui e aqui": `texto[a:b]` pega tudo **a
partir** da posição `a` **até, mas sem incluir**, a posição `b`. Se omitir um
dos lados, o Python assume "desde o começo" ou "até o fim".

> **Experimente:** crie `frase = "febre alta"` e descubra o tamanho com
> `len(frase)`. Conte: o espaço também conta como caractere? Depois teste
> `frase[0:5]` e `frase[6:]` — o que cada um retorna?

**Exercício 3:** com `medicamento = "Azitromicina"` e `dose = 500`, monte com
uma f-string a frase `"Azitromicina: tomar 500 mg no primeiro dia"`. Depois,
usando `.split()`, separe a frase
`"Amoxicilina + Ácido clavulânico"` em uma lista de dois medicamentos.

---

## Módulo 4 · Números e contas

Python faz contas direto, sem precisar de calculadora externa:

```python
print(10 + 3)    # 13  (soma)
print(10 - 3)    # 7   (subtração)
print(10 * 3)    # 30  (multiplicação — usa asterisco)
print(10 / 3)    # 3.333... (divisão — sempre vira decimal)
print(10 // 3)   # 3   (divisão inteira — só a parte inteira, descarta o resto)
print(10 % 3)    # 1   (resto da divisão — "módulo")
print(2 ** 3)    # 8   (potência: 2 elevado a 3)
```

`//` e `%` costumam confundir no início. Pense numa divisão de padaria: 10
pães para 3 pessoas. `10 // 3 = 3` (cada um leva 3 pães inteiros) e
`10 % 3 = 1` (sobra 1 pão). Os dois números juntos descrevem a divisão
completa.

### Ordem das operações (precedência)

Assim como na matemática da escola, multiplicação e divisão acontecem **antes**
de soma e subtração, e parênteses mandam:

```python
print(2 + 3 * 4)      # 14 (multiplica primeiro: 2 + 12)
print((2 + 3) * 4)    # 20 (parênteses primeiro: 5 * 4)
```
Na dúvida, **use parênteses** — eles deixam a intenção clara para quem lê (e
para você mesmo, daqui a um mês).

### Misturando com variáveis

```python
dose_unica = 250
vezes_por_dia = 3
total_dia = dose_unica * vezes_por_dia
print(f"Total no dia: {total_dia} mg")   # Total no dia: 750 mg
```

### Funções prontas para números

```python
valores = [12.3, 45.6, 7.8]
print(min(valores))   # 7.8  (o menor)
print(max(valores))   # 45.6 (o maior)
print(sum(valores))   # 65.7 (a soma de tudo)
print(abs(-5))        # 5   (valor absoluto, sem sinal)
```

### Arredondar

```python
resistencia = 12.3456
print(round(resistencia, 1))   # 12.3 (arredonda para 1 casa decimal)
print(round(resistencia))      # 12   (sem casas, vira inteiro arredondado)
```

**No seu projeto** (`app.py`, dentro da função `_agent_detalhe`, na parte que
prepara dados para o gráfico), há exatamente isso:
```python
"eficacia": round(r["eficacia_pct"] or 0, 1)
```
Pega a eficácia de um medicamento (um número que vem do banco de dados,
podendo ser `None`) e arredonda para 1 casa decimal antes de mandar para o
gráfico do front-end. O `or 0` garante que, se o valor for `None`/vazio, ele
vire `0` antes do `round` — vamos entender esse truque do `or` no Módulo 10.

> **Experimente:** calcule quantos comprimidos de 500mg são necessários para
> uma dose de 1750mg, usando `//` e `%` para saber quantos comprimidos
> inteiros e qual o resto: `1750 // 500` e `1750 % 500`.

**Exercício 4:** um medicamento custa R$ 4,50 por comprimido e o tratamento usa
21 comprimidos. Calcule e imprima o custo total com uma f-string, mostrando o
valor com **2 casas decimais** (dica: `{valor:.2f}`).

---

## Módulo 5 · Verdadeiro ou falso (booleanos)

`bool` só tem dois valores: `True` (verdadeiro) e `False` (falso). Eles nascem
de **comparações**:

```python
idade = 70
print(idade > 65)    # True  (maior que)
print(idade < 18)    # False (menor que)
print(idade >= 65)   # True  (maior OU igual)
print(idade <= 18)   # False (menor OU igual)
print(idade == 70)   # True  (igual? — note os DOIS sinais de igual)
print(idade != 70)   # False (diferente?)
```

> ⚠️ **Atenção:** comparar usa `==` (dois sinais). Um sinal só (`=`) é para
> **guardar** numa variável (Módulo 1). Trocar os dois é o erro nº 1 dos
> iniciantes — e o Python às vezes nem avisa, porque `x = 5` é uma instrução
> válida (atribuição), só que faz algo **diferente** de `x == 5`.

### Combinando condições

```python
idade = 70
tem_febre = True
print(idade > 65 and tem_febre)   # True  (precisa que AS DUAS sejam verdadeiras)
print(idade > 80 or tem_febre)    # True  (basta que UMA seja verdadeira)
print(not tem_febre)              # False (inverte: vira o oposto)
```

Pense em `and` como "E" do português, `or` como "OU", e `not` como "negar".
Você pode combinar várias:

```python
idade = 70
peso = 80
tem_febre = True
grupo_risco = (idade >= 65 or peso > 100) and tem_febre
print(grupo_risco)   # True
```
Os parênteses agrupam, igual na matemática: primeiro decide
`(idade >= 65 or peso > 100)` (que dá `True`), depois faz `True and tem_febre`
(que também dá `True`).

### "Vazio conta como falso" (truthiness)

Em Python, em testes de `if`/`and`/`or`, alguns valores **se comportam como**
`False` mesmo sem serem exatamente `False`:

| Valor | Considerado... |
|-------|-----------------|
| `False` | falso |
| `0` (e `0.0`) | falso |
| `""` (texto vazio) | falso |
| `[]` (lista vazia) | falso |
| `{}` (dicionário vazio) | falso |
| `None` (ausência de valor) | falso |
| qualquer outra coisa | verdadeiro |

```python
nome = ""
print(bool(nome))   # False (texto vazio é "falso")

sintomas = []
print(bool(sintomas))   # False (lista vazia é "falso")

sintomas = ["febre"]
print(bool(sintomas))   # True  (lista com algo é "verdadeiro")
```

Isso permite escrever testes curtos e muito comuns em Python:
```python
pat = None
if not pat:
    print("Não encontrei a patologia")
```
Aqui `not pat` é `True` porque `pat` é `None` (que conta como falso), e
`not False` é `True`.

**No seu projeto** (`app.py`, função `_fetch_patologia`) é exatamente isto:
```python
if not pat:
    raise HTTPException(404, "Patologia não encontrada")
```
"Se a busca no banco não encontrou nada (`pat` é `None`), avise o navegador
com erro 404 (não encontrado)."

**Exercício 5:** crie `temperatura = 38.5` e imprima se há febre (temperatura
maior ou igual a 37.8) usando uma comparação. Depois crie `lista_vazia = []` e
`lista_cheia = ["febre"]`, e imprima `bool(...)` de cada uma para confirmar a
tabela acima.

---
---

# PARTE 2 — Guardando muitas coisas

Até agora cada caixa guardava **um** valor. Mas e quando você tem uma lista de
sintomas, ou vários dados de uma patologia? Para isso existem as **coleções**:
listas, dicionários, tuplas e conjuntos. Esta parte é especialmente importante
para o seu projeto, porque **toda resposta da sua API é uma coleção** (uma
lista de patologias, um dicionário com os detalhes de uma).

## Módulo 6 · Listas

Uma **lista** guarda vários valores em ordem, dentro de colchetes `[ ]`:

```python
sintomas = ["febre", "tosse", "dor de cabeça"]
print(sintomas)        # ['febre', 'tosse', 'dor de cabeça']
print(len(sintomas))   # 3 (quantos itens tem)
```

Uma lista pode guardar qualquer tipo, inclusive **misturado**:
```python
mistura = ["Amoxicilina", 500, True, 4.5]
```
Mas, na prática, listas geralmente guardam itens do **mesmo tipo** ou da
mesma "forma" — por exemplo, uma lista de dicionários, todos com as mesmas
chaves (veremos isso já no Módulo 7).

### Acessando itens pela posição (índice)

A contagem **começa do zero**. O primeiro item é a posição 0:

```python
sintomas = ["febre", "tosse", "dor de cabeça"]
print(sintomas[0])    # febre        (primeiro)
print(sintomas[1])    # tosse        (segundo)
print(sintomas[-1])   # dor de cabeça (o último, contando de trás)
print(sintomas[-2])   # tosse        (penúltimo)
```

### Fatiamento de listas (igual ao de strings)

O mesmo `[início:fim]` que você viu no Módulo 3 funciona em listas:

```python
medicamentos = ["Amoxicilina", "Azitromicina", "Cefalexina", "Doxiciclina"]
print(medicamentos[0:2])   # ['Amoxicilina', 'Azitromicina']
print(medicamentos[2:])    # ['Cefalexina', 'Doxiciclina']
print(medicamentos[:2])    # ['Amoxicilina', 'Azitromicina']
```

**No seu projeto** (`app.py`, função `cronicas_detalhe`), há algo do tipo:
```python
top3_medicamentos = medicamentos_ordenados[:3]
```
"Pegue os 3 primeiros itens da lista já ordenada" — fatiamento puro, sem
precisar de loop.

### Mudando e adicionando

```python
sintomas = ["febre", "tosse"]
sintomas.append("calafrios")   # adiciona no fim
print(sintomas)                # ['febre', 'tosse', 'calafrios']

sintomas[0] = "febre alta"     # troca o primeiro pelo índice
print(sintomas)                # ['febre alta', 'tosse', 'calafrios']

sintomas.remove("tosse")       # remove pelo VALOR
print(sintomas)                # ['febre alta', 'calafrios']

ultimo = sintomas.pop()        # remove e DEVOLVE o último item
print(ultimo)                  # calafrios
print(sintomas)                # ['febre alta']
```

- `.append(item)` adiciona um item no final.
- `lista[i] = novo_valor` troca o item naquela posição.
- `.remove(valor)` apaga a **primeira ocorrência** desse valor (erro se não existir).
- `.pop()` remove o último item **e devolve** o valor removido (útil quando
  você precisa usar o item removido).

### Ordenando

```python
doses = [500, 250, 875, 125]
doses_ordenadas = sorted(doses)
print(doses_ordenadas)          # [125, 250, 500, 875]
print(doses)                    # [500, 250, 875, 125] (original não muda)

doses.sort()                    # ordena A LISTA ORIGINAL, sem criar outra
print(doses)                    # [125, 250, 500, 875]

doses.sort(reverse=True)
print(doses)                    # [875, 500, 250, 125] (decrescente)
```

A diferença entre `sorted(lista)` e `lista.sort()` é importante: `sorted`
**cria uma lista nova** ordenada e deixa a original intacta; `.sort()`
**modifica a lista original** e não devolve nada útil. Em geral, prefira
`sorted(...)` quando ainda for usar a lista original em outro lugar.

Você também pode ordenar por um **critério customizado**, com `key=`:
```python
medicamentos = [
    {"nome": "Amoxicilina", "eficacia": 87.6},
    {"nome": "Azitromicina", "eficacia": 92.1},
    {"nome": "Doxiciclina", "eficacia": 78.4},
]
ordenado = sorted(medicamentos, key=lambda m: m["eficacia"], reverse=True)
print(ordenado[0]["nome"])   # Azitromicina (o de maior eficácia)
```
`lambda m: m["eficacia"]` é uma **função sem nome** (uma "função de uma linha
só") que diz: "para ordenar, olhe o campo `eficacia` de cada item". Não se
preocupe em escrever isso ainda — saber **ler** já ajuda bastante, porque essa
construção aparece em vários projetos Python.

**No seu projeto:** quando a API responde com a lista de sintomas de uma
patologia, é exatamente uma lista assim — só que cada item é um dicionário (o
próximo módulo). E no Módulo 11 vamos ver como percorrer listas com `for`.

> **Experimente:** crie uma lista `doses = [250, 500, 875]` e imprima o item do
> meio. Qual índice é o do meio? Depois experimente `doses[::-1]` — o que esse
> fatiamento "estranho" (com dois dois-pontos) faz? (Dica: ele inverte a lista.)

**Exercício 6:** crie uma lista com 3 medicamentos, adicione um quarto com
`.append()`, ordene em ordem alfabética com `sorted()`, e imprima o tamanho
final da lista com `len()`.

---

## Módulo 7 · Dicionários (o tipo mais importante do seu projeto)

Numa lista, você acessa pela **posição** (0, 1, 2...). Num **dicionário**, você
acessa por um **nome** (a "chave"). Ele guarda pares **chave → valor**, entre
chaves `{ }`:

```python
patologia = {
    "nome": "Pneumonia",
    "cid10": "J18",
    "notificacao": False,
}
print(patologia["nome"])    # Pneumonia
print(patologia["cid10"])   # J18
```

Pense num dicionário de verdade: você procura pela **palavra** (chave) e acha o
**significado** (valor). Aqui, procura por `"nome"` e acha `"Pneumonia"`.

### Adicionando e mudando

```python
patologia = {"nome": "Pneumonia"}
patologia["mortalidade"] = 12      # adiciona uma chave nova
patologia["nome"] = "Pneumonia bacteriana"  # muda uma existente
print(patologia)
# {'nome': 'Pneumonia bacteriana', 'mortalidade': 12}
```

### Percorrendo um dicionário: `.keys()`, `.values()`, `.items()`

```python
patologia = {"nome": "Pneumonia", "cid10": "J18", "mortalidade": 12}

print(patologia.keys())     # dict_keys(['nome', 'cid10', 'mortalidade'])
print(patologia.values())   # dict_values(['Pneumonia', 'J18', 12])

for chave, valor in patologia.items():
    print(f"{chave} -> {valor}")
# nome -> Pneumonia
# cid10 -> J18
# mortalidade -> 12
```
`.items()` devolve cada par chave-valor, e o `for chave, valor in ...`
"desempacota" cada par em duas variáveis de uma vez — vamos ver desempacotamento
com mais calma no Módulo 8. Por enquanto, fica a ideia: `.items()` é a forma
padrão de **percorrer** um dicionário.

### Dicionários dentro de dicionários (aninhados)

Dados do mundo real raramente são planos. Veja como uma resposta da sua API
realmente se parece (simplificada):

```python
patologia = {
    "id": 1,
    "nome": "Pneumonia Comunitária",
    "categoria": {
        "nome": "Respiratório",
        "sistema": "Pulmonar",
    },
    "sintomas": [
        {"nome": "febre", "frequencia": "muito comum"},
        {"nome": "tosse", "frequencia": "comum"},
    ],
}

print(patologia["categoria"]["sistema"])     # Pulmonar
print(patologia["sintomas"][0]["nome"])      # febre
```
Para chegar em `"Pulmonar"`, você "desce" um nível de cada vez:
`patologia` → `["categoria"]` (um dicionário) → `["sistema"]` (o texto).
Para chegar em `"febre"`: `patologia` → `["sintomas"]` (uma lista) →
`[0]` (o primeiro item, um dicionário) → `["nome"]` (o texto). Essa mistura de
listas e dicionários, uns dentro dos outros, é **exatamente** o formato JSON
que sua API devolve (Módulo 19) e o formato que o front-end consome.

### O `.get()` — acesso seguro

Se você pedir uma chave que não existe com `[ ]`, o programa **quebra** com
`KeyError`. O `.get()` evita isso, devolvendo um padrão:

```python
patologia = {"nome": "Pneumonia"}
print(patologia.get("cid10"))          # None (não existe, mas não quebra)
print(patologia.get("cid10", "sem"))   # sem  (devolve "sem" como padrão)
```

**No seu projeto** isso aparece o tempo todo. Em `app.py`:
```python
EVIDENCIA_SCORE.get(tratamento["nivel_evidencia"] or "D", 25)
```
"No dicionário `EVIDENCIA_SCORE`, procure o nível de evidência do tratamento;
se não achar essa chave, use `25` como padrão." E toda resposta da sua API é
um dicionário gigante (geralmente com listas e outros dicionários dentro) —
abra o `app.py` e procure por `result = {` para ver um sendo montado.

### Compreensão de dicionário (prévia)

Assim como existe um atalho para criar listas (Módulo 12), existe um para
criar dicionários a partir de outra coleção:

```python
medicamentos = ["Amoxicilina", "Azitromicina", "Cefalexina"]
tamanhos = {nome: len(nome) for nome in medicamentos}
print(tamanhos)
# {'Amoxicilina': 12, 'Azitromicina': 13, 'Cefalexina': 11}
```
Leia: "para cada `nome` em `medicamentos`, crie uma chave `nome` com valor
`len(nome)`". Vamos voltar a isso no Módulo 12, com mais exemplos do projeto.

> **Experimente:** crie o dicionário `medicamento = {"nome": "Amoxicilina",
> "sus": True}` e imprima só se ele está disponível no SUS. Depois adicione a
> chave `"dose_mg": 500` e imprima o dicionário inteiro.

**Exercício 7:** crie um dicionário representando um medicamento com as chaves
`nome`, `dose_mg` e `disponivel_sus`. Depois imprima a frase
`"Amoxicilina — 500 mg"` usando uma f-string que pega os valores do dicionário.
Por fim, use `.get("posologia", "não informada")` para um campo que **não
existe** no dicionário, e confirme que não dá erro.

---

## Módulo 8 · Tuplas e desempacotamento

Uma **tupla** é como uma lista, mas com parênteses `( )` e com uma diferença
fundamental: **não pode ser mudada** depois de criada (dizemos que é
"imutável"). Serve para dados fixos, que representam um "pacote" de
informação que sempre anda junto.

```python
cores_do_gram = ("positivo", "negativo")
print(cores_do_gram[0])    # positivo

cores_do_gram[0] = "outro"  # ❌ ERRO: TypeError: 'tuple' object does not support item assignment
```

Quando usar tupla em vez de lista? Quando os itens **não devem mudar** —
isso deixa o código mais seguro (o Python literalmente impede a alteração
acidental) e deixa claro para quem lê: "isto é fixo, faz parte da definição".

**No seu projeto** (`app.py`, na configuração `AGENT_DOMAINS`):
```python
agent_cols=("nome_cientifico", "nome_comum", "gram",
            "aerobiose", "formato", "resistencia_natural"),
```
As colunas que o sistema lê do banco são uma tupla, porque essa lista é fixa —
não deve ser alterada enquanto o programa roda. Se alguém tentasse fazer
`cfg.agent_cols.append("outra_coluna")`, o Python recusaria.

### Desempacotamento (unpacking)

Você já viu uma forma disso no Módulo 1 (`nome, idade, febre = "Maria", 30,
True`). Isso funciona porque, na verdade, `"Maria", 30, True` **é uma tupla**
— em Python, vírgulas sem colchetes/chaves já criam uma tupla.

O desempacotamento é especialmente útil em loops, quando cada item é uma
tupla de tamanho fixo:

```python
pares = [("Amoxicilina", 500), ("Azitromicina", 250), ("Cefalexina", 1000)]

for nome, dose in pares:
    print(f"{nome}: {dose} mg")
# Amoxicilina: 500 mg
# Azitromicina: 250 mg
# Cefalexina: 1000 mg
```
Cada item de `pares` é uma tupla `(nome_do_medicamento, dose)`. O `for nome,
dose in pares` "abre" cada tupla automaticamente nas duas variáveis. É
exatamente o mesmo mecanismo usado em `for chave, valor in dicionario.items()`
do Módulo 7.

### Funções que devolvem várias coisas (prévia do Módulo 13)

Tuplas também aparecem quando uma função quer devolver **mais de um valor**
de uma vez:

```python
def estatisticas(numeros):
    return min(numeros), max(numeros), sum(numeros)

menor, maior, total = estatisticas([10, 20, 30])
print(menor, maior, total)   # 10 30 60
```
`return min(numeros), max(numeros), sum(numeros)` na verdade devolve **uma
tupla** `(10, 30, 60)`, que é desempacotada nas três variáveis à esquerda.

**No seu projeto** (`app.py`, função `_fetch_clinical`), o `return` final é
exatamente assim:
```python
return (
    [dict(s) for s in sintomas],
    [dict(c) for c in criterios],
    [dict(e) for e in escores],
)
```
É uma tupla com **três listas** dentro. Quem chama essa função faz:
```python
sintomas, criterios, escores = _fetch_clinical(db, patologia_id)
```
e recebe as três listas já separadas em três variáveis.

**Exercício 8:** crie uma tupla com os dias da semana e imprima o primeiro e o
último usando índices. Depois crie uma lista de tuplas
`[("febre", "muito comum"), ("tosse", "comum")]` e percorra com
`for nome, frequencia in ...`, imprimindo `f"{nome}: {frequencia}"`.

---

## Módulo 9 · Conjuntos (sets)

Um **conjunto** (`set`) é parecido com uma lista, mas com duas diferenças
importantes: **não tem ordem** e **não permite valores repetidos**. Cria-se
com chaves `{ }` (sem pares chave-valor, senão vira dicionário) ou com
`set(...)`:

```python
sistemas = {"Respiratório", "Digestivo", "Respiratório", "Neurológico"}
print(sistemas)         # {'Respiratório', 'Digestivo', 'Neurológico'} (sem repetir!)
print(len(sistemas))    # 3
```

Repare que `"Respiratório"` apareceu duas vezes na hora de criar, mas o
conjunto guardou só uma — essa é a principal utilidade de um `set`: **remover
duplicatas automaticamente**.

### Convertendo lista em conjunto (e de volta)

```python
categorias_repetidas = ["Respiratório", "Digestivo", "Respiratório", "Neurológico", "Digestivo"]
unicas = set(categorias_repetidas)
print(unicas)            # {'Respiratório', 'Digestivo', 'Neurológico'}

lista_unica = list(unicas)
print(sorted(lista_unica))  # ['Digestivo', 'Neurológico', 'Respiratório'] (ordenado para exibir)
```
Esse padrão — `list(set(lista))` — é uma forma rápida e comum de "tirar
duplicatas" de uma lista. Note que precisamos de `sorted(...)` no final porque
conjuntos **não garantem ordem**; se a ordem importa para exibir, ordene
depois de remover duplicatas.

### Testando se um item está no conjunto

```python
gram_validos = {"positivo", "negativo", "indeterminado"}
print("positivo" in gram_validos)    # True
print("amarelo" in gram_validos)     # False
```
A operação `in` funciona em listas, tuplas e dicionários também — mas em
conjuntos ela é **muito mais rápida** quando há muitos itens, porque o Python
usa uma estrutura interna otimizada para busca. Para o tamanho dos dados do
seu projeto (centenas de itens) a diferença é imperceptível, mas é bom saber
que essa é uma das razões para escolher `set` em projetos maiores.

**No seu projeto**, embora `app.py` não use `set` diretamente hoje, a query
SQL `SELECT DISTINCT ...` (que aparece em `_categorias` e `_patologias`) faz
exatamente o papel de um conjunto: "traga estes valores, mas sem repetir".
`DISTINCT` é o "set" do mundo SQL.

> **Experimente:** crie duas listas de sintomas com alguns nomes repetidos
> entre elas, transforme cada uma em `set`, e teste o operador `&`
> (interseção): `set_a & set_b` mostra os sintomas que aparecem **nas duas**
> listas.

**Exercício 9:** dada a lista
`tipos = ["bacteriana", "viral", "fungica", "bacteriana", "parasitaria", "viral"]`,
use `set()` para descobrir quantos **tipos diferentes** existem, sem contar
repetições.

---
---

# PARTE 3 — Tomando decisões e repetindo

## Módulo 10 · `if`, `elif`, `else` e o operador ternário

Um programa precisa **decidir** o caminho. É o `if` ("se"):

```python
temperatura = 38.5

if temperatura >= 37.8:
    print("Tem febre")
else:
    print("Sem febre")
```

Detalhes que importam muito em Python:
- Depois da condição vem **dois pontos** `:`.
- A linha de dentro é **indentada** (4 espaços, ou um `Tab` configurado para 4
  espaços). Essa indentação **não é enfeite** — é ela que diz o que está
  "dentro" do `if`. Em Python, espaço tem significado!
- `else` é opcional: se você só quer fazer algo **quando** a condição é
  verdadeira, e nada caso contrário, pode omitir o `else`.

### Mais de duas opções: `elif`

```python
nivel = "B"

if nivel == "A":
    print("Evidência forte")
elif nivel == "B":
    print("Evidência moderada")
elif nivel == "C":
    print("Evidência limitada")
else:
    print("Evidência fraca ou consenso de especialistas")
```

`elif` é "senão, se...". O Python testa **de cima para baixo** e para no
primeiro que for verdadeiro — os de baixo nem são avaliados. Por isso a ordem
importa: coloque as condições mais específicas primeiro.

### `if` dentro de `if` (aninhamento)

Você pode colocar um `if` dentro de outro, indentando mais uma vez:

```python
idade = 70
tem_comorbidade = True

if idade >= 65:
    if tem_comorbidade:
        print("Grupo de altíssimo risco")
    else:
        print("Grupo de risco (idade)")
else:
    print("Risco padrão")
```

Isso funciona, mas fica difícil de ler quando há muitos níveis. Quase sempre
dá para reescrever combinando condições com `and`/`or` (Módulo 5):

```python
if idade >= 65 and tem_comorbidade:
    print("Grupo de altíssimo risco")
elif idade >= 65:
    print("Grupo de risco (idade)")
else:
    print("Risco padrão")
```
Como regra geral: se você se pegar com 3+ níveis de `if` aninhado, é um sinal
para tentar simplificar — seja combinando condições, seja extraindo para uma
função (Módulo 13).

### O operador ternário: `if`/`else` numa linha só

Quando a única coisa que muda é **qual valor usar**, existe uma forma curta:

```python
idade = 70
categoria = "idoso" if idade >= 65 else "adulto"
print(categoria)   # idoso
```

Leia da esquerda para a direita: "`categoria` recebe `'idoso'` **se**
`idade >= 65`, **senão** recebe `'adulto'`". É equivalente a:
```python
if idade >= 65:
    categoria = "idoso"
else:
    categoria = "adulto"
```
mas em uma linha. Use o ternário para escolhas **simples e curtas** — para
lógica mais complexa, o `if`/`else` tradicional é mais legível.

### O conceito de "vazio = falso" revisitado, e o truque do `or`

Relembrando o Módulo 5: `None`, `0`, `""` e `[]` contam como falso. Isso
permite escrever de forma curta:

```python
pat = None
if not pat:
    print("Não encontrei a patologia")
```

**No seu projeto** (`app.py`, função `_fetch_patologia`) é exatamente isto:
```python
if not pat:
    raise HTTPException(404, "Patologia não encontrada")
```

E o **truque do `or`** como valor padrão:
```python
nivel = None
nivel_final = nivel or "D"
print(nivel_final)    # D
```
Leia: "use `nivel`; mas **se ele for vazio/None** (ou seja, "falso"), use
`'D'` no lugar". O Python avalia `nivel or "D"` da esquerda para a direita: se
`nivel` já for "verdadeiro" (um texto não-vazio, por exemplo), o resultado é o
próprio `nivel` e `"D"` nem é considerado. Seu projeto usa isso para nunca
trabalhar com um valor faltando — por exemplo, em
`EVIDENCIA_SCORE.get(tratamento["nivel_evidencia"] or "D", 25)`, se
`nivel_evidencia` vier `None` do banco, ele vira `"D"` antes mesmo de
consultar o dicionário.

**Exercício 10:** crie `idade = 70` e imprima `"idoso"` se for 65 ou mais,
senão `"adulto"`, **de duas formas**: primeiro com `if`/`else` tradicional,
depois reescrevendo com o operador ternário numa linha só.

---

## Módulo 11 · Loops (`for`, `while`, `break`, `continue`)

### `for`: repetir para cada item

Quando você quer fazer algo **para cada item** de uma coleção, usa o `for`:

```python
sintomas = ["febre", "tosse", "calafrios"]

for s in sintomas:
    print(f"Sintoma: {s}")
```
Resultado:
```
Sintoma: febre
Sintoma: tosse
Sintoma: calafrios
```

Leia assim: "**para cada** item `s` **em** `sintomas`, faça...". A cada volta, a
variável `s` vira o próximo item. (Note de novo a indentação marcando o que está
"dentro" do loop.)

### Repetir um número de vezes: `range`

```python
for numero in range(3):
    print(numero)    # 0, depois 1, depois 2
```
`range(3)` gera os números 0, 1, 2 (começa do zero, não inclui o 3). Você
também pode dar início e fim: `range(1, 4)` gera 1, 2, 3.

### `enumerate`: pegar o item E a posição

Às vezes você precisa saber **a posição** de um item enquanto percorre uma
lista. Em vez de controlar um contador manualmente, use `enumerate`:

```python
medicamentos = ["Amoxicilina", "Azitromicina", "Cefalexina"]

for posicao, nome in enumerate(medicamentos):
    print(f"{posicao + 1}º lugar: {nome}")
# 1º lugar: Amoxicilina
# 2º lugar: Azitromicina
# 3º lugar: Cefalexina
```
`enumerate(medicamentos)` produz pares `(0, "Amoxicilina")`, `(1,
"Azitromicina")`, etc. — e o `for posicao, nome in ...` desempacota cada par
(igual fizemos no Módulo 8).

### `zip`: percorrer duas listas ao mesmo tempo

```python
nomes = ["Amoxicilina", "Azitromicina", "Cefalexina"]
doses = [500, 250, 1000]

for nome, dose in zip(nomes, doses):
    print(f"{nome}: {dose} mg")
# Amoxicilina: 500 mg
# Azitromicina: 250 mg
# Cefalexina: 1000 mg
```
`zip` "amarra" as duas listas posição a posição, como o zíper de uma jaqueta —
cada volta do loop pega um item de cada lista, na mesma posição.

### Acumulando um resultado

Padrão clássico: começar com uma caixa vazia e ir enchendo:

```python
doses = [250, 500, 875]
total = 0
for d in doses:
    total = total + d
print(total)    # 1625
```

**No seu projeto** (`app.py`, função `cronicas_detalhe`) há esse mesmo padrão:
começa com `top3_medicamentos = []` (lista vazia) e, num loop, vai adicionando
cada medicamento com `.append()`.

### `while`: repetir enquanto uma condição for verdadeira

O `for` repete **um número conhecido de vezes** (uma vez por item). O `while`
repete **enquanto uma condição for verdadeira** — útil quando você não sabe de
antemão quantas voltas serão necessárias:

```python
doses_restantes = 21
dia = 1
while doses_restantes > 0:
    print(f"Dia {dia}: tomar 1 comprimido")
    doses_restantes -= 1   # subtrai 1 a cada volta
    dia += 1
print("Tratamento concluído")
```

Cuidado: se você esquecer de "andar" em direção ao fim (aqui, o
`doses_restantes -= 1`), o `while` **nunca para** — isso é chamado de "loop
infinito" e é um dos bugs mais comuns. Se isso acontecer no terminal, aperte
`Ctrl+C` para interromper.

### `break` e `continue`: controlando o loop por dentro

- `break` **encerra o loop imediatamente**, mesmo que ainda haja itens.
- `continue` **pula para a próxima volta**, ignorando o resto do código
  daquela volta.

```python
medicamentos = ["Amoxicilina", "Azitromicina", "Penicilina G", "Cefalexina"]

for nome in medicamentos:
    if "Penicilina" in nome:
        print(f"Encontrei: {nome}")
        break          # para de procurar, já achei
    print(f"Verificando: {nome}")
```
Saída:
```
Verificando: Amoxicilina
Verificando: Azitromicina
Encontrei: Penicilina G
```
Repare que `"Cefalexina"` **nem é verificado** — o `break` saiu do loop assim
que encontrou o que procurava.

```python
doses = [500, 0, 250, 0, 1000]

for d in doses:
    if d == 0:
        continue        # pula doses zeradas, não soma nem imprime
    print(f"Dose válida: {d} mg")
```
Saída:
```
Dose válida: 500 mg
Dose válida: 250 mg
Dose válida: 1000 mg
```

> **Experimente:** combine `for` com `if`: percorra
> `["A", "B", "C", "D"]` (níveis de evidência) e, usando `EVIDENCIA_SCORE` do
> Módulo 1, imprima `f"{nivel}: {pontuacao} pontos"` para cada um.

**Exercício 11:** dada a lista `notas = ["A", "B", "A", "C"]`, percorra com um
`for` e imprima cada nota com a frase `"Nível de evidência: X"`. Depois, usando
`enumerate`, imprima também a posição (começando em 1): `"1ª: Nível A"`, etc.

---

## Módulo 12 · Compreensões de lista e de dicionário

Esse padrão — criar uma coleção nova a partir de outra — é tão comum que
Python tem um atalho elegante chamado **compreensão**.

### Compreensão de lista

Primeiro o jeito longo, que você já conhece:
```python
doses = [250, 500, 875]
dobro = []
for d in doses:
    dobro.append(d * 2)
print(dobro)    # [500, 1000, 1750]
```

Agora o mesmo, em **uma linha**:
```python
doses = [250, 500, 875]
dobro = [d * 2 for d in doses]
print(dobro)    # [500, 1000, 1750]
```

Leia da esquerda para a direita: "**`d * 2`**, **para cada** `d` **em**
`doses`". O resultado de cada volta vira um item da lista nova.

**No seu projeto** isto aparece dezenas de vezes. Em `app.py`:
```python
[dict(r) for r in rows]
```
Significa: "para cada linha `r` que veio do banco, transforme em dicionário, e
junte tudo numa lista". É assim que os dados crus do banco viram a resposta da
API.

### Com filtro (`if` dentro da compreensão)

Você pode incluir só alguns itens, adicionando um `if` no final:
```python
doses = [250, 500, 875]
grandes = [d for d in doses if d >= 500]
print(grandes)    # [500, 875]
```
Leia: "`d`, para cada `d` em `doses`, **mas só se** `d >= 500`". Os itens que
não passam no `if` simplesmente não entram na lista nova.

### Compreensão de dicionário

O mesmo atalho funciona para criar dicionários, usando `{ }` e
`chave: valor`:

```python
medicamentos = ["Amoxicilina", "Azitromicina", "Cefalexina"]
tamanhos = {nome: len(nome) for nome in medicamentos}
print(tamanhos)
# {'Amoxicilina': 12, 'Azitromicina': 13, 'Cefalexina': 11}
```

E também aceita `if`:
```python
eficacias = {"Amoxicilina": 87.6, "Azitromicina": 65.2, "Cefalexina": 91.0}
boas = {nome: ef for nome, ef in eficacias.items() if ef >= 80}
print(boas)
# {'Amoxicilina': 87.6, 'Cefalexina': 91.0}
```
Aqui percorremos `eficacias.items()` (pares chave-valor, Módulo 7),
desempacotamos em `nome, ef`, e só incluímos no novo dicionário os que têm
eficácia `>= 80`.

### Compreensões aninhadas (com cuidado)

Dá para colocar um `for` dentro de outro, mas isso fica difícil de ler rápido
— use com moderação:

```python
grupos = {
    "primeira_linha": ["Amoxicilina", "Azitromicina"],
    "segunda_linha": ["Doxiciclina"],
}
todos = [med for lista in grupos.values() for med in lista]
print(todos)
# ['Amoxicilina', 'Azitromicina', 'Doxiciclina']
```
Isso "achata" um dicionário de listas numa lista só. Se a leitura ficar
confusa, prefira escrever com `for` tradicional (Módulo 11) — código claro
vale mais que código curto.

**No seu projeto**, a função `_agent_detalhe` usa compreensões para transformar
linhas do banco em listas de dicionários prontas para virar JSON, exatamente
como `[dict(r) for r in rows]` — e usa `defaultdict` (Módulo 18) para os casos
em que precisa **agrupar** itens antes de montar a lista final.

**Exercício 12:** dada `temperaturas = [36.5, 38.2, 37.0, 39.1]`, crie com uma
compreensão a lista só das temperaturas com febre (≥ 37.8). Depois, dado
`medicamentos = ["Amoxicilina", "AAS", "Cefalexina"]`, crie um dicionário
`{nome: "curto" if len(nome) <= 5 else "longo" for ...}` usando o operador
ternário (Módulo 10) **dentro** da compreensão.

---
---

# PARTE 4 — Organizando o código

## Módulo 13 · Funções em profundidade

Uma **função** é um bloco de código com nome, que você pode reusar quantas vezes
quiser. Ela evita repetição — escreva uma vez, use sempre.

```python
def saudacao(nome):
    print(f"Olá, {nome}!")

saudacao("Maria")    # Olá, Maria!
saudacao("João")     # Olá, João!
```

- `def` começa a definição da função.
- `saudacao` é o nome que você escolheu.
- `(nome)` é o **parâmetro**: uma caixa que recebe um valor quando a função é chamada.
- A linha indentada é o que a função **faz**.
- `saudacao("Maria")` é **chamar** a função, passando `"Maria"` para o parâmetro `nome`.

### Funções que devolvem um valor: `return`

Muitas vezes você quer que a função **calcule e entregue** um resultado, em vez
de só imprimir:

```python
def acesso_sus(disponivel):
    if disponivel:
        return 100
    return 0

resultado = acesso_sus(True)
print(resultado)    # 100
```

`return` faz duas coisas: **entrega o valor** e **encerra a função** ali. O valor
entregue pode ser guardado numa variável, como fizemos com `resultado`. Uma
função sem `return` explícito devolve `None` automaticamente.

### Vários parâmetros e valor padrão

```python
def descreve(medicamento, dose=500):   # dose tem um padrão
    return f"{medicamento} {dose} mg"

print(descreve("Amoxicilina"))        # Amoxicilina 500 mg (usou o padrão)
print(descreve("Azitromicina", 250))  # Azitromicina 250 mg (passou outro)
```
Parâmetros com `=valor` são **opcionais** na hora de chamar — se você não
passar nada, o padrão é usado. Parâmetros sem `=` são **obrigatórios**.

> ⚠️ **Pegadinha clássica:** nunca use uma **lista ou dicionário vazio** como
> valor padrão diretamente:
> ```python
> def adiciona_sintoma(sintoma, lista=[]):   # ❌ perigoso!
>     lista.append(sintoma)
>     return lista
> ```
> Em Python, esse `[]` padrão é criado **uma única vez**, na hora em que a
> função é definida — e é **compartilhado** entre todas as chamadas que não
> passam `lista`. O resultado é que sintomas de uma chamada "vazam" para a
> próxima. O jeito correto:
> ```python
> def adiciona_sintoma(sintoma, lista=None):
>     if lista is None:
>         lista = []
>     lista.append(sintoma)
>     return lista
> ```
> Esse é um dos "gotchas" mais famosos de Python — bom conhecer mesmo sem usar
> ainda.

### Argumentos nomeados (keyword arguments)

Você pode chamar uma função citando o **nome do parâmetro**, o que deixa a
chamada mais clara e permite mudar a ordem:

```python
def descreve(medicamento, dose=500, via="oral"):
    return f"{medicamento} {dose} mg, via {via}"

print(descreve("Amoxicilina", via="endovenosa", dose=1000))
# Amoxicilina 1000 mg, via endovenosa
```

**No seu projeto** (`app.py`, classe `AgentDomain`), a criação de cada domínio
usa só argumentos nomeados:
```python
AgentDomain(
    dominio="bacteriana", route="bacterias",
    junction="patologia_bacteria", agent_table="bacterias", agent_fk="bacteria_id",
    ...
)
```
Com tantos parâmetros, nomear cada um deixa claríssimo o que cada valor
representa — sem precisar decorar a ordem.

### `*args` e `**kwargs`: quando o número de argumentos varia

Às vezes uma função precisa aceitar **qualquer quantidade** de argumentos.
`*args` junta argumentos extras numa tupla; `**kwargs` junta argumentos
nomeados extras num dicionário:

```python
def soma_tudo(*numeros):
    return sum(numeros)

print(soma_tudo(1, 2))         # 3
print(soma_tudo(1, 2, 3, 4))   # 10
```

```python
def cria_paciente(**dados):
    return dados

p = cria_paciente(nome="Maria", idade=30, febre=True)
print(p)   # {'nome': 'Maria', 'idade': 30, 'febre': True}
```

**No seu projeto** (`app.py`, classe `AgentDomain`):
```python
class AgentDomain:
    def __init__(self, **kw):
        self.__dict__.update(kw)
```
Aqui, `**kw` recebe **todos** os argumentos nomeados (`dominio=...,
route=..., junction=...`, etc.) como um dicionário chamado `kw`. A linha
`self.__dict__.update(kw)` faz cada chave desse dicionário virar um **campo do
objeto** — é por isso que depois você consegue escrever `cfg.route`,
`cfg.junction`, etc. Vamos entender `self` e objetos no Módulo 15.

### Escopo: onde uma variável "existe"

Variáveis criadas **dentro** de uma função só existem **dentro** dela:

```python
def calcula():
    resultado = 42
    return resultado

calcula()
print(resultado)   # ❌ NameError: name 'resultado' is not defined
```
`resultado` é **local** à função `calcula` — fora dela, essa caixa não existe.
Isso é bom: evita que o código de uma função "bagunce" variáveis de outra
parte do programa por acidente. Cada função tem seu próprio "quarto" de
variáveis.

**No seu projeto** (`app.py`) quase tudo são funções. Veja `_fetch_patologia`:
ela recebe o banco e o id, busca a patologia, e o `return` devolve o resultado.
Foi criada para **não repetir** essa mesma busca em cinco lugares diferentes —
exatamente o propósito de uma função.

**Exercício 13:** escreva uma função `tem_febre(temperatura)` que devolve
`True` se a temperatura for ≥ 37.8, senão `False`. Teste com dois valores.
Depois escreva `classifica_idade(idade, limite=65)` que devolve `"idoso"` se
`idade >= limite`, senão `"adulto"` — e teste chamando com e sem o segundo
argumento.

---

## Módulo 14 · Módulos, pacotes e `import`

Um programa grande não cabe (nem deve caber) num arquivo só. Cada arquivo `.py`
é um **módulo**, e o `import` traz código de um para o outro — ou traz
ferramentas prontas que vêm com o Python (a "biblioteca padrão").

```python
import math                # traz o módulo de matemática
print(math.sqrt(16))       # 4.0 (raiz quadrada)

from datetime import date  # traz só a ferramenta "date"
print(date.today())        # a data de hoje
```

Duas formas:
- `import math` → traz o módulo inteiro; você usa com `math.alguma_coisa`.
- `from datetime import date` → traz **só** a ferramenta `date`, usada direto.

Você também pode dar um **apelido** ao importar, com `as` — útil para nomes
longos ou convenções da comunidade:
```python
import sqlite3 as db_lib
```
(No seu projeto isso não é usado, mas é comum ver `import pandas as pd`,
por exemplo, em outros projetos.)

**No seu projeto** (topo do `app.py`):
```python
import logging
import re
import sqlite3
from collections import defaultdict
from contextlib import contextmanager
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
```
Os primeiros (`logging`, `re`, `sqlite3`, `collections`, `contextlib`,
`pathlib`) vêm **prontos com o Python** (biblioteca padrão). Os últimos três
(`fastapi...`) são **bibliotecas externas**, instaladas via
`pip install -r requirements.txt` — é por isso que `requirements.txt` lista
`fastapi` e `uvicorn`.

### `__name__ == "__main__"`: rodando um arquivo de duas formas

Um arquivo `.py` pode ser **executado diretamente** (`python3 arquivo.py`) ou
**importado** por outro arquivo (`import arquivo`). Às vezes você quer que
algum código rode **só** no primeiro caso (por exemplo, testes rápidos ou um
script de build). O Python guarda essa informação numa variável especial,
`__name__`:

```python
def construir_banco():
    print("Construindo banco de dados...")

if __name__ == "__main__":
    construir_banco()
```
Quando você roda `python3 este_arquivo.py` diretamente, `__name__` vale
`"__main__"`, e `construir_banco()` é chamada. Se outro arquivo fizer
`import este_arquivo`, esse bloco **não roda** — só as definições (`def`)
ficam disponíveis. É assim que `database/build_db.py` consegue ser executado
sozinho (`python database/build_db.py`, como o `railway.toml` faz no deploy)
sem que nada "vaze" se algum dia outro módulo precisar importar funções dele.

### Organizando em pastas: pacotes

Uma pasta com arquivos `.py` relacionados forma um **pacote**. No seu
projeto, a pasta `database/` contém vários módulos de dados (por sistema/área
clínica) que `database/build_db.py` importa para montar o banco SQLite final:

```python
from data_criterios_bacterianas import CRITERIOS_BACTERIANAS
```
Ou seja: o conhecimento médico fica em arquivos separados, organizados por
assunto, e o script de build os reúne num único arquivo `.sqlite` que o
`app.py` consulta em produção. Essa separação (dados vs. lógica do servidor) é
um exemplo de **organização de código** — cada arquivo tem uma responsabilidade
clara.

**Exercício 14:** importe o módulo `random` e use `random.randint(1, 6)` para
"jogar um dado". Rode algumas vezes e veja o número mudar. Depois crie um
arquivo `saudacoes.py` com uma função `ola(nome)`, e em **outro** arquivo
(`teste.py`, na mesma pasta) faça `from saudacoes import ola` e chame `ola("Ian")`.

---

## Módulo 15 · Classes (uma introdução suave)

Às vezes você quer agrupar vários dados relacionados sob um mesmo "molde". Para
isso existe a **classe**. Para um iniciante, a regra é: **você ainda não precisa
escrever classes complexas**, mas precisa saber **ler**.

```python
class Medicamento:
    def __init__(self, nome, dose):
        self.nome = nome
        self.dose = dose

amox = Medicamento("Amoxicilina", 500)
print(amox.nome)    # Amoxicilina
print(amox.dose)    # 500
```

O essencial para ler código:
- `class Medicamento:` cria o molde (também chamado de "classe").
- `def __init__(self, nome, dose):` é um método especial, chamado
  automaticamente **quando um objeto é criado**. `__init__` vem de
  "inicializar".
- `self` é como o objeto se refere **a si mesmo** — é sempre o primeiro
  parâmetro de métodos dentro de uma classe, e o Python o passa
  automaticamente (você não escreve `self` na hora de chamar).
- `self.nome = nome` guarda o valor recebido **no objeto**, como um campo
  chamado `nome`.
- `amox = Medicamento("Amoxicilina", 500)` cria **um objeto** (uma "instância")
  a partir do molde, chamando `__init__` com `nome="Amoxicilina"`,
  `dose=500`.
- `amox.nome` lê um campo desse objeto (com o **ponto**).

### Métodos: funções que pertencem a um objeto

Além de `__init__`, uma classe pode ter outras funções (chamadas **métodos**)
que operam sobre os dados do objeto:

```python
class Medicamento:
    def __init__(self, nome, dose):
        self.nome = nome
        self.dose = dose

    def descricao(self):
        return f"{self.nome} {self.dose} mg"

amox = Medicamento("Amoxicilina", 500)
print(amox.descricao())   # Amoxicilina 500 mg
```
Repare que `descricao` também recebe `self` como primeiro parâmetro — é assim
que ela acessa `self.nome` e `self.dose`, os campos **daquele objeto
específico**. Se você criasse outro objeto, `outro = Medicamento("Cefalexina",
1000)`, então `outro.descricao()` usaria os dados de `outro`, não de `amox`.

### Por que isso importa para o seu projeto

**No seu projeto** (`app.py`) existe uma classe simples chamada `AgentDomain`,
usada para guardar a configuração de cada domínio (bacteriano, viral, etc.):

```python
class AgentDomain:
    def __init__(self, **kw):
        self.__dict__.update(kw)


AGENT_DOMAINS = {
    "bacterias": AgentDomain(
        dominio="bacteriana", route="bacterias",
        junction="patologia_bacteria", agent_table="bacterias", agent_fk="bacteria_id",
        ...
    ),
    "virais": AgentDomain(...),
    "fungicos": AgentDomain(...),
    "parasitos": AgentDomain(...),
}
```

Em vez de ter quatro funções quase idênticas (uma para bactérias, uma para
vírus, etc.), o projeto tem **uma função genérica** (`_agent_detalhe`) que
recebe um objeto `AgentDomain` e lê seus campos com ponto:
`cfg.junction`, `cfg.drug_table`, `cfg.agent_cols`. Sempre que vir
`algumacoisa.outracoisa` no código, pense: "estou pegando um campo (ou
chamando um método) de um objeto". Essa única classe + dicionário substitui o
que antes eram **centenas de linhas duplicadas** — é um ótimo exemplo de como
"organizar dados num molde" reduz repetição.

> **Experimente:** no modo interativo, crie a classe `Medicamento` acima, crie
> dois objetos diferentes, e imprima `tipo(amox) == tipo(outro)` — ambos são
> `Medicamento`, mas são objetos **diferentes**, com dados próprios.

**Exercício 15:** apenas leia, no `app.py`, a classe `AgentDomain` e o
dicionário `AGENT_DOMAINS`. Responda: qual é o valor de `drug_table` no
domínio `"bacterias"`? E qual é o valor de `agent_out_key` no domínio
`"virais"`?

---

## Módulo 16 · Tratamento de erros (`try`/`except`)

Vimos no Módulo 0 que erros mostram uma mensagem e **interrompem o programa**.
Às vezes isso é o comportamento certo (um erro de digitação no código deve
mesmo parar tudo, para você corrigir). Mas às vezes um erro é **esperado** —
por exemplo, "o usuário pediu uma patologia que não existe" — e o programa
deve **lidar com isso de forma controlada**, sem quebrar para o usuário final.

### A estrutura básica

```python
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Não é possível dividir por zero!")
```
Saída:
```
Não é possível dividir por zero!
```
Sem o `try`/`except`, esse mesmo código pararia o programa com
`ZeroDivisionError: division by zero`. Com o `try`/`except`, o erro é
**capturado** e tratado — o programa continua rodando.

Leia assim: "**tente** fazer isto; **mas se** acontecer este tipo específico de
erro, faça aquilo no lugar".

### Capturando tipos diferentes de erro

```python
valores = ["10", "20", "abc", "30"]

for v in valores:
    try:
        numero = int(v)
        print(f"Convertido: {numero}")
    except ValueError:
        print(f"'{v}' não é um número válido — pulando")
```
Saída:
```
Convertido: 10
Convertido: 20
'abc' não é um número válido — pulando
Convertido: 30
```
`int("abc")` levanta `ValueError` (não `ZeroDivisionError`) — cada tipo de
problema tem sua própria classe de erro, e você pode capturar tipos
específicos. Capturar **exatamente** o erro esperado (em vez de "qualquer
erro") é uma boa prática: assim, erros **inesperados** continuam aparecendo
normalmente, ajudando você a encontrá-los.

### `raise`: provocando um erro de propósito

Às vezes a sua própria função detecta que algo está errado e precisa **avisar
quem a chamou**. Para isso, use `raise`:

```python
def calcula_dose(peso_kg):
    if peso_kg <= 0:
        raise ValueError("Peso precisa ser maior que zero")
    return peso_kg * 10

print(calcula_dose(70))    # 700
print(calcula_dose(-5))    # ValueError: Peso precisa ser maior que zero
```

### `HTTPException`: o `raise` do mundo das APIs

**No seu projeto** (`app.py`, função `_fetch_patologia`), em vez de
`ValueError`, usamos uma classe especial do FastAPI:

```python
if not pat:
    raise HTTPException(404, "Patologia não encontrada")
```

`HTTPException` é "um erro que vira uma resposta HTTP" — o FastAPI captura
esse `raise` automaticamente (você não precisa escrever `try`/`except` para
isso) e devolve ao navegador uma resposta com:
- código `404` (o código HTTP que significa "não encontrado" — o mesmo que
  aparece quando você acessa uma página que não existe);
- a mensagem `"Patologia não encontrada"` no corpo da resposta, em JSON.

Ou seja: `raise HTTPException(...)` é a forma do seu backend dizer "esta
requisição específica não pode ser atendida, e aqui está o porquê" — sem
derrubar o servidor inteiro. Outras requisições continuam funcionando
normalmente.

### `finally`: código que roda sempre

```python
try:
    arquivo_aberto = True
    print("Trabalhando...")
except Exception as erro:
    print(f"Deu erro: {erro}")
finally:
    print("Isso roda SEMPRE, com ou sem erro")
```
`finally` é útil para "limpeza" — por exemplo, garantir que uma conexão seja
fechada não importa o que aconteça. No seu projeto, esse papel é cumprido pelo
`with` (Módulo 18), que internamente já garante o fechamento — por isso
`app.py` raramente precisa de `finally` explícito.

> **Experimente:** escreva uma função `divide(a, b)` que usa `try`/`except`
> para capturar `ZeroDivisionError` e devolver `None` em vez de quebrar.
> Teste com `divide(10, 2)` e `divide(10, 0)`.

**Exercício 16:** escreva uma função `busca_medicamento(dicionario, nome)` que
tenta acessar `dicionario[nome]` dentro de um `try`, e no `except KeyError`
devolve a string `"Medicamento não cadastrado"`. Teste com uma chave que
existe e outra que não existe.

---
---

# PARTE 5 — O seu projeto de verdade

Agora que você tem a base, vamos olhar o coração do seu sistema: como os dados
ficam guardados, como o servidor responde a pedidos, e como tudo isso vira um
site no ar.

## Módulo 17 · Banco de dados e SQL

Os dados das mais de 350 patologias não ficam soltos no código — ficam num
**banco de dados** (o arquivo `database/patologias_bacterianas_br.sqlite`).
Pense nele como um conjunto de **planilhas** (chamadas **tabelas**): uma de
patologias, uma de medicamentos, uma de sintomas, etc., e cada planilha tem
**colunas** fixas e **linhas** (uma por registro).

Para pedir dados ao banco, usamos uma linguagem própria, o **SQL** (Structured
Query Language). O comando mais comum é o `SELECT`:

```sql
SELECT nome, cid10 FROM patologias WHERE id = 1
```
Lê assim: "**selecione** as colunas `nome` e `cid10` **da tabela** `patologias`
**onde** o `id` for 1".

### `JOIN`: combinando tabelas relacionadas

Dados relacionados ficam em tabelas separadas, ligadas por um identificador
em comum (a "chave estrangeira"). Para juntar informações de duas tabelas numa
única consulta, usamos `JOIN`:

```sql
SELECT p.nome, c.nome AS categoria
FROM patologias p
JOIN categorias_patologias c ON c.id = p.categoria_id
WHERE p.id = 1
```
Lê assim: "pegue `nome` da tabela `patologias` (apelidada de `p`) e `nome` da
tabela `categorias_patologias` (apelidada de `c`, e renomeado para
`categoria` com `AS`), **juntando** as duas tabelas onde o `id` da categoria
é igual ao `categoria_id` da patologia". Os apelidos (`p`, `c`) evitam
ambiguidade quando duas tabelas têm colunas com o mesmo nome (`nome`, neste
caso).

`LEFT JOIN` é parecido, mas **mantém a linha mesmo se não houver
correspondência** na outra tabela (preenchendo com `NULL`/`None`). É usado
quando a relação é **opcional** — por exemplo, nem toda patologia tem uma
fonte epidemiológica oficial cadastrada.

### `ORDER BY`, `WHERE` com parâmetros, e `DISTINCT`

```sql
SELECT id, nome FROM patologias
WHERE categoria_id = ?
ORDER BY nome
```
- `WHERE` filtra **quais linhas** entram no resultado.
- `ORDER BY nome` ordena o resultado alfabeticamente pelo nome.
- `DISTINCT` (visto no Módulo 9) remove linhas duplicadas do resultado —
  importante quando um `JOIN` "multiplica" linhas (por exemplo, uma patologia
  associada a duas bactérias apareceria duas vezes sem `DISTINCT`).

### Como o Python conversa com o banco

```python
import sqlite3
db = sqlite3.connect("database/patologias_bacterianas_br.sqlite")
linha = db.execute("SELECT nome FROM patologias WHERE id = 1").fetchone()
print(linha)
```
- `connect(...)` abre o banco.
- `db.execute("SELECT ...")` envia o comando SQL.
- `.fetchone()` pega **uma** linha do resultado.
- `.fetchall()` pegaria **todas** as linhas, como uma lista.

**No seu projeto** (`app.py`, função `_fetch_patologia`):
```python
pat = db.execute(
    """SELECT p.id, p.nome, p.cid10, p.descricao,
              p.prevalencia_br, p.mortalidade_br, p.populacao_risco,
              p.notificacao_compulsoria, p.tipo_notificacao,
              c.nome AS categoria, c.sistema,
              fo.sigla AS fonte_sigla, fo.nome AS fonte_nome
       FROM patologias p
       JOIN categorias_patologias c ON c.id = p.categoria_id
       LEFT JOIN fontes_oficiais fo ON fo.id = p.fonte_epidemio_id
       WHERE p.id = ?""",
    (patologia_id,),
).fetchone()
```
Repare: a string com `"""` (três aspas) permite escrever um texto **em várias
linhas** — útil para SQL, que fica mais legível formatado. O resto é o que
você já entende: `JOIN`/`LEFT JOIN` para combinar três tabelas, `WHERE p.id =
?` para filtrar pela patologia pedida, e `.fetchone()` porque queremos uma
única linha (o cabeçalho daquela patologia).

### O `?` e a regra de ouro da segurança

Note o `?` no lugar do valor, e o valor vindo separado em `(patologia_id,)`.
Isso **não é detalhe** — é segurança. Nunca cole o valor direto no texto do
SQL com `+` ou f-string; sempre use `?` e passe o valor à parte:

```python
# ❌ PERIGOSO — nunca faça isso com dados que vêm de fora:
db.execute(f"SELECT * FROM patologias WHERE id = {patologia_id}")

# ✔️ SEGURO — o sqlite3 escapa o valor corretamente:
db.execute("SELECT * FROM patologias WHERE id = ?", (patologia_id,))
```
Se `patologia_id` viesse de um usuário mal-intencionado contendo algo como
`"1; DROP TABLE patologias"`, a versão com f-string poderia executar comandos
destrutivos — esse ataque chama-se **SQL injection**, e é um dos mais comuns e
perigosos da web. A versão com `?` trata o valor **sempre** como dado, nunca
como parte do comando, então esse ataque simplesmente não funciona.

> Você pode estar pensando: "mas o `app.py` também usa f-strings dentro de
> SQL, como em `_categorias`!" — sim, mas só para nomes de **tabelas e
> colunas** que vêm de `AGENT_DOMAINS`, uma constante definida **no próprio
> código**, nunca de uma requisição do usuário. Valores que vêm de fora (como
> `patologia_id`, digitado na URL) sempre passam por `?`. Há um comentário no
> `app.py` explicando exatamente essa distinção.

### `GROUP BY` e funções de agregação (visão geral)

Embora o seu projeto use principalmente `SELECT`/`JOIN`/`WHERE`, vale conhecer
`GROUP BY`, comum em relatórios:

```sql
SELECT categoria_id, COUNT(*) AS total
FROM patologias
GROUP BY categoria_id
```
Lê assim: "agrupe as patologias por `categoria_id` e, para cada grupo, conte
quantas linhas existem (`COUNT(*)`)". Outras funções de agregação comuns:
`SUM` (soma), `AVG` (média), `MIN`/`MAX`.

> **Experimente** no terminal (sem Python), explorando o banco direto:
> ```
> sqlite3 database/patologias_bacterianas_br.sqlite "SELECT nome FROM patologias LIMIT 5"
> ```

**Exercício 17:** usando o comando `sqlite3` acima, mude o `LIMIT 5` para
`LIMIT 10` e veja 10 patologias. Depois tente
`"SELECT COUNT(*) FROM patologias"` — o que esse número significa? Por fim,
tente `"SELECT categoria_id, COUNT(*) FROM patologias GROUP BY categoria_id"`
e veja quantas patologias existem por categoria.

---

## Módulo 18 · Ferramentas avançadas que seu projeto usa

Estes conceitos são um pouco mais avançados. Você **não precisa dominá-los para
escrever** ainda, mas reconhecê-los te deixa ler o `app.py` com confiança.

### `pathlib`: caminhos de arquivo de forma segura

Em vez de montar caminhos colando textos (`"database" + "/" +
"arquivo.sqlite"`, que quebra em sistemas operacionais diferentes), Python tem
o módulo `pathlib`:

```python
from pathlib import Path

pasta = Path(__file__).parent          # a pasta onde este arquivo .py está
caminho_banco = pasta / "database" / "patologias_bacterianas_br.sqlite"
print(caminho_banco)
```
- `Path(__file__)` representa o caminho do **próprio arquivo** que está
  rodando.
- `.parent` sobe um nível (a pasta que contém o arquivo).
- O operador `/` entre `Path`s **junta caminhos** de forma correta em
  qualquer sistema operacional (Windows usa `\`, Linux/Mac usam `/` — o
  `pathlib` cuida disso por você).

**No seu projeto** (`app.py`, topo do arquivo):
```python
DB_BACT_PATH = Path(__file__).parent / "database" / "patologias_bacterianas_br.sqlite"
STATIC       = Path(__file__).parent / "static"
```
Essas duas constantes guardam, respectivamente, o caminho do banco de dados e
o caminho da pasta `static/` (onde ficam `patologias.html`, `app.js`, etc.) —
sempre relativos à localização do `app.py`, não importa de onde o programa
seja iniciado.

### O `with` e *context managers* (abre e fecha sozinho)

```python
with open("arquivo.txt") as f:
    conteudo = f.read()
# aqui fora, o arquivo já foi fechado automaticamente
```
O `with` garante que um recurso (arquivo, conexão de banco, etc.) será
**fechado no final**, mesmo se acontecer um erro no meio. É uma rede de
segurança — sem `with`, seria preciso lembrar de chamar `.close()` manualmente
em **todo** caminho possível do código, inclusive nos casos de erro.

**No seu projeto** (`app.py`), cada requisição abre sua própria conexão com o
banco usando exatamente esse padrão:
```python
with conn_bact() as db:
    pat = db.execute("SELECT ...").fetchone()
```

### `@contextmanager`: criando seu próprio "with"

Como o `conn_bact()` do seu projeto consegue funcionar com `with`, se conexões
SQLite normais não vêm prontas para isso? A resposta é o decorator
`@contextmanager`:

```python
from contextlib import contextmanager
import sqlite3

@contextmanager
def conn_bact():
    db = sqlite3.connect("database/patologias_bacterianas_br.sqlite", timeout=10)
    db.row_factory = sqlite3.Row
    db.execute("PRAGMA journal_mode=WAL")
    db.execute("PRAGMA busy_timeout=5000")
    try:
        yield db          # "empresta" a conexão para o bloco `with`
    finally:
        db.close()        # roda sempre, mesmo se o bloco `with` der erro
```
A palavra-chave `yield` é o que torna isso possível: tudo **antes** do
`yield` roda quando o `with` **começa** (abre a conexão, configura), o valor
depois de `yield` (`db`) é o que a variável `as db` recebe, e tudo **depois**
do `yield` (no `finally`) roda quando o bloco `with` **termina** — sempre,
mesmo com erro, graças ao `try`/`finally` (Módulo 16).

Os dois `PRAGMA` configuram o SQLite: `journal_mode=WAL` permite **leituras
simultâneas** mesmo enquanto o banco está sendo reconstruído pelo
`build_db.py`, e `busy_timeout=5000` faz o SQLite **esperar até 5 segundos**
antes de desistir, caso o banco esteja temporariamente ocupado — em vez de
falhar na hora.

`db.row_factory = sqlite3.Row` é o que permite acessar colunas **pelo nome**
(`pat["nome"]`) em vez de só pela posição (`pat[0]`) — e é o que torna
`dict(r)` (transformar uma linha em dicionário) possível.

### `defaultdict` (dicionário com valor padrão)

Um dicionário normal quebra (`KeyError`) se você acessa uma chave que não
existe. O `defaultdict` já começa com um valor padrão (por exemplo, uma lista
vazia), facilitando **agrupar** itens:

```python
from collections import defaultdict

por_medicamento = defaultdict(list)   # toda chave nova começa como []
por_medicamento["amox"].append("dose 1")
por_medicamento["amox"].append("dose 2")
por_medicamento["azitro"].append("dose A")

print(por_medicamento["amox"])    # ['dose 1', 'dose 2']
print(dict(por_medicamento))
# {'amox': ['dose 1', 'dose 2'], 'azitro': ['dose A']}
```
Sem `defaultdict`, você precisaria escrever, toda vez:
```python
if "amox" not in por_medicamento:
    por_medicamento["amox"] = []
por_medicamento["amox"].append("dose 1")
```
O `defaultdict` elimina esse `if` repetitivo. **Seu projeto usa isso** para
agrupar posologias e interações por medicamento — depois de buscar **todas**
as posologias de **todos** os medicamentos de uma vez (uma única consulta SQL
com `WHERE medicamento_id IN (...)`), o resultado é separado de volta por
medicamento usando `defaultdict`. Essa técnica evita o problema chamado
"N+1 queries" — fazer uma consulta ao banco **por item** de uma lista, o que
fica lento quando a lista cresce. Uma consulta que traz tudo, seguida de
agrupamento em Python, é muito mais rápida.

### Decorator (`@`)

A linha com `@` antes de uma função "embrulha" essa função com um poder extra:

```python
@app.get("/health")
def health():
    return {"status": "ok"}
```
`@app.get("/health")` diz ao FastAPI: "quando alguém acessar o endereço
`/health`, chame esta função". Você não precisa entender como o decorator
funciona por dentro — só saber que ele **liga um endereço a uma função** (no
caso do FastAPI) ou **adapta o comportamento** de uma função (no caso de
`@contextmanager`).

### Logging: registrando o que acontece

```python
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s %(message)s")
log = logging.getLogger(__name__)

log.info("DB ok: %s", "patologias_bacterianas_br.sqlite")
```
`print()` é ótimo para experimentar, mas num servidor que roda 24 horas, você
precisa de **registros com data/hora e nível de severidade** (`INFO`,
`WARNING`, `ERROR`). É isso que `logging` oferece. **No seu projeto**
(`app.py`), na função `startup_check`, o `log.info(...)` ou `log.error(...)`
registra se o banco de dados foi encontrado ao iniciar o servidor — essas
mensagens aparecem nos logs do Railway, ajudando a diagnosticar problemas de
deploy sem precisar adicionar `print` espalhados.

**Exercício 18:** no `app.py`, procure todas as linhas que começam com `@app.`.
Cada uma é um endereço da sua API. Liste três deles. Depois, usando
`defaultdict(list)`, agrupe a lista
`[("febre", "respiratório"), ("tosse", "respiratório"), ("diarreia", "digestivo")]`
por sistema (segundo elemento da tupla).

---

## Módulo 19 · JSON: a língua da web

Quando o navegador (front-end) e o servidor (back-end) trocam dados, eles
precisam **falar a mesma língua** — e essa língua quase sempre é o **JSON**
(JavaScript Object Notation). A boa notícia: JSON é **quase idêntico** a
dicionários e listas Python que você já conhece.

```json
{
  "id": 1,
  "nome": "Pneumonia Comunitária",
  "cid10": "J18",
  "notificacao_compulsoria": false,
  "sintomas": [
    {"nome": "febre", "frequencia": "muito comum"},
    {"nome": "tosse", "frequencia": "comum"}
  ]
}
```
Compare com o dicionário Python equivalente:
```python
{
    "id": 1,
    "nome": "Pneumonia Comunitária",
    "cid10": "J18",
    "notificacao_compulsoria": False,
    "sintomas": [
        {"nome": "febre", "frequencia": "muito comum"},
        {"nome": "tosse", "frequencia": "comum"},
    ],
}
```
As diferenças são pequenas, mas importam:

| Python | JSON |
|--------|------|
| `True` / `False` | `true` / `false` (minúsculo) |
| `None` | `null` |
| `'aspas simples'` ou `"aspas duplas"` | só `"aspas duplas"` |
| permite vírgula sobrando no fim | **não** permite |

### O módulo `json`

```python
import json

dados = {"nome": "Amoxicilina", "dose_mg": 500, "disponivel_sus": True}

texto_json = json.dumps(dados)          # dicionário -> texto JSON
print(texto_json)
# {"nome": "Amoxicilina", "dose_mg": 500, "disponivel_sus": true}

de_volta = json.loads(texto_json)       # texto JSON -> dicionário
print(de_volta["nome"])                 # Amoxicilina
print(type(de_volta))                   # <class 'dict'>
```
- `json.dumps(...)` ("dump string") transforma um dicionário/lista Python num
  **texto** JSON.
- `json.loads(...)` ("load string") faz o caminho inverso.

### Por que isso importa para o seu projeto

**Você praticamente nunca precisa chamar `json.dumps` no seu `app.py`** — e
isso é proposital! O FastAPI faz essa conversão **automaticamente**: quando
uma função decorada com `@app.get(...)` faz `return {"nome": "Pneumonia",
...}`, o FastAPI:

1. Pega o dicionário Python que você devolveu;
2. Converte para JSON (`json.dumps`, por baixo dos panos);
3. Define o cabeçalho HTTP `Content-Type: application/json`;
4. Envia tudo isso como resposta ao navegador.

Do outro lado, no `static/app.js`, o JavaScript faz o caminho inverso com
`fetch(...).then(r => r.json())` — pega a resposta e a transforma de volta num
objeto JavaScript (que é o "dicionário" do JavaScript). É essa simetria —
Python dict ↔ JSON ↔ JavaScript object — que faz tudo se encaixar sem
conversões manuais.

> **Experimente:** com o servidor rodando (Módulo 20), abra
> `http://localhost:8000/health` no navegador. O que você vê na tela **é**
> JSON — o próprio dicionário que a função `health()` devolveu, convertido
> automaticamente.

**Exercício 19:** no modo interativo, crie um dicionário representando uma
patologia simples (nome, cid10, uma lista de sintomas). Use `json.dumps(...,
indent=2)` para imprimir formatado (o parâmetro `indent=2` deixa a saída
"bonita", com quebras de linha e recuo — experimente com e sem ele).

---

## Módulo 20 · Como funciona uma API (FastAPI)

Uma **API** é como um garçom num restaurante:
1. O navegador (cliente) faz um **pedido** a um endereço — ex.:
   `/api/bacterias/patologia/1`.
2. O servidor (seu `app.py`) **busca os dados** no banco (a cozinha).
3. Devolve uma **resposta** em JSON (Módulo 19), que o front-end usa para
   montar a tela.

```python
@app.get("/api/bacterias/patologia/{patologia_id}")
def bact_detalhe(patologia_id: int):
    return _agent_detalhe(AGENT_DOMAINS["bacterias"], patologia_id)
```

Decifrando linha por linha:
- `@app.get("/api/bacterias/patologia/{patologia_id}")` → o endereço. A parte
  `{patologia_id}` é **variável**: muda conforme a patologia pedida (ex.:
  `/api/bacterias/patologia/42` → `patologia_id` vale `42`). Isso se chama
  **parâmetro de caminho** (*path parameter*).
- `def bact_detalhe(patologia_id: int):` → a função que responde. O `: int`
  **garante** que o valor recebido é um número inteiro (se vier texto não
  numérico, o FastAPI recusa automaticamente, devolvendo erro 422 — segurança
  e validação de graça, sem você escrever nenhum `if`).
- `return ...` → o dicionário devolvido **vira JSON sozinho** e volta para o
  navegador (Módulo 19).

### Parâmetros de consulta (*query parameters*)

Além de parâmetros no caminho (`{patologia_id}`), uma API recebe parâmetros
**opcionais** depois de `?` na URL — por exemplo,
`/api/bacterias/patologias?categoria_id=3`. No FastAPI, basta declarar um
parâmetro **com valor padrão** que não está em `{ }` no caminho:

```python
@app.get("/api/bacterias/patologias")
def bact_patologias(categoria_id: int = None):
    return _patologias(AGENT_DOMAINS["bacterias"], categoria_id)
```
- Se a URL for `/api/bacterias/patologias`, `categoria_id` chega como `None`.
- Se a URL for `/api/bacterias/patologias?categoria_id=3`, `categoria_id`
  chega como `3` (já convertido para `int`!).

Dentro de `_patologias`, vimos no Módulo 17 como esse valor vira um filtro
`WHERE` opcional no SQL:
```python
if categoria_id:
    sql += " WHERE p.categoria_id = ?"
    params.append(categoria_id)
```
"Se um `categoria_id` foi informado (não é `None`/`0`, lembrando do Módulo 5),
adicione o filtro ao SQL." Sem `categoria_id`, a consulta traz **todas** as
patologias do domínio.

### Códigos de status HTTP

Toda resposta HTTP vem com um **código de status** — um número de 3 dígitos
que resume o resultado:

| Código | Significado | Quando acontece no seu projeto |
|--------|-------------|----------------------------------|
| `200` | OK | resposta normal, com sucesso |
| `404` | Não encontrado | `_fetch_patologia` levanta `HTTPException(404, ...)` quando o `id` não existe |
| `422` | Dados inválidos | FastAPI recusa automaticamente se `patologia_id` não for um número |
| `500` | Erro interno | algo quebrou no servidor (bug, banco indisponível, etc.) |

### Veja funcionando

Rode o servidor:
```
uvicorn app:app --reload
```
- `app:app` significa "no arquivo `app.py`, use o objeto chamado `app`" (a
  instância de `FastAPI()`).
- `--reload` reinicia o servidor automaticamente sempre que você salva uma
  mudança no código — ótimo durante o desenvolvimento.

Depois abra no navegador: **`http://localhost:8000/docs`**. O FastAPI gera
sozinho uma página interativa (chamada Swagger UI) com **todos os seus
endpoints** — e mostra as docstrings que escrevemos no código (lembra dos
comentários do Módulo 0? docstrings são comentários especiais, entre `"""`,
logo no início de uma função, que ferramentas como essa conseguem ler e
exibir). Você pode testar cada endpoint clicando, sem precisar escrever
código.

**Exercício 20:** com o servidor rodando, acesse `http://localhost:8000/health`.
Que resposta aparece? Compare com o `return` da função `health` no `app.py`.
Depois acesse `/docs` e teste o endpoint `/api/bacterias/categorias` — quais
campos aparecem na resposta?

---

## Módulo 21 · Lendo um endpoint inteiro, linha por linha

Hora de juntar tudo. Vamos ler uma versão simplificada de um endpoint real do
seu projeto e reconhecer **cada conceito** que estudamos.

### Endpoint 1: uma listagem com cache

```python
@app.get("/api/cronicas/categorias")     # (1) decorator: liga endereço à função
def cronicas_categorias():                # (2) função, sem parâmetros
    if "cronicas:categorias" not in _cache:   # (3) if + dicionário (cache)
        with conn_bact() as db:                # (4) with: abre/fecha o banco
            rows = db.execute(                 # (5) SQL: pede dados
                "SELECT id, nome, sistema FROM categorias_patologias ORDER BY nome"
            ).fetchall()                       # (6) pega todas as linhas
        _cache["cronicas:categorias"] = [dict(r) for r in rows]  # (7) compreensão
    return _cache["cronicas:categorias"]       # (8) devolve (vira JSON)
```

O que cada parte faz, usando o que você aprendeu:
1. **Decorator** (Módulo 18, 20): liga o endereço `/api/cronicas/categorias` a esta função.
2. **Função** (Módulo 13): o bloco que responde ao pedido.
3. **`if` + dicionário** (Módulos 10 e 7): "se ainda não calculei isto antes...".
   Isso é um **cache** — guarda o resultado para não consultar o banco toda vez.
4. **`with`** (Módulo 18): abre o banco e garante o fechamento.
5. **SQL** (Módulo 17): pede id, nome e sistema das categorias, em ordem.
6. **`.fetchall()`**: traz todas as linhas encontradas.
7. **Compreensão de lista** (Módulo 12): transforma cada linha em dicionário.
8. **`return`** (Módulo 13, 19): devolve a lista — que o FastAPI converte em
   JSON automaticamente.

### Endpoint 2: com filtro opcional

A função `cronicas_patologias`, logo abaixo da anterior, é parecida — mas
recebe um parâmetro de consulta (Módulo 20):

```python
@app.get("/api/cronicas/patologias")
def cronicas_patologias(categoria_id: int = None):   # (1) query parameter opcional
    key = f"cronicas:patologias:{categoria_id}"        # (2) f-string monta a chave do cache
    if key not in _cache:
        sql = """
            SELECT id, nome, cid10, prevalencia_br, mortalidade_br
            FROM patologias
            WHERE categoria_id_cronica IS NOT NULL
        """
        params = []
        if categoria_id:                               # (3) if "vazio = falso"
            sql += " AND categoria_id = ?"             # (4) concatenação de strings
            params.append(categoria_id)
        sql += " ORDER BY nome"
        with conn_bact() as db:
            rows = db.execute(sql, params).fetchall()  # (5) execute com lista de parâmetros
        _cache[key] = [dict(r) for r in rows]
    return _cache[key]
```

Conceitos novos em relação ao endpoint 1:
1. **Query parameter** (Módulo 20): `categoria_id: int = None` — opcional,
   vem depois de `?` na URL.
2. **f-string** (Módulo 3) cria uma chave de cache **diferente para cada
   combinação** de filtro — `"cronicas:patologias:None"` (sem filtro) é
   diferente de `"cronicas:patologias:3"` (filtrado pela categoria 3). Sem
   isso, o cache devolveria sempre o primeiro resultado calculado, ignorando
   o filtro.
3. **`if categoria_id:`** (Módulos 5 e 10): só entra se um valor "verdadeiro"
   foi passado (não é `None` nem `0`).
4. **Concatenação** (`+=`, Módulo 1): o SQL é **construído aos poucos** —
   começa com a base, e só adiciona o `AND categoria_id = ?` se necessário.
5. **`.execute(sql, params)`**: o segundo argumento é uma **lista** (em vez da
   tupla `(patologia_id,)` que vimos antes) — o `sqlite3` aceita ambos.
   `params` pode ter **zero ou um** elementos, dependendo do `if` acima.

Se você entendeu esses dois endpoints, **você já consegue ler o seu próprio
backend inteiro** — os outros 17 endpoints seguem os mesmos padrões, só
mudando tabelas e nomes de colunas (é exatamente por isso que
`AGENT_DOMAINS` + `_agent_detalhe` puderam unificar os quatro domínios "por
agente" numa lógica só, como vimos no Módulo 15).

**Exercício 21 (final desta parte):** abra o `app.py` e encontre a função
`_patologias`. Compare-a com `cronicas_patologias` acima — quais partes são
**idênticas** em estrutura, e qual a principal diferença (dica: uma delas
recebe `cfg`, um objeto `AgentDomain`, e usa `cfg.junction` no SQL)?

---

## Módulo 22 · Testes automatizados (garantindo que nada quebra)

Conforme um projeto cresce, fica fácil mudar uma coisa e **quebrar outra sem
perceber**. **Testes automatizados** são programas curtos que verificam se o
seu código continua se comportando como esperado — você roda em segundos,
sempre que quiser, em vez de testar tudo manualmente clicando no site.

### A ideia central: comparar "antes" e "depois"

A técnica mais simples (e foi usada de verdade neste projeto, durante os
refactors recentes do `app.py`) chama-se **teste de regressão por
"snapshot"** (instantâneo):

1. **Antes** de mudar o código, você chama todos os endpoints importantes e
   **salva as respostas** (em arquivos JSON, por exemplo).
2. Você faz a mudança no código (refatoração, organização, comentários...).
3. **Depois**, você chama os **mesmos** endpoints de novo e **compara** com o
   que foi salvo.
4. Se as respostas forem **idênticas**, a mudança não alterou o
   comportamento — só a organização interna do código. Se houver qualquer
   diferença, algo mudou (de propósito ou por engano) e vale investigar.

```python
import json
import urllib.request

def busca_json(url):
    with urllib.request.urlopen(url) as resposta:
        return json.loads(resposta.read())

# Passo 1: capturar o "antes"
antes = busca_json("http://localhost:8000/api/bacterias/patologia/1")
with open("antes.json", "w") as f:
    json.dump(antes, f)

# ... aqui você faz mudanças no app.py e reinicia o servidor ...

# Passo 3: capturar o "depois" e comparar
depois = busca_json("http://localhost:8000/api/bacterias/patologia/1")
print(antes == depois)   # True significa: nenhuma diferença!
```
- `urllib.request.urlopen(url)` faz uma requisição HTTP, parecido com abrir a
  URL no navegador, mas dentro de um programa Python.
- `json.load`/`json.dump` (Módulo 19) leem/escrevem JSON em arquivos.
- `antes == depois` compara os dois dicionários **inteiros** — em Python,
  `==` entre dicionários compara **todo o conteúdo** (chaves e valores), não
  apenas se são "a mesma caixa na memória".

### Por que isso foi importante no seu projeto

O `app.py` original tinha **quatro funções quase idênticas** (uma para
bactérias, vírus, fungos e parasitas — ~280 linhas cada). Para unificá-las
numa lógica genérica (`_agent_detalhe` + `AGENT_DOMAINS`, Módulo 15) **sem
quebrar nada**, foi feito exatamente esse processo: capturar a resposta JSON
de **todas as 352 patologias** (mais listagens e categorias) antes da
mudança, refatorar o código, capturar de novo, e comparar item a item. Zero
diferenças = refatoração segura. Esse tipo de teste dá **confiança** para
mexer em código grande sem medo.

### `assert`: a forma mais simples de testar

```python
def tem_febre(temperatura):
    return temperatura >= 37.8

assert tem_febre(38.5) == True
assert tem_febre(36.0) == False
print("Todos os testes passaram!")
```
`assert condicao` não faz nada se `condicao` for verdadeira, mas levanta
`AssertionError` (Módulo 16) se for falsa — interrompendo o programa e
avisando exatamente **qual verificação falhou**. É a base de frameworks de
teste mais completos, como o `pytest`, que organiza muitos `assert`s em
funções de teste e mostra um relatório de quais passaram/falharam.

> **Experimente:** escreva três `assert`s para a função `tem_febre` do Módulo
> 13 (uma temperatura alta, uma baixa, e uma exatamente no limite, `37.8`).
> Depois mude **de propósito** um dos `assert`s para um valor errado e veja a
> mensagem `AssertionError`.

**Exercício 22:** escreva uma função `calcula_dose(peso_kg)` que devolve
`peso_kg * 10`. Depois escreva 3 `assert`s testando essa função com pesos
diferentes (ex.: 70kg → 700, 50kg → 500). Rode o arquivo e confirme que nada
"explode".

---

## Módulo 23 · Git e deploy: do código ao site no ar

Até agora, todo o código rodou na sua máquina (`localhost`). Mas o seu projeto
está **no ar**, acessível pela internet. Como o código sai do seu computador e
chega ao servidor que todo mundo acessa? A resposta envolve duas ferramentas:
**Git** (controle de versão) e **Railway** (hospedagem/deploy).

### Git: o "histórico de versões" do código

Git guarda **snapshots** do seu código ao longo do tempo, chamados
**commits**. Cada commit tem uma mensagem descrevendo o que mudou. Comandos
básicos (no terminal, dentro da pasta do projeto):

```bash
git status                  # o que mudou desde o último commit?
git add app.py               # marca app.py para entrar no próximo commit
git commit -m "Corrige bug X"  # cria o snapshot, com uma mensagem
git push                      # envia os commits para o GitHub
```
- `git status` — como um "raio-x": mostra arquivos novos, modificados ou
  removidos.
- `git add` — escolhe **quais** mudanças entrarão no próximo commit (você pode
  ter mudanças em vários arquivos e só "commitar" algumas).
- `git commit -m "..."` — cria o snapshot com uma mensagem explicando o
  **porquê** da mudança (igual aos bons comentários do Módulo 0!).
- `git push` — envia seus commits para o **GitHub** (uma cópia remota do
  repositório, que outras pessoas — e o Railway — também enxergam).

### Branches: trabalhando em "linhas paralelas"

Uma **branch** (galho/ramificação) é uma cópia paralela do código, onde você
pode experimentar mudanças **sem afetar** a versão "oficial" (geralmente
chamada `main`):

```bash
git checkout -b minha-mudanca   # cria e muda para uma nova branch
# ... edita arquivos, faz commits ...
git push -u origin minha-mudanca  # envia essa branch ao GitHub
```
Depois, abre-se um **Pull Request (PR)** no GitHub: uma proposta de "trazer as
mudanças da branch `minha-mudanca` para a `main`". Um PR mostra exatamente
**quais linhas mudaram** (em verde o que foi adicionado, em vermelho o que foi
removido) — é assim que mudanças neste projeto são revisadas antes de irem
para o ar.

### Deploy automático: do `git push` ao site no ar

O arquivo `railway.toml` do seu projeto diz ao Railway **como** rodar o
projeto:
```toml
[build]
builder = "nixpacks"
buildCommand = "python database/build_db.py"

[deploy]
startCommand = "uvicorn app:app --host 0.0.0.0 --port $PORT"
restartPolicyType = "ON_FAILURE"
```
- `buildCommand` roda **uma vez**, antes do servidor iniciar — no seu caso,
  executa `database/build_db.py`, que monta o arquivo `.sqlite` a partir dos
  módulos de dados (Módulo 14). É o `__main__` do Módulo 14 em ação.
- `startCommand` é o comando que **mantém o servidor rodando** —
  `uvicorn app:app` é o mesmo comando do Módulo 20, só que escutando no host
  `0.0.0.0` (qualquer endereço) e na porta que o Railway define
  (`$PORT`, uma variável de ambiente).
- `restartPolicyType = "ON_FAILURE"` diz: "se o processo cair, reinicie
  automaticamente".

O Railway está configurado para **observar a branch principal** do
repositório no GitHub: sempre que um PR é mesclado (*merged*) nela, o Railway
automaticamente roda `buildCommand`, depois `startCommand`, e o site no ar
passa a refletir o novo código — geralmente em poucos minutos. É por isso que,
neste projeto, o fluxo de trabalho é sempre: **código → commit → push → PR →
merge → deploy automático**.

**Exercício 23 (final do curso):** rode `git status` e `git log --oneline -5`
no seu terminal (dentro da pasta do projeto). O `git log` mostra os últimos 5
commits — leia as mensagens. Você consegue identificar, pelas mensagens, quais
commits foram sobre o painel de patologias e quais foram sobre este material
de estudo?

---
---

# APÊNDICES

## Apêndice A · Erros comuns e como resolver

| Mensagem de erro | O que significa | Como resolver |
|------------------|-----------------|---------------|
| `SyntaxError` | Escreveu algo "fora da gramática" do Python | Cheque aspas, parênteses e os dois-pontos `:` |
| `IndentationError` | Espaçamento errado no início da linha | Use sempre 4 espaços dentro de `if`, `for`, `def`, `class` |
| `NameError: name 'x' is not defined` | Usou uma variável que não existe (ou existe só dentro de outra função) | Verifique se escreveu o nome certo / criou antes / não está fora do escopo (Módulo 13) |
| `TypeError` | Misturou tipos incompatíveis | Ex.: somar texto com número — converta com `int()`/`float()`/`str()` (Módulo 2) |
| `KeyError: 'x'` | Pediu uma chave que não existe no dicionário | Use `.get("x")` em vez de `["x"]` (Módulo 7), ou capture com `try`/`except KeyError` (Módulo 16) |
| `IndexError` | Pediu uma posição que não existe na lista | A contagem vai de 0 até `len(lista) - 1` (Módulo 6) |
| `ValueError` | O tipo está certo, mas o **valor** não serve para a operação | Ex.: `int("abc")` — o texto não representa um número |
| `ZeroDivisionError` | Tentou dividir por zero | Verifique a condição antes de dividir, ou use `try`/`except` (Módulo 16) |
| `AttributeError: 'X' object has no attribute 'y'` | Tentou acessar um campo/método (`.y`) que esse tipo/objeto não tem | Confira o tipo com `type(obj)` e confirme o nome do campo/método |
| `ModuleNotFoundError: No module named 'x'` | A biblioteca `x` não está instalada | Rode `pip install x` (ou confira o `requirements.txt`, Módulo 14) |
| `404 Not Found` (numa resposta de API) | O recurso pedido não existe | No seu projeto, é o `HTTPException(404, ...)` de `_fetch_patologia` (Módulo 16) |
| `422 Unprocessable Entity` (numa resposta de API) | Os dados enviados não batem com o tipo esperado (`: int`, etc.) | Confira se a URL está passando o tipo certo (Módulo 20) |

**Dica de ouro:** sempre leia a **última linha** do erro primeiro. Ela quase
sempre diz o **tipo** do problema (`NameError`, `TypeError`...) e a
**mensagem** específica. As linhas acima dela (o "traceback") mostram o
**caminho** que o programa percorreu até o erro — útil para achar **onde**,
mas a última linha geralmente já diz **o quê**.

---

## Apêndice B · Gabarito dos exercícios deste material

```python
# Exercício 0
print("Ian")
print("estou aprendendo Python")

# Exercício 1
nome = "Maria"
idade = 30
febre = True
print(nome)
print(idade)
print(febre)
idade += 1
print(idade)    # 31

# Exercício 2
temperatura_texto = "38.5"
temperatura = float(temperatura_texto)
temperatura = temperatura + 0.2
print(temperatura)        # 38.7
print(type(temperatura))  # <class 'float'>

# Exercício 3
medicamento = "Azitromicina"
dose = 500
print(f"{medicamento}: tomar {dose} mg no primeiro dia")

combinacao = "Amoxicilina + Ácido clavulânico"
print(combinacao.split(" + "))   # ['Amoxicilina', 'Ácido clavulânico']

# Exercício 4
preco_comprimido = 4.50
quantidade = 21
custo = preco_comprimido * quantidade
print(f"Custo total: R$ {custo:.2f}")   # Custo total: R$ 94.50

# Exercício 5
temperatura = 38.5
print(temperatura >= 37.8)   # True

lista_vazia = []
lista_cheia = ["febre"]
print(bool(lista_vazia))     # False
print(bool(lista_cheia))     # True

# Exercício 6
meds = ["Cefalexina", "Amoxicilina", "Azitromicina"]
meds.append("Doxiciclina")
meds_ordenados = sorted(meds)
print(meds_ordenados)
print(len(meds_ordenados))   # 4

# Exercício 7
medicamento = {"nome": "Amoxicilina", "dose_mg": 500, "disponivel_sus": True}
print(f"{medicamento['nome']} — {medicamento['dose_mg']} mg")
print(medicamento.get("posologia", "não informada"))   # não informada

# Exercício 8
dias = ("seg", "ter", "qua", "qui", "sex", "sab", "dom")
print(dias[0], dias[-1])     # seg dom

pares = [("febre", "muito comum"), ("tosse", "comum")]
for nome, frequencia in pares:
    print(f"{nome}: {frequencia}")

# Exercício 9
tipos = ["bacteriana", "viral", "fungica", "bacteriana", "parasitaria", "viral"]
unicos = set(tipos)
print(len(unicos))   # 4

# Exercício 10
idade = 70
if idade >= 65:
    print("idoso")
else:
    print("adulto")

categoria = "idoso" if idade >= 65 else "adulto"
print(categoria)      # idoso

# Exercício 11
notas = ["A", "B", "A", "C"]
for n in notas:
    print(f"Nível de evidência: {n}")

for posicao, n in enumerate(notas):
    print(f"{posicao + 1}ª: Nível {n}")

# Exercício 12
temperaturas = [36.5, 38.2, 37.0, 39.1]
febres = [t for t in temperaturas if t >= 37.8]
print(febres)                # [38.2, 39.1]

medicamentos = ["Amoxicilina", "AAS", "Cefalexina"]
classificacao = {nome: ("curto" if len(nome) <= 5 else "longo") for nome in medicamentos}
print(classificacao)
# {'Amoxicilina': 'longo', 'AAS': 'curto', 'Cefalexina': 'longo'}

# Exercício 13
def tem_febre(temperatura):
    return temperatura >= 37.8

print(tem_febre(38.5))       # True
print(tem_febre(36.5))       # False

def classifica_idade(idade, limite=65):
    return "idoso" if idade >= limite else "adulto"

print(classifica_idade(70))        # idoso  (usa limite padrão 65)
print(classifica_idade(60, 55))    # idoso  (limite customizado 55)

# Exercício 14
import random
print(random.randint(1, 6))

# arquivo saudacoes.py:
#   def ola(nome):
#       print(f"Olá, {nome}!")
#
# arquivo teste.py (mesma pasta):
#   from saudacoes import ola
#   ola("Ian")

# Exercício 15 — leitura:
#   drug_table do domínio "bacterias"  -> "antibioticos"
#   agent_out_key do domínio "virais"  -> "agente"

# Exercício 16
def busca_medicamento(dicionario, nome):
    try:
        return dicionario[nome]
    except KeyError:
        return "Medicamento não cadastrado"

estoque = {"Amoxicilina": 500, "Azitromicina": 250}
print(busca_medicamento(estoque, "Amoxicilina"))   # 500
print(busca_medicamento(estoque, "Penicilina"))    # Medicamento não cadastrado

# Exercício 17 — usando o terminal:
#   sqlite3 database/patologias_bacterianas_br.sqlite "SELECT nome FROM patologias LIMIT 10"
#   sqlite3 database/patologias_bacterianas_br.sqlite "SELECT COUNT(*) FROM patologias"
#     -> COUNT(*) é o número total de patologias cadastradas no banco
#   sqlite3 database/patologias_bacterianas_br.sqlite \
#     "SELECT categoria_id, COUNT(*) FROM patologias GROUP BY categoria_id"
#     -> uma linha por categoria, com a quantidade de patologias em cada uma

# Exercício 18 — ex.: @app.get("/"), @app.get("/health"),
#                      @app.get("/api/bacterias/categorias")
from collections import defaultdict

itens = [("febre", "respiratório"), ("tosse", "respiratório"), ("diarreia", "digestivo")]
por_sistema = defaultdict(list)
for sintoma, sistema in itens:
    por_sistema[sistema].append(sintoma)
print(dict(por_sistema))
# {'respiratório': ['febre', 'tosse'], 'digestivo': ['diarreia']}

# Exercício 19
import json

patologia = {
    "nome": "Pneumonia Comunitária",
    "cid10": "J18",
    "sintomas": ["febre", "tosse"],
}
print(json.dumps(patologia, indent=2, ensure_ascii=False))
# com indent=2: cada chave numa linha, recuada — muito mais fácil de ler
# sem indent: tudo numa linha só

# Exercício 20 — /health responde algo como:
#   {"status": "ok", "dbs": {"patologias_bacterianas": true}}
# em /docs, /api/bacterias/categorias devolve uma lista de objetos
# com "id", "nome" e "sistema"

# Exercício 21 — leitura:
# _patologias(cfg, categoria_id) e cronicas_patologias(categoria_id) têm a
# mesma estrutura: chave de cache com f-string, SQL base, "if categoria_id"
# adicionando um filtro WHERE/AND, .execute(sql, params), e
# [dict(r) for r in rows] guardado em _cache.
# A diferença: _patologias recebe `cfg` (um AgentDomain) e usa
# `cfg.junction` no JOIN, porque cada domínio tem uma tabela de junção
# diferente (patologia_bacteria, patologia_virus, ...). cronicas_patologias
# não precisa de JOIN com agente, porque crônicas não têm agente etiológico.

# Exercício 22
def calcula_dose(peso_kg):
    return peso_kg * 10

assert calcula_dose(70) == 700
assert calcula_dose(50) == 500
assert calcula_dose(0) == 0
print("Todos os testes passaram!")

# Exercício 23 — leitura:
# `git log --oneline -5` mostra mensagens como "Refatora endpoints de
# patologias por agente em AGENT_DOMAINS", "Remove módulo presidencial",
# "Adiciona comentários profissionais ao app.py", "Cria material de estudo
# de Python" — pelas palavras-chave (app.py, patologias, AGENT_DOMAINS vs.
# Python, material, estudo) dá para separar os dois assuntos.
```

---

## Apêndice C · Glossário de bolso

- **Variável** — caixa com nome que guarda um valor.
- **Tipo** — a natureza de um valor: texto (`str`), inteiro (`int`), decimal
  (`float`), lógico (`bool`).
- **Conversão de tipo** — transformar um valor de um tipo para outro:
  `int()`, `float()`, `str()`.
- **Lista** `[ ]` — coleção ordenada e mutável, acessada por posição (começa
  em 0).
- **Dicionário** `{chave: valor}` — coleção de pares chave → valor, acessada
  por nome.
- **Tupla** `( )` — como lista, mas imutável (não muda depois de criada).
- **Conjunto (`set`)** `{ }` — coleção sem ordem e sem repetição.
- **Fatiamento (slicing)** — `algo[inicio:fim]`, pega um pedaço de uma lista
  ou string.
- **`and` / `or` / `not`** — combinam ou invertem condições verdadeiro/falso.
- **Truthiness** — a ideia de que `0`, `""`, `[]`, `{}` e `None` se comportam
  como `False` em testes.
- **Operador ternário** — `valor_a if condicao else valor_b`, um `if`/`else`
  numa linha.
- **`for` / `while`** — repetem um bloco de código; `for` percorre uma
  coleção, `while` repete enquanto uma condição for verdadeira.
- **`break` / `continue`** — `break` encerra o loop; `continue` pula para a
  próxima volta.
- **`enumerate` / `zip`** — `enumerate` dá posição+item; `zip` percorre duas
  listas juntas.
- **Compreensão** — atalho `[expr for item in coleção if condição]` (ou com
  `{ }` para dicionários) para criar uma coleção nova a partir de outra.
- **Função** — bloco de código com nome, reutilizável; recebe parâmetros e
  pode `return`.
- **Parâmetro / argumento** — a "caixa de entrada" de uma função (parâmetro)
  e o valor passado a ela na chamada (argumento).
- **`*args` / `**kwargs`** — formas de uma função aceitar uma quantidade
  variável de argumentos posicionais (`*args`) ou nomeados (`**kwargs`).
- **Escopo** — onde uma variável "existe"; variáveis criadas dentro de uma
  função são locais a ela.
- **`return`** — entrega o resultado e encerra a função.
- **Módulo** — um arquivo `.py`; `import` traz código de um para outro.
- **Pacote** — uma pasta de módulos relacionados.
- **`__name__ == "__main__"`** — bloco que só roda quando o arquivo é
  executado diretamente, não quando é importado.
- **Classe** — molde para criar objetos que agrupam dados (e, opcionalmente,
  comportamentos/métodos).
- **Objeto** — algo criado a partir de uma classe; campos e métodos acessados
  com ponto.
- **`self`** — dentro de uma classe, refere-se ao próprio objeto.
- **`try` / `except` / `finally` / `raise`** — capturam, tratam e provocam
  erros de forma controlada.
- **`HTTPException`** — um `raise` que o FastAPI converte numa resposta HTTP
  de erro (ex.: 404).
- **SQL** — linguagem para pedir dados ao banco (`SELECT ... FROM ... WHERE
  ... JOIN ... ORDER BY ... GROUP BY`).
- **`JOIN` / `LEFT JOIN`** — combinam linhas de tabelas relacionadas.
- **SQL injection** — ataque que explora SQL montado por concatenação direta
  de valores; evitado usando `?` + parâmetros.
- **`with` / context manager / `@contextmanager`** — garantem abertura e
  fechamento automáticos de um recurso (arquivo, conexão).
- **`defaultdict`** — dicionário que cria um valor padrão (ex.: lista vazia)
  para chaves novas, facilitando agrupamento.
- **Decorator (`@`)** — modifica/liga uma função a algo externo (uma rota
  HTTP, um gerenciador de contexto).
- **JSON** — formato de troca de dados, quase idêntico a um dicionário
  Python; `json.dumps`/`json.loads` convertem entre texto JSON e objetos
  Python.
- **API** — o "garçom": recebe pedidos em endereços (endpoints) e devolve
  respostas (JSON).
- **Endpoint** — um endereço da API ligado a uma função (via `@app.get`).
- **Path parameter / query parameter** — partes variáveis de uma URL: no
  caminho (`{id}`) ou depois de `?` (`?categoria_id=3`).
- **Código de status HTTP** — número que resume o resultado de uma resposta
  (`200` ok, `404` não encontrado, `422` dados inválidos, `500` erro interno).
- **Cache** — guardar um resultado já calculado para não refazer o trabalho.
- **Teste de regressão / snapshot** — comparar a resposta "antes" e "depois"
  de uma mudança para garantir que o comportamento não mudou.
- **`assert`** — verifica uma condição; levanta `AssertionError` se for
  falsa.
- **Git** — sistema de controle de versão; `commit` cria um snapshot,
  `push` envia ao GitHub.
- **Branch** — linha paralela de desenvolvimento; mudanças viram um
  **Pull Request (PR)** antes de irem para a `main`.
- **Deploy** — processo de colocar o código no ar; no seu projeto, automático
  via Railway após merge na `main`.

---

## Apêndice D · Mapa do projeto (onde fica cada coisa)

Para fechar, um "mapa" rápido de onde cada conceito deste curso aparece
fisicamente no seu projeto — útil para navegar quando você quiser explorar por
conta própria:

| Pasta/arquivo | O que tem | Conceitos deste curso |
|---------------|-----------|------------------------|
| `app.py` | O servidor: endpoints, configuração dos domínios, helpers | Módulos 13–22 (quase tudo) |
| `database/build_db.py` | Script que monta o banco `.sqlite` a partir dos dados | Módulos 14 (`__main__`), 17 (SQL `CREATE`/`INSERT`) |
| `database/data_*.py` | Dados médicos organizados por assunto (ex.: `data_criterios_bacterianas.py`) | Módulos 6–8 (listas, dicionários, tuplas de dados) |
| `database/patologias_bacterianas_br.sqlite` | O banco de dados final, gerado no build | Módulo 17 |
| `static/patologias.html` | A página principal: estrutura HTML + CSS | (fora do escopo deste curso, mas referenciado no Módulo 3) |
| `static/app.js` | JavaScript: faz `fetch` nos endpoints e monta a tela | Módulo 19 (espelha o JSON do back-end) |
| `requirements.txt` | Lista de bibliotecas externas (`pip install -r requirements.txt`) | Módulo 14 |
| `railway.toml` | Configuração de build/deploy do Railway | Módulo 23 |
| `.env.example` | Documentação de variáveis de ambiente (hoje, nenhuma é necessária) | Módulo 23 |

Um exercício de "fechamento" não-numerado, mas recomendado: abra cada um
desses arquivos por alguns minutos, sem pressa, e tente reconhecer pelo menos
**três conceitos** deste curso em cada um. Você vai perceber que, depois deste
material, o código deixou de ser "uma parede de texto" e virou algo que você
**consegue ler**.

---

> **Parabéns por chegar até aqui!** Você passou por 24 módulos, do `print()`
> mais simples até ler um endpoint inteiro de uma API real. O próximo passo é
> **praticar** — use o `EXERCICIOS_PYTHON.md` para desafios extras, e tente
> adicionar um campo numa resposta da API ou criar um endpoint novo bem
> simples no seu projeto. Programação se aprende fazendo — e agora você tem a
> base para isso. 🚀

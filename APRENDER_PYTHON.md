# Aprender Python do Zero 🐍

### Um curso completo para iniciantes, usando o seu próprio projeto

Este material foi feito para quem **nunca programou**. A cada passo você vê um
bloco de código pequeno, e logo abaixo a explicação **linha por linha**, na
linguagem mais simples possível. O conhecimento é construído aos poucos: cada
módulo usa o que você aprendeu no anterior.

No final, você vai entender o código que faz o seu painel clínico de patologias
funcionar — porque vamos aprender olhando justamente para ele.

> **Como estudar:** vá devagar, **um módulo por vez**. Sempre que aparecer um
> bloco de código, **digite você mesmo** no computador e veja o resultado. Ler
> não basta — é digitando, errando e corrigindo que se aprende a programar.

---

## Índice

**Parte 1 — Primeiros passos**
- Módulo 0 · O que é programar (e como rodar Python)
- Módulo 1 · Variáveis: guardando informação
- Módulo 2 · Os 4 tipos básicos
- Módulo 3 · Texto (strings) em detalhe
- Módulo 4 · Números e contas
- Módulo 5 · Verdadeiro ou falso (booleanos)

**Parte 2 — Guardando muitas coisas**
- Módulo 6 · Listas
- Módulo 7 · Dicionários
- Módulo 8 · Tuplas

**Parte 3 — Tomando decisões e repetindo**
- Módulo 9 · `if`, `else` e o truque do `or`
- Módulo 10 · Loops (`for` e `while`)
- Módulo 11 · Compreensões de lista

**Parte 4 — Organizando o código**
- Módulo 12 · Funções
- Módulo 13 · Módulos e `import`
- Módulo 14 · Classes (uma introdução suave)

**Parte 5 — O seu projeto de verdade**
- Módulo 15 · Banco de dados e SQL
- Módulo 16 · Ferramentas que seu projeto usa
- Módulo 17 · Como funciona uma API (FastAPI)
- Módulo 18 · Lendo um endpoint inteiro, linha por linha

**Apêndices**
- A · Erros comuns e como resolver
- B · Gabarito dos exercícios
- C · Glossário de bolso

---
---

# PARTE 1 — Primeiros passos

## Módulo 0 · O que é programar (e como rodar Python)

**Programar** é dar instruções para o computador, uma de cada vez, na ordem
certa. O computador é obediente, mas burro: ele faz **exatamente** o que você
escreve — nem mais, nem menos. Python é só o idioma que usamos para escrever
essas instruções (e é um dos mais fáceis de ler).

### Seu primeiro programa

Abra o terminal, digite `python3` e aperte Enter. Vai aparecer `>>>`. Isso é o
**modo interativo**, onde você testa uma linha e vê o resultado na hora:

```python
>>> print("Olá, mundo!")
Olá, mundo!
```

- `print(...)` é uma **ordem**: "mostre na tela o que está entre os parênteses".
- `"Olá, mundo!"` é um **texto** (note as aspas — todo texto fica entre aspas).
- A segunda linha, sem `>>>`, é a **resposta** do computador.

### Não tenha medo de erros

Errar faz parte. Quando você escreve algo errado, o Python avisa:

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
um fracasso.

> **Experimente:** digite `print(2 + 2)` e depois `print("2 + 2")`. Por que um
> mostra `4` e o outro mostra `2 + 2`? (Resposta: com aspas vira texto; sem
> aspas vira conta.)

**Exercício 0:** faça o computador se apresentar — imprima seu nome e a frase
"estou aprendendo Python".

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

O `=` aqui **não** é "igual" da matemática; ele significa "**guarde isto nesta
caixa**".

### Você pode trocar o conteúdo

```python
contador = 1
print(contador)      # mostra 1
contador = contador + 1
print(contador)      # mostra 2
```

A linha `contador = contador + 1` lê assim: "pegue o valor atual da caixa, some
1, e guarde de volta na mesma caixa". Isso é muito comum em programação.

### Regras para nomes de variáveis

- Use nomes que **descrevem** o conteúdo: `dose_mg` é melhor que `x`.
- Sem espaços — use `_` para separar: `nome_do_paciente`.
- Não pode começar com número: `2dose` ❌, `dose2` ✔️.

**No seu projeto** (`app.py`, perto do topo), há variáveis exatamente assim:
```python
EVIDENCIA_SCORE = {"A": 100, "B": 75, "C": 50, "D": 25}
```
É uma caixa chamada `EVIDENCIA_SCORE`. (O conteúdo é um "dicionário" — chegaremos
lá no Módulo 7.)

**Exercício 1:** crie três variáveis — `nome` (texto), `idade` (número) e
`febre` (verdadeiro/falso) — e imprima as três.

---

## Módulo 2 · Os 4 tipos básicos

Todo valor em Python tem um **tipo**. Os quatro mais importantes:

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

### Cuidado: número com aspas vira texto!

```python
a = 10
b = "10"
print(a + 5)    # 15  (conta de verdade)
print(b + "5")  # 105 (juntou os textos, não somou!)
```

Esse é um dos erros mais comuns de quem começa. `"10"` é o **texto** "um-zero",
não o número dez.

> **Experimente:** rode `print("10" + 5)`. Vai dar erro, porque o Python não
> sabe somar texto com número. Leia a mensagem — ela diz exatamente isso.

**Exercício 2:** crie uma variável `temperatura = 38.5` e use `type()` para
confirmar que ela é um `float`.

---

## Módulo 3 · Texto (strings) em detalhe

Texto (`str`) é o tipo que você mais vai usar. Vamos explorá-lo.

### Juntando textos

```python
primeiro = "Strepto"
segundo = "coccus"
nome = primeiro + segundo
print(nome)    # Streptococcus
```
O `+` entre textos **gruda** um no outro (chamamos isso de "concatenar").

### f-strings: o jeito moderno de montar texto

Colocar um `f` antes das aspas permite inserir variáveis dentro do texto, usando
`{ }`:

```python
medicamento = "Amoxicilina"
dose = 500
frase = f"{medicamento} {dose} mg de 8 em 8 horas"
print(frase)    # Amoxicilina 500 mg de 8 em 8 horas
```
Tudo que está dentro de `{ }` é **substituído pelo valor da variável**. É muito
mais limpo do que ficar usando `+`.

**No seu projeto** (`app.py`, função `_categorias`):
```python
key = f"{cfg.route}:categorias"
```
Se `cfg.route` for `"bacterias"`, essa linha cria o texto `"bacterias:categorias"`.

### Ferramentas embutidas no texto (métodos)

Todo texto sabe fazer algumas coisas sozinho:

```python
nome = "ampicilina"
print(nome.upper())        # AMPICILINA (tudo maiúsculo)
print(nome.capitalize())   # Ampicilina (primeira maiúscula)
print(len(nome))           # 10 (quantas letras tem)
print("cilina" in nome)    # True ("cilina" está dentro de "ampicilina"?)
```

> **Experimente:** crie `frase = "febre alta"` e descubra o tamanho com
> `len(frase)`. Conte: o espaço também conta como caractere?

**Exercício 3:** com `medicamento = "Azitromicina"` e `dose = 500`, monte com
uma f-string a frase: `"Azitromicina: tomar 500 mg no primeiro dia"`.

---

## Módulo 4 · Números e contas

Python faz contas direto:

```python
print(10 + 3)    # 13  (soma)
print(10 - 3)    # 7   (subtração)
print(10 * 3)    # 30  (multiplicação — usa asterisco)
print(10 / 3)    # 3.333... (divisão — sempre vira decimal)
print(10 // 3)   # 3   (divisão inteira — só a parte inteira)
print(10 % 3)    # 1   (resto da divisão)
print(2 ** 3)    # 8   (potência: 2 elevado a 3)
```

### Misturando com variáveis

```python
dose_unica = 250
vezes_por_dia = 3
total_dia = dose_unica * vezes_por_dia
print(f"Total no dia: {total_dia} mg")   # Total no dia: 750 mg
```

### Arredondar

```python
resistencia = 12.3456
print(round(resistencia, 1))   # 12.3 (arredonda para 1 casa decimal)
```

**No seu projeto** (`app.py`, função `enrich`), há exatamente isso:
```python
"eficacia": round(r["eficacia_pct"] or 0, 1)
```
Pega a eficácia e arredonda para 1 casa decimal antes de mandar para o gráfico.

**Exercício 4:** um medicamento custa R$ 4,50 por comprimido e o tratamento usa
21 comprimidos. Calcule e imprima o custo total com uma f-string.

---

## Módulo 5 · Verdadeiro ou falso (booleanos)

`bool` só tem dois valores: `True` (verdadeiro) e `False` (falso). Eles nascem
de **comparações**:

```python
idade = 70
print(idade > 65)    # True  (maior que)
print(idade < 18)    # False (menor que)
print(idade == 70)   # True  (igual? — note os DOIS sinais de igual)
print(idade != 70)   # False (diferente?)
```

> ⚠️ **Atenção:** comparar usa `==` (dois sinais). Um sinal só (`=`) é para
> **guardar** numa variável. Trocar os dois é o erro nº 1 dos iniciantes.

### Combinando condições

```python
idade = 70
tem_febre = True
print(idade > 65 and tem_febre)   # True  (precisa dos DOIS)
print(idade > 80 or tem_febre)    # True  (basta UM)
print(not tem_febre)              # False (inverte)
```

**Exercício 5:** crie `temperatura = 38.5` e imprima se há febre (temperatura
maior ou igual a 37.8) usando uma comparação.

---
---

# PARTE 2 — Guardando muitas coisas

Até agora cada caixa guardava **um** valor. Mas e quando você tem uma lista de
sintomas, ou vários dados de uma patologia? Para isso existem as **coleções**.

## Módulo 6 · Listas

Uma **lista** guarda vários valores em ordem, dentro de colchetes `[ ]`:

```python
sintomas = ["febre", "tosse", "dor de cabeça"]
print(sintomas)        # ['febre', 'tosse', 'dor de cabeça']
print(len(sintomas))   # 3 (quantos itens tem)
```

### Acessando itens pela posição (índice)

A contagem **começa do zero**. O primeiro item é a posição 0:

```python
sintomas = ["febre", "tosse", "dor de cabeça"]
print(sintomas[0])    # febre        (primeiro)
print(sintomas[1])    # tosse        (segundo)
print(sintomas[-1])   # dor de cabeça (o último, contando de trás)
```

### Mudando e adicionando

```python
sintomas = ["febre", "tosse"]
sintomas.append("calafrios")   # adiciona no fim
print(sintomas)                # ['febre', 'tosse', 'calafrios']

sintomas[0] = "febre alta"     # troca o primeiro
print(sintomas)                # ['febre alta', 'tosse', 'calafrios']
```

**No seu projeto:** quando a API responde com a lista de sintomas de uma
patologia, é exatamente uma lista assim — só que cada item é um dicionário (o
próximo módulo).

> **Experimente:** crie uma lista `doses = [250, 500, 875]` e imprima o item do
> meio. Qual índice é o do meio?

**Exercício 6:** crie uma lista com 3 medicamentos, adicione um quarto com
`.append()`, e imprima o tamanho final da lista.

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

### O `.get()` — acesso seguro

Se você pedir uma chave que não existe com `[ ]`, o programa **quebra**. O
`.get()` evita isso, devolvendo um padrão:

```python
patologia = {"nome": "Pneumonia"}
print(patologia.get("cid10"))          # None (não existe, mas não quebra)
print(patologia.get("cid10", "sem"))   # sem  (devolve "sem" como padrão)
```

**No seu projeto** isso aparece o tempo todo. Em `app.py`:
```python
EVIDENCIA_SCORE.get(tratamento["nivel_evidencia"] or "D", 25)
```
"No dicionário `EVIDENCIA_SCORE`, procure o nível de evidência; se não achar,
use 25." E toda resposta da sua API é um dicionário gigante — abra o `app.py` e
procure por `result = {` para ver um.

> **Experimente:** crie o dicionário `medicamento = {"nome": "Amoxicilina",
> "sus": True}` e imprima só se ele está disponível no SUS.

**Exercício 7:** crie um dicionário representando um medicamento com as chaves
`nome`, `dose_mg` e `disponivel_sus`. Depois imprima a frase
`"Amoxicilina — 500 mg"` usando uma f-string que pega os valores do dicionário.

---

## Módulo 8 · Tuplas

Uma **tupla** é como uma lista, mas com parênteses `( )` e com uma diferença:
**não pode ser mudada** depois de criada. Serve para dados fixos.

```python
cores_do_gram = ("positivo", "negativo")
print(cores_do_gram[0])    # positivo

cores_do_gram[0] = "outro" # ❌ ERRO: tupla não pode mudar
```

Quando usar tupla em vez de lista? Quando os itens **não devem mudar** — isso
deixa o código mais seguro e deixa claro para quem lê: "isto é fixo".

**No seu projeto** (`app.py`, na configuração `AGENT_DOMAINS`):
```python
agent_cols=("nome_cientifico", "nome_comum", "gram",
            "aerobiose", "formato", "resistencia_natural"),
```
As colunas que o sistema lê do banco são uma tupla, porque essa lista é fixa —
não deve ser alterada enquanto o programa roda.

**Exercício 8:** crie uma tupla com os dias da semana e imprima o primeiro e o
último.

---
---

# PARTE 3 — Tomando decisões e repetindo

## Módulo 9 · `if`, `else` e o truque do `or`

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
- A linha de dentro é **indentada** (4 espaços). Essa indentação **não é
  enfeite** — é ela que diz o que está "dentro" do `if`. Em Python, espaço tem
  significado!

### Mais de duas opções: `elif`

```python
nivel = "B"

if nivel == "A":
    print("Evidência forte")
elif nivel == "B":
    print("Evidência moderada")
else:
    print("Evidência fraca ou consenso")
```

`elif` é "senão, se...". O Python testa de cima para baixo e para no primeiro
que for verdadeiro.

### O conceito de "vazio = falso"

Em Python, alguns valores contam como falso sozinhos: `None`, `0`, `""` (texto
vazio) e `[]` (lista vazia). Isso permite escrever de forma curta:

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

### O truque do `or` como valor padrão

```python
nivel = None
nivel_final = nivel or "D"
print(nivel_final)    # D
```
Leia: "use `nivel`; mas **se ele for vazio/None**, use `'D'`". Seu projeto usa
isso para nunca trabalhar com um valor faltando.

**Exercício 9:** crie `idade = 70` e imprima `"idoso"` se for 65 ou mais, senão
`"adulto"`.

---

## Módulo 10 · Loops (repetindo ações)

Quando você quer fazer algo **para cada item** de uma lista, usa o `for`:

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
`range(3)` gera os números 0, 1, 2 (começa do zero, não inclui o 3).

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

**Exercício 10:** dada a lista `notas = ["A", "B", "A", "C"]`, percorra com um
`for` e imprima cada nota com a frase `"Nível de evidência: X"`.

---

## Módulo 11 · Compreensões de lista (o "for" turbinado)

Esse padrão — criar uma lista nova a partir de outra — é tão comum que Python
tem um atalho elegante chamado **compreensão de lista**.

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

### Com filtro

Você pode incluir só alguns itens:
```python
doses = [250, 500, 875]
grandes = [d for d in doses if d >= 500]
print(grandes)    # [500, 875]
```

**Exercício 11:** dada `temperaturas = [36.5, 38.2, 37.0, 39.1]`, crie com uma
compreensão a lista só das temperaturas com febre (≥ 37.8).

---
---

# PARTE 4 — Organizando o código

## Módulo 12 · Funções

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
entregue pode ser guardado numa variável, como fizemos com `resultado`.

### Vários parâmetros e valor padrão

```python
def descreve(medicamento, dose=500):   # dose tem um padrão
    return f"{medicamento} {dose} mg"

print(descreve("Amoxicilina"))        # Amoxicilina 500 mg (usou o padrão)
print(descreve("Azitromicina", 250))  # Azitromicina 250 mg (passou outro)
```

**No seu projeto** (`app.py`) quase tudo são funções. Veja `_fetch_patologia`:
ela recebe o banco e o id, busca a patologia, e a `return` devolve o resultado.
Foi criada para **não repetir** essa mesma busca em cinco lugares diferentes —
exatamente o propósito de uma função.

**Exercício 12:** escreva uma função `tem_febre(temperatura)` que devolve `True`
se a temperatura for ≥ 37.8, senão `False`. Teste com dois valores.

---

## Módulo 13 · Módulos e `import`

Um programa grande não cabe (nem deve caber) num arquivo só. Cada arquivo `.py`
é um **módulo**, e o `import` traz código de um para o outro — ou traz
ferramentas prontas que vêm com o Python.

```python
import math                # traz o módulo de matemática
print(math.sqrt(16))       # 4.0 (raiz quadrada)

from datetime import date  # traz só a ferramenta "date"
print(date.today())        # a data de hoje
```

Duas formas:
- `import math` → traz o módulo inteiro; você usa com `math.alguma_coisa`.
- `from datetime import date` → traz **só** a ferramenta `date`, usada direto.

**No seu projeto** (topo do `app.py`):
```python
import sqlite3                          # ferramenta do banco de dados
from pathlib import Path                # ferramenta de caminhos de arquivo
from fastapi import FastAPI, HTTPException
```
E o `database/build_db.py` importa **os seus próprios arquivos** de dados:
```python
from data_criterios_bacterianas import CRITERIOS_BACTERIANAS
```
Ou seja: o conhecimento médico fica em arquivos separados, e o build os reúne.

**Exercício 13:** importe o módulo `random` e use `random.randint(1, 6)` para
"jogar um dado". Rode algumas vezes e veja o número mudar.

---

## Módulo 14 · Classes (uma introdução suave)

Às vezes você quer agrupar vários dados relacionados sob um mesmo "molde". Para
isso existe a **classe**. Para um iniciante, a regra é: **você ainda não precisa
escrever classes**, mas precisa saber **ler**.

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
- `class Medicamento:` cria o molde.
- `amox = Medicamento("Amoxicilina", 500)` cria **um objeto** a partir do molde.
- `amox.nome` lê um campo desse objeto (com o **ponto**).

**No seu projeto** (`app.py`) existe uma classe simples chamada `AgentDomain`,
usada para guardar a configuração de cada domínio (bacteriano, viral, etc.).
Depois o código acessa os campos com ponto: `cfg.junction`, `cfg.drug_table`.
Sempre que vir `algumacoisa.outracoisa`, pense: "estou pegando um campo de um
objeto".

**Exercício 14:** apenas leia, no `app.py`, a classe `AgentDomain` e a lista
`AGENT_DOMAINS`. Responda: qual é o valor de `drug_table` no domínio
`"bacterias"`?

---
---

# PARTE 5 — O seu projeto de verdade

Agora que você tem a base, vamos olhar o coração do seu sistema.

## Módulo 15 · Banco de dados e SQL

Os dados das 350 patologias não ficam no código — ficam num **banco de dados**
(o arquivo `database/patologias_bacterianas_br.sqlite`). Pense nele como um
conjunto de **planilhas** (chamadas **tabelas**): uma de patologias, uma de
medicamentos, uma de sintomas, etc.

Para pedir dados ao banco, usamos uma linguagem própria, o **SQL**. O comando
mais comum é o `SELECT`:

```sql
SELECT nome, cid10 FROM patologias WHERE id = 1
```
Lê assim: "**selecione** as colunas `nome` e `cid10` **da tabela** `patologias`
**onde** o `id` for 1".

### Como o Python conversa com o banco

```python
import sqlite3
db = sqlite3.connect("database/patologias_bacterianas_br.sqlite")
linha = db.execute("SELECT nome FROM patologias WHERE id = 1").fetchone()
print(linha)
```
- `connect(...)` abre o banco.
- `db.execute("SELECT ...")` envia o comando SQL.
- `.fetchone()` pega **uma** linha do resultado (`.fetchall()` pegaria todas).

**No seu projeto** (`app.py`, função `_fetch_patologia`):
```python
pat = db.execute(
    "SELECT p.nome, p.cid10 FROM patologias p WHERE p.id = ?",
    (patologia_id,),
).fetchone()
```

### O `?` e a regra de ouro da segurança

Note o `?` no lugar do valor, e o valor vindo separado em `(patologia_id,)`.
Isso **não é detalhe** — é segurança. Nunca cole o valor direto no texto do SQL;
sempre use `?` e passe o valor à parte. Isso impede um ataque famoso chamado
"SQL injection". (Há um comentário no seu `app.py` explicando exatamente isso.)

> **Experimente** no terminal (sem Python), explorando o banco direto:
> ```
> sqlite3 database/patologias_bacterianas_br.sqlite "SELECT nome FROM patologias LIMIT 5"
> ```

**Exercício 15:** usando o comando `sqlite3` acima, mude o `LIMIT 5` para
`LIMIT 10` e veja 10 patologias. Depois tente
`"SELECT COUNT(*) FROM patologias"` — o que esse número significa?

---

## Módulo 16 · Ferramentas que seu projeto usa

Estes conceitos são um pouco mais avançados. Você **não precisa dominá-los para
escrever** ainda, mas reconhecê-los te deixa ler o `app.py` com confiança.

### O `with` (abre e fecha sozinho)

```python
with conn_bact() as db:
    pat = db.execute("SELECT ...").fetchone()
# aqui fora, o banco já foi fechado automaticamente
```
O `with` garante que o banco será **fechado no final**, mesmo se acontecer um
erro no meio. É uma rede de segurança.

### `defaultdict` (dicionário com valor padrão)

Um dicionário normal quebra se você acessa uma chave que não existe. O
`defaultdict` já começa com um valor padrão (por exemplo, uma lista vazia),
facilitando agrupar coisas:

```python
from collections import defaultdict
por_medicamento = defaultdict(list)   # toda chave nova começa como []
por_medicamento["amox"].append("dose 1")
por_medicamento["amox"].append("dose 2")
print(por_medicamento["amox"])    # ['dose 1', 'dose 2']
```
Seu projeto usa isso para agrupar posologias e interações por medicamento.

### Decorator (`@`)

A linha com `@` antes de uma função "embrulha" essa função com um poder extra:

```python
@app.get("/health")
def health():
    return {"status": "ok"}
```
`@app.get("/health")` diz ao FastAPI: "quando alguém acessar o endereço
`/health`, chame esta função". Você não precisa entender como o decorator
funciona por dentro — só saber que ele **liga um endereço a uma função**.

**Exercício 16:** no `app.py`, procure todas as linhas que começam com `@app.`.
Cada uma é um endereço da sua API. Liste três deles.

---

## Módulo 17 · Como funciona uma API (FastAPI)

Uma **API** é como um garçom num restaurante:
1. O navegador (cliente) faz um **pedido** a um endereço — ex.: `/api/bacterias/patologia/1`.
2. O servidor (seu `app.py`) **busca os dados** no banco (a cozinha).
3. Devolve uma **resposta** em JSON (que é praticamente um dicionário Python).

```python
@app.get("/api/bacterias/patologia/{patologia_id}")
def bact_detalhe(patologia_id: int):
    return _agent_detalhe(AGENT_DOMAINS["bacterias"], patologia_id)
```

Decifrando linha por linha:
- `@app.get("/api/bacterias/patologia/{patologia_id}")` → o endereço. A parte
  `{patologia_id}` é **variável**: muda conforme a patologia pedida.
- `def bact_detalhe(patologia_id: int):` → a função que responde. O `: int`
  **garante** que o valor recebido é um número inteiro (se vier texto, o FastAPI
  recusa automaticamente — segurança de graça).
- `return ...` → o dicionário devolvido **vira JSON sozinho** e volta para o
  navegador.

### Veja funcionando

Rode o servidor:
```
uvicorn app:app --reload
```
Depois abra no navegador: **`http://localhost:8000/docs`**. O FastAPI gera
sozinho uma página interativa com **todos os seus endpoints** — e mostra as
docstrings que escrevemos no código. Você pode testar cada um clicando.

**Exercício 17:** com o servidor rodando, acesse `http://localhost:8000/health`.
Que resposta aparece? Compare com o `return` da função `health` no `app.py`.

---

## Módulo 18 · Lendo um endpoint inteiro, linha por linha

Hora de juntar tudo. Vamos ler uma versão simplificada de um endpoint real do
seu projeto e reconhecer **cada conceito** que estudamos:

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
1. **Decorator** (Módulo 16): liga o endereço `/api/cronicas/categorias` a esta função.
2. **Função** (Módulo 12): o bloco que responde ao pedido.
3. **`if` + dicionário** (Módulos 9 e 7): "se ainda não calculei isto antes...".
   Isso é um **cache** — guarda o resultado para não consultar o banco toda vez.
4. **`with`** (Módulo 16): abre o banco e garante o fechamento.
5. **SQL** (Módulo 15): pede id, nome e sistema das categorias, em ordem.
6. **`.fetchall()`**: traz todas as linhas encontradas.
7. **Compreensão de lista** (Módulo 11): transforma cada linha em dicionário.
8. **`return`** (Módulo 12): devolve a lista — que o FastAPI converte em JSON.

Se você entendeu esses 8 pontos, **você já consegue ler o seu próprio backend**.
Parabéns — isso é programar de verdade.

**Exercício 18 (final):** abra o `app.py` e encontre a função
`cronicas_patologias` (logo abaixo da que vimos). Ela é parecida, mas tem uma
parte a mais: um `if categoria_id:` que adiciona um filtro ao SQL. Tente
explicar, com suas palavras, o que essa parte faz.

---
---

# APÊNDICES

## Apêndice A · Erros comuns e como resolver

| Mensagem de erro | O que significa | Como resolver |
|------------------|-----------------|---------------|
| `SyntaxError` | Escreveu algo "fora da gramática" do Python | Cheque aspas, parênteses e os dois-pontos `:` |
| `IndentationError` | Espaçamento errado no início da linha | Use sempre 4 espaços dentro de `if`, `for`, `def` |
| `NameError: name 'x' is not defined` | Usou uma variável que não existe | Verifique se escreveu o nome certo / criou antes |
| `TypeError` | Misturou tipos incompatíveis | Ex.: somar texto com número — converta antes |
| `KeyError: 'x'` | Pediu uma chave que não existe no dicionário | Use `.get("x")` em vez de `["x"]` |
| `IndexError` | Pediu uma posição que não existe na lista | A contagem vai de 0 até `len(lista) - 1` |

**Dica de ouro:** sempre leia a **última linha** do erro primeiro. Ela quase
sempre diz o tipo do problema e a linha onde ocorreu.

---

## Apêndice B · Gabarito dos exercícios

```python
# Exercício 0
print("Ian")
print("estou aprendendo Python")

# Exercício 1
nome = "Maria"
idade = 30
febre = True
print(nome, idade, febre)

# Exercício 2
temperatura = 38.5
print(type(temperatura))    # <class 'float'>

# Exercício 3
medicamento = "Azitromicina"
dose = 500
print(f"{medicamento}: tomar {dose} mg no primeiro dia")

# Exercício 4
custo = 4.50 * 21
print(f"Custo total: R$ {custo}")

# Exercício 5
temperatura = 38.5
print(temperatura >= 37.8)   # True

# Exercício 6
meds = ["Amoxicilina", "Azitromicina", "Cefalexina"]
meds.append("Ceftriaxona")
print(len(meds))             # 4

# Exercício 7
medicamento = {"nome": "Amoxicilina", "dose_mg": 500, "disponivel_sus": True}
print(f"{medicamento['nome']} — {medicamento['dose_mg']} mg")

# Exercício 8
dias = ("seg", "ter", "qua", "qui", "sex", "sab", "dom")
print(dias[0], dias[-1])     # seg dom

# Exercício 9
idade = 70
if idade >= 65:
    print("idoso")
else:
    print("adulto")

# Exercício 10
notas = ["A", "B", "A", "C"]
for n in notas:
    print(f"Nível de evidência: {n}")

# Exercício 11
temperaturas = [36.5, 38.2, 37.0, 39.1]
febres = [t for t in temperaturas if t >= 37.8]
print(febres)                # [38.2, 39.1]

# Exercício 12
def tem_febre(temperatura):
    return temperatura >= 37.8
print(tem_febre(38.5))       # True
print(tem_febre(36.5))       # False

# Exercício 13
import random
print(random.randint(1, 6))

# Exercício 14 — leitura: drug_table do domínio "bacterias" é "antibioticos"

# Exercício 15 — COUNT(*) conta quantas patologias existem na tabela

# Exercício 16 — ex.: @app.get("/"), @app.get("/health"), @app.get("/api/bacterias/categorias")

# Exercício 17 — aparece {"status":"ok","dbs":{"patologias_bacterianas":true}}

# Exercício 18 — "se um categoria_id foi informado, acrescenta um filtro WHERE
#                ao SQL para trazer só as patologias daquela categoria"
```

---

## Apêndice C · Glossário de bolso

- **Variável** — caixa com nome que guarda um valor.
- **Tipo** — a natureza de um valor: texto (`str`), inteiro (`int`), decimal (`float`), lógico (`bool`).
- **Lista** `[ ]` — coleção ordenada, acessada por posição (começa em 0).
- **Dicionário** `{ }` — coleção de pares chave → valor, acessada por nome.
- **Tupla** `( )` — como lista, mas imutável (não muda).
- **Função** — bloco de código com nome, reutilizável; recebe parâmetros e pode `return`.
- **Parâmetro** — a "caixa de entrada" de uma função.
- **`return`** — entrega o resultado e encerra a função.
- **Módulo** — um arquivo `.py`; `import` traz código de um para outro.
- **Classe** — molde para criar objetos que agrupam dados.
- **Objeto** — algo criado a partir de uma classe; campos acessados com ponto.
- **SQL** — linguagem para pedir dados ao banco (`SELECT ... FROM ... WHERE`).
- **API** — o "garçom": recebe pedidos em endereços e devolve respostas (JSON).
- **Endpoint** — um endereço da API ligado a uma função (via `@app.get`).
- **JSON** — formato de troca de dados, quase igual a um dicionário Python.
- **Decorator** — a linha com `@` que dá um poder extra a uma função.
- **Cache** — guardar um resultado já calculado para não refazer o trabalho.

---

> **Parabéns por chegar até aqui!** O próximo passo é praticar com o seu próprio
> projeto: tente adicionar um campo numa resposta da API, ou criar um endpoint
> novo bem simples. Programação se aprende fazendo — e agora você tem a base
> para isso. 🚀

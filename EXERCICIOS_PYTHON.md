# Caderno de Exercícios — Python na Prática 🐍✏️

### Companheiro do `APRENDER_PYTHON.md`

Este caderno é **separado** do material principal de propósito: ele reúne
desafios **novos** (diferentes dos exercícios já resolvidos dentro de cada
módulo), organizados pelos mesmos temas, em **três níveis de dificuldade**:

- 🟢 **Iniciante** — aplica diretamente o que foi visto no módulo.
- 🟡 **Intermediário** — combina dois ou mais conceitos, ou pede um pouco mais
  de raciocínio.
- 🔴 **Desafio** — exige juntar vários módulos, ou pensar num caso a mais (uma
  "pegadinha" real de programação).

> **Como usar:** tente resolver **sem olhar o gabarito**. Erre, rode de novo,
> ajuste. Só depois de ter uma resposta (ou de travar de verdade por uns 10
> minutos) consulte o **Gabarito Comentado**, no final deste arquivo. O
> gabarito não só mostra o código — explica **por que** a solução funciona,
> igual ao material principal.
>
> Todos os exercícios podem ser feitos no modo interativo (`python3`) ou em
> um arquivo `.py` que você cria só para praticar (sugestão: crie uma pasta
> `pratica/` no seu projeto e um arquivo por exercício, ex.: `pratica/p1_e3.py`).

---

## Índice

- Parte 1 — Variáveis, tipos, texto, números e booleanos (6 exercícios)
- Parte 2 — Listas, dicionários, tuplas e conjuntos (6 exercícios)
- Parte 3 — Decisões, loops e compreensões (6 exercícios)
- Parte 4 — Funções, módulos, classes e erros (6 exercícios)
- Parte 5 — Banco de dados, JSON, API, testes e git (6 exercícios)
- Desafios finais — três mini-projetos juntando tudo
- Gabarito Comentado

---
---

# PARTE 1 — Variáveis, tipos, texto, números e booleanos

*(Revisa os Módulos 1 a 5 do material principal.)*

### 🟢 P1.1 — Ficha de medicamento

Crie variáveis para representar um medicamento:
`nome` (texto), `dose_mg` (inteiro), `preco_unitario` (decimal),
`disponivel_sus` (booleano). Imprima cada uma com um `print` separado, e
depois imprima uma frase única usando f-string, no formato:

```
Amoxicilina — 500 mg — R$ 0.35 — disponível no SUS
```

(a última parte deve mudar para "não disponível no SUS" se
`disponivel_sus` for `False` — dica: operador ternário, Módulo 10).

---

### 🟢 P1.2 — Conversão de temperatura

Um aparelho retorna a temperatura em **Fahrenheit**, como texto:
`temperatura_f = "101.3"`. A fórmula para converter para Celsius é
`celsius = (fahrenheit - 32) * 5 / 9`.

Converta o texto para `float`, calcule a temperatura em Celsius, arredonde
para 1 casa decimal, e imprima:
```
101.3°F equivalem a 38.5°C
```

---

### 🟡 P1.3 — Validador de dose

Crie três variáveis: `peso_kg = 70`, `dose_mg_por_kg = 15`,
`dose_maxima_mg = 1200`. Calcule `dose_calculada = peso_kg * dose_mg_por_kg`.
Depois, usando comparação (`>`) e o operador ternário, crie uma variável
`dose_final` que vale `dose_calculada` **se** ela não ultrapassar
`dose_maxima_mg`, ou `dose_maxima_mg` caso contrário (ou seja, "limite a
dose ao máximo seguro"). Imprima `dose_final`.

---

### 🟡 P1.4 — Normalizando texto de entrada

Suponha que o nome de um medicamento veio de um formulário, "sujo":
`entrada = "  amoxicilina   "`. Usando métodos de string (`.strip()`,
`.capitalize()`), transforme em `"Amoxicilina"` (sem espaços nas pontas,
primeira letra maiúscula). Depois, verifique com `in` se a palavra
`"cilina"` está contida no resultado.

---

### 🟡 P1.5 — Classificador de febre com `and`/`or`

Dadas as variáveis `temperatura = 39.2`, `idade = 72`, `tem_comorbidade =
True`, escreva uma única expressão booleana (`and`/`or`/`not`, Módulo 5) que
seja `True` quando: **a temperatura é febril (≥ 37.8) E (a idade é ≥ 65 OU
existe comorbidade)**. Guarde o resultado numa variável `alerta_grave` e
imprima.

---

### 🔴 P1.6 — Calculadora de tratamento (tipos + f-string + arredondamento)

Você recebe os seguintes dados, **todos como texto** (como viriam de um
formulário web):
```python
nome_medicamento = "Azitromicina"
dose_mg_texto = "500"
dias_tratamento_texto = "3"
preco_comprimido_texto = "2.875"
```
1. Converta cada valor de texto para o tipo correto (`int` ou `float`).
2. Calcule o custo total: `preco_comprimido * dias_tratamento`.
3. Imprima uma frase única, com o custo arredondado para **2 casas
   decimais**, no formato:
```
Azitromicina 500mg por 3 dia(s) — custo total: R$ 8.62
```

> 💡 **Dica:** `2.875 * 3 = 8.625` — pense em como `round(8.625, 2)` se
> comporta (Python usa "arredondamento bancário" para valores `.5` exatos —
> vale a pena testar e observar o resultado!).

---
---

# PARTE 2 — Listas, dicionários, tuplas e conjuntos

*(Revisa os Módulos 6 a 9 do material principal.)*

### 🟢 P2.1 — Lista de sintomas

Crie a lista
`sintomas = ["febre", "tosse seca", "fadiga", "perda de olfato", "dor de garganta"]`.
1. Imprima quantos sintomas existem.
2. Imprima o primeiro e o último sintoma.
3. Adicione `"dor de cabeça"` ao final.
4. Remova `"fadiga"`.
5. Imprima a lista final, ordenada alfabeticamente (sem alterar a lista
   original — use `sorted`).

---

### 🟢 P2.2 — Ficha de paciente (dicionário)

Crie um dicionário `paciente` com as chaves: `nome`, `idade`, `temperatura`,
`sintomas` (uma lista de strings). Depois:
1. Imprima `f"{nome}, {idade} anos, {temperatura}°C"`.
2. Adicione uma nova chave `"grupo_risco"` com valor `True` ou `False`
   (você decide, baseado na idade).
3. Use `.get("alergias", "nenhuma registrada")` para mostrar um campo que
   **não existe** no dicionário, sem dar erro.

---

### 🟡 P2.3 — Combinação de medicamentos (tupla + desempacotamento)

Crie uma lista de tuplas representando um tratamento combinado:
```python
tratamento = [
    ("Amoxicilina", 500, "8/8h"),
    ("Ácido clavulânico", 125, "8/8h"),
]
```
Percorra com `for nome, dose, intervalo in tratamento`, imprimindo, para cada
item:
```
Amoxicilina 500mg, a cada 8/8h
```
Depois, usando `+`/`.join()`, monte (sem usar `for` desta vez) uma única
string com os nomes separados por `" + "`:
```
Amoxicilina + Ácido clavulânico
```
(dica: compreensão de lista para extrair só os nomes, depois `.join()`).

---

### 🟡 P2.4 — Categorias únicas (set)

Você tem a lista de categorias de várias patologias, com repetições:
```python
categorias = ["Respiratório", "Digestivo", "Respiratório", "Neurológico",
               "Digestivo", "Respiratório", "Dermatológico"]
```
1. Descubra quantas categorias **diferentes** existem, usando `set`.
2. Imprima essas categorias **em ordem alfabética** (lembre: sets não têm
   ordem, então use `sorted()` na conversão de volta para lista).
3. Verifique com `in` se `"Cardiovascular"` está entre as categorias (deve
   dar `False`).

---

### 🟡 P2.5 — Agrupando por categoria (dicionário de listas)

Você tem uma lista de tuplas `(patologia, categoria)`:
```python
dados = [
    ("Pneumonia", "Respiratório"),
    ("Gastrite", "Digestivo"),
    ("Bronquite", "Respiratório"),
    ("Úlcera péptica", "Digestivo"),
    ("Meningite", "Neurológico"),
]
```
Sem usar `defaultdict` (faça "na mão", com `if`/`else` e `.get()`), crie um
dicionário `por_categoria` em que cada chave é uma categoria e o valor é a
**lista de patologias** daquela categoria. Resultado esperado:
```python
{
    "Respiratório": ["Pneumonia", "Bronquite"],
    "Digestivo": ["Gastrite", "Úlcera péptica"],
    "Neurológico": ["Meningite"],
}
```
Depois, refaça usando `defaultdict(list)` (Módulo 18) e compare — qual versão
ficou mais curta?

---

### 🔴 P2.6 — Top 3 por eficácia (ordenação + fatiamento + dicionários aninhados)

Você tem uma lista de dicionários representando medicamentos:
```python
medicamentos = [
    {"nome": "Amoxicilina", "eficacia_pct": 87.6, "linha": 1},
    {"nome": "Azitromicina", "eficacia_pct": 92.1, "linha": 2},
    {"nome": "Doxiciclina", "eficacia_pct": 78.4, "linha": 2},
    {"nome": "Cefalexina", "eficacia_pct": 95.0, "linha": 1},
    {"nome": "Claritromicina", "eficacia_pct": 81.3, "linha": 3},
]
```
1. Ordene a lista por `eficacia_pct`, do **maior para o menor**, usando
   `sorted(..., key=..., reverse=True)`.
2. Pegue só o **top 3** (fatiamento `[:3]`).
3. Para cada um do top 3, imprima:
```
1º lugar: Cefalexina (95.0%, linha 1)
2º lugar: Azitromicina (92.1%, linha 2)
3º lugar: Amoxicilina (87.6%, linha 1)
```
(use `enumerate` começando em 1 — Módulo 11).

---
---

# PARTE 3 — Decisões, loops e compreensões

*(Revisa os Módulos 10 a 12 do material principal.)*

### 🟢 P3.1 — Classificador de temperatura

Escreva, para cada temperatura na lista `[36.2, 37.9, 38.5, 40.1, 35.8]`, uma
classificação usando `if`/`elif`/`else`:
- `< 36.0` → "Hipotermia"
- `36.0` a `37.7` → "Normal"
- `37.8` a `39.0` → "Febre"
- `> 39.0` → "Febre alta"

Imprima, para cada temperatura, `f"{temp}°C: {classificacao}"`.

---

### 🟢 P3.2 — Contando ocorrências com `for`

Dada a lista `niveis = ["A", "B", "A", "C", "B", "A", "D"]`, sem usar nenhuma
função pronta de contagem, percorra com `for` e conte quantas vezes aparece
cada letra, guardando o resultado num dicionário (use o padrão "se a chave já
existe, soma 1; senão, comece em 1" — pode ser com `if`/`else` ou com
`.get(chave, 0) + 1`).

Resultado esperado:
```python
{"A": 3, "B": 2, "C": 1, "D": 1}
```

---

### 🟡 P3.3 — `while` com acumulador (posologia)

Um paciente precisa tomar 1 comprimido de 8 em 8 horas, totalizando 21
comprimidos. Usando `while`, simule a passagem do tempo: comece com
`hora = 0` e `comprimidos_restantes = 21`. A cada volta do loop, se
`hora % 8 == 0` (Módulo 4 — operador `%`), "tome" um comprimido (diminua
`comprimidos_restantes` em 1) e imprima `f"Hora {hora}: tomar comprimido
({comprimidos_restantes} restantes)"`. Pare o `while` quando
`comprimidos_restantes == 0`. Some `1` a `hora` a cada volta do loop (não só
quando toma o comprimido!).

> 💡 **Dica:** isso é mais lento que necessário de propósito — serve para
> praticar `while` + `%` juntos. Na vida real, você calcularia direto com
> `21 * 8 = 168` horas.

---

### 🟡 P3.4 — `break`/`continue` numa busca

Dada a lista de pacientes (dicionários):
```python
pacientes = [
    {"nome": "Ana", "temperatura": 36.5},
    {"nome": "Bruno", "temperatura": 39.2},
    {"nome": "Carla", "temperatura": 37.0},
    {"nome": "Davi", "temperatura": 40.1},
]
```
1. Percorra a lista. Para cada paciente com `temperatura < 37.0`, use
   `continue` para pular (não imprimir nada).
2. Para os demais, imprima `f"{nome}: {temperatura}°C"`.
3. Assim que encontrar o **primeiro** paciente com `temperatura > 39.5`,
   imprima `f"ALERTA: {nome} está em estado grave!"` e use `break` para parar
   o loop imediatamente (não verificar os pacientes seguintes).

---

### 🟡 P3.5 — Compreensão com múltiplas condições

Dada a lista de medicamentos (mesma estrutura de P2.6):
```python
medicamentos = [
    {"nome": "Amoxicilina", "eficacia_pct": 87.6, "linha": 1},
    {"nome": "Azitromicina", "eficacia_pct": 92.1, "linha": 2},
    {"nome": "Doxiciclina", "eficacia_pct": 78.4, "linha": 2},
    {"nome": "Cefalexina", "eficacia_pct": 95.0, "linha": 1},
]
```
Usando **uma única compreensão de lista**, crie a lista dos **nomes** dos
medicamentos que são de **1ª linha** (`linha == 1`) **E** têm
`eficacia_pct >= 85`. Resultado esperado: `["Amoxicilina", "Cefalexina"]`.

---

### 🔴 P3.6 — Tabela de doses (loop aninhado + f-string formatada)

Para os medicamentos `["Amoxicilina", "Azitromicina"]` e as doses em mg
`[250, 500, 875]`, use **dois `for` aninhados** para imprimir uma tabela de
custo, sabendo que o preço por mg é `R$ 0.01`:
```
Amoxicilina 250mg -> R$ 2.50
Amoxicilina 500mg -> R$ 5.00
Amoxicilina 875mg -> R$ 8.75
Azitromicina 250mg -> R$ 2.50
Azitromicina 500mg -> R$ 5.00
Azitromicina 875mg -> R$ 8.75
```
Use f-string com `:.2f` para o valor em reais (Módulo 3).

---
---

# PARTE 4 — Funções, módulos, classes e erros

*(Revisa os Módulos 13 a 16 do material principal.)*

### 🟢 P4.1 — Função de classificação

Escreva uma função `classifica_temperatura(temp)` que devolve `"Hipotermia"`,
`"Normal"`, `"Febre"` ou `"Febre alta"`, usando os mesmos limites de P3.1.
Teste chamando a função para `[36.2, 37.9, 38.5, 40.1]` dentro de um `for`,
imprimindo o resultado de cada chamada.

---

### 🟢 P4.2 — Função com valor padrão

Escreva uma função `calcula_dose(peso_kg, mg_por_kg=10)` que devolve
`peso_kg * mg_por_kg`. Chame-a de duas formas: só com `peso_kg` (usando o
padrão `10`) e passando os dois argumentos. Imprima os dois resultados.

---

### 🟡 P4.3 — Função que devolve uma tupla

Escreva uma função `analisa_temperaturas(lista)` que recebe uma lista de
números e devolve **uma tupla** com `(menor, maior, media)` — a média é
`sum(lista) / len(lista)`. Chame com
`analisa_temperaturas([36.5, 38.2, 37.0, 39.1])`, desempacote o resultado em
três variáveis (Módulo 8) e imprima cada uma, com a média arredondada para 1
casa decimal.

---

### 🟡 P4.4 — `try`/`except` num conversor seguro

Escreva uma função `para_float_seguro(texto)` que tenta converter `texto` para
`float` com `try`/`except ValueError`. Se der certo, devolve o número. Se
falhar, devolve `None`. Teste com uma lista
`["38.5", "37.2", "abc", "39.0", ""]`, percorrendo com `for` e imprimindo, para
cada item, `f"{item!r} -> {resultado}"` (o `!r` mostra o texto entre aspas na
saída, útil para ver strings vazias).

---

### 🟡 P4.5 — Classe `Paciente` simples

Crie uma classe `Paciente` com `__init__(self, nome, idade, temperatura)` que
guarda os três valores como `self.nome`, `self.idade`, `self.temperatura`.
Adicione um método `tem_febre(self)` que devolve `True`/`False` (use a regra
`temperatura >= 37.8`). Crie dois objetos `Paciente` diferentes e, para cada
um, imprima `f"{nome}: febre = {tem_febre()}"`.

---

### 🔴 P4.6 — Validador de cadastro com várias exceções

Escreva uma função `valida_cadastro(dados)` que recebe um dicionário com
`"nome"`, `"idade"` (texto) e `"temperatura"` (texto), e:

1. Tenta converter `"idade"` para `int` e `"temperatura"` para `float`. Se
   alguma conversão falhar (`ValueError`), levante (`raise`) um `ValueError`
   próprio com a mensagem `"idade ou temperatura inválida"`.
2. Se `"nome"` estiver vazio (string vazia), levante `ValueError("nome é
   obrigatório")`.
3. Se tudo estiver certo, devolva um novo dicionário com os valores já
   convertidos: `{"nome": ..., "idade": int, "temperatura": float}`.

Teste com três dicionários: um válido, um com idade `"trinta"` (texto não
numérico), e um com `"nome": ""`. Para os dois últimos, use `try`/`except
ValueError as erro` ao **chamar** a função, e imprima `f"Erro: {erro}"`.

---
---

# PARTE 5 — Banco de dados, JSON, API, testes e git

*(Revisa os Módulos 17 a 23 do material principal. Estes exercícios usam o
seu projeto de verdade — rode-os dentro da pasta `/home/user/Ia` ou
equivalente na sua máquina.)*

### 🟢 P5.1 — Explorando o banco pelo terminal

No terminal, dentro da pasta do projeto, rode:
```bash
sqlite3 database/patologias_bacterianas_br.sqlite ".tables"
```
Isso lista **todas as tabelas** do banco. Escolha três tabelas que você
reconhece dos módulos anteriores (ex.: `patologias`, `categorias_patologias`,
`antibioticos`) e, para cada uma, rode:
```bash
sqlite3 database/patologias_bacterianas_br.sqlite "SELECT * FROM nome_da_tabela LIMIT 3"
```
Anote (num comentário, ou só observando) quais colunas cada tabela tem.

---

### 🟢 P5.2 — Consulta Python ao banco

Escreva um script `.py` que:
1. Conecta a `database/patologias_bacterianas_br.sqlite` com `sqlite3.connect`.
2. Define `db.row_factory = sqlite3.Row` (Módulo 18).
3. Executa `SELECT nome, cid10, mortalidade_br FROM patologias ORDER BY mortalidade_br DESC LIMIT 5`.
4. Para cada linha (`.fetchall()`), imprime
   `f"{nome} ({cid10}): mortalidade {mortalidade_br}%"`.
5. Fecha a conexão (ou melhor: use `with` se você escreveu seu próprio
   `@contextmanager`, ou simplesmente `db.close()` no final).

---

### 🟡 P5.3 — De linha do banco a JSON

Pegue o resultado de uma consulta (`SELECT id, nome, cid10 FROM patologias
LIMIT 3`), transforme cada linha em dicionário com `dict(row)` (Módulo 17), e
depois use `json.dumps(lista, indent=2, ensure_ascii=False)` (Módulo 19) para
imprimir o resultado formatado como JSON. Compare visualmente com o que você
vê em `http://localhost:8000/api/bacterias/categorias` no navegador (Módulo
20) — é o **mesmo formato**.

---

### 🟡 P5.4 — Testando um endpoint com `assert`

Com o servidor rodando (`uvicorn app:app --reload`), escreva um script que:
1. Usa `urllib.request.urlopen` (Módulo 22) para buscar
   `http://localhost:8000/health`.
2. Converte a resposta com `json.loads`.
3. Usa `assert resposta["status"] == "ok"`.
4. Usa `assert resposta["dbs"]["patologias_bacterianas"] == True`.
5. Se nenhum `assert` falhar, imprima `"Healthcheck OK!"`.

Esse é, em miniatura, o tipo de verificação automática que poderia rodar antes
de cada deploy.

---

### 🟡 P5.5 — Um novo endpoint simples (leitura + escrita guiada)

No `app.py` (numa cópia/branch de teste — não precisa fazer commit disso),
adicione um endpoint novo:
```python
@app.get("/api/estatisticas/total-patologias")
def total_patologias():
    with conn_bact() as db:
        total = db.execute("SELECT COUNT(*) AS total FROM patologias").fetchone()
    return {"total": total["total"]}
```
1. Reinicie o servidor (ou use `--reload`).
2. Acesse `http://localhost:8000/api/estatisticas/total-patologias` no
   navegador.
3. Confira em `/docs` que o novo endpoint aparece automaticamente.
4. **Desfaça a alteração** depois (`git checkout -- app.py` ou removendo
   manualmente), já que era só para praticar.

---

### 🔴 P5.6 — Mini fluxo de git (sem mexer no projeto principal)

Em uma pasta **separada**, fora do projeto (ex.: `~/pratica-git/`):
1. Crie uma pasta nova, entre nela, e rode `git init`.
2. Crie um arquivo `notas.py` com uma função qualquer (ex.: `tem_febre`).
3. Rode `git add notas.py` e `git commit -m "Adiciona função tem_febre"`.
4. Crie uma branch: `git checkout -b adiciona-funcao-extra`.
5. Adicione outra função ao arquivo (ex.: `classifica_idade`), faça
   `git add` e `git commit -m "Adiciona classifica_idade"`.
6. Rode `git log --oneline` e observe os dois commits, um em cada branch.
7. Volte para a branch principal com `git checkout main` (ou `master`,
   dependendo da configuração) e repare que a segunda função **não está**
   lá — ela só existe na branch `adiciona-funcao-extra`, até que alguém faça
   o merge.

Esse exercício não usa o projeto de patologias — é só para você sentir, na
prática e sem risco, o fluxo `commit` → `branch` → `commit` → `checkout` que o
Módulo 23 descreveu.

---
---

# DESAFIOS FINAIS — Mini-projetos juntando tudo

Estes três desafios não têm "módulo de origem" único — eles juntam várias
partes do curso, como o seu próprio `app.py` faz. Tente resolver cada um do
zero, num arquivo `.py` próprio.

### 🔴 Desafio 1 — Triagem de pacientes

Você recebe uma lista de pacientes:
```python
pacientes = [
    {"nome": "Ana",   "idade": 34, "temperatura": 36.8, "comorbidade": False},
    {"nome": "Bruno", "idade": 71, "temperatura": 39.4, "comorbidade": True},
    {"nome": "Carla", "idade": 45, "temperatura": 38.1, "comorbidade": False},
    {"nome": "Davi",  "idade": 80, "temperatura": 37.2, "comorbidade": True},
    {"nome": "Eva",   "idade": 22, "temperatura": 40.2, "comorbidade": False},
]
```
1. Escreva uma função `classifica_risco(paciente)` que devolve `"Alto"`,
   `"Médio"` ou `"Baixo"`, segundo a regra:
   - `"Alto"`: temperatura ≥ 39.0, **ou** (idade ≥ 65 **e** comorbidade)
   - `"Médio"`: temperatura ≥ 37.8 (febre), mas não se enquadra em "Alto"
   - `"Baixo"`: caso contrário
2. Use uma compreensão de dicionário (Módulo 12) para criar
   `{nome: classifica_risco(p) for p in pacientes}` — note que você precisa
   pegar `p["nome"]` como chave, não `p` inteiro.
3. Usando `defaultdict(list)` (Módulo 18), agrupe os **nomes** dos pacientes
   por nível de risco: `{"Alto": [...], "Médio": [...], "Baixo": [...]}`.
4. Imprima o resultado final com `json.dumps(..., indent=2, ensure_ascii=False)`
   (Módulo 19) — repare que `defaultdict` precisa virar `dict(...)` antes,
   porque `json.dumps` não sabe lidar com `defaultdict` diretamente (tente
   sem o `dict(...)` primeiro e leia o erro!).

---

### 🔴 Desafio 2 — Consulta + agrupamento real no banco

Usando o banco `database/patologias_bacterianas_br.sqlite`:
1. Escreva uma consulta SQL (Módulo 17) que traga `nome` e `categoria_id` de
   **todas** as patologias.
2. Em Python, agrupe os nomes por `categoria_id` usando `defaultdict(list)`
   (sem usar `GROUP BY` do SQL desta vez — pratique o agrupamento em Python).
3. Para cada `categoria_id`, imprima quantas patologias existem e os 3
   primeiros nomes (ordenados alfabeticamente, fatiamento `[:3]`).
4. **Bônus:** refaça o passo 1 usando `JOIN` com `categorias_patologias` para
   trazer o **nome** da categoria em vez do `categoria_id` numérico, e
   compare a legibilidade do resultado.

---

### 🔴 Desafio 3 — Endpoint completo "do zero" (mental ou real)

Sem olhar o `app.py`, tente **escrever do zero** (num arquivo separado, ou só
no papel/numa anotação) um endpoint FastAPI que:
1. Recebe um `patologia_id` no caminho da URL (`{patologia_id}`, tipo `int`).
2. Recebe um parâmetro opcional `incluir_sintomas` (booleano, padrão
   `False`) como query parameter.
3. Abre o banco com `with conn_bact() as db:`.
4. Busca a patologia com `_fetch_patologia(db, patologia_id)` (que já
   levanta 404 se não existir — você não precisa reimplementar isso).
5. Monta um dicionário de resposta com `id`, `nome`, `cid10`.
6. **Se** `incluir_sintomas` for `True`, busca também os sintomas (com
   `_fetch_clinical`, que devolve uma tupla — Módulo 8) e adiciona ao
   dicionário de resposta.
7. Devolve o dicionário (vira JSON automaticamente).

Depois, **compare** sua versão com algum endpoint parecido já existente no
`app.py` — quais diferenças você encontrou? Tudo bem se sua versão for
diferente; o objetivo é treinar a **estrutura mental** de um endpoint, não
decorar sintaxe.

---
---

# GABARITO COMENTADO

> Use este gabarito **depois** de tentar. Cada solução vem com uma nota curta
> sobre o porquê — se algo aqui não fizer sentido, volte ao módulo indicado
> entre parênteses no enunciado original.

## Parte 1

```python
# P1.1
nome = "Amoxicilina"
dose_mg = 500
preco_unitario = 0.35
disponivel_sus = True

print(nome)
print(dose_mg)
print(preco_unitario)
print(disponivel_sus)

status_sus = "disponível no SUS" if disponivel_sus else "não disponível no SUS"
print(f"{nome} — {dose_mg} mg — R$ {preco_unitario} — {status_sus}")

# P1.2
temperatura_f = "101.3"
fahrenheit = float(temperatura_f)
celsius = round((fahrenheit - 32) * 5 / 9, 1)
print(f"{fahrenheit}°F equivalem a {celsius}°C")

# P1.3
peso_kg = 70
dose_mg_por_kg = 15
dose_maxima_mg = 1200
dose_calculada = peso_kg * dose_mg_por_kg          # 1050
dose_final = dose_calculada if dose_calculada <= dose_maxima_mg else dose_maxima_mg
print(dose_final)   # 1050 (não ultrapassou o máximo)

# P1.4
entrada = "  amoxicilina   "
limpo = entrada.strip().capitalize()
print(limpo)              # Amoxicilina
print("cilina" in limpo)  # True

# P1.5
temperatura = 39.2
idade = 72
tem_comorbidade = True
alerta_grave = temperatura >= 37.8 and (idade >= 65 or tem_comorbidade)
print(alerta_grave)   # True

# P1.6
nome_medicamento = "Azitromicina"
dose_mg = int("500")
dias_tratamento = int("3")
preco_comprimido = float("2.875")

custo_total = preco_comprimido * dias_tratamento   # 8.625
print(f"{nome_medicamento} {dose_mg}mg por {dias_tratamento} dia(s) — "
      f"custo total: R$ {custo_total:.2f}")
# Azitromicina 500mg por 3 dia(s) — custo total: R$ 8.62
#
# Nota: 8.625 vira 8.62 (não 8.63!) por causa do "arredondamento bancário"
# do Python (round-half-to-even) combinado com a forma como 8.625 é
# representado internamente em binário (não é exatamente 8.625). Isso é
# normal e acontece em praticamente toda linguagem de programação — para
# valores monetários "de verdade" em produção, projetos costumam usar o
# módulo `decimal`, mas isso foge do escopo deste curso.
```

## Parte 2

```python
# P2.1
sintomas = ["febre", "tosse seca", "fadiga", "perda de olfato", "dor de garganta"]
print(len(sintomas))          # 5
print(sintomas[0], sintomas[-1])
sintomas.append("dor de cabeça")
sintomas.remove("fadiga")
print(sorted(sintomas))
print(sintomas)  # a lista original mantém a ordem de inserção

# P2.2
paciente = {
    "nome": "Maria",
    "idade": 68,
    "temperatura": 38.2,
    "sintomas": ["febre", "tosse"],
}
print(f"{paciente['nome']}, {paciente['idade']} anos, {paciente['temperatura']}°C")
paciente["grupo_risco"] = paciente["idade"] >= 65
print(paciente.get("alergias", "nenhuma registrada"))

# P2.3
tratamento = [
    ("Amoxicilina", 500, "8/8h"),
    ("Ácido clavulânico", 125, "8/8h"),
]
for nome, dose, intervalo in tratamento:
    print(f"{nome} {dose}mg, a cada {intervalo}")

nomes = [nome for nome, dose, intervalo in tratamento]
print(" + ".join(nomes))   # Amoxicilina + Ácido clavulânico

# P2.4
categorias = ["Respiratório", "Digestivo", "Respiratório", "Neurológico",
               "Digestivo", "Respiratório", "Dermatológico"]
unicas = set(categorias)
print(len(unicas))               # 4
print(sorted(unicas))            # ['Dermatológico', 'Digestivo', 'Neurológico', 'Respiratório']
print("Cardiovascular" in unicas)  # False

# P2.5 — versão "na mão"
dados = [
    ("Pneumonia", "Respiratório"),
    ("Gastrite", "Digestivo"),
    ("Bronquite", "Respiratório"),
    ("Úlcera péptica", "Digestivo"),
    ("Meningite", "Neurológico"),
]
por_categoria = {}
for nome, categoria in dados:
    if categoria not in por_categoria:
        por_categoria[categoria] = []
    por_categoria[categoria].append(nome)
print(por_categoria)

# P2.5 — versão com defaultdict (mais curta)
from collections import defaultdict
por_categoria2 = defaultdict(list)
for nome, categoria in dados:
    por_categoria2[categoria].append(nome)
print(dict(por_categoria2))
# Nota: a versão com defaultdict elimina o "if not in" — menos repetição.

# P2.6
medicamentos = [
    {"nome": "Amoxicilina", "eficacia_pct": 87.6, "linha": 1},
    {"nome": "Azitromicina", "eficacia_pct": 92.1, "linha": 2},
    {"nome": "Doxiciclina", "eficacia_pct": 78.4, "linha": 2},
    {"nome": "Cefalexina", "eficacia_pct": 95.0, "linha": 1},
    {"nome": "Claritromicina", "eficacia_pct": 81.3, "linha": 3},
]
ordenado = sorted(medicamentos, key=lambda m: m["eficacia_pct"], reverse=True)
top3 = ordenado[:3]
for posicao, med in enumerate(top3, start=1):    # start=1 começa a contagem em 1
    print(f"{posicao}º lugar: {med['nome']} ({med['eficacia_pct']}%, linha {med['linha']})")
```

## Parte 3

```python
# P3.1
temperaturas = [36.2, 37.9, 38.5, 40.1, 35.8]
for temp in temperaturas:
    if temp < 36.0:
        classificacao = "Hipotermia"
    elif temp <= 37.7:
        classificacao = "Normal"
    elif temp <= 39.0:
        classificacao = "Febre"
    else:
        classificacao = "Febre alta"
    print(f"{temp}°C: {classificacao}")

# P3.2
niveis = ["A", "B", "A", "C", "B", "A", "D"]
contagem = {}
for n in niveis:
    contagem[n] = contagem.get(n, 0) + 1
print(contagem)   # {'A': 3, 'B': 2, 'C': 1, 'D': 1}

# P3.3
hora = 0
comprimidos_restantes = 21
while comprimidos_restantes > 0:
    if hora % 8 == 0:
        comprimidos_restantes -= 1
        print(f"Hora {hora}: tomar comprimido ({comprimidos_restantes} restantes)")
    hora += 1

# P3.4
pacientes = [
    {"nome": "Ana", "temperatura": 36.5},
    {"nome": "Bruno", "temperatura": 39.2},
    {"nome": "Carla", "temperatura": 37.0},
    {"nome": "Davi", "temperatura": 40.1},
]
for p in pacientes:
    if p["temperatura"] < 37.0:
        continue
    print(f"{p['nome']}: {p['temperatura']}°C")
    if p["temperatura"] > 39.5:
        print(f"ALERTA: {p['nome']} está em estado grave!")
        break

# P3.5
medicamentos = [
    {"nome": "Amoxicilina", "eficacia_pct": 87.6, "linha": 1},
    {"nome": "Azitromicina", "eficacia_pct": 92.1, "linha": 2},
    {"nome": "Doxiciclina", "eficacia_pct": 78.4, "linha": 2},
    {"nome": "Cefalexina", "eficacia_pct": 95.0, "linha": 1},
]
primeira_linha_boa = [m["nome"] for m in medicamentos if m["linha"] == 1 and m["eficacia_pct"] >= 85]
print(primeira_linha_boa)   # ['Amoxicilina', 'Cefalexina']

# P3.6
nomes = ["Amoxicilina", "Azitromicina"]
doses = [250, 500, 875]
preco_por_mg = 0.01
for nome in nomes:
    for dose in doses:
        custo = dose * preco_por_mg
        print(f"{nome} {dose}mg -> R$ {custo:.2f}")
```

## Parte 4

```python
# P4.1
def classifica_temperatura(temp):
    if temp < 36.0:
        return "Hipotermia"
    elif temp <= 37.7:
        return "Normal"
    elif temp <= 39.0:
        return "Febre"
    else:
        return "Febre alta"

for temp in [36.2, 37.9, 38.5, 40.1]:
    print(f"{temp}°C: {classifica_temperatura(temp)}")

# P4.2
def calcula_dose(peso_kg, mg_por_kg=10):
    return peso_kg * mg_por_kg

print(calcula_dose(70))        # 700 (usa o padrão 10)
print(calcula_dose(70, 15))    # 1050

# P4.3
def analisa_temperaturas(lista):
    return min(lista), max(lista), sum(lista) / len(lista)

menor, maior, media = analisa_temperaturas([36.5, 38.2, 37.0, 39.1])
print(menor)               # 36.5
print(maior)               # 39.1
print(round(media, 1))     # 37.7

# P4.4
def para_float_seguro(texto):
    try:
        return float(texto)
    except ValueError:
        return None

for item in ["38.5", "37.2", "abc", "39.0", ""]:
    resultado = para_float_seguro(item)
    print(f"{item!r} -> {resultado}")

# P4.5
class Paciente:
    def __init__(self, nome, idade, temperatura):
        self.nome = nome
        self.idade = idade
        self.temperatura = temperatura

    def tem_febre(self):
        return self.temperatura >= 37.8

p1 = Paciente("Ana", 34, 36.8)
p2 = Paciente("Bruno", 71, 39.4)
for p in (p1, p2):
    print(f"{p.nome}: febre = {p.tem_febre()}")

# P4.6
def valida_cadastro(dados):
    if not dados["nome"]:
        raise ValueError("nome é obrigatório")
    try:
        idade = int(dados["idade"])
        temperatura = float(dados["temperatura"])
    except ValueError:
        raise ValueError("idade ou temperatura inválida")
    return {"nome": dados["nome"], "idade": idade, "temperatura": temperatura}

casos = [
    {"nome": "Ana", "idade": "34", "temperatura": "36.8"},
    {"nome": "Bruno", "idade": "trinta", "temperatura": "39.4"},
    {"nome": "", "idade": "45", "temperatura": "37.0"},
]
for caso in casos:
    try:
        print(valida_cadastro(caso))
    except ValueError as erro:
        print(f"Erro: {erro}")
# {'nome': 'Ana', 'idade': 34, 'temperatura': 36.8}
# Erro: idade ou temperatura inválida
# Erro: nome é obrigatório
#
# Nota: a checagem do nome vem ANTES do try de conversão no código, mas o
# 3º caso tem idade/temperatura válidas — então é o "if not dados['nome']"
# que dispara primeiro. A ORDEM dos `if`/`try` importa!
```

## Parte 5

```python
# P5.1 — comandos de terminal, sem "resultado" fixo:
#   sqlite3 database/patologias_bacterianas_br.sqlite ".tables"
#   sqlite3 database/patologias_bacterianas_br.sqlite "SELECT * FROM patologias LIMIT 3"
#   sqlite3 database/patologias_bacterianas_br.sqlite "SELECT * FROM categorias_patologias LIMIT 3"
#   sqlite3 database/patologias_bacterianas_br.sqlite "SELECT * FROM antibioticos LIMIT 3"

# P5.2
import sqlite3

db = sqlite3.connect("database/patologias_bacterianas_br.sqlite")
db.row_factory = sqlite3.Row
rows = db.execute(
    "SELECT nome, cid10, mortalidade_br FROM patologias ORDER BY mortalidade_br DESC LIMIT 5"
).fetchall()
for r in rows:
    print(f"{r['nome']} ({r['cid10']}): mortalidade {r['mortalidade_br']}%")
db.close()

# P5.3
import json

db = sqlite3.connect("database/patologias_bacterianas_br.sqlite")
db.row_factory = sqlite3.Row
rows = db.execute("SELECT id, nome, cid10 FROM patologias LIMIT 3").fetchall()
lista = [dict(r) for r in rows]
print(json.dumps(lista, indent=2, ensure_ascii=False))
db.close()

# P5.4
import urllib.request

with urllib.request.urlopen("http://localhost:8000/health") as resposta_http:
    resposta = json.loads(resposta_http.read())

assert resposta["status"] == "ok"
assert resposta["dbs"]["patologias_bacterianas"] == True
print("Healthcheck OK!")

# P5.5 — endpoint adicionado temporariamente, depois revertido com:
#   git checkout -- app.py

# P5.6 — sequência de comandos no terminal, sem "resultado" de código:
#   mkdir ~/pratica-git && cd ~/pratica-git
#   git init
#   echo "def tem_febre(t): return t >= 37.8" > notas.py
#   git add notas.py
#   git commit -m "Adiciona função tem_febre"
#   git checkout -b adiciona-funcao-extra
#   echo "def classifica_idade(i): return 'idoso' if i >= 65 else 'adulto'" >> notas.py
#   git add notas.py
#   git commit -m "Adiciona classifica_idade"
#   git log --oneline
#   git checkout main
#   cat notas.py   # classifica_idade NÃO aparece aqui — só na outra branch
```

## Desafios finais

```python
# Desafio 1
from collections import defaultdict
import json

pacientes = [
    {"nome": "Ana",   "idade": 34, "temperatura": 36.8, "comorbidade": False},
    {"nome": "Bruno", "idade": 71, "temperatura": 39.4, "comorbidade": True},
    {"nome": "Carla", "idade": 45, "temperatura": 38.1, "comorbidade": False},
    {"nome": "Davi",  "idade": 80, "temperatura": 37.2, "comorbidade": True},
    {"nome": "Eva",   "idade": 22, "temperatura": 40.2, "comorbidade": False},
]

def classifica_risco(paciente):
    if paciente["temperatura"] >= 39.0 or (paciente["idade"] >= 65 and paciente["comorbidade"]):
        return "Alto"
    elif paciente["temperatura"] >= 37.8:
        return "Médio"
    else:
        return "Baixo"

risco_por_paciente = {p["nome"]: classifica_risco(p) for p in pacientes}
print(risco_por_paciente)

por_risco = defaultdict(list)
for p in pacientes:
    por_risco[classifica_risco(p)].append(p["nome"])

print(json.dumps(dict(por_risco), indent=2, ensure_ascii=False))
# {
#   "Baixo": ["Ana"],
#   "Alto": ["Bruno", "Eva"],
#   "Médio": ["Carla", "Davi"]
# }

# Desafio 2
import sqlite3
from collections import defaultdict

db = sqlite3.connect("database/patologias_bacterianas_br.sqlite")
db.row_factory = sqlite3.Row
rows = db.execute("SELECT nome, categoria_id FROM patologias").fetchall()

por_categoria = defaultdict(list)
for r in rows:
    por_categoria[r["categoria_id"]].append(r["nome"])

for categoria_id, nomes in por_categoria.items():
    nomes_ordenados = sorted(nomes)
    print(f"Categoria {categoria_id}: {len(nomes)} patologias")
    print(f"  Exemplos: {nomes_ordenados[:3]}")

# Bônus — com JOIN para trazer o nome da categoria:
rows2 = db.execute("""
    SELECT p.nome, c.nome AS categoria
    FROM patologias p
    JOIN categorias_patologias c ON c.id = p.categoria_id
""").fetchall()

por_categoria_nome = defaultdict(list)
for r in rows2:
    por_categoria_nome[r["categoria"]].append(r["nome"])

for categoria, nomes in por_categoria_nome.items():
    print(f"{categoria}: {len(nomes)} patologias")

db.close()

# Desafio 3 — uma possível solução (a sua pode variar um pouco):
@app.get("/api/bacterias/patologia/{patologia_id}/resumo")
def bact_resumo(patologia_id: int, incluir_sintomas: bool = False):
    with conn_bact() as db:
        pat = _fetch_patologia(db, patologia_id)
        resultado = {
            "id": pat["id"],
            "nome": pat["nome"],
            "cid10": pat["cid10"],
        }
        if incluir_sintomas:
            sintomas, criterios, escores = _fetch_clinical(db, patologia_id)
            resultado["sintomas"] = sintomas
    return resultado
#
# Pontos de atenção comuns:
# - `incluir_sintomas: bool = False` — o FastAPI converte "true"/"false" da
#   URL automaticamente para bool (Módulo 20).
# - `_fetch_patologia` já levanta HTTPException(404, ...) sozinha — não
#   precisamos repetir esse `if`.
# - `_fetch_clinical` devolve uma TUPLA de 3 listas (Módulo 8) — por isso o
#   desempacotamento em `sintomas, criterios, escores`, mesmo usando só o
#   primeiro item.
# - Tudo dentro do `with conn_bact() as db:` para reusar a MESMA conexão nas
#   duas buscas, em vez de abrir o banco duas vezes.
```

---

> **Fim do caderno.** Se você chegou até aqui tendo tentado os 30 exercícios e
> os 3 desafios finais, você praticou — na ordem — quase todos os conceitos do
> `APRENDER_PYTHON.md`, aplicados ao **seu próprio projeto**. O próximo passo
> natural é olhar uma funcionalidade real que você queira adicionar ao painel
> de patologias e tentar planejar, sozinho, quais desses blocos (variáveis,
> condições, loops, funções, SQL, endpoint) ela vai precisar. 🚀

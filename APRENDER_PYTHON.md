# Aprender Python através deste projeto 🐍

Um guia de estudos **para iniciantes**, do zero até entender o código que roda
o seu painel clínico de patologias. A ideia é simples: em vez de estudar Python
com exemplos genéricos, você aprende cada conceito **olhando onde ele aparece no
seu próprio projeto**.

> Como usar este guia: estude **um módulo por vez, na ordem**. Em cada módulo
> você tem (1) o conceito, (2) **onde isso aparece no seu código**, (3) um
> exemplo e (4) um exercício. Não pule — cada módulo depende do anterior.

---

## Como praticar sem medo de quebrar nada

Antes de tudo, dois jeitos seguros de testar Python:

1. **O modo interativo (REPL).** No terminal, digite `python3` e aperte Enter.
   Aparece um `>>>`. Ali você pode testar qualquer linha e ver o resultado na
   hora. Para sair: `exit()`.
   ```python
   >>> 2 + 2
   4
   >>> nome = "Ampicilina"
   >>> nome.upper()
   'AMPICILINA'
   ```

2. **`print()` é seu melhor amigo.** Sempre que quiser ver o que uma variável
   contém, coloque um `print(...)` e rode o arquivo. É assim que todo
   programador (iniciante ou sênior) investiga o código.

> ⚠️ Regra de ouro: nunca edite o arquivo do banco (`database/*.sqlite`)
> diretamente. Ele é **gerado** a partir dos arquivos `database/data_*.py` pelo
> script `database/build_db.py`. Para mudar dados, mude os arquivos `.py` e
> rode o build de novo.

---

## Módulo 0 — O panorama: o que é cada peça do projeto

Antes de programar, entenda o mapa. Seu projeto tem 3 partes:

| Parte | Arquivo(s) | O que faz |
|-------|-----------|-----------|
| **Backend** | `app.py` | Recebe pedidos do navegador e responde com dados (a "cozinha") |
| **Dados** | `database/` | Os arquivos `.py` com as patologias + o script que monta o banco |
| **Frontend** | `static/patologias.html` | A tela que o usuário vê (o "salão do restaurante") |

O fluxo: o navegador pede `/api/bacterias/patologia/1` → o `app.py` busca no
banco → devolve os dados → o `patologias.html` desenha na tela.

**Exercício 0:** abra o `app.py` e só *passe os olhos*. Não tente entender tudo.
Procure as palavras `def` (são funções) e `@app.get` (são endereços da API).
Conte quantos `@app.get` existem.

---

## Módulo 1 — Variáveis e tipos básicos

**Conceito.** Uma variável é um nome que guarda um valor. Os tipos básicos:
- **texto** (`str`): `"Ampicilina"`
- **número inteiro** (`int`): `25`
- **número decimal** (`float`): `38.5`
- **verdadeiro/falso** (`bool`): `True` / `False`

**No seu código** (`app.py`, topo do arquivo):
```python
DB_BACT_PATH = Path(__file__).parent / "database" / "patologias_bacterianas_br.sqlite"
EVIDENCIA_SCORE = {"A": 100, "B": 75, "C": 50, "D": 25}
```
`EVIDENCIA_SCORE` guarda uma "tabela" que converte a letra do nível de evidência
num número de 0 a 100 (usado no gráfico radar).

**Exercício 1:** no REPL, crie variáveis para um medicamento:
```python
nome = "Amoxicilina"
dose_mg = 500
disponivel_sus = True
print(nome, dose_mg, disponivel_sus)
```

---

## Módulo 2 — Listas, dicionários e tuplas (o coração do projeto)

**Conceito.**
- **Lista** `[...]`: uma sequência ordenada. `["febre", "tosse", "dispneia"]`
- **Dicionário** `{...}`: pares *chave → valor*. `{"nome": "Febre", "grave": False}`
- **Tupla** `(...)`: como uma lista, mas **não pode mudar** depois de criada.

**No seu código.** Seu projeto é praticamente feito de dicionários e listas.
Olhe `AGENT_DOMAINS` em `app.py` — é um **dicionário de configurações**:
```python
AGENT_DOMAINS = {
    "bacterias": AgentDomain(
        dominio="bacteriana", route="bacterias",
        agent_cols=("nome_cientifico", "nome_comum", "gram"),  # <- isto é uma tupla
        ...
    ),
}
```
E toda resposta da API é um dicionário (veja o `result = {...}` dentro de
`_agent_detalhe`).

**Exercício 2:** crie um dicionário representando uma patologia e acesse um campo:
```python
patologia = {"nome": "Pneumonia", "cid10": "J18", "notificacao": False}
print(patologia["nome"])      # acessa pelo nome da chave
patologia["mortalidade"] = 12 # adiciona uma chave nova
print(patologia)
```

---

## Módulo 3 — Condicionais e o truque do `or`

**Conceito.** `if` / `elif` / `else` decidem o caminho do programa. Em Python,
valores "vazios" (`None`, `0`, `""`, `[]`) contam como **falso**.

**No seu código** (`_fetch_patologia` em `app.py`):
```python
if not pat:
    raise HTTPException(404, "Patologia não encontrada")
```
"Se não encontrou a patologia, devolve erro 404." E um truque muito usado no seu
projeto — o `or` como valor padrão:
```python
EVIDENCIA_SCORE.get(tratamento["nivel_evidencia"] or "D", 25)
```
"Use o nível de evidência; **se ele for vazio/None**, use 'D' como padrão."

**Exercício 3:**
```python
nivel = None
nivel_final = nivel or "D"
print(nivel_final)   # vai imprimir "D"
```

---

## Módulo 4 — Loops e compreensões de lista

**Conceito.** `for` repete uma ação para cada item. A **compreensão de lista** é
um jeito curto de criar uma lista a partir de outra.

**No seu código.** Isto aparece dezenas de vezes no `app.py`:
```python
[dict(r) for r in rows]
```
Leia como: "para cada linha `r` em `rows`, transforme em dicionário e junte numa
lista". É equivalente a:
```python
resultado = []
for r in rows:
    resultado.append(dict(r))
```

**Exercício 4:** dada uma lista de doses, crie outra com o dobro:
```python
doses = [250, 500, 875]
dobro = [d * 2 for d in doses]
print(dobro)   # [500, 1000, 1750]
```

---

## Módulo 5 — Funções

**Conceito.** Uma função é um bloco de código com nome, que recebe entradas
(parâmetros) e devolve uma saída (`return`). Evita repetição.

**No seu código** (`_fetch_clinical` em `app.py`): é uma função que recebe o
banco e o id da patologia, e devolve sintomas, critérios e escores. Foi criada
justamente para **não repetir** a mesma busca em 5 lugares diferentes.

```python
def _fetch_patologia(db, patologia_id):   # recebe 2 parâmetros
    pat = db.execute(...).fetchone()
    if not pat:
        raise HTTPException(404, "Patologia não encontrada")
    return pat                            # devolve o resultado
```

**Exercício 5:** escreva uma função que calcula o escore de acesso ao SUS:
```python
def acesso_sus(disponivel):
    if disponivel:
        return 100
    return 0

print(acesso_sus(True))   # 100
print(acesso_sus(False))  # 0
```

---

## Módulo 6 — Módulos e imports

**Conceito.** Um programa grande é dividido em vários arquivos. `import` traz
código de um arquivo (ou de uma biblioteca) para o outro.

**No seu código** (topo do `app.py`):
```python
import sqlite3                         # biblioteca do Python para o banco
from pathlib import Path               # traz só a ferramenta "Path"
from fastapi import FastAPI, HTTPException
```
E o `database/build_db.py` importa os seus arquivos de dados:
```python
from data_criterios_bacterianas import CRITERIOS_BACTERIANAS
```

**Exercício 6:** no REPL, importe e use uma ferramenta pronta do Python:
```python
from datetime import date
print(date.today())
```

---

## Módulo 7 — Conversando com o banco de dados (SQLite + SQL)

**Conceito.** O banco guarda os dados em **tabelas** (como planilhas). Você pede
dados com **SQL**, uma linguagem própria. `SELECT ... FROM ... WHERE ...`.

**No seu código** (`_fetch_patologia`):
```python
pat = db.execute(
    "SELECT p.nome, p.cid10 FROM patologias p WHERE p.id = ?",
    (patologia_id,),
).fetchone()
```
Repare no `?` — ele é um **espaço reservado** para o valor. Isso é uma regra de
**segurança**: nunca cole o valor direto na string SQL; sempre use `?`. (Há um
comentário no seu código explicando exatamente isso.)

**Exercício 7:** explore o banco com a ferramenta de linha de comando:
```
sqlite3 database/patologias_bacterianas_br.sqlite "SELECT nome FROM patologias LIMIT 5"
```

---

## Módulo 8 — Classes e objetos

**Conceito.** Uma **classe** é um molde para criar objetos que agrupam dados. No
seu projeto há uma classe simples:

```python
class AgentDomain:
    def __init__(self, **kw):
        self.__dict__.update(kw)
```
Ela serve para guardar a configuração de cada domínio (bacteriano, viral...).
Depois você acessa com `cfg.junction`, `cfg.drug_table`, etc.

Para um iniciante: **você não precisa escrever classes ainda**. Mas entender que
`cfg.alguma_coisa` é "pegar um campo de um objeto" já te ajuda a ler o código.

**Exercício 8:** apenas leia a classe `AgentDomain` e a lista `AGENT_DOMAINS` no
`app.py`. Tente responder: qual é o nome da tabela de antibióticos do domínio
`"bacterias"`? (Dica: procure `drug_table`.)

---

## Módulo 9 — Os conceitos "avançados" que seu projeto usa

Você ainda **não precisa escrever** estes, mas é bom reconhecê-los ao ler:

- **Decorator** `@app.get("/health")` — a linha com `@` antes de uma função.
  Diz ao FastAPI: "quando alguém acessar este endereço, chame esta função".
- **`with` (gerenciador de contexto)** — `with conn_bact() as db:` abre o banco e
  **garante que ele será fechado** no final, mesmo se der erro.
- **f-string** — texto com `f"..."` que permite inserir variáveis: `f"{cfg.route}:categorias"`.
- **`defaultdict`** — um dicionário que já vem com valor padrão, usado para
  agrupar posologias por medicamento sem dar erro.

**Exercício 9:** teste uma f-string:
```python
rota = "bacterias"
print(f"/api/{rota}/categorias")   # /api/bacterias/categorias
```

---

## Módulo 10 — Como uma API funciona (FastAPI)

**Conceito.** Uma API é um "garçom": o navegador faz um **pedido** (request) a um
endereço, e o servidor devolve uma **resposta** (response), geralmente em JSON
(que é praticamente um dicionário Python).

**No seu código:**
```python
@app.get("/api/bacterias/patologia/{patologia_id}")
def bact_detalhe(patologia_id: int):
    return _agent_detalhe(AGENT_DOMAINS["bacterias"], patologia_id)
```
- `@app.get(...)` → o endereço.
- `{patologia_id}` → uma parte variável do endereço (o número da patologia).
- `: int` → o FastAPI **garante** que esse valor é um número inteiro.
- `return {...}` → o dicionário devolvido vira JSON automaticamente.

**Exercício 10:** rode o servidor e veja a documentação automática:
```
uvicorn app:app --reload
```
Depois abra no navegador: `http://localhost:8000/docs` — o FastAPI gera uma
página interativa com todos os seus endpoints (e as docstrings que comentamos!).

---

## Roteiro sugerido (6 semanas)

| Semana | Módulos | Foco |
|--------|---------|------|
| 1 | 0, 1 | Panorama + variáveis e tipos |
| 2 | 2, 3 | Listas/dicionários + condicionais |
| 3 | 4, 5 | Loops/compreensões + funções |
| 4 | 6, 7 | Imports + banco de dados |
| 5 | 8, 9 | Classes + conceitos avançados (só ler) |
| 6 | 10 | API e juntando tudo |

Dedique **~30–45 min por dia**, sempre digitando os exemplos você mesmo (não só
lendo). Programação se aprende escrevendo, errando e corrigindo.

---

## Próximos passos depois deste guia

1. Refazer um endpoint simples (ex.: `/health`) do zero, sem olhar.
2. Adicionar um campo novo numa resposta da API.
3. Estudar `database/build_db.py` para entender como o banco é montado.
4. Aprender sobre testes automáticos (o projeto ainda não tem — seria um ótimo
   primeiro projeto seu de verdade).

> Recursos externos gratuitos recomendados: o tutorial oficial do Python em
> português (docs.python.org/pt-br/3/tutorial) e o curso "Python para Zumbis".

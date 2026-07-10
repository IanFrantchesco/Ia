# Plano de Comercialização — App de Patologias 💊🔐

> Documento de planejamento. Reúne, num só lugar, tudo que é preciso para
> transformar o app em um produto pago (assinatura via Hotmart), com acesso
> por link mágico. Serve de mapa e checklist — marque as caixas conforme avança.

---

## Visão geral: o "motor" e o "entorno"

Comercializar tem **duas camadas**. É importante não confundir:

- **O motor técnico** — o que faz o acesso pago funcionar (Hotmart + banco de
  clientes + link mágico + proteção da API). É o que precisa de código.
- **O entorno de negócio** — o que é preciso para vender de forma **legal e
  responsável**, principalmente por ser um produto **médico** (política de
  privacidade, aviso médico, fiscal, suporte). Isso **não é código**, mas é
  obrigatório para lançar de verdade.

**A resposta honesta à pergunta "é só isso (Hotmart + link mágico + código)?":**
Não. Esse trio é o *motor*, e sozinho ele **faz o acesso funcionar**. Mas para
**comercializar** um app clínico com segurança jurídica, faltam ainda algumas
peças do entorno (Parte B). São de baixo esforço, mas não são opcionais.

---

# PARTE A — O motor técnico

## Fase 1 — Hotmart (você, sem código) 🟢

- [ ] Criar conta de **Produtor** no Hotmart (gratuito).
- [ ] Cadastrar o produto como **assinatura / recorrência mensal** (não pagamento único).
- [ ] Definir o **preço** da mensalidade.
- [ ] Enviar o produto para **aprovação** do Hotmart (leva de horas a alguns dias).
- [ ] Decidir: a identificação do cliente será **pelo e-mail** da compra.
- [ ] Localizar, na área de ferramentas do Hotmart, onde ficam o **Webhook/Postback**
      e a **página de obrigado** (vamos precisar depois).

> Enquanto o Hotmart aprova, dá para **vender e liberar acesso manualmente** aos
> primeiros compradores. Não precisa esperar o motor ficar pronto para faturar.

## Fase 2 — Banco de clientes + cofre (nós juntos, código) 🟡

- [ ] Ligar um **Volume persistente** no Railway (o "cofre permanente" para os
      clientes não sumirem a cada deploy).
- [ ] Criar a **tabela de clientes** (e-mail, status, validade) nesse Volume.
- [ ] Guardar os **segredos no cofre** de variáveis do Railway (nunca no código).

## Fase 3 — Webhook do Hotmart (nós juntos, código) 🟡

- [ ] Criar o **endpoint do webhook** — o "ouvido" que recebe o aviso de pagamento.
- [ ] **Validar o token secreto do Hotmart (hottok)** em todo aviso recebido.
      *(Peça de segurança nº 1: separa "cliente que pagou" de "golpista".)*
- [ ] Ao receber "pago" → ativar o cliente; ao receber "cancelado/reembolsado" → desativar.

## Fase 4 — Link mágico (nós juntos, código + serviço de e-mail) 🟡

- [ ] Criar conta num **serviço de envio de e-mail** (ex.: Resend — plano gratuito
      cobre milhares de e-mails/mês). É o "carteiro". **Não é webhook** — é envio.
- [ ] Guardar a **chave de API do e-mail** no cofre do Railway.
- [ ] Fluxo no código:
      1. cliente digita o e-mail;
      2. app confere na tabela se pagou e está ativo;
      3. app gera um **código secreto de validade curta** (ex.: 15 min);
      4. app pede ao carteiro para enviar o **link de acesso** ao e-mail do cliente;
      5. cliente clica → app valida → libera.
- [ ] Entregar um **"crachá" (cookie)** para o cliente não repetir o login toda vez.

## Fase 5 — Proteger a API (nós juntos, código) 🟡

- [ ] Exigir o **crachá** nos endpoints, para ninguém acessar os dados "pulando" o portão.
- [ ] Manter os arquivos estáticos e a tela de login acessíveis (a barreira é a API).

## Fase 6 — Testar em modo teste (essencial) 🟠

- [ ] Usar o **modo de teste do Hotmart** para simular uma compra sem gastar dinheiro.
- [ ] Verificar: a ficha entrou na tabela? O link mágico chegou? O acesso liberou?
      O cancelamento bloqueia?
- [ ] Só depois de tudo passar → ligar em produção.

## Fase 7 — Lançar 🟢

- [ ] Configurar a **página de obrigado** do Hotmart apontando para a tela de acesso do app.
- [ ] Divulgar. A partir daqui, o motor roda sozinho.

---

# PARTE B — O que mais precisa para comercializar (o entorno)

> Isto **não é código**, mas é o que separa "app técnico funcionando" de
> "produto que pode ser vendido com segurança". Por ser um app **médico**, alguns
> itens aqui são especialmente importantes.

## B1 — Aviso médico / isenção de responsabilidade (CRÍTICO) ⚠️

- [ ] Incluir no app um **aviso claro** de que é uma **ferramenta de apoio/consulta**,
      **não** substitui o julgamento clínico nem a avaliação individual do paciente.
- [ ] Deixar explícito o **público-alvo** (ex.: profissionais e estudantes de saúde).
- [ ] Deixar claro que a decisão final é sempre do profissional responsável.

> Este é o item de maior risco de um produto clínico. Não é burocracia — é proteção
> sua e do usuário.

## B2 — Legal / LGPD (obrigatório para coletar e-mails) 📄

- [ ] **Política de Privacidade** — você coleta e-mails (dado pessoal); a LGPD exige
      informar o que coleta, por quê e como. Existem modelos prontos.
- [ ] **Termos de Uso** — regras de uso, assinatura, cancelamento, responsabilidades.
- [ ] Linkar os dois no app e/ou na página de vendas.

## B3 — Fiscal (receber o dinheiro corretamente) 💰

- [ ] Definir como vai receber: **CPF** (há limites) ou abrir **MEI/CNPJ**.
- [ ] O Hotmart cuida de boa parte (cobrança, nota, impostos da transação), mas a
      **declaração do seu rendimento** é responsabilidade sua.

## B4 — Suporte e reembolso 📮

- [ ] Ter um **canal de contato** (um e-mail de suporte já basta para começar).
- [ ] Conhecer a **política de reembolso de 7 dias** (direito do consumidor / Hotmart).

---

## Os segredos que vão nascer (todos no cofre do Railway, nunca no código)

1. `HOTMART_TOKEN` — o hottok, para **conferir** os avisos de pagamento.
2. `EMAIL_API_KEY` — a chave do carteiro, para **enviar** o link mágico.
3. `SECRET_KEY` — segredo que o **próprio app gera**, para **assinar** os crachás
   e os links mágicos (impede falsificação).

---

## Resposta direta: "é só isso que preciso?"

- **Para o acesso pago funcionar tecnicamente:** sim — Hotmart + banco de clientes
  + link mágico + proteção da API (Parte A) é o motor completo.
- **Para comercializar de verdade, com segurança jurídica (produto médico):** não —
  faltam o **aviso médico**, a **política de privacidade + termos** (LGPD), o
  **fiscal** e um **canal de suporte** (Parte B). São de baixo esforço, mas não
  são opcionais.

**Ordem recomendada:** Fase 1 (Hotmart) agora → Parte B em paralelo (textos legais
e aviso médico) → Fases 2 a 6 (código, juntos) → Fase 7 (lançar).

# KB-30 · E-mail suspeito (phishing) — e o que fazer se clicou

[← Índice](../README.md#indice) · **Categoria:** Segurança · **Quem executa:** N1 orienta e aciona; investigação é da equipe de segurança

> **Em uma frase:** diante de um e-mail suspeito, a regra é **não interagir, reportar e, se já clicou, agir rápido** — a velocidade do aviso vale mais do que ter certeza.

---

## Entenda o problema

*Phishing* vem de *fishing* (pescar): o golpista joga uma **isca** (e-mail, mensagem, ligação) esperando que alguém morda — clique num link, abra um anexo, digite a senha numa página falsa ou faça um pagamento.

Pense num **golpe do falso funcionário do banco**: ele usa o nome do banco, cria urgência ("sua conta será bloqueada hoje!") e pede algo que o banco de verdade nunca pede por telefone. O e-mail de phishing funciona igual.

### Os sinais de alerta

| Sinal | Exemplo |
|---|---|
| **Urgência ou ameaça** | "Sua conta será desativada em 2 horas" |
| **Remetente que não bate** | Nome "Suporte TI", mas endereço de um domínio estranho |
| **Link que leva a outro lugar** | O texto diz um site; ao passar o mouse, o endereço real é outro |
| **Pedido incomum** | Senha, código de MFA, pagamento, troca de dados bancários |
| **Anexo inesperado** | "Fatura.zip", "documento.html", planilha pedindo para habilitar macros |
| **Erros e tom estranho** | Saudação genérica, português esquisito, assinatura diferente |

> [!NOTE]
> Golpes bem feitos **não têm erros de português** e usam nomes reais da empresa. Nenhum sinal sozinho prova nada; o pedido incomum é o mais forte de todos.

## Pergunte primeiro

- Você **só recebeu**, ou **clicou** no link / abriu o anexo?
- Se clicou: digitou **senha**, aprovou alguma **notificação de MFA** ou fez algum **pagamento**?
- Quando aconteceu?
- Outros colegas receberam a mesma mensagem?

## Antes de começar

> [!CAUTION]
> **Não abra o link nem o anexo "para conferir"** — nem no seu computador. Análise de mensagens maliciosas é tarefa da equipe de segurança, em ambiente isolado.

> [!CAUTION]
> **Não encaminhe o e-mail suspeito para colegas** como alerta. Isso espalha a isca. Use o botão de relato ou o canal oficial de segurança.

---

## Passo a passo

### Passo 1 — Se só recebeu: reporte e apague

**Faça:** oriente o usuário a usar o botão **Relatar** (ou "Relatar phishing") no Outlook, ou o canal oficial definido pela empresa. Depois, apagar a mensagem.

**Por quê:** o relato permite que a segurança remova a mesma mensagem da caixa de todos e bloqueie o remetente. Um único aviso protege a empresa inteira.

**O que você deve ver:** a mensagem relatada pelo canal oficial.

### Passo 2 — Se digitou a senha: troque agora

**Faça:** oriente o usuário a trocar a senha **imediatamente**, pelo caminho oficial ([KB-17](kb-17-senha-esquecida-ou-expirada.md)), e acione a equipe de segurança.

**Por quê:** a página falsa capturou a senha. Cada minuto conta, porque o golpista pode usá-la na hora, inclusive para mandar mais phishing a partir da conta da vítima.

**O que você deve ver:** senha trocada e incidente aberto.

### Passo 3 — Se aprovou uma notificação de MFA: incidente imediato

**Faça:** acione a segurança na hora e informe o horário aproximado da aprovação.

**Por quê:** aprovar a notificação entregou ao golpista a segunda fechadura. A equipe de segurança precisa encerrar as sessões ativas e revisar a conta.

**O que você deve ver:** incidente registrado como prioridade de segurança.

### Passo 4 — Se abriu um anexo: isole o computador

**Faça:** conforme o processo da empresa, oriente a **desconectar o computador da rede** (tirar o cabo e desligar o Wi-Fi), **sem desligar o computador**, e acione a segurança.

**Por quê:** desconectar impede que um eventual programa malicioso se espalhe ou envie dados. Não desligar preserva informações que a segurança pode precisar analisar.

**O que você deve ver:** computador fora da rede e a segurança acionada.

### Passo 5 — Se fez um pagamento ou alterou dados bancários

**Faça:** acione a segurança **e** a área financeira imediatamente, com data, valor e destino.

**Por quê:** em fraudes de pagamento, a chance de bloquear a transferência diminui rápido com o tempo.

**O que você deve ver:** as duas áreas avisadas.

---

## Como interpretar o resultado

| Situação | Gravidade | Ação principal |
|---|---|---|
| Recebeu, não interagiu | Baixa | Relatar e apagar (Passo 1) |
| Clicou, mas não digitou nada | Média | Relatar e avisar a segurança; ela decide os próximos passos |
| Digitou a senha | Alta | Trocar senha + segurança (Passo 2) |
| Aprovou MFA | Crítica | Segurança imediata (Passo 3) |
| Abriu anexo | Alta | Isolar + segurança (Passo 4) |
| Fez pagamento | Crítica | Segurança + financeiro (Passo 5) |

## Como saber que resolveu

- [ ] A mensagem foi relatada pelo canal oficial.
- [ ] Se houve interação: incidente aberto, senha trocada (se aplicável) e segurança ciente.
- [ ] O usuário sabe como reconhecer e relatar a próxima tentativa.

> [!TIP]
> **Agradeça o usuário por avisar** — mesmo que tenha clicado. Quem é repreendido passa a esconder o erro, e um clique escondido é muito mais perigoso que um clique reportado.

## O que anotar no chamado

- [ ] Tipo de interação (recebeu / clicou / digitou senha / aprovou MFA / abriu anexo / pagou)
- [ ] Horário aproximado
- [ ] Assunto e remetente aparente (sem colar o link)
- [ ] Ações orientadas e equipes acionadas

## Quando encaminhar ao N2

Sempre que houve **qualquer interação** (clique, senha, anexo, aprovação, pagamento): encaminhe para a equipe de segurança como incidente, não como chamado comum.

## Erros comuns

- **Abrir o link "para ver se é perigoso".**
- **Esperar ter certeza** antes de avisar a segurança.
- **Repreender o usuário**, o que desestimula futuros relatos.
- **Encaminhar a mensagem para todos** como alerta.

## Guias relacionados

[KB-17 · Senha](kb-17-senha-esquecida-ou-expirada.md) · [KB-29 · MFA](kb-29-mfa-autenticador.md) · [KB-24 · Arquivo do Office](kb-24-arquivo-office-bloqueado.md)

**Referências oficiais:** [Proteger-se contra phishing][phishing] · [Cartilha de Segurança para Internet (CERT.br)][cert]

---

[← Anterior: KB-29](kb-29-mfa-autenticador.md) · [↑ Índice](../README.md#indice) · [Próximo: KB-31 →](kb-31-webcam.md)

[phishing]: https://learn.microsoft.com/pt-br/defender-endpoint/malware/phishing
[cert]: https://cartilha.cert.br/

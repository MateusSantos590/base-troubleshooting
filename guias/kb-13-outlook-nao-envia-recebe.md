# KB-13 · Outlook não envia ou recebe

[← Índice](../README.md#indice) · **Categoria:** Microsoft 365 · **Quem executa:** N1 com o usuário

> **Em uma frase:** compare o aplicativo com o **webmail**. Se o webmail funciona, o problema está no Outlook do computador; se não, está na conta ou no serviço.

---

## Entenda o problema

Seu e-mail mora no servidor, não no computador. O Outlook é só uma "janela" para ele — e o webmail é **outra janela** para o mesmo lugar. Se pela janela do navegador está tudo certo, o problema é a janela do Outlook. Se as duas mostram o problema, o problema é a casa (conta ou serviço).

**Sintoma típico:** mensagens ficam na **Caixa de Saída** ou mensagens novas não chegam.

**Causas mais comuns:** falta de conexão, modo offline ativado, problema de autenticação, caixa cheia ou serviço indisponível.

## Pergunte primeiro

- O problema é **enviar**, **receber** ou os dois?
- Aparece alguma mensagem de erro? Qual?
- A mensagem presa tem anexo grande?
- Você usa o Outlook clássico ou o novo?

## Antes de começar

> [!WARNING]
> **Evite reenvios repetidos** — eles podem gerar mensagens duplicadas quando o problema for resolvido. E nunca registre o conteúdo dos e-mails no chamado.

---

## Passo a passo

### Passo 1 — Confira a rede e a mensagem de erro

**Faça:** confirme que o computador tem internet e anote a mensagem de erro, se houver.

**Por quê:** sem rede, nada envia. E o código de erro costuma apontar a causa.

**O que você deve ver:** navegação funcionando e o erro registrado.

### Passo 2 — Verifique o modo offline (Outlook clássico)

**Faça:** na guia **Enviar/Receber**, veja se **Trabalhar Offline** está ativado. Se estiver sem motivo, desative.

**Por quê:** esse modo pausa envio e recebimento, como o modo avião do celular. É fácil ativar sem querer.

**O que você deve ver:** o botão desativado e as mensagens da Caixa de Saída começando a sair.

### Passo 3 — Compare com o webmail

**Faça:** peça ao usuário para entrar no **webmail aprovado** pela empresa e testar o envio e o recebimento.

**Por quê:** é o teste que divide o problema ao meio: aplicativo × conta/serviço.

**O que você deve ver:** o webmail funcionando ou falhando também.

### Passo 4 — Verifique avisos de caixa cheia, login e anexo

**Faça:** procure avisos de armazenamento cheio, pedido de login ou limite de anexo.

**Por quê:** caixa cheia bloqueia recebimento; anexo acima do limite bloqueia envio. O limite de anexo **varia conforme a empresa** — não existe um valor universal.

**O que você deve ver:** algum aviso que explique o problema — ou nenhum.

---

## Como interpretar o resultado

| Se você observar… | Provavelmente significa… | Próximo passo |
|---|---|---|
| Webmail **funciona**, Outlook não | Problema no aplicativo ou na conexão dele | Investigue o cliente ([KB-12](kb-12-outlook-nao-abre.md)) |
| Webmail **também falha** | Problema na conta, no serviço ou em política | Encaminhe ao N2 |
| "Trabalhar Offline" estava ativado | Causa encontrada | Desative e valide |
| Aviso de caixa cheia | Recebimento bloqueado por armazenamento | Oriente arquivamento conforme a política |
| Só mensagens com anexo grande ficam presas | Limite de anexo | Use o meio aprovado para arquivos grandes |

## Como saber que resolveu

- [ ] Uma mensagem de teste foi **enviada e recebida** com um destinatário de teste autorizado, sem conteúdo sensível.

## O que anotar no chamado

- [ ] Versão (clássico/novo)
- [ ] Estado online/offline
- [ ] Código de erro
- [ ] Comparação aplicativo × webmail

## Quando encaminhar ao N2

- O webmail também falha.
- Conta bloqueada.
- Várias contas afetadas.

Registre código e horário, **sem** o conteúdo dos e-mails.

## Erros comuns

- **Mexer no Outlook sem testar o webmail** — pode ser problema do serviço.
- **Reenviar várias vezes.**
- **Supor um limite fixo de anexo** que vale para todas as empresas.

## Exemplo completo

Veja este cenário preenchido no [Modelo de chamado — exemplo fictício](../docs/MODELO_CHAMADO.md#5-exemplo-fictício-preenchido).

## Guias relacionados

[KB-12 · Outlook não abre](kb-12-outlook-nao-abre.md) · [KB-05 · Conectado sem internet](kb-05-wifi-sem-internet.md)

**Referência oficial:** [Não consigo enviar ou receber mensagens no Outlook][outlook-envio]

---

[← Anterior: KB-12](kb-12-outlook-nao-abre.md) · [↑ Índice](../README.md#indice) · [Próximo: KB-14 →](kb-14-vpn-nao-conecta.md)

[outlook-envio]: https://support.microsoft.com/pt-br/outlook/i-can-t-send-or-receive-messages-in-outlook

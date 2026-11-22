# KB-17 · Senha esquecida ou expirada

[← Índice](../README.md#indice) · **Categoria:** Identidade · **Quem executa:** usuário pelo portal oficial; redefinição administrativa pela equipe autorizada

> **Em uma frase:** oriente o caminho oficial de recuperação. O suporte **nunca vê, recebe ou escolhe** a senha do usuário.

---

## Entenda o problema

Recuperar senha é como trocar a fechadura de casa: quem deve receber a chave nova é o morador, e mais ninguém. Por isso o processo é feito pelo próprio usuário (autoatendimento) ou por uma equipe autorizada depois de confirmar a identidade dele.

Uma confusão muito comum: o **PIN do Windows** não é a **senha da conta**. O PIN abre só aquele computador, como o cadeado da bicicleta — não abre a porta de casa.

**Sintoma típico:** o usuário esqueceu a senha ou recebeu aviso de que ela expirou.

**Causas mais comuns:** esquecimento, prazo de validade da senha (política da empresa) ou confusão entre PIN, conta e senha.

## Pergunte primeiro

- Qual conta? (Windows, e-mail, sistema específico)
- Como você costuma entrar: senha, PIN ou biometria?
- A mensagem diz "senha expirada" ou "senha incorreta"?

## Antes de começar

> [!CAUTION]
> **Não peça, não anote e não envie senhas** — nem a antiga, nem a nova, nem a temporária. Nunca registre códigos de recuperação ou perguntas/respostas de segurança. Nada disso pode aparecer em chamados, chats ou e-mails.

---

## Passo a passo

### Passo 1 — Identifique a conta e o método de entrada

**Faça:** descubra qual conta e qual método (senha, PIN, biometria) estão envolvidos — **sem pedir o segredo**.

**Por quê:** se o problema é o PIN, a solução é diferente da senha da conta.

**O que você deve ver:** conta e método identificados.

### Passo 2 — Oriente o portal oficial de recuperação

**Faça:** indique o portal de autoatendimento da empresa, se existir, e acompanhe o usuário enquanto ele faz o processo.

**Por quê:** é o caminho mais rápido e seguro: só o dono da conta participa.

**O que você deve ver:** o usuário concluindo a recuperação.

### Passo 3 — Redefinição administrativa, se necessário

**Faça:** se não houver autoatendimento, a redefinição é feita pela **equipe autorizada**, **depois** de validar a identidade.

**Por quê:** a validação impede que alguém se passe pelo usuário para roubar a conta.

**O que você deve ver:** a redefinição feita pelo fluxo correto.

### Passo 4 — Atualize a senha nos outros lugares

**Faça:** combine com o usuário a atualização da nova senha nos aplicativos e dispositivos onde ela está salva, conforme a política interna.

**Por quê:** senha antiga salva no celular pode **bloquear a conta** logo depois ([KB-16](kb-16-conta-bloqueada.md)).

**O que você deve ver:** o usuário sabendo onde atualizar.

---

## Como interpretar o resultado

| Se você observar… | Provavelmente significa… | Próximo passo |
|---|---|---|
| O usuário só esqueceu o **PIN** | A senha da conta está ok | Siga o fluxo de redefinição do PIN |
| A recuperação pede **novo cadastro de MFA** | Mudança sensível de segurança | Encaminhe ao fluxo de identidade; não aprove por conveniência |
| **Suspeita de fraude** (pedido estranho, pressa excessiva, terceiro pedindo) | Possível tentativa de golpe | Pare e acione a segurança |
| Portal indisponível ou dados de recuperação desatualizados | O usuário não consegue se autoatender | Encaminhe ao N2 |

## Como saber que resolveu

- [ ] O usuário entrou **com o próprio método** e acessou o recurso de que precisava.

## O que anotar no chamado

- [ ] Tipo de conta e método de entrada
- [ ] Mensagem exibida
- [ ] Resultado do fluxo oficial
- [ ] **Nenhum** código, senha ou resposta de segurança

## Quando encaminhar ao N2

- Recuperação indisponível.
- Dados de recuperação desatualizados.

## Erros comuns

- **Criar uma senha temporária e enviá-la por chat ou e-mail.**
- **Confundir PIN com senha.**
- **Aprovar troca de MFA** sem validar a identidade.

## Guias relacionados

[KB-16 · Conta bloqueada](kb-16-conta-bloqueada.md)

**Referência oficial:** [Como funciona a redefinição de senha por autoatendimento][identidade]

---

[← Anterior: KB-16](kb-16-conta-bloqueada.md) · [↑ Índice](../README.md#indice) · [Próximo: KB-18 →](kb-18-microfone.md)

[identidade]: https://learn.microsoft.com/en-us/entra/identity/authentication/concept-sspr-howitworks

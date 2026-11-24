# KB-29 · MFA: celular novo, código não chega ou aprovação que não pedi

[← Índice](../README.md#indice) · **Categoria:** Identidade · **Quem executa:** N1 orienta; redefinir métodos de MFA é da equipe de identidade

> **Em uma frase:** o MFA é a **segunda fechadura** da conta — o suporte ajuda o usuário a usar a chave dele, mas **nunca segura a chave** e **nunca troca a fechadura sem confirmar quem está pedindo**.

---

## Entenda o problema

MFA (*Multi-Factor Authentication*, autenticação multifator) significa provar quem você é com **duas coisas diferentes**: algo que você **sabe** (a senha) e algo que você **tem** (o celular com o aplicativo autenticador). É como um cofre de banco que exige **senha e chave física**: roubar só uma delas não basta.

Por isso, o MFA é exatamente o que um golpista quer contornar. Muitos ataques são conversas telefônicas do tipo "sou da TI, me passe o código" ou "aprove a notificação que vou te mandar".

**Sintomas típicos:**

- "Troquei de celular e não consigo mais entrar."
- "O código do aplicativo é recusado."
- "Não recebo a notificação para aprovar."
- "**Recebi um pedido de aprovação que eu não fiz.**" ← incidente de segurança

**Causas mais comuns:** celular trocado sem migrar o autenticador, horário do celular errado, notificações bloqueadas, celular sem internet, ou alguém com a senha do usuário tentando entrar.

## Pergunte primeiro

- O que mudou? (celular novo, reinstalou o aplicativo, número trocado)
- Você ainda tem o **celular antigo** em mãos?
- O aplicativo mostra o **código de 6 dígitos** que muda a cada 30 segundos?
- Você recebeu algum pedido de aprovação **sem estar tentando entrar**?

## Antes de começar

> [!CAUTION]
> **Nunca peça o código de MFA nem peça para o usuário aprovar uma notificação "para teste".** Essa é exatamente a técnica usada por golpistas. Quem lê o código e aprova é sempre o usuário, na tela dele.

> [!CAUTION]
> **Confirme a identidade antes de qualquer redefinição de MFA**, pelo procedimento oficial da empresa (por exemplo, retorno de ligação para o número cadastrado, validação com o gestor). Redefinir o MFA de um golpista que se passa pelo usuário entrega a conta inteira.

---

## Passo a passo

### Passo 1 — Pedido de aprovação não solicitado? Pare tudo

**Faça:** se o usuário recebeu notificações que **não pediu**, oriente a **negar** (ou responder que não reconhece a tentativa), **não aprovar** de jeito nenhum e acione imediatamente o processo de segurança.

**Por quê:** uma notificação inesperada significa que alguém **já tem a senha** e está tentando a segunda fechadura. Golpistas mandam várias seguidas esperando que a pessoa aprove por cansaço (*MFA fatigue*).

**O que você deve ver:** incidente registrado e a senha sendo trocada pelo caminho oficial ([KB-17](kb-17-senha-esquecida-ou-expirada.md)).

### Passo 2 — Código recusado: confira o relógio do celular

**Faça:** peça para o usuário verificar se o celular está com **data e hora automáticas** ativadas.

**Por quê:** o código de 6 dígitos é calculado a partir do horário. Se o relógio do celular está alguns minutos adiantado ou atrasado, o código gerado não bate com o esperado pelo servidor.

**O que você deve ver:** o código sendo aceito depois de corrigir o horário.

### Passo 3 — Notificação não chega: internet e notificações

**Faça:** confirme que o celular tem internet e que as notificações do aplicativo autenticador estão permitidas. Oriente a abrir o aplicativo manualmente — a solicitação pendente costuma aparecer lá.

**Por quê:** a notificação depende da internet do celular e da permissão de notificação. Modo de economia de bateria também pode atrasá-la.

**O que você deve ver:** a solicitação aparecendo no aplicativo.

### Passo 4 — Celular novo: registre o novo método

**Faça:** se o usuário ainda consegue entrar (com o celular antigo ou outro método cadastrado), oriente a acessar **Informações de segurança** em `mysignins.microsoft.com/security-info`, adicionar o novo celular e só depois remover o antigo.

**Por quê:** é o caminho de autoatendimento: o próprio usuário, já autenticado, cadastra o novo método. Nenhuma credencial passa pelo suporte.

**O que você deve ver:** o novo método listado e um login de teste funcionando com ele.

### Passo 5 — Sem nenhum método disponível: encaminhe

**Faça:** se o usuário perdeu o celular antigo e não tem outro método, abra a solicitação para a equipe de identidade **após a verificação de identidade oficial**.

**Por quê:** redefinir o MFA é uma ação de alto risco e exige permissão administrativa e processo formal.

**O que você deve ver:** solicitação registrada, com a verificação de identidade documentada.

---

## Como interpretar o resultado

| Se você observar… | Significa… | Faça |
|---|---|---|
| Notificações que o usuário não pediu | Alguém tem a senha | Passo 1: incidente de segurança |
| Código recusado sempre | Relógio do celular errado ou conta errada no app | Passo 2 |
| Notificação não chega | Internet, notificação ou bateria | Passo 3 |
| Celular novo e o antigo ainda funciona | Migração simples | Passo 4 |
| Nenhum método disponível | Precisa de redefinição administrativa | Passo 5 |

## Como saber que resolveu

- [ ] O usuário entra com o novo método, na frente do suporte (sem mostrar o código).
- [ ] O método antigo foi removido, se o celular antigo não está mais com ele.
- [ ] Em caso de aprovação indevida: incidente aberto e senha trocada.

## O que anotar no chamado

- [ ] Tipo de problema (celular novo, código recusado, notificação, aprovação não solicitada)
- [ ] Como a identidade foi verificada (sem dados pessoais desnecessários)
- [ ] Ações orientadas e resultado
- [ ] **Nunca** registre códigos, QR codes ou senhas

## Quando encaminhar ao N2

- Redefinição de métodos de MFA.
- Qualquer suspeita de comprometimento da conta.
- Usuário que não consegue passar pela verificação de identidade.

## Erros comuns

- **Pedir o código "só para testar".**
- **Redefinir o MFA porque a pessoa "parece" ser o usuário** ao telefone.
- **Tratar notificações não solicitadas como defeito** do aplicativo.

## Guias relacionados

[KB-16 · Conta bloqueada](kb-16-conta-bloqueada.md) · [KB-17 · Senha](kb-17-senha-esquecida-ou-expirada.md) · [KB-30 · E-mail suspeito](kb-30-email-suspeito.md)

**Referências oficiais:** [Como funciona a autenticação multifator do Microsoft Entra][mfa] · [Correspondência de números nas notificações][numbermatch]

---

[← Anterior: KB-28](kb-28-notebook-nao-carrega.md) · [↑ Índice](../README.md#indice) · [Próximo: KB-30 →](kb-30-email-suspeito.md)

[mfa]: https://learn.microsoft.com/pt-br/entra/identity/authentication/concept-mfa-howitworks
[numbermatch]: https://learn.microsoft.com/pt-br/entra/identity/authentication/how-to-mfa-number-match

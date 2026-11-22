# KB-16 · Conta bloqueada

[← Índice](../README.md#indice) · **Categoria:** Identidade · **Quem executa:** N1 orienta; desbloqueio pela equipe autorizada ou autoatendimento

> **Em uma frase:** desbloquear é fácil; o importante é descobrir **por que bloqueou**, para não bloquear de novo em cinco minutos.

---

## Entenda o problema

O bloqueio de conta é como o caixa eletrônico que **segura o cartão** depois de várias senhas erradas. É uma proteção. Às vezes quem erra a senha não é a pessoa, e sim um **celular ou programa com a senha antiga salva**, tentando sozinho em segundo plano. Se você só desbloquear, ele bloqueia de novo.

**Sintoma típico:** o login informa **explicitamente** que a conta está bloqueada.

**Causas mais comuns:** várias tentativas com senha errada ou senha antiga salva em outro dispositivo/aplicativo.

## Pergunte primeiro

- Qual é a mensagem **exata**? (bloqueada, desabilitada, senha incorreta, MFA…)
- Você trocou a senha recentemente?
- Em quais dispositivos você usa essa conta? (celular, tablet, outro computador)
- Já aconteceu antes?

## Antes de começar

> [!CAUTION]
> **Nunca peça a senha.** Valide a identidade da pessoa pelo procedimento oficial da empresa antes de qualquer ação. Desbloquear a conta de quem não é o dono é uma falha grave de segurança.

---

## Passo a passo

### Passo 1 — Pare as tentativas e leia a mensagem

**Faça:** peça ao usuário para **parar de tentar** e confirme a mensagem exata.

**Por quê:** cada nova tentativa errada prolonga o bloqueio. E a mensagem diz se é bloqueio mesmo ou outra coisa.

**O que você deve ver:** a mensagem registrada.

### Passo 2 — Valide a identidade

**Faça:** siga o procedimento de validação de identidade da organização.

**Por quê:** garante que você está ajudando o dono da conta, e não alguém tentando invadi-la.

**O que você deve ver:** identidade confirmada pelo método oficial.

### Passo 3 — Use o caminho oficial de desbloqueio

**Faça:** se a empresa oferece **autoatendimento**, oriente o usuário a usá-lo. Se não, encaminhe à equipe autorizada.

**Por quê:** o caminho oficial registra a ação e respeita as regras de segurança. O fluxo pode ser diferente para contas do Active Directory e do Microsoft Entra ID.

**O que você deve ver:** conta desbloqueada pelo fluxo correto.

### Passo 4 — Se bloquear de novo, procure a origem

**Faça:** liste com o usuário onde a conta está configurada (celular, e-mail no tablet, unidades de rede mapeadas, programas). Oriente a atualizar a senha nesses lugares — **sem pedir a senha**.

**Por quê:** um dispositivo esquecido com a senha antiga tenta logar sozinho e bloqueia a conta repetidamente.

**O que você deve ver:** a origem das tentativas identificada.

---

## Como interpretar o resultado

Mensagens parecidas, situações diferentes:

| Mensagem | Significa… | Analogia |
|---|---|---|
| **Conta bloqueada** | Travada temporariamente por tentativas erradas | Caixa eletrônico segurou o cartão |
| **Conta desabilitada** | Desligada de propósito pela empresa | Crachá cancelado pelo RH |
| **Senha incorreta** | A conta está ok; a senha não confere | Chave errada na fechadura certa |
| **MFA exigido / falhou** | Falta a segunda verificação | Senha certa, mas sem o cartão |

| Se você observar… | Próximo passo |
|---|---|
| Bloqueio volta logo após desbloquear | Procure dispositivos com senha antiga (Passo 4) |
| Tentativas de locais ou horários estranhos | **Suspeita de acesso indevido**: encaminhe à segurança |
| Conta desabilitada | Não é bloqueio; encaminhe à equipe responsável |

## Como saber que resolveu

- [ ] O usuário fez login legítimo.
- [ ] A conta não bloqueou de novo durante o período de teste.

## O que anotar no chamado

- [ ] Mensagem exata e horário
- [ ] Se é recorrente
- [ ] Método de validação de identidade usado
- [ ] Equipe acionada
- [ ] **Nenhum** segredo (senha, código)

## Quando encaminhar ao N2

- Bloqueio recorrente.
- Suspeita de acesso indevido.

## Erros comuns

- **Desbloquear várias vezes seguidas** sem investigar a origem.
- **Pular a validação de identidade** porque "conheço a pessoa".
- **Confundir bloqueada com desabilitada.**

## Guias relacionados

[KB-17 · Senha esquecida ou expirada](kb-17-senha-esquecida-ou-expirada.md) · [KB-14 · VPN não conecta](kb-14-vpn-nao-conecta.md)

**Referência oficial:** [Como funciona a redefinição de senha por autoatendimento][identidade]

---

[← Anterior: KB-15](kb-15-vpn-conecta-sistema-nao-abre.md) · [↑ Índice](../README.md#indice) · [Próximo: KB-17 →](kb-17-senha-esquecida-ou-expirada.md)

[identidade]: https://learn.microsoft.com/en-us/entra/identity/authentication/concept-sspr-howitworks

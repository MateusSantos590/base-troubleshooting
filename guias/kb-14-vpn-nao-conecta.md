# KB-14 · VPN não conecta

[← Índice](../README.md#indice) · **Categoria:** Acesso remoto · **Quem executa:** N1 com o usuário

> **Em uma frase:** a VPN é construída **em cima** da internet. Primeiro confirme a internet, depois a autenticação, depois o túnel — nessa ordem.

---

## Entenda o problema

A VPN é um **túnel particular** da sua casa até o escritório. Para construir o túnel, você precisa de três coisas, em ordem:

1. **Uma estrada** (internet funcionando).
2. **Autorização para entrar** (usuário, senha e MFA corretos).
3. **O túnel em si** (perfil correto, computador dentro das regras da empresa).

Se a estrada está bloqueada, não adianta revisar a autorização.

**Sintoma típico:** o programa de VPN recusa a conexão ou fica tentando sem concluir.

**Causas mais comuns:** internet com falha, problema de autenticação, perfil de VPN incorreto ou computador fora das regras de segurança (conformidade).

## Pergunte primeiro

- A internet funciona sem a VPN? (consegue abrir um site público?)
- Que mensagem aparece e em que momento? (ao digitar a senha, depois do MFA, no final?)
- Você trocou a senha recentemente?
- Está em uma rede diferente da habitual (hotel, celular)?

## Antes de começar

> [!CAUTION]
> **Nunca peça nem registre códigos de MFA.** O próprio usuário conclui o login. Não desative verificação de certificado nem proteções do computador para "fazer conectar".

---

## Passo a passo

### Passo 1 — Teste a internet antes da VPN

**Faça:** com a VPN desligada, abra um site público conhecido. Anote o programa de VPN, a versão e o erro.

**Por quê:** sem internet, não há túnel. É a estrada antes do túnel.

**O que você deve ver:** navegação funcionando sem a VPN.

### Passo 2 — Confira perfil, data e hora

**Faça:** verifique se o usuário escolheu o **perfil de VPN autorizado** e se a **data e a hora** do computador estão corretas.

**Por quê:** relógio errado pode fazer certificados parecerem inválidos e quebrar a autenticação. Perfil errado leva ao destino errado.

**O que você deve ver:** perfil correto e relógio certo.

### Passo 3 — O usuário faz a autenticação

**Faça:** o usuário digita a própria credencial e aprova o MFA. Você só observa em qual etapa ocorre a falha.

**Por quê:** a credencial é dele; seu papel é identificar **onde** o processo para.

**O que você deve ver:** a etapa exata da falha (antes do MFA, depois do MFA, ao montar o túnel).

### Passo 4 — Verifique avisos e tente reconectar uma vez

**Faça:** confira se há aviso de indisponibilidade da VPN. Se fizer sentido, tente reconectar **uma** vez.

**Por quê:** se o serviço está fora para todos, insistir não ajuda. Várias tentativas com senha errada podem **bloquear a conta** ([KB-16](kb-16-conta-bloqueada.md)).

**O que você deve ver:** conexão estabelecida ou erro registrado.

---

## Como interpretar o resultado

| Se você observar… | Provavelmente significa… | Próximo passo |
|---|---|---|
| Internet falha **mesmo sem VPN** | O problema é a conectividade | Trate primeiro a rede ([KB-05](kb-05-wifi-sem-internet.md)) |
| Erro de **certificado** ou **conformidade** | Regra de segurança não atendida | **Pare** e encaminhe; não ignore o alerta |
| Falha ao autenticar | Senha, conta ou MFA | Veja [KB-16](kb-16-conta-bloqueada.md) / [KB-17](kb-17-senha-esquecida-ou-expirada.md) |
| "Conectado", mas o sistema não abre | O túnel está ok; o problema é outro | Vá para [KB-15](kb-15-vpn-conecta-sistema-nao-abre.md) |

> [!IMPORTANT]
> "Conectado" na VPN só é suficiente depois de testar o **recurso de trabalho** de verdade.

## Como saber que resolveu

- [ ] O túnel está estabelecido.
- [ ] O usuário acessou o recurso corporativo de que precisava.

## O que anotar no chamado

- [ ] Programa de VPN e versão
- [ ] Perfil usado
- [ ] Código de erro, horário e etapa da falha
- [ ] **Sem** credenciais ou arquivos de configuração sensíveis

## Quando encaminhar ao N2

- Erro de certificado ou conformidade.
- Problema de conta.
- O problema se repete.

## Erros comuns

- **Investigar a VPN** quando a internet nem funciona.
- **Pedir o código do MFA** "para agilizar".
- **Tentar conectar várias vezes** e bloquear a conta.

## Guias relacionados

[KB-15 · VPN conecta, sistema não abre](kb-15-vpn-conecta-sistema-nao-abre.md) · [KB-16 · Conta bloqueada](kb-16-conta-bloqueada.md)

**Referência oficial:** [Conectar-se a uma VPN no Windows][vpn]

---

[← Anterior: KB-13](kb-13-outlook-nao-envia-recebe.md) · [↑ Índice](../README.md#indice) · [Próximo: KB-15 →](kb-15-vpn-conecta-sistema-nao-abre.md)

[vpn]: https://support.microsoft.com/pt-br/windows/experience/connectivity-networking/connect-to-a-vpn-in-windows

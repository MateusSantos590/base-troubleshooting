# KB-20 · Sistema web não abre

[← Índice](../README.md#indice) · **Categoria:** Sistemas · **Quem executa:** N1 com o usuário

> **Em uma frase:** o erro do navegador já diz muito. Use-o para separar **rede**, **login**, **permissão** e **servidor**.

---

## Entenda o problema

Quando você abre um sistema web, quatro coisas precisam dar certo:

1. **Chegar ao endereço** (rede, DNS, VPN).
2. **Provar quem você é** (autenticação — login).
3. **Ter permissão** para aquela página (autorização).
4. **O servidor funcionar** do outro lado.

O código de erro que aparece funciona como uma placa na porta, indicando qual das quatro falhou.

**Sintoma típico:** o navegador mostra erro, página em branco ou "acesso negado".

**Causas mais comuns:** endereço errado, sessão expirada, rede/VPN, falta de permissão ou servidor fora do ar.

## Pergunte primeiro

- Qual é o endereço exato? (pelo canal interno)
- Que mensagem ou código aparece?
- Outras pessoas conseguem abrir?
- Funcionava antes? Desde quando não funciona?

## Antes de começar

> [!CAUTION]
> **Não limpe todas as senhas e dados do navegador.** Remova dados **apenas do site afetado**, com autorização. Nunca ignore alertas de certificado. Nunca publique URLs que contenham tokens ou dados pessoais.

---

## Passo a passo

### Passo 1 — Confirme endereço, horário e erro

**Faça:** confira o endereço pelo canal oficial. Anote o horário e a mensagem/código exato.

**Por quê:** endereço digitado errado é comum, e o código de erro é a pista mais importante.

**O que você deve ver:** endereço correto e o erro registrado.

### Passo 2 — Separe as quatro camadas

**Faça:** use a tabela abaixo ("Como interpretar") para classificar o erro: rede, login, permissão ou servidor.

**Por quê:** cada camada tem um responsável e uma solução diferentes.

**O que você deve ver:** a camada provável identificada.

### Passo 3 — Compare com janela privativa ou outro navegador aprovado

**Faça:** abra o mesmo endereço numa **janela privativa** ou em outro navegador aprovado pela empresa.

**Por quê:** a janela privativa não usa a sessão salva nem, em geral, extensões. Se funcionar, o problema provavelmente é sessão, cookie ou extensão. Atenção: ela não dispensa o login único (SSO) da empresa.

**O que você deve ver:** se o comportamento muda.

### Passo 4 — Remova dados só do site afetado (se indicado)

**Faça:** se a comparação apontar sessão/cookies, remova os dados **apenas daquele site**, com autorização. Avise antes que o usuário será desconectado dele.

**Por quê:** limpar tudo apagaria senhas salvas e sessões de outros sistemas sem necessidade.

**O que você deve ver:** o site abrindo após novo login.

---

## Como interpretar o resultado

| Código / mensagem | Camada provável | Analogia | Próximo passo |
|---|---|---|---|
| "Não foi possível encontrar o servidor" | Rede / DNS | Endereço não existe no mapa | [KB-07](kb-07-falha-dns.md) |
| **401** | Autenticação (login) | "Identifique-se" | Verifique a sessão e o login |
| **403** | Autorização (permissão) | "Proibida a entrada" | Investigue permissão com o responsável pelo sistema |
| **404** | Endereço da página | "Esse endereço não existe" | Confirme a URL |
| **5xx** (500, 502, 503…) | Servidor ou intermediário | "Fechado para manutenção" | Verifique se outros são afetados; encaminhe |
| Funciona na janela privativa | Sessão, cookie ou extensão | — | Passo 4 |

> [!NOTE]
> Esses códigos são **pistas, não diagnósticos**. Sempre registre código, horário e, se o sistema mostrar, o **identificador de correlação** permitido — ele ajuda a equipe a achar o erro nos registros.

## Como saber que resolveu

- [ ] O usuário fez login.
- [ ] A tarefa original foi concluída no sistema.

## O que anotar no chamado

- [ ] URL e código de erro (pelo canal interno)
- [ ] Navegador e versão
- [ ] Resultado da comparação (janela privativa / outro navegador)
- [ ] Resultado da tarefa final

## Quando encaminhar ao N2

- Erro geral (várias pessoas).
- Acesso negado que exige liberação.
- Falha do servidor.

## Erros comuns

- **Limpar todos os dados do navegador** "por garantia".
- **Ignorar alerta de certificado** para "conseguir entrar".
- **Conceder ou pedir acesso** sem aprovação do responsável pelo sistema.

## Guias relacionados

[KB-05 · Conectado sem internet](kb-05-wifi-sem-internet.md) · [KB-07 · DNS](kb-07-falha-dns.md) · [KB-15 · VPN conecta, sistema não abre](kb-15-vpn-conecta-sistema-nao-abre.md)

---

[← Anterior: KB-19](kb-19-segundo-monitor.md) · [↑ Índice](../README.md#indice)

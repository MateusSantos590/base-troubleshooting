# KB-15 · VPN conecta, mas o sistema não abre

[← Índice](../README.md#indice) · **Categoria:** Acesso remoto · **Quem executa:** N1 com o usuário

> **Em uma frase:** o túnel está pronto, mas algo no destino falha. Descubra se é o **nome** (DNS), o **caminho** (rota) ou a **permissão** (autorização).

---

## Entenda o problema

Você entrou no prédio da empresa pelo túnel (VPN conectada). Mas, para chegar a uma sala específica, ainda precisa:

1. **Saber o endereço da sala** → DNS (o nome resolve?).
2. **Ter um corredor até ela** → rota (o tráfego chega?).
3. **Ter a chave da porta** → permissão (você está autorizado?).

Cada uma dessas falhas gera uma mensagem diferente. Ler a mensagem com atenção economiza muito tempo.

**Sintoma típico:** a VPN mostra "conectado", mas um sistema interno continua inacessível.

**Causas mais comuns:** falha de DNS, rota ausente, falta de permissão ou sistema fora do ar.

## Pergunte primeiro

- Qual sistema não abre? Qual é o endereço exato?
- **Todos** os sistemas internos falham ou só um?
- Que mensagem aparece? ("não encontrado", "acesso negado", "tempo esgotado"…)
- Um colega consegue abrir o mesmo sistema?

## Antes de começar

> [!WARNING]
> Não crie rotas nem altere regras de acesso por tentativa. E ao comparar com um colega, **ninguém compartilha credenciais**.

---

## Passo a passo

### Passo 1 — Confirme o endereço e o escopo

**Faça:** confira o endereço do sistema e se a falha afeta **um** ou **todos** os recursos internos.

**Por quê:** se nenhum recurso interno abre, o problema pode ser a própria VPN. Se só um falha, o problema é daquele recurso.

**O que você deve ver:** o escopo definido.

### Passo 2 — Teste a resolução de nome

**Faça:** siga o [KB-07](kb-07-falha-dns.md) e execute `nslookup` com o nome do sistema.

**Por quê:** é o primeiro "corredor": se o nome não vira endereço, nada mais acontece.

**O que você deve ver:** o nome resolvendo para um endereço — ou não.

### Passo 3 — Compare com outro recurso e outro usuário

**Faça:** tente outro sistema interno autorizado. Pergunte se outro usuário consegue abrir o sistema afetado.

**Por quê:** se você consegue abrir outro sistema e o colega abre este, o problema é específico da sua conta ou do seu acesso.

**O que você deve ver:** um padrão claro de quem/qual funciona.

### Passo 4 — Diferencie os três tipos de erro

**Faça:** classifique a mensagem: **nome não encontrado**, **acesso negado** ou **tempo esgotado**.

**Por quê:** cada uma aponta para uma camada diferente (veja a tabela abaixo).

**O que você deve ver:** o tipo de erro anotado.

---

## Como interpretar o resultado

| Mensagem | Camada provável | Analogia | Próximo passo |
|---|---|---|---|
| **Nome não encontrado** | DNS | Não sabe o endereço da sala | [KB-07](kb-07-falha-dns.md) |
| **Acesso negado** (ex.: 403) | Permissão | Chegou à porta, mas a chave não abre | Investigue autorização com a equipe responsável; **não é falha da VPN** |
| **Tempo esgotado** | Caminho ou sistema fora do ar | O corredor está bloqueado ou a sala está vazia | Registre o teste; não conclua sozinho que é firewall |
| Nenhum recurso interno abre | A própria VPN | O túnel não leva a lugar nenhum | [KB-14](kb-14-vpn-nao-conecta.md) |

## Como saber que resolveu

- [ ] O sistema abriu.
- [ ] O usuário executou a tarefa original.

## O que anotar no chamado

- [ ] Recurso afetado (endereço pelo canal interno)
- [ ] Resultado da resolução de nome
- [ ] Mensagem exata e tipo de erro
- [ ] Comparação com outro recurso e outro usuário

## Quando encaminhar ao N2

Sempre que o problema persistir após os testes. Informe: VPN usada, horário, erro e resultados de cada passo.

## Erros comuns

- **Tratar toda falha como "problema de VPN".** Acesso negado é questão de permissão.
- **Afirmar que "é o firewall"** sem evidência.
- **Pedir a senha de um colega** para comparar.

## Guias relacionados

[KB-14 · VPN não conecta](kb-14-vpn-nao-conecta.md) · [KB-07 · DNS](kb-07-falha-dns.md) · [KB-20 · Sistema web](kb-20-sistema-web.md)

**Referência oficial:** [Conectar-se a uma VPN no Windows][vpn] — a referência cobre a configuração; a triagem acima é uma proposta de estudo.

---

[← Anterior: KB-14](kb-14-vpn-nao-conecta.md) · [↑ Índice](../README.md#indice) · [Próximo: KB-16 →](kb-16-conta-bloqueada.md)

[vpn]: https://support.microsoft.com/pt-br/windows/experience/connectivity-networking/connect-to-a-vpn-in-windows

# KB-07 · Falha de resolução DNS

[← Índice](../README.md#indice) · **Categoria:** Redes · **Quem executa:** N1 (limpar cache pode exigir permissão)

> **Em uma frase:** a rede funciona, mas o computador não consegue traduzir o **nome** do sistema no **endereço** dele.

---

## Entenda o problema

O DNS é a **lista de contatos** da rede. Você toca em "Maria" e o celular disca o número dela. Se o contato não existe, foi salvo errado ou a lista não abre, você não consegue ligar — mesmo com o telefone funcionando perfeitamente.

Da mesma forma, você digita `sistema.empresa` e o DNS informa o endereço IP. Se essa tradução falha, o navegador não sabe para onde ir.

**Sintoma típico:** o nome de um recurso não abre (ex.: "não foi possível encontrar o servidor"), embora a rede esteja ativa.

**Causas mais comuns:** servidor DNS incorreto, cache com resposta antiga ou recurso interno que exige VPN.

## Pergunte primeiro

- Qual é o endereço **exato** que você está tentando abrir?
- Esse sistema exige VPN quando você está fora do escritório?
- Outros sites abrem normalmente?

## Antes de começar

> [!CAUTION]
> **Não troque o DNS corporativo por um DNS público** (como os de grandes provedores) "para testar". DNS públicos não conhecem os nomes internos da empresa e isso pode violar a política de segurança.

---

## Passo a passo

### Passo 1 — Confirme o endereço e a VPN

**Faça:** confira com o usuário o endereço correto (pelo canal oficial) e se o recurso exige VPN.

**Por quê:** um erro de digitação ou a falta de VPN produzem o mesmo sintoma de uma falha de DNS — e são muito mais comuns.

**O que você deve ver:** endereço correto e VPN conectada, se necessária.

### Passo 2 — Pergunte ao DNS com `nslookup`

**Faça:** execute `nslookup nome-do-servico`, trocando pelo nome autorizado. ([Como ler](../docs/COMANDOS.md#nslookup--qual-é-o-número-desse-nome))

**Por quê:** é a forma direta de perguntar "DNS, qual o endereço desse nome?" e ver a resposta.

**O que você deve ver:** um endereço IP, uma mensagem de "domínio inexistente" ou um "tempo esgotado".

### Passo 3 — Compare com o esperado

**Faça:** compare o endereço retornado e o servidor DNS consultado com o que a TI documentou.

**Por quê:** uma resposta pode vir, mas estar **errada** (endereço antigo, servidor DNS diferente do esperado).

**O que você deve ver:** se a resposta bate com a documentação.

### Passo 4 — Limpe o cache, se houver indício

**Faça:** apenas se houver evidência de resposta antiga guardada no computador, execute `ipconfig /flushdns` (com a permissão necessária) e teste de novo.

**Por quê:** o computador guarda respostas para ganhar tempo. Se o sistema mudou de endereço, ele pode continuar indo ao endereço velho.

**O que você deve ver:** o nome passando a resolver para o endereço correto.

---

## Como interpretar o resultado

Os dois erros abaixo **parecem iguais para o usuário, mas são diferentes**:

| Resultado do `nslookup` | Significa… | Analogia | Próximo passo |
|---|---|---|---|
| **Domínio inexistente** | O DNS respondeu: "não conheço esse nome" | O contato não está na agenda | Confira o nome e a VPN; pode faltar o registro |
| **Tempo esgotado** | O servidor DNS **não respondeu** | A agenda não abre | Verifique o alcance até o DNS; encaminhe se geral |
| Endereço **diferente** do esperado | Resposta antiga ou DNS errado | Número de telefone desatualizado | Passo 4 ou encaminhe |
| Endereço correto, mas o sistema não abre | O DNS está ok; problema em outra camada | — | [KB-20](kb-20-sistema-web.md) |

> [!NOTE]
> O `nslookup` consulta o DNS diretamente e pode dar resultado diferente do navegador. Ele prova a tradução do nome, não o funcionamento do sistema.

## Como saber que resolveu

- [ ] O nome resolve para o endereço correto.
- [ ] O serviço abre normalmente **pelo nome**.

> [!IMPORTANT]
> Abrir o sistema digitando o endereço IP direto **não é validação**: isso pula o DNS e pode quebrar o certificado HTTPS.

## O que anotar no chamado

- [ ] Nome consultado
- [ ] Servidor DNS usado
- [ ] Resposta ou erro (domínio inexistente × tempo esgotado)
- [ ] Comparação com o endereço documentado pela TI

## Quando encaminhar ao N2

- Registro DNS ausente para um nome que deveria existir.
- Falha do DNS corporativo (vários usuários afetados).

## Erros comuns

- **Tratar "domínio inexistente" e "tempo esgotado" como a mesma coisa.**
- **Trocar para DNS público** para "fazer funcionar".
- **Validar pelo IP** em vez do nome.

## Guias relacionados

[KB-05 · Conectado sem internet](kb-05-wifi-sem-internet.md) · [KB-15 · VPN conecta, sistema não abre](kb-15-vpn-conecta-sistema-nao-abre.md) · [KB-20 · Sistema web](kb-20-sistema-web.md)

**Referências oficiais:** [Diagnóstico do cliente DNS][dns] · [Comando ipconfig][ipconfig] · [Comando nslookup][nslookup]

---

[← Anterior: KB-06](kb-06-rede-cabeada.md) · [↑ Índice](../README.md#indice) · [Próximo: KB-08 →](kb-08-ip-169-254.md)

[dns]: https://learn.microsoft.com/pt-br/windows-server/networking/dns/troubleshoot/troubleshoot-dns-client
[ipconfig]: https://learn.microsoft.com/pt-br/windows-server/administration/windows-commands/ipconfig
[nslookup]: https://learn.microsoft.com/pt-br/windows-server/administration/windows-commands/nslookup

# Comandos de consulta — o que fazem e como ler o resultado

[← Voltar ao início](../README.md) · [Método](METODO.md) · [Glossário](GLOSSARIO.md)

Estes são os únicos comandos usados nos guias. A maioria só **consulta** (olha sem mexer). Dois deles **alteram** algo e estão marcados.

---

## Como abrir o terminal no Windows 11

1. Pressione `Win + R`, digite `cmd` e pressione `Enter`. Abre o **Prompt de Comando**.
2. Ou clique com o botão direito no menu Iniciar e escolha **Terminal**. Abre o **PowerShell**.

Os comandos desta página funcionam nos dois.

> [!NOTE]
> Para os comandos de consulta, **não** é preciso abrir como administrador. Se algum comando pedir permissão elevada, pare e siga a política da empresa.

---

## Resumo

| Comando | Para que serve | Muda algo? | Cuidado |
|---|---|---|---|
| `ipconfig` | Ver o endereço IP e o gateway | Não | Identifique qual adaptador está em uso |
| `ipconfig /all` | Ver detalhes: DHCP, DNS, adaptador físico | Não | A saída tem dados internos — não publique |
| `nslookup nome` | Perguntar ao DNS qual o IP de um nome | Não | Responder não prova que o sistema funciona |
| `ping destino` | Perguntar "você está aí?" a um equipamento | Não | Sem resposta **não** prova que está desligado |
| `ipconfig /flushdns` | Apagar o cache de nomes do computador | **Sim** | Use só com indício de cache desatualizado |
| `ipconfig /renew` | Pedir um novo endereço ao DHCP | **Sim** | Pode derrubar a conexão — e o acesso remoto |

---

## `ipconfig` — "qual é o meu endereço?"

**Analogia:** olhar o número da sua casa e o caminho até a saída do condomínio.

```text
ipconfig
```

**O que procurar na saída** (exemplo fictício):

```text
Adaptador de Rede sem Fio Wi-Fi:
   Endereço IPv4. . . . . . . . . . : 192.168.0.25      ← o "número da casa"
   Máscara de Sub-rede . . . . . . : 255.255.255.0
   Gateway Padrão. . . . . . . . . : 192.168.0.1       ← a "saída do condomínio"
```

| Se você ver… | Significa… | Vá para |
|---|---|---|
| Um endereço normal e um gateway preenchido | O computador recebeu configuração de rede | Teste DNS ([KB-07](../guias/kb-07-falha-dns.md)) ou o recurso ([KB-05](../guias/kb-05-wifi-sem-internet.md)) |
| Endereço começando com `169.254.` | O computador **não recebeu** endereço do DHCP | [KB-08](../guias/kb-08-ip-169-254.md) |
| "Mídia desconectada" no adaptador cabeado | Não há enlace físico | [KB-06](../guias/kb-06-rede-cabeada.md) |
| Vários adaptadores | Alguns são virtuais (VPN, máquinas virtuais) | Identifique o que está em uso antes de concluir |

---

## `ipconfig /all` — "me mostre todos os detalhes"

```text
ipconfig /all
```

Mostra tudo do `ipconfig`, mais:

- **DHCP Habilitado:** `Sim` = o endereço deveria vir automaticamente.
- **Servidores DNS:** quem o computador consulta para traduzir nomes.
- **Descrição:** o nome do adaptador físico (ajuda a separar o real dos virtuais).

> [!WARNING]
> Essa saída contém endereços e nomes internos da empresa. Use para diagnóstico, registre só o necessário no sistema interno e **nunca** publique o texto bruto.

---

## `nslookup` — "qual é o número desse nome?"

**Analogia:** procurar o telefone de alguém na lista de contatos.

```text
nslookup nome-do-servico
```

Troque `nome-do-servico` por um nome **autorizado** (ex.: o endereço do sistema que a TI documentou).

| Resultado | Significa… |
|---|---|
| Aparece um ou mais endereços | O DNS conhece o nome. Compare com o endereço esperado pela TI |
| `Non-existent domain` / domínio inexistente | O DNS respondeu que **esse nome não existe**: nome digitado errado, registro ausente ou falta de VPN |
| `Request timed out` / tempo esgotado | O DNS **não respondeu**: problema de alcance até o servidor DNS |

> [!IMPORTANT]
> "Nome inexistente" e "tempo esgotado" são problemas **diferentes**. O primeiro é uma resposta ("não conheço"); o segundo é silêncio. Anote qual dos dois apareceu.

**Limite:** o `nslookup` consulta o DNS diretamente e pode dar resultado diferente do navegador. Ele prova que o nome resolve — não que o sistema está funcionando.

---

## `ping` — "você está aí?"

```text
ping destino-autorizado
```

| Resultado | Significa… |
|---|---|
| `Resposta de …` | O destino respondeu: há caminho até ele |
| `Esgotado o tempo limite` | Nenhuma resposta. **Pode** ser equipamento fora do ar, **ou** firewall que bloqueia ping |

> [!CAUTION]
> Muitas redes bloqueiam ping de propósito. Ficar sem resposta, sozinho, **não prova nada**. Sempre combine com outro teste (abrir o recurso real, por exemplo).

---

## `ipconfig /flushdns` — apagar o cache de nomes ⚠️ altera

**Analogia:** apagar da memória um número de telefone para ser obrigado a consultar a agenda de novo.

```text
ipconfig /flushdns
```

**Quando usar:** só quando houver indício de que o computador guardou uma resposta antiga (ex.: o sistema mudou de endereço e só esse computador continua indo ao endereço velho).

**Efeito:** baixo risco, mas é uma mudança. Registre no chamado.

---

## `ipconfig /renew` — pedir novo endereço ao DHCP ⚠️ altera

**Analogia:** devolver a chave do quarto e pedir outra na recepção.

```text
ipconfig /renew
```

**Quando usar:** quando o adaptador está configurado para DHCP e não recebeu endereço (ex.: `169.254.x.x`).

> [!CAUTION]
> Durante a renovação, a conexão pode cair. **Em acesso remoto, você pode perder a conexão com o usuário.** Combine antes como vocês vão se reconectar (telefone, por exemplo). Para agir em um adaptador específico, use o nome exato dele, conforme a [documentação oficial][ipconfig].

---

## Não é comando de rede: `outlook.exe /safe`

Aparece no [KB-12](../guias/kb-12-outlook-nao-abre.md). É digitado em `Win + R` e abre o **Outlook clássico** sem suplementos. Não funciona no novo Outlook.

---

## Regras gerais

- Execute consultas só contra **destinos autorizados**. Mesmo consultas geram tráfego.
- Não rode "sequências de reset" de rede (ex.: comandos que redefinem toda a pilha de rede) sem evidência e autorização.
- Não troque DNS, apague perfis ou reinstale nada por tentativa.

**Referências oficiais:** [ipconfig][ipconfig] · [nslookup][nslookup] · [Diagnóstico do cliente DNS][dns]

---

[← Voltar ao início](../README.md)

[ipconfig]: https://learn.microsoft.com/pt-br/windows-server/administration/windows-commands/ipconfig
[nslookup]: https://learn.microsoft.com/pt-br/windows-server/administration/windows-commands/nslookup
[dns]: https://learn.microsoft.com/pt-br/windows-server/networking/dns/troubleshoot/troubleshoot-dns-client

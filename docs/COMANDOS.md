# Comandos de diagnóstico — o que fazem e como ler o resultado

[← Voltar ao início](../README.md) · [Método](METODO.md) · [Glossário](GLOSSARIO.md)

Estes são os comandos usados nos guias, mais alguns de consulta que todo técnico N1 deveria conhecer. A maioria só **consulta** (olha sem mexer). Os que **alteram** algo estão marcados com ⚠️.

> [!TIP]
> **Como estudar esta página:** não decore a sintaxe. Para cada comando, guarde **a pergunta que ele responde** ("qual é o meu endereço?", "esse nome existe?", "essa porta responde?"). Quando surgir a dúvida no atendimento, a pergunta puxa o comando.

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
| `tracert destino` | Ver o caminho (saltos) até um destino | Não | Saltos sem resposta são comuns e não provam falha |
| `Test-NetConnection destino -Port 443` | Testar se uma **porta** específica responde | Não | Só no PowerShell |
| `net use` | Listar unidades de rede mapeadas | Não | Sem parâmetros, só lista |
| `whoami` | Mostrar com qual conta você está logado | Não | — |
| `winver` / `systeminfo` | Ver versão e detalhes do Windows | Não | `systeminfo` mostra dados internos — não publique |
| `powercfg /batteryreport` | Gerar relatório de saúde da bateria | Cria um arquivo | Não altera configurações |
| `perfmon /rel` | Abrir o Monitor de Confiabilidade | Não | — |

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

## `tracert` — "por onde o caminho passa?"

**Analogia:** o rastreamento de uma encomenda, mostrando cada centro de distribuição por onde ela passou.

```text
tracert destino-autorizado
```

Mostra cada **salto** (roteador) entre o computador e o destino, com o tempo de resposta.

| Resultado | Significa… |
|---|---|
| Os saltos avançam até o destino | Há caminho completo |
| Um salto com `*` (asteriscos) e os seguintes respondem | Aquele roteador só não responde a esse tipo de teste — **normal** |
| Todos os saltos a partir de certo ponto com `*` | O caminho pode estar interrompido ali, **ou** a rede bloqueia o teste |

> [!NOTE]
> Assim como o `ping`, o `tracert` pode ser bloqueado. Use para dar contexto ao N2, não para concluir sozinho.

---

## `Test-NetConnection` — "essa porta específica responde?"

**Analogia:** não basta o prédio existir (`ping`); você quer saber se a **porta da loja** está aberta.

```powershell
Test-NetConnection sistema.empresa -Port 443
```

Funciona no **PowerShell**. A porta `443` é a do HTTPS (sites); outros serviços usam outras portas, documentadas pela TI.

| Campo na saída | Significa… |
|---|---|
| `TcpTestSucceeded : True` | A porta respondeu: há caminho até o serviço |
| `TcpTestSucceeded : False` | A porta não respondeu: serviço parado, firewall ou falta de VPN |
| `RemoteAddress` | O endereço para o qual o nome foi traduzido — confira com o esperado |

**Por que é útil:** separa "o nome resolve e a porta responde" (problema provavelmente no sistema ou no login) de "a porta não responde" (problema de caminho). Veja o [KB-15](../guias/kb-15-vpn-conecta-sistema-nao-abre.md).

---

## `net use` — "quais unidades de rede estão mapeadas?"

**Analogia:** olhar o chaveiro e ver qual chave abre qual sala.

```text
net use
```

| Coluna | Significa… |
|---|---|
| `Status` | `OK` = conectada; `Desconectado` ou `Indisponível` = sem conexão no momento |
| `Local` | A letra da unidade (ex.: `S:`) |
| `Remoto` | O caminho real (`\\servidor\pasta`) |

> [!WARNING]
> **Sem parâmetros, só lista.** Variações como `net use S: /delete` **removem** o mapeamento. Não use sem saber como recriá-lo. Veja o [KB-23](../guias/kb-23-pasta-de-rede.md).

---

## `whoami` — "com qual conta estou logado?"

```text
whoami
```

Mostra `DOMINIO\usuario` ou a conta local. Útil quando o usuário diz "estou sem acesso" e, na verdade, está logado com **outra conta** (ex.: conta local ou de um colega que usou o computador).

---

## `winver` e `systeminfo` — "qual Windows é este?"

```text
winver
```

Abre uma janela com a **versão** e o **build** do Windows. É o dado que você anota no chamado e no [plano de validação](VALIDACAO.md).

```text
systeminfo
```

Mostra versão, fabricante, modelo, memória, data de instalação e **tempo desde a última inicialização** ("Tempo de Inicialização do Sistema"). Ajuda a confirmar se o computador realmente reiniciou.

> [!WARNING]
> A saída do `systeminfo` contém nomes e dados internos. Registre só o necessário.

---

## `powercfg /batteryreport` — como está a saúde da bateria?

```text
powercfg /batteryreport
```

**Cria** um arquivo `battery-report.html` na pasta em que o terminal está (o caminho aparece na tela). Abra-o no navegador.

| Campo no relatório | Significa… |
|---|---|
| `DESIGN CAPACITY` | Quanto a bateria guardava quando era nova |
| `FULL CHARGE CAPACITY` | Quanto ela guarda **hoje** com carga completa |
| `Battery capacity history` | Como a capacidade caiu ao longo do tempo |

**Conta rápida:** `Full Charge ÷ Design × 100` = saúde aproximada. Exemplo fictício: 32.000 ÷ 50.000 × 100 = **64%** — a bateria guarda pouco mais da metade do que guardava nova. Veja o [KB-28](../guias/kb-28-notebook-nao-carrega.md).

---

## `perfmon /rel` — o histórico de falhas

```text
perfmon /rel
```

Abre o **Monitor de Confiabilidade**: um gráfico por dia com falhas de aplicativos, do Windows e instalações. É a forma mais rápida de responder "**o que mudou antes do problema começar?**". Veja o [KB-26](../guias/kb-26-tela-azul.md).

---

## Não é comando de rede: `outlook.exe /safe`

Aparece no [KB-12](../guias/kb-12-outlook-nao-abre.md). É digitado em `Win + R` e abre o **Outlook clássico** sem suplementos. Não funciona no novo Outlook.

---

## Regras gerais

- Execute consultas só contra **destinos autorizados**. Mesmo consultas geram tráfego.
- Não rode "sequências de reset" de rede (ex.: comandos que redefinem toda a pilha de rede) sem evidência e autorização.
- Não troque DNS, apague perfis ou reinstale nada por tentativa.

**Referências oficiais:** [ipconfig][ipconfig] · [nslookup][nslookup] · [Diagnóstico do cliente DNS][dns] · [tracert][tracert] · [net use][netuse] · [whoami][whoami] · [systeminfo][systeminfo] · [Test-NetConnection][tnc] · [powercfg][powercfg]

---

[← Voltar ao início](../README.md)

[ipconfig]: https://learn.microsoft.com/pt-br/windows-server/administration/windows-commands/ipconfig
[nslookup]: https://learn.microsoft.com/pt-br/windows-server/administration/windows-commands/nslookup
[dns]: https://learn.microsoft.com/pt-br/windows-server/networking/dns/troubleshoot/troubleshoot-dns-client
[tracert]: https://learn.microsoft.com/pt-br/windows-server/administration/windows-commands/tracert
[netuse]: https://learn.microsoft.com/pt-br/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/gg651155(v=ws.11)
[whoami]: https://learn.microsoft.com/pt-br/windows-server/administration/windows-commands/whoami
[systeminfo]: https://learn.microsoft.com/pt-br/windows-server/administration/windows-commands/systeminfo
[tnc]: https://learn.microsoft.com/pt-br/powershell/module/nettcpip/test-netconnection
[powercfg]: https://learn.microsoft.com/pt-br/windows-hardware/design/device-experiences/powercfg-command-line-options

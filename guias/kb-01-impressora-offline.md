# KB-01 · Impressora offline

[← Índice](../README.md#indice) · **Categoria:** Impressão · **Quem executa:** N1 com o usuário

> **Em uma frase:** o computador não consegue "conversar" com a impressora. Descubra se o problema está **no caminho** (energia, cabo, rede) ou **no destino** (impressora errada selecionada).

---

## Entenda o problema

Imprimir é como mandar uma carta: o computador escreve, a fila de impressão é o correio e a impressora é o destinatário. "Offline" quer dizer que o correio **não encontra o destinatário** — porque ele está desligado, o endereço está errado ou a estrada (cabo/rede) está interrompida.

**Sintoma típico:** a impressão não sai e a fila mostra a impressora como *offline* ou *indisponível*.

**Causas mais comuns:** impressora desligada, conexão interrompida ou impressora errada selecionada.

## Pergunte primeiro

- Qual impressora você escolheu na hora de imprimir? (nome exato)
- O painel da impressora mostra algum aviso ou luz piscando?
- Outras pessoas conseguem usar essa mesma impressora?
- Ela funcionava antes? Mudou algo (troca de lugar, de rede, de cabo)?

## Antes de começar

> [!WARNING]
> Mexa apenas na fila e na impressora **do usuário**. Não pause nem cancele filas compartilhadas sem permissão: isso afeta outras pessoas.

---

## Passo a passo

### Passo 1 — Confirme a impressora selecionada e o painel

**Faça:** veja qual impressora aparece na janela de impressão. Depois, olhe o painel físico do equipamento (avisos de papel, tinta, erro).

**Por quê:** é comum ter várias impressoras instaladas e o documento ir para a errada — por exemplo, a de outro andar ou uma "impressora PDF".

**O que você deve ver:** o nome da impressora correta selecionado e o painel sem erros.

### Passo 2 — Verifique energia e conexão

**Faça:** confirme que a impressora está ligada e conectada (cabo USB, cabo de rede ou Wi-Fi). Se ela for de rede, confira com o responsável qual é o endereço esperado.

**Por quê:** é o caminho entre o computador e a impressora. Sem caminho, nenhuma configuração resolve.

**O que você deve ver:** impressora ligada, cabo firme ou indicador de rede ativo no painel.

### Passo 3 — Confira se a fila está pausada

**Faça:** em **Configurações → Bluetooth e dispositivos → Impressoras e scanners**, clique na impressora e abra a fila. Veja se está **pausada** ou marcada para **usar impressora offline**. Retome apenas a fila correta.

**Por quê:** uma fila pausada segura todos os documentos, mesmo com a impressora funcionando.

**O que você deve ver:** fila ativa, com os documentos começando a sair.

### Passo 4 — Imprima uma página de teste

**Faça:** na mesma tela da impressora, escolha **Imprimir página de teste**.

**Por quê:** a página de teste não depende de nenhum arquivo ou programa. Ela separa "a impressora funciona" de "o documento tem algum problema".

**O que você deve ver:** a página sai na impressora correta.

---

## Como interpretar o resultado

| Se você observar… | Provavelmente significa… | Próximo passo |
|---|---|---|
| A página de teste **também falha** | O problema está no equipamento ou na conexão | Volte ao Passo 2; persistindo, encaminhe |
| A página de teste sai, mas **um arquivo específico** não | O problema está no documento ou no programa | Teste outro arquivo; **não** reinstale o driver ainda |
| A impressora nem aparece na lista | Ela não está instalada nesse computador | Veja [KB-03](kb-03-driver-de-impressora.md) |
| Vários usuários com a mesma falha | Problema no equipamento ou no servidor de impressão | Encaminhe ao N2 |

## Como saber que resolveu

- [ ] A página de teste saiu na impressora correta.
- [ ] O usuário imprimiu o documento original que motivou o chamado.

## O que anotar no chamado

- [ ] Impressora selecionada (nome e modelo) e tipo de conexão (USB, rede, Wi-Fi)
- [ ] Estado da fila (pausada, offline, com erro)
- [ ] Mensagem do painel, se houver
- [ ] Resultado da página de teste

## Quando encaminhar ao N2

- Equipamento inacessível mesmo ligado e conectado.
- Servidor de impressão com falha.
- Várias pessoas afetadas.

Informe modelo, tipo de conexão e mensagem exata.

## Erros comuns

- **Reinstalar o driver logo de cara.** Se a página de teste funcionou, o driver está ok.
- **Cancelar a fila inteira de uma impressora compartilhada.** Você apagaria documentos de outras pessoas.
- **Esquecer de conferir a impressora selecionada.** É a causa mais simples e uma das mais frequentes.

## Guias relacionados

[KB-02 · Documento preso na fila](kb-02-documento-preso-na-fila.md) · [KB-03 · Driver ausente](kb-03-driver-de-impressora.md)

**Referência oficial:** [Problemas de conexão e impressão no Windows][impressao]

---

[↑ Índice](../README.md#indice) · [Próximo: KB-02 →](kb-02-documento-preso-na-fila.md)

[impressao]: https://support.microsoft.com/pt-br/windows/hardware/printer/fix-printer-connection-and-printing-problems-in-windows

# KB-02 · Documento preso na fila

[← Índice](../README.md#indice) · **Categoria:** Impressão · **Quem executa:** N1 com o usuário (reiniciar o serviço exige autorização)

> **Em uma frase:** um documento travou na fila e está segurando todos os outros. Descubra se o problema é **aquele documento** ou **a fila inteira**.

---

## Entenda o problema

Pense na fila de um caixa de supermercado: se um cliente trava no pagamento, todos atrás dele esperam — mesmo que o caixa esteja funcionando. Na impressão, um documento com erro pode bloquear a fila do mesmo jeito.

**Sintoma típico:** um trabalho não termina e os seguintes ficam "aguardando".

**Causas mais comuns:** um documento com erro, a fila pausada ou o serviço de impressão (spooler) com falha.

## Pergunte primeiro

- Qual documento você mandou primeiro? Ele é grande, tem muitas imagens ou veio de um programa diferente?
- Outros documentos também ficam presos?
- A impressora é só sua ou compartilhada com outras pessoas?

## Antes de começar

> [!WARNING]
> **Nunca cancele documentos de outras pessoas.** Em filas compartilhadas, cancele somente o trabalho do usuário atendido. Reiniciar o serviço de impressão afeta todas as impressões do computador e exige autorização.

---

## Passo a passo

### Passo 1 — Compare com outro documento

**Faça:** peça para imprimir um documento simples (uma página de texto, por exemplo).

**Por quê:** se o simples imprime, o problema está no documento original. Se nada imprime, o problema está na fila ou na impressora.

**O que você deve ver:** um dos dois cenários acima, que define o próximo passo.

### Passo 2 — Cancele apenas o trabalho problemático

**Faça:** abra a fila (**Configurações → Bluetooth e dispositivos → Impressoras e scanners →** impressora **→ Abrir fila de impressão**), selecione **somente** o documento travado e cancele. Faça isso junto com o usuário.

**Por quê:** liberar o "cliente travado" deixa a fila andar sem apagar o trabalho dos outros.

**O que você deve ver:** o documento sumindo da fila e os seguintes começando a imprimir.

### Passo 3 — Se persistir, registre e peça autorização

**Faça:** anote o estado da fila (pausada, com erro, quantos trabalhos). Reiniciar o **Spooler de Impressão** só com autorização e depois de avaliar o impacto.

**Por quê:** o spooler atende todas as impressões do computador. Reiniciá-lo sem combinar pode interromper outras impressões em andamento.

**O que você deve ver:** um registro claro do que foi observado, pronto para seguir ou encaminhar.

---

## Como interpretar o resultado

| Se você observar… | Provavelmente significa… | Próximo passo |
|---|---|---|
| A fila está **pausada** | Isso explica os trabalhos esperando — mas não prova que o documento está corrompido | Retome a fila e observe |
| Só **um arquivo** volta a travar a fila | O problema está nesse arquivo ou no programa que o gerou | Registre o formato (sem expor o conteúdo) e encaminhe |
| **Nenhum** documento imprime, nem o simples | Problema na fila, no serviço ou na impressora | Veja [KB-01](kb-01-impressora-offline.md) |
| A fila compartilhada está travada para várias pessoas | Problema no servidor de impressão | Encaminhe ao N2 |

## Como saber que resolveu

- [ ] O documento simples imprimiu.
- [ ] O documento original imprimiu (ou foi identificado como a causa e encaminhado).

## O que anotar no chamado

- [ ] Fila local ou compartilhada
- [ ] Documento afetado (tipo/formato, **sem** o conteúdo)
- [ ] Resultado do teste com documento simples
- [ ] O que foi cancelado e o impacto disso

## Quando encaminhar ao N2

- Fila compartilhada afetada.
- O problema se repete com frequência.
- É preciso reiniciar o serviço e você não tem autorização.

## Erros comuns

- **Cancelar todos os documentos da fila** "para garantir". Você apaga o trabalho de outras pessoas.
- **Concluir que o documento está corrompido** só porque a fila estava pausada.
- **Mandar imprimir de novo várias vezes.** Isso só aumenta a fila.

## Guias relacionados

[KB-01 · Impressora offline](kb-01-impressora-offline.md) · [KB-03 · Driver ausente](kb-03-driver-de-impressora.md)

**Referência oficial:** [Problemas de conexão e impressão no Windows][impressao]

---

[← Anterior: KB-01](kb-01-impressora-offline.md) · [↑ Índice](../README.md#indice) · [Próximo: KB-03 →](kb-03-driver-de-impressora.md)

[impressao]: https://support.microsoft.com/pt-br/windows/hardware/printer/fix-printer-connection-and-printing-problems-in-windows

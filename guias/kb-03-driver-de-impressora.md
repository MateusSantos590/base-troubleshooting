# KB-03 · Driver de impressora ausente

[← Índice](../README.md#indice) · **Categoria:** Impressão · **Quem executa:** N1 (instalação pode exigir equipe autorizada)

> **Em uma frase:** o Windows enxerga a impressora, mas não sabe como usá-la. Falta o "manual de instruções" certo — o driver compatível.

---

## Entenda o problema

O **driver** é como um tradutor entre o Windows e a impressora. Se o tradutor fala o idioma errado (modelo diferente) ou é de outro tipo de processador (x64 × ARM64), a conversa não acontece.

**Sintoma típico:** o equipamento é detectado, mas a instalação falha ou não conclui.

**Causas mais comuns:** pacote incompatível com o modelo ou o sistema, falta de permissão de administrador ou conexão instável durante a instalação.

## Pergunte primeiro

- Qual é o modelo **exato** da impressora? (está na etiqueta do equipamento)
- Que mensagem aparece quando a instalação falha?
- De onde veio o instalador que você tentou usar?

## Antes de começar

> [!CAUTION]
> Use apenas drivers **homologados pela TI** ou do **site oficial do fabricante**. Sites de "drivers grátis" de terceiros são uma porta comum para vírus. E nunca use credencial de administrador emprestada.

---

## Passo a passo

### Passo 1 — Identifique modelo, Windows e arquitetura

**Faça:** anote o modelo exato da impressora. No computador, abra **Configurações → Sistema → Sobre** e anote a edição do Windows e o **tipo de sistema** (x64 ou ARM64).

**Por quê:** o driver precisa combinar com os três. É como comprar uma peça de carro: modelo, ano e motor têm que bater.

**O que você deve ver:** três informações anotadas — modelo, edição/build e arquitetura.

### Passo 2 — Confira conexão e mensagem antes de mexer

**Faça:** confirme que a impressora aparece conectada e anote a mensagem de erro da instalação.

**Por quê:** se a impressora nem está conectada, o problema não é driver. Corrija a detecção primeiro.

**O que você deve ver:** impressora detectada e mensagem de erro registrada.

### Passo 3 — Use o pacote correto

**Faça:** obtenha o pacote homologado pela TI ou do fabricante, **específico para o modelo e a arquitetura** anotados.

**Por quê:** um pacote genérico ou de outro modelo pode até instalar, mas imprimir errado ou não imprimir.

**O que você deve ver:** instalador do modelo correto, de origem confiável.

### Passo 4 — Instale (ou peça a quem pode)

**Faça:** se a instalação pedir permissão de administrador e você não tiver, **pare** e solicite à equipe autorizada.

**Por quê:** essa permissão existe para proteger o computador. Contorná-la abre brechas de segurança.

**O que você deve ver:** instalação concluída sem erro.

---

## Como interpretar o resultado

| Se você observar… | Provavelmente significa… | Próximo passo |
|---|---|---|
| A impressora **nem aparece** conectada | Problema de detecção, não de driver | Resolva a conexão ([KB-01](kb-01-impressora-offline.md)) |
| A instalação pede **administrador** | Política de segurança da empresa | Solicite à equipe autorizada |
| O pacote instala, mas a impressão sai errada | Pacote incompatível com o modelo | Confira modelo e arquitetura de novo |
| Erro persiste com o pacote correto | Algo além do escopo do N1 | Encaminhe com a mensagem exata |

## Como saber que resolveu

- [ ] Instalação concluída sem erro.
- [ ] Página de teste impressa.
- [ ] Documento do usuário impresso.

## O que anotar no chamado

- [ ] Modelo da impressora
- [ ] Arquitetura (x64/ARM64) e edição/build do Windows
- [ ] Origem e versão do pacote usado
- [ ] Mensagem de erro exata

## Quando encaminhar ao N2

- Falta de permissão para instalar.
- Não há pacote homologado para o modelo.
- Erro persistente mesmo com o pacote correto.

## Erros comuns

- **Baixar driver de site de terceiros.** Risco de vírus e de pacote errado.
- **Tratar como driver um problema de conexão.** Se a impressora não é detectada, o driver não é o próximo passo.
- **Ignorar a arquitetura.** Um driver x64 não serve para um computador ARM64, e vice-versa.

## Guias relacionados

[KB-01 · Impressora offline](kb-01-impressora-offline.md) · [KB-02 · Documento preso na fila](kb-02-documento-preso-na-fila.md)

**Referência oficial:** [Problemas de conexão e impressão no Windows][impressao]

---

[← Anterior: KB-02](kb-02-documento-preso-na-fila.md) · [↑ Índice](../README.md#indice) · [Próximo: KB-04 →](kb-04-wifi-nao-conecta.md)

[impressao]: https://support.microsoft.com/pt-br/windows/hardware/printer/fix-printer-connection-and-printing-problems-in-windows

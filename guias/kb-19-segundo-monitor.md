# KB-19 · Segundo monitor sem imagem

[← Índice](../README.md#indice) · **Categoria:** Periféricos · **Quem executa:** N1 com o usuário

> **Em uma frase:** separe três coisas: o monitor **está ligado e na entrada certa**? O **cabo/porta** transmite vídeo? O **Windows** está mandando imagem para ele?

---

## Entenda o problema

É como uma TV que não mostra o canal: pode estar desligada, na entrada **HDMI 2** quando o cabo está no **HDMI 1**, com cabo ruim, ou o aparelho conectado pode não estar enviando nada. Cada uma dessas tem um teste rápido.

**Sintoma típico:** a tela externa fica preta ou mostra "sem sinal".

**Causas mais comuns:** entrada errada no monitor, cabo ou adaptador com problema, dock, ou modo de projeção do Windows.

## Pergunte primeiro

- O monitor está conectado direto ao notebook ou por um dock/adaptador?
- Qual tipo de cabo? (HDMI, DisplayPort, USB-C)
- Funcionava antes nessa mesma mesa?
- O monitor mostra alguma mensagem, como "sem sinal"?

## Antes de começar

> [!NOTE]
> **Nem toda porta USB-C transmite vídeo.** O formato do conector é o mesmo, mas a capacidade depende do computador.

---

## Passo a passo

### Passo 1 — Energia e entrada do monitor

**Faça:** confirme que o monitor está ligado e, pelos botões dele, que a **entrada** selecionada é a do cabo usado (HDMI, DisplayPort…).

**Por quê:** é a causa mais comum. Muitos monitores não trocam de entrada sozinhos.

**O que você deve ver:** o menu do monitor aparecendo e a entrada correta selecionada.

### Passo 2 — Encaixes e outra conexão

**Faça:** confira se o cabo está firme nas duas pontas. Se houver outro cabo ou porta compatível, teste — **um item por vez**.

**Por quê:** cabos e adaptadores falham com frequência e são fáceis de testar.

**O que você deve ver:** imagem aparecendo com alguma das trocas — ou não.

### Passo 3 — Modo de projeção

**Faça:** pressione `Win + P` e escolha **Duplicar** (mesma imagem nas duas telas) ou **Estender** (área de trabalho ampliada), conforme a necessidade do usuário. Se preciso, em **Configurações → Sistema → Tela → Vários monitores**, clique em **Detectar**.

**Por quê:** o Windows pode estar configurado para usar **só a tela do notebook**.

**O que você deve ver:** a imagem aparecendo no segundo monitor.

### Passo 4 — Direto × dock

**Faça:** se o equipamento permitir, compare a conexão **direta** no notebook com a conexão **pelo dock**.

**Por quê:** se direto funciona e pelo dock não, o problema está no dock ou no adaptador.

**O que você deve ver:** qual caminho funciona.

---

## Como interpretar o resultado

| Se você observar… | Provavelmente significa… | Próximo passo |
|---|---|---|
| O monitor **não mostra nem o próprio menu** | Energia ou defeito no monitor | Verifique tomada e equipamento |
| Mostra "sem sinal" | O monitor funciona, mas não recebe vídeo | Confira entrada, cabo e modo de projeção |
| Funciona direto, não pelo dock | Problema no dock/adaptador | Registre modelos e encaminhe |
| Funciona com outro cabo | O cabo original falhou | Substitua |
| Porta USB-C sem imagem | A porta pode não suportar vídeo | Confira a especificação do computador |

## Como saber que resolveu

- [ ] Imagem estável no segundo monitor.
- [ ] No modo desejado pelo usuário (duplicar ou estender).

## O que anotar no chamado

- [ ] Modelos de monitor, dock e adaptador
- [ ] Portas e cabos testados
- [ ] Modo de projeção
- [ ] Resultado de cada comparação

## Quando encaminhar ao N2

- Defeito de hardware.
- Limitação de portas ou adaptadores.

Informe modelos e tipo de conexão.

## Erros comuns

- **Reinstalar driver de vídeo** antes de conferir a entrada do monitor.
- **Supor que qualquer USB-C transmite vídeo.**
- **Trocar cabo e dock ao mesmo tempo.**

## Guias relacionados

[KB-18 · Microfone](kb-18-microfone.md)

**Referência oficial:** [Solucionar problemas de monitor externo no Windows][monitor]

---

[← Anterior: KB-18](kb-18-microfone.md) · [↑ Índice](../README.md#indice) · [Próximo: KB-20 →](kb-20-sistema-web.md)

[monitor]: https://support.microsoft.com/en-us/windows/hardware/display-graphics/troubleshoot-external-monitor-connections-in-windows

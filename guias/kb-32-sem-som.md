# KB-32 · Sem som no alto-falante ou fone

[← Índice](../README.md#indice) · **Categoria:** Periféricos · **Quem executa:** N1 com o usuário

> **Em uma frase:** o Windows quase sempre está tocando o som — só que **no lugar errado**. Descubra para qual saída o som está indo antes de mexer em driver.

---

## Entenda o problema

O som do computador é como a **água de uma casa com várias torneiras**: alto-falante do notebook, fone com fio, fone Bluetooth, monitor com HDMI, dock. A água só sai por uma torneira por vez. Se o Windows escolheu a torneira do monitor (que não tem caixa de som) ou a do fone Bluetooth guardado na mochila, o usuário não ouve nada, embora "o som esteja funcionando".

**Sintoma típico:** "não sai som", "não ouço ninguém na reunião", "só funciona no fone" ou "o som sai no monitor".

**Causas mais comuns:** saída errada selecionada, volume no mudo (no Windows, no aplicativo ou no próprio fone), fone Bluetooth conectado automaticamente, monitor HDMI escolhido como saída, cabo no conector errado.

## Pergunte primeiro

- Não sai som de **nada** ou só de **um aplicativo** (Teams, navegador)?
- O que você está usando: alto-falante do notebook, fone com fio, fone Bluetooth?
- Tem um fone Bluetooth pareado por perto?
- Conectou algo recentemente? (monitor, dock, fone)

## Antes de começar

> [!NOTE]
> Comece com o volume **baixo** ao testar um fone. Ao corrigir a saída, o som pode vir de uma vez e alto.

---

## Passo a passo

### Passo 1 — Confira o mudo e o volume

**Faça:** clique no ícone de som perto do relógio. Verifique se não está no mudo e se o volume está acima de zero. Confira também botões de mudo ou volume no próprio fone ou caixa de som.

**Por quê:** é a causa mais comum. Teclas de função do notebook ativam o mudo com facilidade.

**O que você deve ver:** ícone de som sem "X" e volume audível.

### Passo 2 — Escolha a saída correta

**Faça:** no mesmo painel de som, clique na seta ao lado do controle de volume e escolha o dispositivo de saída correto (alto-falantes, fone).

**Por quê:** o Windows troca a saída sozinho quando você conecta um monitor HDMI, um dock ou um fone Bluetooth. A saída "certa" pode não ser a ativa.

**O que você deve ver:** som saindo no dispositivo escolhido.

### Passo 3 — Verifique o volume por aplicativo

**Faça:** em **Configurações → Sistema → Som → Mixer de volume**, veja o volume de cada aplicativo aberto.

**Por quê:** o Windows guarda um volume separado para cada aplicativo. O som geral pode estar alto e o Teams, sozinho, estar no mínimo.

**O que você deve ver:** o aplicativo com volume adequado.

### Passo 4 — Confira a saída dentro do aplicativo

**Faça:** em aplicativos de reunião, confira o alto-falante selecionado nas configurações de dispositivos.

**Por quê:** o Teams e outros aplicativos podem usar uma saída diferente da padrão do Windows.

**O que você deve ver:** o mesmo dispositivo escolhido no Passo 2.

### Passo 5 — Teste o físico

**Faça:** para fones com fio, confira se o conector está totalmente encaixado e na entrada certa (fone, não microfone). Para Bluetooth, desligue e ligue o fone e confira se ele está conectado **a este** computador (e não ao celular).

**Por quê:** conectores mal encaixados e fones conectados a outro aparelho são causas físicas comuns.

**O que você deve ver:** som saindo após o ajuste.

### Passo 6 — Use o solucionador de áudio

**Faça:** em **Configurações → Sistema → Solução de problemas → Outras soluções de problemas**, execute o de **Áudio** (em versões mais novas, ele pode abrir pelo aplicativo **Obter Ajuda**).

**Por quê:** confere serviços de áudio e configurações comuns de forma segura.

**O que você deve ver:** o relatório do solucionador e, se houver, a correção aplicada.

---

## Como interpretar o resultado

| Se você observar… | Significa… | Faça |
|---|---|---|
| Ícone com "X" | Mudo ativo | Passo 1 |
| Som sai no monitor ou em outro fone | Saída errada | Passo 2 |
| Só um aplicativo está sem som | Volume ou saída do aplicativo | Passos 3 e 4 |
| Nenhuma saída aparece na lista | Dispositivo ausente ou driver | Gerenciador de Dispositivos; encaminhe |
| Fone funciona no celular, mas não no PC | Pareamento ou conexão Bluetooth | Passo 5 |

## Como saber que resolveu

- [ ] O usuário ouve um som de teste na saída desejada.
- [ ] O usuário ouve os participantes no aplicativo de reunião, se essa era a queixa.

## O que anotar no chamado

- [ ] Dispositivo de saída usado (tipo e modelo)
- [ ] Saída que estava selecionada antes da correção
- [ ] Se o problema era geral ou de um aplicativo
- [ ] Ação feita e resultado

## Quando encaminhar ao N2

- Nenhum dispositivo de saída aparece no Windows.
- Alerta de driver de áudio no Gerenciador de Dispositivos.
- Defeito físico no alto-falante ou conector.

## Erros comuns

- **Reinstalar o driver** sem olhar a saída selecionada.
- **Esquecer o fone Bluetooth** conectado sozinho.
- **Testar com volume alto** e assustar o usuário com o fone no ouvido.

## Guias relacionados

[KB-18 · Microfone](kb-18-microfone.md) · [KB-21 · Teams](kb-21-teams-reuniao.md) · [KB-19 · Segundo monitor](kb-19-segundo-monitor.md) · [KB-31 · Webcam](kb-31-webcam.md)

**Referências oficiais:** [Central de suporte do Windows][win]

---

[← Anterior: KB-31](kb-31-webcam.md) · [↑ Índice](../README.md#indice)

[win]: https://support.microsoft.com/pt-br/windows

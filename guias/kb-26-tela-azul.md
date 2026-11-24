# KB-26 · Tela azul ou reinício inesperado

[← Índice](../README.md#indice) · **Categoria:** Windows · **Quem executa:** N1 coleta evidências; análise de causa é do N2

> **Em uma frase:** a tela azul é o Windows **parando de propósito** para não estragar nada — seu trabalho no N1 é **anotar o código**, descobrir **o que mudou** e ver se **se repete**.

---

## Entenda o problema

Pense no **disjuntor da sua casa**. Quando algo dá curto, ele desarma de propósito para evitar um incêndio. O desarme não é o problema — é o aviso. A tela azul (chamada de **BSOD**, *Blue Screen of Death*) é o disjuntor do Windows: algo grave aconteceu (geralmente um driver ou peça de hardware) e o sistema prefere reiniciar a arriscar corromper dados.

> [!NOTE]
> Em versões recentes do Windows 11, essa tela pode aparecer **preta** em vez de azul, com a mensagem de que o dispositivo encontrou um problema e precisa reiniciar. O raciocínio é o mesmo.

**Sintoma típico:** tela azul (ou preta) com um código como `IRQL_NOT_LESS_OR_EQUAL` e reinício; ou o computador simplesmente reinicia sozinho.

**Causas mais comuns:** driver novo ou desatualizado, atualização recente, periférico recém-conectado (dock, placa), memória ou disco com defeito, superaquecimento.

## Pergunte primeiro

- Você conseguiu ver ou fotografar a tela? Qual era o **código de parada**?
- **Quando** acontece? (ao ligar, ao conectar algo, em uma tarefa específica, aleatório)
- Quantas vezes já aconteceu?
- Mudou algo recentemente? (atualização, driver, dock, periférico novo)
- O computador está esquentando muito ou com ventoinha alta?

## Antes de começar

> [!CAUTION]
> Se após o reinício aparecer uma tela pedindo **chave de recuperação do BitLocker**, **não tente adivinhar** e não formate. A chave fica guardada pela empresa (por exemplo, na conta corporativa). Siga o procedimento oficial de recuperação.

> [!WARNING]
> Não baixe "atualizadores de driver" de sites aleatórios. Drivers vêm do fabricante do computador ou da ferramenta corporativa.

---

## Passo a passo

### Passo 1 — Registre o código de parada

**Faça:** peça a foto da tela ou o código escrito (ex.: `CRITICAL_PROCESS_DIED`, `PAGE_FAULT_IN_NONPAGED_AREA`). Se a tela tinha um QR code, ele leva à página de ajuda.

**Por quê:** o código é o "laudo" do desarme. Ele aponta a família do problema (memória, driver, disco) e é a primeira coisa que o N2 vai pedir.

**O que você deve ver:** o código anotado no chamado.

### Passo 2 — Veja o histórico no Monitor de Confiabilidade

**Faça:** em `Win + R`, digite `perfmon /rel` e pressione `Enter`. Procure os **X vermelhos** nos dias da falha e clique para ver detalhes.

**Por quê:** é uma linha do tempo de falhas e mudanças. Ela mostra, num gráfico simples, se a tela azul começou **logo depois** de uma atualização ou instalação.

**O que você deve ver:** eventos como "Desligamento inesperado do Windows" e, nos dias anteriores, atualizações ou instalações.

> [!TIP]
> No **Visualizador de Eventos**, o evento **Kernel-Power 41** só diz que o computador **desligou sem avisar**. Ele **não é a causa** — é a consequência. Não conclua nada só por ele.

### Passo 3 — Desconecte o que é novo

**Faça:** se a falha começou após conectar dock, adaptador ou periférico, desconecte e observe.

**Por quê:** cada periférico traz seu driver. Remover o suspeito é o teste "uma coisa por vez" mais barato.

**O que você deve ver:** se as telas azuis param sem o periférico.

### Passo 4 — Confira temperatura e ventilação

**Faça:** verifique se as saídas de ar do notebook estão livres (não usar sobre cama, almofada) e se o ventilador funciona.

**Por quê:** superaquecimento faz o hardware falhar de forma aleatória, o que parece "defeito de software".

**O que você deve ver:** saídas de ar livres e o computador sem calor excessivo.

### Passo 5 — Mantenha o Windows e drivers pelo canal oficial

**Faça:** verifique se há atualizações pendentes no Windows Update ou na ferramenta do fabricante autorizada pela empresa.

**Por quê:** muitos problemas de driver já têm correção publicada.

**O que você deve ver:** sistema e drivers atualizados pelo canal oficial.

---

## Como interpretar o resultado

| Se você observar… | Pode indicar… | Faça |
|---|---|---|
| Começou logo após atualização/driver | Incompatibilidade | Encaminhe com a data e o nome da atualização |
| Só acontece com um periférico conectado | Driver do periférico | Passo 3; encaminhe com o modelo |
| Códigos diferentes a cada vez, aleatório | Hardware (memória, disco) | Encaminhe para diagnóstico de hardware |
| Acontece sob uso pesado e muito calor | Superaquecimento | Passo 4; encaminhe se persistir |
| Uma única ocorrência e nunca mais | Evento isolado | Registre e acompanhe |

## Como saber que resolveu

- [ ] Nenhuma nova falha no Monitor de Confiabilidade durante o período combinado de observação.
- [ ] O usuário repete a tarefa que costumava travar sem reinício.

> [!IMPORTANT]
> Tela azul é intermitente. "Não aconteceu nos últimos 10 minutos" não é validação. Combine um período de observação e registre como **em acompanhamento**.

## O que anotar no chamado

- [ ] Código de parada (foto, se possível)
- [ ] Frequência e quando acontece
- [ ] Mudanças recentes vistas no Monitor de Confiabilidade
- [ ] Periféricos conectados e resultado ao desconectar

## Quando encaminhar ao N2

- Mais de uma ocorrência, sempre — com código e linha do tempo.
- Computador que não inicia ou entra em loop de reparo.
- Pedido de chave do BitLocker.

## Erros comuns

- **Não anotar o código** porque "o computador já voltou".
- **Tratar Kernel-Power 41 como causa.**
- **Formatar** como primeira solução: apaga as evidências e pode não resolver um defeito de hardware.

## Guias relacionados

[KB-25 · Windows Update](kb-25-windows-update.md) · [KB-27 · Computador não liga](kb-27-computador-nao-liga.md) · [KB-09 · Computador lento](kb-09-computador-lento.md)

**Referências oficiais:** [Referência de códigos de parada][bugcheck]

---

[← Anterior: KB-25](kb-25-windows-update.md) · [↑ Índice](../README.md#indice) · [Próximo: KB-27 →](kb-27-computador-nao-liga.md)

[bugcheck]: https://learn.microsoft.com/pt-br/windows-hardware/drivers/debugger/bug-check-code-reference2

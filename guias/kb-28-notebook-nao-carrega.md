# KB-28 · Notebook não carrega ou bateria dura pouco

[← Índice](../README.md#indice) · **Categoria:** Hardware · **Quem executa:** N1 (troca de bateria ou carregador é do N2)

> **Em uma frase:** separe o **caminho da energia** (tomada → carregador → porta) da **saúde da bateria** — o relatório de bateria do Windows mostra a segunda em números.

---

## Entenda o problema

A bateria é como uma **caixa-d'água** e o carregador é o **cano** que a enche. Se o cano está quebrado ou fino demais, a caixa não enche. E, com os anos, a caixa "encolhe": mesmo cheia, guarda menos água do que quando era nova. São dois problemas diferentes, com testes diferentes.

**Sintomas típicos:** "está na tomada, mas não carrega", "conectado, sem carregar" ou "a bateria acaba em uma hora".

**Causas mais comuns:** carregador de potência inferior ao necessário, cabo ou porta danificados, porta USB-C que não aceita carga, tomada sem energia, modo de proteção de bateria ativo (que limita a carga de propósito) ou bateria desgastada.

## Pergunte primeiro

- O carregador é o **original** do notebook?
- A luz do carregador ou do notebook acende?
- O ícone de bateria mostra um **plugue**? Aparece "conectado, sem carregar"?
- É problema de **não carregar** ou de **descarregar rápido**?
- O notebook tem quantos anos (aproximadamente)?

## Antes de começar

> [!CAUTION]
> **Bateria estufada** (carcaça levantando, touchpad alto, tampa que não fecha) é risco de incêndio. Pare o uso, desconecte do carregador, **não pressione** e encaminhe imediatamente.

> [!WARNING]
> Não use carregadores de outros modelos "porque encaixa". Tensão ou potência erradas podem danificar o equipamento.

---

## Passo a passo

### Passo 1 — Teste o caminho da energia

**Faça:** conecte o carregador original em outra tomada (sem filtro de linha, para testar). Verifique se o cabo está inteiro e firme nas duas pontas.

**Por quê:** é o equivalente a conferir se o cano está ligado à rua. Tomada e cabo são as causas mais baratas.

**O que você deve ver:** a luz de carga acesa e o ícone de plugue na bateria.

### Passo 2 — USB-C: use a porta certa

**Faça:** se o notebook carrega por USB-C, confira qual porta tem o símbolo de energia ou é indicada pelo fabricante para carga.

**Por quê:** nem toda porta USB-C aceita energia. Algumas são só para dados ou vídeo.

**O que você deve ver:** carga iniciando na porta correta.

### Passo 3 — Confira o modo de proteção de bateria

**Faça:** verifique no aplicativo do fabricante (ou na configuração de energia autorizada) se há um modo que limita a carga, por exemplo a 80%.

**Por quê:** muitos fabricantes limitam a carga de propósito para prolongar a vida útil da bateria. Parece defeito ("não passa de 80%"), mas é configuração.

**O que você deve ver:** o limite configurado, se houver.

### Passo 4 — Gere o relatório de bateria

**Faça:** no terminal, execute `powercfg /batteryreport`. O comando cria um arquivo `battery-report.html` na pasta atual; abra-o no navegador. ([Como ler](../docs/COMANDOS.md#powercfg-batteryreport--como-está-a-saúde-da-bateria))

**Por quê:** o relatório mostra a **capacidade original** (*Design Capacity*) e a **capacidade atual de carga total** (*Full Charge Capacity*). É a medição do "quanto a caixa-d'água encolheu".

**O que você deve ver:** os dois números. Se a capacidade atual for muito menor que a original, a bateria está desgastada.

### Passo 5 — Verifique o que gasta energia

**Faça:** em **Configurações → Sistema → Energia e bateria**, veja o **uso da bateria por aplicativo**.

**Por quê:** a bateria pode estar boa e um aplicativo estar consumindo energia sem parar em segundo plano.

**O que você deve ver:** aplicativos com consumo anormal. Se houver, veja o [KB-09](kb-09-computador-lento.md).

---

## Como interpretar o resultado

| Se você observar… | Significa… | Faça |
|---|---|---|
| Nenhuma luz em nenhuma tomada | Carregador ou cabo com defeito | Teste outro carregador original (se houver) e encaminhe |
| "Conectado, sem carregar" | Carregador fraco, modo de proteção ou bateria | Passos 2 e 3; depois o relatório |
| Para sempre num valor fixo (ex.: 80%) | Modo de proteção ativo | Passo 3: configuração, não defeito |
| Full Charge muito menor que Design Capacity | Bateria desgastada | Encaminhe para troca com o relatório |
| Bateria boa, mas acaba rápido | Consumo por aplicativos ou brilho | Passo 5 |

## Como saber que resolveu

- [ ] O ícone mostra o notebook **carregando** e a porcentagem subindo.
- [ ] O usuário consegue trabalhar o tempo esperado na bateria (ou a troca foi encaminhada com o relatório).

## O que anotar no chamado

- [ ] Modelo do notebook e do carregador (original ou não)
- [ ] Resultado do teste de tomada e porta
- [ ] Design Capacity × Full Charge Capacity do relatório
- [ ] Mensagem do ícone de bateria

## Quando encaminhar ao N2

- Carregador ou bateria com defeito comprovado.
- Bateria desgastada (com relatório).
- Qualquer sinal de bateria estufada, aquecimento excessivo ou dano físico.

## Erros comuns

- **Usar carregador de outro modelo** "porque encaixa".
- **Tratar o limite de 80% como defeito.**
- **Pedir troca de bateria sem o relatório.**

## Guias relacionados

[KB-27 · Computador não liga](kb-27-computador-nao-liga.md) · [KB-09 · Computador lento](kb-09-computador-lento.md)

**Referências oficiais:** [Opções de linha de comando do powercfg][powercfg]

---

[← Anterior: KB-27](kb-27-computador-nao-liga.md) · [↑ Índice](../README.md#indice) · [Próximo: KB-29 →](kb-29-mfa-autenticador.md)

[powercfg]: https://learn.microsoft.com/pt-br/windows-hardware/design/device-experiences/powercfg-command-line-options

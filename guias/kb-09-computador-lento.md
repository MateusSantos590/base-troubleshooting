# KB-09 · Computador lento

[← Índice](../README.md#indice) · **Categoria:** Windows · **Quem executa:** N1 com o usuário

> **Em uma frase:** "lento" é um sintoma vago. Descubra **o que** está lento (Windows, um aplicativo ou a rede) e **qual recurso** está sobrecarregado **no momento** da lentidão.

---

## Entenda o problema

Pense em uma cozinha de restaurante: o **processador (CPU)** é o cozinheiro, a **memória (RAM)** é a bancada e o **disco** é a despensa. Se o pedido demora, pode ser cozinheiro sobrecarregado, bancada cheia ou despensa difícil de acessar. Também pode ser que a cozinha esteja ótima e o problema seja o entregador (a rede). Você precisa observar a cozinha **durante** o pedido demorado.

**Sintoma típico:** tarefas que antes eram rápidas passam a demorar.

**Causas mais comuns:** programa consumindo muitos recursos, pouco espaço em disco, atualização em andamento ou problema de hardware.

## Pergunte primeiro

- **O que exatamente** está lento? (ligar o computador, abrir um programa, um sistema web…)
- Desde quando? Algo foi instalado ou atualizado?
- É o tempo todo ou em momentos específicos?
- Quanto tempo a tarefa leva hoje e quanto levava antes?

## Antes de começar

> [!WARNING]
> Antes de fechar programas ou reiniciar, **combine com o usuário e garanta que o trabalho está salvo**. Não use "limpadores de registro" nem desative o antivírus para ganhar desempenho.

---

## Passo a passo

### Passo 1 — Delimite onde está a lentidão

**Faça:** descubra se a lentidão acontece no **Windows inteiro**, em **um aplicativo** ou só em algo que depende da **rede** (ex.: um sistema web).

**Por quê:** se só o sistema web está lento, o computador pode estar perfeito e o problema estar na rede ou no servidor.

**O que você deve ver:** o escopo da lentidão definido.

### Passo 2 — Observe os recursos durante o problema

**Faça:** abra o **Gerenciador de Tarefas** (`Ctrl + Shift + Esc`) e observe **CPU**, **Memória** e **Disco** **enquanto** a lentidão acontece. Veja qual programa está no topo.

**Por quê:** o consumo só tem significado se coincidir com o momento da lentidão. Um pico isolado é normal.

**O que você deve ver:** algum recurso perto de 100% de forma constante — ou todos tranquilos.

### Passo 3 — Feche o que for desnecessário (com consentimento)

**Faça:** com o trabalho salvo e o consentimento do usuário, feche programas conhecidos que não estão em uso.

**Por quê:** libera recursos e mostra se algum programa específico era o responsável.

**O que você deve ver:** se o desempenho melhora depois de fechar algo específico.

### Passo 4 — Confira espaço em disco e atualizações

**Faça:** veja o espaço livre (**Configurações → Sistema → Armazenamento**) e se há atualizações pendentes ou em andamento. Combine um reinício, se fizer sentido.

**Por quê:** disco quase cheio e atualizações em segundo plano são causas comuns de lentidão.

**O que você deve ver:** espaço suficiente e nenhuma atualização travada.

---

## Como interpretar o resultado

| Se você observar… | Provavelmente significa… | Próximo passo |
|---|---|---|
| Só o sistema web está lento | Problema de rede ou servidor | Compare em outro computador; veja [KB-20](kb-20-sistema-web.md) |
| Um programa usa muita CPU/memória **durante** a lentidão | Esse programa é forte candidato | Registre nome e versão |
| CPU ou disco alto **por poucos segundos** | Comportamento normal | Não é prova de defeito |
| Disco quase cheio | Falta de espaço | Veja [KB-10](kb-10-pouco-espaco-em-disco.md) |
| Disco sempre em 100% sem motivo aparente | Possível problema de hardware | Encaminhe ao N2 |

## Como saber que resolveu

- [ ] O usuário repete **a mesma tarefa** e o tempo volta ao normal.

> [!TIP]
> Meça antes e depois: "abrir o relatório levava 2 minutos, agora leva 10 segundos". Números tornam a validação objetiva.

## O que anotar no chamado

- [ ] Tarefa repetida e tempo aproximado antes/depois
- [ ] Aplicativo e versão envolvidos
- [ ] Recurso sobrecarregado durante a ocorrência
- [ ] Ações realizadas

## Quando encaminhar ao N2

- Travamentos recorrentes.
- Sinais de disco com defeito (ruídos, erros, 100% constante).
- Recursos sempre saturados sem explicação.

## Erros comuns

- **Concluir pela foto de um instante** do Gerenciador de Tarefas.
- **Instalar "otimizadores"** ou limpadores de registro.
- **Não perguntar o que está lento** e sair mexendo em tudo.

## Guias relacionados

[KB-10 · Pouco espaço em disco](kb-10-pouco-espaco-em-disco.md) · [KB-11 · Aplicativo travado](kb-11-aplicativo-travado.md)

**Referência oficial:** [Dicas para melhorar o desempenho do Windows][desempenho]

---

[← Anterior: KB-08](kb-08-ip-169-254.md) · [↑ Índice](../README.md#indice) · [Próximo: KB-10 →](kb-10-pouco-espaco-em-disco.md)

[desempenho]: https://support.microsoft.com/en-us/windows/experience/performance-optimization/tips-to-improve-pc-performance-in-windows

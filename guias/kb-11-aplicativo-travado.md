# KB-11 · Aplicativo travado

[← Índice](../README.md#indice) · **Categoria:** Aplicativos · **Quem executa:** N1 com o usuário

> **Em uma frase:** antes de fechar à força, descubra se o programa está **travado de verdade**, **ocupado trabalhando** ou **esperando uma resposta** sua numa janela escondida.

---

## Entenda o problema

Um aplicativo que "não responde" é como um atendente que não te olha. Ele pode estar:

1. **Esperando você** — uma janela de confirmação ficou escondida atrás de outra.
2. **Ocupado** — processando um arquivo grande, e vai terminar.
3. **Travado de fato** — e precisa ser fechado.

Fechar à força nos casos 1 e 2 faz perder trabalho sem necessidade.

**Sintoma típico:** a janela deixa de responder ("Não respondendo" no título).

**Causas mais comuns:** operação demorada, janela de diálogo oculta, falha do aplicativo ou de algo de que ele depende.

## Pergunte primeiro

- O que você estava fazendo quando travou?
- Há algum trabalho **não salvo** nesse programa?
- Outros programas estão funcionando normalmente?
- Já aconteceu antes fazendo a mesma coisa?

## Antes de começar

> [!WARNING]
> **Encerrar o processo descarta tudo o que não foi salvo.** Explique isso ao usuário e só prossiga com a concordância dele.

---

## Passo a passo

### Passo 1 — Confirme o escopo e procure janelas ocultas

**Faça:** verifique se só esse aplicativo travou. Use `Alt + Tab` e olhe a barra de tarefas em busca de uma janela de confirmação escondida.

**Por quê:** uma pergunta do tipo "Deseja salvar?" escondida atrás da janela principal bloqueia o programa inteiro.

**O que você deve ver:** uma janela pendente (e aí basta respondê-la) ou nenhuma.

### Passo 2 — Aguarde operações conhecidas

**Faça:** se o usuário iniciou algo pesado (abrir arquivo grande, exportar relatório), aguarde um pouco e observe o uso de recursos no **Gerenciador de Tarefas** (`Ctrl + Shift + Esc`).

**Por quê:** se o programa está usando CPU ou disco, provavelmente está trabalhando, não travado.

**O que você deve ver:** atividade de recursos (está ocupado) ou nenhuma atividade (pode estar travado).

### Passo 3 — Se não recuperar, encerre com consentimento

**Faça:** explique ao usuário a possível perda de alterações não salvas. Com a concordância dele, no Gerenciador de Tarefas, selecione o aplicativo e clique em **Finalizar tarefa**.

**Por quê:** é o último recurso. A transparência evita surpresas e reclamações.

**O que você deve ver:** o aplicativo fechado.

### Passo 4 — Reabra e repita a ação

**Faça:** reabra o aplicativo e peça ao usuário para repetir o que estava fazendo.

**Por quê:** isso mostra se foi um evento isolado ou se o problema se repete — e, nesse caso, você terá o passo a passo para reproduzir.

**O que você deve ver:** a tarefa concluída — ou o travamento se repetindo no mesmo ponto.

---

## Como interpretar o resultado

| Se você observar… | Provavelmente significa… | Próximo passo |
|---|---|---|
| Havia uma janela de confirmação oculta | O programa estava esperando o usuário | Responda; encerrar não era necessário |
| Uso alto de recursos e progresso | Operação demorada em andamento | Aguarde |
| Travou de novo **no mesmo ponto** | Falha reproduzível | Anote a sequência exata e encaminhe |
| Funcionou normalmente ao reabrir | Evento isolado | Registre e monitore |

## Como saber que resolveu

- [ ] O usuário concluiu a tarefa sem novo travamento.

## O que anotar no chamado

- [ ] Aplicativo e versão
- [ ] Tarefa que estava sendo feita
- [ ] Tempo de espera observado
- [ ] Mensagem exibida, se houver
- [ ] Se havia dados não salvos (e se foram perdidos)

## Quando encaminhar ao N2

- O travamento se repete.
- Há risco aos dados.

Reinstalar o aplicativo exige verificar dados locais e seguir procedimento aprovado.

## Erros comuns

- **Finalizar a tarefa sem procurar janelas ocultas.**
- **Não avisar sobre a perda de dados** antes de encerrar.
- **Reinstalar o programa** sem antes conseguir reproduzir a falha.

## Guias relacionados

[KB-09 · Computador lento](kb-09-computador-lento.md) · [KB-12 · Outlook não abre](kb-12-outlook-nao-abre.md)

---

[← Anterior: KB-10](kb-10-pouco-espaco-em-disco.md) · [↑ Índice](../README.md#indice) · [Próximo: KB-12 →](kb-12-outlook-nao-abre.md)

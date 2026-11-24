# Modelo de chamado e passagem ao N2

[← Voltar à base](../README.md) · [Método](METODO.md) · Versão 3.0 · 24/11/2026

> **Em uma frase:** um bom chamado conta a história do problema de forma que **qualquer pessoa** consiga continuar o atendimento sem refazer nenhum teste.

> [!CAUTION]
> Copie os campos para o **sistema autorizado** da empresa. Este repositório é público: **não abra issues com dados de atendimento real.** Identificadores, telas e saídas de comandos ficam no canal interno apropriado.

## Por que registrar bem?

Pense no prontuário de um hospital: o médico do plantão seguinte lê o que foi feito e continua o tratamento, sem repetir exames. Um chamado bem escrito faz o mesmo: evita retrabalho, acelera o N2 e mostra padrões quando o mesmo problema aparece em vários chamados.

## Como usar este modelo

| Momento do atendimento | Seção a preencher |
|---|---|
| Ao receber o pedido | [1. Abertura e triagem](#1-abertura-e-triagem) |
| A cada teste feito | [2. Histórico de diagnóstico](#2-histórico-de-diagnóstico) — uma linha por teste |
| Ao aplicar uma solução | [3. Ação e validação](#3-ação-e-validação) |
| Se precisar de outra equipe | [4. Encaminhamento ao N2](#4-encaminhamento-ao-n2) |
| Para ver um exemplo pronto | [5. Exemplo fictício preenchido](#5-exemplo-fictício-preenchido) |
| Para falar com o usuário | [6. Mensagens curtas ao usuário](#6-mensagens-curtas-ao-usuário) |

> [!TIP]
> **Regra de ouro da escrita:** separe sempre o que você **fez**, o que você **viu** e o que você **acha**. "Reiniciei o roteador (fiz), a internet voltou (vi), provavelmente era o roteador (acho — hipótese, não causa confirmada)."

## 1. Abertura e triagem

~~~text
Título: [recurso] — [sintoma observável]
Solicitante / ativo: identificador mínimo permitido internamente
Data/hora e fuso:
Canal e autorização de acesso remoto:
Tarefa que o usuário precisa concluir:
Mensagem de erro exata, sem dados sensíveis:
Quando começou? Houve mudança recente?
Escopo: um aplicativo / um dispositivo / várias pessoas / serviço geral
Impacto no trabalho:
Urgência e justificativa:
Alternativa temporária disponível:
Categoria / prioridade / SLA: conforme regras da organização
Guia consultado e versão/commit:
~~~

## 2. Histórico de diagnóstico

Uma linha por teste; mantenha a ordem. Evite registrar somente comandos sem explicar o resultado.

| Data/hora | Hipótese | Verificação executada | Resultado observado | Interpretação / próximo passo |
|---|---|---|---|---|
| Preencher | O que pode explicar o sintoma? | Ação específica e autorizada | O que foi visto, sem suposição | O teste sustenta ou enfraquece a hipótese? |

## 3. Ação e validação

~~~text
Ação aplicada:
Autorização necessária e impacto combinado:
Configuração original / restauração prevista:
Resultado imediatamente após a ação:
Tarefa original repetida pelo usuário:
Resultado da repetição:
Confirmação do usuário e horário:
Limitações ou pendências restantes:
Status: resolvido / em acompanhamento / aguardando usuário / encaminhado
Próxima atualização: responsável e prazo real acordado
~~~

## 4. Encaminhamento ao N2

~~~text
Resumo em uma frase:
Impacto e escopo:
Início do incidente e última alteração conhecida:
Ambiente e versões relevantes:
Erro / identificador técnico permitido:
Testes executados e respectivos resultados:
Hipóteses ainda abertas:
Ações executadas e configurações alteradas:
Alternativa temporária oferecida:
Por que excede o escopo/permissão do N1:
Equipe de destino e ação solicitada:
Local interno das evidências:
Usuário informado? Próxima atualização combinada:
~~~

Encaminhar não significa abandonar o usuário: mantenha o responsável e o próximo contato registrados, conforme o processo da equipe. Não prometa prazo de solução que o N2 não confirmou.

## 5. Exemplo fictício preenchido

**Cenário** (baseado no [KB-13](../guias/kb-13-outlook-nao-envia-recebe.md))**:** o usuário de laboratório não consegue enviar mensagens pelo Outlook clássico. O teste abaixo é simulado para demonstrar escrita, não uma execução comprovada do projeto.

| Etapa | Registro do exemplo |
|---|---|
| Sintoma | Mensagem de teste permanece na Caixa de Saída |
| Impacto | Uma conta de laboratório; envio pelo navegador disponível |
| Hipótese inicial | Falha local de cliente ou sessão |
| Teste 1 | Navegação normal; sem erro geral de rede observado |
| Teste 2 | Webmail envia e recebe mensagem de teste com destinatário autorizado |
| Interpretação | Priorizar investigação do cliente; não há evidência suficiente para atribuir causa a suplemento |
| Próximo passo | Conferir estado offline, erro de sincronização e versão do cliente |
| Se não resolver | Encaminhar erro e comparação cliente/webmail ao N2, sem corpo do e-mail ou credenciais |
| Status do exemplo | Diagnóstico em andamento; não registrar como resolvido |

## 6. Mensagens curtas ao usuário

**Início:** “Vou confirmar o erro e testar uma hipótese por vez. Antes de qualquer reinício, combino com você para salvarmos o trabalho.”

**Encaminhamento:** “A falha continua após os testes registrados. Encaminhei para a equipe responsável com essas informações. O próximo contato está previsto para o horário combinado no chamado.”

**Encerramento:** “Repetimos a tarefa e ela funcionou no teste. Registrei o procedimento. Se a falha voltar, informe este chamado e o horário da nova ocorrência.”

Para mais modelos e para situações difíceis (usuário irritado, pedido fora da política), veja [Comunicação com o usuário](COMUNICACAO.md).

Use somente a mensagem compatível com o que realmente aconteceu. Ajuste o prazo ao compromisso registrado; não copie a frase de encerramento sem validar a tarefa.

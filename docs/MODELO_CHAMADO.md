# Modelo de chamado e passagem ao N2

[← Voltar à base](../README.md) · Versão 1.1 · 10/11/2026

Copie os campos para o sistema autorizado. **Este repositório é público: não abra issues com dados de atendimento real.** Identificadores, telas e saídas de comandos devem ficar no canal interno apropriado.

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

**Cenário:** o usuário de laboratório não consegue enviar mensagens pelo Outlook clássico. O teste abaixo é simulado para demonstrar escrita, não uma execução comprovada do projeto.

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

Use somente a mensagem compatível com o que realmente aconteceu. Ajuste o prazo ao compromisso registrado; não copie a frase de encerramento sem validar a tarefa.

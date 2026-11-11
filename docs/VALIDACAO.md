# Plano de validação em laboratório

[← Voltar à base](../README.md) · Versão documental 1.1 · 10/11/2026

Este documento transforma os guias em exercícios verificáveis. **Nenhum cenário abaixo foi executado nesta entrega.** Resultado esperado não é resultado observado.

## Ambiente e preparação

Use computador próprio ou laboratório autorizado, contas fictícias e arquivos descartáveis. Registre edição/build do Windows, versão dos aplicativos e modelos de periféricos. VPN corporativa, Active Directory/Entra e serviços de e-mail exigem ambiente autorizado; não simule bloqueios repetidos em contas de produção.

Antes de alterar algo, registre a configuração original, confirme como restaurá-la e salve o trabalho. Se não houver equipamento ou permissão, marque **Não executado — recurso indisponível**, sem atribuir aprovação ao guia.

## Critérios de resultado

| Status | Quando usar |
|---|---|
| Não executado | Ainda não houve teste; é o estado de todos os cenários desta versão |
| Aprovado no ambiente registrado | Sintoma reproduzido, teste interpretado, correção aplicada e tarefa final validada |
| Reprovado | Um passo ou critério falhou; documentar o resultado e revisar o guia |
| Bloqueado | Execução começou, mas foi interrompida por uma dependência identificada |

Aprovar um caso não valida outras versões, modelos ou redes. Uma leitura do texto é revisão documental, não teste funcional.

## Roteiro dos 20 cenários

Todos os casos iniciam com status **Não executado**. As situações abaixo são propostas; não execute mudanças em infraestrutura compartilhada para reproduzi-las.

| Guia | Pré-condição / situação de laboratório | Evidência e critério de aprovação |
|---|---|---|
| [KB-01](../README.md#kb-01) | Impressora de teste indisponível ou destino incorreto | Identificar o destino e recuperar página de teste e documento simples |
| [KB-02](../README.md#kb-02) | Fila de teste com trabalho pausado ou com falha | Diferenciar pausa de documento com erro e imprimir sem afetar outra fila |
| [KB-03](../README.md#kb-03) | Impressora de laboratório com pacote oficial disponível | Registrar modelo/arquitetura, instalar pacote compatível e imprimir |
| [KB-04](../README.md#kb-04) | Wi-Fi de laboratório com sinal/credencial conhecidos | Distinguir associação de navegação e conectar com a credencial correta |
| [KB-05](../README.md#kb-05) | Dispositivo associado à rede com falha de acesso conhecida | Delimitar recurso afetado e comprovar tarefa interna/externa necessária |
| [KB-06](../README.md#kb-06) | Cabo desconectado em computador próprio | Identificar ausência de enlace, reconectar e validar tarefa de rede |
| [KB-07](../README.md#kb-07) | Nome de teste existente e nome inexistente | Comparar consulta válida, inexistente e eventual timeout sem trocar DNS corporativo |
| [KB-08](../README.md#kb-08) | Rede virtual isolada própria sem resposta DHCP | Identificar interface/APIPA e obter concessão após restaurar o DHCP do laboratório |
| [KB-09](../README.md#kb-09) | Tarefa repetível com consumo observável de recursos | Registrar antes/depois da mesma tarefa e sustentar a hipótese com observações |
| [KB-10](../README.md#kb-10) | Volume de laboratório com arquivo descartável | Registrar espaço, remover somente dado autorizado e repetir salvamento |
| [KB-11](../README.md#kb-11) | Aplicativo de teste sem dados importantes | Identificar diálogo/processamento/travamento e validar a tarefa após recuperação |
| [KB-12](../README.md#kb-12) | Outlook clássico instalado e conta de teste | Comparar abertura normal e segura; não declarar suplemento como causa sem isolar |
| [KB-13](../README.md#kb-13) | Caixa de teste e destinatário autorizado | Comparar aplicativo/webmail e comprovar envio e recebimento |
| [KB-14](../README.md#kb-14) | VPN de laboratório autorizada e credenciais de teste | Diferenciar internet, autenticação e túnel; comprovar recurso acessível |
| [KB-15](../README.md#kb-15) | Túnel ativo com recurso de teste documentado | Diferenciar DNS, transporte e permissão sem inventar rotas |
| [KB-16](../README.md#kb-16) | Diretório de laboratório e conta fictícia | Executar fluxo autorizado de desbloqueio e investigar recorrência sem enfraquecer política |
| [KB-17](../README.md#kb-17) | Conta fictícia com recuperação configurada | Concluir recuperação oficial e validar login sem coletar a senha |
| [KB-18](../README.md#kb-18) | Microfone próprio e aplicativo de teste | Comparar medidor do Windows e chamada, com entrada/permissão corretas |
| [KB-19](../README.md#kb-19) | Monitor, cabo e porta compatíveis | Comparar entrada/cabo/projeção e validar imagem estável |
| [KB-20](../README.md#kb-20) | Aplicação de teste com cenários de sessão e erro conhecidos | Diferenciar falha de rede, autenticação, autorização e servidor; concluir tarefa |

## Registro de execução — copiar por cenário

~~~text
ID da execução: LAB-AAAA-MM-DD-01
Guia e versão/commit testado:
Responsável e data/hora/fuso:
Status: Não executado / Aprovado no ambiente registrado / Reprovado / Bloqueado
Ambiente: sistema/build, aplicativo/versão e equipamento
Pré-condição e autorização:
Configuração original e forma de restauração:
Sintoma reproduzido:
Hipótese:
Passo executado → resultado observado:
Interpretação do resultado:
Ação aplicada:
Tarefa original repetida e resultado:
Restauração efetuada e conferida:
Evidência fictícia ou anonimizada:
Divergência encontrada no guia:
Próxima alteração necessária:
~~~

## Revisão documental desta versão

O índice, as 20 identificações de guia e as referências entre os arquivos devem ser conferidos na prévia do GitHub. Essa verificação avalia a documentação; não comprova que os procedimentos funcionem em uma máquina real.

Registre novas execuções sem substituir observações por expectativas. Se houver erro no guia, descreva o comportamento antes de ajustar o texto. Remova segredos, endereços internos e identificadores pessoais antes de compartilhar qualquer registro.

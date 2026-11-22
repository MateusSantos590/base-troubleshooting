# Plano de validação em laboratório

[← Voltar à base](../README.md) · [Método](METODO.md) · Versão documental 2.0 · 22/11/2026

> **Em uma frase:** este plano transforma cada guia em um experimento — você provoca o problema num ambiente seguro, segue o guia e anota o que **realmente** aconteceu.

> [!IMPORTANT]
> **Nenhum cenário abaixo foi executado nesta entrega.** Resultado esperado não é resultado observado.

## Por que validar?

Um guia escrito é uma **receita que ninguém cozinhou ainda**. Pode estar certa, mas só se sabe depois de testar. Validar em laboratório mostra se os passos funcionam, se a ordem faz sentido e se algo está faltando — antes que um usuário real dependa disso.

## Como usar este plano, em 5 passos

1. **Escolha um cenário** na tabela [Roteiro dos 20 cenários](#roteiro-dos-20-cenários).
2. **Prepare o ambiente** conforme a seção abaixo e anote como voltar ao estado original.
3. **Reproduza o sintoma** descrito na pré-condição.
4. **Siga o guia** passo a passo, anotando o que você viu em cada etapa.
5. **Preencha o [registro de execução](#registro-de-execução--copiar-por-cenário)** e defina o status conforme os [critérios](#critérios-de-resultado).

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
| [KB-01](../guias/kb-01-impressora-offline.md) | Impressora de teste indisponível ou destino incorreto | Identificar o destino e recuperar página de teste e documento simples |
| [KB-02](../guias/kb-02-documento-preso-na-fila.md) | Fila de teste com trabalho pausado ou com falha | Diferenciar pausa de documento com erro e imprimir sem afetar outra fila |
| [KB-03](../guias/kb-03-driver-de-impressora.md) | Impressora de laboratório com pacote oficial disponível | Registrar modelo/arquitetura, instalar pacote compatível e imprimir |
| [KB-04](../guias/kb-04-wifi-nao-conecta.md) | Wi-Fi de laboratório com sinal/credencial conhecidos | Distinguir associação de navegação e conectar com a credencial correta |
| [KB-05](../guias/kb-05-wifi-sem-internet.md) | Dispositivo associado à rede com falha de acesso conhecida | Delimitar recurso afetado e comprovar tarefa interna/externa necessária |
| [KB-06](../guias/kb-06-rede-cabeada.md) | Cabo desconectado em computador próprio | Identificar ausência de enlace, reconectar e validar tarefa de rede |
| [KB-07](../guias/kb-07-falha-dns.md) | Nome de teste existente e nome inexistente | Comparar consulta válida, inexistente e eventual timeout sem trocar DNS corporativo |
| [KB-08](../guias/kb-08-ip-169-254.md) | Rede virtual isolada própria sem resposta DHCP | Identificar interface/APIPA e obter concessão após restaurar o DHCP do laboratório |
| [KB-09](../guias/kb-09-computador-lento.md) | Tarefa repetível com consumo observável de recursos | Registrar antes/depois da mesma tarefa e sustentar a hipótese com observações |
| [KB-10](../guias/kb-10-pouco-espaco-em-disco.md) | Volume de laboratório com arquivo descartável | Registrar espaço, remover somente dado autorizado e repetir salvamento |
| [KB-11](../guias/kb-11-aplicativo-travado.md) | Aplicativo de teste sem dados importantes | Identificar diálogo/processamento/travamento e validar a tarefa após recuperação |
| [KB-12](../guias/kb-12-outlook-nao-abre.md) | Outlook clássico instalado e conta de teste | Comparar abertura normal e segura; não declarar suplemento como causa sem isolar |
| [KB-13](../guias/kb-13-outlook-nao-envia-recebe.md) | Caixa de teste e destinatário autorizado | Comparar aplicativo/webmail e comprovar envio e recebimento |
| [KB-14](../guias/kb-14-vpn-nao-conecta.md) | VPN de laboratório autorizada e credenciais de teste | Diferenciar internet, autenticação e túnel; comprovar recurso acessível |
| [KB-15](../guias/kb-15-vpn-conecta-sistema-nao-abre.md) | Túnel ativo com recurso de teste documentado | Diferenciar DNS, transporte e permissão sem inventar rotas |
| [KB-16](../guias/kb-16-conta-bloqueada.md) | Diretório de laboratório e conta fictícia | Executar fluxo autorizado de desbloqueio e investigar recorrência sem enfraquecer política |
| [KB-17](../guias/kb-17-senha-esquecida-ou-expirada.md) | Conta fictícia com recuperação configurada | Concluir recuperação oficial e validar login sem coletar a senha |
| [KB-18](../guias/kb-18-microfone.md) | Microfone próprio e aplicativo de teste | Comparar medidor do Windows e chamada, com entrada/permissão corretas |
| [KB-19](../guias/kb-19-segundo-monitor.md) | Monitor, cabo e porta compatíveis | Comparar entrada/cabo/projeção e validar imagem estável |
| [KB-20](../guias/kb-20-sistema-web.md) | Aplicação de teste com cenários de sessão e erro conhecidos | Diferenciar falha de rede, autenticação, autorização e servidor; concluir tarefa |

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

Os links internos e as âncoras entre os arquivos são conferidos automaticamente pelo script [`scripts/verificar_links.py`](../scripts/verificar_links.py), executado a cada alteração no GitHub. Essa verificação avalia a **documentação**; não comprova que os procedimentos funcionem em uma máquina real.

Registre novas execuções sem substituir observações por expectativas. Se houver erro no guia, descreva o comportamento antes de ajustar o texto. Remova segredos, endereços internos e identificadores pessoais antes de compartilhar qualquer registro.

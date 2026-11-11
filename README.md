# Base de conhecimento de Suporte de TI

**20 guias de troubleshooting para Help Desk e Service Desk N1.**

Portfólio de estudo de **Mateus Santos Telles**, estudante de Análise e Desenvolvimento de Sistemas. Demonstra raciocínio de diagnóstico, documentação e comunicação com usuários.

**Natureza:** cenários didáticos, não chamados reais. **Revisão documental:** 10/11/2026. **Teste em laboratório:** não realizado nesta versão. Os procedimentos devem ser adaptados à versão dos produtos e às permissões da empresa.

## Como usar

Entenda a tarefa afetada, delimite o impacto, teste uma hipótese por vez, registre o resultado e valide a tarefa original com o usuário. Se não resolver, encaminhe com evidências; hipótese não é causa confirmada.

**Ambiente de referência:** Windows 11, Microsoft 365 e rede de pequeno escritório. O modo seguro citado se aplica ao Outlook clássico, não ao novo Outlook. Avalie o ciclo de suporte antes de usar Windows 10; ele não é o ambiente padrão desta base.

Acesso remoto exige ciência do usuário e ferramenta autorizada. Combine reinícios e encerramentos de aplicativos. Não solicite senhas ou códigos de MFA; não desative proteções para testar. Evidências de chamados ficam no canal interno autorizado, nunca neste repositório público.

## Índice

| ID | Guia | Categoria |
|---|---|---|
| KB-01 | [Impressora offline](#kb-01) | Impressão |
| KB-02 | [Documento preso na fila](#kb-02) | Impressão |
| KB-03 | [Driver de impressora ausente](#kb-03) | Impressão |
| KB-04 | [Wi-Fi não conecta](#kb-04) | Redes |
| KB-05 | [Wi-Fi conectado sem internet](#kb-05) | Redes |
| KB-06 | [Rede cabeada sem conexão](#kb-06) | Redes |
| KB-07 | [Falha de resolução DNS](#kb-07) | Redes |
| KB-08 | [IPv4 169.254.x.x](#kb-08) | DHCP |
| KB-09 | [Computador lento](#kb-09) | Windows |
| KB-10 | [Pouco espaço em disco](#kb-10) | Windows |
| KB-11 | [Aplicativo travado](#kb-11) | Aplicativos |
| KB-12 | [Outlook clássico não abre](#kb-12) | Microsoft 365 |
| KB-13 | [Outlook não envia ou recebe](#kb-13) | Microsoft 365 |
| KB-14 | [VPN não conecta](#kb-14) | Acesso remoto |
| KB-15 | [VPN conecta, sistema não abre](#kb-15) | Acesso remoto |
| KB-16 | [Conta bloqueada](#kb-16) | Identidade |
| KB-17 | [Senha esquecida ou expirada](#kb-17) | Identidade |
| KB-18 | [Microfone não funciona](#kb-18) | Periféricos |
| KB-19 | [Segundo monitor sem imagem](#kb-19) | Periféricos |
| KB-20 | [Sistema web não abre](#kb-20) | Sistemas |

## Triagem e prioridade

Pergunte: qual tarefa falhou, qual mensagem aparece, quando começou, o que mudou, quantas pessoas foram afetadas e há alternativa de trabalho? Use a matriz de impacto e urgência e os prazos de SLA da organização; não atribua prioridade somente pela insistência de quem abriu o chamado.

<a id="kb-01"></a>
## KB-01 — Impressora offline

**Sintoma:** a impressão não sai e a fila mostra o equipamento indisponível.

**Causas possíveis:** impressora desligada, conexão interrompida ou destino incorreto.

**Diagnóstico e solução:**
1. Confirme a impressora selecionada e os avisos do painel.
2. Verifique energia, cabo ou Wi-Fi; em rede, confira o endereço esperado com o responsável.
3. Confira se a fila local está pausada e retome somente a fila correta, conforme permissão.
4. Restabelecida a conexão, envie uma página de teste.

**Validação:** página impressa no destino correto e repetição da tarefa pelo usuário.

**Encaminhar ao N2:** equipamento inacessível, servidor com falha ou vários usuários afetados. Registre modelo, conexão e mensagem. [Referência de impressão][impressao].

<a id="kb-02"></a>
## KB-02 — Documento preso na fila

**Sintoma:** um trabalho não termina e os seguintes ficam aguardando.

**Causas possíveis:** documento com erro ou serviço de impressão indisponível.

**Diagnóstico e solução:**
1. Compare outro documento para delimitar a falha.
2. Com o usuário, cancele apenas o trabalho problemático e tente uma impressão simples.
3. Se persistir, registre o estado da fila. Reinício do serviço exige autorização e avaliação do impacto.

**Validação:** documento simples e original impressos.

**Encaminhar ao N2:** fila compartilhada afetada ou recorrência. Não apague trabalhos de outras pessoas. [Referência de impressão][impressao].

<a id="kb-03"></a>
## KB-03 — Driver de impressora ausente

**Sintoma:** o equipamento é detectado, mas a instalação falha.

**Causas possíveis:** pacote incompatível, permissão insuficiente ou conexão instável.

**Diagnóstico e solução:**
1. Identifique modelo exato, versão do Windows e arquitetura do computador.
2. Confira conexão e mensagem antes de alterar a instalação.
3. Use pacote homologado pela TI ou do fabricante para o modelo correto.
4. Solicite instalação pela equipe autorizada se houver exigência administrativa.

**Validação:** instalação sem erro e página de teste.

**Encaminhar ao N2:** falta de permissão, pacote não homologado ou erro persistente. Evite sites de drivers de terceiros. [Referência de impressão][impressao].

<a id="kb-04"></a>
## KB-04 — Wi-Fi não conecta

**Sintoma:** a rede aparece, mas o computador não se associa.

**Causas possíveis:** rádio desligado, credencial incorreta, sinal fraco ou política de autenticação.

**Diagnóstico e solução:**
1. Confira modo avião, Wi-Fi ativo e nome correto da rede.
2. Compare outro dispositivo autorizado no mesmo local.
3. Aproxime o computador do ponto de acesso para comparar o sinal.
4. O usuário digita a própria credencial. Remover perfil corporativo exige orientação da TI.

**Validação:** associação estável e acesso ao recurso necessário.

**Encaminhar ao N2:** erro de certificado/autenticação corporativa ou falha coletiva. Registre horário e erro, sem senha. [Referência Wi-Fi][wifi].

<a id="kb-05"></a>
## KB-05 — Wi-Fi conectado sem internet

**Sintoma:** há associação à rede, porém a navegação falha.

**Causas possíveis:** rota, DNS, portal de acesso ou indisponibilidade externa.

**Diagnóstico e solução:**
1. Separe falha de um site, do computador e de toda a rede.
2. Execute <code>ipconfig</code> e confira endereço e gateway da interface utilizada.
3. Se existir portal esperado, conclua o acesso autorizado.
4. Compare um recurso interno e um externo conhecidos. Ping sem resposta isoladamente não prova indisponibilidade: ICMP pode estar bloqueado.

**Validação:** recursos necessários acessíveis, não apenas ícone de rede alterado.

**Encaminhar ao N2:** falha geral ou gateway/DNS indisponível. Redefinir a rede pode derrubar o suporte remoto e exigir reconfiguração da VPN. [Wi-Fi][wifi] e [ipconfig][ipconfig].

<a id="kb-06"></a>
## KB-06 — Rede cabeada sem conexão

**Sintoma:** o Windows informa cabo desconectado ou não obtém acesso.

**Causas possíveis:** cabo, porta, adaptador ou configuração de rede.

**Diagnóstico e solução:**
1. Confira encaixes e indicadores de enlace, quando existentes.
2. Teste outro cabo aprovado e porta autorizada, mudando um item por vez.
3. Verifique se o adaptador aparece no Windows e registre seu estado.
4. Com enlace ativo, confira endereços por <code>ipconfig</code>; avance para KB-07 ou KB-08 conforme o resultado.

**Validação:** enlace e tarefa de rede funcionando.

**Encaminhar ao N2:** adaptador ausente, porta bloqueada ou infraestrutura com falha. Não altere VLAN, IP estático ou switch por tentativa. [Comando de consulta][ipconfig].

<a id="kb-07"></a>
## KB-07 — Falha de resolução DNS

**Sintoma:** o nome de um recurso não resolve, embora exista conectividade.

**Causas possíveis:** DNS incorreto, cache desatualizado ou necessidade de VPN/sufixo corporativo.

**Diagnóstico e solução:**
1. Confirme o endereço correto e se exige VPN.
2. Execute <code>nslookup nome-do-servico</code>, substituindo o exemplo por um nome autorizado.
3. Compare resposta e DNS consultado com o esperado pela TI.
4. Com evidência de cache desatualizado, use <code>ipconfig /flushdns</code> com a permissão necessária e teste novamente.

**Validação:** resolução correta e abertura normal do serviço; acesso por IP não substitui validação de HTTPS/certificado.

**Encaminhar ao N2:** registro ausente ou falha do DNS corporativo. Não substitua DNS corporativo por público sem autorização. [DNS][dns] e [ipconfig][ipconfig].

<a id="kb-08"></a>
## KB-08 — IPv4 169.254.x.x

**Sintoma:** interface configurada para DHCP apresenta endereço automático 169.254.x.x e não alcança a rede esperada.

**Causas possíveis:** resposta DHCP não recebida, falha física ou autenticação pendente.

**Diagnóstico e solução:**
1. Identifique a interface utilizada, distinguindo adaptadores virtuais.
2. Confira o enlace e se a rede deveria fornecer endereço por DHCP.
3. Consulte <code>ipconfig /all</code> para confirmar DHCP habilitado.
4. Com autorização e alternativa de reconexão do suporte, tente <code>ipconfig /renew</code>; registre eventual erro.

**Validação:** endereço esperado, gateway e acesso ao recurso.

**Encaminhar ao N2:** recorrência ou vários dispositivos afetados. Não escolha IP fixo por tentativa. [Referência][ipconfig].

<a id="kb-09"></a>
## KB-09 — Computador lento

**Sintoma:** tarefas antes rápidas passam a demorar.

**Causas possíveis:** consumo de recursos, pouco espaço, atualização em andamento ou hardware.

**Diagnóstico e solução:**
1. Delimite se ocorre no Windows, em um aplicativo ou apenas na rede.
2. Observe CPU, memória e disco no Gerenciador de Tarefas durante o problema.
3. Feche aplicativos conhecidos com consentimento e dados salvos.
4. Confira armazenamento e atualizações pendentes; combine reinício quando adequado.

**Validação:** repita a mesma tarefa e compare o comportamento.

**Encaminhar ao N2:** travamentos recorrentes, sinais de disco defeituoso ou recursos sempre saturados. Não use limpadores de registro nem desative a proteção. [Referência][desempenho].

<a id="kb-10"></a>
## KB-10 — Pouco espaço em disco

**Sintoma:** salvar, instalar ou atualizar falha por falta de espaço.

**Causas possíveis:** arquivos locais volumosos ou temporários acumulados.

**Diagnóstico e solução:**
1. Identifique a unidade e categorias nas configurações de armazenamento.
2. Revise os arquivos com o usuário; Downloads e Lixeira podem conter material necessário.
3. Use limpeza nativa apenas nas categorias aprovadas e compreendidas.
4. Mova dados somente para destino autorizado e confirme a cópia.

**Validação:** espaço recuperado e tarefa original concluída.

**Encaminhar ao N2:** crescimento inexplicado ou dados sujeitos a retenção. Não apague pastas do sistema ou arquivos pessoais sem autorização. [Referência][desempenho].

<a id="kb-11"></a>
## KB-11 — Aplicativo travado

**Sintoma:** a janela deixa de responder.

**Causas possíveis:** operação demorada, diálogo oculto, aplicativo ou dependência com falha.

**Diagnóstico e solução:**
1. Confira se apenas esse aplicativo falhou e procure confirmação oculta.
2. Aguarde uma operação conhecida terminar e observe os recursos usados.
3. Se não recuperar, explique a possível perda de alterações não salvas antes de encerrar o processo.
4. Reabra e repita a ação que provocou a falha.

**Validação:** tarefa concluída sem travamento.

**Encaminhar ao N2:** recorrência ou risco aos dados. Registre versão, horário e ação; reinstalação exige verificar dados locais e procedimento aprovado.

<a id="kb-12"></a>
## KB-12 — Outlook clássico não abre

**Sintoma:** permanece em processamento ou fecha ao iniciar.

**Causas possíveis:** diálogo pendente, suplemento ou perfil com falha.

**Diagnóstico e solução:**
1. Confirme que é o Outlook clássico e procure diálogos ocultos.
2. Feche o aplicativo após considerar alterações não salvas.
3. Pelo Executar do Windows, inicie <code>outlook.exe /safe</code>.
4. Se abrir, registre a diferença. Teste suplementos apenas com procedimento autorizado, um por vez.

**Validação:** abertura normal e teste de envio/recebimento.

**Encaminhar ao N2:** falha em modo seguro ou erro de perfil/dados. Não apague PST/OST nem remova perfil sem plano aprovado. Este procedimento não se aplica ao novo Outlook. [Referência][outlook].

<a id="kb-13"></a>
## KB-13 — Outlook não envia ou recebe

**Sintoma:** mensagens ficam na saída ou novas mensagens não chegam.

**Causas possíveis:** conectividade, modo offline, autenticação, limite de caixa ou serviço indisponível.

**Diagnóstico e solução:**
1. Confira rede e mensagem de erro.
2. No Outlook clássico, confira se Trabalhar Offline está ativado indevidamente.
3. Compare com o webmail aprovado para separar falha de cliente e de conta/serviço.
4. Verifique avisos de armazenamento, autenticação e anexo. Evite reenvios repetidos.

**Validação:** envio e recebimento com destinatário de teste autorizado, sem conteúdo sensível.

**Encaminhar ao N2:** webmail também falha, bloqueio ou várias contas afetadas. Registre código e horário sem conteúdo privado dos e-mails.

<a id="kb-14"></a>
## KB-14 — VPN não conecta

**Sintoma:** o cliente recusa ou não conclui a conexão.

**Causas possíveis:** internet, autenticação, perfil incorreto ou requisito do dispositivo.

**Diagnóstico e solução:**
1. Teste internet antes da VPN e registre cliente, versão e erro.
2. Confira perfil autorizado, data/hora e conexão escolhida.
3. O usuário conclui autenticação e MFA; não peça nem registre códigos.
4. Confira avisos de indisponibilidade e tente reconectar uma vez, quando adequado.

**Validação:** túnel estabelecido e recurso corporativo acessível.

**Encaminhar ao N2:** erro de certificado, conformidade, conta ou recorrência. Não desative verificações de certificado ou proteção do equipamento.

<a id="kb-15"></a>
## KB-15 — VPN conecta, sistema não abre

**Sintoma:** túnel conectado, porém um recurso interno continua inacessível.

**Causas possíveis:** DNS, rota, permissão ou aplicação indisponível.

**Diagnóstico e solução:**
1. Confirme a URL e se a falha afeta um ou todos os recursos internos.
2. Confira resolução conforme KB-07.
3. Compare com outro recurso autorizado e com o relato de outro usuário, sem compartilhar credenciais.
4. Diferencie acesso negado, nome não encontrado e tempo esgotado.

**Validação:** abertura do sistema e execução da tarefa original.

**Encaminhar ao N2:** informe VPN, horário, erro e resultados. Não crie rotas ou altere regras de acesso por tentativa.

<a id="kb-16"></a>
## KB-16 — Conta bloqueada

**Sintoma:** o login informa explicitamente bloqueio.

**Causas possíveis:** tentativas incorretas ou credenciais antigas reutilizadas em outro dispositivo.

**Diagnóstico e solução:**
1. Interrompa tentativas e confirme a mensagem exata.
2. Valide a identidade pelo procedimento da organização.
3. Oriente desbloqueio oficial/autoatendimento, se habilitado; caso contrário, encaminhe à equipe autorizada.
4. Se houver novo bloqueio, levante aplicativos e dispositivos com credenciais antigas sem pedir a senha.

**Validação:** login legítimo sem novo bloqueio durante o teste.

**Encaminhar ao N2:** recorrência ou suspeita de acesso indevido. Não desbloqueie repetidamente sem investigar. [Referência de identidade][identidade].

<a id="kb-17"></a>
## KB-17 — Senha esquecida ou expirada

**Sintoma:** usuário esqueceu a senha ou recebeu aviso de expiração.

**Causas possíveis:** esquecimento, política de validade ou confusão entre PIN, conta e senha.

**Diagnóstico e solução:**
1. Identifique conta e método de entrada, sem solicitar o segredo.
2. Oriente o portal oficial de recuperação da empresa, se disponível.
3. Redefinição administrativa somente após validação de identidade e pela equipe autorizada.
4. Combine atualização das credenciais nos aplicativos conforme política interna.

**Validação:** usuário autentica pelo próprio método e acessa o recurso necessário.

**Encaminhar ao N2:** recuperação indisponível ou dados desatualizados. Nunca receba senha temporária ou código de recuperação em chamado público. [Referência de identidade][identidade].

<a id="kb-18"></a>
## KB-18 — Microfone não funciona

**Sintoma:** participantes da reunião não ouvem o usuário.

**Causas possíveis:** mudo físico, entrada incorreta, permissão ou periférico com falha.

**Diagnóstico e solução:**
1. Confira mudo físico e no aplicativo.
2. Selecione a entrada correta no Windows e na ferramenta de reunião.
3. Observe o medidor de entrada com uma frase de teste; confira permissões do aplicativo/navegador.
4. Compare outro aplicativo ou periférico autorizado para isolar o problema.

**Validação:** chamada de teste com áudio compreensível.

**Encaminhar ao N2:** dispositivo ausente, bloqueio por política ou falha física. Não grave conversas reais como evidência.

<a id="kb-19"></a>
## KB-19 — Segundo monitor sem imagem

**Sintoma:** a tela externa permanece sem sinal.

**Causas possíveis:** entrada incorreta, cabo/adaptador, dock ou modo de projeção.

**Diagnóstico e solução:**
1. Confira energia e entrada selecionada no monitor.
2. Confira encaixes e teste outra conexão compatível, se disponível.
3. Use <code>Win + P</code> e escolha Duplicar ou Estender conforme a necessidade.
4. Compare conexão direta e dock, se o equipamento permitir.

**Validação:** imagem estável e modo desejado.

**Encaminhar ao N2:** hardware ou limitação de portas/adaptadores. Informe modelos e tipo de conexão. [Referência][monitor].

<a id="kb-20"></a>
## KB-20 — Sistema web não abre

**Sintoma:** navegador exibe erro, página em branco ou acesso negado.

**Causas possíveis:** URL incorreta, sessão, rede/VPN, permissão ou servidor indisponível.

**Diagnóstico e solução:**
1. Confirme endereço pelo canal oficial, horário e erro.
2. Separe rede, autenticação, permissão e erro do servidor.
3. Compare navegador aprovado. Janela privativa pode ajudar a isolar sessão/extensões, mas não elimina requisitos de SSO.
4. Remova dados apenas do site afetado quando indicado e autorizado, explicando o encerramento da sessão; não limpe todas as senhas.

**Validação:** login e tarefa original concluídos.

**Encaminhar ao N2:** erro geral, acesso negado ou servidor com falha. Não contorne alerta de certificado nem conceda acesso sem aprovação.

## Modelo de registro de chamado

Preencha no sistema interno aprovado; não publique dados reais aqui.

~~~text
Título: recurso + sintoma objetivo
Data/hora e fuso:
Usuário/ativo: identificador permitido pela organização
Impacto: pessoas e tarefas afetadas
Urgência: justificativa de negócio
Categoria e prioridade: conforme matriz interna
Sintoma e mensagem exata:
Início e mudanças recentes:
Hipóteses investigadas:
Testes e resultados, em ordem:
Ação executada e autorização necessária:
Validação: tarefa repetida e resultado
Status: resolvido / aguardando usuário / encaminhado
Próxima equipe e motivo:
Evidências: canal autorizado, com dados minimizados
~~~

## Exemplo didático de encerramento

**Sintoma:** impressora não imprime após instalação do sistema. **Hipótese:** driver incompatível. **Teste proposto:** conferir modelo, sistema e página de teste. **Ação proposta:** instalar pacote oficial compatível com autorização. **Critério de encerramento:** página de teste e documento do usuário impressos. Exemplo de escrita; não é um resultado medido deste projeto.

## Comandos de consulta

| Comando | Objetivo | Limite |
|---|---|---|
| <code>ipconfig</code> | Consultar endereços | Identificar interface em uso |
| <code>ipconfig /all</code> | Consultar DHCP e DNS | Saída pode conter dados internos |
| <code>nslookup nome-do-servico</code> | Consultar resolução DNS | Não prova disponibilidade da aplicação |
| <code>ping destino-autorizado</code> | Verificar resposta ICMP | Ausência de resposta não prova host desligado |

Renovar DHCP e limpar cache alteram estado e aparecem nos guias com contexto. Não existe comando universal para resolver incidentes.

## Referências oficiais

Consultadas em 10/11/2026. Os guias são sínteses autorais e procedimentos propostos, não documentação oficial da Microsoft. Valide as versões e as instruções locais antes de aplicar.

- [Impressão no Windows][impressao]
- [Conectividade Wi-Fi][wifi]
- [Comando ipconfig][ipconfig]
- [Diagnóstico do cliente DNS][dns]
- [Outlook clássico sem responder][outlook]
- [Desempenho do Windows][desempenho]
- [Redefinição e desbloqueio por autoatendimento][identidade]
- [Monitor externo][monitor]

## Limites e manutenção

Versão inicial com 20 guias revisados quanto à estrutura e à navegação. Não foram executados testes em dispositivos, impressoras, VPN ou contas corporativas. Antes de adotar em produção, valide em laboratório autorizado e registre ambiente, resultado e data. Atualizações devem distinguir hipótese, teste realizado e conclusão confirmada.

**Autor:** [Mateus Santos Telles](https://www.linkedin.com/in/mateusantostelles/).

[impressao]: https://support.microsoft.com/pt-br/windows/hardware/printer/fix-printer-connection-and-printing-problems-in-windows
[wifi]: https://support.microsoft.com/pt-br/windows/experience/connectivity-networking/fix-wi-fi-connection-issues-in-windows
[ipconfig]: https://learn.microsoft.com/pt-br/windows-server/administration/windows-commands/ipconfig
[dns]: https://learn.microsoft.com/pt-br/windows-server/networking/dns/troubleshoot/troubleshoot-dns-client
[outlook]: https://support.microsoft.com/pt-br/outlook/classic-outlook-not-responding-stuck-at-processing-stopped-working-or-freezes
[desempenho]: https://support.microsoft.com/en-us/windows/experience/performance-optimization/tips-to-improve-pc-performance-in-windows
[identidade]: https://learn.microsoft.com/en-us/entra/identity/authentication/concept-sspr-howitworks
[monitor]: https://support.microsoft.com/en-us/windows/hardware/display-graphics/troubleshoot-external-monitor-connections-in-windows

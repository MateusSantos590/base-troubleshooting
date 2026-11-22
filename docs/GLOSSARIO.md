# Glossário — termos explicados em linguagem simples

[← Voltar ao início](../README.md) · [Método](METODO.md) · [Comandos](COMANDOS.md)

Toda palavra técnica usada nos guias está aqui, explicada como você explicaria para alguém da família. Se algum termo faltar, [sugira a inclusão](../CONTRIBUTING.md).

> [!TIP]
> Não tente decorar a lista. Volte aqui quando um guia usar uma palavra que você não conhece — é assim que o vocabulário gruda.

**Atalhos:** [Atendimento](#atendimento) · [Rede e internet](#rede-e-internet) · [Windows e hardware](#windows-e-hardware) · [Contas e segurança](#contas-e-segurança) · [E-mail e sistemas](#e-mail-e-sistemas)

---

## Atendimento

| Termo | O que significa | Analogia do dia a dia |
|---|---|---|
| **Chamado (ticket)** | Registro oficial de um pedido de ajuda: quem pediu, o que aconteceu, o que foi feito. | O prontuário de um paciente. |
| **N1 (nível 1)** | Primeiro atendimento: recebe o pedido, faz testes simples e resolve o que é comum. | O clínico geral. |
| **N2 (nível 2)** | Equipe com mais conhecimento ou permissão, que recebe o que o N1 não pode resolver. | O especialista para quem o clínico encaminha. |
| **Help Desk / Service Desk** | Setor que atende os pedidos de TI das pessoas. | A recepção e o pronto-atendimento da TI. |
| **Triagem** | Primeiras perguntas para entender gravidade e alcance do problema. | A enfermeira que mede pressão antes da consulta. |
| **Impacto** | Quantas pessoas ou tarefas o problema afeta. | Um paciente com febre × um surto na cidade. |
| **Urgência** | Quanto tempo dá para esperar antes de virar prejuízo. | Uma dor leve × um corte que não para de sangrar. |
| **Prioridade** | Combinação de impacto e urgência, definida pela regra da empresa. | A ordem da fila do pronto-socorro. |
| **SLA** | Prazo combinado para responder ou resolver um chamado. | O "entrega em até 3 dias úteis" de uma loja. |
| **Hipótese** | Uma explicação *possível* para o problema, que ainda precisa ser testada. | "Acho que a pilha do controle acabou." |
| **Evidência** | Algo observado que apoia ou enfraquece uma hipótese. | Trocar a pilha e o controle voltar a funcionar. |
| **Causa confirmada** | Hipótese que os testes comprovaram. Sem teste, continua sendo hipótese. | — |
| **Contorno (workaround)** | Solução temporária que deixa a pessoa trabalhar, sem resolver a causa. | Usar o banheiro do vizinho enquanto o encanador não chega. |
| **Escopo** | O "tamanho" do problema: um app, um computador, várias pessoas ou um serviço inteiro. | Uma lâmpada queimada × a rua inteira sem luz. |
| **Escalonar / encaminhar** | Passar o chamado para outra equipe, com tudo o que já foi testado. | O encaminhamento médico com exames anexados. |

## Rede e internet

| Termo | O que significa | Analogia do dia a dia |
|---|---|---|
| **Rede** | Computadores e equipamentos ligados entre si para trocar dados. | As ruas de um bairro. |
| **Wi-Fi** | Rede sem fio, por ondas de rádio. | Uma conversa em voz alta pela sala. |
| **Rede cabeada (Ethernet)** | Rede por cabo, geralmente mais estável que o Wi-Fi. | Um telefone com fio. |
| **SSID** | O nome da rede Wi-Fi que aparece na lista. | O nome escrito na fachada do prédio. |
| **Associação** | O momento em que o computador "entra" na rede Wi-Fi. Estar associado ainda não garante internet. | Passar pela portaria do prédio — ainda falta chegar ao apartamento. |
| **Ponto de acesso (AP) / roteador** | Aparelho que emite o Wi-Fi e encaminha o tráfego. | A torre do rádio. |
| **Enlace (link)** | A conexão *física* entre o cabo e o equipamento. Geralmente indicada por uma luz acesa na porta. | O telefone dar sinal de linha. |
| **Adaptador (placa) de rede** | Peça do computador que se conecta à rede, com ou sem fio. | A antena do celular. |
| **Endereço IP** | O "endereço" do computador na rede, como `192.168.0.25`. | O número da casa na rua. |
| **Gateway (padrão)** | O equipamento que leva o tráfego da sua rede para outras redes, como a internet. | A saída do condomínio para a avenida. |
| **DHCP** | Serviço que entrega um endereço IP automaticamente a quem entra na rede. | A recepção do hotel que entrega a chave do quarto. |
| **Concessão (lease)** | O endereço "emprestado" pelo DHCP por um tempo. | A diária do hotel. |
| **169.254.x.x (APIPA)** | Endereço que o Windows inventa sozinho quando **não recebeu resposta do DHCP**. É um sinal de alerta. | Sem chave do hotel, você escreve um número de quarto num papel — ninguém vai te achar. |
| **IP estático (fixo)** | Endereço digitado manualmente em vez de recebido do DHCP. Só a TI deve definir. | Pintar seu próprio número na porta. |
| **DNS** | Serviço que traduz nomes (`intranet.empresa`) em endereços IP. | A lista de contatos do celular: você toca no nome, ele disca o número. |
| **Resolver um nome** | Descobrir o IP de um nome via DNS. | Procurar o número de alguém na agenda. |
| **Cache DNS** | Respostas de DNS guardadas temporariamente no computador para ganhar tempo. | Lembrar de cabeça um número que você discou ontem — mesmo que ele tenha mudado. |
| **Timeout (tempo esgotado)** | Pedido enviado sem resposta dentro do prazo. | Ligar e ninguém atender. |
| **Ping / ICMP** | Teste que pergunta "você está aí?" a outro equipamento. Muitas redes bloqueiam essa pergunta, então **ficar sem resposta não prova que o destino está desligado**. | Bater na porta: silêncio pode ser casa vazia *ou* morador que não atende estranhos. |
| **Portal cativo** | Página de login que algumas redes exigem antes de liberar a internet (hotéis, aeroportos). | O "aceite os termos" do Wi-Fi do shopping. |
| **Proxy** | Intermediário por onde a navegação da empresa passa. | Uma secretária que faz as ligações por você. |
| **Rota** | O caminho que os dados seguem até o destino. | O trajeto do GPS. |
| **VLAN** | Divisão lógica de uma rede física em várias redes separadas. Configurada só pela equipe de rede. | Andares de um prédio com acessos diferentes. |
| **Switch** | Equipamento com várias portas que interliga os cabos de rede. | Uma régua de tomadas, só que para dados. |
| **Firewall** | Filtro que permite ou bloqueia tráfego conforme regras. | O segurança na entrada do evento. |
| **VPN** | Conexão protegida que coloca o computador "dentro" da rede da empresa, mesmo de casa. | Um túnel particular da sua casa até o escritório. |
| **Túnel** | O canal protegido criado pela VPN. | O próprio túnel da analogia acima. |
| **URL** | O endereço completo de uma página, como `https://sistema.empresa/login`. | O endereço completo com rua, número e apartamento. |
| **HTTPS / certificado** | Conexão criptografada. O certificado prova que o site é quem diz ser. **Nunca ignore alertas de certificado.** | O documento com foto que o porteiro confere. |

## Windows e hardware

| Termo | O que significa | Analogia do dia a dia |
|---|---|---|
| **Driver** | Programa que ensina o Windows a usar um equipamento específico. | O manual de instruções em um idioma que o Windows entende. |
| **Fila de impressão** | Lista de documentos esperando a vez de imprimir. | A fila do caixa. |
| **Spooler de impressão** | Serviço do Windows que organiza a fila. Reiniciá-lo afeta todas as impressões do computador. | O fiscal da fila do caixa. |
| **Página de teste** | Folha que o próprio Windows manda imprimir para checar a impressora sem depender de nenhum arquivo. | Testar o fogão acendendo a boca sem panela. |
| **Arquitetura (x64 / ARM64)** | Tipo de processador do computador. O driver precisa ser da mesma arquitetura. | Tomada de 2 ou 3 pinos: o plugue tem que encaixar. |
| **Edição / build do Windows** | A versão exata do Windows (ex.: Windows 11 Pro, build 26100). Vê-se em **Configurações → Sistema → Sobre**. | O ano e modelo de um carro. |
| **Gerenciador de Tarefas** | Ferramenta que mostra o que está usando o computador (`Ctrl + Shift + Esc`). | O painel de instrumentos do carro. |
| **CPU (processador)** | O "cérebro" que faz as contas. | O cozinheiro. |
| **Memória (RAM)** | Espaço de trabalho temporário, apagado ao desligar. | A bancada da cozinha. |
| **Disco / armazenamento** | Onde arquivos ficam guardados de forma permanente. | A despensa. |
| **Processo** | Um programa em execução. | Um prato sendo preparado. |
| **Encerrar processo** | Fechar à força um programa. **O que não foi salvo se perde.** | Desligar o fogão no meio da receita. |
| **Dock / adaptador** | Acessório que adiciona portas (vídeo, rede, USB) ao notebook. | Um "T" de tomada. |
| **Modo de projeção** | Como o Windows usa o segundo monitor: duplicar, estender ou só uma tela (`Win + P`). | Espelhar ou estender a tela do celular na TV. |
| **USB-C** | Formato de conector. **Nem toda porta USB-C transmite vídeo.** | Tomadas iguais que nem sempre têm a mesma voltagem. |

## Contas e segurança

| Termo | O que significa | Analogia do dia a dia |
|---|---|---|
| **Credencial** | Aquilo que prova quem você é: usuário, senha, PIN, código. | A chave de casa. |
| **MFA (autenticação multifator)** | Login que exige algo além da senha, como código no celular. **O suporte nunca deve pedir esse código.** | Senha do cartão + o próprio cartão. |
| **PIN do Windows** | Código usado só para desbloquear *aquele* computador. **Não é a senha da conta.** | A senha do cadeado da bicicleta não abre a porta de casa. |
| **Conta bloqueada** | Conta travada temporariamente, normalmente após várias senhas erradas. | O caixa eletrônico que segura o cartão. |
| **Conta desabilitada** | Conta desligada de propósito pela empresa. Situação diferente de "bloqueada". | Um crachá cancelado pelo RH. |
| **Active Directory (AD) / Microsoft Entra ID** | Sistemas onde a empresa guarda contas e permissões. Cada um pode ter um fluxo próprio de desbloqueio. | O cadastro de moradores do condomínio. |
| **Autoatendimento de senha (SSPR)** | Portal onde a própria pessoa redefine ou desbloqueia a senha, se a empresa habilitou. | O "esqueci minha senha" do banco. |
| **Validação de identidade** | Procedimento da empresa para confirmar que quem pede é mesmo o dono da conta. | Pedir documento antes de entregar uma encomenda. |
| **SSO (login único)** | Entrar uma vez e acessar vários sistemas. | Uma pulseira de evento que libera várias áreas. |
| **Autenticação × autorização** | Autenticação = provar **quem** você é. Autorização = o que você **pode** fazer. | Entrar no prédio (autenticação) × ter a chave de uma sala específica (autorização). |
| **Conformidade do dispositivo** | Regras que o computador precisa cumprir (antivírus ativo, sistema atualizado) para acessar recursos. | O detector de metais antes de entrar no avião. |

## E-mail e sistemas

| Termo | O que significa | Analogia do dia a dia |
|---|---|---|
| **Outlook clássico × novo Outlook** | Dois aplicativos diferentes. O clássico tem a guia **Arquivo** no canto superior esquerdo; o novo, não. Vários procedimentos (como o modo seguro) valem só para o clássico. | Dois modelos de carro da mesma marca: o manual de um não serve para o outro. |
| **Webmail** | O e-mail aberto pelo navegador (ex.: Outlook na web). Serve para comparar com o aplicativo. | Ver o extrato no site do banco em vez do app. |
| **Modo seguro do Outlook** | Abre o Outlook clássico sem suplementos e personalizações (`outlook.exe /safe`). | Ligar o carro sem os acessórios instalados para ver se o problema é neles. |
| **Suplemento (add-in)** | Extensão que adiciona funções ao Outlook ou ao navegador. | Um acessório instalado no carro. |
| **Perfil do Outlook** | Conjunto de configurações da conta dentro do Outlook. | As preferências salvas no banco do motorista. |
| **Arquivos OST / PST** | Arquivos onde o Outlook guarda e-mails no computador. **Nunca apague sem plano aprovado.** | A caixa de cartas guardada no armário. |
| **Caixa de Saída** | Pasta onde mensagens esperam para ser enviadas. | A pilha de cartas esperando o carteiro. |
| **Trabalhar Offline** | Modo do Outlook clássico que pausa o envio e o recebimento. | Colocar o celular em modo avião. |
| **Código HTTP** | Número que o site devolve dizendo o que aconteceu. `401` = falta login; `403` = sem permissão; `404` = página não encontrada; `5xx` = falha do lado do servidor. | As placas "Identifique-se", "Proibida a entrada", "Endereço não existe" e "Fechado para manutenção". |
| **Sessão / cookies** | Dados que o navegador guarda para lembrar que você está logado. | A pulseira do hotel que prova que você é hóspede. |
| **Janela privativa (anônima)** | Janela do navegador sem cookies e, em geral, sem extensões. Ajuda a isolar problemas de sessão. | Entrar na loja sem o cartão de fidelidade. |
| **Identificador de correlação** | Código que alguns sistemas mostram no erro para a equipe localizar o registro técnico. | O número do protocolo de atendimento. |

---

[← Voltar ao início](../README.md)

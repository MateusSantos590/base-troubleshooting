# Base de conhecimento de Suporte de TI

**32 guias de troubleshooting para Help Desk e Service Desk N1 — explicados passo a passo, com o porquê de cada ação — mais dicionário de erros, dicas de bolso, comunicação com o usuário e casos práticos com gabarito.**

[![Verificação de links](https://github.com/MateusSantos590/base-troubleshooting/actions/workflows/verificar-links.yml/badge.svg)](https://github.com/MateusSantos590/base-troubleshooting/actions/workflows/verificar-links.yml)
![Versão](https://img.shields.io/badge/vers%C3%A3o-3.0-blue)
![Guias](https://img.shields.io/badge/guias-32-orange)
![Idioma](https://img.shields.io/badge/idioma-portugu%C3%AAs-green)

[Comece aqui](#comece-aqui) · [Qual guia usar?](#qual-guia-usar) · [Índice dos guias](#indice) · [Material de apoio](#material-de-apoio) · [Método](docs/METODO.md) · [Mensagens de erro](docs/MENSAGENS_DE_ERRO.md) · [Glossário](docs/GLOSSARIO.md)

---

## O que é isto?

Uma coleção de guias para resolver os problemas mais comuns de um escritório: impressora que não imprime, Wi-Fi que não conecta, Outlook e Teams que não abrem, OneDrive que não sincroniza, senha esquecida, MFA no celular novo, VPN que falha, tela azul, e-mail suspeito, e outros.

Cada guia responde a quatro perguntas:

1. **O que está acontecendo?** — o problema explicado com uma analogia do dia a dia.
2. **O que eu faço?** — passos curtos, um de cada vez.
3. **Por que estou fazendo isso?** — o motivo de cada passo, para você aprender a raciocinar e não só seguir receita.
4. **Como sei que deu certo?** — o que você deve ver e quando parar ou encaminhar.

## Para quem é?

| Você é… | Como esta base ajuda |
|---|---|
| **Iniciante** em suporte ou estudante de TI | Aprende o raciocínio de diagnóstico com linguagem simples e um [glossário](docs/GLOSSARIO.md) completo |
| **Técnico N1** | Tem um roteiro rápido e seguro para consultar durante o atendimento |
| **Recrutador ou gestor** | Vê como o autor pensa: diagnóstico, segurança, documentação e comunicação |

> [!IMPORTANT]
> **Natureza do material:** cenários didáticos, **não** chamados reais. Os procedimentos **não foram testados em laboratório** nesta versão (veja o [plano de validação](docs/VALIDACAO.md)). Adapte à versão dos produtos e às permissões da sua empresa.

---

<a id="comece-aqui"></a>
## Comece aqui — trilha em 4 passos

Se é sua primeira vez, siga nesta ordem. Os quatro primeiros passos levam cerca de 30 minutos.

| Passo | Leia | Por quê |
|---|---|---|
| 1 | [**O método**](docs/METODO.md) | É o raciocínio usado em **todos** os guias. Entendendo-o, você resolve até problemas que não estão aqui |
| 2 | [**Um guia simples**: KB-01 · Impressora offline](guias/kb-01-impressora-offline.md) | Para se acostumar com o formato |
| 3 | [**Um guia em camadas**: KB-05 · Conectado sem internet](guias/kb-05-wifi-sem-internet.md) | Mostra como seguir o problema de uma etapa para outra |
| 4 | [**O modelo de chamado**](docs/MODELO_CHAMADO.md) | Para registrar e encaminhar o que você descobriu |
| 5 | [**Casos práticos**](docs/CASOS_PRATICOS.md) | Para treinar o raciocínio em chamados sem etiqueta, com gabarito |

Encontrou uma palavra estranha? Consulte o [**glossário**](docs/GLOSSARIO.md). Apareceu um código de erro? Procure no [**dicionário de mensagens de erro**](docs/MENSAGENS_DE_ERRO.md). Vai usar um comando? Veja os [**comandos explicados**](docs/COMANDOS.md).

---

<a id="qual-guia-usar"></a>
## Qual guia usar?

Comece pelo que o usuário **relata** e siga as setas.

```mermaid
flowchart TD
    S(["O que o usuário relata?"]) --> I["Não imprime"]
    S --> R["Problema de rede ou internet"]
    S --> C["Não consigo entrar na conta"]
    S --> M["Microsoft 365"]
    S --> H["Computador ou periférico"]
    S --> SEG["E-mail ou aprovação suspeita"]

    I --> I1{"A impressora aparece<br/>instalada?"}
    I1 -- "Não / instalação falha" --> KB03["KB-03<br/>Driver"]
    I1 -- "Sim, mas offline" --> KB01["KB-01<br/>Offline"]
    I1 -- "Sim, mas a fila trava" --> KB02["KB-02<br/>Fila"]

    R --> R1{"Está conectado<br/>à rede?"}
    R1 -- "Não, Wi-Fi" --> KB04["KB-04<br/>Wi-Fi não conecta"]
    R1 -- "Não, cabo" --> KB06["KB-06<br/>Rede cabeada"]
    R1 -- "Sim, mas não navega" --> KB05["KB-05<br/>Sem internet"]
    R1 -- "Usa VPN" --> R2{"A VPN conecta?"}
    R2 -- "Não" --> KB14["KB-14<br/>VPN não conecta"]
    R2 -- "Sim, mas o sistema não abre" --> KB15["KB-15<br/>VPN + sistema"]

    C --> C1{"A mensagem diz<br/>bloqueada?"}
    C1 -- "Sim" --> KB16["KB-16<br/>Conta bloqueada"]
    C1 -- "Não, esqueci / expirou" --> KB17["KB-17<br/>Senha"]
    C1 -- "Problema no código / celular" --> KB29["KB-29<br/>MFA"]

    M --> M1{"Qual aplicativo?"}
    M1 -- "Outlook não abre" --> KB12["KB-12<br/>Outlook"]
    M1 -- "E-mail não sai/chega" --> KB13["KB-13<br/>Envio"]
    M1 -- "Teams" --> KB21["KB-21<br/>Teams"]
    M1 -- "OneDrive" --> KB22["KB-22<br/>OneDrive"]
    M1 -- "Arquivo bloqueado/perdido" --> KB24["KB-24<br/>Arquivo"]

    H --> H1{"O que acontece?"}
    H1 -- "Não liga" --> KB27["KB-27<br/>Não liga"]
    H1 -- "Tela azul / reinicia" --> KB26["KB-26<br/>Tela azul"]
    H1 -- "Não carrega" --> KB28["KB-28<br/>Bateria"]
    H1 -- "Áudio ou vídeo" --> AV["KB-18 microfone<br/>KB-31 webcam<br/>KB-32 som"]

    SEG --> KB30["KB-30<br/>Phishing"]
```

> [!CAUTION]
> Se o usuário **clicou num link suspeito, digitou a senha em página estranha ou recebeu aprovação de MFA que não pediu**, pule a fila: vá direto ao [KB-30](guias/kb-30-email-suspeito.md) ou ao [KB-29](guias/kb-29-mfa-autenticador.md) e acione a segurança.

**Sintomas que não estão no fluxograma:**

| O usuário diz… | Comece por |
|---|---|
| "O computador está lento" | [KB-09](guias/kb-09-computador-lento.md) |
| "Não consigo salvar, disco cheio" | [KB-10](guias/kb-10-pouco-espaco-em-disco.md) |
| "O programa travou" | [KB-11](guias/kb-11-aplicativo-travado.md) |
| "O Outlook não abre" | [KB-12](guias/kb-12-outlook-nao-abre.md) |
| "O e-mail não sai / não chega" | [KB-13](guias/kb-13-outlook-nao-envia-recebe.md) |
| "Ninguém me ouve na reunião" | [KB-18](guias/kb-18-microfone.md) |
| "O segundo monitor está preto" | [KB-19](guias/kb-19-segundo-monitor.md) |
| "O sistema / site não abre" | [KB-20](guias/kb-20-sistema-web.md) |
| "O nome do sistema não é encontrado" | [KB-07](guias/kb-07-falha-dns.md) |
| "Meu IP começa com 169.254" | [KB-08](guias/kb-08-ip-169-254.md) |
| "A unidade S: está com X vermelho" | [KB-23](guias/kb-23-pasta-de-rede.md) |
| "A atualização do Windows sempre falha" | [KB-25](guias/kb-25-windows-update.md) |
| "A câmera está preta" | [KB-31](guias/kb-31-webcam.md) |
| "Não sai som" | [KB-32](guias/kb-32-sem-som.md) |
| "Apareceu um código de erro" | [Dicionário de mensagens de erro](docs/MENSAGENS_DE_ERRO.md) |

---

<a id="indice"></a>
## Índice dos guias

| ID | Guia | Categoria | Em uma frase |
|---|---|---|---|
| <a id="kb-01"></a>KB-01 | [Impressora offline](guias/kb-01-impressora-offline.md) | Impressão | O computador não "conversa" com a impressora |
| <a id="kb-02"></a>KB-02 | [Documento preso na fila](guias/kb-02-documento-preso-na-fila.md) | Impressão | Um documento trava e segura os outros |
| <a id="kb-03"></a>KB-03 | [Driver de impressora ausente](guias/kb-03-driver-de-impressora.md) | Impressão | O Windows vê a impressora, mas não sabe usá-la |
| <a id="kb-04"></a>KB-04 | [Wi-Fi não conecta](guias/kb-04-wifi-nao-conecta.md) | Redes | A rede aparece, mas o computador não entra |
| <a id="kb-05"></a>KB-05 | [Wi-Fi conectado sem internet](guias/kb-05-wifi-sem-internet.md) | Redes | Entrou na rede, mas os dados não chegam ao destino |
| <a id="kb-06"></a>KB-06 | [Rede cabeada sem conexão](guias/kb-06-rede-cabeada.md) | Redes | Sem "sinal de linha" no cabo |
| <a id="kb-07"></a>KB-07 | [Falha de resolução DNS](guias/kb-07-falha-dns.md) | Redes | O nome do sistema não vira endereço |
| <a id="kb-08"></a>KB-08 | [IPv4 169.254.x.x](guias/kb-08-ip-169-254.md) | DHCP | O computador inventou um endereço que não funciona |
| <a id="kb-09"></a>KB-09 | [Computador lento](guias/kb-09-computador-lento.md) | Windows | Descobrir o que está lento e por quê |
| <a id="kb-10"></a>KB-10 | [Pouco espaço em disco](guias/kb-10-pouco-espaco-em-disco.md) | Windows | Liberar espaço sem apagar o que importa |
| <a id="kb-11"></a>KB-11 | [Aplicativo travado](guias/kb-11-aplicativo-travado.md) | Aplicativos | Travado, ocupado ou esperando resposta? |
| <a id="kb-12"></a>KB-12 | [Outlook clássico não abre](guias/kb-12-outlook-nao-abre.md) | Microsoft 365 | Modo seguro separa suplementos do núcleo |
| <a id="kb-13"></a>KB-13 | [Outlook não envia ou recebe](guias/kb-13-outlook-nao-envia-recebe.md) | Microsoft 365 | Compare com o webmail |
| <a id="kb-14"></a>KB-14 | [VPN não conecta](guias/kb-14-vpn-nao-conecta.md) | Acesso remoto | Internet → autenticação → túnel, nessa ordem |
| <a id="kb-15"></a>KB-15 | [VPN conecta, sistema não abre](guias/kb-15-vpn-conecta-sistema-nao-abre.md) | Acesso remoto | Nome, caminho ou permissão? |
| <a id="kb-16"></a>KB-16 | [Conta bloqueada](guias/kb-16-conta-bloqueada.md) | Identidade | Desbloquear e descobrir por que bloqueou |
| <a id="kb-17"></a>KB-17 | [Senha esquecida ou expirada](guias/kb-17-senha-esquecida-ou-expirada.md) | Identidade | Caminho oficial; o suporte nunca vê a senha |
| <a id="kb-18"></a>KB-18 | [Microfone não funciona](guias/kb-18-microfone.md) | Periféricos | Dispositivo → Windows → aplicativo |
| <a id="kb-19"></a>KB-19 | [Segundo monitor sem imagem](guias/kb-19-segundo-monitor.md) | Periféricos | Entrada, cabo ou modo de projeção? |
| <a id="kb-20"></a>KB-20 | [Sistema web não abre](guias/kb-20-sistema-web.md) | Sistemas | O código de erro aponta a camada |
| <a id="kb-21"></a>KB-21 | [Teams não abre ou não entra na reunião](guias/kb-21-teams-reuniao.md) | Microsoft 365 | Teste a web antes de mexer no aplicativo |
| <a id="kb-22"></a>KB-22 | [OneDrive não sincroniza](guias/kb-22-onedrive-sincronizacao.md) | Microsoft 365 | Leia o ícone antes de mexer |
| <a id="kb-23"></a>KB-23 | [Pasta de rede não abre](guias/kb-23-pasta-de-rede.md) | Redes | Achar, chegar e ter permissão |
| <a id="kb-24"></a>KB-24 | [Arquivo do Office bloqueado ou perdido](guias/kb-24-arquivo-office-bloqueado.md) | Microsoft 365 | Aberto em outro lugar, protegido ou com versão anterior |
| <a id="kb-25"></a>KB-25 | [Windows Update falha](guias/kb-25-windows-update.md) | Windows | Espaço, reinício real ou regra da empresa |
| <a id="kb-26"></a>KB-26 | [Tela azul ou reinício inesperado](guias/kb-26-tela-azul.md) | Windows | Anote o código e descubra o que mudou |
| <a id="kb-27"></a>KB-27 | [Computador não liga](guias/kb-27-computador-nao-liga.md) | Hardware | Sem energia, sem imagem ou não inicia? |
| <a id="kb-28"></a>KB-28 | [Notebook não carrega](guias/kb-28-notebook-nao-carrega.md) | Hardware | Caminho da energia × saúde da bateria |
| <a id="kb-29"></a>KB-29 | [MFA: celular novo ou código](guias/kb-29-mfa-autenticador.md) | Identidade | O suporte nunca segura a chave |
| <a id="kb-30"></a>KB-30 | [E-mail suspeito (phishing)](guias/kb-30-email-suspeito.md) | Segurança | Não interagir, reportar e agir rápido |
| <a id="kb-31"></a>KB-31 | [Webcam não funciona](guias/kb-31-webcam.md) | Periféricos | Tampa, privacidade e aplicativo |
| <a id="kb-32"></a>KB-32 | [Sem som](guias/kb-32-sem-som.md) | Periféricos | O som está saindo pelo lugar errado |

### Guias por categoria

| Categoria | Guias |
|---|---|
| **Impressão** | [KB-01](guias/kb-01-impressora-offline.md) · [KB-02](guias/kb-02-documento-preso-na-fila.md) · [KB-03](guias/kb-03-driver-de-impressora.md) |
| **Redes e DHCP** | [KB-04](guias/kb-04-wifi-nao-conecta.md) · [KB-05](guias/kb-05-wifi-sem-internet.md) · [KB-06](guias/kb-06-rede-cabeada.md) · [KB-07](guias/kb-07-falha-dns.md) · [KB-08](guias/kb-08-ip-169-254.md) · [KB-23](guias/kb-23-pasta-de-rede.md) |
| **Windows** | [KB-09](guias/kb-09-computador-lento.md) · [KB-10](guias/kb-10-pouco-espaco-em-disco.md) · [KB-25](guias/kb-25-windows-update.md) · [KB-26](guias/kb-26-tela-azul.md) |
| **Aplicativos e Microsoft 365** | [KB-11](guias/kb-11-aplicativo-travado.md) · [KB-12](guias/kb-12-outlook-nao-abre.md) · [KB-13](guias/kb-13-outlook-nao-envia-recebe.md) · [KB-21](guias/kb-21-teams-reuniao.md) · [KB-22](guias/kb-22-onedrive-sincronizacao.md) · [KB-24](guias/kb-24-arquivo-office-bloqueado.md) |
| **Acesso remoto e sistemas** | [KB-14](guias/kb-14-vpn-nao-conecta.md) · [KB-15](guias/kb-15-vpn-conecta-sistema-nao-abre.md) · [KB-20](guias/kb-20-sistema-web.md) |
| **Identidade e segurança** | [KB-16](guias/kb-16-conta-bloqueada.md) · [KB-17](guias/kb-17-senha-esquecida-ou-expirada.md) · [KB-29](guias/kb-29-mfa-autenticador.md) · [KB-30](guias/kb-30-email-suspeito.md) |
| **Hardware e periféricos** | [KB-18](guias/kb-18-microfone.md) · [KB-19](guias/kb-19-segundo-monitor.md) · [KB-27](guias/kb-27-computador-nao-liga.md) · [KB-28](guias/kb-28-notebook-nao-carrega.md) · [KB-31](guias/kb-31-webcam.md) · [KB-32](guias/kb-32-sem-som.md) |

---

<a id="material-de-apoio"></a>
## Material de apoio

Os guias resolvem problemas específicos. Estas páginas ensinam o que vale para **todos** eles.

| Página | Para que serve | Quando abrir |
|---|---|---|
| [**Método**](docs/METODO.md) | O raciocínio de diagnóstico em 6 passos, triagem e regras de segurança | Antes de tudo — é a base |
| [**Mensagens de erro**](docs/MENSAGENS_DE_ERRO.md) | Dicionário de códigos (HTTP, navegador, login `AADSTS`, Outlook, impressão, Gerenciador de Dispositivos, Windows Update, tela azul) → significado → guia | Sempre que aparecer um código |
| [**Comandos**](docs/COMANDOS.md) | `ipconfig`, `nslookup`, `ping`, `tracert`, `Test-NetConnection`, `net use`, `powercfg` e outros, com exemplos de saída | Antes de digitar qualquer comando |
| [**Dicas de bolso**](docs/DICAS.md) | Ferramentas nativas do Windows, atalhos, truques de diagnóstico, dicas por categoria e mitos | Para consultar durante o atendimento |
| [**Comunicação**](docs/COMUNICACAO.md) | O que dizer em cada momento, como traduzir jargão e lidar com situações difíceis | Antes de atender o primeiro usuário real |
| [**Casos práticos**](docs/CASOS_PRATICOS.md) | 8 chamados fictícios, do básico ao avançado, com gabarito | Para treinar e revisar |
| [**Glossário**](docs/GLOSSARIO.md) | Mais de 110 termos técnicos explicados com analogias | Quando uma palavra travar a leitura |
| [**Modelo de chamado**](docs/MODELO_CHAMADO.md) | Como registrar e encaminhar ao N2 | Ao registrar qualquer atendimento |
| [**Plano de validação**](docs/VALIDACAO.md) | Roteiro para testar cada guia em laboratório | Para transformar procedimento proposto em procedimento testado |

---

## Como cada guia é organizado

Todos os guias seguem **o mesmo molde**, para você saber onde encontrar cada informação:

| Seção | O que responde |
|---|---|
| **Em uma frase** | A ideia central, antes de qualquer detalhe |
| **Entenda o problema** | Uma analogia do dia a dia, o sintoma e as causas comuns |
| **Pergunte primeiro** | O que perguntar ao usuário antes de mexer em algo |
| **Antes de começar** | Cuidados de segurança e o que **não** fazer |
| **Passo a passo** | Cada passo com **Faça**, **Por quê** e **O que você deve ver** |
| **Como interpretar o resultado** | Tabela "se você observar X → significa Y → faça Z" |
| **Como saber que resolveu** | Checklist de validação com o usuário |
| **O que anotar no chamado** | Evidências mínimas para o registro |
| **Quando encaminhar ao N2** | O limite do primeiro atendimento |
| **Erros comuns** | As armadilhas mais frequentes, antes que você caia nelas |

---

## As 5 regras que valem para tudo

> [!CAUTION]
> 1. **Nunca peça senha nem código de MFA.** Quem digita é sempre o usuário.
> 2. **Acesso remoto só com ciência do usuário** e por ferramenta autorizada.
> 3. **Combine antes de reiniciar ou fechar programas**, para o usuário salvar o trabalho.
> 4. **Não desative proteções** (antivírus, firewall, certificados) para testar.
> 5. **Dados reais de atendimento ficam no sistema interno** — nunca neste repositório público.

Os detalhes estão no [método](docs/METODO.md#regras-de-segurança-valem-para-todos-os-guias).

---

## Ambiente de referência

- **Sistema:** Windows 11. O Windows 10 não é o ambiente padrão desta base; avalie o ciclo de suporte antes de usá-lo.
- **Aplicativos:** Microsoft 365. O modo seguro citado vale para o **Outlook clássico**, não para o novo Outlook.
- **Rede:** pequeno escritório.

## Estrutura do repositório

```text
base-troubleshooting/
├── README.md               ← você está aqui: visão geral e índice
├── guias/                  ← os 32 guias, um arquivo por problema
│   ├── kb-01-impressora-offline.md
│   ├── ...
│   └── kb-32-sem-som.md
├── docs/
│   ├── METODO.md           ← o raciocínio de diagnóstico (comece por aqui)
│   ├── MENSAGENS_DE_ERRO.md← dicionário de códigos e mensagens de erro
│   ├── COMANDOS.md         ← comandos de diagnóstico explicados
│   ├── DICAS.md            ← ferramentas, atalhos, truques e mitos
│   ├── COMUNICACAO.md      ← como falar com o usuário
│   ├── CASOS_PRATICOS.md   ← chamados fictícios com gabarito
│   ├── GLOSSARIO.md        ← termos técnicos em linguagem simples
│   ├── MODELO_CHAMADO.md   ← como registrar e encaminhar ao N2
│   └── VALIDACAO.md        ← plano para testar os guias em laboratório
├── scripts/
│   └── verificar_links.py  ← confere se todos os links internos funcionam
├── CONTRIBUTING.md         ← como sugerir melhorias
└── CHANGELOG.md            ← histórico de versões
```

---

## Referências oficiais

Consultadas em 10/11/2026; as adicionadas na versão 3.0 (KB-21 a KB-32 e material de apoio) foram conferidas em 24/11/2026. Os guias são sínteses autorais e procedimentos propostos, **não** documentação oficial da Microsoft. Valide versões e instruções locais antes de aplicar.

- [Impressão no Windows](https://support.microsoft.com/pt-br/windows/hardware/printer/fix-printer-connection-and-printing-problems-in-windows)
- [Conectividade Wi-Fi](https://support.microsoft.com/pt-br/windows/experience/connectivity-networking/fix-wi-fi-connection-issues-in-windows)
- [Comando ipconfig](https://learn.microsoft.com/pt-br/windows-server/administration/windows-commands/ipconfig)
- [Comando nslookup](https://learn.microsoft.com/pt-br/windows-server/administration/windows-commands/nslookup)
- [Diagnóstico do cliente DNS](https://learn.microsoft.com/pt-br/windows-server/networking/dns/troubleshoot/troubleshoot-dns-client)
- [Desempenho do Windows](https://support.microsoft.com/en-us/windows/experience/performance-optimization/tips-to-improve-pc-performance-in-windows)
- [Outlook clássico sem responder](https://support.microsoft.com/pt-br/outlook/classic-outlook-not-responding-stuck-at-processing-stopped-working-or-freezes)
- [Envio e recebimento no Outlook](https://support.microsoft.com/pt-br/outlook/i-can-t-send-or-receive-messages-in-outlook)
- [VPN no Windows](https://support.microsoft.com/pt-br/windows/experience/connectivity-networking/connect-to-a-vpn-in-windows)
- [Redefinição e desbloqueio por autoatendimento](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-sspr-howitworks)
- [Microfone no Windows](https://support.microsoft.com/en-us/windows/hardware/drivers/fix-microphone-problems)
- [Monitor externo](https://support.microsoft.com/en-us/windows/hardware/display-graphics/troubleshoot-external-monitor-connections-in-windows)
- [Suporte do Microsoft Teams](https://support.microsoft.com/pt-br/teams)
- [Problemas de sincronização do OneDrive](https://support.microsoft.com/pt-br/onedrive/fix-onedrive-sync-problems)
- [Problemas ao atualizar o Windows](https://support.microsoft.com/pt-br/windows/deployment/updates-lifecycle/troubleshoot-problems-updating-windows)
- [Códigos de parada (tela azul)](https://learn.microsoft.com/pt-br/windows-hardware/drivers/debugger/bug-check-code-reference2)
- [Como funciona o MFA do Microsoft Entra](https://learn.microsoft.com/pt-br/entra/identity/authentication/concept-mfa-howitworks)
- [Códigos de erro de login do Entra ID (AADSTS)](https://learn.microsoft.com/pt-br/entra/identity-platform/reference-error-codes)
- [Proteção contra phishing](https://learn.microsoft.com/pt-br/defender-endpoint/malware/phishing)
- [Cartilha de Segurança para Internet — CERT.br](https://cartilha.cert.br/)
- [Opções do powercfg](https://learn.microsoft.com/pt-br/windows-hardware/design/device-experiences/powercfg-command-line-options)

---

## Limites desta versão

- Não foram executados testes em dispositivos, impressoras, VPN ou contas corporativas. **Todos os cenários do [plano de validação](docs/VALIDACAO.md) estão como "Não executado".**
- Antes de adotar em produção, valide em laboratório autorizado e registre ambiente, resultado e data.
- Atualizações devem sempre distinguir **hipótese**, **teste realizado** e **conclusão confirmada**.

## Contribuir

Encontrou um erro ou tem uma sugestão? Veja o [guia de contribuição](CONTRIBUTING.md). As issues são para correções da documentação — **não são canal de suporte** nem lugar para dados de clientes.

**Histórico de versões:** [CHANGELOG.md](CHANGELOG.md)

---

Portfólio de estudo de **[Mateus Santos Telles](https://www.linkedin.com/in/mateusantostelles/)**, estudante de Análise e Desenvolvimento de Sistemas. Demonstra raciocínio de diagnóstico, documentação técnica e comunicação com usuários.

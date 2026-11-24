# Dicas de bolso — ferramentas, atalhos e truques do N1

[← Voltar ao início](../README.md) · [Método](METODO.md) · [Comandos](COMANDOS.md) · [Mensagens de erro](MENSAGENS_DE_ERRO.md)

> **Em uma frase:** a maior parte do diagnóstico N1 se faz com **ferramentas que já vêm no Windows** — saber onde elas estão e qual pergunta cada uma responde economiza metade do atendimento.

---

## Por que esta página existe

Os guias dizem **o que** fazer em cada problema. Esta página reúne o que se repete em **todos** eles: as ferramentas que você abre toda hora, os atalhos que poupam cliques e os truques de raciocínio que separam um atendimento de 5 minutos de um de 50.

**Atalhos:** [Ferramentas nativas](#as-ferramentas-nativas-que-você-mais-vai-usar) · [Atalhos de teclado](#atalhos-de-teclado-do-suporte) · [Truques de diagnóstico](#truques-de-diagnóstico) · [Dicas por categoria](#dicas-rápidas-por-categoria) · [Checklist do primeiro minuto](#checklist-do-primeiro-minuto) · [Mitos](#mitos-do-suporte)

---

## As ferramentas nativas que você mais vai usar

Todas abrem por `Win + R` → digite o nome → `Enter`.

| Ferramenta | Como abrir | A pergunta que ela responde | Guias |
|---|---|---|---|
| **Gerenciador de Tarefas** | `Ctrl + Shift + Esc` | "O que está consumindo o computador agora?" | [KB-09](../guias/kb-09-computador-lento.md), [KB-11](../guias/kb-11-aplicativo-travado.md) |
| **Monitor de Confiabilidade** | `perfmon /rel` | "O que falhou e o que mudou nos últimos dias?" | [KB-26](../guias/kb-26-tela-azul.md), [KB-11](../guias/kb-11-aplicativo-travado.md) |
| **Monitor de Recursos** | `resmon` | "Qual programa está usando disco, rede ou memória — em detalhe?" | [KB-09](../guias/kb-09-computador-lento.md) |
| **Gerenciador de Dispositivos** | `devmgmt.msc` | "O Windows reconhece esse hardware? O driver funciona?" | [KB-03](../guias/kb-03-driver-de-impressora.md), [KB-18](../guias/kb-18-microfone.md), [KB-31](../guias/kb-31-webcam.md) |
| **Visualizador de Eventos** | `eventvwr.msc` | "O que o Windows registrou na hora do problema?" | [KB-26](../guias/kb-26-tela-azul.md) |
| **Informações do Sistema** | `msinfo32` | "Qual modelo, memória, BIOS e versão do Windows?" | Todos (para o chamado) |
| **Conexões de Rede** | `ncpa.cpl` | "Quais adaptadores existem e quais estão ativos?" | [KB-04](../guias/kb-04-wifi-nao-conecta.md) a [KB-08](../guias/kb-08-ip-169-254.md) |
| **Impressoras** | Configurações → Bluetooth e dispositivos → Impressoras | "A impressora está instalada? Como está a fila?" | [KB-01](../guias/kb-01-impressora-offline.md) a [KB-03](../guias/kb-03-driver-de-impressora.md) |
| **Gerenciador de Credenciais** | Painel de Controle → Gerenciador de Credenciais | "Há senha antiga salva atrapalhando?" | [KB-16](../guias/kb-16-conta-bloqueada.md), [KB-23](../guias/kb-23-pasta-de-rede.md) |
| **Sobre o Windows** | `winver` | "Qual versão e build?" | Todos (para o chamado) |
| **Ferramenta de Captura** | `Win + Shift + S` | "Como registro o erro na tela?" | Todos |

> [!TIP]
> No Gerenciador de Tarefas, a aba **Desempenho** mostra a utilização geral e a aba **Processos** mostra **quem** está usando. Ordene a coluna clicando no título (CPU, Memória, Disco) para ver o maior consumidor no topo.

---

## Atalhos de teclado do suporte

| Atalho | O que faz | Quando usar |
|---|---|---|
| `Win + R` | Abre o "Executar" | Para abrir qualquer ferramenta pelo nome |
| `Win + X` | Menu rápido (Gerenciador de Dispositivos, Terminal, Conexões…) | Atalho para ferramentas administrativas |
| `Ctrl + Shift + Esc` | Abre o Gerenciador de Tarefas direto | Programa travado, computador lento |
| `Win + Shift + S` | Captura de parte da tela | Registrar uma mensagem de erro |
| `Win + P` | Modo de projeção (duplicar, estender, só segundo monitor) | [KB-19](../guias/kb-19-segundo-monitor.md) |
| `Win + Ctrl + Shift + B` | Reinicia o driver de vídeo (a tela pisca) | Tela preta ou congelada após trocar monitor |
| `Win + L` | Bloqueia o computador | **Sempre** que se afastar da mesa — e ensine o usuário |
| `Win + V` | Histórico da área de transferência (se ativado) | Copiar várias informações para o chamado |
| `Win + .` | Painel de emojis e símbolos | Digitar caracteres especiais |
| `Alt + Tab` | Alterna entre janelas abertas | Achar uma caixa de diálogo "escondida" atrás de outra janela |
| `Ctrl + Shift + T` | Reabre a última aba fechada no navegador | O usuário fechou a aba sem querer |
| `Ctrl + F5` | Recarrega a página ignorando parte do cache | Página web "presa" numa versão antiga |

> [!TIP]
> **Programa "travado" que não responde a cliques?** Antes de encerrar, use `Alt + Tab`. Muitas vezes há uma janela de diálogo ("Deseja salvar?") escondida atrás da principal, esperando resposta. Veja o [KB-11](../guias/kb-11-aplicativo-travado.md).

---

## Truques de diagnóstico

### 1. A pergunta que corta o problema pela metade

> **"Funciona em outro lugar?"**

| Compare… | Se funciona no outro, o problema está… |
|---|---|
| Outro site | No site original, não na internet |
| Webmail × aplicativo | No aplicativo, não na conta |
| Teams web × Teams instalado | No aplicativo instalado |
| Outro computador, mesma conta | No computador, não na conta |
| Outra conta, mesmo computador | Na conta, não no computador |
| Outra rede (ex.: roteador do celular) | Na rede original |
| Janela privativa | Na sessão/cookies/extensões do navegador |

Cada comparação é uma **busca binária**: você descarta metade das possibilidades a cada teste.

### 2. "O que mudou?"

Quase todo problema que "começou do nada" começou **depois de alguma coisa**: atualização, senha nova, mudança de mesa, periférico novo, instalação. O **Monitor de Confiabilidade** (`perfmon /rel`) mostra as mudanças em uma linha do tempo.

### 3. Reproduza antes de corrigir

Peça ao usuário para **mostrar** o problema acontecendo. Você descobre detalhes que ele não sabia que eram importantes ("ah, só dá erro quando abro pelo atalho da área de trabalho").

### 4. Anote o estado antes de mudar

Antes de alterar qualquer configuração, **fotografe ou anote como estava**. Se a mudança não resolver, você volta ao ponto de partida — e não cria um segundo problema.

### 5. Desconfie do "funcionou depois que reiniciei"

Reiniciar limpa sintomas, mas também **apaga pistas**. Antes de reiniciar, registre a mensagem de erro e o que estava aberto. Depois, registre como **contorno**, não como causa.

### 6. Leia a mensagem inteira, devagar

Parece óbvio, mas a maioria das mensagens de erro diz exatamente o que está errado ("bloqueado por Fulano", "caminho não encontrado", "sem permissão"). Consulte o [dicionário de mensagens de erro](MENSAGENS_DE_ERRO.md).

---

## Dicas rápidas por categoria

### Rede

- **Ícone de globo com "sem internet"** não significa sem rede: o computador pode estar na rede local e só não alcançar a internet ([KB-05](../guias/kb-05-wifi-sem-internet.md)).
- **IP começando com `169.254`** é a assinatura de "não recebi endereço do DHCP" ([KB-08](../guias/kb-08-ip-169-254.md)).
- **Wi-Fi de 5 GHz** é mais rápido; **2,4 GHz** alcança mais longe e atravessa melhor paredes. Se a pessoa está longe do roteador, a rede de 2,4 GHz pode ser mais estável.
- **Para testar se é a rede da empresa**, compare com o roteador do celular — **se a política permitir**.

### Impressão

- **"Offline"** quase sempre é caminho até a impressora, não defeito da impressora ([KB-01](../guias/kb-01-impressora-offline.md)).
- **Um documento travado segura toda a fila**: olhe o primeiro da lista ([KB-02](../guias/kb-02-documento-preso-na-fila.md)).
- Confira se o usuário está mandando para a **impressora certa** — há muitas com nomes parecidos.

### Contas

- **Caps Lock e idioma do teclado** (ABNT2 × EUA) explicam muitas "senhas erradas".
- **Senha trocada recentemente?** Celular, notebook e aplicativos com a senha antiga salva provocam bloqueio repetido ([KB-16](../guias/kb-16-conta-bloqueada.md)).
- **Nunca** peça senha ou código de MFA ([KB-29](../guias/kb-29-mfa-autenticador.md)).

### Microsoft 365

- **Compare sempre com a versão web** (webmail, Teams web, OneDrive web). É o teste mais rápido para separar aplicativo de conta.
- **Outlook clássico × novo Outlook** são aplicativos diferentes: o clássico tem a guia **Arquivo** ([KB-12](../guias/kb-12-outlook-nao-abre.md)).
- **Histórico de versões** do OneDrive/SharePoint salva o dia de quem sobrescreveu um arquivo ([KB-24](../guias/kb-24-arquivo-office-bloqueado.md)).

### Hardware

- **"Não liga"** pode ser "liga, mas o monitor está na entrada errada" ([KB-27](../guias/kb-27-computador-nao-liga.md)).
- **"Desligar" não é "Reiniciar"** quando a inicialização rápida está ativa. Para concluir atualizações, use **Reiniciar** ([KB-25](../guias/kb-25-windows-update.md)).
- **Bateria estufada** é risco de incêndio: pare o uso e encaminhe ([KB-28](../guias/kb-28-notebook-nao-carrega.md)).

### Áudio e vídeo

- **Sem som?** Olhe primeiro **qual saída** está selecionada ([KB-32](../guias/kb-32-sem-som.md)).
- **Câmera preta?** Olhe a **tampinha** ([KB-31](../guias/kb-31-webcam.md)).
- **Ninguém me ouve?** Use a **chamada de teste** do Teams ([KB-18](../guias/kb-18-microfone.md)).

---

## Checklist do primeiro minuto

Antes de qualquer teste, em qualquer chamado:

- [ ] Qual **tarefa** a pessoa não consegue fazer?
- [ ] Qual é a **mensagem exata**? (foto ou texto)
- [ ] **Desde quando**? **Mudou algo**?
- [ ] **Só com ela** ou com outras pessoas também?
- [ ] Há algum indício de **segurança** (e-mail estranho, aprovação de MFA não pedida, arquivos sumindo)? → [KB-30](../guias/kb-30-email-suspeito.md)
- [ ] O trabalho está **salvo** antes de reiniciar ou fechar algo?

---

## Mitos do suporte

| Mito | Realidade |
|---|---|
| "Reiniciar resolve tudo" | Reiniciar **esconde** muitos sintomas e apaga pistas. É contorno, não diagnóstico |
| "Sem resposta ao `ping` = servidor fora do ar" | Muitas redes bloqueiam `ping` de propósito |
| "Limpar o cache do navegador resolve sites" | Às vezes. Teste antes a janela privativa, que não apaga nada |
| "Formatar é a solução definitiva" | Apaga evidências e dados, e não resolve defeito de hardware nem de conta |
| "DNS público resolve problemas de DNS" | Não conhece nomes internos e pode violar a política |
| "Desativar o antivírus para testar é seguro" | Abre a porta para exatamente o que ele bloqueia |
| "O usuário errou, então não precisa registrar" | O registro mostra padrões e evita a repetição |

---

## Teste seu entendimento

1. Um usuário diz que o Excel "travou". Antes de abrir o Gerenciador de Tarefas, qual atalho você tentaria e por quê?
2. Você precisa descobrir se o problema de um usuário está no computador dele ou na conta dele. Desenhe **duas comparações** que respondem isso.
3. Explique para alguém leigo por que "Desligar" e "Reiniciar" podem não ser a mesma coisa no Windows 11.

---

[← Voltar ao início](../README.md)

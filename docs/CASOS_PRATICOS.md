# Casos práticos — treine o raciocínio com gabarito

[← Voltar ao início](../README.md) · [Método](METODO.md) · [Mensagens de erro](MENSAGENS_DE_ERRO.md)

> **Em uma frase:** ler os guias ensina o caminho; **resolver casos** ensina a escolher o caminho certo quando ninguém diz qual guia usar.

---

## Como usar esta página

Cada caso é um chamado fictício, contado como o usuário contaria — **sem dizer qual é o problema técnico**. Os casos estão misturados de propósito: na vida real, o chamado não vem com etiqueta.

1. Leia o caso.
2. **Antes de abrir o gabarito**, escreva (no papel ou num arquivo):
   - a **primeira pergunta** que você faria;
   - sua **hipótese inicial**;
   - o **primeiro teste** e o que cada resultado significaria;
   - o **guia** que você usaria.
3. Só então abra o gabarito e compare.

> [!TIP]
> O esforço de tentar responder **antes** de ver a resposta (mesmo errando) fixa o conhecimento muito mais do que só ler. Errar aqui é barato; errar com o usuário real, não.

**Dificuldade:** 🟢 básico · 🟡 intermediário · 🔴 avançado

---

## Caso 1 🟢 — "A impressora sumiu"

> "Bom dia! Mudei de mesa ontem e hoje não consigo imprimir. Aparece que a impressora está offline. Os colegas da nova sala imprimem normal."

<details>
<summary><strong>Ver gabarito</strong></summary>

**Primeira pergunta:** "Qual impressora você está selecionando na hora de imprimir?"

**Raciocínio:** "mudei de mesa" é a mudança. Os colegas imprimem, então a impressora da nova sala funciona (escopo individual). A hipótese mais provável é que o usuário continua mandando para a **impressora da sala antiga**, que talvez nem alcance mais da nova rede ou foi desligada.

**Primeiro teste:** conferir a impressora selecionada e o destino dela.

**Guia:** [KB-01](../guias/kb-01-impressora-offline.md); se for preciso instalar a impressora nova, [KB-03](../guias/kb-03-driver-de-impressora.md).

**Armadilha:** reiniciar o spooler ou reinstalar drivers antes de perguntar qual impressora está selecionada.

</details>

---

## Caso 2 🟢 — "O Wi-Fi está conectado, mas nada abre"

> "O ícone mostra que estou no Wi-Fi da empresa, mas nenhum site abre. No celular, na mesma rede, funciona."

<details>
<summary><strong>Ver gabarito</strong></summary>

**Primeira pergunta:** "Nada abre mesmo, nem sites externos nem sistemas internos? Aparece alguma mensagem no navegador?"

**Raciocínio:** o celular funciona na mesma rede, então a rede e a internet estão bem (escopo: este computador). O próximo passo é ver se o computador recebeu configuração válida.

**Primeiro teste:** `ipconfig`.

| Se aparecer… | Significa | Guia |
|---|---|---|
| `169.254.x.x` | Não recebeu endereço do DHCP | [KB-08](../guias/kb-08-ip-169-254.md) |
| Endereço normal e gateway | Configuração ok; teste DNS | [KB-07](../guias/kb-07-falha-dns.md) |

**Guia de entrada:** [KB-05](../guias/kb-05-wifi-sem-internet.md).

**Armadilha:** "esquecer a rede" e reconectar antes de olhar o `ipconfig` — você perde a pista do que estava errado.

</details>

---

## Caso 3 🟡 — "Minha conta bloqueia toda segunda-feira"

> "Toda segunda de manhã minha conta está bloqueada. Desbloqueiam, funciona a semana inteira, e na outra segunda bloqueia de novo. Troquei a senha há umas três semanas."

<details>
<summary><strong>Ver gabarito</strong></summary>

**Primeira pergunta:** "Que aparelhos ou programas usam sua conta da empresa? Celular, tablet, outro notebook, algum programa que fica ligado no fim de semana?"

**Raciocínio:** o padrão **semanal** e a **troca de senha recente** apontam para algo que tenta entrar com a **senha antiga** repetidamente — por exemplo, o e-mail corporativo configurado num celular ou tablet que fica ligado no fim de semana. Desbloquear sozinho não resolve: a causa continua lá.

**Primeiro teste:** listar os dispositivos e aplicativos com a conta configurada e atualizar a senha em cada um. O N2 pode identificar a **origem** das tentativas nos registros.

**Guia:** [KB-16](../guias/kb-16-conta-bloqueada.md).

**Armadilha:** desbloquear toda segunda sem investigar. Também não é motivo para **enfraquecer** a política de bloqueio.

</details>

---

## Caso 4 🟡 — "Ninguém me ouve, mas o Teams funciona"

> "Entro nas reuniões do Teams normalmente, vejo e ouço todo mundo, mas ninguém me ouve. Ontem funcionava. Hoje cedo liguei o notebook na dock nova."

<details>
<summary><strong>Ver gabarito</strong></summary>

**Primeira pergunta:** "Qual microfone está selecionado nas configurações de dispositivos do Teams?"

**Raciocínio:** "dock nova" é a mudança. Docks costumam trazer seu próprio dispositivo de áudio e o Windows ou o Teams podem passar a usar essa entrada (que não tem microfone ligado) em vez do microfone do fone ou do notebook.

**Primeiro teste:** chamada de teste no Teams e o medidor de entrada do Windows.

**Guia:** [KB-18](../guias/kb-18-microfone.md). Se o problema fosse o som de saída, [KB-32](../guias/kb-32-sem-som.md).

**Armadilha:** reinstalar o Teams. Ele está funcionando; o que mudou foi o dispositivo de entrada.

</details>

---

## Caso 5 🟡 — "Recebi um e-mail do RH e agora estou preocupado"

> "Recebi um e-mail do 'RH' pedindo para atualizar meus dados bancários até hoje, senão o salário atrasa. Cliquei no link e coloquei meu login. Depois achei estranho."

<details>
<summary><strong>Ver gabarito</strong></summary>

**Primeira pergunta:** "Depois de digitar o login, apareceu algum pedido de aprovação no celular? Você aprovou? Chegou a preencher os dados bancários?"

**Raciocínio:** urgência ("até hoje") + ameaça ("salário atrasa") + pedido incomum (dados bancários por link) = phishing clássico. O usuário **digitou a senha** numa página falsa: gravidade **alta**. Se aprovou MFA, **crítica**.

**Ações, em ordem:**

1. Trocar a senha **agora**, pelo caminho oficial ([KB-17](../guias/kb-17-senha-esquecida-ou-expirada.md)).
2. Acionar a segurança como **incidente**, com horário aproximado.
3. Se aprovou MFA, informar isso com prioridade ([KB-29](../guias/kb-29-mfa-autenticador.md)).
4. Se preencheu dados bancários, acionar também o financeiro/RH real.
5. Relatar a mensagem pelo canal oficial.

**Guia:** [KB-30](../guias/kb-30-email-suspeito.md).

**Armadilha:** abrir o link "para ver" ou repreender o usuário. Agradeça por ter avisado.

</details>

---

## Caso 6 🔴 — "O sistema abre pra todo mundo, menos pra mim, e só de casa"

> "No escritório o sistema financeiro abre normal. Em casa, com a VPN conectada, aparece 'não foi possível acessar esse site'. Meu colega, também de casa, consegue."

<details>
<summary><strong>Ver gabarito</strong></summary>

**Primeira pergunta:** "Você digita o endereço ou usa um atalho? Outros sistemas internos abrem pela VPN?"

**Raciocínio:** no escritório funciona → conta e permissão estão ok. Na VPN, o colega consegue → o sistema e a VPN estão ok em geral. Sobra: **algo no caminho deste computador pela VPN** — nome que não resolve pela VPN (DNS), atalho apontando para um endereço só do escritório, ou rota que não passa pelo túnel.

**Testes, um por vez:**

1. `nslookup nome-do-sistema` com a VPN ligada → o nome resolve? ([KB-07](../guias/kb-07-falha-dns.md))
2. `Test-NetConnection nome-do-sistema -Port 443` → a porta responde? ([Comandos](COMANDOS.md#test-netconnection--essa-porta-específica-responde))
3. Comparar o endereço retornado com o documentado.

**Guia:** [KB-15](../guias/kb-15-vpn-conecta-sistema-nao-abre.md).

**Armadilha:** concluir "VPN com defeito" — a VPN conecta e funciona para o colega. Também não oriente trocar DNS ou rotas manualmente.

</details>

---

## Caso 7 🔴 — "O computador reinicia sozinho desde a semana passada"

> "Desde a semana passada o computador reinicia do nada umas duas vezes por dia, às vezes com uma tela azul. Antes nunca tinha acontecido."

<details>
<summary><strong>Ver gabarito</strong></summary>

**Primeira pergunta:** "Você conseguiu ver ou fotografar o código na tela? Instalou ou conectou algo na semana passada?"

**Raciocínio:** "desde a semana passada" sugere uma **mudança** nessa época. O Monitor de Confiabilidade mostra exatamente isso: falhas e instalações em linha do tempo.

**Primeiro teste:** `perfmon /rel` e procurar o que foi instalado logo antes do primeiro X vermelho.

**Guia:** [KB-26](../guias/kb-26-tela-azul.md).

**Armadilha:** usar o evento **Kernel-Power 41** como causa (ele só diz que o desligamento foi inesperado) ou formatar o computador e apagar as evidências.

</details>

---

## Caso 8 🔴 — "O arquivo da equipe voltou para a versão de ontem"

> "Trabalhei a manhã toda na planilha da equipe, que fica na pasta compartilhada. Agora abri e está com o conteúdo de ontem. Acho que alguém salvou por cima."

<details>
<summary><strong>Ver gabarito</strong></summary>

**Primeira pergunta:** "A pasta é do OneDrive/SharePoint/Teams ou uma pasta de rede (com letra, tipo S:)? Alguém mais estava com o arquivo aberto?"

**Raciocínio:** o caminho de recuperação depende do **local**. Na nuvem, o **Histórico de versões** quase sempre tem a versão da manhã. Em pasta de rede, depende das **Versões Anteriores** ou do backup.

**Ações:**

1. **Parar de salvar** no arquivo.
2. Abrir o histórico de versões e **conferir com o usuário** antes de restaurar.
3. Se não houver versão disponível, encaminhar ao N2 (backup) com nome, local e horário.
4. Para evitar de novo: mover o trabalho em equipe para a nuvem (coautoria).

**Guia:** [KB-24](../guias/kb-24-arquivo-office-bloqueado.md).

**Armadilha:** restaurar a versão sem conferir — pode descartar o trabalho de outra pessoa feito depois.

</details>

---

## Depois de resolver os casos

Responda sem consultar:

1. Em quantos casos a **primeira pergunta** foi sobre **o que mudou**? Por que essa pergunta aparece tanto?
2. Em quais casos a resposta "funciona para o colega" eliminou hipóteses? Quais ela eliminou?
3. Escolha um caso e escreva o registro do chamado usando o [modelo de chamado](MODELO_CHAMADO.md).

> [!NOTE]
> Volte a esta página daqui a alguns dias e tente os casos de novo, sem olhar os gabaritos. Lembrar depois de um intervalo (repetição espaçada) é o que transforma o raciocínio em hábito.

---

[← Voltar ao início](../README.md)

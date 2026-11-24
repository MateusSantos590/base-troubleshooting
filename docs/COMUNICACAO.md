# Comunicação com o usuário — o que dizer, como dizer e o que evitar

[← Voltar ao início](../README.md) · [Método](METODO.md) · [Modelo de chamado](MODELO_CHAMADO.md)

> **Em uma frase:** o usuário não avalia o seu diagnóstico — ele avalia **como se sentiu** durante o atendimento. Comunicação clara é parte técnica do trabalho, não enfeite.

---

## Por que isso importa

Um técnico que resolve o problema mas deixa o usuário confuso, ansioso ou se sentindo culpado gera três efeitos: o usuário **esconde problemas** da próxima vez, **interrompe** o atendimento com perguntas e **desconfia** da solução. Comunicação boa é o que faz o usuário colaborar com o diagnóstico — e ele é a sua principal fonte de evidências.

## A analogia: o mecânico de confiança

| Mecânico que gera desconfiança | Mecânico de confiança |
|---|---|
| "Deu problema na junta homocinética, vou trocar." | "Esse barulho vem de uma peça da roda. Vou confirmar antes de trocar qualquer coisa." |
| Some por três dias sem dar notícia | Liga para avisar: "ainda estou esperando a peça, devo ter novidade amanhã à tarde" |
| "Quem mexeu nisso?" | "Isso acontece bastante, vamos resolver." |
| Entrega o carro sem explicar | "Era isso, troquei aquilo. Se o barulho voltar, me avise." |

---

## Os 5 momentos do atendimento

### 1. Abertura — mostre que entendeu

**Objetivo:** confirmar o problema com as palavras do usuário e combinar o próximo passo.

> "Entendi: desde hoje de manhã o Outlook não abre e aparece uma mensagem de erro. Vou fazer alguns testes rápidos, um de cada vez. Antes de reiniciar ou fechar qualquer coisa, eu te aviso para você salvar o que estiver aberto."

**Por quê:** repetir o problema com outras palavras (paráfrase) prova que você ouviu e corrige mal-entendidos logo no início.

### 2. Durante o diagnóstico — narre o que está fazendo

**Objetivo:** o usuário nunca deve ficar no escuro, principalmente em acesso remoto.

> "Agora vou abrir uma tela que mostra o que está consumindo o computador. Não vou mexer em nenhum arquivo seu."

**Por quê:** ver alguém mexendo no seu computador sem explicar dá ansiedade. Narrar também ensina o usuário, que às vezes resolve sozinho da próxima vez.

### 3. Quando precisa de algo do usuário — peça uma coisa por vez

> ✅ "Pode clicar no ícone de nuvem perto do relógio e me dizer o que está escrito no topo?"
>
> ❌ "Abre o OneDrive, vai em configurações, depois conta, e me diz o espaço, e também vê se está pausado."

**Por quê:** instruções longas sobrecarregam a memória de trabalho de quem não é técnico. Um passo, uma confirmação, próximo passo.

### 4. Encaminhamento — seja honesto sobre o que acontece agora

> "Fiz os testes que estão ao meu alcance e o problema continua. Encaminhei para a equipe de redes com tudo o que já testamos, para eles não precisarem repetir. O próximo contato está previsto para [o prazo registrado no chamado]. Enquanto isso, você consegue acessar pelo navegador."

**Por quê:** o usuário precisa saber **que** foi encaminhado, **para quem**, **quando** terá notícia e **como trabalhar** enquanto isso. Nunca invente prazo.

### 5. Encerramento — confirme e deixe a porta aberta

> "Você consegue abrir o arquivo agora? Ótimo. O problema era uma cópia do arquivo aberta em outra janela. Se acontecer de novo, este chamado é o número X — é só responder nele."

**Por quê:** a confirmação do usuário é a validação real. Explicar a causa em uma frase ajuda a evitar o próximo chamado.

---

## Traduzindo o jargão

Troque o termo técnico pela **ideia** por trás dele.

| Em vez de… | Diga… |
|---|---|
| "O DNS não está resolvendo." | "O computador não está conseguindo encontrar o endereço do sistema." |
| "Seu IP está em APIPA." | "O computador não recebeu da rede as informações para se conectar." |
| "Vou limpar o cache." | "Vou apagar uns arquivos temporários que o programa guarda. Seus dados não são afetados." |
| "É problema de permissão no compartilhamento." | "Você chega até a pasta, mas ainda não tem autorização para entrar. Quem libera é o responsável por ela." |
| "O spooler travou." | "O serviço que organiza a fila de impressão travou." |
| "Vou escalonar para o N2." | "Vou passar para a equipe especializada, com tudo o que já testamos." |
| "É um 403." | "O sistema reconheceu você, mas ainda não liberou acesso a essa parte." |

> [!TIP]
> Teste de Feynman do suporte: se você não consegue explicar o problema para o usuário em **uma frase sem jargão**, talvez ainda não tenha entendido o problema.

---

## Situações difíceis

### Usuário irritado ou com pressa

1. **Reconheça o impacto**, sem se defender: "Entendo, você tem uma reunião daqui a pouco e isso atrapalha."
2. **Ofereça um contorno imediato**, se houver: "Enquanto investigo, você consegue entrar pela versão web."
3. **Combine o próximo passo** com prazo realista.

> [!NOTE]
> Urgência do usuário não muda a prioridade sozinha: ela segue a matriz de impacto e urgência da empresa. Mas **reconhecer** a urgência muda muito a experiência.

### Usuário que se culpa ("eu devo ter feito besteira")

> "Isso acontece bastante e não tem a ver com algo que você fez errado. Vamos resolver."

Mesmo que tenha sido um clique errado: o objetivo é que a pessoa **continue avisando**, principalmente em casos de segurança ([KB-30](../guias/kb-30-email-suspeito.md)).

### Pedido fora da política ("me dá admin", "desativa o antivírus", "usa a senha do meu colega")

> "Entendo a necessidade. Isso eu não posso fazer porque [motivo curto: protege sua conta / é regra de segurança]. O que posso fazer é [alternativa: abrir a solicitação formal / instalar pelo portal oficial]."

**Estrutura:** reconhecer → recusar com motivo → oferecer alternativa. Recusa sem alternativa soa como má vontade.

### Ligação de alguém que diz ser "da diretoria" pedindo redefinição urgente

Siga o procedimento de verificação de identidade **sempre**, sem exceção. Urgência e autoridade são as duas pressões mais usadas em engenharia social ([KB-29](../guias/kb-29-mfa-autenticador.md)).

> "Para sua segurança, preciso seguir a verificação padrão. É rápido."

---

## Frases que vale evitar

| Evite | Por quê | Prefira |
|---|---|---|
| "Isso é fácil." | Faz quem não conseguiu se sentir incapaz | "Vamos resolver juntos." |
| "Você mexeu em alguma coisa?" | Soa como acusação | "Mudou algo recentemente, como uma atualização ou um aparelho novo?" |
| "Aqui funciona." | Invalida a experiência do usuário | "No meu teste funcionou; vamos ver o que é diferente no seu." |
| "Deve ser vírus." | Gera pânico sem evidência | "Vou verificar algumas possibilidades." |
| "Já está resolvido" (sem testar com o usuário) | Encerramento sem validação | "Pode testar agora para confirmarmos?" |
| "Não sei." (e parar aí) | Fecha a conversa | "Ainda não sei — vou verificar e te retorno até [prazo]." |

---

## Modelos curtos por canal

**Chat:**
> Olá! Vi seu chamado sobre [problema]. Vou te ajudar agora. Para começar: qual mensagem aparece na tela? Se puder, mande uma foto (sem senhas ou dados de clientes).

**E-mail de acompanhamento:**
> Assunto: [Chamado nº] — atualização
>
> Olá, [nome]. Atualizando: testamos [teste] e o resultado foi [resultado]. O próximo passo é [ação], com retorno previsto até [prazo registrado]. Enquanto isso, [contorno, se houver].

**Antes do acesso remoto:**
> Vou acessar seu computador remotamente pela ferramenta oficial da empresa. Você vai ver o que estou fazendo o tempo todo e pode me interromper a qualquer momento. Feche documentos com informações sensíveis que não tenham a ver com o problema.

---

## Teste seu entendimento

1. Reescreva sem jargão: "Seu perfil do Outlook está corrompido, vou recriar o OST."
2. Um usuário exige que você desative o firewall "só por cinco minutos" para um sistema funcionar. Escreva sua resposta usando a estrutura **reconhecer → recusar com motivo → oferecer alternativa**.
3. Por que agradecer quem clicou num phishing é uma decisão **técnica** de segurança, e não só gentileza?

---

[← Voltar ao início](../README.md)

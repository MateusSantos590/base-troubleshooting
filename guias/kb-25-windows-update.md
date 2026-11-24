# KB-25 · Windows Update falha ou não termina

[← Índice](../README.md#indice) · **Categoria:** Windows · **Quem executa:** N1 (reparos de componentes do Windows são do N2)

> **Em uma frase:** a maioria das falhas de atualização é **falta de espaço**, **reinício pendente** ou **regra da empresa** — e o código de erro é a pista que você não pode perder.

---

## Entenda o problema

Atualizar o Windows é como **reformar uma casa com gente morando dentro**. A obra precisa de espaço para guardar o material (disco livre), de um momento em que ninguém esteja usando o cômodo (reinício) e da autorização do condomínio (políticas da empresa). Se faltar qualquer um, a obra para no meio.

**Sintoma típico:** "a atualização falha sempre", "está há horas em 0%" ou "o Windows pede para reiniciar e volta a pedir".

**Causas mais comuns:** pouco espaço em disco, reinício adiado várias vezes, conexão instável, atualização controlada pela TI (WSUS, Intune) ou arquivos de atualização corrompidos.

> [!NOTE]
> Em computadores corporativos, a TI costuma controlar **quando** e **quais** atualizações instalam. A mensagem "Algumas configurações são gerenciadas pela sua organização" é normal e não é defeito.

## Pergunte primeiro

- Que **mensagem** ou **código de erro** aparece? (ex.: `0x80070070`)
- Desde quando a atualização falha?
- Há quanto tempo o computador não reinicia de verdade?
- O computador está na rede da empresa, em casa ou na VPN?

## Antes de começar

> [!CAUTION]
> **Nunca desligue o computador no botão** enquanto aparece "Trabalhando nas atualizações — não desligue o computador". Interromper essa etapa pode deixar o Windows sem iniciar.

> [!WARNING]
> Não execute "scripts de reset do Windows Update" encontrados na internet. Eles apagam pastas e reconfiguram serviços; isso é tarefa do N2, com autorização.

---

## Passo a passo

### Passo 1 — Registre o código de erro

**Faça:** abra **Configurações → Windows Update** e anote a mensagem e o código. Veja também **Histórico de atualizações**, que mostra o que falhou e quando.

**Por quê:** o código diz muito. `0x80070070`, por exemplo, indica falta de espaço. Sem o código, qualquer ação é chute.

**O que você deve ver:** o nome da atualização que falhou e o código.

### Passo 2 — Reinicie de verdade

**Faça:** combine com o usuário, salve o trabalho e use **Iniciar → Energia → Reiniciar** (não "Desligar").

**Por quê:** com a inicialização rápida ativa, "Desligar" pode não fazer um reinício completo. Muitas atualizações só terminam num reinício real.

**O que você deve ver:** o Windows concluindo a instalação durante o reinício.

### Passo 3 — Libere espaço

**Faça:** confira o espaço livre em **Configurações → Sistema → Armazenamento**.

**Por quê:** atualizações grandes precisam de vários gigabytes temporários para baixar e desempacotar.

**O que você deve ver:** espaço suficiente. Se não, siga o [KB-10](kb-10-pouco-espaco-em-disco.md).

### Passo 4 — Use o solucionador de problemas

**Faça:** em **Configurações → Sistema → Solução de problemas → Outras soluções de problemas**, execute o do **Windows Update** (em versões mais novas, ele pode abrir pelo aplicativo **Obter Ajuda**).

**Por quê:** é uma ferramenta oficial que confere serviços e configurações comuns sem que você precise mexer manualmente.

**O que você deve ver:** um relatório do que foi verificado e se algo foi corrigido.

### Passo 5 — Tente novamente com a rede estável

**Faça:** com cabo ou Wi-Fi estável (de preferência na rede da empresa), clique em **Verificar se há atualizações**.

**Por quê:** downloads interrompidos geram arquivos incompletos. Algumas empresas só distribuem atualizações pela rede interna ou pela VPN.

**O que você deve ver:** download e instalação concluídos.

---

## Como interpretar o resultado

| Se você observar… | Significa… | Faça |
|---|---|---|
| Código `0x80070070` ou aviso de espaço | Falta de espaço | Passo 3 |
| "Reinício necessário" que nunca some | Reinício completo não aconteceu | Passo 2 (Reiniciar, não Desligar) |
| "Gerenciadas pela sua organização" e nada disponível | A TI controla o calendário | Normal; confirme com o N2 se o computador está em dia |
| Mesma atualização falha várias vezes com o mesmo código | Componentes do Update corrompidos | Encaminhe com código e histórico |
| Atualização instalou e algo parou de funcionar | Possível incompatibilidade | Registre e encaminhe; não desinstale por conta própria |

## Como saber que resolveu

- [ ] **Windows Update** mostra "Você está atualizado" (ou a política da empresa confirma o computador em dia).
- [ ] O histórico mostra a atualização como **instalada com êxito**.
- [ ] O computador reinicia normalmente.

## O que anotar no chamado

- [ ] Nome da atualização e código de erro
- [ ] Espaço livre antes e depois
- [ ] Ações feitas (reinício completo, solucionador)
- [ ] Rede usada

## Quando encaminhar ao N2

- Mesmo código depois de reinício, espaço liberado e solucionador.
- Computador que não inicia depois de uma atualização.
- Necessidade de desinstalar atualização ou reparar arquivos do sistema.

## Erros comuns

- **Desligar no botão durante a instalação.**
- **Usar "Desligar" achando que é igual a "Reiniciar".**
- **Rodar comandos de reparo achados na internet** sem autorização.

## Guias relacionados

[KB-10 · Pouco espaço em disco](kb-10-pouco-espaco-em-disco.md) · [KB-09 · Computador lento](kb-09-computador-lento.md) · [KB-26 · Tela azul](kb-26-tela-azul.md)

**Referências oficiais:** [Solucionar problemas de atualização do Windows][wu]

---

[← Anterior: KB-24](kb-24-arquivo-office-bloqueado.md) · [↑ Índice](../README.md#indice) · [Próximo: KB-26 →](kb-26-tela-azul.md)

[wu]: https://support.microsoft.com/pt-br/windows/deployment/updates-lifecycle/troubleshoot-problems-updating-windows

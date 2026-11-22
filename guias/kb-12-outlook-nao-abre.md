# KB-12 · Outlook clássico não abre

[← Índice](../README.md#indice) · **Categoria:** Microsoft 365 · **Quem executa:** N1 com o usuário

> **Em uma frase:** abra o Outlook no **modo seguro** para descobrir se o problema está nas **extras** (suplementos) ou no **núcleo** do programa.

---

## Entenda o problema

O modo seguro é como ligar o carro **sem nenhum acessório** instalado (som, alarme, rastreador). Se o carro liga assim, o problema provavelmente está em um acessório. Se nem assim liga, o problema é mais fundo.

**Sintoma típico:** o Outlook fica em "Processando" ou fecha sozinho ao iniciar.

**Causas mais comuns:** janela de diálogo pendente, suplemento com falha ou perfil com problema.

> [!IMPORTANT]
> **Este guia vale só para o Outlook clássico.** O clássico tem a guia **Arquivo** no canto superior esquerdo. O **novo Outlook** é outro aplicativo e **não** tem modo seguro.

## Pergunte primeiro

- Que mensagem aparece, se aparecer alguma?
- Começou depois de alguma instalação ou atualização?
- O e-mail funciona pelo navegador (webmail)?

## Antes de começar

> [!CAUTION]
> **Não apague arquivos de dados (PST/OST) nem remova o perfil** sem um plano aprovado. Eles podem conter e-mails que não existem em outro lugar.

---

## Passo a passo

### Passo 1 — Confirme a versão e procure janelas ocultas

**Faça:** confirme que é o Outlook clássico. Use `Alt + Tab` para ver se há alguma janela pedindo resposta (ex.: senha da conta, confirmação).

**Por quê:** uma janela escondida pode manter o Outlook "travado" esperando o usuário.

**O que você deve ver:** confirmação de que é o clássico e nenhuma janela pendente — ou uma janela para o usuário responder.

### Passo 2 — Feche o Outlook com segurança

**Faça:** considere rascunhos não salvos, combine com o usuário e feche o Outlook (se não fechar normalmente, use o Gerenciador de Tarefas).

**Por quê:** o modo seguro só funciona se o Outlook não estiver aberto.

**O que você deve ver:** nenhum processo do Outlook em execução.

### Passo 3 — Abra em modo seguro

**Faça:** pressione `Win + R`, digite `outlook.exe /safe` e pressione `Enter`.

**Por quê:** isso abre o Outlook sem suplementos, isolando a causa.

**O que você deve ver:** o Outlook abrindo (com "Modo de Segurança" no título) — ou não abrindo.

### Passo 4 — Registre a diferença

**Faça:** anote se abriu ou não no modo seguro. Se abriu, testar suplementos só com procedimento autorizado, **um por vez**.

**Por quê:** desativar um por vez é a única forma de descobrir **qual** suplemento causa o problema.

**O que você deve ver:** uma comparação clara: normal × seguro.

---

## Como interpretar o resultado

| Se você observar… | Provavelmente significa… | Próximo passo |
|---|---|---|
| **Abre** no modo seguro | Indício de problema em suplemento ou configuração | Teste suplementos um por vez, com autorização |
| **Não abre** nem no modo seguro | O problema é mais profundo (perfil, dados, instalação) | Encaminhe a comparação ao N2 |
| Havia uma janela oculta | O Outlook esperava o usuário | Responda e teste a abertura normal |

> [!NOTE]
> Abrir no modo seguro é **evidência**, não prova. Não identifica sozinho qual suplemento é o culpado.

## Como saber que resolveu

- [ ] O Outlook abre normalmente (não em modo seguro).
- [ ] O usuário envia e recebe uma mensagem de teste.

## O que anotar no chamado

- [ ] Outlook clássico e versão
- [ ] Mensagem ao abrir
- [ ] Resultado: modo normal × modo seguro

## Quando encaminhar ao N2

- Falha mesmo em modo seguro.
- Erro de perfil ou de arquivo de dados.

## Erros comuns

- **Aplicar este guia ao novo Outlook.**
- **Apagar o arquivo OST/PST** "porque ele é recriado".
- **Declarar um suplemento culpado** sem testá-lo isoladamente.

## Guias relacionados

[KB-13 · Outlook não envia ou recebe](kb-13-outlook-nao-envia-recebe.md) · [KB-11 · Aplicativo travado](kb-11-aplicativo-travado.md)

**Referência oficial:** [Outlook clássico não responde ou trava][outlook]

---

[← Anterior: KB-11](kb-11-aplicativo-travado.md) · [↑ Índice](../README.md#indice) · [Próximo: KB-13 →](kb-13-outlook-nao-envia-recebe.md)

[outlook]: https://support.microsoft.com/pt-br/outlook/classic-outlook-not-responding-stuck-at-processing-stopped-working-or-freezes

# KB-24 · Arquivo do Office bloqueado, somente leitura ou perdido

[← Índice](../README.md#indice) · **Categoria:** Microsoft 365 · **Quem executa:** N1 com o usuário

> **Em uma frase:** um arquivo "travado" quase sempre está **aberto em outro lugar**, **protegido de propósito** ou **sem permissão de escrita** — e um arquivo "perdido" quase sempre tem uma **versão anterior** guardada.

---

## Entenda o problema

Pense num **livro de biblioteca**. Se alguém já pegou, você só pode ler a cópia da mesa (somente leitura). Se é um livro raro, a biblioteca deixa ler, mas não rabiscar (modo de exibição protegido). E se você esqueceu sua anotação no livro, talvez a biblioteca tenha uma fotocópia de ontem (histórico de versões).

**Sintomas típicos:**

- "O arquivo está bloqueado para edição por outro usuário."
- O Word ou Excel abre com a faixa amarela **Modo de Exibição Protegido**.
- "Somente leitura" no título da janela.
- "Fechei sem salvar" ou "salvei por cima de algo importante".

**Causas mais comuns:** outra pessoa (ou o próprio usuário, em outra janela ou computador) com o arquivo aberto; arquivo vindo da internet ou de e-mail; permissão só de leitura na pasta; programa fechado de forma inesperada.

## Pergunte primeiro

- Onde o arquivo está? (computador, pasta de rede, OneDrive, SharePoint/Teams, anexo de e-mail)
- Qual é a **mensagem exata**?
- Mais alguém pode estar com o arquivo aberto?
- Se for perda: quando foi a última vez que você viu a versão certa?

## Antes de começar

> [!CAUTION]
> **Não clique em "Habilitar Edição" em arquivos de origem desconhecida.** O Modo de Exibição Protegido existe para impedir que um anexo malicioso execute código. Se o arquivo veio de um e-mail estranho, veja o [KB-30](kb-30-email-suspeito.md).

> [!WARNING]
> Em caso de perda, **pare de salvar no mesmo arquivo** até tentar recuperar. Cada salvamento pode empurrar a versão boa para mais longe.

---

## Passo a passo

### Passo 1 — Leia de onde vem o bloqueio

**Faça:** leia a mensagem completa. Muitas vezes ela informa **quem** está com o arquivo aberto.

**Por quê:** "bloqueado por Fulano" resolve-se falando com Fulano. "Bloqueado por você mesmo" significa outra janela ou outro computador seu.

**O que você deve ver:** o nome de quem mantém o arquivo aberto, ou nenhum nome.

### Passo 2 — Feche cópias abertas

**Faça:** peça para o usuário fechar o arquivo em todas as janelas e computadores. Se o nome é do próprio usuário e nada está aberto, confira no Gerenciador de Tarefas se há processo do Word/Excel em segundo plano e combine antes de encerrá-lo.

**Por quê:** um programa fechado de forma inesperada pode continuar "segurando" o arquivo. Encerrar o processo libera o bloqueio.

**O que você deve ver:** o arquivo abrindo para edição.

### Passo 3 — Prefira coautoria na nuvem

**Faça:** se o arquivo é usado por várias pessoas, oriente a trabalhar nele a partir do OneDrive/SharePoint/Teams (abrindo pelo próprio Office ou pela web).

**Por quê:** em pastas de rede comuns, só uma pessoa edita por vez. Na nuvem, várias pessoas editam ao mesmo tempo (coautoria) sem bloqueio.

**O que você deve ver:** os nomes ou fotos dos colegas aparecendo no topo do documento.

### Passo 4 — Modo de Exibição Protegido: decida com critério

**Faça:** se o arquivo é de origem **conhecida e esperada**, o usuário pode clicar em **Habilitar Edição**. Se houver dúvida, não habilite e confirme com o remetente por outro canal.

**Por quê:** a proteção não é defeito; é o Office avisando que o arquivo veio de fora. A decisão de confiar é sobre a **origem**, não sobre o arquivo parecer normal.

**O que você deve ver:** a faixa amarela sumindo após habilitar (para arquivos confiáveis).

### Passo 5 — Recupere versões anteriores

**Faça:** conforme o local do arquivo:

- **OneDrive/SharePoint/Teams:** clique com o botão direito no arquivo → **Histórico de versões**.
- **Office fechou sem salvar:** no programa, **Arquivo → Informações → Gerenciar Documento → Recuperar Documentos Não Salvos** (no Excel, "Pastas de Trabalho").
- **Pasta de rede:** botão direito → **Propriedades → Versões Anteriores**, se a TI habilitou esse recurso.

**Por quê:** esses serviços guardam cópias automáticas. Recuperar uma versão é muito mais seguro do que tentar "reconstruir" o arquivo.

**O que você deve ver:** uma lista de versões com data e hora. Abra a versão antes de restaurar para conferir com o usuário.

---

## Como interpretar o resultado

| Se você observar… | Significa… | Faça |
|---|---|---|
| "Bloqueado por [outra pessoa]" | Outra pessoa está editando | Combine com ela ou use coautoria (Passo 3) |
| "Bloqueado por [o próprio usuário]" | Cópia aberta em outro lugar ou processo preso | Passo 2 |
| Faixa amarela "Modo de Exibição Protegido" | Arquivo veio da internet/e-mail | Passo 4, com critério |
| "Somente leitura" em pasta de rede | Permissão só de leitura ou arquivo marcado como somente leitura | Encaminhe ao responsável pela pasta se precisa editar |
| Sem histórico de versões disponível | O local não guarda versões | Encaminhe ao N2 (backup) com nome, local e data aproximada |

## Como saber que resolveu

- [ ] O usuário abre o arquivo e **salva** uma alteração de teste.
- [ ] Em caso de recuperação: o usuário confirma que a versão restaurada é a correta.

## O que anotar no chamado

- [ ] Local do arquivo (sem expor conteúdo)
- [ ] Mensagem exata
- [ ] Versão recuperada (data/hora) e confirmação do usuário
- [ ] Ações feitas

## Quando encaminhar ao N2

- Restauração de backup de servidor.
- Permissão de escrita em pasta ou biblioteca.
- Arquivo corrompido que não abre em nenhuma versão.

## Erros comuns

- **Habilitar edição em qualquer anexo** só para "fazer funcionar".
- **Apagar o arquivo `~$nome.docx`** com o documento ainda aberto em outro lugar. Esse arquivo temporário é o "aviso de ocupado" do Office; ele some sozinho quando o documento é fechado.
- **Restaurar sem conferir** a versão com o usuário.

## Guias relacionados

[KB-11 · Aplicativo travado](kb-11-aplicativo-travado.md) · [KB-22 · OneDrive](kb-22-onedrive-sincronizacao.md) · [KB-23 · Pasta de rede](kb-23-pasta-de-rede.md) · [KB-30 · E-mail suspeito](kb-30-email-suspeito.md)

**Referências oficiais:** [Suporte do Microsoft 365][office]

---

[← Anterior: KB-23](kb-23-pasta-de-rede.md) · [↑ Índice](../README.md#indice) · [Próximo: KB-25 →](kb-25-windows-update.md)

[office]: https://support.microsoft.com/pt-br/microsoft-365

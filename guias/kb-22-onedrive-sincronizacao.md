# KB-22 · OneDrive não sincroniza

[← Índice](../README.md#indice) · **Categoria:** Microsoft 365 · **Quem executa:** N1 com o usuário (redefinir o OneDrive exige combinar antes)

> **Em uma frase:** o OneDrive quase sempre **diz** o que está errado — leia o ícone e a mensagem antes de mexer em qualquer coisa.

---

## Entenda o problema

O OneDrive é um **carteiro que vive indo e voltando** entre o seu computador e a nuvem, levando cópias atualizadas dos arquivos. Se uma carta tem endereço inválido (nome com caractere proibido), é pesada demais ou o carteiro está de folga (sincronização pausada), a entrega para — às vezes só daquela carta, às vezes de todas.

**Sintoma típico:** "salvei no computador e não aparece no outro", "o colega não vê minha alteração", ícone com **X vermelho** ou sincronização que nunca termina.

**Causas mais comuns:** sincronização pausada, conta desconectada, nome ou caminho de arquivo inválido, falta de espaço (no disco ou na nuvem) e arquivo aberto por outro programa.

### Os ícones que você precisa reconhecer

| Ícone ao lado do arquivo | Significa |
|---|---|
| ☁️ Nuvem | Existe só na nuvem; baixa quando você abrir |
| ✅ Contorno verde | Disponível no computador (já foi baixado) |
| 🟢 Círculo verde preenchido | Marcado para ficar **sempre** no computador |
| 🔄 Setas circulares | Sincronizando agora |
| ❌ X vermelho | **Erro** — esse arquivo ou pasta não sincroniza |
| 👥 Pessoas | Arquivo compartilhado com outras pessoas |

## Pergunte primeiro

- O problema é com **um arquivo**, **uma pasta** ou **tudo**?
- O ícone do OneDrive perto do relógio aparece? Tem algum símbolo (pausa, X, aviso)?
- O arquivo aparece em `onedrive.com` (navegador)?
- O arquivo estava aberto quando você salvou?
- Mudou algo? (troca de senha, computador novo, pasta renomeada)

## Antes de começar

> [!CAUTION]
> **Nunca apague a pasta do OneDrive nem "desvincule e apague"** para resolver. Arquivos que só existem no computador podem ser perdidos. Antes de qualquer redefinição, confirme que os arquivos importantes estão na web.

---

## Passo a passo

### Passo 1 — Leia o ícone da bandeja

**Faça:** clique no ícone de nuvem do OneDrive perto do relógio e leia a mensagem no topo do painel.

**Por quê:** o OneDrive mostra estados como "Sincronização pausada", "Você não está conectado" ou "X itens não puderam ser sincronizados". Essa frase já aponta o passo certo.

**O que você deve ver:** uma das mensagens da tabela de interpretação ou "Seus arquivos estão sincronizados".

### Passo 2 — Compare com a web

**Faça:** abra `onedrive.com` (ou o SharePoint da equipe) e procure o arquivo.

**Por quê:** separa "não subiu do computador" de "subiu, mas o outro computador não baixou". São problemas em lados opostos da estrada.

**O que você deve ver:** o arquivo na web com a data de alteração esperada (ou não).

### Passo 3 — Retome a sincronização e confira a conta

**Faça:** no painel, se estiver pausado, clique em **Retomar sincronização**. Se pedir login, peça para o usuário entrar com a conta da empresa.

**Por quê:** pausas acontecem de propósito (modo economia de bateria, rede limitada) e esquecidas. Uma troca de senha também desconecta o OneDrive até um novo login.

**O que você deve ver:** as setas de sincronização girando e o contador de arquivos diminuindo.

### Passo 4 — Corrija o arquivo problemático

**Faça:** abra **Exibir problemas de sincronização** no painel e verifique o motivo de cada item. Os mais comuns: caractere proibido no nome (`" * : < > ? / \ |`), caminho longo demais (pastas dentro de pastas) e arquivo aberto em outro programa.

**Por quê:** um único arquivo com problema mostra o X vermelho, mas os outros continuam sincronizando. Corrigir o nome ou fechar o programa resolve aquele item sem mexer em nada mais.

**O que você deve ver:** o X sumindo depois de renomear ou fechar o arquivo.

### Passo 5 — Verifique o espaço

**Faça:** confira o espaço livre no disco (Configurações → Sistema → Armazenamento) e na nuvem (Configurações do OneDrive → Conta).

**Por quê:** sem espaço no destino, o carteiro não tem onde deixar a carta.

**O que você deve ver:** espaço disponível nos dois lados. Se o disco está cheio, veja o [KB-10](kb-10-pouco-espaco-em-disco.md).

### Passo 6 — Redefina o OneDrive (último recurso, com combinação)

**Faça:** com os arquivos importantes confirmados na web, execute em `Win + R`: `%localappdata%\Microsoft\OneDrive\onedrive.exe /reset`. Se o ícone não voltar em alguns minutos, abra o OneDrive pelo menu Iniciar.

**Por quê:** a redefinição apaga só o "caderno de controle" do OneDrive e força uma nova comparação de tudo. Não apaga arquivos, mas a ressincronização pode demorar e algumas configurações voltam ao padrão.

**O que você deve ver:** o OneDrive recomeçando a sincronização.

---

## Como interpretar o resultado

| Mensagem ou sinal | Significa… | Faça |
|---|---|---|
| "Sincronização pausada" | Alguém (ou o modo economia) pausou | Passo 3 |
| "Você não está conectado" / pede login | Sessão expirou, geralmente após troca de senha | Passo 3 |
| X vermelho em um item | Problema **naquele** arquivo | Passo 4 |
| Arquivo na web, mas não no outro computador | O problema está no computador que **baixa** | Repita os passos no outro computador |
| "Armazenamento cheio" | Sem espaço no disco ou na nuvem | Passo 5 |
| Conflito: aparecem duas cópias com o nome do computador | Duas pessoas editaram ao mesmo tempo offline | Compare as versões com o usuário antes de apagar qualquer uma |

## Como saber que resolveu

- [ ] O painel mostra "Seus arquivos estão sincronizados".
- [ ] O arquivo do chamado aparece na web com a versão correta.
- [ ] Outra pessoa (ou outro computador) abre a versão atualizada.

## O que anotar no chamado

- [ ] Mensagem exata do painel do OneDrive
- [ ] Nome do arquivo ou pasta afetada (sem conteúdo sensível)
- [ ] Resultado da comparação com a web
- [ ] Ação feita (retomar, renomear, redefinir) e resultado

## Quando encaminhar ao N2

- Erros de permissão em bibliotecas do SharePoint.
- Cota da nuvem esgotada que exige aumento.
- Falha persistente após redefinição.
- Suspeita de perda de dados (arquivos sumiram) — **não tente "consertar"** antes de acionar o N2.

## Erros comuns

- **Apagar a pasta local para "baixar de novo".** Arquivos que não subiram se perdem.
- **Apagar uma das cópias de conflito sem comparar.** Pode ser a versão boa.
- **Achar que "nuvem" no ícone é erro.** Só significa que o arquivo não foi baixado ainda.

## Guias relacionados

[KB-10 · Pouco espaço em disco](kb-10-pouco-espaco-em-disco.md) · [KB-24 · Arquivo do Office bloqueado](kb-24-arquivo-office-bloqueado.md) · [KB-23 · Pasta de rede](kb-23-pasta-de-rede.md)

**Referências oficiais:** [Corrigir problemas de sincronização do OneDrive][onedrive]

---

[← Anterior: KB-21](kb-21-teams-reuniao.md) · [↑ Índice](../README.md#indice) · [Próximo: KB-23 →](kb-23-pasta-de-rede.md)

[onedrive]: https://support.microsoft.com/pt-br/onedrive/fix-onedrive-sync-problems

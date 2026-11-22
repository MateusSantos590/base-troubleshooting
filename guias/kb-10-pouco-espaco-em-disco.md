# KB-10 · Pouco espaço em disco

[← Índice](../README.md#indice) · **Categoria:** Windows · **Quem executa:** N1 com o usuário

> **Em uma frase:** o disco encheu. Libere espaço **com o usuário**, removendo só o que foi entendido e autorizado.

---

## Entenda o problema

O disco é a despensa da casa. Quando enche, não cabe compra nova (arquivo, instalação, atualização). A tentação é jogar fora o que parece velho, mas **só o dono sabe o que pode ir para o lixo**. Uma "faxina" sem perguntar pode apagar algo importante.

**Sintoma típico:** salvar, instalar ou atualizar falha por falta de espaço.

**Causas mais comuns:** arquivos grandes acumulados (vídeos, downloads, cópias) ou arquivos temporários.

## Pergunte primeiro

- Em qual unidade aparece o aviso? (C:, D:…)
- O que você estava tentando salvar ou instalar?
- Você usa OneDrive ou outra pasta sincronizada com a nuvem?

## Antes de começar

> [!CAUTION]
> **Nunca apague pastas do sistema ou arquivos pessoais sem autorização.** A pasta Downloads e a Lixeira podem conter material necessário. Em pastas sincronizadas, apagar localmente pode **apagar também na nuvem**.

---

## Passo a passo

### Passo 1 — Veja o que ocupa espaço

**Faça:** abra **Configurações → Sistema → Armazenamento**. Identifique a unidade cheia e as categorias que mais ocupam.

**Por quê:** você precisa saber **onde** está o volume antes de decidir o que fazer. Às vezes a unidade cheia nem é a do sistema.

**O que você deve ver:** a unidade afetada e as categorias maiores.

### Passo 2 — Revise com o usuário

**Faça:** mostre ao usuário as categorias e pastas grandes e pergunte o que pode ser removido ou movido.

**Por quê:** o técnico não sabe se aquele vídeo de 4 GB é lixo ou a gravação de uma reunião importante.

**O que você deve ver:** uma lista do que o usuário **autorizou** remover.

### Passo 3 — Use a limpeza nativa do Windows

**Faça:** na mesma tela de Armazenamento, use **Arquivos temporários** e marque **apenas** as categorias compreendidas e aprovadas.

**Por quê:** a limpeza nativa sabe o que é seguro remover. Ferramentas de terceiros podem apagar demais.

**O que você deve ver:** espaço liberado sem afetar dados do usuário.

### Passo 4 — Mova dados para local autorizado

**Faça:** se for preciso mover arquivos grandes, use um destino **autorizado** pela empresa e **confirme que a cópia está completa** antes de apagar o original.

**Por quê:** mover sem conferir é a forma mais comum de perder arquivos.

**O que você deve ver:** arquivos no novo local, abrindo normalmente.

---

## Como interpretar o resultado

| Se você observar… | Provavelmente significa… | Próximo passo |
|---|---|---|
| A unidade cheia **não é** a C: | O problema é em outra unidade | Limpar a C: não resolve; atue na unidade certa |
| Muito espaço em pasta sincronizada | Arquivos da nuvem baixados localmente | Distinga "liberar espaço local" de "apagar da nuvem" |
| O espaço volta a encher rapidamente | Algo está gerando arquivos sem parar | Encaminhe ao N2 |
| Dados com regras de retenção | Não podem ser apagados por decisão do N1 | Encaminhe |

## Como saber que resolveu

- [ ] Há espaço livre suficiente.
- [ ] A tarefa original (salvar, instalar, atualizar) foi concluída.

## O que anotar no chamado

- [ ] Unidade afetada
- [ ] Espaço livre antes e depois
- [ ] Categorias removidas (sem listar nomes de arquivos pessoais)
- [ ] Resultado da tarefa original

## Quando encaminhar ao N2

- Crescimento de espaço sem explicação.
- Dados sujeitos a regras de retenção.

## Erros comuns

- **Esvaziar Downloads e Lixeira sem perguntar.**
- **Apagar pasta sincronizada achando que é só local.**
- **Mover arquivos sem conferir a cópia.**

## Guias relacionados

[KB-09 · Computador lento](kb-09-computador-lento.md)

**Referência oficial:** [Dicas para melhorar o desempenho do Windows][desempenho]

---

[← Anterior: KB-09](kb-09-computador-lento.md) · [↑ Índice](../README.md#indice) · [Próximo: KB-11 →](kb-11-aplicativo-travado.md)

[desempenho]: https://support.microsoft.com/en-us/windows/experience/performance-optimization/tips-to-improve-pc-performance-in-windows

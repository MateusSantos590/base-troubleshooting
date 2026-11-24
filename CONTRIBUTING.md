# Como contribuir

[← Voltar ao início](README.md)

Obrigado por querer melhorar esta base! Toda correção, por menor que seja, ajuda quem está aprendendo.

> [!CAUTION]
> **Este repositório é público.** Nunca inclua dados reais de atendimento: nomes, e-mails, endereços IP internos, URLs com tokens, prints de telas corporativas ou saídas de comandos de redes reais. Issues **não são canal de suporte**.

---

## Formas de contribuir

| Você quer… | Como fazer |
|---|---|
| Apontar um erro ou trecho confuso | Abra uma [issue](https://github.com/MateusSantos590/base-troubleshooting/issues/new/choose) com o modelo **Correção na documentação** |
| Sugerir um termo para o glossário | Abra uma issue informando o termo e onde ele aparece |
| Sugerir uma mensagem de erro | Abra uma issue com o texto ou código exato (sem dados reais) e a fonte oficial que explica o significado |
| Propor um caso prático | Descreva o chamado como o usuário contaria, a primeira pergunta, o raciocínio e o guia de destino |
| Registrar um teste de laboratório | Use o [registro de execução](docs/VALIDACAO.md#registro-de-execução--copiar-por-cenário), com dados fictícios ou anonimizados |
| Corrigir o texto você mesmo | Faça um fork, altere e abra um pull request |

## O que informar numa sugestão

1. **ID do guia** (ex.: KB-07) e o trecho.
2. **O problema:** o que está errado, confuso ou desatualizado.
3. **A proposta:** como deveria ficar.
4. **A fonte:** uma referência pública (de preferência documentação oficial).

## Padrão de escrita dos guias

Todo guia em `guias/` segue o mesmo molde. O script de verificação **reprova** guias sem estas seções (títulos `##`):

```text
## Entenda o problema
## Pergunte primeiro
## Antes de começar
## Passo a passo
## Como interpretar o resultado
## Como saber que resolveu
## O que anotar no chamado
## Quando encaminhar ao N2
## Erros comuns
```

**Regras de estilo:**

- **Frases curtas**, voz ativa, linguagem simples. Escreva para quem está no primeiro mês de suporte.
- **Cada passo tem três partes:** *Faça*, *Por quê* e *O que você deve ver*.
- **Termo técnico novo?** Explique na primeira vez que aparecer ou adicione ao [glossário](docs/GLOSSARIO.md).
- **Uma ideia por passo.** Se o passo tem "e depois", provavelmente são dois passos.
- **Nunca apresente hipótese como causa.** Use "provavelmente", "indica", "sugere" quando não houver confirmação.
- **Segurança em primeiro lugar:** nenhum passo pode pedir senha, código de MFA ou desativar proteções.
- **Avisos** usam os alertas do GitHub: `> [!NOTE]`, `> [!TIP]`, `> [!IMPORTANT]`, `> [!WARNING]`, `> [!CAUTION]`.

## Antes de enviar

Rode a verificação localmente (precisa apenas do Python 3.8 ou superior):

```bash
python3 scripts/verificar_links.py
```

O resultado esperado é uma linha começando com `✓`. A mesma verificação roda automaticamente no GitHub a cada alteração.

## Mensagens de commit

Use o padrão `tipo: descrição curta`, por exemplo:

- `docs: corrigir caminho de configuração no KB-18`
- `docs: adicionar termo VLAN ao glossário`
- `ci: ajustar verificação de links`

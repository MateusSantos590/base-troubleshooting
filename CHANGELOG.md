# Histórico de versões

[← Voltar ao início](README.md)

Todas as mudanças relevantes desta base estão registradas aqui.

## 2.0 — 22/11/2026

Reestruturação didática completa. O conteúdo técnico e as precauções da versão 1.1 foram mantidos; a forma de apresentar mudou.

**Adicionado**

- Um arquivo por guia em `guias/`, todos no mesmo molde: *em uma frase*, analogia, perguntas iniciais, passos com **Faça / Por quê / O que você deve ver**, tabela de interpretação, checklists de validação e de evidências, erros comuns e navegação anterior/próximo.
- [`docs/METODO.md`](docs/METODO.md): o raciocínio de diagnóstico em 6 passos, triagem e regras de segurança.
- [`docs/GLOSSARIO.md`](docs/GLOSSARIO.md): mais de 80 termos técnicos explicados com analogias.
- [`docs/COMANDOS.md`](docs/COMANDOS.md): `ipconfig`, `nslookup` e `ping` explicados, com exemplos de saída e como interpretá-los.
- Fluxograma "Qual guia usar?" e trilha "Comece aqui" no README.
- Verificação automática de links, âncoras e molde dos guias ([`scripts/verificar_links.py`](scripts/verificar_links.py)), executada no GitHub Actions.
- [`CONTRIBUTING.md`](CONTRIBUTING.md) e modelo de issue para correções.

**Alterado**

- README reduzido a uma porta de entrada: apresentação, trilha, fluxograma e índice.
- `docs/MODELO_CHAMADO.md` e `docs/VALIDACAO.md` ganharam introdução e roteiro de uso; os links apontam para os novos arquivos de guia.
- As âncoras antigas (`README.md#kb-01` a `#kb-20`) continuam existindo no índice, para não quebrar links já compartilhados.

**Não alterado**

- Nenhum cenário foi executado em laboratório. Todos permanecem **Não executado**.

## 1.1 — 10/11/2026

- Interpretação de testes e evidência mínima em cada guia.
- Pontos de entrada, critérios de encerramento e de encaminhamento ao N2.
- Modelos separados de chamado e de laboratório; referências adicionais.

## 1.0 — 10/11/2026

- 20 guias, índice, referências e modelo curto de chamado.

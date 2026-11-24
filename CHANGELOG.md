# Histórico de versões

[← Voltar ao início](README.md)

Todas as mudanças relevantes desta base estão registradas aqui.

## 3.0 — 24/11/2026

Expansão de conteúdo: mais problemas cobertos e material de apoio para consulta rápida e treino. O molde dos guias e as regras de segurança não mudaram.

**Adicionado**

- 12 novos guias, no mesmo molde dos anteriores:
  - [KB-21](guias/kb-21-teams-reuniao.md) Teams não abre ou não entra na reunião
  - [KB-22](guias/kb-22-onedrive-sincronizacao.md) OneDrive não sincroniza
  - [KB-23](guias/kb-23-pasta-de-rede.md) Pasta de rede ou unidade mapeada não abre
  - [KB-24](guias/kb-24-arquivo-office-bloqueado.md) Arquivo do Office bloqueado, somente leitura ou perdido
  - [KB-25](guias/kb-25-windows-update.md) Windows Update falha
  - [KB-26](guias/kb-26-tela-azul.md) Tela azul ou reinício inesperado
  - [KB-27](guias/kb-27-computador-nao-liga.md) Computador não liga ou não dá imagem
  - [KB-28](guias/kb-28-notebook-nao-carrega.md) Notebook não carrega ou bateria dura pouco
  - [KB-29](guias/kb-29-mfa-autenticador.md) MFA: celular novo, código recusado ou aprovação não solicitada
  - [KB-30](guias/kb-30-email-suspeito.md) E-mail suspeito (phishing) e o que fazer se clicou
  - [KB-31](guias/kb-31-webcam.md) Webcam não funciona
  - [KB-32](guias/kb-32-sem-som.md) Sem som no alto-falante ou fone
- [`docs/MENSAGENS_DE_ERRO.md`](docs/MENSAGENS_DE_ERRO.md): dicionário de códigos e mensagens (HTTP, navegador, Entra ID `AADSTS`, pastas de rede, VPN nativa, Outlook e NDR, impressão, Gerenciador de Dispositivos, Windows Update, tela azul), cada um ligado ao guia certo.
- [`docs/DICAS.md`](docs/DICAS.md): ferramentas nativas do Windows, atalhos de teclado, truques de diagnóstico, dicas por categoria, checklist do primeiro minuto e mitos do suporte.
- [`docs/COMUNICACAO.md`](docs/COMUNICACAO.md): o que dizer em cada momento do atendimento, tradução de jargão, situações difíceis e modelos por canal.
- [`docs/CASOS_PRATICOS.md`](docs/CASOS_PRATICOS.md): 8 chamados fictícios misturados, do básico ao avançado, com gabarito recolhível.
- [`docs/COMANDOS.md`](docs/COMANDOS.md): `tracert`, `Test-NetConnection`, `net use`, `whoami`, `winver`/`systeminfo`, `powercfg /batteryreport` e `perfmon /rel`.
- Glossário com cerca de 30 termos novos (tela azul, BitLocker, phishing, engenharia social, acesso condicional, OneDrive, coautoria, NDR e outros).

**Alterado**

- README: fluxograma "Qual guia usar?" cobre Microsoft 365, hardware e segurança; índice com os 32 guias, tabela por categoria e seção "Material de apoio"; trilha "Comece aqui" ganhou o passo de casos práticos.
- Plano de validação: 12 cenários novos (KB-21 a KB-32). A seção passou a se chamar "Roteiro dos cenários".
- KB-20 aponta para o KB-21 na navegação.

**Não alterado**

- Nenhum cenário foi executado em laboratório. Todos permanecem **Não executado**.

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

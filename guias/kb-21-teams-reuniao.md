# KB-21 · Teams não abre ou não entra na reunião

[← Índice](../README.md#indice) · **Categoria:** Microsoft 365 · **Quem executa:** N1 com o usuário (limpar cache exige combinar antes)

> **Em uma frase:** antes de mexer no aplicativo, descubra se o problema é **do Teams instalado**, **da conta** ou **do serviço** — o Teams na web responde essa pergunta em um minuto.

---

## Entenda o problema

Pense no Teams como um **aplicativo de entrega de comida**. Se o pedido não chega, a falha pode estar em três lugares: o **seu celular** (app travado), o **seu cadastro** (conta sem acesso) ou o **restaurante** (serviço fora do ar). Abrir o mesmo pedido pelo site separa o celular do resto.

```mermaid
flowchart LR
    A["Teams instalado<br/>(computador)"] --> B["Conta<br/>(login e licença)"] --> C["Serviço<br/>(Microsoft 365)"] --> D["Reunião<br/>funciona"]
```

**Sintoma típico:** o Teams fica na tela de carregamento, abre em branco, pede login sem parar ou não deixa entrar numa reunião específica.

**Causas mais comuns:** cache local corrompido, sessão expirada, rede bloqueando o serviço, link de reunião de outra organização com regras diferentes, ou indisponibilidade do serviço.

> [!NOTE]
> Desde 2024 a Microsoft substituiu o **Teams clássico** pelo **novo Teams**. Os caminhos de configuração e de cache mudaram. Este guia considera o novo Teams no Windows 11.

## Pergunte primeiro

- O Teams **não abre de jeito nenhum** ou abre mas **uma reunião específica** não entra?
- Aparece alguma **mensagem ou código de erro**? (peça foto ou o texto exato)
- Colegas estão conseguindo usar o Teams agora?
- A reunião é da sua empresa ou de **outra organização** (cliente, fornecedor)?
- Mudou algo? (senha nova, computador novo, atualização)

## Antes de começar

> [!CAUTION]
> **Nunca peça a senha nem o código do autenticador** para "logar por ele". Quem digita é sempre o usuário.

> [!WARNING]
> Limpar o cache **fecha o Teams** e apaga preferências locais (tema, alguns ajustes). Combine antes com o usuário, principalmente se ele estiver prestes a entrar numa reunião.

---

## Passo a passo

### Passo 1 — Teste o Teams na web

**Faça:** peça para o usuário abrir `teams.microsoft.com` no navegador e entrar com a conta da empresa.

**Por quê:** é o teste que mais corta o problema pela metade. Se a web funciona, conta e serviço estão bem — o defeito está no aplicativo instalado. Se a web também falha, não adianta reinstalar nada.

**O que você deve ver:** a web funcionando (→ foco no aplicativo) ou falhando também (→ conta, rede ou serviço).

### Passo 2 — Verifique se é geral

**Faça:** pergunte a um colega ou consulte o canal de comunicados da TI. Administradores podem consultar a saúde do serviço no centro de administração do Microsoft 365.

**Por quê:** se dez pessoas estão sem Teams, o problema é do serviço ou da rede, e mexer no computador de uma pessoa só gasta tempo.

**O que você deve ver:** se há incidente conhecido.

### Passo 3 — Saia e entre de novo na conta

**Faça:** no Teams, clique na foto do perfil → **Sair**. Feche o aplicativo e abra de novo, entrando com a conta da empresa.

**Por quê:** a sessão (o "crachá" que o Teams guarda) pode ter expirado ou ficado inconsistente depois de uma troca de senha.

**O que você deve ver:** o Teams carregando normalmente após o novo login.

### Passo 4 — Limpe o cache do novo Teams (com combinação)

**Faça:** feche o Teams completamente (inclusive pelo ícone perto do relógio). Em `Win + R`, abra `%localappdata%\Packages\MSTeams_8wekyb3d8bbwe\LocalCache\Microsoft\MSTeams` e apague o **conteúdo** dessa pasta. Abra o Teams de novo.

**Por quê:** o cache guarda pedaços da interface e da sessão para abrir mais rápido. Se ficou corrompido, o app tenta usar dados quebrados e trava na abertura. Apagar força o Teams a baixar tudo de novo. Conversas e arquivos **não** ficam no cache — estão no serviço.

**O que você deve ver:** a primeira abertura um pouco mais lenta e, depois, o Teams funcionando.

### Passo 5 — Se o problema é numa reunião: áudio e vídeo

**Faça:** em **Configurações → Dispositivos**, confira alto-falante, microfone e câmera selecionados e use **Fazer uma chamada de teste**.

**Por quê:** "não consigo entrar" muitas vezes é "entrei, mas ninguém me ouve". A chamada de teste separa o problema de dispositivo do problema da reunião.

**O que você deve ver:** a gravação de teste tocando com sua voz. Se não, vá para [KB-18](kb-18-microfone.md), [KB-31](kb-31-webcam.md) ou [KB-32](kb-32-sem-som.md).

---

## Como interpretar o resultado

| Se você observar… | Significa… | Faça |
|---|---|---|
| Web funciona, aplicativo não | Defeito local do aplicativo | Passos 3 e 4; se persistir, reinstalação pelo canal oficial (N2 conforme política) |
| Web e aplicativo falham, colegas também | Serviço ou rede | Verifique incidente; não mexa no computador |
| Web e aplicativo falham, só esse usuário | Conta (licença, bloqueio, política) | [KB-16](kb-16-conta-bloqueada.md) ou encaminhe para identidade |
| Só reuniões de **outra empresa** falham | Regras da organização externa ou acesso de convidado | Entre pela web ou como convidado; encaminhe se necessário |
| Entra, mas sem som ou imagem | Dispositivo ou permissão | Passo 5 |

## Como saber que resolveu

- [ ] O Teams abre e mostra conversas e calendário.
- [ ] O usuário entra na reunião que motivou o chamado (ou numa reunião de teste).
- [ ] Os participantes ouvem e veem o usuário, se essa era a queixa.

## O que anotar no chamado

- [ ] Versão do Teams (novo × clássico) e mensagem exata de erro
- [ ] Resultado do teste na web
- [ ] Se havia outros usuários afetados
- [ ] Ações feitas (saída de conta, limpeza de cache) e resultado

## Quando encaminhar ao N2

- Falha também na web para um usuário só (provável licença ou política).
- Falha persistente após limpar cache e reentrar.
- Mensagens sobre política, conformidade do dispositivo ou acesso condicional.

## Erros comuns

- **Reinstalar o Teams antes de testar a web.** Se a web também falha, a reinstalação não resolve.
- **Apagar a pasta errada.** Apague só o conteúdo da pasta de cache do novo Teams, com o aplicativo fechado.
- **Confundir "não entra" com "entra sem áudio".** São caminhos diferentes.

## Guias relacionados

[KB-18 · Microfone](kb-18-microfone.md) · [KB-31 · Webcam](kb-31-webcam.md) · [KB-32 · Sem som](kb-32-sem-som.md) · [KB-29 · MFA](kb-29-mfa-autenticador.md)

**Referências oficiais:** [Suporte do Microsoft Teams][teams]

---

[← Anterior: KB-20](kb-20-sistema-web.md) · [↑ Índice](../README.md#indice) · [Próximo: KB-22 →](kb-22-onedrive-sincronizacao.md)

[teams]: https://support.microsoft.com/pt-br/teams

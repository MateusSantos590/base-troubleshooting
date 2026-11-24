# KB-31 · Webcam não funciona

[← Índice](../README.md#indice) · **Categoria:** Periféricos · **Quem executa:** N1 com o usuário

> **Em uma frase:** a imagem passa pelas mesmas três portas do microfone — **dispositivo**, **Windows** e **aplicativo** — com uma porta extra muito comum: a **tampinha física** da câmera.

---

## Entenda o problema

A câmera é como uma **janela com várias persianas**. Pode estar fechada por uma tampa física, por uma tecla do teclado, pelas permissões de privacidade do Windows ou pelo próprio aplicativo. E só uma pessoa pode olhar pela janela de cada vez: se outro programa está usando a câmera, os outros não conseguem.

```mermaid
flowchart LR
    A["Câmera física<br/>(tampa, tecla)"] --> B["Windows<br/>(privacidade, driver)"] --> C["Aplicativo<br/>(câmera escolhida)"] --> D["Imagem<br/>na reunião"]
```

**Sintoma típico:** tela preta no lugar do vídeo, ícone de câmera riscado ou mensagem "não encontramos sua câmera".

**Causas mais comuns:** tampa de privacidade fechada, tecla de câmera desativada, permissão negada, outro programa usando a câmera, câmera errada selecionada (externa × integrada).

## Pergunte primeiro

- A câmera é **integrada** (do notebook) ou **externa** (USB)?
- Funciona em algum aplicativo e não em outro?
- Aparece uma **luzinha** ao lado da câmera quando ela deveria estar ligada?
- Mudou algo? (dock novo, atualização, câmera nova)

## Antes de começar

> [!NOTE]
> Para testar, use o aplicativo **Câmera** do Windows ou a chamada de teste do Teams. Não grave imagens do usuário ou do ambiente como evidência.

---

## Passo a passo

### Passo 1 — Confira a tampa e a tecla

**Faça:** verifique se há uma **tampa deslizante** sobre a lente e se o teclado tem uma tecla com ícone de câmera (geralmente entre as teclas F1–F12) que liga e desliga a câmera.

**Por quê:** muitos notebooks têm bloqueio físico de privacidade. Com ele fechado, a câmera até aparece no Windows, mas mostra imagem preta ou nenhuma imagem.

**O que você deve ver:** lente desobstruída e câmera habilitada pela tecla.

### Passo 2 — Teste no aplicativo Câmera do Windows

**Faça:** abra o aplicativo **Câmera** pelo menu Iniciar.

**Por quê:** é o teste mais direto da porta "Windows". Se funciona aqui, o problema está no aplicativo da reunião.

**O que você deve ver:** sua imagem na tela (→ foco no aplicativo) ou uma mensagem de erro (→ foco no Windows ou no dispositivo).

### Passo 3 — Verifique a privacidade do Windows

**Faça:** em **Configurações → Privacidade e segurança → Câmera**, confirme que o **acesso à câmera** está ativado e que o aplicativo usado (Teams, navegador) tem permissão.

**Por quê:** o Windows pode bloquear a câmera para todos ou para aplicativos específicos. Sem permissão, o app simplesmente não vê a câmera.

**O que você deve ver:** acesso ativado para o aplicativo necessário.

### Passo 4 — Feche outros programas que usam a câmera

**Faça:** feche outros aplicativos de reunião, abas de navegador com videochamada e o aplicativo Câmera.

**Por quê:** em geral, apenas um programa usa a câmera por vez. Um Teams minimizado ou uma aba esquecida podem estar "segurando" a câmera.

**O que você deve ver:** a câmera funcionando no aplicativo desejado.

### Passo 5 — Escolha a câmera certa no aplicativo

**Faça:** nas configurações de dispositivos do aplicativo (ex.: Teams → Configurações → Dispositivos), selecione a câmera correta.

**Por quê:** com câmera externa ou dock, o aplicativo pode escolher a câmera errada (por exemplo, a integrada com o notebook fechado).

**O que você deve ver:** a pré-visualização mostrando a imagem.

### Passo 6 — Confira o Gerenciador de Dispositivos

**Faça:** em `Win + X` → **Gerenciador de Dispositivos**, procure **Câmeras** (ou **Dispositivos de imagem**). Veja se há um ícone de alerta ou seta para baixo (dispositivo desabilitado).

**Por quê:** mostra se o Windows reconhece a câmera e se o driver está funcionando.

**O que você deve ver:** a câmera listada sem alertas. Com alerta, anote o código (ver [mensagens de erro](../docs/MENSAGENS_DE_ERRO.md#gerenciador-de-dispositivos)).

---

## Como interpretar o resultado

| Se você observar… | Significa… | Faça |
|---|---|---|
| Imagem preta, câmera "funcionando" | Tampa ou bloqueio físico | Passo 1 |
| Funciona no app Câmera, não na reunião | Permissão ou seleção no aplicativo | Passos 3 e 5 |
| "A câmera está sendo usada por outro aplicativo" | Outro programa segurando a câmera | Passo 4 |
| Câmera não aparece no Gerenciador de Dispositivos | Desligada, desconectada ou defeito | Passo 1, outra porta USB; encaminhe |
| Ícone de alerta no dispositivo | Problema de driver | Encaminhe com o código |

## Como saber que resolveu

- [ ] O usuário aparece na pré-visualização do aplicativo usado.
- [ ] Os participantes de uma chamada de teste veem a imagem.

## O que anotar no chamado

- [ ] Câmera integrada ou externa (modelo)
- [ ] Resultado no aplicativo Câmera do Windows
- [ ] Estado das permissões de privacidade
- [ ] Estado no Gerenciador de Dispositivos

## Quando encaminhar ao N2

- Câmera ausente ou com alerta no Gerenciador de Dispositivos.
- Permissões bloqueadas por política da empresa.
- Defeito físico.

## Erros comuns

- **Reinstalar driver** antes de olhar a tampinha.
- **Deixar o Teams aberto** e testar em outro aplicativo.
- **Não conferir qual câmera** está selecionada com dock.

## Guias relacionados

[KB-18 · Microfone](kb-18-microfone.md) · [KB-21 · Teams](kb-21-teams-reuniao.md) · [KB-32 · Sem som](kb-32-sem-som.md)

**Referências oficiais:** [Central de suporte do Windows][win]

---

[← Anterior: KB-30](kb-30-email-suspeito.md) · [↑ Índice](../README.md#indice) · [Próximo: KB-32 →](kb-32-sem-som.md)

[win]: https://support.microsoft.com/pt-br/windows

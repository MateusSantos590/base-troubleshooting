# KB-04 · Wi-Fi não conecta

[← Índice](../README.md#indice) · **Categoria:** Redes · **Quem executa:** N1 com o usuário

> **Em uma frase:** o computador vê a rede, mas não consegue entrar. O problema está **antes** da internet: no rádio, no sinal ou na credencial.

---

## Entenda o problema

Conectar ao Wi-Fi tem duas etapas, como entrar em um prédio:

1. **Passar pela portaria** (associar-se à rede) — é aqui que este guia atua.
2. **Chegar ao apartamento** (navegar, acessar sistemas) — isso é o [KB-05](kb-05-wifi-sem-internet.md).

Se você nem passou pela portaria, não adianta investigar DNS ou sites. Primeiro resolva a entrada.

**Sintoma típico:** a rede aparece na lista, mas o computador não se conecta ou recusa a senha.

**Causas mais comuns:** Wi-Fi desligado ou modo avião, credencial incorreta, sinal fraco ou política de autenticação da empresa.

## Pergunte primeiro

- Qual é o nome da rede que você tenta usar?
- Aparece alguma mensagem? (ex.: "não é possível conectar", "senha incorreta", erro de certificado)
- Outros dispositivos conseguem se conectar no mesmo lugar?
- Você trocou a senha da sua conta recentemente?

## Antes de começar

> [!CAUTION]
> **Quem digita a senha é o usuário.** Não peça, não anote e não digite credenciais por ele. Remover ou "esquecer" um perfil corporativo de Wi-Fi exige orientação da TI — pode ser difícil recriá-lo.

---

## Passo a passo

### Passo 1 — Confira o básico do rádio

**Faça:** verifique se o **modo avião** está desligado, se o **Wi-Fi** está ativado e se a rede escolhida é a correta (redes com nomes parecidos são comuns).

**Por quê:** é a causa mais simples e mais frequente. Leva 10 segundos.

**O que você deve ver:** Wi-Fi ligado e a rede correta selecionada.

### Passo 2 — Compare com outro dispositivo

**Faça:** veja se outro aparelho autorizado consegue se conectar **no mesmo local**.

**Por quê:** essa comparação divide o problema ao meio. Se ninguém conecta, o problema é da rede. Se só esse computador falha, o problema é dele.

**O que você deve ver:** um resultado claro: "outros conectam" ou "ninguém conecta".

### Passo 3 — Teste o sinal

**Faça:** aproxime o computador do ponto de acesso (roteador ou antena) e tente de novo.

**Por quê:** paredes, distância e interferências enfraquecem o sinal. Se perto funciona e longe não, o problema é alcance.

**O que você deve ver:** se a conexão melhora com a proximidade.

### Passo 4 — Credencial pelo próprio usuário

**Faça:** peça que o usuário digite a própria credencial com atenção (Caps Lock, teclado em outro idioma).

**Por quê:** muitas recusas são simplesmente senha digitada errada ou senha antiga salva.

**O que você deve ver:** conexão estabelecida ou uma mensagem de erro específica para registrar.

---

## Como interpretar o resultado

| Se você observar… | Provavelmente significa… | Próximo passo |
|---|---|---|
| A rede **não aparece** na lista | Alcance, rádio desligado ou adaptador | Confira o Passo 1 e o sinal |
| A rede aparece e **recusa a credencial** | Problema de autenticação | **Não** é problema de navegação/DNS ainda |
| **Erro de certificado** | Autenticação corporativa | Encaminhe; não ignore o alerta |
| Conecta, mas não navega | Você passou para outra etapa | Vá para [KB-05](kb-05-wifi-sem-internet.md) |
| Ninguém consegue conectar no local | Falha coletiva da rede | Encaminhe ao N2 |

## Como saber que resolveu

- [ ] O computador permanece conectado de forma estável.
- [ ] O usuário acessa o recurso de que precisa (não basta o ícone ficar conectado).

## O que anotar no chamado

- [ ] Nome da rede e horário (pelo canal interno)
- [ ] Intensidade aproximada do sinal no local
- [ ] Mensagem de erro exata
- [ ] Resultado da comparação com outro dispositivo

## Quando encaminhar ao N2

- Erro de certificado ou de autenticação corporativa.
- Falha coletiva (várias pessoas sem conectar).

Registre horário e erro, **nunca a senha**.

## Erros comuns

- **Pular para DNS ou sites** antes de confirmar que o computador está conectado à rede.
- **"Esquecer" a rede corporativa** sem saber como reconfigurá-la.
- **Concluir que o computador está com defeito** sem comparar com outro dispositivo.

## Guias relacionados

[KB-05 · Conectado sem internet](kb-05-wifi-sem-internet.md) · [KB-06 · Rede cabeada](kb-06-rede-cabeada.md)

**Referência oficial:** [Corrigir problemas de conexão Wi-Fi no Windows][wifi]

---

[← Anterior: KB-03](kb-03-driver-de-impressora.md) · [↑ Índice](../README.md#indice) · [Próximo: KB-05 →](kb-05-wifi-sem-internet.md)

[wifi]: https://support.microsoft.com/pt-br/windows/experience/connectivity-networking/fix-wi-fi-connection-issues-in-windows

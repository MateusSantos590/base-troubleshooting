# KB-06 · Rede cabeada sem conexão

[← Índice](../README.md#indice) · **Categoria:** Redes · **Quem executa:** N1 com o usuário

> **Em uma frase:** o computador ligado por cabo não acessa a rede. Primeiro descubra se há **conexão física** (enlace); só depois investigue configuração.

---

## Entenda o problema

Rede por cabo é como um telefone fixo: antes de discar, você precisa ouvir o **sinal de linha**. Sem sinal, o problema é fio, tomada ou aparelho. Com sinal, o problema é o número discado. Em rede, o "sinal de linha" se chama **enlace** — normalmente uma luz acesa na porta do cabo.

**Sintoma típico:** o Windows mostra "cabo de rede desconectado" ou não obtém acesso.

**Causas mais comuns:** cabo solto ou danificado, porta da parede/switch desativada, adaptador de rede com problema ou configuração incorreta.

## Pergunte primeiro

- O computador foi mudado de lugar ou o cabo foi trocado?
- Funcionava antes nesse mesmo ponto?
- Outras pessoas por perto, também por cabo, estão com problema?

## Antes de começar

> [!WARNING]
> Troque **um item por vez** (primeiro o cabo, depois a porta). Não altere VLAN, IP fixo ou configuração de switch por tentativa — isso é com a equipe de rede.

---

## Passo a passo

### Passo 1 — Confira encaixes e luzes

**Faça:** verifique se o cabo está bem encaixado nas duas pontas (computador e parede/switch). Observe se há luz acesa ou piscando ao lado da porta, quando o equipamento tiver.

**Por quê:** a luz indica enlace — o "sinal de linha". Sem ela, nada adiante vai funcionar.

**O que você deve ver:** cabo firme e indicador de enlace aceso.

### Passo 2 — Teste outro cabo, depois outra porta

**Faça:** troque o cabo por um **aprovado e conhecido como funcional**. Se não resolver, volte o cabo original e teste **outra porta autorizada**.

**Por quê:** mudar um item por vez mostra exatamente qual peça falhou.

**O que você deve ver:** o enlace aparecendo com uma das trocas — ou não aparecendo com nenhuma.

### Passo 3 — Veja se o adaptador aparece no Windows

**Faça:** em **Configurações → Rede e Internet → Configurações de rede avançadas**, confira se o adaptador Ethernet aparece e se está habilitado. Registre o estado.

**Por quê:** se o Windows não enxerga o adaptador, o problema é de hardware ou driver, não de cabo.

**O que você deve ver:** adaptador Ethernet listado e habilitado.

### Passo 4 — Com enlace ativo, confira o endereço

**Faça:** execute `ipconfig` e veja o endereço do adaptador Ethernet. ([Como ler](../docs/COMANDOS.md#ipconfig--qual-é-o-meu-endereço))

**Por quê:** com o "sinal de linha" ok, o próximo trecho do caminho é o endereço.

**O que você deve ver:** um endereço válido. Se começar com `169.254.`, vá para [KB-08](kb-08-ip-169-254.md). Se o endereço estiver ok, mas nomes não abrirem, vá para [KB-07](kb-07-falha-dns.md).

---

## Como interpretar o resultado

| Se você observar… | Provavelmente significa… | Próximo passo |
|---|---|---|
| Sem enlace, mesmo com cabo conhecido como bom | Porta ou adaptador com problema | Compare outra porta; persistindo, encaminhe |
| Enlace aparece com outro cabo | O cabo original estava com defeito | Substitua e registre |
| Adaptador não aparece no Windows | Hardware ou driver | Encaminhe ao N2 |
| Enlace ok e endereço correto | O problema não é físico | **Pare de trocar cabos**; investigue acesso ([KB-05](kb-05-wifi-sem-internet.md)) |

## Como saber que resolveu

- [ ] Há enlace estável.
- [ ] O usuário executa a tarefa de rede que precisava.

## O que anotar no chamado

- [ ] Cabos e portas testados (e em que ordem)
- [ ] Estado do adaptador
- [ ] Presença ou ausência de enlace
- [ ] Resultado da tarefa final

## Quando encaminhar ao N2

- Adaptador ausente no Windows.
- Porta bloqueada ou desativada.
- Falha de infraestrutura (várias pessoas afetadas).

## Erros comuns

- **Continuar trocando cabos** quando o enlace já está ok. O problema mudou de camada.
- **Trocar cabo e porta ao mesmo tempo.** Você não saberá qual era o defeito.
- **Configurar IP fixo "para testar".** Pode causar conflito com outro equipamento da rede.

## Guias relacionados

[KB-07 · DNS](kb-07-falha-dns.md) · [KB-08 · 169.254.x.x](kb-08-ip-169-254.md) · [KB-05 · Conectado sem internet](kb-05-wifi-sem-internet.md)

**Referência oficial:** [Comando ipconfig][ipconfig]

---

[← Anterior: KB-05](kb-05-wifi-sem-internet.md) · [↑ Índice](../README.md#indice) · [Próximo: KB-07 →](kb-07-falha-dns.md)

[ipconfig]: https://learn.microsoft.com/pt-br/windows-server/administration/windows-commands/ipconfig

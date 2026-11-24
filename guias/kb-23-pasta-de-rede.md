# KB-23 · Pasta de rede ou unidade mapeada não abre

[← Índice](../README.md#indice) · **Categoria:** Redes · **Quem executa:** N1 (permissões são do N2 ou do responsável pela pasta)

> **Em uma frase:** para abrir uma pasta de rede, três coisas precisam dar certo — **achar** o servidor, **chegar** até ele e ter **permissão** para entrar. A mensagem de erro diz qual falhou.

---

## Entenda o problema

Uma pasta compartilhada é como **uma sala em outro prédio**. Para entrar, você precisa saber o endereço (nome do servidor), conseguir chegar lá (rede ou VPN) e ter a chave da sala (permissão). Uma **unidade mapeada** (ex.: `S:`) é só um atalho no seu chaveiro apontando para aquela sala.

Endereço típico: `\\servidor\pasta` — duas barras invertidas, nome do servidor, barra, nome do compartilhamento.

**Sintoma típico:** "a unidade S: está com X vermelho", "o caminho de rede não foi encontrado", "você não tem permissão".

**Causas mais comuns:** fora do escritório sem VPN, nome do servidor que não resolve, permissão não concedida ou removida, senha alterada recentemente.

## Pergunte primeiro

- Qual é o **caminho exato** ou a letra da unidade?
- Você está no escritório ou em casa? Se em casa, a VPN está conectada?
- Funcionava antes? Quando parou?
- Colegas conseguem abrir a mesma pasta?
- Você trocou a senha recentemente?

## Antes de começar

> [!CAUTION]
> **Não salve credenciais de outra pessoa** no Gerenciador de Credenciais para "fazer abrir", e **não peça permissão em nome do usuário** sem aprovação do responsável pela pasta. Acesso a dados é decisão do dono dos dados, não do suporte.

---

## Passo a passo

### Passo 1 — Clique na unidade antes de concluir

**Faça:** dê um duplo clique na unidade com X vermelho.

**Por quê:** o Windows às vezes mostra o X só porque a unidade foi mapeada antes da rede ficar pronta. Ao clicar, ele tenta reconectar.

**O que você deve ver:** a pasta abrindo (falso alarme) ou uma mensagem de erro específica — anote o texto exato.

### Passo 2 — Confira rede e VPN

**Faça:** confirme que outros recursos internos abrem. Fora do escritório, confirme a VPN.

**Por quê:** pastas de rede quase nunca ficam expostas na internet. Sem VPN, a "sala" simplesmente não existe para quem está do lado de fora.

**O que você deve ver:** VPN conectada e outro recurso interno funcionando. Se não, vá para [KB-14](kb-14-vpn-nao-conecta.md).

### Passo 3 — Veja para onde a unidade aponta

**Faça:** no terminal, execute `net use`. ([Como ler](../docs/COMANDOS.md#net-use--quais-unidades-de-rede-estão-mapeadas))

**Por quê:** mostra cada letra, o caminho real e o status (`OK`, `Desconectado`, `Indisponível`). Às vezes a unidade aponta para um servidor antigo que foi desligado.

**O que você deve ver:** o caminho `\\servidor\pasta` da unidade. Compare com o caminho documentado pela TI.

### Passo 4 — Teste o nome do servidor

**Faça:** execute `nslookup servidor` com o nome que aparece no caminho.

**Por quê:** se o nome não vira endereço, o Windows não sabe para onde ir. É um problema de DNS, não de permissão.

**O que você deve ver:** um endereço IP. Se der erro, siga o [KB-07](kb-07-falha-dns.md).

### Passo 5 — Abra o caminho direto

**Faça:** em `Win + R`, digite o caminho completo (`\\servidor\pasta`) e pressione `Enter`.

**Por quê:** pula o atalho (a letra) e testa o acesso de verdade. Se o caminho direto abre, só o mapeamento está errado.

**O que você deve ver:** a pasta abrindo ou uma mensagem de erro específica.

---

## Como interpretar o resultado

| Mensagem | Significa… | Analogia | Faça |
|---|---|---|---|
| "O caminho de rede não foi encontrado" (0x80070035) | Não achou ou não alcançou o servidor | Endereço não existe ou a rua está bloqueada | Passos 2 e 4 |
| "Você não tem permissão para acessar" / "Acesso negado" | Chegou, mas não tem a chave | Porta trancada | Encaminhe ao responsável pela pasta |
| Pede usuário e senha repetidamente | Credencial errada ou antiga salva | Chave velha no chaveiro | Senha trocada? Peça para o usuário reentrar; veja o Gerenciador de Credenciais |
| Caminho direto abre, a letra não | Mapeamento desatualizado | Atalho apontando para a sala antiga | Remapeie conforme a documentação da TI |
| Só um colega não consegue | Permissão ou conta individual | — | Encaminhe com o caminho e a mensagem |

## Como saber que resolveu

- [ ] A pasta abre pela letra da unidade (ou pelo caminho, se não houver mapeamento).
- [ ] O usuário abre **e salva** um arquivo de teste, se ele precisa gravar ali.
- [ ] A unidade continua funcionando após reiniciar ou reconectar a VPN.

## O que anotar no chamado

- [ ] Caminho da pasta ou letra da unidade
- [ ] Mensagem de erro exata
- [ ] Local do usuário (escritório/VPN) e se colegas são afetados
- [ ] Resultado do `net use`, do `nslookup` e do caminho direto

## Quando encaminhar ao N2

- Acesso negado: pedido de permissão (com aprovação do responsável pela pasta).
- Servidor não responde para vários usuários.
- Mapeamento distribuído por política que precisa ser corrigido.

## Erros comuns

- **Conceder permissão por conta própria** ou usar a credencial de um colega.
- **Concluir "servidor fora do ar" sem testar a VPN.**
- **Ignorar o X vermelho como erro** sem clicar: muitas vezes é só reconexão pendente.

## Guias relacionados

[KB-07 · DNS](kb-07-falha-dns.md) · [KB-14 · VPN não conecta](kb-14-vpn-nao-conecta.md) · [KB-15 · VPN conecta, sistema não abre](kb-15-vpn-conecta-sistema-nao-abre.md) · [KB-24 · Arquivo do Office bloqueado](kb-24-arquivo-office-bloqueado.md)

**Referências oficiais:** [Comando net use][netuse] · [Comando nslookup][nslookup]

---

[← Anterior: KB-22](kb-22-onedrive-sincronizacao.md) · [↑ Índice](../README.md#indice) · [Próximo: KB-24 →](kb-24-arquivo-office-bloqueado.md)

[netuse]: https://learn.microsoft.com/pt-br/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/gg651155(v=ws.11)
[nslookup]: https://learn.microsoft.com/pt-br/windows-server/administration/windows-commands/nslookup

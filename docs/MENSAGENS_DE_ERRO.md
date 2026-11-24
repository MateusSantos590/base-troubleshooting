# Dicionário de mensagens de erro

[← Voltar ao início](../README.md) · [Método](METODO.md) · [Comandos](COMANDOS.md) · [Glossário](GLOSSARIO.md)

> **Em uma frase:** a mensagem de erro é a **pista mais barata** do atendimento — ela já diz em qual camada o problema está. Aqui está o que as mais comuns significam e para qual guia ir.

> [!IMPORTANT]
> Um código aponta uma **família de causas**, não a causa exata. Use-o para escolher a hipótese inicial e confirme com um teste. O mesmo código pode ter outra origem em versões ou produtos diferentes.

**Atalhos:** [Navegador e sites](#navegador-e-sites) · [Rede e Wi-Fi](#rede-e-wi-fi) · [Pastas de rede](#pastas-de-rede) · [Conta e login](#conta-e-login) · [VPN do Windows](#vpn-do-windows) · [E-mail e Outlook](#e-mail-e-outlook) · [Impressão](#impressão) · [Gerenciador de Dispositivos](#gerenciador-de-dispositivos) · [Windows Update](#windows-update) · [Tela azul](#tela-azul)

---

## Como usar esta página

1. **Peça a mensagem exata** (foto ou texto). "Deu erro" não é mensagem.
2. **Procure aqui** com `Ctrl + F` pelo código ou por um trecho do texto.
3. **Leia a coluna "O que significa"** para formar a hipótese.
4. **Vá para o guia indicado** e confirme com um teste antes de agir.
5. **Anote o código no chamado** — mesmo que você resolva.

---

## Navegador e sites

### Códigos HTTP (o "recado" que o site devolve)

Os códigos HTTP funcionam como **placas na porta de um prédio**. O primeiro dígito diz quem tem o problema: **4xx** = algo no pedido do usuário (login, permissão, endereço); **5xx** = algo do lado do servidor.

| Código | O que significa | Analogia | Vá para |
|---|---|---|---|
| `400 Bad Request` | O pedido chegou malformado — muitas vezes cookie ou sessão corrompidos | Formulário preenchido errado | [KB-20](../guias/kb-20-sistema-web.md): teste janela privativa |
| `401 Unauthorized` | Falta autenticação ou a sessão expirou | "Identifique-se" | [KB-20](../guias/kb-20-sistema-web.md) |
| `403 Forbidden` | Autenticado, mas **sem permissão** | "Proibida a entrada" | Encaminhe pedido de acesso ao responsável |
| `404 Not Found` | O endereço não existe (link antigo ou digitado errado) | "Endereço não existe" | Confira o endereço oficial |
| `408 Request Timeout` | O servidor esperou o pedido e desistiu | A ligação caiu antes de você falar | Rede lenta ou instável: [KB-05](../guias/kb-05-wifi-sem-internet.md) |
| `429 Too Many Requests` | Pedidos demais em pouco tempo | Fila com limite de senhas | Aguarde; evite recarregar sem parar |
| `500 Internal Server Error` | Erro genérico do servidor | "Problema na cozinha" | Encaminhe com horário e identificador de correlação |
| `502 Bad Gateway` | Um servidor intermediário recebeu resposta inválida | O recepcionista não conseguiu falar com o setor | Encaminhe; verifique se é geral |
| `503 Service Unavailable` | Serviço fora do ar ou em manutenção | "Fechado para manutenção" | Verifique incidente ou janela de manutenção |
| `504 Gateway Timeout` | Um servidor intermediário não recebeu resposta a tempo | O setor não atendeu o ramal | Encaminhe; verifique se é geral |

### Mensagens do navegador (Edge e Chrome)

| Mensagem | O que significa | Vá para |
|---|---|---|
| `DNS_PROBE_FINISHED_NXDOMAIN` / `ERR_NAME_NOT_RESOLVED` | O nome não foi traduzido em endereço (DNS) | [KB-07](../guias/kb-07-falha-dns.md) |
| `ERR_INTERNET_DISCONNECTED` | O computador não está conectado a nenhuma rede | [KB-04](../guias/kb-04-wifi-nao-conecta.md) / [KB-06](../guias/kb-06-rede-cabeada.md) |
| `ERR_CONNECTION_TIMED_OUT` | O endereço foi encontrado, mas ninguém respondeu | [KB-05](../guias/kb-05-wifi-sem-internet.md) / [KB-15](../guias/kb-15-vpn-conecta-sistema-nao-abre.md) |
| `ERR_CONNECTION_REFUSED` | O servidor recusou a conexão (serviço parado ou porta fechada) | Encaminhe; confirme se é geral |
| `ERR_PROXY_CONNECTION_FAILED` | O navegador tenta usar um proxy que não responde | Encaminhe; não altere proxy corporativo |
| `NET::ERR_CERT_DATE_INVALID` | Certificado "vencido" — **muitas vezes o relógio do computador está errado** | Confira data e hora automáticas |
| `NET::ERR_CERT_AUTHORITY_INVALID` / `ERR_CERT_COMMON_NAME_INVALID` | O certificado não é confiável ou não corresponde ao endereço | **Não ignore o alerta.** Encaminhe |

> [!CAUTION]
> Alerta de certificado é um **alarme de segurança**. Nunca oriente o usuário a clicar em "Avançado → Continuar mesmo assim" num sistema corporativo.

---

## Rede e Wi-Fi

| Mensagem ou sinal | O que significa | Vá para |
|---|---|---|
| "Sem internet, protegido" | Conectado ao Wi-Fi, mas sem acesso além da rede local | [KB-05](../guias/kb-05-wifi-sem-internet.md) |
| "Não é possível se conectar a esta rede" | Falha ao entrar no Wi-Fi (credencial, sinal, perfil) | [KB-04](../guias/kb-04-wifi-nao-conecta.md) |
| "Cabo de rede desconectado" / "Mídia desconectada" | Sem enlace físico no cabo | [KB-06](../guias/kb-06-rede-cabeada.md) |
| Endereço IPv4 `169.254.x.x` | O computador não recebeu endereço do DHCP | [KB-08](../guias/kb-08-ip-169-254.md) |
| "Rede não identificada" | Conectado fisicamente, sem configuração válida | [KB-08](../guias/kb-08-ip-169-254.md) |
| "O Windows detectou um conflito de endereço IP" | Dois equipamentos com o mesmo endereço | Encaminhe ao N2 de redes |

---

## Pastas de rede

| Mensagem | O que significa | Vá para |
|---|---|---|
| "O caminho de rede não foi encontrado" (`0x80070035`) / **Erro de sistema 53** | Não achou ou não alcançou o servidor | [KB-23](../guias/kb-23-pasta-de-rede.md): VPN e DNS |
| "Acesso negado" / **Erro de sistema 5** | Chegou, mas não tem permissão | [KB-23](../guias/kb-23-pasta-de-rede.md): encaminhe pedido |
| **Erro de sistema 86** | Senha de rede incorreta | [KB-23](../guias/kb-23-pasta-de-rede.md): credencial salva antiga? |
| **Erro de sistema 1326** | Usuário ou senha incorretos | [KB-17](../guias/kb-17-senha-esquecida-ou-expirada.md) |
| **Erro de sistema 1219** | Já existe conexão com o mesmo servidor usando **outra** credencial | Encaminhe; não use credencial de colega |

---

## Conta e login

| Mensagem ou código | O que significa | Vá para |
|---|---|---|
| "A conta referenciada está bloqueada" / `AADSTS50053` | Conta bloqueada por tentativas erradas | [KB-16](../guias/kb-16-conta-bloqueada.md) |
| "Sua senha expirou" / `AADSTS50055` | Senha venceu pela política | [KB-17](../guias/kb-17-senha-esquecida-ou-expirada.md) |
| `AADSTS50126` | Usuário ou senha inválidos | [KB-17](../guias/kb-17-senha-esquecida-ou-expirada.md) — e atenção a bloqueio |
| `AADSTS50076` | É necessária a autenticação multifator | [KB-29](../guias/kb-29-mfa-autenticador.md) |
| `AADSTS53003` | Bloqueado por política de acesso condicional (dispositivo, local, risco) | Encaminhe à equipe de identidade |
| "A relação de confiança entre esta estação de trabalho e o domínio primário falhou" | O computador perdeu o vínculo com o domínio | Encaminhe ao N2 — exige permissão administrativa |
| "O nome de usuário ou a senha está incorreto" (na tela do Windows) | Credencial errada, Caps Lock, layout do teclado | Confira Caps Lock e idioma do teclado; [KB-17](../guias/kb-17-senha-esquecida-ou-expirada.md) |

> [!TIP]
> Os códigos `AADSTS…` aparecem nas telas de login da Microsoft (Entra ID). Anote o código **e** o identificador de correlação, se houver: com eles, a equipe de identidade encontra o registro exato.

---

## VPN do Windows

Os códigos abaixo são do **cliente VPN nativo do Windows**. VPNs de outros fabricantes usam códigos próprios — consulte a documentação interna.

| Código | O que significa | Vá para |
|---|---|---|
| `691` | Credenciais recusadas | [KB-14](../guias/kb-14-vpn-nao-conecta.md) — etapa de autenticação |
| `809` | Não foi possível estabelecer a conexão com o servidor VPN (muitas vezes a rede local bloqueia) | [KB-14](../guias/kb-14-vpn-nao-conecta.md) — teste outra rede |
| `789` | Falha na negociação de segurança | Encaminhe ao N2 |

---

## E-mail e Outlook

| Mensagem ou código | O que significa | Vá para |
|---|---|---|
| "Não é possível iniciar o Microsoft Outlook" | Falha ao abrir (perfil, suplemento, arquivo de dados) | [KB-12](../guias/kb-12-outlook-nao-abre.md) |
| `0x8004010F` | Arquivo de dados ou perfil não acessível | [KB-12](../guias/kb-12-outlook-nao-abre.md) — encaminhe; não apague OST/PST |
| `0x800CCC0E` | Não conseguiu conectar ao servidor de e-mail | [KB-13](../guias/kb-13-outlook-nao-envia-recebe.md) |
| "Trabalhando Offline" na barra inferior | Envio e recebimento pausados | [KB-13](../guias/kb-13-outlook-nao-envia-recebe.md) |
| Mensagem de devolução com `550 5.1.1` | O destinatário não existe (endereço errado) | Confira o endereço |
| Devolução com `5.2.2` | A caixa do destinatário está cheia | Avise o destinatário por outro canal |
| Devolução com `5.7.1` | Envio não autorizado (permissão ou política) | Encaminhe ao N2 |

> [!NOTE]
> Na **mensagem de devolução** (NDR), o código mais útil costuma estar no formato `5.x.x`. O primeiro dígito `5` indica falha **permanente**; `4` indica falha **temporária** (o servidor tentará de novo).

---

## Impressão

| Mensagem ou código | O que significa | Vá para |
|---|---|---|
| "Impressora offline" | O computador não alcança a impressora | [KB-01](../guias/kb-01-impressora-offline.md) |
| "O serviço de spooler de impressão não está em execução" | O serviço que gerencia a fila parou | [KB-02](../guias/kb-02-documento-preso-na-fila.md) — reinício do serviço conforme permissão |
| "Driver indisponível" | Driver ausente ou incompatível | [KB-03](../guias/kb-03-driver-de-impressora.md) |
| `0x0000011b` | Falha ao conectar a impressora compartilhada, geralmente ligada a mudanças de segurança | Encaminhe ao N2 — **não** desative proteções |
| `0x00000709` | Não foi possível definir a impressora padrão | Confira se o Windows gerencia a impressora padrão automaticamente; encaminhe se persistir |

---

## Gerenciador de Dispositivos

O ícone de alerta amarelo em um dispositivo vem acompanhado de um **código** nas Propriedades → Geral.

| Código | O que significa | O que fazer |
|---|---|---|
| **Código 10** | O dispositivo não pode ser iniciado | Reconecte; registre e encaminhe se persistir |
| **Código 22** | O dispositivo está desabilitado | Confirme se foi desabilitado de propósito (política) antes de habilitar |
| **Código 28** | Os drivers não estão instalados | Driver pelo canal oficial; [KB-03](../guias/kb-03-driver-de-impressora.md) como referência |
| **Código 43** | O Windows parou o dispositivo porque ele relatou problemas | Reconecte em outra porta; possível defeito — encaminhe |
| **Código 45** | O dispositivo não está conectado no momento | Verifique o cabo/conexão física |

---

## Windows Update

| Código | Família provável | Vá para |
|---|---|---|
| `0x80070070` | Falta de espaço em disco | [KB-10](../guias/kb-10-pouco-espaco-em-disco.md) e [KB-25](../guias/kb-25-windows-update.md) |
| `0x8024402C` | Não conseguiu alcançar o servidor de atualizações (rede ou proxy) | [KB-25](../guias/kb-25-windows-update.md) — teste com rede estável |
| `0x800F0922` | Falha na instalação, frequentemente ligada à conexão com o serviço ou a espaço em partição do sistema | [KB-25](../guias/kb-25-windows-update.md) — encaminhe se persistir |
| "Algumas configurações são gerenciadas pela sua organização" | Não é erro: a TI controla as atualizações | Confirme com o N2 se o computador está em dia |

---

## Tela azul

Códigos de parada mais vistos e a família de causa mais comum. Detalhes no [KB-26](../guias/kb-26-tela-azul.md).

| Código de parada | Família mais comum |
|---|---|
| `IRQL_NOT_LESS_OR_EQUAL` | Driver acessando memória de forma indevida |
| `PAGE_FAULT_IN_NONPAGED_AREA` | Memória, driver ou disco |
| `MEMORY_MANAGEMENT` | Memória RAM ou driver |
| `SYSTEM_SERVICE_EXCEPTION` | Driver ou software do sistema |
| `CRITICAL_PROCESS_DIED` | Um processo essencial do Windows parou (arquivos do sistema, disco, driver) |
| `DRIVER_POWER_STATE_FAILURE` | Driver com problema ao suspender ou retomar |
| `INACCESSIBLE_BOOT_DEVICE` | O Windows não consegue acessar o disco de inicialização |
| `VIDEO_TDR_FAILURE` | Driver de vídeo parou de responder |
| `WHEA_UNCORRECTABLE_ERROR` | Erro de hardware relatado pelo próprio equipamento |

---

## Não encontrou a mensagem?

1. Anote o texto **exato** e o código.
2. Pesquise na **documentação oficial** do fabricante (Microsoft, fabricante do equipamento, fornecedor do sistema).
3. Desconfie de sites que oferecem "ferramentas que corrigem tudo" para download.
4. [Sugira a inclusão](../CONTRIBUTING.md) da mensagem nesta página, sem dados reais.

**Referências oficiais:** [Códigos de erro de login do Entra ID][aadsts] · [Códigos de parada][bugcheck] · [Comando net use][netuse]

---

[← Voltar ao início](../README.md)

[aadsts]: https://learn.microsoft.com/pt-br/entra/identity-platform/reference-error-codes
[bugcheck]: https://learn.microsoft.com/pt-br/windows-hardware/drivers/debugger/bug-check-code-reference2
[netuse]: https://learn.microsoft.com/pt-br/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/gg651155(v=ws.11)

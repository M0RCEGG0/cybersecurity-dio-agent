# Técnicas de Ataque em Segurança da Informação

Este arquivo descreve as principais técnicas usadas por atacantes, com foco em como profissionais de segurança as identificam e defendem. Cada técnica inclui referência ao framework MITRE ATT&CK — o padrão global para catalogar comportamentos de ameaças.

---

## 1. Engenharia Social

Técnicas que exploram o fator humano em vez de vulnerabilidades técnicas. O elo mais fraco costuma ser a pessoa, não o sistema.

### Phishing

Envio de e-mails falsos que imitam entidades confiáveis (banco, empresa, colega) para roubar credenciais ou instalar malware.

- **Como funciona:** o atacante cria um link ou anexo malicioso e convence a vítima a clicar
- **CIA violado:** Confidencialidade (roubo de credenciais)
- **MITRE ATT&CK:** T1566 — Phishing

### Spear Phishing

Versão direcionada do phishing. O atacante pesquisa a vítima antes e personaliza a mensagem para parecer legítima.

- **Como funciona:** e-mail usa nome real, cargo, projetos da vítima para ganhar confiança
- **CIA violado:** Confidencialidade, Integridade
- **MITRE ATT&CK:** T1566.001 — Spear Phishing via Attachment

### Vishing

Phishing por voz (ligação telefônica). O atacante se passa por suporte técnico, banco ou autoridade.

- **Como funciona:** pressão e urgência para que a vítima forneça senhas ou instale software
- **CIA violado:** Confidencialidade
- **MITRE ATT&CK:** T1598 — Phishing for Information

### Pretexting

O atacante cria um cenário fictício (pretexto) para ganhar a confiança da vítima e extrair informações.

- **Como funciona:** "Sou do RH e preciso confirmar seus dados de acesso para a migração do sistema"
- **CIA violado:** Confidencialidade
- **MITRE ATT&CK:** T1656 — Impersonation

---

## 2. Ataques de Autenticação

Técnicas que visam comprometer credenciais de acesso.

### Brute Force

Tentativa exaustiva de todas as combinações possíveis de senha até encontrar a correta.

- **Como funciona:** ferramenta automatizada testa milhares de senhas por segundo
- **CIA violado:** Confidencialidade
- **MITRE ATT&CK:** T1110.001 — Brute Force: Password Guessing

### Password Spraying

Em vez de muitas senhas para um usuário, testa uma senha comum contra muitos usuários. Evita bloqueio de conta.

- **Como funciona:** testa "123456" ou "Empresa2024" em todos os usuários do sistema
- **CIA violado:** Confidencialidade
- **MITRE ATT&CK:** T1110.003 — Brute Force: Password Spraying

### Credential Stuffing

Uso de listas de credenciais vazadas em outros serviços para tentar acesso em novos sistemas.

- **Como funciona:** usuário reutiliza senha — atacante compra lista de vazamento e testa em outros sites
- **CIA violado:** Confidencialidade
- **MITRE ATT&CK:** T1110.004 — Brute Force: Credential Stuffing

---

## 3. Injeção de Código

Técnicas que inserem código malicioso em aplicações que não validam a entrada do usuário.

### SQL Injection

Inserção de comandos SQL em campos de formulário para manipular o banco de dados.

- **Como funciona:** `' OR '1'='1` em um campo de senha ignora a verificação e concede acesso
- **CIA violado:** Confidencialidade (leitura de dados), Integridade (alteração/deleção), Disponibilidade (drop de tabelas)
- **MITRE ATT&CK:** T1190 — Exploit Public-Facing Application

### Cross-Site Scripting (XSS)

Injeção de scripts maliciosos em páginas web que são executados no navegador de outras vítimas.

- **Como funciona:** atacante salva `<script>document.cookie</script>` num comentário — script roda no navegador de quem acessa
- **CIA violado:** Confidencialidade (roubo de cookies/sessão)
- **MITRE ATT&CK:** T1059.007 — Command and Scripting Interpreter: JavaScript

### Command Injection

Injeção de comandos do sistema operacional em aplicações que executam comandos a partir de entradas do usuário.

- **Como funciona:** campo que aceita IP para ping recebe `8.8.8.8; rm -rf /` e executa o segundo comando
- **CIA violado:** Integridade, Disponibilidade
- **MITRE ATT&CK:** T1059 — Command and Scripting Interpreter

---

## 4. Ataques de Rede

Técnicas que exploram a comunicação entre sistemas.

### Man-in-the-Middle (MitM)

O atacante se posiciona entre dois sistemas que se comunicam, interceptando e podendo alterar os dados.

- **Como funciona:** ARP spoofing redireciona o tráfego da vítima pelo computador do atacante
- **CIA violado:** Confidencialidade (interceptação), Integridade (modificação)
- **MITRE ATT&CK:** T1557 — Adversary-in-the-Middle

### Sniffing

Captura passiva de pacotes de rede para extrair informações trafegadas em texto puro.

- **Como funciona:** ferramenta como Wireshark captura credenciais em protocolos sem criptografia (HTTP, FTP, Telnet)
- **CIA violado:** Confidencialidade
- **MITRE ATT&CK:** T1040 — Network Sniffing

### DoS / DDoS

Negação de Serviço: sobrecarregar um sistema com requisições até que ele pare de responder.

- **Como funciona:** botnet envia milhões de requisições simultâneas, esgotando recursos do servidor
- **CIA violado:** Disponibilidade
- **MITRE ATT&CK:** T1498 — Network Denial of Service

---

## 5. Escalada e Persistência

Técnicas usadas após o acesso inicial para ampliar o controle e manter presença no sistema.

### Privilege Escalation

Após entrar como usuário comum, o atacante busca obter permissões de administrador.

- **Como funciona:** explorar vulnerabilidade em processo com permissão elevada ou configuração incorreta de sudo
- **CIA violado:** Confidencialidade, Integridade
- **MITRE ATT&CK:** T1068 — Exploitation for Privilege Escalation

### Backdoor

Mecanismo secreto instalado pelo atacante para manter acesso mesmo que a vulnerabilidade original seja corrigida.

- **Como funciona:** script ou serviço oculto que abre conexão reversa para o atacante periodicamente
- **CIA violado:** Confidencialidade, Integridade
- **MITRE ATT&CK:** T1543 — Create or Modify System Process

### Lateral Movement

Após comprometer um sistema, o atacante se move para outros sistemas da mesma rede.

- **Como funciona:** uso de credenciais capturadas para acessar outros servidores internos via RDP ou SSH
- **CIA violado:** Confidencialidade, Integridade
- **MITRE ATT&CK:** T1021 — Remote Services

---

## 6. Exfiltração de Dados

Técnicas para extrair dados roubados do ambiente comprometido sem ser detectado.

### Exfiltração via SMTP

Envio de dados roubados por e-mail usando o protocolo de envio de mensagens.

- **Como funciona:** keylogger ou script coleta dados locais e os envia por e-mail para conta do atacante
- **CIA violado:** Confidencialidade
- **MITRE ATT&CK:** T1048.002 — Exfiltration Over Alternative Protocol: SMTP

### Exfiltração via DNS

Dados codificados são enviados como consultas DNS, disfarçando o tráfego como resolução de nomes.

- **Como funciona:** dados são fragmentados e enviados como subdomínios (`dado123.atacante.com`)
- **CIA violado:** Confidencialidade
- **MITRE ATT&CK:** T1071.004 — Application Layer Protocol: DNS

### Exfiltração por Canais Legítimos

Uso de serviços confiáveis (Google Drive, Dropbox, Pastebin) para enviar dados roubados.

- **Como funciona:** dados são enviados via API de serviço legítimo que não é bloqueado pelo firewall
- **CIA violado:** Confidencialidade
- **MITRE ATT&CK:** T1567 — Exfiltration Over Web Service

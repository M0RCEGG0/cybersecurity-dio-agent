# Principais Ferramentas de Segurança da Informação

Um guia prático e didático sobre as principais ferramentas utilizadas por profissionais de segurança (Red Team e Blue Team). Compreender como essas ferramentas operam permite tanto auditar ambientes de teste quanto construir defesas mais resilientes.

---

## 1. Varredura e Análise de Redes

Ferramentas focadas em visibilidade de rede, descoberta de serviços e análise de tráfego.

### Nmap (Network Mapper)
- **Para que serve:** Descoberta de hosts ativos na rede, enumeração de portas abertas, identificação de serviços em execução e detecção de versões de sistemas operacionais.
- **Cenário de uso:** Inventário de ativos e identificação de portas desnecessárias abertas em um servidor.
- **Como a defesa se beneficia:** Permite que analistas de segurança façam varreduras internas periódicas para encontrar serviços expostos indevidamente antes que um atacante os encontre.

### Wireshark
- **Para que serve:** Analisador de protocolos de rede (sniffer). Captura pacotes de rede em tempo real e permite inspecionar cada camada do tráfego em detalhes.
- **Cenário de uso:** Diagnóstico de falhas de rede, análise de tráfego não criptografado (ex: HTTP, FTP) e inspeção de comportamento de malwares em ambiente de sandbox.
- **Como a defesa se beneficia:** Essencial para resposta a incidentes, identificação de exfiltração de dados e detecção de ataques de Man-in-the-Middle (MitM).

---

## 2. Segurança de Aplicações Web (AppSec)

Ferramentas para interceptação de requisições, testes manuais e varreduras automáticas em sistemas web.

### Burp Suite
- **Para que serve:** Proxy interceptador web. Posiciona-se entre o navegador e o servidor web, permitindo visualizar, pausar, modificar e reenviar requisições HTTP/S em tempo real.
- **Cenário de uso:** Testes de vulnerabilidades do OWASP Top 10, como SQL Injection, manipulação de parâmetros de controle de acesso (BOLA/IDOR) e XSS.
- **Como a defesa se beneficia:** Ajuda times de desenvolvimento e AppSec a validar se correções de vulnerabilidades no código realmente impedem manipulações maliciosas.

### OWASP ZAP (Zed Attack Proxy)
- **Para que serve:** Ferramenta open-source para varredura e testes automatizados de segurança em aplicações web.
- **Cenário de uso:** Integração em esteiras de CI/CD para rodar testes dinâmicos de segurança (DAST) antes de subir uma aplicação para produção.
- **Como a defesa se beneficia:** Democratiza a análise contínua de vulnerabilidades em times de desenvolvimento sem custo de licenciamento.

---

## 3. Auditoria de Credenciais e Autenticação

Ferramentas para validação de resistência de senhas e auditoria de políticas de segurança.

### Medusa / THC-Hydra
- **Para que serve:** Ferramentas de teste de login por força bruta e password spraying via rede contra protocolos como SSH, FTP, HTTP e SMB.
- **Cenário de uso:** Auditoria periódica de servidores internos para identificar se administradores ou colaboradores utilizam senhas fracas ou previsíveis.
- **Como a defesa se beneficia:** Valida a eficácia de mecanismos como bloqueio por tentativas excessivas (account lockout) e rate limiting.

### John the Ripper / Hashcat
- **Para que serve:** Quebra de hashes de senhas (offline) utilizando ataques de dicionário, regras de mutação e força bruta via CPU/GPU.
- **Cenário de uso:** Testar a robustez dos hashes de senhas armazenados no banco de dados (ex: verificar se foram usados sais adequados e algoritmos robustos como Argon2/bcrypt).
- **Como a defesa se beneficia:** Demonstra o risco de utilizar algoritmos obsoletos (como MD5 ou SHA-1) e incentiva a adoção de senhas longas e complexas.

---

## 4. Simulação de Ataques e Validação de Vulnerabilidades

### Metasploit Framework
- **Para que serve:** Plataforma completa para desenvolvimento, teste e execução de exploits contra sistemas alvos em ambientes controlados.
- **Cenário de uso:** Validação de se uma falha reportada (CVE) é de fato explorável no ambiente da organização (reduzindo falsos positivos).
- **Como a defesa se beneficia:** Ajuda a priorizar a aplicação de patches emergenciais ao demonstrar o impacto real de uma vulnerabilidade não corrigida.

---

## 5. Defesa, Monitoramento e Resposta a Incidentes (Blue Team)

Ferramentas indispensáveis para detecção, registro e contenção de ameaças.

### Splunk / Elastic Stack (ELK)
- **Para que serve:** Plataformas de SIEM (Security Information and Event Management) que centralizam, indexam e analisam logs de servidores, firewalls e aplicações.
- **Cenário de uso:** Correlação de eventos de múltiplos sistemas para identificar comportamentos anômalos (ex: 50 tentativas de login com falha seguidas de um login bem-sucedido às 3h da manhã).
- **Como a defesa se beneficia:** Reduz drasticamente o tempo de detecção de invasões e fornece trilha de auditoria completa para perícia forense.

### Snort / Suricata
- **Para que serve:** Sistemas de Detecção e Prevenção de Intrusão em Redes (NIDS/NIPS). Inspecionam o tráfego em busca de assinaturas conhecidas de ataques e tráfego malicioso.
- **Cenário de uso:** Bloqueio automático de tentativas de varreduras de portas ou pacotes de exploits conhecidos antes que atinjam o servidor de aplicação.
- **Como a defesa se beneficia:** Primeira linha de defesa perimetral em nível de rede.

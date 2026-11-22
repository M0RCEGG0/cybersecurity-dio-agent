# Simulação: Command Injection & Vazamento de Credenciais

Este laboratório demonstra o processo de auditoria de código (DevSecOps) utilizando o **DIO Agent** para identificar e remediar vulnerabilidades críticas em um utilitário de diagnóstico de rede.

---

## 🎯 Cenário Avaliado

O script `server_ping_vulnerable.py` foi submetido à análise do agente com o objetivo de auditar potenciais riscos antes de uma hipotética ida para produção.

---

## 🔍 Relatório do Agente (Hermes / DIO Agent)

O agente utilizou a skill `secure-code-review` e identificou duas vulnerabilidades críticas:

### 1. Injeção de Comando no SO (OS Command Injection — MITRE T1059 / OWASP A03)
- **Vulnerabilidade:** O comando era construído via concatenação de strings (`f"ping -c 2 {target_ip}"`) e executado através de `os.system()`, que invoca o shell do sistema operacional.
- **Vetor de Exploração:** O envio de metacaracteres de encadeamento de comandos (`8.8.8.8; cat /etc/passwd` ou `127.0.0.1 && whoami`) permitiria Execução Remota de Código (RCE) com os privilégios do processo.
- **Correção Aplicada:** Substituição de `os.system` por `subprocess.run` com lista de argumentos explícita, `shell=False`, validação rigorosa de entrada (rejeitando caracteres especiais) e limite de timeout.

### 2. Credenciais Hardcoded no Código (OWASP A07)
- **Vulnerabilidade:** Chaves de API (`AWS_ACCESS_KEY_ID` e `AWS_SECRET_ACCESS_KEY`) embutidas diretamente no código-fonte em texto claro.
- **Risco:** Qualquer acesso ao repositório ou artefatos expõe as chaves e permite movimentação lateral ou abuso da infraestrutura em nuvem.
- **Correção Aplicada:** Remoção total das credenciais do código, delegando o gerenciamento a variáveis de ambiente (`os.environ`) ou serviços dedicados de cofre (AWS Secrets Manager/Vault).

---

## 📁 Arquivos da Simulação

- `server_ping_vulnerable.py`: Código vulnerável original com concatenação de shell e chaves hardcoded.
- `server_ping_secure.py`: Versão blindada gerada a partir das recomendações do agente.

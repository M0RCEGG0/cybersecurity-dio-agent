# Fundamentos de Segurança da Informação

## A Tríade CIA

A base de toda análise de segurança. Qualquer vulnerabilidade viola pelo menos um desses três princípios.

### Confidencialidade

Garantir que a informação só seja acessada por quem tem permissão.

Exemplos de violação:
- Banco de dados exposto sem autenticação
- Senha trafegando em texto puro (sem HTTPS)
- SQL Injection que retorna dados de outros usuários

Boas práticas:
- Criptografar dados sensíveis em trânsito e em repouso
- Controle de acesso por menor privilégio
- Autenticação forte (MFA)

---

### Integridade

Garantir que a informação não seja alterada de forma não autorizada.

Exemplos de violação:
- Atacante modifica registros no banco via SQL Injection
- Arquivo adulterado sem que ninguém perceba
- Log de auditoria apagado após invasão

Boas práticas:
- Usar queries parametrizadas para evitar manipulação de banco
- Hashes (SHA-256) para verificar integridade de arquivos
- Logs imutáveis e monitorados

---

### Disponibilidade

Garantir que sistemas e informações estejam acessíveis quando necessário.

Exemplos de violação:
- Ataque de negação de serviço (DoS/DDoS) derruba o servidor
- Ransomware criptografa arquivos e impede acesso
- Falha não tratada derruba a aplicação

Boas práticas:
- Redundância e backups regulares (3-2-1)
- Rate limiting para evitar sobrecarga
- Tratamento de erros para evitar crash da aplicação

---

## Conceitos de Vulnerabilidade

### O que é uma vulnerabilidade

Uma fraqueza em um sistema, código ou processo que pode ser explorada por um atacante para causar dano.

### O que é uma ameaça

Um agente ou evento capaz de explorar uma vulnerabilidade. Pode ser um atacante externo, um funcionário mal-intencionado ou até um erro humano.

### O que é risco

Risco = Probabilidade × Impacto

Um sistema pode ter uma vulnerabilidade grave (impacto alto) mas pouco exposta (probabilidade baixa) — o risco combinado determina a prioridade de correção.

---

## SQL Injection

### O que é

SQL Injection é uma vulnerabilidade que ocorre quando dados fornecidos pelo usuário são inseridos diretamente em uma query SQL sem tratamento. O atacante injeta comandos SQL junto com os dados.

### Por que acontece

O código trata a entrada do usuário como parte do comando SQL, em vez de como dado puro.

Exemplo vulnerável:
```python
query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
```

Se o usuário digitar `' OR '1'='1` como senha, a query vira:
```sql
SELECT * FROM users WHERE username = 'admin' AND password = '' OR '1'='1'
```
A condição `'1'='1'` é sempre verdadeira — o atacante entra sem saber a senha.

### Qual princípio viola

- **Confidencialidade:** acesso a dados de outros usuários
- **Integridade:** possibilidade de alterar ou deletar registros
- **Disponibilidade:** possibilidade de derrubar o banco com comandos destrutivos

### MITRE ATT&CK

T1190 — Exploit Public-Facing Application

### Como corrigir

Usar queries parametrizadas (placeholders). Os dados nunca são interpretados como SQL:

```python
cursor.execute(
    "SELECT * FROM users WHERE username = ? AND password = ?",
    (username, password)
)
```

---

## Boas Práticas de Desenvolvimento Seguro

- Manter sistemas e dependências atualizados
- Utilizar autenticação forte (senhas longas, MFA)
- Aplicar o princípio do menor privilégio
- Nunca confiar em dados externos sem validação
- Usar queries parametrizadas em toda interação com banco de dados
- Monitorar eventos e manter logs de auditoria
- Realizar backups regulares e testados
- Tratar erros sem expor detalhes internos do sistema
- Corrigir vulnerabilidades conhecidas (CVEs) com patches

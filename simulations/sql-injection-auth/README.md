# Simulação: Vulnerabilidade de Autenticação com SQL Injection

Este diretório contém uma aplicação de teste educacional para demonstrar a exploração e a correção de uma vulnerabilidade clássica de **SQL Injection** em fluxo de login.

---

## 🎯 Objetivo da Simulação

1. **Demonstrar a Falha (`app_vulnerable.py`):**
   - A query SQL é montada por concatenação de strings direta (`f-string`).
   - Entrada maliciosa como `' OR '1'='1` bypassa a validação de senha sem conhecer credenciais legítimas.
   - MITRE ATT&CK: **T1190** (Exploit Public-Facing Application).
   - OWASP Top 10 (2021): **A03 — Injection**.

2. **Demonstrar a Correção (`app_secure.py`):**
   - A query é refatorada utilizando **consultas parametrizadas (placeholders `?`)**.
   - O SQLite trata qualquer entrada do usuário estritamente como dado literal, neutralizando a injeção.
   - Tratamento de exceções e fechamento seguro de conexão com `try/finally`.

---

## 📁 Arquivos da Simulação

- `app_vulnerable.py`: Versão insegura com concatenação de strings.
- `app_secure.py`: Versão corrigida e segura com query parametrizada.
- `app.py`: Versão de execução padrão do laboratório.
- `users_bank.db`: Banco de dados SQLite local contendo a tabela `users` para teste de autenticação.

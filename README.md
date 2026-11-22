# 🛡️ Cybersecurity DIO Agent — AI Security Mentor

![Cybersecurity](https://img.shields.io/badge/Cybersecurity-AI%20Agent-red?style=for-the-badge&logo=hackthebox)
![Santander Bootcamp](https://img.shields.io/badge/Santander%20Bootcamp-Ciberseguran%C3%A7a%202026-orange?style=for-the-badge)
![DIO](https://img.shields.io/badge/DIO-Digital%20Innovation%20One-blue?style=for-the-badge)
![Standard](https://img.shields.io/badge/Standard-AGENTS.md-purple?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed%20%7C%20Actively%20Evolving-brightgreen?style=for-the-badge)

---

## 📖 Visão Geral

Este projeto é uma especialização avançada do **DIO Agent** — um agente de inteligência artificial desenhado sob o padrão aberto `AGENTS.md`. 

A versão base da DIO atua como um mentor geral de estudos de programação. Nesta evolução, transformamos o agente em um **Mentor Especialista em Cibersegurança e DevSecOps**, capaz de conduzir análises defensivas, auditar código-fonte, mapear ameaças arquiteturais e guiar planos de resposta a incidentes de forma metódica e didática.

> **Zero Fine-Tuning, Puro Context Engineering:** Nenhum modelo precisou ser retreinado. O agente aprende e especializa suas decisões com base no que está documentado nos manifestos de `skills/`, na `agent/persona.md` e na base de conhecimento em `agent/knowledge/`.

---

## ⚖️ Repositório Base vs. Especialização em Cibersegurança

Para demonstrar com transparência o valor técnico agregado neste projeto, a tabela abaixo compara os recursos originais do template da DIO com os módulos desenvolvidos nesta versão:

| Componente | Base Original DIO | Especialização em Cibersegurança (Criado neste projeto) |
|---|---|---|
| **Persona (`agent/persona.md`)** | Mentor educacional para transição de carreira e dúvidas genéricas. | Especialização de Blue Team / AppSec: postura investigativa, foco defensivo e recusa de respostas prontas para cópia. |
| **Base de Conhecimento (`agent/knowledge/`)** | Plataforma DIO (`dio-platform.md`) e tipos de experiências (`learning-experiences.md`). | • `security-basics.md` (Tríade CIA, Risco e SQLi)<br>• `attack-techniques.md` (17 técnicas com MITRE ATT&CK)<br>• `owasp-top10.md` (OWASP Top 10 2021 com mitigações)<br>• `security-tools.md` (Nmap, Wireshark, Burp, Metasploit, SIEM) |
| **Habilidades (`skills/`)** | Plano de estudos, destravar desafios, explicar conceitos e busca na web. | • `vulnerability-analysis` (Análise de riscos e CVEs)<br>• `secure-code-review` (Revisão estática de vulnerabilidades no código)<br>• `incident-response` (Ciclo de contenção e recuperação NIST)<br>• `threat-modeling` (Modelagem de ameaças com STRIDE) |
| **Laboratório de Testes (`simulations/`)** | Não continha aplicações de teste ou laboratórios práticos. | Criação de ambiente de simulação com casos reais de vulnerabilidades (SQLi e Command Injection) e versões auditadas pelo agente. |

---

## 🧩 As 4 Skills Especializadas de Cibersegurança

O agente sabe exatamente quando carregar cada habilidade a partir da intenção da sua mensagem:

| Skill | Escopo de Atuação | Framework de Referência | Exemplo de Pergunta / Prompt |
|---|---|---|---|
| **[Análise de Vulnerabilidades](skills/vulnerability-analysis/SKILL.md)** | Diagnóstico de falhas em servidores e avaliação de severidade/impacto. | MITRE ATT&CK / CVSS | *"Encontrei uma porta 21 aberta em um servidor legado, qual o risco e como investigo?"* |
| **[Revisão de Código Seguro](skills/secure-code-review/SKILL.md)** | Auditoria estática de código-fonte (SAST) buscando injeções e segredos. | OWASP Top 10 / DevSecOps | *"Hermes, pode revisar esse script Python em busca de falhas de segurança?"* |
| **[Resposta a Incidentes](skills/incident-response/SKILL.md)** | Orientação para contenção imediata, preservação de RAM e recuperação. | NIST SP 800-61 | *"Suspeito que um servidor foi invadido e tem ransomware ativo, o que faço primeiro?"* |
| **[Modelagem de Ameaças](skills/threat-modeling/SKILL.md)** | Identificação de brechas de arquitetura antes de programar (Security by Design). | Microsoft STRIDE | *"Estou desenhando a arquitetura de uma API de pagamento, como aplico o STRIDE nela?"* |

---

## 🧪 Laboratório de Simulações (`simulations/`)

O projeto inclui cenários práticos projetados para auditar e validar a capacidade técnica do agente em identificar problemas reais:

### 1. [SQL Injection em Fluxo de Autenticação](simulations/sql-injection-auth/)
- **Vulnerabilidade:** Montagem de query SQL com `f-string`, permitindo bypass completo de autenticação via `' OR '1'='1`.
- **Mitigação:** Parametrização estrita de consultas (placeholders `?`) e gerenciamento seguro de conexões SQLite com `try/finally`.
- **Arquivos:** `app_vulnerable.py` vs. `app_secure.py`.

### 2. [OS Command Injection & Credenciais Expostas](simulations/command-injection-api/)
- **Vulnerabilidade:** Utilitário de diagnóstico de rede concatenando parâmetros no `os.system()` (RCE via `;` ou `&&`) e chaves da AWS gravadas em texto plano.
- **Auditoria do Hermes:** O agente identificou as duas falhas críticas, recomendou a substituição por `subprocess.run(shell=False)` e gerou o código blindado com validação por regex e biblioteca `ipaddress`.
- **Arquivos:** `server_ping_vulnerable.py` vs. `server_ping_secure.py`.

---

## 🚀 Como Executar o Agente

O DIO Agent é compatível com qualquer harness que implemente a especificação aberta `AGENTS.md` (Hermes, Google Antigravity, Claude Code, Codex, OpenCode).

### 1. Clone o repositório
```bash
git clone https://github.com/M0RCEGG0/cybersecurity-dio-agent.git
cd cybersecurity-dio-agent
```

### 2. Abra a pasta no seu Harness
No caso do **Hermes Agent** via terminal do VS Code:
```bash
hermes
```
O harness lê automaticamente as instruções do arquivo `AGENTS.md` e inicializa o agente como mentor de segurança.

### 3. Converse
Faça perguntas sobre segurança, envie trechos de código para revisão ou peça apoio em arquiteturas de sistemas.

---

## 🗺️ Roadmap & Evolução Contínua

Este projeto foi formalmente concluído e entregue para o **Bootcamp Santander Cibersegurança 2026**, porém está sob **ciclo de evolução ativa**. Novas funcionalidades planejadas para as próximas versões:

- [ ] **Skill de Análise Forense:** Guia para análise de dumps de memória volátil e extração de evidências com Volatility.
- [ ] **Skill de Engenharia Reversa:** Metodologia de descompilação e análise comportamental estática de binários em sandbox.
- [ ] **Simulação de SSRF & IDOR:** Expansão da pasta `simulations/` com cenários de falhas modernas de controle de acesso (OWASP A01).
- [ ] **Integração com Ferramentas CLI:** Configuração de MCP (Model Context Protocol) para permitir que o agente execute varreduras locais controladas com Nmap e ZAP.

---

## 🤖 Ecossistema de IA & Créditos

Este laboratório foi construído com o suporte de ferramentas de Inteligência Artificial utilizadas de ponta a ponta como mentoras de aprendizado, validação de arquitetura e parceiras de code review:

- **Hermes Agent (Nous Research):** Harness de execução local utilizado para os testes e auditorias dos códigos.
- **Antigravity (Google DeepMind):** Revisão de documentação, estruturação do repositório e suporte de arquitetura.
- **Gemini (Google):** Pesquisa e consolidação técnica das referências de cibersegurança.

Projeto desenvolvido como parte do **Bootcamp Santander Cibersegurança 2026** em parceria com a **DIO (Digital Innovation One)**.

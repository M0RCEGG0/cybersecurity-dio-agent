---
name: threat-modeling
description: Use quando o estudante quiser desenhar ou avaliar a segurança da arquitetura de um sistema, mapear vetores de ataque potenciais ou aplicar a metodologia STRIDE antes de escrever código.
---

# Skill: Modelagem de Ameaças (Threat Modeling)

Guia o agente a conduzir uma sessão prática e estruturada de modelagem de ameaças com o estudante, utilizando o framework **STRIDE** (desenvolvido pela Microsoft).

O objetivo é ensinar a mentalidade de "Security by Design": identificar brechas conceituais e estruturais na arquitetura do sistema antes mesmo da primeira linha de código ser escrita.

---

# Quando Usar

Use esta skill quando o estudante:

- descrever a arquitetura de uma aplicação (front-end, API, banco de dados, integrações externas)
- perguntar "como avaliar os riscos dessa ideia/projeto?"
- quiser aprender ou aplicar a metodologia STRIDE
- estiver planejando um novo sistema e quiser evitar falhas de arquitetura (Insecure Design - OWASP A04)

---

## 1. Mapear o Diagrama do Sistema

Antes de listar ameaças, entenda o fluxo de dados:

1. **Atores e Componentes:**
   - Quem usa o sistema? (Usuário comum, admin, sistemas parceiros)
   - Quais são os componentes? (Web App, API Gateway, Microserviços, Banco de Dados, Cloud Storage)
2. **Fronteiras de Confiança (Trust Boundaries):**
   - Onde os dados saem de uma área não confiável (Internet pública) para uma área confiável (rede interna corporativa)?

---

## 2. Aplicar o Modelo STRIDE

Avalie cada componente e fluxo de dados contra as 6 categorias de ameaça:

### S — Spoofing (Falsificação de Identidade)
- **Risco:** Um atacante se passar por um usuário legítimo ou forjar a identidade de outro serviço.
- **Pergunta norteadora:** "Como sabemos com 100% de certeza que quem enviou essa requisição é quem diz ser?"
- **Defesa:** Autenticação multifator (MFA), tokens assinados (JWT com chave segura), certificados TLS mútuos (mTLS).

### T — Tampering (Adulteração de Dados)
- **Risco:** Dados serem modificados em trânsito pela rede ou em repouso no banco de dados sem autorização.
- **Pergunta norteadora:** "Alguém conseguiria alterar os parâmetros ou o valor desta transação no meio do caminho?"
- **Defesa:** HTTPS/TLS obrigatório, assinaturas digitais, hashes (SHA-256), integridade de banco de dados.

### R — Repudiation (Repúdio / Negativa de Autoria)
- **Risco:** Um usuário executar uma ação crítica (ex: excluir um registro financeiro) e o sistema não conseguir provar quem foi.
- **Pergunta norteadora:** "Se alguém negar que fez essa ação, temos provas forenses auditáveis?"
- **Defesa:** Logs de auditoria centralizados, imutáveis, sincronizados com servidor NTP e assinados.

### I — Information Disclosure (Vazamento de Informação)
- **Risco:** Exposição indevida de dados sensíveis para quem não deveria visualizá-los.
- **Pergunta norteadora:** "Se o tráfego for interceptado ou o banco for copiado, o que o invasor consegue ler?"
- **Defesa:** Criptografia em repouso e em trânsito, mascaramento de dados (data masking), tratamento genérico de erros.

### D — Denial of Service (Negação de Serviço)
- **Risco:** O sistema ficar indisponível devido a esgotamento de recursos (CPU, memória, conexões de banco de dados).
- **Pergunta norteadora:** "O que acontece se um usuário enviar 100.000 requisições simultâneas para este endpoint pesado?"
- **Defesa:** Rate limiting, WAF (Web Application Firewall), timeouts bem definidos, balanceamento de carga.

### E — Elevation of Privilege (Elevação de Privilégio)
- **Risco:** Um usuário comum conseguir acessar funções exclusivas de administradores.
- **Pergunta norteadora:** "O que impede este usuário de manipular seu ID ou token para virar admin?"
- **Defesa:** Princípio do menor privilégio, validação de autorização (RBAC/ABAC) estritamente no servidor.

---

## 3. Priorizar e Propor Mitigações

Ajude o estudante a transformar as ameaças encontradas em um plano de ação:

- Listar as ameaças de maior impacto primeiro (geralmente Spoofing e Elevation of Privilege).
- Propor controles compensatórios arquiteturais simples e modernos.

---

## 4. Verificar o Aprendizado

Finalize a sessão confirmando o entendimento:
- "Qual das letras do STRIDE você achou mais crítica para a sua arquitetura?"
- "Consegue ver como aplicar isso antes de codificar economiza tempo de retrabalho e correções?"

---

# Formato das Respostas

Estrutura recomendada:

## 🗺️ Visão dos Componentes
Resumo dos fluxos e fronteiras de confiança identificados.

## ⚠️ Matriz STRIDE de Ameaças
Tabela rápida apontando cada risco identificado nas letras do STRIDE.

## 🛡️ Controles Recomendados
Medidas arquiteturais preventivas para blindar o sistema.

---

# Regras

Nunca:
- considere uma arquitetura segura apenas porque o código ainda não foi feito
- esqueça de avaliar conexões com terceiros e APIs externas

Sempre:
- ensine que a segurança de arquitetura (Security by Design) é mais barata do que corrigir falhas em produção
- conduza o estudante a pensar ativamente sobre cada vetor do STRIDE

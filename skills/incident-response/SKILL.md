---
name: incident-response
description: Use quando o estudante relatar um incidente de segurança, suspeita de invasão, comprometimento de servidor, vazamento de credenciais ou ransomware, e precisar de um plano de contenção e recuperação.
---

# Skill: Resposta a Incidentes de Segurança

Guia o agente a orientar o estudante de forma metódica e defensiva durante incidentes de segurança, seguindo as melhores práticas do framework NIST SP 800-61.

O objetivo é evitar ações impulsivas que destruam evidências forenses ou agravem o ataque, ensinando o raciocínio estruturado de contenção, investigação e recuperação.

---

# Quando Usar

Use esta skill quando o estudante:

- relatar que um servidor, sistema ou banco de dados foi invadido
- suspeitar de credenciais ou tokens de API vazados
- identificar atividades anômalas (tráfego de rede estranho, processos desconhecidos consumindo recursos)
- enfrentar ataque de ransomware ou sequestro de dados
- pedir ajuda para conduzir uma simulação de resposta a incidentes

---

## 1. Triagem e Avaliação de Emergência

Antes de sugerir qualquer comando destrutivo ou reinicialização, oriente com calma:

1. **Evitar o pânico e preservar evidências:**
   - **NÃO reiniciar a máquina:** O desligamento apaga dados voláteis críticos armazenados na memória RAM (processos ativos, conexões de rede ativas e chaves de criptografia em memória).
   - **NÃO apagar logs:** Eles são o único mapa para entender a extensão do dano.

2. **Perguntar o cenário inicial:**
   - Qual sistema ou máquina foi afetado? (Ambiente de testes, lab, produção?)
   - Qual sintoma foi observado? (Alerta de antivírus, ransom note, tráfego anormal?)
   - O ataque parece estar em andamento no momento?

---

## 2. Contenção Imediata (Interromper o Sangramento)

O primeiro foco é impedir que o atacante avance para outros sistemas (movimento lateral) ou continue exfiltrando dados:

- **Isolamento de Rede:** Desconectar interfaces de rede ou aplicar regras de firewall restritivas bloqueando tráfego externo e lateral.
- **Revogação de Credenciais:** Invalidar senhas de contas comprometidas, revogar sessões ativas e trocar tokens/chaves de API expostas.
- **Isolamento de Contas:** Suspender temporariamente contas com privilégios suspeitos.

---

## 3. Investigação e Erradicação (Identificar a Causa Raiz)

Descubra por onde o atacante entrou e elimine sua presença:

- **Análise da Entrada (Vetor Inicial):**
  - Revisar logs de autenticação (ex: falhas seguidas de sucesso indicando força bruta).
  - Revisar logs de servidores web procurando requisições maliciosas (injeções, exploração de CVEs).
- **Remoção de Persistência:**
  - Identificar e eliminar processos maliciosos ativos.
  - Verificar tarefas agendadas (Cron no Linux, Task Scheduler no Windows) e serviços criados recentemente.
  - Verificar chaves SSH autorizadas (`~/.ssh/authorized_keys`) e novas contas de usuário criadas.

---

## 4. Recuperação Segura (Retorno à Operação)

Restabelecer os serviços de forma confiável e monitorada:

- **Restauração Confiável:**
  - Restaurar sistemas a partir de backups confiáveis anteriores à data do comprometimento confirmado.
  - Aplicar patches em todas as vulnerabilidades que permitiram a entrada do invasor antes de religar à rede.
- **Monitoramento Reforçado:**
  - Acompanhar de perto os logs e o tráfego do sistema recuperado nas primeiras 48h para garantir que não há reincidência.

---

## 5. Lições Aprendidas (Prevenção Futura)

Finalize a resposta orientando o estudante a refletir e fortalecer a postura de segurança:

- O que falhou na defesa original?
- Quais controles defensivos poderiam ter prevenido ou detectado o ataque mais cedo? (Ex: MFA obrigatório, EDR, segmentação de rede, backups 3-2-1).
- Documentar o incidente e as ações tomadas.

---

# Formato das Respostas

Sempre que guiar um incidente, estruture a resposta de maneira clara e prioritária:

## ⚠️ Ação Imediata (Não Perca o Controle)
O que fazer no primeiro minuto (isolar, não reiniciar).

## 🛡️ Contenção
Passo a passo para conter a disseminação da ameaça.

## 🔍 Investigação e Causa Raiz
Como inspecionar o que aconteceu e remover a persistência do atacante.

## 🔄 Recuperação e Blindagem
Como restabelecer o ambiente e garantir que o mesmo vetor não seja usado novamente.

---

# Regras

Nunca:
- sugira comandos que destruam evidências antes da contenção
- aconselhe o pagamento de resgate em caso de ransomware
- assuma a extensão do ataque sem orientar a checagem de logs

Sempre:
- mantenha uma postura calma, técnica e encorajadora
- priorize a segurança dos dados e o isolamento perimetral
- ensine o raciocínio investigativo de um analista de SOC / Blue Team

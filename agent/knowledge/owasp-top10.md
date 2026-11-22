# OWASP Top 10 — As 10 Vulnerabilidades Web Mais Críticas

A **OWASP** (Open Worldwide Application Security Project) é uma organização sem fins lucrativos dedicada a melhorar a segurança de software. O **OWASP Top 10** é uma lista publicada periodicamente com as vulnerabilidades web mais críticas do mundo, amplamente usada como referência por desenvolvedores, times de segurança e auditores.

A edição vigente é a de **2021**. Conhecer essa lista é o ponto de partida para qualquer profissional de segurança.

---

## A01 — Broken Access Control (Controle de Acesso Quebrado)

### O que é

O sistema não verifica corretamente se o usuário tem permissão para acessar um recurso. É a vulnerabilidade mais comum desde 2021.

### Exemplo prático

Um usuário comum acessa `https://sistema.com/admin/relatorios` simplesmente digitando a URL — sem ser administrador. O sistema não verificou o perfil antes de exibir a página.

### CIA violado

- Confidencialidade — acesso a dados de outros usuários
- Integridade — possibilidade de alterar registros sem permissão

### Como mitigar

- Negar acesso por padrão — liberar apenas o que for explicitamente autorizado
- Verificar permissões no servidor, nunca só no front-end
- Registrar tentativas de acesso negado e gerar alertas

---

## A02 — Cryptographic Failures (Falhas Criptográficas)

### O que é

Dados sensíveis trafegam ou são armazenados sem criptografia adequada, ou com algoritmos fracos e obsoletos.

### Exemplo prático

Senhas armazenadas em MD5 (quebrado) em vez de bcrypt. Dados de cartão de crédito trafegando por HTTP em vez de HTTPS.

### CIA violado

- Confidencialidade — dados sensíveis expostos em texto puro

### Como mitigar

- Usar HTTPS em toda comunicação
- Armazenar senhas com algoritmos modernos: bcrypt, Argon2 ou scrypt
- Nunca usar MD5 ou SHA-1 para dados sensíveis
- Criptografar dados em repouso (banco de dados, backups)

---

## A03 — Injection (Injeção)

### O que é

Dados fornecidos pelo usuário são interpretados como comandos pelo sistema, em vez de serem tratados como dados puros. Inclui SQL Injection, Command Injection e Cross-Site Scripting (XSS).

### Exemplo prático

Campo de login aceita `' OR '1'='1` como senha e concede acesso sem verificar credenciais reais.

### CIA violado

- Confidencialidade — leitura de dados não autorizados
- Integridade — alteração ou deleção de registros
- Disponibilidade — destruição de dados com comandos como `DROP TABLE`

### Como mitigar

- Usar queries parametrizadas (placeholders) em toda interação com banco de dados
- Validar e sanitizar toda entrada do usuário
- Aplicar o princípio do menor privilégio no banco de dados

---

## A04 — Insecure Design (Design Inseguro)

### O que é

A falha está na arquitetura ou no modelo de negócio do sistema, não apenas no código. Nenhum patch corrige um design fundamentalmente inseguro.

### Exemplo prático

Um sistema de recuperação de senha baseado em perguntas secretas ("qual o nome do seu pet?") — a resposta é adivinhável por engenharia social, independente do código estar correto.

### CIA violado

- Confidencialidade e Integridade — depende da falha de design específica

### Como mitigar

- Aplicar Threat Modeling (modelagem de ameaças) antes de desenvolver
- Seguir padrões de design seguro desde o início (Security by Design)
- Revisar fluxos de negócio com olhar de segurança

---

## A05 — Security Misconfiguration (Configuração Incorreta de Segurança)

### O que é

O sistema está funcional, mas configurado de forma insegura: portas abertas desnecessariamente, credenciais padrão mantidas, mensagens de erro expondo detalhes internos.

### Exemplo prático

Banco de dados com usuário `root` sem senha, acessível pela internet. Servidor web exibindo stack trace completo com nomes de arquivos e versões ao ocorrer um erro.

### CIA violado

- Confidencialidade — exposição de informações internas
- Disponibilidade — superfície de ataque ampliada

### Como mitigar

- Desabilitar funcionalidades, portas e serviços que não são usados
- Trocar todas as credenciais padrão antes de colocar em produção
- Exibir mensagens de erro genéricas para o usuário; registrar detalhes apenas em log interno

---

## A06 — Vulnerable and Outdated Components (Componentes Vulneráveis e Desatualizados)

### O que é

A aplicação usa bibliotecas, frameworks ou sistemas operacionais com vulnerabilidades conhecidas (CVEs) que já têm correção disponível mas não foram aplicadas.

### Exemplo prático

Aplicação usando uma versão antiga do Log4j — vulnerável ao Log4Shell (CVE-2021-44228), uma das falhas mais críticas da história, que permite execução remota de código.

### CIA violado

- Todos os três — depende da vulnerabilidade do componente

### Como mitigar

- Manter um inventário de todas as dependências e suas versões
- Monitorar CVEs das bibliotecas usadas (ferramentas como Dependabot, Snyk)
- Atualizar dependências regularmente e remover as que não são mais usadas

---

## A07 — Identification and Authentication Failures (Falhas de Identificação e Autenticação)

### O que é

O sistema não protege adequadamente o processo de login e o gerenciamento de sessões, permitindo que atacantes assumam identidades de outros usuários.

### Exemplo prático

Sistema permite tentativas ilimitadas de senha (sem rate limiting), facilitando brute force. Sessão não é invalidada após logout — token antigo ainda funciona.

### CIA violado

- Confidencialidade — acesso indevido à conta de outro usuário

### Como mitigar

- Implementar autenticação multifator (MFA)
- Bloquear ou adicionar delay após tentativas excessivas de login
- Invalidar tokens de sessão no logout e após expiração
- Usar senhas longas e verificar contra listas de senhas conhecidas

---

## A08 — Software and Data Integrity Failures (Falhas de Integridade de Software e Dados)

### O que é

O sistema confia em atualizações, plugins ou dados externos sem verificar sua autenticidade e integridade. Inclui pipelines de CI/CD comprometidos.

### Exemplo prático

Aplicação instala atualização automática de um CDN externo sem verificar assinatura digital — um atacante que comprometa o CDN distribui código malicioso para todos os usuários.

### CIA violado

- Integridade — código ou dados adulterados entram no sistema
- Disponibilidade — sistema comprometido pode ser derrubado

### Como mitigar

- Verificar assinaturas digitais de pacotes e atualizações
- Usar repositórios confiáveis e fixar versões de dependências
- Proteger pipelines de CI/CD com controles de acesso e auditoria

---

## A09 — Security Logging and Monitoring Failures (Falhas de Log e Monitoramento)

### O que é

O sistema não registra eventos relevantes de segurança ou não monitora os logs existentes. Sem visibilidade, ataques não são detectados nem investigados.

### Exemplo prático

Após um vazamento de dados, a empresa descobre que não há logs de acesso ao banco de dados — é impossível saber o que foi acessado, quando e por quem.

### CIA violado

- Todos os três — a falha não causa o ataque, mas impede a detecção e resposta

### Como mitigar

- Registrar tentativas de login (sucesso e falha), acessos a dados sensíveis e alterações de permissão
- Proteger os logs contra alteração (logs imutáveis)
- Configurar alertas para padrões anômalos (muitas falhas de login, acesso fora do horário)

---

## A10 — Server-Side Request Forgery (SSRF — Falsificação de Requisição do Lado do Servidor)

### O que é

O atacante faz o servidor da aplicação realizar requisições HTTP para destinos que ele controla — incluindo serviços internos que normalmente não seriam acessíveis.

### Exemplo prático

Uma funcionalidade de "preview de URL" aceita qualquer endereço. O atacante envia `http://169.254.169.254/latest/meta-data/` (endereço interno de metadados em ambientes cloud) e obtém credenciais do servidor.

### CIA violado

- Confidencialidade — acesso a serviços e dados internos
- Integridade — possibilidade de acionar ações internas

### Como mitigar

- Validar e restringir as URLs que a aplicação pode requisitar
- Bloquear requisições para endereços internos (127.0.0.1, 169.254.x.x, 10.x.x.x)
- Usar allowlist de domínios permitidos em vez de blocklist

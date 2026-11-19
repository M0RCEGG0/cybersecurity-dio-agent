---
name: secure-code-review
description: Use quando o estudante quiser revisar um trecho de código em busca de falhas de segurança, como SQL Injection, senhas hardcoded, falta de validação de entrada ou exposição de dados sensíveis.
---

# Skill: Revisão de Código Seguro

Guia o agente a analisar trechos de código com olhar de segurança, ensinando o estudante a identificar vulnerabilidades antes que cheguem à produção.

O objetivo não é apenas apontar o problema, mas ensinar o raciocínio por trás de cada falha e como corrigi-la com boas práticas.

---

# Quando Usar

Use esta skill quando o estudante:

- compartilhar um trecho de código e pedir revisão de segurança
- quiser saber se o código está "seguro"
- perguntar sobre boas práticas de código
- quiser entender por que uma prática é perigosa
- estiver aprendendo desenvolvimento seguro (DevSecOps)

---

## 1. Peça o Código e o Contexto

Antes de analisar, colete:

- Qual linguagem e framework está sendo usado?
- O código é de estudo ou produção?
- Qual é a função desse trecho no sistema?

Se o estudante já compartilhou o código, passe direto para a análise.

---

## 2. Analise o Código

Examine o trecho buscando as categorias de falha mais comuns:

### Injeção
- SQL montado com f-string ou concatenação de strings
- Comandos do sistema operacional construídos com entrada do usuário
- Queries sem uso de placeholders ou ORM

### Autenticação e Credenciais
- Senhas ou tokens hardcoded no código (`password = "admin123"`)
- Chaves de API expostas diretamente no código-fonte
- Ausência de hashing em senhas armazenadas

### Validação de Entrada
- Dados do usuário usados sem sanitização ou validação
- Ausência de verificação de tipo, tamanho ou formato
- Redirecionamentos baseados em parâmetros não validados

### Exposição de Dados
- Mensagens de erro que revelam estrutura interna do sistema
- Logs que registram senhas ou tokens
- Respostas de API com mais dados do que o necessário

### Controle de Acesso
- Ausência de verificação de permissão antes de operações sensíveis
- Funções administrativas acessíveis sem autenticação

---

## 3. Explique Cada Falha Encontrada

Para cada problema identificado, explique:

- O que é a falha e por que ela existe no código
- Como um atacante poderia explorá-la
- Qual princípio da tríade CIA ela viola
- Referência MITRE ATT&CK quando aplicável

Use linguagem adequada ao nível do estudante. Nunca trate a falha como óbvia.

---

## 4. Mostre a Correção

Apresente o trecho corrigido com comentários explicando a mudança:

- O que foi alterado e por quê
- Qual boa prática foi aplicada
- O que isso impede que aconteça

Não entregue apenas o código corrigido. Explique antes para o estudante entender a lógica da correção.

---

## 5. Verifique o Aprendizado

Ao final, pergunte algo como:

- "Faz sentido por que essa mudança resolve o problema?"
- "Você conseguiria identificar esse padrão em outro trecho de código?"

---

# Formato das Respostas

Sempre que possível, estruture assim:

## Falhas Encontradas

Lista das vulnerabilidades identificadas.

## Análise

Explicação de cada falha: o que é, como funciona, o que viola.

## Código Corrigido

Trecho corrigido com comentários.

## O que Guardar

Uma frase resumindo o aprendizado principal da revisão.

---

# Regras

Nunca:

- entregue apenas o código corrigido sem explicar o problema
- trate uma falha como óbvia ou desnecessária de explicar
- incentive práticas inseguras mesmo que "funcionem"

Sempre:

- explique o raciocínio antes de mostrar a solução
- conecte a falha com um impacto real possível
- reforce que código seguro é responsabilidade do desenvolvedor, não só do time de segurança

# ADR 0002: Arquitetura do Gerador de Assinaturas (BT Blue)

## Status

Accepted

---

## Context

O sistema será um **gerador interno de assinaturas de e-mail**, utilizado por RH e TI da BT Blue.

Características do problema:

- escopo simples e bem definido
- baixo volume de usuários
- uso interno (sem multi-tenant)
- foco em geração de HTML compatível com Outlook
- principal valor: **padronização + eficiência operacional**
- risco principal: **overengineering e baixa adoção**

Requisitos relevantes:

- formulário simples
- geração de HTML via template
- preview
- copiar assinatura
- configuração institucional centralizada
- manutenção fácil

---

## Decision

A arquitetura adotada será:

### **Monólito modular (modular monolith)**

Com as seguintes características:

- backend único (FastAPI)
- renderização de templates via Jinja2
- separação lógica por camadas (sem excesso de abstração)
- sem microserviços
- sem mensageria
- sem arquitetura distribuída

---

## Alternatives Considered

### 1. Monólito simples (sem separação interna)

**Prós**

- extremamente rápido de implementar

**Contras**

- tende a virar código bagunçado rapidamente
- difícil manutenção após evolução mínima

👉 Rejeitado por risco de desorganização

---

### 2. Microserviços

**Prós**

- escalabilidade e isolamento

**Contras**

- COMPLETAMENTE desnecessário
- alto custo operacional
- complexidade absurda para o problema

👉 Rejeitado por overengineering

---

### 3. Monólito modular (escolhido)

**Prós**

- simples de implementar
- organizado desde o início
- fácil evolução
- baixo acoplamento interno
- sem custo operacional extra

**Contras**

- exige disciplina mínima de organização

---

## Decision Drivers

- simplicidade
- facilidade de manutenção
- clareza de responsabilidades
- baixo custo de evolução
- evitar complexidade prematura

---

## Trade-offs

Ao não usar uma arquitetura mais complexa:

**Perdemos**

- isolamento extremo de componentes
- escalabilidade independente

**Ganhamos**

- velocidade de entrega
- menor custo cognitivo
- menor custo de manutenção
- menor risco de erro arquitetural

---

## Consequences

### Positivas

- código fácil de entender
- onboarding técnico simples
- manutenção barata
- evolução incremental segura

### Negativas

- crescimento exige disciplina
- modularização depende do time (não só do framework)

---

## Diretrizes obrigatórias

- separar **API / domínio / templates**
- evitar camadas artificiais
- manter **lógica de negócio em serviços**
- templates devem ser **estáticos e controlados**
- não introduzir abstrações sem necessidade real

---

# Estrutura de Pastas (Recomendada)

Aqui está uma estrutura:

app/
├── main.py                # entrypoint FastAPI
│
├── api/                   # camada HTTP
│   ├── routes/
│   │   ├── signature.py
│   │   ├── settings.py
│   │   └── health.py
│   └── dependencies.py
│
├── domain/                # regra de negócio
│   ├── schemas/
│   │   ├── signature.py
│   │   └── settings.py
│   │
│   ├── services/
│   │   ├── signature_service.py
│   │   ├── template_service.py
│   │   └── validation_service.py
│
├── templates/             # HTML (Jinja2)
│   ├── email/
│   │   └── default_signature.html
│   └── pages/
│       └── index.html
│
├── core/                  # config e setup
│   ├── config.py
│   └── security.py
│
├── infrastructure/        # integração externa (futuro)
│   └── repository/
│
└── static/                # css, js (se necessário)

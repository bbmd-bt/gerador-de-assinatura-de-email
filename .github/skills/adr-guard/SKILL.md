---
name: adr-guard
description: "Enforce ADR (Architecture Decision Records) consistency. USE FOR: before writing code, suggesting architecture, changing tech stack, proposing database schema, or evaluating any technical approach — read the ADRs in /docs/adr/ first and flag contradictions. USE WHEN: user asks to add a feature, change architecture, pick a library, or modify the tech stack. Trigger phrases: ADR, architecture decision, tech stack, database, microservice, framework choice, architectural change, design decision."
---

# ADR Guard

Ensure every technical suggestion is consistent with the project's Architecture Decision Records (ADRs) stored in `/docs/adr/`.

## Workflow

### Step 1 — Load All ADRs

Read every file in `/docs/adr/` before producing any technical output.

For each ADR, extract:
- **ID** (e.g., ADR-0001)
- **Status** (Accepted / Deprecated / Superseded)
- **Decision summary** (one sentence)
- **Key constraints** it imposes (tech, patterns, anti-patterns)

Only consider ADRs with status **Accepted** as binding. Deprecated or superseded ADRs are informational only.

### Step 2 — Analyse the User Request

Map the request to the relevant ADR constraints:

| Request type | ADRs to check |
|---|---|
| Language / framework choice | ADR-0001 |
| Architecture pattern (layers, services, messaging) | ADR-0002 |
| Database / persistence | ADR-0001, ADR-0002 |
| New microservice or distributed component | ADR-0002 |
| Any other significant technical decision | All accepted ADRs |

### Step 3 — Check for Contradictions

A contradiction exists when the proposed change **violates a constraint** from an accepted ADR.

Examples of contradictions in this project:
- Proposing microservices → violates ADR-0002 (modular monolith)
- Adding a message broker (e.g., RabbitMQ, Kafka) → violates ADR-0002 (no messaging)
- Switching from Python/FastAPI to another language or framework → violates ADR-0001
- Adding PostgreSQL without a demonstrated persistence need → violates ADR-0001 (only if real need exists)
- Introducing DDD aggregates, CQRS, or event sourcing for this scope → violates ADR-0002 (excess abstraction)

### Step 4 — Respond

**If no contradiction is found:**
Proceed with the suggestion. Briefly note which ADR(s) the approach aligns with.

**If a contradiction is found:**
1. **Alert** the user clearly:
   > ⚠️ This request conflicts with **[ADR-XXXX]: [Title]**.
2. **Explain** what the ADR decided and why.
3. **Propose an aligned alternative** that solves the user's underlying need within the established constraints.
4. If the user's need is genuinely unmet by the current decision, suggest they formally **revise or supersede the ADR** before implementing the change.

## Quality Criteria

A response is complete when:
- [ ] All accepted ADRs have been consulted.
- [ ] Any contradiction is surfaced before code is written.
- [ ] The final suggestion respects the constraints of all accepted ADRs.
- [ ] If no ADRs exist yet, the agent notes the absence and proceeds, recommending the team document the decision.

## Example Prompt

> "I want to split the signature generation into a separate microservice."

Expected behaviour:
1. Load ADR-0002 (Modular Monolith).
2. Detect contradiction: microservice violates the accepted monolith decision.
3. Alert the user, cite ADR-0002, and propose an alternative: extract a well-bounded module inside the monolith instead.

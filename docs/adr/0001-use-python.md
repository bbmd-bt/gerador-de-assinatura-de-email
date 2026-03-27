## ADR 0001: Escolha da pilha tecnológica do gerador interno de assinaturas de e-mail da BT Blue

### Status

Accepted

### Context

A BT Blue precisa de um sistema interno para geração padronizada de assinaturas de e-mail usadas no Microsoft 365, com foco em Outlook Web e Outlook Desktop.

Os usuários principais serão RH e TI. O objetivo do produto é reduzir retrabalho operacional, evitar assinaturas inconsistentes e diminuir dependência do TI para tarefas repetitivas de onboarding e atualização cadastral.

Os requisitos mais importantes do sistema são:

- formulário simples para preenchimento dos dados do colaborador
- validação de dados
- geração de assinatura a partir de template oficial
- preview antes da cópia
- compatibilidade com Outlook
- manutenção simples por TI
- baixo custo operacional
- baixo risco de overengineering

A solução é interna, restrita à BT Blue, sem necessidade de multi-tenant, alta escala distribuída ou monetização externa.

### Decision

Foi escolhida a pilha:

- **Python 3.12+**
- **FastAPI**
- **Jinja2**
- **Docker**
- **PostgreSQL apenas se houver necessidade real de persistência**

A aplicação será implementada como um **monólito simples**, sem microserviços e sem integração automática com Microsoft Graph no MVP.

### Alternatives Considered

#### 1. Python + FastAPI + Jinja2

**Vantagens**

- boa aderência a APIs enxutas e regras simples
- validação clara de dados
- implementação rápida
- fácil renderização de templates HTML
- menor boilerplate
- menor risco de abstrações desnecessárias
- testes simples com pytest/HTTPX, conforme documentação oficial do FastAPI.

**Desvantagens**

- menos estrutura “opinionated” que NestJS
- se o sistema crescer muito, pode exigir disciplina maior de organização interna

---

#### 2. Node.js + NestJS + template engine

**Vantagens**

- forte estrutura modular
- excelente suporte a TypeScript
- injeção de dependência nativa no framework
- bom encaixe para projetos que crescem em múltiplos módulos e integrações.

**Desvantagens**

- maior volume de estrutura para um problema simples
- maior custo cognitivo no MVP
- risco mais alto de overengineering
- maior tendência a desenhar camadas e abstrações antes da necessidade real

### Decision Drivers

Os principais critérios que guiaram a decisão foram:

1. **simplicidade de implementação**
2. **facilidade de manutenção por TI**
3. **clareza da regra de negócio**
4. **rapidez para entregar MVP**
5. **baixo risco de overengineering**
6. **boa experiência para RH como usuário operacional**
7. **compatibilidade com um backend centrado em geração de HTML**

### Trade-offs

A decisão por Python/FastAPI sacrifica parte da estrutura arquitetural rígida que o NestJS oferece.

Em troca, ganha-se:

- menor complexidade inicial
- menor boilerplate
- menor tempo de entrega
- maior legibilidade para regras de template e validação

Ou seja, foi priorizada **adequação ao problema atual** em vez de capacidade de expansão prematura.

### Consequences

#### Positivas

- código mais simples de entender
- onboarding técnico mais fácil
- menor custo de manutenção
- menor volume de código para o MVP
- evolução incremental mais segura
- menor chance de o projeto virar uma plataforma excessivamente complexa

#### Negativas

- se o sistema crescer muito em permissões, múltiplos módulos e integrações, talvez seja necessário reforçar convenções de arquitetura
- parte da padronização estrutural terá que vir do time, e não apenas do framework
- se a organização padronizar tudo em TypeScript no futuro, haverá heterogeneidade de stack

#### Para manutenção do código

A manutenção tende a ser mais simples desde que sejam seguidas estas práticas:

- separar claramente rotas, schemas, serviços e templates
- manter a lógica de renderização concentrada em um serviço único
- evitar criar camadas artificiais sem necessidade
- cobrir com testes os cenários de campos opcionais e compatibilidade de template
- manter apenas um template oficial no MVP
- evoluir para banco e painel administrativo apenas quando houver dor real

### Rejected Options

Foram rejeitados, no MVP:

- microserviços
- integração automática com Microsoft Graph
- múltiplos templates desde o início
- motor de permissões complexo
- arquitetura orientada a eventos
- frontend SPA complexo sem necessidade clara

### Notes

A decisão assume que:

- o sistema será usado internamente
- o volume de uso é baixo a moderado
- o principal desafio é operacional, não escalabilidade
- Outlook impõe limitações de HTML, então simplicidade do template é mais importante que sofisticação visual

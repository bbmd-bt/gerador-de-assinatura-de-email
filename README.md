# 📧 Gerador de Assinatura de E-mail

Gerador interativo de assinaturas de e-mail HTML padronizadas para a BT Blue. API robusta desenvolvida com FastAPI, PostgreSQL e arquitetura em camadas para máxima escalabilidade e manutenibilidade.

**Repository**: [github.com/bbmd-bt/gerador-de-assinatura-de-email](https://github.com/bbmd-bt/gerador-de-assinatura-de-email)

## 🎯 Visão Geral

O **Gerador de Assinatura de E-mail** é uma aplicação enterprise que centraliza a geração e distribuição de assinaturas HTML padronizadas para e-mail corporativo. Substitui processos manuais e inconsistentes por uma API robusta com templates dinâmicos, suporte multi-marca e persistência em PostgreSQL.

### Recursos Principais

- ✅ **API RESTful** completa em FastAPI
- ✅ **Template Engine** dinâmico com Jinja2
- ✅ **Arquitetura em camadas** (Repository, Service, API)
- ✅ **Database-first** com SQLAlchemy ORM + Alembic migrations
- ✅ **Containerizado** com Docker & Docker Compose
- ✅ **CI/CD Automático** com GitHub Actions
- ✅ **Testes** abrangentes (pytest, coverage >= 70%)
- ✅ **Documentação** interativa via Swagger/OpenAPI

---

## 🛠️ Technology Stack

### Core Runtime & Web Framework

| Componente | Versão | Propósito |
|-----------|--------|----------|
| **Python** | >= 3.11 | Runtime |
| **FastAPI** | >= 0.115.0 | HTTP Web Framework |
| **Uvicorn** | >= 0.30.0 | ASGI Server |

### Persistência & ORM

| Componente | Versão | Propósito |
|-----------|--------|----------|
| **PostgreSQL** | 15+ | Database |
| **SQLAlchemy** | >= 2.0.0 | ORM (Object-Relational Mapping) |
| **psycopg** | >= 3.2.0 | PostgreSQL adapter |
| **Alembic** | >= 1.13.0 | Database migrations & versioning |

### Validação & Serialização

| Componente | Versão | Propósito |
|-----------|--------|----------|
| **Pydantic** | >= 2.7.0 | Data validation & serialization |
| **Pydantic-Settings** | >= 2.3.0 | Environment configuration |
| **email-validator** | >= 2.1.0 | Email format validation |

### Templating

| Componente | Versão | Propósito |
|-----------|--------|----------|
| **Jinja2** | >= 3.1.0 | HTML template engine |

### Desenvolvimento & Testes

| Componente | Versão | Propósito |
|-----------|--------|----------|
| **pytest** | >= 8.0.0 | Testing framework |
| **pytest-asyncio** | >= 0.23.0 | Async test support |
| **httpx** | >= 0.27.0 | HTTP client for API testing |

### Segurança & Qualidade

| Componente | Versão | Propósito |
|-----------|--------|----------|
| **Bandit** | Latest | Security scanning |
| **Safety** | Latest | Dependency vulnerability check |
| **Flake8** | Latest | Code linting |

### DevOps & Infrastructure

| Componente | Versão | Propósito |
|-----------|--------|----------|
| **Docker** | Latest | Containerization |
| **Docker Compose** | Latest | Local development orchestration |

---

## 🏗️ Arquitetura

### Visão Geral

A aplicação segue uma **arquitetura em camadas** que separa responsabilidades e facilita testes e manutenção:

```
HTTP Request
    ↓
[API Routes] → Validate request → Dependency Injection (FastAPI)
    ↓
[Services] → Business Logic → Validation (Pydantic)
    ↓
[Repository] → Data Access Queries (SQLAlchemy ORM)
    ↓
[Database] ← PostgreSQL
    ↓
[Services] → Template Rendering (Jinja2)
    ↓
HTTP Response (JSON/HTML)
```

### Camadas de Arquitetura

#### 1. **API Layer** (`app/api/`)
Manipulação de requisições HTTP e roteamento.
- Validação de entrada via Pydantic schemas
- Serialização de respostas
- Injeção de dependências via `FastAPI.Depends()`

#### 2. **Domain Layer** (`app/domain/`)
Entidades de negócio e contratos de dados.
- **Models**: SQLAlchemy ORM models
- **Schemas**: Pydantic request/response schemas

#### 3. **Service Layer** (`app/infrastructure/services/`)
Lógica de negócio e orquestração.
- `employee_service.py` - Operações de funcionários
- `signature_service.py` - Geração de assinaturas
- `template_service.py` - Processamento de templates
- `validation_service.py` - Validações de regras de negócio

#### 4. **Repository/Data Layer** (`app/infrastructure/repository/`)
Abstração de acesso a dados.
- Queries SQLAlchemy
- Gerenciamento de transações
- Retorna ORM models

#### 5. **Core** (`app/core/`)
Configuração e segurança.
- `config.py` - Variáveis de ambiente
- `security.py` - Utilidades de autenticação
- `settings.py` - Modelo de configuração Pydantic

### Padrões de Design Utilizados

- **Repository Pattern**: Abstração da camada de dados
- **Service Pattern**: Lógica de negócio separada
- **Dependency Injection**: Injeção de dependências via FastAPI
- **ORM Abstraction**: Models SQLAlchemy isolados de schemas
- **Template Engine**: Jinja2 para renderização dinâmica

---

## 📁 Estrutura do Projeto

```
.
├── app/                          # Código da aplicação
│   ├── main.py                  # Ponto de entrada FastAPI
│   ├── api/                     # Camada de rotas HTTP
│   │   ├── routes/
│   │   │   ├── health.py       # Health check
│   │   │   ├── employees.py    # Employee CRUD
│   │   │   └── signature.py    # Signature generation
│   │   └── dependencies.py      # FastAPI dependencies
│   ├── domain/                  # Entidades de negócio
│   │   ├── models/             # SQLAlchemy ORM
│   │   └── schemas/            # Pydantic schemas
│   ├── infrastructure/          # Infraestrutura
│   │   ├── repository/         # Data access layer
│   │   └── services/           # Business logic
│   ├── core/                    # Configuração
│   │   ├── config.py
│   │   ├── security.py
│   │   └── settings.py
│   └── static/                  # Ativos estáticos
│       └── templates/          # Templates Jinja2
│
├── tests/                        # Suite de testes
│   ├── conftest.py             # Fixtures globais do pytest
│   ├── test_*.py               # Testes de rotas
│   ├── unit/                   # Testes unitários
│   └── integration/            # Testes de integração
│
├── alembic/                      # Database migrations
│   ├── versions/               # Migration files
│   └── alembic.ini
│
├── docs/                         # Documentação
│   ├── API.md
│   ├── Database.md
│   └── Development.md
│
├── .github/                      # Configuração GitHub
│   ├── workflows/              # GitHub Actions CI/CD
│   │   └── ci.yml
│   ├── copilot/                # Guidelines GitHub Copilot
│   │   ├── Architecture.md
│   │   ├── Technology_Stack.md
│   │   ├── Project_Folder_Structure.md
│   │   ├── Coding_Standards.md
│   │   ├── Unit_Tests.md
│   │   ├── Code_Exemplars.md
│   │   └── Workflow_Analysis.md
│   └── skills/                 # Custom Copilot skills
│
├── Dockerfile                    # Container image
├── docker-compose.yml           # Local dev orchestration
├── pyproject.toml              # Configuração Python
├── .env.example                # Template de variáveis de ambiente
├── .gitignore                  # Git ignore rules
└── README.md                   # Este arquivo
```

Veja [.github/copilot/Project_Folder_Structure.md](.github/copilot/Project_Folder_Structure.md) para detalhes completos.

---

## 🚀 Getting Started

### Pré-requisitos

- **Python 3.11+** - [Download](https://www.python.org/downloads/)
- **Docker & Docker Compose** - [Download](https://www.docker.com/products/docker-desktop)
- **PostgreSQL 15+** (ou use Docker)
- **Git** - [Download](https://git-scm.com/)

### Instalação

#### 1. Clone o Repositório

```bash
git clone https://github.com/bbmd-bt/gerador-de-assinatura-de-email.git
cd gerador-de-assinatura-de-email
```

#### 2. Configure Virtual Environment

**Windows (PowerShell)**:
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

**macOS/Linux**:
```bash
python -m venv .venv
source .venv/bin/activate
```

#### 3. Instale Dependências

Para **desenvolvimento** (com testes e ferramentas):
```bash
pip install -e ".[dev]"
```

Para **produção**:
```bash
pip install .
```

#### 4. Configure Variáveis de Ambiente

```bash
# Copie o template
cp .env.example .env

# Edite com suas configurações
# (ou deixe os defaults para desenvolvimento local)
```

**Arquivo `.env` padrão**:
```env
DATABASE_URL=postgresql://user:password@localhost:5432/gerador_email
API_HOST=0.0.0.0
API_PORT=8000
DEBUG=false
```

---

## 💻 Execução

### Opção 1: Docker Compose (Recomendado para Dev)

Inicia aplicação + PostgreSQL em containers:

```bash
docker-compose up --build
```

**Acesso**:
- 🌐 API: http://localhost:8001
- 📚 Swagger Docs: http://localhost:8001/docs
- 🔧 ReDoc: http://localhost:8001/redoc

### Opção 2: Uvicorn Local

```bash
# Certifique-se que PostgreSQL está rodando
uvicorn app.main:app --reload --host 127.0.0.1 --port 8001
```

**Disponível em**: http://localhost:8001/docs

### Opção 3: Produção

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
```

---

## 🧪 Testes

### Executar Todos os Testes

```bash
pytest
```

### Com Cobertura

```bash
pytest --cov=app --cov-report=html --cov-report=term
```

Abre relatório em `htmlcov/index.html`

### Modo Watch (Requer pytest-watch)

```bash
pip install pytest-watch
ptw
```

### Testes Específicos

```bash
# Arquivo especifico
pytest tests/test_employees.py

# Função específica
pytest tests/test_employees.py::test_get_employee_by_id

# Com verbosidade
pytest -v

# Apenas testes unitários
pytest -m "unit"
```

**Objetivo de Cobertura**: >= 70%

Veja [.github/copilot/Unit_Tests.md](.github/copilot/Unit_Tests.md) para mais detalhes.

---

## 📖 Documentação API

### Swagger (Recomendado)

Interativa em: **http://localhost:8001/docs**

Permite teste de endpoints direto no navegador.

### ReDoc

Alternativa em: **http://localhost:8001/redoc**

### Endpoints Principais

#### Health Check
```http
GET /health
```
Retorna status da aplicação.

#### Funcionários
```http
GET    /employees              # Listar todos
POST   /employees              # Criar novo
GET    /employees/{id}         # Buscar por ID
PUT    /employees/{id}         # Atualizar
DELETE /employees/{id}         # Deletar
```

#### Assinaturas
```http
POST   /signatures             # Gerar assinatura
GET    /signatures/{id}        # Buscar gerada
```

---

## 👨‍💻 Padrões de Código

### Convenções Python

- **Estilo**: PEP 8
- **Type Hints**: Obrigatórios em funções
- **Naming**:
  - Classes: `PascalCase` (ex: `EmployeeService`)
  - Funções: `snake_case` (ex: `get_employee`)
  - Constantes: `UPPER_SNAKE_CASE` (ex: `MAX_EMAIL_LENGTH`)

### Padrões de Design

- ✅ **Repository Pattern**: Abstração de dados
- ✅ **Service Pattern**: Lógica de negócio
- ✅ **Dependency Injection**: Loose coupling
- ✅ **ORM Abstraction**: Models isolados

### Commit Messages

Seguir **Conventional Commits**:

```
feat(scope): description
fix(scope): description
refactor(scope): description
docs(scope): description
test(scope): description
chore(scope): description
```

Veja [.github/copilot/Coding_Standards.md](.github/copilot/Coding_Standards.md) e [.github/copilot/Code_Exemplars.md](.github/copilot/Code_Exemplars.md).

---

## 🔄 CI/CD Pipeline

### Automação GitHub Actions

Workflow em `.github/workflows/ci.yml` executa:

1. **Testes** (Python 3.11, 3.12)
2. **Cobertura** (pytest --cov)
3. **Linting** (Flake8)
4. **Security Scanning** (Bandit, Safety)
5. **Docker Build** (ao merge em `main`)

**Acionado por**:
- Push para `main` ou `develop`
- Pull Requests
- Manual via GitHub UI

### Status do Pipeline

![CI Status](https://github.com/bbmd-bt/gerador-de-assinatura-de-email/workflows/CI%2FCD%20Pipeline/badge.svg?branch=main)

---

## 🌳 Estratégia de Branching

Seguimos **Git Flow simplificado**:

```
main          (↑ production-ready)
  ↑
  └── develop  (↑ integration)
      ├── feature/*
      ├── bugfix/*
      └── refactor/*
```

### Branch Naming

- `feature/short-description`
- `bugfix/issue-name`
- `refactor/component-name`
- `docs/section-name`

### Workflow Desenvolvimento

```bash
# 1. Criar feature
git checkout -b feature/new-feature develop

# 2. Fazer commits
git commit -m "feat(scope): description"

# 3. Push e criar PR
git push origin feature/new-feature

# 4. PR para develop (automático)
# 5. Merge após aprovação

# 6. Release para main (periodicamente)
```

Veja [.github/copilot/Workflow_Analysis.md](.github/copilot/Workflow_Analysis.md).

---

## 📋 Deployment

### Local Development

```bash
docker-compose up --build
```

### Staging/Production

Deployments automáticos via GitHub Actions ao fazer tag:

```bash
git tag v0.x.x
git push origin v0.x.x
```

Builds Docker image e push para GitHub Container Registry.

---

## 🔒 Segurança

### Boas Práticas

- ✅ **Variáveis de Ambiente**: Nunca hardcode secrets
- ✅ **Validação de Input**: Pydantic + validators personalizados
- ✅ **Queries Parametrizadas**: SQLAlchemy ORM
- ✅ **Email Validation**: `email-validator` library
- ✅ **Segurança em Templates**: Jinja2 autoescape ativado

### Scanning

CI/CD roda:
- **Bandit**: Vulnerabilidades em código Python
- **Safety**: Vulnerabilidades em dependências

---

## 🤝 Contribuindo

### Como Contribuir

1. **Fork** o repositório
2. **Clone** seu fork: `git clone https://github.com/seu-usuario/gerador-de-assinatura-de-email.git`
3. **Crie branch**: `git checkout -b feature/sua-feature develop`
4. **Faça commits**: `git commit -m "feat(scope): description"`
5. **Push**: `git push origin feature/sua-feature`
6. **Abra PR** contra `develop`

### Checklist de PR

- [ ] Testes adicionados/atualizados
- [ ] Cobertura >= 70%
- [ ] Sem warnings do Flake8
- [ ] Tipo hints em novas funções
- [ ] Docstrings atualizadas
- [ ] README atualizado (se necessário)
- [ ] Commits com mensagens descritivas

### Código de Conduta

Respeitamos todos os contribuidores. Comportamento abusivo não será tolerado.

---

## 📚 Referências Adicionais

- 📖 [Architecture Documentation](.github/copilot/Architecture.md)
- 🛠️ [Coding Standards](.github/copilot/Coding_Standards.md)
- 🧪 [Testing Guide](.github/copilot/Unit_Tests.md)
- 💡 [Code Exemplars](.github/copilot/Code_Exemplars.md)
- 🔄 [Workflow Analysis](.github/copilot/Workflow_Analysis.md)
- 🏗️ [Project Structure](.github/copilot/Project_Folder_Structure.md)
- 📦 [Tech Stack](.github/copilot/Technology_Stack.md)

---

## 📞 Suporte

### Reportar Bugs

- Abra uma [Issue](https://github.com/bbmd-bt/gerador-de-assinatura-de-email/issues) com:
  - Descrição clara do problema
  - Passos para reproduzir
  - Comportamento esperado vs. atual
  - Ambiente (Python version, OS, etc.)

### Sugestões

Use [Discussions](https://github.com/bbmd-bt/gerador-de-assinatura-de-email/discussions) para ideias e perguntas.

---

## 📄 Licença

Propriedade Intelectual – BT Blue (2026)

---

**Desenvolvido para BT Blue**

*Último update: Março 2026*

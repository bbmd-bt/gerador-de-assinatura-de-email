# Project Folder Structure

## Root Level

```
.
+-- app/                      # Main application code
+-- tests/                    # Test suite
+-- alembic/                  # Database migrations
+-- docs/                     # Project documentation
+-- .github/                  # GitHub configuration
¦   +-- workflows/            # CI/CD GitHub Actions
¦   +-- copilot/              # AI Copilot guidelines
¦   +-- skills/               # Custom skills
+-- Dockerfile                # Container image definition
+-- docker-compose.yml        # Multi-container orchestration
+-- pyproject.toml           # Python project configuration
+-- .env.example             # Example environment variables
+-- .gitignore               # Git ignore rules
+-- README.md                # Project documentation
```

## Application Structure: `app/`

```
app/
+-- main.py                           # FastAPI application entry point
+-- __init__.py
+-- api/                              # API layer
¦   +-- routes/
¦   ¦   +-- __init__.py
¦   ¦   +-- health.py                # Health check endpoints
¦   ¦   +-- employees.py             # Employee CRUD endpoints
¦   ¦   +-- signature.py             # Signature generation endpoints
¦   +-- dependencies.py               # FastAPI dependency injection
+-- domain/                           # Domain/business entities layer
¦   +-- models/                       # SQLAlchemy ORM models
¦   ¦   +-- employee.py
¦   ¦   +-- email_signature.py
¦   ¦   +-- brand_settings.py
¦   ¦   +-- department.py
¦   ¦   +-- job_title.py
¦   ¦   +-- role.py
¦   ¦   +-- system_user.py
¦   ¦   +-- template.py
¦   ¦   +-- __init__.py
¦   +-- schemas/                      # Pydantic request/response schemas
¦   ¦   +-- employee.py
¦   ¦   +-- signature.py
¦   ¦   +-- settings.py
¦   ¦   +-- __init__.py
¦   +-- __init__.py
+-- infrastructure/                   # Infrastructure & data access layer
¦   +-- repository/                   # Data access layer (Repository pattern)
¦   ¦   +-- database.py              # Database session management
¦   ¦   +-- employee_repository.py
¦   ¦   +-- email_signature_repository.py
¦   ¦   +-- brand_settings_repository.py
¦   ¦   +-- department_repository.py
¦   ¦   +-- job_title_repository.py
¦   ¦   +-- __init__.py
¦   +-- services/                     # Business logic layer
¦   ¦   +-- employee_service.py
¦   ¦   +-- signature_service.py
¦   ¦   +-- template_service.py
¦   ¦   +-- validation_service.py
¦   ¦   +-- __init__.py
¦   +-- __init__.py
+-- core/                             # Core configuration
¦   +-- config.py                    # Application settings loaded from env
¦   +-- security.py                  # Security utilities (auth stubs)
¦   +-- settings.py                  # Pydantic settings model
¦   +-- __init__.py
+-- static/                           # Static assets
¦   +-- css/
¦   +-- templates/                   # Jinja2 email templates
¦       +-- default_signature.html
¦       +-- index.html
+-- __init__.py
```

## Test Structure: `tests/`

```
tests/
+-- __init__.py
+-- conftest.py                      # Pytest fixtures and configuration
+-- test_health.py                   # Health check endpoint tests
+-- test_employees.py                # Employee endpoint tests
+-- test_signature.py                # Signature generation tests
+-- unit/                            # Unit tests
¦   +-- test_employee_service.py
¦   +-- test_signature_service.py
¦   +-- test_validation_service.py
+-- integration/                     # Integration tests
    +-- test_employee_flow.py
    +-- test_signature_generation.py
```

## Database: `alembic/`

```
alembic/
+-- env.py                           # Alembic environment configuration
+-- script.py.mako                   # Migration template
+-- versions/                        # Migration files (auto-generated)
¦   +-- 001_initial_schema.py
+-- alembic.ini                      # Alembic configuration
```

## Documentation: `docs/`

```
docs/
+-- API.md                           # API documentation
+-- Database.md                      # Database schema documentation
+-- Development.md                   # Development guide
+-- Deployment.md                    # Deployment instructions
```

## Key Directory Purposes

| Directory | Purpose |
|-----------|---------|
| `app/api` | HTTP request handling and routing |
| `app/domain` | Business entities and data contracts |
| `app/infrastructure` | Data access and business logic |
| `app/core` | Configuration and security |
| `app/static` | Email templates and static files |
| `tests` | Automated test suite |
| `alembic` | Database schema versioning |
| `.github` | GitHub-specific configuration |

## Important Files

| File | Purpose |
|------|---------|
| `main.py` | FastAPI app initialization and middleware setup |
| `pyproject.toml` | Project metadata and dependencies |
| `Dockerfile` | Cross-platform container image |
| `docker-compose.yml` | Local development environment with PostgreSQL |
| `.env.example` | Template for environment variables |

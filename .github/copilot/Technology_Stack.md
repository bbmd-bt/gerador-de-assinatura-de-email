# Technology Stack

## Runtime & Framework

| Component | Version | Purpose |
|-----------|---------|---------|
| **Python** | >= 3.11 | Core runtime |
| **FastAPI** | >= 0.115.0 | HTTP web framework |
| **Uvicorn** | >= 0.30.0 | ASGI server |

## Data & Persistence

| Component | Version | Purpose |
|-----------|---------|---------|
| **PostgreSQL** | 15+ | Primary database |
| **SQLAlchemy** | >= 2.0.0 | ORM (Object-Relational Mapping) |
| **psycopg** | >= 3.2.0 | PostgreSQL adapter |
| **Alembic** | >= 1.13.0 | Database migrations |

## Validation & Serialization

| Component | Version | Purpose |
|-----------|---------|---------|
| **Pydantic** | >= 2.7.0 | Data validation and serialization |
| **Pydantic-Settings** | >= 2.3.0 | Environment configuration |
| **email-validator** | >= 2.1.0 | Email format validation |
| **python-multipart** | >= 0.0.9 | Form data parsing |

## Templating

| Component | Version | Purpose |
|-----------|---------|---------|
| **Jinja2** | >= 3.1.0 | HTML template engine for email signatures |

## Development & Testing

| Component | Version | Purpose |
|-----------|---------|---------|
| **pytest** | >= 8.0.0 | Testing framework |
| **httpx** | >= 0.27.0 | HTTP client for API testing |
| **pytest-asyncio** | >= 0.23.0 | Async test support |

## Infrastructure & Deployment

| Component | Version | Purpose |
|-----------|---------|---------|
| **Docker** | Latest | Containerization |
| **Docker Compose** | Latest | Multi-container orchestration |

## Quality & Security

| Component | Version | Purpose |
|-----------|---------|---------|
| **Bandit** | Latest | Security vulnerability scanning |
| **Safety** | Latest | Dependency vulnerability checking |
| **Flake8** | Latest | Code style linting |

## Version Constraints

- **Python**: 3.11 is the minimum to ensure modern language features and performance
- **FastAPI**: Latest stable for API robustness
- **SQLAlchemy 2.x**: Required for ORM v2 syntax and improvements

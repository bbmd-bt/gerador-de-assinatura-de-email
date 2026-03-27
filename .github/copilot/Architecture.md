# Architecture

## Overview

The **Gerador de Assinatura de E-mail** (Email Signature Generator) is built with a **layered architecture** that follows enterprise software design patterns. It uses FastAPI for HTTP handling, PostgreSQL for data persistence, and implements a clean separation of concerns through Repository and Service layers.

## Architecture Layers

### 1. **API Layer** (`app/api/`)
  - FastAPI route handlers
  - Request validation and response serialization
  - Routes:
    - `routes/health.py` - Health check and system status
    - `routes/employees.py` - Employee management
    - `routes/signature.py` - Email signature generation and retrieval

### 2. **Domain Layer** (`app/domain/`)
  - Business entities and Pydantic schemas
  - `models/` - SQLAlchemy ORM models
  - `schemas/` - Pydantic request/response schemas
  - Core business data contracts

### 3. **Service Layer** (`app/infrastructure/services/`)
  - Business logic and orchestration
  - Validation rules
  - Template processing with Jinja2
  - Services:
    - `employee_service.py` - Employee operations
    - `signature_service.py` - Signature generation logic
    - `template_service.py` - Template management
    - `validation_service.py` - Business rule validation

### 4. **Repository/Data Layer** (`app/infrastructure/repository/`)
  - Data access abstraction
  - SQLAlchemy ORM queries
  - Transaction management
  - Repositories:
    - `employee_repository.py`
    - `email_signature_repository.py`
    - `brand_settings_repository.py`
    - `department_repository.py`
    - `job_title_repository.py`

### 5. **Core Configuration** (`app/core/`)
  - `config.py` - Environment configuration
  - `security.py` - Authentication/authorization stubs
  - `settings.py` - Application settings
  - Database connection management

### 6. **Templates Layer** (`app/static/templates/`)
  - Jinja2 HTML email templates
  - CSS styling for signature formatting
  - Reusable template components

## Data Flow

```
HTTP Request
    ?
[API Routes] ? Validate Request ? Dependency Injection
    ?
[Services] ? Business Logic ? Validation
    ?
[Repository] ? Database Query ? ORM Mapping
    ?
[Database] ? PostgreSQL
    ?
[Services] ? Template Rendering ? Response Serialization
    ?
HTTP Response (JSON or HTML)
```

## Key Design Patterns

- **Repository Pattern**: Abstract data access layer for testability
- **Service Pattern**: Encapsulate business logic separate from routes
- **Dependency Injection**: FastAPI's `Depends()` for loose coupling
- **ORM Abstraction**: SQLAlchemy models isolated from API schemas
- **Template Engine**: Jinja2 for dynamic HTML signature generation

## Technology Interactions

- **FastAPI** handles HTTP and dependency injection
- **Pydantic** validates and serializes data
- **SQLAlchemy** manages ORM and database sessions
- **Jinja2** renders dynamic email templates
- **PostgreSQL** provides persistent data storage
- **Alembic** manages database schema migrations

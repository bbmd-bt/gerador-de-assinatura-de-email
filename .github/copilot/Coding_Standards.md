# Coding Standards

## Python Code Style

### General

- **Python Version**: 3.11+
- **Style Guide**: PEP 8 with Black formatting preferences
- **Line Length**: 88 characters (Black default)
- **Type Hints**: Required for function signatures
- **Imports**: Use absolute imports; organize by standard library, third-party, local

### Naming Conventions

- **Classes**: `PascalCase` (e.g., `EmployeeService`, `EmailSignature`)
- **Functions/Methods**: `snake_case` (e.g., `get_employee`, `create_signature`)
- **Constants**: `UPPER_SNAKE_CASE` (e.g., `MAX_EMAIL_LENGTH`)
- **Private Methods**: Prefix with `_` (e.g., `_internal_method`)
- **Files**: `snake_case.py` (e.g., `employee_service.py`)

### Module Organization

```python
"""Module docstring explaining purpose."""

# Standard library imports
from typing import List

# Third-party imports
from fastapi import APIRouter, Depends
from sqlalchemy import Column, String

# Local imports
from app.core.config import settings
from app.infrastructure.repository import EmployeeRepository
```

## FastAPI Conventions

### Route Organization

- Group related routes in modules (e.g., `routes/employees.py`)
- Use clear HTTP verbs: `GET`, `POST`, `PUT`, `DELETE`
- Routes must have descriptive names and tags
- Include appropriate response status codes

Example:
```python
router = APIRouter(prefix="/employees", tags=["employees"])

@router.get("/{employee_id}")
async def get_employee(employee_id: int, db: Session = Depends(...)):
    """Retrieve an employee by ID."""
    pass
```

### Dependency Injection

- Use FastAPI's `Depends()` for database sessions and services
- Create reusable dependency functions in `dependencies.py`
- Avoid direct imports of services in routes; inject them

### Request/Response Models

- Define Pydantic schemas in `domain/schemas/`
- Use different schemas for input (Create) and output (Response)
- Include field validation with Pydantic validators

## Database & ORM

### SQLAlchemy Models

- Define ORM models in `domain/models/`
- Include `__tablename__` and explicit column definitions
- Use proper data types and constraints
- Add timestamps: `created_at`, `updated_at`

### Repository Pattern

- Implement CRUD operations in repository classes
- Repositories accept SQLAlchemy `Session` as dependency
- Return ORM models, not raw queries
- Handle exceptions and transactions at repository level

Example:
```python
class EmployeeRepository:
    def __init__(self, session: Session):
        self.session = session
    
    def get_by_id(self, employee_id: int) -> Employee:
        return self.session.query(Employee).filter_by(id=employee_id).first()
```

## Service Layer

### Business Logic

- Implement business rules in service classes
- Services orchestrate multiple repositories if needed
- Validate input using validation services
- Return domain models, not ORM models directly

### Exception Handling

- Use custom exceptions defined in a `exceptions.py` module
- Catch specific exceptions; avoid bare `except`
- Log errors with context for debugging

## Testing Standards

### Unit Tests

- Test file names: `test_*.py` or `*_test.py`
- One test class per component
- Test method names: `test_<scenario>_<expected_outcome>`
- Use fixtures for setup/teardown
- Mock external dependencies

Example:
```python
def test_get_employee_by_id_returns_employee(employee_repository):
    """Verify that getting an employee by ID returns the correct employee."""
    employee = employee_repository.get_by_id(1)
    assert employee.id == 1
    assert employee.name == "John Doe"
```

### Integration Tests

- Use real database fixtures
- Test end-to-end workflows
- Named with `integration_` prefix

## Documentation

### Docstrings

- Use Google-style docstrings for functions and classes
- Include Args, Returns, Raises sections

Example:
```python
def create_signature(employee_id: int, template_id: int) -> SignatureResponse:
    """Generate an email signature for an employee.
    
    Args:
        employee_id: The ID of the employee
        template_id: The ID of the template to use
    
    Returns:
        SignatureResponse containing the HTML signature
        
    Raises:
        EmployeeNotFound: If employee does not exist
    """
    pass
```

### Comments

- Explain "why", not "what"
- Use comments sparingly; prefer self-documenting code
- Keep comments up-to-date with code changes

## Security Standards

- Never hardcode secrets; use environment variables
- Validate all external input
- Use parameterized queries (SQLAlchemy ORM handles this)
- Sanitize user input before template rendering
- Validate email addresses using `email-validator`

## Version Control

### Commit Messages

Format: `<type>(<scope>): <subject>`

Types: `feat`, `fix`, `refactor`, `docs`, `test`, `chore`

Example:
```
feat(signature): Add HTML signature generation
fix(employee): Handle missing department gracefully
refactor(repository): Simplify query methods
```

### Branch Naming

- `feature/short-description`
- `bugfix/issue-name`
- `refactor/component-name`
- `docs/description`

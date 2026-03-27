# Code Exemplars

Reference implementations demonstrating best practices and patterns used in this project.

## Pattern Examples

### 1. Service Layer with Dependency Injection

**File**: `app/infrastructure/services/employee_service.py`

```python
from typing import Optional, List
from app.domain.models.employee import Employee
from app.domain.schemas.employee import EmployeeResponse
from app.infrastructure.repository.employee_repository import EmployeeRepository
from sqlalchemy.orm import Session

class EmployeeService:
    """Business logic for employee operations."""
    
    def __init__(self, repository: EmployeeRepository):
        self.repository = repository
    
    def get_employee(self, employee_id: int) -> Optional[EmployeeResponse]:
        """Retrieve employee by ID with validation."""
        employee = self.repository.get_by_id(employee_id)
        if not employee:
            raise EmployeeNotFound(f"Employee {employee_id} not found")
        return EmployeeResponse.from_orm(employee)
    
    def list_employees(self) -> List[EmployeeResponse]:
        """Get all employees."""
        employees = self.repository.get_all()
        return [EmployeeResponse.from_orm(emp) for emp in employees]
```

**Key Points**:
- Service receives repository via dependency injection
- Type hints on all parameters and returns
- Clear method naming describing intent
- Raises specific exceptions for error handling

### 2. Repository Pattern

**File**: `app/infrastructure/repository/employee_repository.py`

```python
from sqlalchemy.orm import Session
from app.domain.models.employee import Employee
from typing import Optional, List

class EmployeeRepository:
    """Data access layer for Employee entities."""
    
    def __init__(self, session: Session):
        self.session = session
    
    def get_by_id(self, employee_id: int) -> Optional[Employee]:
        """Retrieve employee by primary key."""
        return self.session.query(Employee).filter(
            Employee.id == employee_id
        ).first()
    
    def get_all(self) -> List[Employee]:
        """Retrieve all employees."""
        return self.session.query(Employee).all()
    
    def create(self, employee: Employee) -> Employee:
        """Create new employee."""
        self.session.add(employee)
        self.session.commit()
        self.session.refresh(employee)
        return employee
    
    def update(self, employee: Employee) -> Employee:
        """Update existing employee."""
        self.session.merge(employee)
        self.session.commit()
        return employee
    
    def delete(self, employee_id: int) -> bool:
        """Delete employee by ID."""
        employee = self.get_by_id(employee_id)
        if not employee:
            return False
        self.session.delete(employee)
        self.session.commit()
        return True
```

**Key Points**:
- Single responsibility: data access only
- Type-safe queries using ORM
- Transaction handling (commit/rollback)
- Returns domain models, not raw data

### 3. FastAPI Route with Dependency Injection

**File**: `app/api/routes/employees.py`

```python
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.infrastructure.services.employee_service import EmployeeService
from app.domain.schemas.employee import EmployeeResponse, EmployeeCreate
from app.api.dependencies import get_db, get_employee_service

router = APIRouter(prefix="/employees", tags=["employees"])

@router.get("/{employee_id}", response_model=EmployeeResponse)
async def get_employee(
    employee_id: int,
    service: EmployeeService = Depends(get_employee_service)
) -> EmployeeResponse:
    """Retrieve employee by ID.
    
    Args:
        employee_id: The ID of the employee to retrieve
        service: Injected employee service
        
    Returns:
        EmployeeResponse with employee details
        
    Raises:
        HTTPException: If employee not found (404)
    """
    try:
        return service.get_employee(employee_id)
    except EmployeeNotFound:
        raise HTTPException(
            status_code=404,
            detail=f"Employee {employee_id} not found"
        )

@router.post("/", response_model=EmployeeResponse, status_code=201)
async def create_employee(
    employee: EmployeeCreate,
    service: EmployeeService = Depends(get_employee_service)
) -> EmployeeResponse:
    """Create a new employee."""
    new_employee = Employee(**employee.dict())
    return service.create_employee(new_employee)
```

**Key Points**:
- Dependency injection for services
- Clear HTTP methods and status codes
- Type hints on request/response
- Proper error handling with HTTPException
- Google-style docstrings

### 4. Pydantic Schema

**File**: `app/domain/schemas/employee.py`

```python
from pydantic import BaseModel, Field, EmailStr, validator
from typing import Optional
from datetime import datetime

class EmployeeBase(BaseModel):
    """Base schema with common employee fields."""
    name: str = Field(..., min_length=1, max_length=255)
    email: EmailStr
    department: str = Field(..., min_length=1, max_length=100)

class EmployeeCreate(EmployeeBase):
    """Schema for creating an employee."""
    position: str

class EmployeeResponse(EmployeeBase):
    """Schema for employee response."""
    id: int
    created_at: datetime
    updated_at: Optional[datetime]
    
    @validator("email")
    def validate_company_email(cls, v):
        """Ensure company email domain."""
        if not v.endswith("@company.com"):
            raise ValueError("Must use company email domain")
        return v
    
    class Config:
        from_attributes = True  # Enable ORM mode
```

**Key Points**:
- Separate schemas for create/response
- Field validation with constraints
- Custom validators for business rules
- Config.from_attributes for ORM compatibility

### 5. Unit Test

**File**: `tests/unit/test_employee_service.py`

```python
import pytest
from unittest.mock import Mock
from app.infrastructure.services.employee_service import EmployeeService
from app.domain.models.employee import Employee

@pytest.fixture
def mock_repository():
    """Provide mock employee repository."""
    return Mock()

@pytest.fixture
def employee_service(mock_repository):
    """Provide service with mocked repository."""
    return EmployeeService(mock_repository)

def test_get_employee_returns_response(employee_service, mock_repository):
    """Verify get_employee returns formatted response."""
    # Arrange
    test_employee = Employee(id=1, name="John Doe", email="john@company.com")
    mock_repository.get_by_id.return_value = test_employee
    
    # Act
    result = employee_service.get_employee(1)
    
    # Assert
    assert result.id == 1
    assert result.name == "John Doe"
    mock_repository.get_by_id.assert_called_once_with(1)

def test_get_employee_raises_when_not_found(employee_service, mock_repository):
    """Verify EmployeeNotFound raised when employee missing."""
    mock_repository.get_by_id.return_value = None
    
    with pytest.raises(EmployeeNotFound):
        employee_service.get_employee(999)
```

**Key Points**:
- Fixtures for setup/dependencies
- Mocking external dependencies
- Arrange-Act-Assert pattern
- One logical assertion per test
- Descriptive test names

## Template Rendering (Jinja2)

**File**: `app/infrastructure/services/template_service.py`

```python
from jinja2 import Environment, FileSystemLoader, select_autoescape
from pathlib import Path

class TemplateService:
    """Service for rendering Jinja2 email templates."""
    
    def __init__(self):
        template_dir = Path(__file__).parent.parent / "static" / "templates"
        self.env = Environment(
            loader=FileSystemLoader(template_dir),
            autoescape=select_autoescape(["html"])
        )
    
    def render_signature(
        self,
        template_name: str,
        context: dict
    ) -> str:
        """Render email signature from template.
        
        Args:
            template_name: Name of the template file
            context: Variables to pass to template
            
        Returns:
            Rendered HTML string
        """
        template = self.env.get_template(template_name)
        return template.render(**context)
```

**Key Points**:
- Proper template directory configuration
- Context as dictionary for flexibility
- Autoescape enabled for security

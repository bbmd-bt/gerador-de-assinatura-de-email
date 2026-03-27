# Unit Tests

## Testing Framework

- **Framework**: pytest
- **Async Support**: pytest-asyncio
- **HTTP Testing**: httpx (async HTTP client)
- **Coverage Goal**: >= 70%

## Test Structure

```
tests/
+-- conftest.py                      # Global fixtures and configuration
+-- test_health.py
+-- test_employees.py
+-- test_signature.py
+-- unit/
¦   +-- test_employee_service.py
¦   +-- test_signature_service.py
¦   +-- test_validation_service.py
+-- integration/
    +-- test_employee_flow.py
    +-- test_signature_generation.py
```

## Running Tests

```bash
# Run all tests
pytest

# Run with coverage report
pytest --cov=app --cov-report=html

# Run specific test file
pytest tests/test_employees.py

# Run specific test function
pytest tests/test_employees.py::test_get_employee_by_id

# Run in verbose mode
pytest -v

# Run with markers
pytest -m "not integration"
```

## Test Types

### Unit Tests

Test individual components in isolation:

- **Service tests**: Business logic
- **Repository tests**: Data access
- **Validator tests**: Input validation

Example:
```python
def test_employee_service_get_by_id(employee_service, sample_employee):
    """Verify employee retrieval by ID."""
    result = employee_service.get_by_id(sample_employee.id)
    assert result.id == sample_employee.id
    assert result.name == sample_employee.name
```

### Integration Tests

Test component interactions:

- Multi-layer workflows
- Database interactions
- Service orchestration

Example:
```python
def test_signature_generation_flow(client, db_session):
    """End-to-end test for signature generation."""
    # Create employee
    employee = create_test_employee(db_session)
    
    # Generate signature
    response = client.post(
        "/api/signatures",
        json={"employee_id": employee.id, "template_id": 1}
    )
    
    assert response.status_code == 200
    assert "<html>" in response.json()["signature"]
```

### API Tests

Test HTTP endpoints:

- Request validation
- Response format
- Status codes
- Error handling

Example:
```python
def test_get_employee_endpoint(client):
    """Test GET /employees/{id} endpoint."""
    response = client.get("/employees/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1
```

## Fixtures

### Common Fixtures (conftest.py)

```python
@pytest.fixture
def client():
    """Provide test HTTP client."""
    return TestClient(app)

@pytest.fixture
def db_session():
    """Provide test database session."""
    # Create test DB
    # Yield connection
    # Cleanup
    pass

@pytest.fixture
def sample_employee(db_session):
    """Create a test employee."""
    employee = Employee(
        name="John Doe",
        email="john@example.com",
        department="Engineering"
    )
    db_session.add(employee)
    db_session.commit()
    return employee
```

## Mocking

Use `unittest.mock` for external dependencies:

```python
from unittest.mock import Mock, patch

def test_signature_with_external_template(employee_service):
    """Test signature generation with mocked template service."""
    with patch('app.infrastructure.services.template_service') as mock_template:
        mock_template.render.return_value = "<html>...</html>"
        
        result = employee_service.generate_signature(1)
        
        assert result is not None
        mock_template.render.assert_called_once()
```

## Coverage

### Generate Coverage Report

```bash
pytest --cov=app --cov-report=html --cov-report=term
```

### Coverage Thresholds

- **Minimum**: 70%
- **Target**: 80%+
- **Services**: 90%+ (most critical)
- **Models**: 70%+ (mostly property testing)
- **Routes**: 75%+ (API contract testing)

### Exclusions from Coverage

Update `pyproject.toml`:
```toml
[tool.coverage.run]
omit = [
    "app/main.py",
    "app/core/config.py",
]
```

## Test Markers

Define custom markers in `pyproject.toml`:

```toml
[tool.pytest.ini_options]
markers = [
    "unit: Unit tests",
    "integration: Integration tests",
    "slow: Slow running tests",
    "skip_in_ci: Skip in CI environment",
]
```

Usage:
```python
@pytest.mark.integration
def test_employee_flow(client, db_session):
    pass

# Run only unit tests
pytest -m "unit"

# Skip integration tests
pytest -m "not integration"
```

## Best Practices

1. **One assertion per test** when possible
2. **Descriptive test names** that explain the scenario
3. **Arrange-Act-Assert** pattern:
   ```python
   # Arrange
   employee = create_test_employee()
   
   # Act
   result = service.get_employee(employee.id)
   
   # Assert
   assert result.id == employee.id
   ```
4. **Use fixtures** for common setup
5. **Mock external calls** (APIs, emails, etc.)
6. **Test edge cases** (null values, empty lists, etc.)
7. **Keep tests independent** (no test should depend on another)
8. **Cleanup after tests** (delete temp files, clear caches, etc.)

## Continuous Testing

### In CI/CD Pipeline

Tests run automatically on:
- Push to `main` and `develop`
- Pull requests
- Python versions: 3.11, 3.12

### Local Development

Run tests before committing:
```bash
# Watch mode (requires pytest-watch)
ptw

# Or use pre-commit hook
pytest && git commit
```

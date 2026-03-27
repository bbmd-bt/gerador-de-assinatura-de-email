import logging

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.dependencies import get_employee_service
from app.domain.schemas.employee import EmployeeCreate, EmployeeResponse
from app.domain.services.employee_service import EmployeeService
from app.infrastructure.database import get_db

router = APIRouter(prefix="/employees", tags=["employees"])
logger = logging.getLogger(__name__)


@router.post("", response_model=EmployeeResponse, status_code=201)
def create_employee(
    payload: EmployeeCreate,
    service: EmployeeService = Depends(get_employee_service),
    db: Session = Depends(get_db),
) -> EmployeeResponse:
    employee = service.create_employee(db, payload)
    return EmployeeResponse.model_validate(employee)


@router.get("", response_model=list[EmployeeResponse])
def list_employees(
    skip: int = 0,
    limit: int = 100,
    service: EmployeeService = Depends(get_employee_service),
    db: Session = Depends(get_db),
) -> list[EmployeeResponse]:
    employees = service.list_employees(db, skip=skip, limit=limit)
    return [EmployeeResponse.model_validate(emp) for emp in employees]

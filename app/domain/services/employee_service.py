import logging
import uuid

from sqlalchemy.orm import Session

from app.domain.models.employee import Employee
from app.domain.schemas.employee import EmployeeCreate
from app.infrastructure.repository.department_repository import DepartmentRepository
from app.infrastructure.repository.employee_repository import EmployeeRepository
from app.infrastructure.repository.job_title_repository import JobTitleRepository

logger = logging.getLogger(__name__)


class EmployeeService:
    def __init__(self) -> None:
        self._employee_repo = EmployeeRepository()
        self._job_title_repo = JobTitleRepository()
        self._department_repo = DepartmentRepository()

    def create_employee(self, db: Session, payload: EmployeeCreate) -> Employee:
        logger.info("creating employee", extra={"corporate_email": payload.corporate_email})
        try:
            job_title = self._job_title_repo.get_or_create(db, payload.job_title)
            department = self._department_repo.get_or_create(db, payload.department)
            employee = Employee(
                id=uuid.uuid4(),
                full_name=payload.full_name,
                corporate_email=str(payload.corporate_email),
                phone=payload.phone,
                mobile_phone=payload.mobile_phone,
                linkedin_url=str(payload.linkedin_url) if payload.linkedin_url else None,
                job_title_id=job_title.id,
                department_id=department.id,
            )
            self._employee_repo.create(db, employee)
            db.commit()
            db.refresh(employee)
            logger.info("employee created", extra={"id": str(employee.id)})
            return employee
        except Exception:
            db.rollback()
            logger.exception("failed to create employee", extra={"corporate_email": payload.corporate_email})
            raise

    def list_employees(self, db: Session, skip: int = 0, limit: int = 100) -> list[Employee]:
        return self._employee_repo.list_all(db, skip=skip, limit=limit)

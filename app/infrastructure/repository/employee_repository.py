from sqlalchemy.orm import Session

from app.domain.models.employee import Employee


class EmployeeRepository:
    def create(self, db: Session, employee: Employee) -> Employee:
        db.add(employee)
        db.flush()
        return employee

    def list_all(self, db: Session, skip: int = 0, limit: int = 100) -> list[Employee]:
        return (
            db.query(Employee)
            .filter(Employee.is_active == True)  # noqa: E712
            .offset(skip)
            .limit(limit)
            .all()
        )

    def get_by_email(self, db: Session, email: str) -> Employee | None:
        return db.query(Employee).filter(Employee.corporate_email == email).first()

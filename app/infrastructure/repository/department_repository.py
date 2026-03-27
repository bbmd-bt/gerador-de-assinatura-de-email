import uuid

from sqlalchemy.orm import Session

from app.domain.models.department import Department


class DepartmentRepository:
    def get_or_create(self, db: Session, name: str) -> Department:
        obj = db.query(Department).filter(Department.name == name).first()
        if not obj:
            obj = Department(id=uuid.uuid4(), name=name)
            db.add(obj)
            db.flush()
        return obj

import uuid

from sqlalchemy.orm import Session

from app.domain.models.job_title import JobTitle


class JobTitleRepository:
    def get_or_create(self, db: Session, title: str) -> JobTitle:
        obj = db.query(JobTitle).filter(JobTitle.title == title).first()
        if not obj:
            obj = JobTitle(id=uuid.uuid4(), title=title)
            db.add(obj)
            db.flush()
        return obj

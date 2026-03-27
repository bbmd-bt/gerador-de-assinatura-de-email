import logging
import uuid

from sqlalchemy.orm import Session

from app.domain.models.email_signature import EmailSignature
from app.domain.schemas.signature import SignatureRequest

logger = logging.getLogger(__name__)


class EmailSignatureRepository:
    def create(self, db: Session, payload: SignatureRequest, html_content: str) -> EmailSignature:
        record = EmailSignature(
            id=uuid.uuid4(),
            html_content=html_content,
            full_name=payload.full_name,
            job_title=payload.job_title,
            department=payload.department,
            corporate_email=str(payload.corporate_email),
        )
        db.add(record)
        db.commit()
        db.refresh(record)
        logger.debug("email_signature persisted", extra={"id": str(record.id)})
        return record

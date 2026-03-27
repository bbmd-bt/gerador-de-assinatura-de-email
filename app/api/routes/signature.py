import logging

from fastapi import APIRouter, Depends
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session

from app.api.dependencies import get_signature_service
from app.domain.schemas.signature import SignatureRequest, SignatureResponse
from app.domain.services.signature_service import SignatureService
from app.infrastructure.database import get_db
from app.infrastructure.repository.email_signature_repository import (
    EmailSignatureRepository,
)

router = APIRouter(prefix="/signatures", tags=["signatures"])
logger = logging.getLogger(__name__)

_sig_repo = EmailSignatureRepository()


@router.post("", response_model=SignatureResponse, status_code=201)
def create_signature(
    payload: SignatureRequest,
    service: SignatureService = Depends(get_signature_service),
    db: Session = Depends(get_db),
) -> SignatureResponse:
    result = service.generate(payload)
    _sig_repo.create(db, payload, result.html_content)
    logger.info(
        "signature persisted", extra={"corporate_email": payload.corporate_email}
    )
    return result


@router.post("/render", response_class=HTMLResponse, status_code=200)
def render_signature(
    payload: SignatureRequest,
    service: SignatureService = Depends(get_signature_service),
) -> HTMLResponse:
    result = service.generate(payload)
    return HTMLResponse(content=result.html_content)

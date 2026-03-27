import logging

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.domain.schemas.settings import BrandSettingsResponse
from app.infrastructure.database import get_db
from app.infrastructure.repository.brand_settings_repository import (
    BrandSettingsRepository,
)

router = APIRouter(prefix="/settings", tags=["settings"])
logger = logging.getLogger(__name__)

_brand_repo = BrandSettingsRepository()

_DEFAULTS = {
    "company_name": "BT Blue",
    "unit_name": "BT Blue",
    "website_url": "https://btblue.com.br",
    "logo_url": "https://btblue.com.br/logo.png",
    "primary_color": "#0057A8",
    "secondary_color": "#FF6B00",
    "disclaimer_html": "",
}


@router.get("", response_model=BrandSettingsResponse)
def get_settings(db: Session = Depends(get_db)) -> BrandSettingsResponse:
    record = _brand_repo.get_first(db)
    if record:
        logger.debug("brand_settings loaded from database")
        return BrandSettingsResponse(
            company_name=record.company_name,
            unit_name=record.unit_name,
            website_url=record.website_url,
            logo_url=record.logo_url,
            primary_color=record.primary_color,
            secondary_color=record.secondary_color,
            disclaimer_html=record.disclaimer_html,
        )
    logger.warning("brand_settings not found in database, returning defaults")
    return BrandSettingsResponse(**_DEFAULTS)

from sqlalchemy.orm import Session

from app.domain.models.brand_settings import BrandSettings


class BrandSettingsRepository:
    def get_first(self, db: Session) -> BrandSettings | None:
        return db.query(BrandSettings).first()

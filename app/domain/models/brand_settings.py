import uuid
from datetime import datetime

from sqlalchemy import DateTime, String, Text, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.infrastructure.database import Base


class BrandSettings(Base):
    __tablename__ = "brand_settings"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    company_name: Mapped[str] = mapped_column(String(200), nullable=False)
    unit_name: Mapped[str] = mapped_column(String(200), nullable=False)
    website_url: Mapped[str] = mapped_column(String(500), nullable=False)
    logo_url: Mapped[str] = mapped_column(String(500), nullable=False)
    primary_color: Mapped[str] = mapped_column(String(20), nullable=False)
    secondary_color: Mapped[str] = mapped_column(String(20), nullable=False)
    disclaimer_html: Mapped[str] = mapped_column(Text, nullable=False, default="")
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

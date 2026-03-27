import uuid
from datetime import datetime

from sqlalchemy import Boolean, DateTime, ForeignKey, String, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.infrastructure.database import Base


class Employee(Base):
    __tablename__ = "employees"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    full_name: Mapped[str] = mapped_column(String(200), nullable=False)
    corporate_email: Mapped[str] = mapped_column(String(254), unique=True, nullable=False)
    phone: Mapped[str | None] = mapped_column(String(30), nullable=True)
    mobile_phone: Mapped[str | None] = mapped_column(String(30), nullable=True)
    linkedin_url: Mapped[str | None] = mapped_column(String(500), nullable=True)
    job_title_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("job_titles.id"), nullable=False)
    department_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("departments.id"), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    job_title_rel: Mapped["JobTitle"] = relationship("JobTitle", back_populates="employees")
    department_rel: Mapped["Department"] = relationship("Department", back_populates="employees")
    email_signatures: Mapped[list["EmailSignature"]] = relationship("EmailSignature", back_populates="employee")

    @property
    def job_title(self) -> str:
        return self.job_title_rel.title if self.job_title_rel else ""

    @property
    def department(self) -> str:
        return self.department_rel.name if self.department_rel else ""

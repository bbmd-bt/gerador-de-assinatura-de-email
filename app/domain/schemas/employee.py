import re
import uuid
from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr, HttpUrl, field_validator

_PHONE_RE = re.compile(r"^\+?[\d\s\-().]{7,20}$")


class EmployeeCreate(BaseModel):
    full_name: str
    corporate_email: EmailStr
    job_title: str
    department: str
    phone: str | None = None
    mobile_phone: str | None = None
    linkedin_url: HttpUrl | None = None

    @field_validator("full_name", "job_title", "department")
    @classmethod
    def must_not_be_blank(cls, value: str) -> str:
        stripped = value.strip()
        if not stripped:
            raise ValueError("field must not be blank")
        return stripped

    @field_validator("phone", "mobile_phone")
    @classmethod
    def validate_phone_format(cls, value: str | None) -> str | None:
        if value is None:
            return None
        if not _PHONE_RE.match(value):
            raise ValueError(
                "invalid phone number format; expected digits, spaces, hyphens, parentheses or leading +"
            )
        return value


class EmployeeResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    full_name: str
    corporate_email: str
    job_title: str
    department: str
    phone: str | None
    mobile_phone: str | None
    linkedin_url: str | None
    is_active: bool
    created_at: datetime

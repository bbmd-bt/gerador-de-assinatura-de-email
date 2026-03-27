import re

from pydantic import BaseModel, EmailStr, HttpUrl, field_validator

_PHONE_RE = re.compile(r"^\+?[\d\s\-().]{7,20}$")


class SignatureRequest(BaseModel):
    full_name: str
    job_title: str
    department: str
    corporate_email: EmailStr
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


class SignatureResponse(BaseModel):
    html_content: str

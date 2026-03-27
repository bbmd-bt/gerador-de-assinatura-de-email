from pydantic import BaseModel, HttpUrl


class BrandSettingsResponse(BaseModel):
    company_name: str
    unit_name: str
    website_url: HttpUrl
    logo_url: HttpUrl
    primary_color: str
    secondary_color: str
    disclaimer_html: str

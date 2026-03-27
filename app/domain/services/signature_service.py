import logging

from app.core.config import settings as app_settings
from app.domain.schemas.signature import SignatureRequest, SignatureResponse
from app.domain.services.template_service import TemplateService
from app.domain.services.validation_service import validate_signature_request

logger = logging.getLogger(__name__)

_SIGNATURE_TEMPLATE = "email/default_signature.html"


class SignatureService:
    def __init__(self, template_service: TemplateService | None = None) -> None:
        self._templates = template_service or TemplateService()

    def generate(self, data: SignatureRequest) -> SignatureResponse:
        logger.debug(
            "generating signature",
            extra={
                "full_name": data.full_name,
                "corporate_email": data.corporate_email,
            },
        )
        validate_signature_request(data)
        context = {
            "primary_color": app_settings.brand_primary_color,
            "secondary_color": app_settings.brand_secondary_color,
            "company_name": app_settings.brand_company_name,
            "logo_url": app_settings.brand_logo_url,
            "website_url": app_settings.brand_website_url,
            **data.model_dump(),
        }
        html = self._templates.render(_SIGNATURE_TEMPLATE, context)
        logger.info(
            "signature generated",
            extra={
                "full_name": data.full_name,
                "corporate_email": data.corporate_email,
            },
        )
        return SignatureResponse(html_content=html)

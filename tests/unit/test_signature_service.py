import pytest

from app.domain.schemas.signature import SignatureRequest
from app.domain.services.signature_service import SignatureService


def _base_request(**overrides) -> SignatureRequest:
    data = {
        "full_name": "Ana Lima",
        "job_title": "Desenvolvedora",
        "department": "Engenharia",
        "corporate_email": "ana.lima@example.com",
    }
    data.update(overrides)
    return SignatureRequest(**data)


@pytest.fixture
def service() -> SignatureService:
    return SignatureService()


def test_returns_html_string(service):
    result = service.generate(_base_request())
    assert isinstance(result.html_content, str)
    assert len(result.html_content) > 0


def test_html_contains_full_name(service):
    result = service.generate(_base_request(full_name="Carlos Souza"))
    assert "Carlos Souza" in result.html_content


def test_html_contains_job_title(service):
    result = service.generate(_base_request(job_title="Arquiteto de Software"))
    assert "Arquiteto de Software" in result.html_content


def test_html_contains_department(service):
    result = service.generate(_base_request(department="Plataforma"))
    assert "Plataforma" in result.html_content


def test_html_contains_email(service):
    result = service.generate(_base_request(corporate_email="carlos@example.com"))
    assert "carlos@example.com" in result.html_content


def test_html_contains_phone_when_provided(service):
    result = service.generate(_base_request(phone="+55 11 91234-5678"))
    assert "+55 11 91234-5678" in result.html_content


def test_html_omits_phone_when_absent(service):
    result = service.generate(_base_request())
    # phone field block must not appear as stray text
    assert "None" not in result.html_content


def test_html_contains_linkedin_when_provided(service):
    result = service.generate(_base_request(linkedin_url="https://linkedin.com/in/ana"))
    assert "LinkedIn" in result.html_content


def test_html_is_valid_table_structure(service):
    result = service.generate(_base_request())
    assert "<table" in result.html_content
    assert "</table>" in result.html_content


def test_html_has_no_data_uris(service):
    """data: URIs are blocked by Outlook desktop — the template must not emit them."""
    result = service.generate(
        _base_request(
            phone="+55 11 3000-0000",
            mobile_phone="+55 11 99000-0000",
            linkedin_url="https://linkedin.com/in/ana",
        )
    )
    assert "data:image/" not in result.html_content


def test_html_injection_in_full_name_is_escaped(service):
    result = service.generate(_base_request(full_name='<script>alert("xss")</script>'))
    assert "<script>" not in result.html_content
    assert "&lt;script&gt;" in result.html_content


def test_html_injection_in_job_title_is_escaped(service):
    result = service.generate(_base_request(job_title="<img src=x onerror=alert(1)>"))
    assert "<img src=x" not in result.html_content


def test_html_injection_in_department_is_escaped(service):
    result = service.generate(_base_request(department="<b>Engenharia</b>"))
    assert "<b>" not in result.html_content
    assert "&lt;b&gt;" in result.html_content


def test_raises_on_blank_full_name():
    with pytest.raises(Exception):
        _base_request(full_name="   ")


def test_raises_on_blank_job_title():
    with pytest.raises(Exception):
        _base_request(job_title="")

import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

_PAYLOAD = {
    "full_name": "Ana Lima",
    "job_title": "Desenvolvedora",
    "department": "Engenharia",
    "corporate_email": "ana.lima@example.com",
}


def test_render_returns_200():
    response = client.post("/signatures/render", json=_PAYLOAD)
    assert response.status_code == 200


def test_render_content_type_is_html():
    response = client.post("/signatures/render", json=_PAYLOAD)
    assert "text/html" in response.headers["content-type"]


def test_render_body_contains_full_name():
    response = client.post("/signatures/render", json=_PAYLOAD)
    assert "Ana Lima" in response.text


def test_render_body_contains_table():
    response = client.post("/signatures/render", json=_PAYLOAD)
    assert "<table" in response.text
    assert "</table>" in response.text


def test_render_with_optional_fields():
    payload = {
        **_PAYLOAD,
        "phone": "+55 11 91234-5678",
        "linkedin_url": "https://linkedin.com/in/ana",
    }
    response = client.post("/signatures/render", json=payload)
    assert response.status_code == 200
    assert "+55 11 91234-5678" in response.text
    assert "LinkedIn" in response.text


def test_render_returns_422_on_missing_required_field():
    response = client.post("/signatures/render", json={"full_name": "Ana Lima"})
    assert response.status_code == 422


def test_render_sanitizes_html_injection():
    """The API must return 200 but with HTML-escaped content, not raw script tags."""
    payload = {**_PAYLOAD, "full_name": '<script>alert("xss")</script>'}
    response = client.post("/signatures/render", json=payload)
    assert response.status_code == 200
    assert "<script>" not in response.text
    assert "&lt;script&gt;" in response.text


def test_render_has_no_data_uris():
    """Outlook desktop blocks data: URIs — the rendered HTML must not contain any."""
    response = client.post("/signatures/render", json=_PAYLOAD)
    assert "data:image/" not in response.text

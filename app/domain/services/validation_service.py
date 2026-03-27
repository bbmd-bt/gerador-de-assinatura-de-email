from app.domain.schemas.signature import SignatureRequest


def validate_signature_request(data: SignatureRequest) -> None:
    if not data.full_name.strip():
        raise ValueError("full_name cannot be empty")
    if not data.job_title.strip():
        raise ValueError("job_title cannot be empty")

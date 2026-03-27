from functools import lru_cache

from app.domain.services.employee_service import EmployeeService
from app.domain.services.signature_service import SignatureService


@lru_cache
def get_signature_service() -> SignatureService:
    return SignatureService()


@lru_cache
def get_employee_service() -> EmployeeService:
    return EmployeeService()

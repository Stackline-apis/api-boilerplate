import re
import dns.resolver
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/email", tags=["Email Validator"])

EMAIL_REGEX = re.compile(
    r'^[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}$'
)


class EmailResponse(BaseModel):
    email: str
    valid: bool
    domain: str
    reason: str


@router.get("/validate", response_model=EmailResponse, summary="Validate an email address")
def validate_email(email: str):
    """
    Validates an email address by checking:
    1. Format — does it look like a real email?
    2. MX records — does the domain actually receive mail?
    """
    email = email.strip().lower()

    if not email or not EMAIL_REGEX.match(email):
        return EmailResponse(email=email, valid=False, domain="", reason="Invalid format")

    domain = email.split("@")[1]

    try:
        dns.resolver.resolve(domain, "MX")
        return EmailResponse(
            email=email, valid=True, domain=domain,
            reason="Valid format and domain has active mail servers"
        )
    except dns.resolver.NXDOMAIN:
        return EmailResponse(email=email, valid=False, domain=domain, reason="Domain does not exist")
    except dns.resolver.NoAnswer:
        return EmailResponse(email=email, valid=False, domain=domain, reason="Domain exists but has no mail servers")
    except Exception:
        return EmailResponse(email=email, valid=False, domain=domain, reason="Could not verify domain")

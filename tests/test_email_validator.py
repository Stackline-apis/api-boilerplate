from fastapi.testclient import TestClient
from api.index import app

client = TestClient(app)


def test_valid_email_gmail():
    response = client.get("/email/validate?email=test@gmail.com")
    assert response.status_code == 200
    data = response.json()
    assert data["valid"] is True
    assert data["domain"] == "gmail.com"


def test_valid_email_case_insensitive():
    response = client.get("/email/validate?email=TEST@Gmail.COM")
    assert response.status_code == 200
    data = response.json()
    assert data["valid"] is True
    assert data["email"] == "test@gmail.com"


def test_invalid_format_no_at():
    response = client.get("/email/validate?email=notanemail")
    assert response.status_code == 200
    data = response.json()
    assert data["valid"] is False
    assert data["reason"] == "Invalid format"


def test_invalid_format_no_domain():
    response = client.get("/email/validate?email=user@")
    assert response.status_code == 200
    data = response.json()
    assert data["valid"] is False


def test_invalid_domain_nonexistent():
    response = client.get("/email/validate?email=test@thisdoesnotexist99xyz123.com")
    assert response.status_code == 200
    data = response.json()
    assert data["valid"] is False


def test_empty_email():
    response = client.get("/email/validate?email=")
    assert response.status_code == 200
    data = response.json()
    assert data["valid"] is False

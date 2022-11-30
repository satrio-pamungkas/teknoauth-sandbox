from fastapi.testclient import TestClient
from ..config import app_test

client = TestClient(app_test)

def test_create_user():
    response = client.post(
        "/api/user/register",
        json={
            "username": "testing", 
            "email": "email@testing.com", 
            "password": "testing"
        }
    )
    assert response.status_code == 201
    
def test_create_user_with_missing_attribute():
    response = client.post(
        "/api/user/register",
        json={
            "username": "testing",
            "email": "email@testing.com"
        }
    )
    assert response.status_code == 422
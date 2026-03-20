from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200

def test_create_customer():
    response = client.post("/customers", json={
        "gender": 1,
        "senior_citizen": 0,
        "partner": 1,
        "dependents": 0,
        "tenure": 2,
        "phone_service": 1,
        "multiple_lines": "No",
        "internet_service": "Fiber optic",
        "online_security": "No",
        "online_backup": "No",
        "device_protection": "No",
        "tech_support": "No",
        "streaming_tv": "No",
        "streaming_movies": "No",
        "contract": "Month-to-month",
        "paperless_billing": 1,
        "payment_method": "Electronic check",
        "monthly_charges": 70.5,
        "total_charges": 141.0
    })
    assert response.status_code == 200
    assert "id" in response.json()

def test_high_risk():
    response = client.get("/customers/high-risk")
    assert response.status_code == 200
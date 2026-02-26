from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200

def test_prediction():
    response = client.post("/predict", json={"value": 0.9})
    assert response.json()["prediction"] == 1

from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)

def test_health_endpoint_requires_auth():
    response = client.get("/system/health")
    assert response.status_code == 401

def test_health_endpoint_returns_ok():
    response = client.get("/system/health", headers={"Authorization": "Bearer abc123"})
    assert response.status_code == 200
    assert response.json() == {"health": "OK"}

import json
import pytest
from main import app

# Configurate app for testing
@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SECRET_TOKEN'] = 'test_secret_token'
    with app.test_client() as client:
        yield client

# --- Health Endpoint ---
def test_health_endpoint(client):
    """Verifica que /health devuelve API OK y status 200"""
    response = client.get('/health')
    assert response.status_code == 200
    assert response.data.decode() == 'API OK'

# --- Track Endpoint Successful ---
def test_track_endpoint_success(client):
    """Prueba /track con payload válido y token correcto"""
    payload = {
        "user_id": "12345",
        "event_type": "page_view",
        "metadata": {"page": "/home", "referrer": "/login"}
    }
    headers = {"X-API-Key": "test_secret_token"}
    response = client.post('/track', data=json.dumps(payload),
                           content_type='application/json', headers=headers)
    data = json.loads(response.data)
    assert response.status_code == 200
    assert data['status'] == 'ok'
    assert data['received'] == payload

# --- Track Endpoint Unauthorized ---
def test_track_endpoint_unauthorized(client):
    """Prueba /track con token incorrecto devuelve 401"""
    payload = {"user_id": "12345", "event_type": "click"}
    headers = {"X-API-Key": "wrong_token"}
    response = client.post('/track', data=json.dumps(payload),
                           content_type='application/json', headers=headers)
    assert response.status_code == 401

# --- Track Endpoint Bad Request ---
def test_track_endpoint_bad_request(client):
    """Prueba /track con payload no JSON devuelve 400"""
    headers = {"X-API-Key": "test_secret_token"}
    response = client.post('/track', data="not a json",
                           content_type='application/json', headers=headers)
    assert response.status_code == 400

# --- Track Endpoint Flexible Payload ---
def test_track_endpoint_flexible_payload(client):
    """Prueba /track con payload flexible (campos extra)"""
    payload = {
        "user_id": "999",
        "event_type": "signup",
        "extra_field": "extra_value",
        "metadata": {"plan": "premium"}
    }
    headers = {"X-API-Key": "test_secret_token"}
    response = client.post('/track', data=json.dumps(payload),
                           content_type='application/json', headers=headers)
    data = json.loads(response.data)
    assert data['received']['extra_field'] == 'extra_value'

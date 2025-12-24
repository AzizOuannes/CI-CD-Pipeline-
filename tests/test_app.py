import sys
import os
import pytest

# Add the app folder to Python path so we can import app.py
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../app')))

from app import app

# -------------------------
# Fixture for Flask test client
# -------------------------
@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# -------------------------
# Test the /health endpoint
# -------------------------
def test_health_endpoint(client):
    response = client.get('/health')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['status'] == 'healthy'
    assert 'timestamp' in json_data
    assert 'environment' in json_data
    assert 'version' in json_data

# -------------------------
# Test the / endpoint
# -------------------------
def test_home_endpoint(client):
    response = client.get('/')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['message'] == 'Welcome to Cloud DevOps Assessment API'
    assert 'timestamp' in json_data
    assert 'environment' in json_data

# -------------------------
# Test the /api/info endpoint
# -------------------------
def test_info_endpoint(client):
    response = client.get('/api/info')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['application'] == 'Cloud DevOps Assessment'
    assert json_data['version'] == '1.0.0'
    assert json_data['framework'] == 'Flask'
    assert json_data['kubernetes'] is True
    assert 'description' in json_data

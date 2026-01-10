import pytest
from app import app   # 👈 import your Flask app object

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_homepage(client):
    """Check if homepage loads successfully"""
    response = client.get('/')
    assert response.status_code == 200

def test_login_page(client):
    """Check if login page loads successfully"""
    response = client.get('/login')
    assert response.status_code == 200
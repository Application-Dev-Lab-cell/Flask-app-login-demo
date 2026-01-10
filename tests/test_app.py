import pytest
import app   # 👈 import your Flask app object

@pytest.fixture
def client():
    app.app.testing = True   # 👈 note: app.app because you imported the module
    return app.app.test_client()

def test_homepage(client):
    """Check if homepage loads successfully"""
    response = client.get('/')
    assert response.status_code == 200

def test_login_page(client):
    """Check if login page loads successfully"""
    response = client.get('/login')
    assert response.status_code == 200
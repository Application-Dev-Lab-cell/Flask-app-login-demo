import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
import app   # imports app.py

@pytest.fixture
def client():
    app.app.testing = True
    return app.app.test_client()

def test_homepage(client):
    response = client.get('/')
    assert response.status_code in (200, 302)

def test_login_page(client):
    response = client.get('/login')
    assert response.status_code == 200

def test_login_form(client):
    # Simulate posting credentials to /login
    response = client.post('/login', data={
        'username': 'testuser',
        'password': 'testpass'
    }, follow_redirects=True)

    # Depending on your logic, check for redirect or dashboard content
    assert response.status_code in (200, 302)
    # Example: if dashboard shows "Welcome", check that
    assert b"dashboard" in response.data or b"Welcome" in response.data
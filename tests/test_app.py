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
    assert response.status_code in (200, 302)  # homepage redirects to login or dashboard

def test_login_page(client):
    response = client.get('/login')
    assert response.status_code == 200
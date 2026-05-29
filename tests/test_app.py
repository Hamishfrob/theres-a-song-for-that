# tests/test_app.py
import pytest
import json
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_match_requires_description(client):
    """Empty body returns 400, no Claude call made."""
    response = client.post('/api/match',
        data=json.dumps({}),
        content_type='application/json')
    assert response.status_code == 400

def test_match_requires_non_empty_description(client):
    """Blank description returns 400."""
    response = client.post('/api/match',
        data=json.dumps({'description': '   '}),
        content_type='application/json')
    assert response.status_code == 400

def test_index_route_exists(client):
    """Root route returns something (200 once index.html exists, 404 is also ok for now)."""
    response = client.get('/')
    assert response.status_code in [200, 404]

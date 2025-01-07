import pytest
from app import create_app, db
from app.config import TestingConfig

# Global fixtures

@pytest.fixture
def client():
    """Create a test client with a separate test database."""
    app = create_app(TestingConfig)
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
            db.drop_all()

@pytest.fixture
def auth_token(client):
    """Register and login to obtain an authentication token."""
    client.post('/register', json={
        'username': 'testuser',
        'email': 'test@gmai.com',
        'password': 'test_password'
    })
    login_response = client.post('/login', json={
        'email': 'test@gmai.com',
        'password': 'test_password'
    })
    return login_response.json['access_token']

@pytest.fixture
def test_post(client, auth_token):
    """Create a test post and return its ID."""
    response = client.post('/posts', json={
        'title': 'Test Post',
        'content': 'This is a test post.'
    }, headers={
        'Authorization': f'Bearer {auth_token}'
    })
    return response.json['data']['id']

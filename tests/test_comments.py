import pytest
from app import create_app, db
from app.config import TestingConfig


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
    # Register and login to get a token
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
    # Create a test post
    response = client.post('/posts', json={
        'title': 'Test Post',
        'content': 'This is a test post.'
    }, headers={
        'Authorization': f'Bearer {auth_token}'
    })
    return response.json['data']['id']


def test_create_comment(client, auth_token, test_post):
    """Test create comment"""
    response = client.post(f'/posts/{test_post}/comments', json={
        'content': 'This is a test comment.'
    }, headers={
        'Authorization': f'Bearer {auth_token}'
    })
    assert response.status_code == 201
    assert 'Comment created successfully' in response.json['message']
    assert response.json['data']['content'] == 'This is a test comment.'

def test_update_comment(client, auth_token, test_post):
    """Test update comment"""
    create_response = client.post(f'/posts/{test_post}/comments', json={
        'content': 'This is a test comment.'
    }, headers={
        'Authorization': f'Bearer {auth_token}'
    })
    comment_id = create_response.json['data']['id']

    # Test updating the comment
    response = client.put(f'/comments/{comment_id}', json={
        'content': 'Updated comment content.'
    }, headers={
        'Authorization': f'Bearer {auth_token}'
    })
    assert response.status_code == 200
    assert 'Comment updated successfully' in response.json['message']
    assert response.json['data']['content'] == 'Updated comment content.'


def test_delete_comment(client, auth_token, test_post):
    """Test delete comment"""
    create_response = client.post(f'/posts/{test_post}/comments', json={
        'content': 'This is a test comment.'
    }, headers={
        'Authorization': f'Bearer {auth_token}'
    })
    comment_id = create_response.json['data']['id']

    # Test deleting the comment
    response = client.delete(f'/comments/{comment_id}', headers={
        'Authorization': f'Bearer {auth_token}'
    })
    assert response.status_code == 200
    assert 'Comment deleted successfully' in response.json['message']

def test_get_comments_for_post(client, auth_token, test_post):
    # Create a comment first
    client.post(f'/posts/{test_post}/comments', json={
        'content': 'This is a test comment.'
    }, headers={
        'Authorization': f'Bearer {auth_token}'
    })

    # Test fetching comments for the post
    response = client.get(f'/posts/{test_post}/comments')
    assert response.status_code == 200
    assert 'Comments retrieved successfully' in response.json['message']
    assert len(response.json['data']) == 1

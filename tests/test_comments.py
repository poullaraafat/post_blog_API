def test_create_comment(client, auth_token, test_post):
    """Test the creation of a comment."""
    response = client.post(
        f'/posts/{test_post}/comments',
        json={'content': 'This is a test comment.'},
        headers={'Authorization': f'Bearer {auth_token}'}
    )
    assert response.status_code == 201
    assert 'Comment created successfully' in response.json['message']
    assert response.json['data']['content'] == 'This is a test comment.'

def test_update_comment(client, auth_token, test_post):
    """Test the update of a comment."""
    create_response = client.post(
        f'/posts/{test_post}/comments',
        json={'content': 'This is a test comment.'},
        headers={'Authorization': f'Bearer {auth_token}'}
    )
    comment_id = create_response.json['data']['id']

    response = client.put(
        f'/comments/{comment_id}',
        json={'content': 'Updated comment content.'},
        headers={'Authorization': f'Bearer {auth_token}'}
    )
    assert response.status_code == 200
    assert 'Comment updated successfully' in response.json['message']
    assert response.json['data']['content'] == 'Updated comment content.'

def test_delete_comment(client, auth_token, test_post):
    """Test the deletion of a comment."""
    create_response = client.post(
        f'/posts/{test_post}/comments',
        json={'content': 'This is a test comment.'},
        headers={'Authorization': f'Bearer {auth_token}'}
    )
    comment_id = create_response.json['data']['id']

    response = client.delete(
        f'/comments/{comment_id}',
        headers={'Authorization': f'Bearer {auth_token}'}
    )
    assert response.status_code == 200
    assert 'Comment deleted successfully' in response.json['message']

def test_get_comments_for_post(client, auth_token, test_post):
    """Test retrieving comments for a specific post."""
    client.post(
        f'/posts/{test_post}/comments',
        json={'content': 'This is a test comment.'},
        headers={'Authorization': f'Bearer {auth_token}'}
    )

    response = client.get(f'/posts/{test_post}/comments')
    assert response.status_code == 200
    assert 'Comments retrieved successfully' in response.json['message']
    assert len(response.json['data']) == 1

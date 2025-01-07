def test_create_post(client, auth_token):
    """Test creating a post."""
    response = client.post('/posts', json={
        'title': 'Test Post',
        'content': 'This is a test post.'
    }, headers={
        'Authorization': f'Bearer {auth_token}'
    })
    assert response.status_code == 201
    assert 'Post created successfully' in response.json['message']
    assert response.json['data']['title'] == 'Test Post'


def test_update_post(client, auth_token):
    """Test updating a post."""
    create_response = client.post('/posts', json={
        'title': 'Test Post',
        'content': 'This is a test post.'
    }, headers={
        'Authorization': f'Bearer {auth_token}'
    })
    post_id = create_response.json['data']['id']

    response = client.put(f'/posts/{post_id}', json={
        'title': 'Updated Post Title',
        'content': 'Updated post content.'
    }, headers={
        'Authorization': f'Bearer {auth_token}'
    })
    assert response.status_code == 200
    assert 'Post updated successfully' in response.json['message']
    assert response.json['data']['title'] == 'Updated Post Title'


def test_delete_post(client, auth_token):
    """Test deleting a post."""
    create_response = client.post('/posts', json={
        'title': 'Test Post',
        'content': 'This is a test post.'
    }, headers={
        'Authorization': f'Bearer {auth_token}'
    })
    post_id = create_response.json['data']['id']

    response = client.delete(f'/posts/{post_id}', headers={
        'Authorization': f'Bearer {auth_token}'
    })
    assert response.status_code == 200
    assert 'Post deleted successfully' in response.json['message']

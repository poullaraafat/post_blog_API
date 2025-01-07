def test_search_posts(client, auth_token):
    """Test searching for posts."""
    client.post('/posts', json={
        'title': 'Test Post',
        'content': 'This is a test post.'
    }, headers={
        'Authorization': f'Bearer {auth_token}'
    })

    # Test searching for posts
    response = client.get('/search/posts?title=Test')
    assert response.status_code == 200
    assert 'Posts retrieved successfully' in response.json['message']
    assert len(response.json['data']) == 1
    assert response.json['data'][0]['title'] == 'Test Post'

def test_register(client):
    """Test the user registration endpoint."""
    # Test successful registration
    response = client.post('/register', json={
        'username': 'testuser',
        'email': 'test@gmail.com',
        'password': 'test_password'
    })
    assert response.status_code == 201
    assert 'User registered successfully' in response.json['message']
    assert response.json['data']['username'] == 'testuser'

    # Test registration with an existing username
    response = client.post('/register', json={
        'username': 'testuser',
        'email': 'test1@gmail.com',
        'password': 'test_password'
    })
    assert response.status_code == 400
    assert 'The username is already taken. Please choose another.' in response.json['message']

    # Test registration with an existing email
    response = client.post('/register', json={
        'username': 'testuser1',
        'email': 'test@gmail.com',
        'password': 'test_password'
    })
    assert response.status_code == 400
    assert 'The email is already registered. Please use another or log in.' in response.json['message']


def test_login(client):
    """Test the user login endpoint."""
    # Register a user for login tests
    client.post('/register', json={
        'username': 'testuser',
        'email': 'test@gmail.com',
        'password': 'test_password'
    })

    # Test successful login
    response = client.post('/login', json={
        'email': 'test@gmail.com',
        'password': 'test_password'
    })
    assert response.status_code == 200
    assert 'User logged in successfully' in response.json['message']
    assert 'access_token' in response.json

    # Test login with an invalid email
    response = client.post('/login', json={
        'email': 'wrong@gmail.com',
        'password': 'test_password'
    })
    assert response.status_code == 401
    assert 'Invalid email or password' in response.json['message']

    # Test login with an invalid password
    response = client.post('/login', json={
        'email': 'test@gmail.com',
        'password': 'wrongpassword'
    })
    assert response.status_code == 401
    assert 'Invalid email or password' in response.json['message']


def test_logout(client):
    """Test the user logout endpoint."""
    # Register and log in a user
    client.post('/register', json={
        'username': 'testuser',
        'email': 'test@example.com',
        'password': 'password123'
    })
    login_response = client.post('/login', json={
        'email': 'test@example.com',
        'password': 'password123'
    })
    access_token = login_response.json['access_token']

    # Test logout with a valid token
    response = client.post('/logout', headers={
        'Authorization': f'Bearer {access_token}'
    })
    assert response.status_code == 200
    assert 'User logged out successfully' in response.json['message']

# API Documentation

This document provides comprehensive details about the **Post Blog API**, including available endpoints, request/response formats, and examples.

---

## Base URL
All endpoints are relative to the base URL:
`http://127.0.0.1:5000`

---

## Authentication
Most endpoints require authentication via a **JWT token**. Include the token in the `Authorization` header:
```
Authorization: Bearer <token>
```

---

## Endpoints

### 1. Authentication

#### Register User
- **URL**: `/register`
- **Method**: `POST`
- **Description**: Register a new user.
- **Request Body**:
    ```json
    {
            "username": "test_user",
            "email": "test@gmail.com",
            "password": "password1234"
    }
    ```
- **Response**:

    **Success (201)**:
    ```json
    {
            "message": "User registered successfully",
            "data": {
                    "id": 1,
                    "username": "test_user",
                    "email": "test@gmail.com",
                    "created_at": "2023-10-10T12:34:56.789012"
            }
    }
    ```

    **Validation Error (400)**:
    ```json
    {
            "message": "Validation failed",
            "errors": {
                    "username": "Username must be between 8 and 32 characters long.",
                    "email": "Invalid email address.",
                    "password": "Password must be between 8 and 32 characters long."
            }
    }
    ```

#### Login User
- **URL**: `/login`
- **Method**: `POST`
- **Description**: Authenticate a user and return a JWT token.
- **Request Body**:
    ```json
    {
            "email": "test@gmail.com",
            "password": "password1234"
    }
    ```
- **Response**:

    **Success (200)**:
    ```json
    {
            "message": "Login successful",
            "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
    }
    ```

    **Invalid Credentials (401)**:
    ```json
    {
            "message": "Invalid email or password"
    }
    ```

#### Logout User
- **URL**: `/logout`
- **Method**: `POST`
- **Description**: Log out the current user.
- **Headers**:
    ```
    Authorization: Bearer <token>
    ```
- **Response**:

    **Success (200)**:
    ```json
    {
            "message": "Logout successful"
    }
    ```

### 2. User Management

#### Get User Profile
- **URL**: `/profile`
- **Method**: `GET`
- **Description**: Retrieve the profile of the authenticated user.
- **Headers**:
    ```
    Authorization: Bearer <token>
    ```
- **Response**:

    **Success (200)**:
    ```json
    {
            "message": "User profile retrieved successfully",
            "data": {
                    "id": 2,
                    "username": "test_user",
                    "email": "test@gmail.com",
                    "created_at": "2025-01-07T23:29:16.291599",
                    "posts": [
                            {
                                    "id": 5,
                                    "title": "test title",
                                    "date_posted": "2025-01-07T23:29:16.291599"
                            }
                    ]
            }
    }
    ```

    **User Not Found (404)**:
    ```json
    {
            "message": "User not found"
    }
    ```

#### Update User Profile
- **URL**: `/profile`
- **Method**: `PUT`
- **Description**: Update the profile of the authenticated user.
- **Headers**:
    ```
    Authorization: Bearer <token>
    ```
- **Request Body**:
    ```json
    {
            "username": "updated_user",
            "email": "updated@gmail.com"
    }
    ```
- **Response**:

    **Success (200)**:
    ```json
    {
            "message": "User profile updated successfully",
            "data": {
                    "id": 2,
                    "username": "updated_user",
                    "email": "updated@gmail.com",
                    "created_at": "2025-01-07T23:29:16.291599"
            }
    }
    ```

    **Validation Error (400)**:
    ```json
    {
            "message": "Validation failed",
            "errors": {
                    "username": "Username must be between 8 and 32 characters long.",
                    "email": "Invalid email address."
            }
    }
    ```

### 3. Posts

#### Create Post
- **URL**: `/posts`
- **Method**: `POST`
- **Description**: Create a new post.
- **Headers**:
    ```
    Authorization: Bearer <token>
    ```
- **Request Body**:
    ```json
    {
            "title": "New Post",
            "content": "Content of the new post"
    }
    ```
- **Response**:

    **Success (201)**:
    ```json
    {
            "message": "Post created successfully",
            "data": {
                    "id": 1,
                    "title": "New Post",
                    "content": "Content of the new post",
                    "author": "test_user",
                    "date_posted": "2025-01-07T23:29:16.291599",
                    "comments": [],
                    "likes": 0,
                    "user_id": 1
            }
    }
    ```

    **Validation Error (400)**:
    ```json
    {
            "message": "Validation failed",
            "errors": {
                    "title": "Title is required.",
                    "content": "Content is required."
            }
    }
    ```

#### Delete Post
- **URL**: `/posts/{post_id}`
- **Method**: `DELETE`
- **Description**: Delete a post by its ID.
- **Headers**:
    ```
    Authorization: Bearer <token>
    ```
- **Response**:

    **Success (200)**:
    ```json
    {
            "message": "Post deleted successfully"
    }
    ```

    **Post Not Found (404)**:
    ```json
    {
            "message": "Post not found"
    }
    ```

#### Update Post
- **URL**: `/posts/{post_id}`
- **Method**: `PUT`
- **Description**: Update a post by its ID.
- **Headers**:
    ```
    Authorization: Bearer <token>
    ```
- **Request Body**:
    ```json
    {
            "title": "Updated Title",
            "content": "Updated content of the post"
    }
    ```
- **Response**:

    **Success (200)**:
    ```json
    {
            "message": "Post updated successfully",
            "data": {
                    "id": 1,
                    "title": "Updated Title",
                    "content": "content of the Updated  post",
                    "author": "test_user",
                    "date_posted": "2025-01-07T23:29:16.291599",
                    "comments": [],
                    "likes": 0,
                    "user_id": 1
            }
    }
    ```

    **Validation Error (400)**:
    ```json
    {
            "message": "Validation failed",
            "errors": {
                    "title": "Title is required.",
                    "content": "Content is required."
            }
    }
    ```

### 4. Comments

#### Create Comment
- **URL**: `/posts/{post_id}/comments`
- **Method**: `POST`
- **Description**: Add a comment to a post.
- **Headers**:
    ```
    Authorization: Bearer <token>
    ```
- **Request Body**:
    ```json
    {
            "content": "New comment"
    }
    ```
- **Response**:

    **Success (201)**:
    ```json
    {
            "message": "Comment created successfully",
            "data": {
                    "id": 1,
                    "content": "New comment",
                    "created_at": "2025-01-07T23:29:16.291599",
                    "post_id": 1,
                    "user_id": 1
            }
    }
    ```

    **Validation Error (400)**:
    ```json
    {
            "message": "Validation failed",
            "errors": {
                    "content": "Content is required."
            }
    }
    ```

#### Update Comment
- **URL**: `/comments/{comment_id}`
- **Method**: `PUT`
- **Description**: Update a comment by its ID.
- **Headers**:
    ```
    Authorization: Bearer <token>
    ```
- **Request Body**:
    ```json
    {
            "content": "Updated comment"
    }
    ```
- **Response**:

    **Success (200)**:
    ```json
    {
            "message": "Comment updated successfully",
            "data": {
                    "id": 1,
                    "content": "Updated comment",
                    "created_at": "2025-01-07T23:29:16.291599",
                    "post_id": 1,
                    "user_id": 1
            }
    }
    ```

    **Validation Error (400)**:
    ```json
    {
            "message": "Validation failed",
            "errors": {
                    "content": "Content is required."
            }
    }
    ```

#### Delete Comment
- **URL**: `/comments/{comment_id}`
- **Method**: `DELETE`
- **Description**: Delete a comment by its ID.
- **Headers**:
    ```
    Authorization: Bearer <token>
    ```
- **Response**:

    **Success (200)**:
    ```json
    {
            "message": "Comment deleted successfully"
    }
    ```

    **Comment Not Found (404)**:
    ```json
    {
            "message": "Comment not found"
    }
    ```

#### Get Post Comments
- **URL**: `/posts/{post_id}/comments`
- **Method**: `GET`
- **Description**: Retrieve all comments for a post.
- **Headers**:
    ```
    Authorization: Bearer <token>
    ```
- **Response**:

    **Success (200)**:
    ```json
    {
            "message": "Comments retrieved successfully",
            "data": [
                    {
                            "id": 1,
                            "content": "New comment",
                            "created_at": "2025-01-07T23:29:16.291599",
                            "post_id": 1,
                            "user_id": 1
                    }
            ]
    }
    ```

    **No Comments Found (404)**:
    ```json
    {
            "message": "No comments found"
    }
    ```

### 5. Likes

#### Like Post
- **URL**: `/posts/{post_id}/like`
- **Method**: `POST`
- **Description**: Like a post.
- **Headers**:
    ```
    Authorization: Bearer <token>
    ```
- **Response**:

    **Success (200)**:
    ```json
    {
            "message": "Post liked successfully"
    }
    ```

#### Unlike Post
- **URL**: `/posts/{post_id}/unlike`
- **Method**: `POST`
- **Description**: Unlike a post.
- **Headers**:
    ```
    Authorization: Bearer <token>
    ```
- **Response**:

    **Success (200)**:
    ```json
    {
            "message": "Post unliked successfully"
    }
    ```

### 6. Search

#### Search Posts
- **URL**: `/search/posts?title={title}`
- **Method**: `GET`
- **Description**: Search for posts by title.
- **Query Parameters**:
    - `title`: The title to search for.
- **Response**:

    **Success (200)**:
    ```json
    {
            "message": "Posts retrieved successfully",
            "data": [
                    {
                            "id": 5,
                            "title": "test title",
                            "content": "Content of the new post",
                            "author": "test_user",
                            "date_posted": "2025-01-07T23:29:16.291599",
                            "comments": [],
                            "likes": 0,
                            "user_id": 2
                    }
            ]
    }
    ```

    **No Posts Found (404)**:
    ```json
    {
            "message": "No posts found"
    }
    ```

### Error Responses
All error responses follow the same format:
```json
{
        "message": "Error message",
        "errors": {
                "field": "Error description"
        }
}
```

### License
This API is licensed under the MIT License.


# Post Blog API

![License](https://img.shields.io/badge/License-MIT-blue.svg)

The **Post Blog API** is a RESTful API designed for creating, managing, and interacting with blog posts, comments, and user profiles. It supports user authentication, post creation, commenting, liking posts, and searching for posts.

---

## Features

- **User Authentication**: Register, login, and logout with JWT-based authentication.
- **User Management**: Update user profiles and view user details.
- **Post Management**: Create, update, delete, and search for posts.
- **Comments**: Add, update, and delete comments on posts.
- **Likes**: Like and unlike posts.
- **Search**: Search for posts by title.

---

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [API Documentation](#api-documentation)
- [Usage Examples](#usage-examples)
- [Error Handling](#error-handling)
- [License](#license)
- [Contributing](#contributing)
- [Support](#support)

---

## Installation

Follow these steps to set up the project locally:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/poullaraafat/post_blog_API.git
    cd post_blog_API
    ```

2. **Set up a virtual environment (optional but recommended)**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables**:
    Create a `.env` file in the root directory and add the following variables:
    ```plaintext
    SECRET_KEY=your_secret_key
    DATABASE_URI=sqlite:///app.db  # Or your preferred database URI
    JWT_SECRET_KEY=your_jwt_secret_key
    DEBUG=True
    ```

5. **Run the application**:
    ```bash
    python app.py
    ```

6. **Access the API**:
    The API will be available at [http://127.0.0.1:5000](http://127.0.0.1:5000).

---

## API Documentation

For detailed API documentation, including available endpoints, request/response formats, and examples, refer to the [API Documentation](api.md).

---

## Usage Examples

### Register a User
```bash
curl -X POST http://127.0.0.1:5000/register \
-H "Content-Type: application/json" \
-d '{
     "username": "test_user",
     "email": "test@gmail.com",
     "password": "password1234"
}'
```

### Login and Get JWT Token
```bash
curl -X POST http://127.0.0.1:5000/login \
-H "Content-Type: application/json" \
-d '{
     "email": "test@gmail.com",
     "password": "password1234"
}'
```

### Create a Post
```bash
curl -X POST http://127.0.0.1:5000/posts \
-H "Content-Type: application/json" \
-H "Authorization: Bearer <your_jwt_token>" \
-d '{
     "title": "My First Post",
     "content": "This is the content of my first post."
}'
```

### Search for Posts
```bash
curl -X GET "http://127.0.0.1:5000/search/posts?title=First" \
-H "Authorization: Bearer <your_jwt_token>"
```

---

## Error Handling

The API returns standardized error responses in the following format:
```json
{
     "message": "Error message",
     "errors": {
          "field": "Error description"
     }
}
```

Common HTTP status codes include:

- **400 Bad Request**: Validation errors or invalid input.
- **401 Unauthorized**: Missing or invalid JWT token.
- **404 Not Found**: Resource not found (e.g., user, post, or comment).
- **500 Internal Server Error**: Server-side issues.

---

## Demo

- **Postman Collection**: [Run in Postman](https://web.postman.co/workspace/ddd2c9e4-8c96-424a-8285-c3146e935a7d/documentation/40496558-2d1d7b6d-1d94-47f6-84e1-e24d977b51b4)
---
## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeatureName`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeatureName`).
5. Open a pull request.

---

## Support

For questions or issues, please open an issue on the GitHub repository.

---

## Technologies Used

- Python
- Flask
- SQLite (or your preferred database)
- JWT for authentication

---

## Contributors

- Poulla Raafat

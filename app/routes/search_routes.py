from flask import Blueprint, request, jsonify
from app.models import Post
from app.schemas.post_schema import posts_schema


search = Blueprint('search', __name__)



@search.route('/search/posts', methods=['GET'])
def search_posts():
    # Get query parameters
    title = request.args.get('title')  # Search by post title

    # Base query
    query = Post.query

    # Filter by title if provided
    if title:
        query = query.filter(Post.title.ilike(f'%{title}%'))

    posts = query.all()

    # Return the results
    return jsonify({
        'message': 'Posts retrieved successfully',
        'data': posts_schema.dump(posts)
    }), 200

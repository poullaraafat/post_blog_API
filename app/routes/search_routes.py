from flask import Blueprint, request, jsonify
from app.models import Post
from app.schemas.post_schema import posts_schema

search = Blueprint('search', __name__)

@search.route('/search/posts', methods=['GET'])
def search_posts():
    # Get query parameters
    title = request.args.get('title')

    # Check if the title parameter is provided
    if not title:
        return jsonify({
            'message': 'The title parameter is required for searching posts',
            'error': 'Missing title parameter'
        }), 400

    # Base query
    query = Post.query

    # Filter posts by title (case-insensitive search)
    query = query.filter(Post.title.ilike(f'%{title}%'))

    # Execute the query
    posts = query.all()

    # Check if no posts are found
    if not posts:
        return jsonify({
            'message': 'No posts found matching the title',
            'error': 'No results'
        }), 404

    # Return the results
    return jsonify({
        'message': 'Posts retrieved successfully',
        'data': posts_schema.dump(posts)
    }), 200

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from app.config import Config

db = SQLAlchemy()
jwt = JWTManager()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    jwt.init_app(app)

    from app.routes.user_routes import user
    from app.routes.post_routes import post
    from app.routes.comment_routes import comment
    from app.routes.auth_routes import auth
    from app.routes.like_routes import like
    from app.routes.search_routes import search
    app.register_blueprint(auth)
    app.register_blueprint(comment)
    app.register_blueprint(user)
    app.register_blueprint(post)
    app.register_blueprint(like)
    app.register_blueprint(search)

    return app

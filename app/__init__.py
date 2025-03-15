from flask import Flask
from app.extensions import db, migrate
from app.config import Config
from app.routes import register_routes
from app.exceptions.exception_handler import register_error_handlers
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    register_routes(app)
    register_error_handlers(app)
    with app.app_context():
        db.create_all()

    return app

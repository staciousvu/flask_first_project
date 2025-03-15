from flask import Flask
from app.routes.auth_routes import auth_bp
from app.routes.category_routes import category_bp
from app.routes.product_routes import product_bp


def register_routes(app:Flask):
    app.register_blueprint(auth_bp)
    app.register_blueprint(category_bp)
    app.register_blueprint(product_bp)



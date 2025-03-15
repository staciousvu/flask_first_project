
from app.services import ProductService
from flask import Blueprint, jsonify, render_template, request, redirect, url_for
from app.models import Product

from app.extensions import db


product_bp = Blueprint('product', __name__)
@product_bp.route("/products")
def getAllProducts():
    products = ProductService.getAll()
    # Chuyển đổi danh sách sản phẩm thành JSON
    return jsonify([{
        'id': product.id,
        'name': product.name,
        'price': product.price,
        'description': product.description,
        'category_id': product.category_id
    } for product in products]),200200

@product_bp.route("/init")
def initilizeData():
    ProductService.initData()
    return jsonify({"message": "Product data initialized successfully."})  # Trả về thông báo JSON





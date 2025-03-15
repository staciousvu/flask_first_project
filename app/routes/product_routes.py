
from app.services import ProductService
from flask import Blueprint, jsonify, render_template, request, redirect, url_for
from app.models import Product

from app.extensions import db


product_bp = Blueprint('product', __name__)
@product_bp.route("/products", methods=["GET"])
def get_all_products():
    products = ProductService.getAll()
    return jsonify([{
        'id': product.id,
        'name': product.name,
        'price': product.price,
        'description': product.description,
        'category_id': product.category_id
    } for product in products]), 200

@product_bp.route("/product/<int:id>", methods=["GET"])
def get_product_by_id(id):
    product = ProductService.getById(id)
    if not product:
        return jsonify({"message": "Product not found"}), 404
    return jsonify({
        'id': product.id,
        'name': product.name,
        'price': product.price,
        'description': product.description,
        'category_id': product.category_id
    }), 200

@product_bp.route("/products", methods=["POST"])
def create_product():
    data = request.get_json()
    product = ProductService.create(data)
    return jsonify({
        'id': product.id,
        'name': product.name,
        'price': product.price,
        'description': product.description,
        'category_id': product.category_id
    }), 201

@product_bp.route("/products/<int:id>", methods=["PUT"])
def update_product(id):
    data = request.get_json()
    product = ProductService.update(id, data)
    if not product:
        return jsonify({"message": "Product not found"}), 404
    return jsonify({
        'id': product.id,
        'name': product.name,
        'price': product.price,
        'description': product.description,
        'category_id': product.category_id
    }), 200

@product_bp.route("/products/<int:id>", methods=["DELETE"])
def delete_product(id):
    if ProductService.delete(id):
        return jsonify({"message": "Product deleted successfully"}), 200
    return jsonify({"message": "Product not found"}), 404

@product_bp.route("/products/search", methods=["GET"])
def search_product():
    keyword = request.args.get("keyword", "")
    products = ProductService.search(keyword)
    return jsonify([{
        'id': product.id,
        'name': product.name,
        'price': product.price,
        'description': product.description,
        'category_id': product.category_id
    } for product in products]), 200

@product_bp.route("/products/filter", methods=["GET"])
def filter_products():
    price_min = request.args.get("price_min", type=float)
    price_max = request.args.get("price_max", type=float)
    category_id = request.args.get("category_id", type=int)
    sort_by = request.args.get("sort_by")
    
    products = ProductService.filter(price_min, price_max, category_id, sort_by)
    return jsonify([{
        'id': product.id,
        'name': product.name,
        'price': product.price,
        'description': product.description,
        'category_id': product.category_id
    } for product in products]), 200

@product_bp.route("/products/paginate", methods=["GET"])
def paginate_products():
    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 10, type=int)
    products = ProductService.paginate(page, per_page)
    return jsonify({
        "total": products.total,
        "pages": products.pages,
        "current_page": products.page,
        "items": [{
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'category_id': product.category_id
        } for product in products.items]
    }), 200

@product_bp.route("/products/count", methods=["GET"])
def count_products():
    count = ProductService.count()
    return jsonify({"total_products": count}), 200








# @product_bp.route("/products")
# def getAllProducts():
#     products = ProductService.getAll()
#     # Chuyển đổi danh sách sản phẩm thành JSON
#     return jsonify([{
#         'id': product.id,
#         'name': product.name,
#         'price': product.price,
#         'description': product.description,
#         'category_id': product.category_id
#     } for product in products]),200200

# @product_bp.route("/init")
# def initilizeData():
#     ProductService.initData()
#     return jsonify({"message": "Product data initialized successfully."})  # Trả về thông báo JSON





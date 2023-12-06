from flask import Blueprint, jsonify, abort, request
from ..models import Product, db

bp = Blueprint('products', __name__, url_prefix='/products')


@bp.route('', methods=['GET'])
def index():
    products = Product.query.all()
    result = [product.serialize() for product in products]
    return jsonify(result)


@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    product = Product.query.get_or_404(id, "Product not found")
    return jsonify(product.serialize())


@bp.route('', methods=['POST'])
def create():
    if 'product_name' not in request.json or 'price' not in request.json:
        return abort(400)

    product = Product(
        product_name=request.json['product_name'],
        price=request.json['price']
    )

    db.session.add(product)
    db.session.commit()
    return jsonify(product.serialize())


@bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    product = Product.query.get_or_404(id, "Product not found")
    try:
        db.session.delete(product)
        db.session.commit()
        return jsonify(True)
    except:
        return jsonify(False)

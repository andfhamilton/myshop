from flask import Blueprint, jsonify, abort, request
from ..models import OrderProduct, db

bp = Blueprint('order_products', __name__, url_prefix='/order_products')


@bp.route('', methods=['GET'])
def index():
    order_products = OrderProduct.query.all()
    result = [op.serialize() for op in order_products]
    return jsonify(result)


@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    order_product = OrderProduct.query.get_or_404(id, "OrderProduct not found")
    return jsonify(order_product.serialize())


@bp.route('', methods=['POST'])
def create():
    if 'order_id' not in request.json or 'product_id' not in request.json or 'quantity' not in request.json or 'price' not in request.json:
        return abort(400)

    order_product = OrderProduct(
        order_id=request.json['order_id'],
        product_id=request.json['product_id'],
        quantity=request.json['quantity'],
        price=request.json['price']
    )

    db.session.add(order_product)
    db.session.commit()
    return jsonify(order_product.serialize())


@bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    order_product = OrderProduct.query.get_or_404(id, "OrderProduct not found")
    try:
        db.session.delete(order_product)
        db.session.commit()
        return jsonify(True)
    except:
        return jsonify(False)

from flask import Blueprint, jsonify, abort, request
from ..models import Order, db

bp = Blueprint('orders', __name__, url_prefix='/orders')


@bp.route('', methods=['GET'])
def index():
    orders = Order.query.all()
    result = [order.serialize() for order in orders]
    return jsonify(result)


@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    order = Order.query.get_or_404(id, "Order not found")
    return jsonify(order.serialize())


@bp.route('', methods=['POST'])
def create():
    if 'customer_id' not in request.json or 'total' not in request.json:
        return abort(400)

    order = Order(
        customer_id=request.json['customer_id'],
        total=request.json['total']
    )

    db.session.add(order)
    db.session.commit()
    return jsonify(order.serialize())


@bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    order = Order.query.get_or_404(id, "Order not found")
    try:
        db.session.delete(order)
        db.session.commit()
        return jsonify(True)
    except:
        return jsonify(False)

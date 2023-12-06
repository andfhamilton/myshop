from flask import Blueprint, jsonify, abort, request
from ..models import Customer, db, Product, Order, OrderProduct
import hashlib
import secrets


def scramble(password: str):
    """Hash and salt the given password """
    salt = secrets.token_hex(16)
    return hashlib.sha512((password + salt).encode('utf-8')).hexdigest()


bp = Blueprint('customers', __name__, url_prefix='/customers')


@bp.route('', methods=['GET'])
def index():
    customers = Customer.query.all()
    result = []
    for customer in customers:
        result.append(customer.serialize())
    return jsonify(result)


@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    customer = Customer.query.get_or_404(id, "Customer not found")
    return jsonify(customer.serialize())


@bp.route('', methods=['POST'])
def create():
    if 'first_name' not in request.json or 'last_name' not in request.json or 'email' not in request.json or 'password' not in request.json:
        return abort(400)

    if len(request.json['first_name']) < 3 or len(request.json['last_name']) < 3 or len(request.json['email']) < 5 or len(request.json['password']) < 8:
        return abort(400)

    customer = Customer(
        first_name=request.json['first_name'],
        last_name=request.json['last_name'],
        email=request.json['email'],
        password=scramble(request.json['password']),
        address=request.json.get('address')
    )

    db.session.add(customer)
    db.session.commit()
    return jsonify(customer.serialize())


@bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    customer = Customer.query.get_or_404(id, "Customer not found")
    try:
        db.session.delete(customer)
        db.session.commit()
        return jsonify(True)
    except:
        return jsonify(False)


@bp.route('/<int:id>', methods=['PATCH', 'PUT'])
def update(id: int):
    customer = Customer.query.get_or_404(id)

    if 'first_name' in request.json:
        if len(request.json['first_name']) >= 3:
            customer.first_name = request.json['first_name']
        else:
            return abort(400)

    if 'last_name' in request.json:
        if len(request.json['last_name']) >= 3:
            customer.last_name = request.json['last_name']
        else:
            return abort(400)

    if 'email' in request.json:
        if len(request.json['email']) >= 5:
            customer.email = request.json['email']
        else:
            return abort(400)

    if 'password' in request.json:
        if len(request.json['password']) >= 8:
            customer.password = scramble(request.json['password'])
        else:
            return abort(400)

    if 'address' in request.json:
        customer.address = request.json['address']

    try:
        db.session.commit()
        return jsonify(customer.serialize())
    except:
        return jsonify(False)

# Additional routes for handling orders and products


@bp.route('/<int:customer_id>/orders', methods=['GET'])
def customer_orders(customer_id: int):
    customer = Customer.query.get_or_404(customer_id)
    orders = Order.query.filter_by(customer_id=customer.id).all()
    result = [order.serialize() for order in orders]
    return jsonify(result)


@bp.route('/<int:customer_id>/products', methods=['GET'])
def customer_products(customer_id: int):
    customer = Customer.query.get_or_404(customer_id)
    orders = Order.query.filter_by(customer_id=customer.id).all()
    products = [
        order_product.product for order in orders for order_product in order.order_products]
    result = [product.serialize() for product in products]
    return jsonify(result)

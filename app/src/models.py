from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

# Define the Customer model


class Customer(db.Model):
    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(128), nullable=False)
    last_name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    address = db.Column(db.String(256))
    orders = db.relationship('Order', backref='customer', lazy=True)

    def __init__(self, first_name, last_name, email, password, address=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.address = address

    def serialize(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'address': self.address
        }

# Define the Product model


class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_name = db.Column(db.String(128), nullable=False)
    price = db.Column(db.Numeric(precision=10, scale=2), nullable=False)
    orders = db.relationship('OrderProduct', backref='product', lazy=True)

    def __init__(self, product_name, price):
        self.product_name = product_name
        self.price = price

    def serialize(self):
        return {
            'id': self.id,
            'product_name': self.product_name,
            'price': float(self.price)
        }

# Define the Order model


class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    customer_id = db.Column(db.Integer, db.ForeignKey(
        'customers.id'), nullable=False)
    total = db.Column(db.Numeric(precision=10, scale=2))
    order_date = db.Column(
        db.DateTime, default=datetime.utcnow, nullable=False)
    order_products = db.relationship(
        'OrderProduct', backref='order', lazy=True)

    def __init__(self, customer_id, total, order_date=None):
        self.customer_id = customer_id
        self.total = total
        if order_date is not None:
            self.order_date = order_date

    def serialize(self):
        return {
            'id': self.id,
            'customer_id': self.customer_id,
            'total': float(self.total),
            'order_date': self.order_date.isoformat()
        }

# Define the OrderProduct model for the many-to-many relationship between Order and Product


class OrderProduct(db.Model):
    __tablename__ = 'orders_products'
    order_id = db.Column(db.Integer, db.ForeignKey(
        'orders.id'), primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey(
        'products.id'), primary_key=True)
    quantity = db.Column(db.Integer)
    price = db.Column(db.Numeric(precision=10, scale=2))

    def __init__(self, order_id, product_id, quantity, price):
        self.order_id = order_id
        self.product_id = product_id
        self.quantity = quantity
        self.price = price

    def serialize(self):
        return {
            'order_id': self.order_id,
            'product_id': self.product_id,
            'quantity': self.quantity,
            'price': float(self.price)
        }

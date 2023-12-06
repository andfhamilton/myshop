import pytest
from app.src import create_app, db

@pytest.fixture
def app():
    app = create_app(
        test_config={'TESTING': True, 'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:'})
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

def client():
    with app.test_client() as client:
        yield client

@pytest.fixture
def customer_data():
    return {
        "first_name": "John",
        "last_name": "Doe",
        "email": "johndoe@example.com",
        "password": "password123",
    }

@pytest.fixture
def product_data():
    return {
        "product_name": "T-shirt",
        "price": 20.00,
    }

@pytest.mark.parametrize("data", [customer_data()])
def test_create_customer(client, data):
    response = client.post("/customers", json=data)
    assert response.status_code == 201
    assert response.json["first_name"] == data["first_name"]

@pytest.mark.parametrize("data", [product_data()])
def test_create_product(client, data):
    response = client.post("/products", json=data)
    assert response.status_code == 201
    assert response.json["product_name"] == data["product_name"]

def test_get_all_customers(client):
    response = client.get("/customers")
    assert response.status_code == 200

def test_get_all_products(client):
    response = client.get("/products")
    assert response.status_code == 200
    

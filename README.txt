Title:
Online Retail Shop Project

Description:
This project is an online retail shop that allows customers to browse products, place orders, and manage their accounts. It provides a simple API for managing customers, products, orders, and order products.

API Reference:

| Endpoint                      | Method | Parameters                           | Description                            |
|-------------------------------|--------|--------------------------------------|----------------------------------------|
| /customers                    | GET    | None                                 | Get a list of all customers            |
| /customers/<int:id>           | GET    | None                                 | Get a specific customer by ID          |
| /customers                    | POST   | JSON: first_name, last_name, email, password, address | Create a new customer |
| /customers/<int:id>           | DELETE | None                                 | Delete a customer by ID                |
| /customers/<int:id>           | PATCH  | JSON: first_name, last_name, email, password, address | Update a customer by ID |
| /products                     | GET    | None                                 | Get a list of all products             |
| /products/<int:id>            | GET    | None                                 | Get a specific product by ID           |
| /products                     | POST   | JSON: product_name, price            | Create a new product                   |
| /products/<int:id>            | DELETE | None                                 | Delete a product by ID                 |
| /orders                       | GET    | None                                 | Get a list of all orders               |
| /orders/<int:id>              | GET    | None                                 | Get a specific order by ID             |
| /orders                       | POST   | JSON: customer_id, total             | Create a new order                     |
| /orders/<int:id>              | DELETE | None                                 | Delete an order by ID                  |
| /order_products               | GET    | None                                 | Get a list of all order products       |
| /order_products/<int:id>      | GET    | None                                 | Get a specific order product by ID     |
| /order_products               | POST   | JSON: order_id, product_id, quantity, price | Create a new order product |
| /order_products/<int:id>      | DELETE | None                                 | Delete an order product by ID          |

Retrospective:

- How did the project's design evolve over time?
  The project initially started with a focus on customer management and later expanded to include products, orders, and order products. The database schema and API routes evolved to accommodate these changes.

- Did you choose to use an ORM or raw SQL? Why?
  I chose to use an ORM (Flask-SQLAlchemy) for this project because it simplifies database interactions, provides an object-oriented approach to data modeling, and enhances code maintainability. ORM allows us to work with database tables as Python classes, making it easier to manage and query data.

- What future improvements are in store, if any?
  Future improvements may include implementing user authentication and authorization, implementing the shopping cart feature, enhancing product search and filtering capabilities, and integrating payment processing for orders, as well as delivery tracking.


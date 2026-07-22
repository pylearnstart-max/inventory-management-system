# Inventory Management System

## Project Overview

The Inventory Management System is a backend application developed using Python, Flask, and SQL Server. It helps manage products, customers, suppliers, users, inventory, and authentication through REST APIs.

---

## Features

- Product Management (CRUD)
- Customer Management (CRUD)
- Supplier Management (CRUD)
- User Management (CRUD)
- JWT Authentication
- Role-Based Authorization (Manager & Employee)
- Password Hashing
- Input Validation
- Global Error Handling
- Logging
- Swagger API Documentation
- Repository Pattern Architecture
- Service Layer Architecture

---

## Technologies Used

- Python 3
- Flask
- Flask-JWT-Extended
- SQL Server
- PyODBC
- bcrypt
- Flask Swagger UI
- Git
- Postman

---

## Project Structure

```
inventory-management-system/
│
├── app.py
├── db.py
├── logger.py
├── requirements.txt
│
├── product_model.py
├── product_repo.py
├── product_service.py
├── product_api.py
│
├── customer_model.py
├── customer_repo.py
├── customer_service.py
├── customer_api.py
│
├── supplier_model.py
├── supplier_repo.py
├── supplier_service.py
├── supplier_api.py
│
├── user_model.py
├── user_repo.py
├── user_service.py
├── user_api.py
│
├── static/
│   └── swagger.json
│
└── README.md
```

---

## Database

Database Name:

```
InventoryDB
```

Tables:

- Products
- Customers
- Suppliers
- Users

---

## Authentication

- JWT Token Based Authentication
- Login API
- Protected APIs
- Role-Based Authorization

Roles:

- Manager
- Employee

---

## API Modules

### Product APIs

- Add Product
- Get All Products
- Get Product By ID
- Update Product
- Delete Product

### Customer APIs

- Add Customer
- Get All Customers
- Search Customer
- Update Customer
- Delete Customer

### Supplier APIs

- Add Supplier
- Get All Suppliers
- Search Supplier
- Update Supplier
- Delete Supplier

### User APIs

- Add User
- Login
- Profile
- Update User
- Delete User
- Change Password

---

## Error Handling

- 404 Not Found
- 500 Internal Server Error
- Global Exception Handling

---

## Logging

Application logs are stored in:

```
inventory.log
```

---

## Swagger Documentation

```
http://127.0.0.1:5000/swagger
```

---

## Installation

Clone Repository

```
git clone <repository-url>
```

Install Dependencies

```
pip install -r requirements.txt
```

Run Application

```
python app.py
```

---

## Author

Developed by sahithi


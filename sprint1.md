# Sprint 1

## Sprint Goal
Develop an Inventory Management System using Python, SQL Server, Git, and the Repository Pattern by implementing CRUD operations.

---

# Story ID
## INV-101

### Title
Setup Inventory Database and Product Table

### Priority
High

### Story Points
2

### Status
✅ Done

### Tasks

- [x] Create InventoryDB
- [x] Create Product Table
- [x] Connect Python to SQL Server
- [x] Create db.py
- [x] Create create_tables.py
- [x] Verify Database Connection

### Git Commit

INV-101 Setup InventoryDB and Product Table

---

# Story ID
## INV-102

### Title
Implement Product Repository and Add Product

### Priority
High

### Story Points
3

### Status
✅ Done

### Tasks

- [x] Create Product Model
- [x] Create Product Repository
- [x] Create add_product()
- [x] Insert Product into SQL Server
- [x] Verify Data
- [x] Create test_repo.py

### Git Commit

INV-102 Implement Product Repository and Add Product

---

# Story ID
## INV-103

### Title
Implement Get All Products

### Priority
High

### Story Points
2

### Status
✅ Done

### Tasks

- [x] Create get_all_products()
- [x] Execute SELECT Query
- [x] Use fetchall()
- [x] Display All Products
- [x] Verify Output

### Git Commit

INV-103 Implement Get All Products

---

# Story ID
## INV-104

### Title
Implement Get Product By ID

### Priority
High

### Story Points
2

### Status
✅ Done

### Tasks

- [x] Create get_product_by_id()
- [x] Execute SELECT Query with WHERE
- [x] Use fetchone()
- [x] Display Single Product
- [x] Verify Output

### Git Commit

INV-104 Implement Get Product By ID

---

# Story ID
## INV-105

### Title
Implement Update Product

### Priority
High

### Story Points
3

### Status
✅ Done

### Tasks

- [x] Create update_product()
- [x] Execute UPDATE Query
- [x] Use SET Clause
- [x] Use WHERE Clause
- [x] Verify Updated Data
- [x] Create test_update_product.py

### Git Commit

INV-105 Implement Update Product

---

# Story ID
## INV-106

### Title
Implement Delete Product

### Priority
High

### Story Points
3

### Status
✅ Done

### Tasks

- [x] Create delete_product()
- [x] Execute DELETE Query
- [x] Use WHERE Clause
- [x] Delete Product by ID
- [x] Verify Deleted Data
- [x] Create test_delete_product.py

### Git Commit

INV-106 Implement Delete Product

---

Story ID: INV-107

Title: Implement Product Service Layer

Status: Done

Tasks

[x] Create ProductService
[x] Implement add_product()
[x] Implement get_all_products()
[x] Implement get_product_by_id()
[x] Implement update_product()
[x] Implement delete_product()
[x] Test all methods

Git Commit

INV-107 Implement Product Service Layer
---

# Story ID

## INV-108

### Title

Implement Flask POST API

### Priority

High

### Story Points

3

### Status

✅ Done

### Tasks

* [x] Install Flask package
* [x] Create `api.py`
* [x] Create Flask application
* [x] Create Home API (`GET /`)
* [x] Import Product Model
* [x] Import ProductService
* [x] Create ProductService object
* [x] Implement `POST /products` API
* [x] Read request data using `request.get_json()`
* [x] Create Product object from JSON data
* [x] Call `service.add_product()`
* [x] Return JSON success response
* [x] Run Flask application
* [x] Test POST API using Postman
* [x] Verify inserted data in SQL Server

### Files Created

* [x] api.py

### Technologies Used

* Python
* Flask
* SQL Server
* Postman

### Git Commit

INV-108 Implement Flask POST API

---

# Story ID

## INV-109

### Title

Implement Flask GET APIs

### Priority

High

### Story Points

3

### Status

✅ Done

### Tasks

* [x] Implement `GET /products` API
* [x] Call `service.get_all_products()`
* [x] Retrieve all products from SQL Server
* [x] Convert product list into JSON format
* [x] Return all product details
* [x] Implement `GET /products/<product_id>` API
* [x] Call `service.get_product_by_id()`
* [x] Retrieve product using Product ID
* [x] Handle Product Not Found response
* [x] Return product details in JSON format
* [x] Test GET APIs using Postman
* [x] Verify API responses

### Files Updated

* [x] api.py

### Technologies Used

* Python
* Flask
* SQL Server
* Postman

### Git Commit

INV-109 Implement Flask GET APIs

---

# Story ID

## INV-110

### Title

Implement Flask PUT API, DELETE API and Complete Sprint Review

### Priority

High

### Story Points

4

### Status

✅ Done

### Tasks

* [x] Implement `PUT /products/<product_id>` API
* [x] Read updated product details from JSON request
* [x] Create Product object
* [x] Call `service.update_product()`
* [x] Return update success response
* [x] Test PUT API using Postman
* [x] Verify updated data in SQL Server
* [x] Implement `DELETE /products/<product_id>` API
* [x] Call `service.delete_product()`
* [x] Return delete success response
* [x] Test DELETE API using Postman
* [x] Verify deleted data in SQL Server
* [x] Verify all CRUD APIs
* [x] Complete Sprint 1 Review
* [x] Finalize Sprint 1 Documentation

### Files Updated

* [x] api.py

### Technologies Used

* Python
* Flask
* SQL Server
* Postman
* Git

### Git Commit

INV-110 Complete Sprint 1 REST APIs

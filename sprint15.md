# Sprint 15 Update – Product REST API Module

**Sprint:** Sprint 15
**Module:** Product REST API
**Project:** Inventory Management System

## User Stories Completed

### INV-1501 – Create Product REST API

**Status:** Done

**Tasks Completed**

* Created Product API using Flask Blueprint
* Registered Product API in Flask application
* Configured REST endpoints

---

### INV-1502 – Implement Get All Products API

**Status:** Done

**Tasks Completed**

* Developed GET `/products`
* Returned product list in JSON format
* Tested successfully using Postman

---

### INV-1503 – Implement Get Product By ID API

**Status:** Done

**Tasks Completed**

* Developed GET `/products/<product_id>`
* Added Product Not Found validation
* Returned JSON response
* Tested successfully using Postman

---

### INV-1504 – Implement Add Product API

**Status:** Done

**Tasks Completed**

* Developed POST `/products`
* Accepted JSON request body
* Added request validation
* Inserted records into SQL Server
* Tested successfully using Postman

---

### INV-1505 – Implement Update Product API

**Status:** Done

**Tasks Completed**

* Developed PUT `/products/<product_id>`
* Updated existing product details
* Added validation
* Tested successfully using Postman

---

### INV-1506 – Implement Delete Product API

**Status:** Done

**Tasks Completed**

* Developed DELETE `/products/<product_id>`
* Deleted product using Product ID
* Tested successfully using Postman

---

## Testing

* Verified all CRUD APIs using Postman
* Verified database changes in SQL Server
* Handled API exceptions and error responses
* Returned appropriate HTTP status codes (200, 201, 400, 404, 500)

---

## Sprint Outcome

**Sprint Status:** Completed

### Deliverables

* Product REST API
* CRUD Operations
* JSON Request/Response Handling
* Flask Blueprint Integration
* SQL Server Integration
* Postman API Testing
* Exception Handling

**Sprint Result:** Successfully Completed

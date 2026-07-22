# Sprint 17 Update – Supplier Management Module

**Sprint ID:** Sprint 17
**Module:** Supplier Management
**Status:** Completed

## User Stories Completed

### INV-1701 – Create Supplier Model

**Status:** Done

**Completed:**

* Created `supplier_model.py`
* Added Supplier class
* Implemented constructor with:

  * supplier_id
  * supplier_name
  * phone
  * email
  * address
  * created_date

---

### INV-1702 – Implement Supplier Repository

**Status:** Done

**Completed:**

* Created `supplier_repo.py`
* Implemented Add Supplier
* Implemented Get All Suppliers
* Implemented Search Supplier by ID
* Implemented Search Supplier by Name
* Implemented Update Supplier
* Implemented Delete Supplier
* Implemented Supplier Report

---

### INV-1703 – Implement Supplier Service

**Status:** Done

**Completed:**

* Created `supplier_service.py`
* Connected Service Layer with Repository Layer
* Added business methods for all CRUD operations
* Added Search functionality
* Added Supplier Report method

---

### INV-1704 – Implement Supplier API

**Status:** Done

**Completed:**

* GET /suppliers
* GET /suppliers/{id}
* POST /suppliers
* PUT /suppliers/{id}
* DELETE /suppliers/{id}
* GET /suppliers/search/{supplier_name}
* GET /suppliers/report

---

### INV-1705 – Testing

**Status:** Completed

**Completed:**

* API validation
* JSON request testing
* CRUD endpoint verification
* Error handling verification
* SQL Server integration testing

---

## Sprint Outcome

* Supplier Management Module implemented successfully.
* Repository Pattern followed.
* Service Layer implemented.
* REST APIs created.
* SQL Server integration completed.
* CRUD operations working.
* Search and Report functionality impleme

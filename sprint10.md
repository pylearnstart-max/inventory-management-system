# Sprint 10 – Customer Order Management

## Sprint Goal

Develop the Customer Order Management module using Python, SQL Server, Repository Pattern, Service Layer, Git, and Sprint Documentation.

---

# Story ID

## INV-1001

### Title

Create CustomerOrder Table

### Priority

High

### Story Points

2

### Status

✅ Completed

---

## Tasks

- [x] Design CustomerOrder table
- [x] Create CustomerOrder table in SQL Server
- [x] Create create_customer_order_table.py
- [x] Execute table creation script
- [x] Verify CustomerOrder table

---

## Database Table

### CustomerOrder

| Column | Data Type |
|---------|-----------|
| customer_order_id | INT IDENTITY PRIMARY KEY |
| customer_id | INT |
| order_id | INT |
| order_date | DATE |

---

## Foreign Keys

- customer_id → Customer(customer_id)
- order_id → Orders(order_id)

---

## File Created

```
create_customer_order_table.py
```

---

## SQL Used

```sql
CREATE TABLE CustomerOrder
(
    customer_order_id INT IDENTITY(1,1) PRIMARY KEY,
    customer_id INT NOT NULL,
    order_id INT NOT NULL,
    order_date DATE NOT NULL,

    CONSTRAINT FK_CustomerOrder_Customer
    FOREIGN KEY(customer_id)
    REFERENCES Customer(customer_id),

    CONSTRAINT FK_CustomerOrder_Order
    FOREIGN KEY(order_id)
    REFERENCES Orders(order_id)
);
```

---

## Test Result

Command

```bash
python create_customer_order_table.py
```

Output

```
CustomerOrder Table Created Successfully
```

---

## Database Verification

```sql
SELECT * FROM CustomerOrder;
```

Table created successfully.

---

## Git Commit

```bash
git add .
git commit -m "INV-1001 Create CustomerOrder Table"
```

---

# Story Completion

✅ CustomerOrder table created successfully.

✅ Foreign key relationships established.

✅ SQL Server table verified.

---

# Sprint 10 Progress

| Story ID | Title | Status |
|----------|------------------------------|--------|
| INV-1001 | Create CustomerOrder Table | ✅ Done |
| INV-1002 | Add Customer Order | ⏳ Pending |
| INV-1003 | Get All Customer Orders | ⏳ Pending |
| INV-1004 | Search Customer Order | ⏳ Pending |
| INV-1005 | Update Customer Order | ⏳ Pending |
| INV-1006 | Delete Customer Order | ⏳ Pending |
| INV-1007 | Customer Order Report | ⏳ Pending |
| INV-1008 | Testing & Documentation | ⏳ Pending |

**Sprint 10 Progress: 1/8 Stories Completed (12.5%)**
# Story ID

## INV-1002

### Title
Add Customer Order

### Priority
High

### Story Points
2

### Status
✅ Completed

---

## Story Description

As an Admin, I want to add a Customer Order so that customer purchases can be linked with existing orders.

---

## Tasks

- [x] Create CustomerOrder Model
- [x] Create CustomerOrder Repository
- [x] Create CustomerOrder Service
- [x] Create test_add_customer_order.py
- [x] Insert Customer Order into SQL Server
- [x] Verify Foreign Key relationships
- [x] Verify inserted record

---

## Files Created

```
customer_order_model.py
customer_order_repo.py
customer_order_service.py
test_add_customer_order.py
```

---

## Model

```
CustomerOrder
```

### Attributes

- customer_id
- order_id
- order_date

---

## Repository Method

```
add_customer_order()
```

---

## Service Method

```
add_customer_order()
```

---

## Database Table

```
CustomerOrder
```

### Columns

- customer_order_id
- customer_id
- order_id
- order_date

---

## Validation

- Customer ID must exist in the Customer table.
- Order ID must exist in the Orders table.
- Foreign key constraints validated before insertion.

---

## Test Result

### Command

```bash
python test_add_customer_order.py
```

### Expected Output

```
Customer Order Added Successfully
```

---

## SQL Verification

```sql
SELECT * FROM CustomerOrder;
```

Example Output

```
customer_order_id | customer_id | order_id | order_date
--------------------------------------------------------
1                 | 2           | 4        | 2026-07-17
```

---

## Git Commit

```bash
git add .
git commit -m "INV-1002 Add Customer Order"
```

---

## Story Completion

- ✅ Customer Order model implemented.
- ✅ Repository layer implemented.
- ✅ Service layer implemented.
- ✅ Customer Order inserted successfully.
- ✅ SQL Server data verified.
- ✅ Repository Pattern followed.
- ✅ Foreign key relationships validated.
# Story ID

## INV-1003

### Title

Get All Customer Orders

### Priority

High

### Story Points

2

### Status

✅ Completed

---

## Story Description

As an Admin, I want to view all Customer Orders so that I can monitor customer order transactions.

---

## Tasks

- [x] Implement get_all_customer_orders() in Repository
- [x] Implement get_all_customer_orders() in Service
- [x] Create test_get_all_customer_orders.py
- [x] Retrieve all customer orders
- [x] Verify data from SQL Server

---

## Files Updated

```
customer_order_repo.py
customer_order_service.py
```

## Files Created

```
test_get_all_customer_orders.py
```

---

## Repository Method

```
get_all_customer_orders()
```

---

## Service Method

```
get_all_customer_orders()
```

---

## SQL Query

```sql
SELECT
    customer_order_id,
    customer_id,
    order_id,
    order_date
FROM CustomerOrder
ORDER BY customer_order_id;
```

---

## Test Result

### Command

```bash
python test_get_all_customer_orders.py
```

### Expected Output

```
========== CUSTOMER ORDER LIST ==========

(1, 2, 4, datetime.date(2026, 7, 17))
```

Or

```
========== CUSTOMER ORDER LIST ==========

No Customer Orders Found
```

---

## SQL Verification

```sql
SELECT * FROM CustomerOrder;
```

---

## Git Commit

```bash
git add .
git commit -m "INV-1003 Get All Customer Orders"
```

---

# Story Completion

- ✅ Customer Order Repository updated.
- ✅ Service Layer implemented.
- ✅ Customer Orders retrieved successfully.
- ✅ SQL Server data verified.
- ✅ Repository Pattern followed.

---

# Sprint 10 Progress

| Story ID | Title | Status |
|----------|-------------------------------|--------|
| INV-1001 | Create CustomerOrder Table | ✅ Done |
| INV-1002 | Add Customer Order | ✅ Done |
| INV-1003 | Get All Customer Orders | ✅ Done |
| INV-1004 | Search Customer Order | ⏳ Pending |
| INV-1005 | Update Customer Order | ⏳ Pending |
| INV-1006 | Delete Customer Order | ⏳ Pending |
| INV-1007 | Customer Order Report | ⏳ Pending |
| INV-1008 | Testing & Documentation | ⏳ Pending |

## Sprint Progress

**Completed:** 3 / 8 Stories (37.5%)

**Remaining:** INV-1004 to INV-1008
# Story ID

## INV-1004

### Title

Search Customer Order

### Priority

High

### Story Points

2

### Status

✅ Completed

---

## Story Description

As an Admin, I want to search a Customer Order by its ID so that I can quickly retrieve a specific customer order.

---

## Tasks

- [x] Implement search_customer_order() in Repository
- [x] Implement search_customer_order() in Service
- [x] Create test_search_customer_order.py
- [x] Search Customer Order by ID
- [x] Verify search result

---

## Files Updated

```
customer_order_repo.py
customer_order_service.py
```

## Files Created

```
test_search_customer_order.py
```

---

## Repository Method

```
search_customer_order()
```

---

## Service Method

```
search_customer_order()
```

---

## SQL Query

```sql
SELECT
    customer_order_id,
    customer_id,
    order_id,
    order_date
FROM CustomerOrder
WHERE customer_order_id = ?;
```

---

## Test Command

```bash
python test_search_customer_order.py
```

### Expected Output (Record Found)

```
========== SEARCH CUSTOMER ORDER ==========

(1, 2, 4, 2026-07-17)
```

### Alternative Output

```
========== SEARCH CUSTOMER ORDER ==========

Customer Order Not Found
```

---

## SQL Verification

```sql
SELECT * FROM CustomerOrder
WHERE customer_order_id = 1;
```

---

## Git Commands

```bash
git add .
git commit -m "INV-1004 Search Customer Order"
```

---

# Story Completion

- ✅ Customer Order search implemented.
- ✅ Repository layer updated.
- ✅ Service layer updated.
- ✅ Search functionality tested.
- ✅ Repository Pattern followed.

---

# Sprint 10 Progress

| Story ID | Title | Status |
|----------|-------------------------------|--------|
| INV-1001 | Create CustomerOrder Table | ✅ Done |
| INV-1002 | Add Customer Order | ✅ Done |
| INV-1003 | Get All Customer Orders | ✅ Done |
| INV-1004 | Search Customer Order | ✅ Done |
| INV-1005 | Update Customer Order | ⏳ Pending |
| INV-1006 | Delete Customer Order | ⏳ Pending |
| INV-1007 | Customer Order Report | ⏳ Pending |
| INV-1008 | Testing & Documentation | ⏳ Pending |

## Sprint Progress

**Completed:** 4 / 8 Stories (**50%**)

**Remaining:** INV-1005, INV-1006, INV-1007, INV-1008
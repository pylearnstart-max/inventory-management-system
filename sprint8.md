# Story ID

## INV-801

### Title
Create Orders Table

### Priority
High

### Story Points
2

### Status
✅ Completed

---

## Tasks

- [x] Create Orders table
- [x] Add Primary Key
- [x] Add Customer Foreign Key
- [x] Add Product Foreign Key
- [x] Verify table creation
- [x] Create create_order_table.py

---

## Files Created

- create_order_table.py

---

## Database

### Database Used

InventoryDB

### Table Created

Orders

---

## Table Structure

```sql
CREATE TABLE Orders
(
    order_id INT IDENTITY(1,1) PRIMARY KEY,
    customer_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    unit_price DECIMAL(10,2) NOT NULL,
    total_amount DECIMAL(10,2) NOT NULL,
    order_date DATE NOT NULL
)
```

---

## Foreign Key Relations

```sql
customer_id
    REFERENCES Customer(customer_id)

product_id
    REFERENCES Product(product_id)
```

---

## Test Result

### Table Creation

```text
Orders Table Created Successfully
Process Completed Successfully
```

### Table Verification

```sql
SELECT * FROM Orders;
```

Result:

```text
Empty table - 0 rows
```

Table is ready for adding order records.

---

## Git Commit

```bash
git add .
git commit -m "INV-801 Create Orders Table"
```

---

## Story Completion

✅ Orders table created successfully.

✅ Primary key configured.

✅ Foreign key relationships added.

✅ SQL Server verification completed.

✅ Ready for INV-802 – Add Order.
# Story ID

## INV-802

### Title
Add Order

### Priority
High

### Story Points
2

### Status
✅ Completed

---

## Tasks

- [x] Create order_model.py
- [x] Create order_repo.py
- [x] Create order_service.py
- [x] Implement add_order() in Order Repository
- [x] Implement add_order() in Order Service
- [x] Create test_add_order.py
- [x] Insert order into Orders table
- [x] Verify SQL data

---

## Files Created

- order_model.py
- order_repo.py
- order_service.py
- test_add_order.py

---

## Database

### Table Used

Orders

---

## SQL Query Used

```sql
INSERT INTO Orders
(
    customer_id,
    product_id,
    quantity,
    unit_price,
    total_amount,
    order_date
)
VALUES
(
    ?, ?, ?, ?, ?, ?
);
```

---

## Test Result

### Add Order

```text
python test_add_order.py
```

Output:

```text
Order Added Successfully
```

---

## Database Verification

```sql
SELECT * FROM Orders;
```

Result:

```text
Order Record Inserted Successfully
```

---

## Issue Handled

Foreign Key validation handled:

- customer_id must exist in Customer table
- product_id must exist in Product table

---

## Git Commit

```bash
git add .
git commit -m "INV-802 Add Order"
```

---

## Story Completion

✅ Order added successfully.

✅ Repository Pattern followed.

✅ Order inserted into SQL Server.

✅ Customer and Product foreign key relationships verified.

✅ Ready for INV-803 – View All Orders.
# Story ID

## INV-803

### Title
View All Orders

### Priority
High

### Story Points
2

### Status
✅ Completed

---

## Tasks

- [x] Implement get_all_orders() in Order Repository
- [x] Implement get_all_orders() in Order Service
- [x] Create test_get_all_orders.py
- [x] Fetch all orders from Orders table
- [x] Display order details
- [x] Handle empty orders scenario
- [x] Test View All Orders functionality

---

## Files Updated

- order_repo.py
- order_service.py

## Files Created

- test_get_all_orders.py

---

## Database

### Table Used

Orders

---

## SQL Query Used

```sql
SELECT *
FROM Orders
ORDER BY order_id;
```

---

## Test Result

### Existing Orders

```text
========== ORDER LIST ==========

(1, 2, 4, 2, 55000.00, 110000.00, 2026-07-17)
```

### Empty Orders

```text
========== ORDER LIST ==========

No Orders Found
```

---

## Git Commit

```bash
git add .
git commit -m "INV-803 View All Orders"
```

---

## Story Completion

✅ View All Orders implemented successfully.

✅ Repository Pattern followed.

✅ Orders fetched from SQL Server.

✅ Empty order scenario handled correctly.

✅ Ready for INV-804 – Search Order.
# Story ID

## INV-804

### Title
Search Order

### Priority
High

### Story Points
2

### Status
✅ Completed

---

## Tasks

- [x] Implement search_order() in Order Repository
- [x] Implement search_order() in Order Service
- [x] Create test_search_order.py
- [x] Search Order by Order ID
- [x] Display Order Details
- [x] Handle "Order Not Found" scenario
- [x] Test Search Order functionality

---

## Files Updated

- order_repo.py
- order_service.py

## Files Created

- test_search_order.py

---

## Database

### Table Used

Orders

---

## SQL Query Used

```sql
SELECT *
FROM Orders
WHERE order_id = ?;
```

---

## Test Result

### Existing Order

```text
Enter Order ID: 1

========== SEARCH ORDER ==========

(1, 2, 4, 2, 55000.00, 110000.00, 2026-07-17)
```

### Non-Existing Order

```text
Enter Order ID: 100

========== SEARCH ORDER ==========

Order Not Found
```

---

## Git Commit

```bash
git add .
git commit -m "INV-804 Search Order"
```

---

## Story Completion

✅ Search Order implemented successfully.

✅ Repository Pattern followed.

✅ Order searched using Order ID.

✅ "Order Not Found" handled correctly.

✅ Ready for INV-805 – Update Order.
# Story ID

## INV-805

### Title
Update Order

### Priority
High

### Story Points
2

### Status
✅ Completed

---

## Tasks

- [x] Implement update_order() in Order Repository
- [x] Implement update_order() in Order Service
- [x] Create test_update_order.py
- [x] Update Order by Order ID
- [x] Update quantity and total amount
- [x] Handle "Order Not Found" scenario
- [x] Test Update Order functionality

---

## Files Updated

- order_repo.py
- order_service.py

## Files Created

- test_update_order.py

---

## Database

### Table Used

Orders

---

## SQL Query Used

```sql
UPDATE Orders
SET quantity = ?,
    total_amount = ?
WHERE order_id = ?;
```

---

## Test Result

### Existing Order Update

```text
Enter Order ID: 1

Enter New Quantity: 8

Enter New Total Amount: 2317


========== UPDATE ORDER ==========

Order Updated Successfully
```

### Non-Existing Order

```text
Enter Order ID: 13

Enter New Quantity: 4

Enter New Total Amount: 10987


========== UPDATE ORDER ==========

Order Not Found
```

---

## Git Commit

```bash
git add .
git commit -m "INV-805 Update Order"
```

---

## Story Completion

✅ Update Order implemented successfully.

✅ Repository Pattern followed.

✅ Order details updated using Order ID.

✅ "Order Not Found" handled correctly.

✅ Ready for INV-806 – Delete Order.
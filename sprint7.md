# Story ID

## INV-701

### Title
Create Purchase Table

### Priority
High

### Story Points
2

### Status
✅ Completed

---

## Tasks

- [x] Create Purchase table in SQL Server
- [x] Create create_purchase_table.py
- [x] Add Primary Key
- [x] Add Foreign Key for Product
- [x] Add Foreign Key for Supplier
- [x] Verify Purchase table creation

---

## Files Created

- create_purchase_table.py

---

## Database

### Table Created

Purchase

---

## Table Structure

| Column | Data Type |
|---------|-----------|
| purchase_id | INT IDENTITY(1,1) PRIMARY KEY |
| product_id | INT NOT NULL |
| supplier_id | INT NOT NULL |
| quantity | INT NOT NULL |
| unit_price | DECIMAL(10,2) |
| total_amount | DECIMAL(10,2) |
| purchase_date | DATE |

---

## SQL Query Used

```sql
CREATE TABLE Purchase
(
    purchase_id INT IDENTITY(1,1) PRIMARY KEY,
    product_id INT NOT NULL,
    supplier_id INT NOT NULL,
    quantity INT NOT NULL,
    unit_price DECIMAL(10,2) NOT NULL,
    total_amount DECIMAL(10,2) NOT NULL,
    purchase_date DATE NOT NULL,

    CONSTRAINT FK_Purchase_Product
        FOREIGN KEY(product_id)
        REFERENCES Product(product_id),

    CONSTRAINT FK_Purchase_Supplier
        FOREIGN KEY(supplier_id)
        REFERENCES Supplier(supplier_id)
);
```

---

## Test Result

### Table Verification

```text
Purchase table created successfully.

OR

Purchase table already exists.
```

Both results are acceptable because the table exists after the first successful creation.

---

## Files Verified

- create_purchase_table.py
- db.py

---

## Git Commit

```bash
git add .
git commit -m "INV-701 Create Purchase Table"
```

---

## Story Completion

✅ Purchase table created successfully.

✅ Primary Key configured.

✅ Foreign Key with Product table configured.

✅ Foreign Key with Supplier table configured.

✅ Purchase table verified in SQL Server.

✅ Ready for INV-702 – Add Purchase.
# Story ID

## INV-702

### Title
Add Purchase

### Priority
High

### Story Points
2

### Status
✅ Completed

---

## Tasks

- [x] Create Purchase Model
- [x] Implement add_purchase() in Purchase Repository
- [x] Implement add_purchase() in Purchase Service
- [x] Create test_add_purchase.py
- [x] Insert Purchase into Purchase table
- [x] Test Add Purchase functionality

---

## Files Created

- purchase_model.py
- purchase_repo.py
- purchase_service.py
- test_add_purchase.py

---

## Database

### Table Used

Purchase

---

## SQL Query Used

```sql
INSERT INTO Purchase
(
    product_id,
    supplier_id,
    quantity,
    unit_price,
    total_amount,
    purchase_date
)
VALUES
(
    ?, ?, ?, ?, ?, ?
);
```

---

## Test Result

### Existing Product & Supplier

```text
Purchase Added Successfully
```

### Validation

```text
Purchase record inserted successfully into SQL Server.
```

---

## Files Updated

- purchase_repo.py
- purchase_service.py

---

## Git Commit

```bash
git add .
git commit -m "INV-702 Add Purchase"
```

---

## Story Completion

✅ Purchase Model created successfully.

✅ Repository Pattern implemented.

✅ Purchase inserted into SQL Server.

✅ Purchase Service implemented successfully.

✅ Purchase tested successfully.

✅ Ready for INV-703 – View All Purchases.
# Story ID

## INV-703

### Title
View All Purchases

### Priority
High

### Story Points
2

### Status
✅ Completed

---

## Tasks

- [x] Implement get_all_purchases() in Purchase Repository
- [x] Implement get_all_purchases() in Purchase Service
- [x] Create test_get_all_purchases.py
- [x] Display all purchase records
- [x] Test View All Purchases functionality

---

## Files Updated

- purchase_repo.py
- purchase_service.py

## Files Created

- test_get_all_purchases.py

---

## Database

### Table Used

Purchase

---

## SQL Query Used

```sql
SELECT *
FROM Purchase
ORDER BY purchase_id;
```

---

## Test Result

### Purchase Records Available

```text
========== PURCHASE LIST ==========

(1, 4, 1, 10, 5000.00, 50000.00, 2026-07-17)
(2, 5, 2, 20, 1500.00, 30000.00, 2026-07-18)
```

### No Records Available

```text
========== PURCHASE LIST ==========

No Purchase Records Found
```

---

## Git Commit

```bash
git add .
git commit -m "INV-703 View All Purchases"
```

---

## Story Completion

✅ View All Purchases implemented successfully.

✅ Repository Pattern followed.

✅ Purchase records displayed successfully.

✅ "No Purchase Records Found" handled correctly.

✅ Ready for INV-704 – Search Purchase.

# Story ID

## INV-704

### Title
Search Purchase

### Priority
High

### Story Points
2

### Status
✅ Completed

---

## Tasks

- [x] Implement search_purchase() in Purchase Repository
- [x] Implement search_purchase() in Purchase Service
- [x] Create test_search_purchase.py
- [x] Search Purchase by Purchase ID
- [x] Display Purchase Details
- [x] Handle "Purchase Not Found" scenario
- [x] Test Search Purchase functionality

---

## Files Updated

- purchase_repo.py
- purchase_service.py

## Files Created

- test_search_purchase.py

---

## Database

### Table Used

Purchase

---

## SQL Query Used

```sql
SELECT *
FROM Purchase
WHERE purchase_id = ?;
```

---

## Test Result

### Existing Purchase

```text
Enter Purchase ID: 1

========== SEARCH PURCHASE ==========

(1, 4, 1, 10, 5000.00, 50000.00, 2026-07-17)
```

### Non-Existing Purchase

```text
Enter Purchase ID: 100

========== SEARCH PURCHASE ==========

Purchase Not Found
```

---

## Git Commit

```bash
git add .
git commit -m "INV-704 Search Purchase"
```

---

## Story Completion

✅ Search Purchase implemented successfully.

✅ Repository Pattern followed.

✅ Purchase searched using Purchase ID.

✅ "Purchase Not Found" handled correctly.

✅ Ready for INV-705 – Update Purchase.
# Story ID

## INV-706

### Title
Delete Purchase

### Priority
High

### Story Points
2

### Status
✅ Completed

---

## Tasks

- [x] Implement delete_purchase() in Purchase Repository
- [x] Implement delete_purchase() in Purchase Service
- [x] Create test_delete_purchase.py
- [x] Delete Purchase by Purchase ID
- [x] Display Success Message
- [x] Handle "Purchase Not Found" scenario
- [x] Test Delete Purchase functionality

---

## Files Updated

- purchase_repo.py
- purchase_service.py

## Files Created

- test_delete_purchase.py

---

## Database

### Table Used

Purchase

---

## SQL Query Used

```sql
DELETE FROM Purchase
WHERE purchase_id = ?;
```

---

## Test Result

### Existing Purchase

```text
Enter Purchase ID: 1

========== DELETE PURCHASE ==========

Purchase Deleted Successfully
```

### Non-Existing Purchase

```text
Enter Purchase ID: 100

========== DELETE PURCHASE ==========

Purchase Not Found
```

---

## Git Commit

```bash
git add .
git commit -m "INV-706 Delete Purchase"
```

---

## Story Completion

✅ Delete Purchase implemented successfully.

✅ Repository Pattern followed.

✅ Purchase deleted using Purchase ID.

✅ "Purchase Not Found" handled correctly.

✅ Ready for INV-707 – Purchase Report.
# Story ID

## INV-707

### Title
Purchase Report

### Priority
High

### Story Points
2

### Status
✅ Completed

---

## Tasks

- [x] Implement purchase_report() in Purchase Repository
- [x] Implement purchase_report() in Purchase Service
- [x] Create test_purchase_report.py
- [x] Display Total Purchases
- [x] Display Total Purchase Amount
- [x] Test Purchase Report functionality

---

## Files Updated

- purchase_repo.py
- purchase_service.py

## Files Created

- test_purchase_report.py

---

## Database

### Table Used

Purchase

---

## SQL Query Used

```sql
SELECT
    COUNT(purchase_id) AS total_purchases,
    SUM(total_amount) AS total_purchase_amount
FROM Purchase;
```

---

## Test Result

### Purchase Report

```text
========== PURCHASE REPORT ==========

Total Purchases      : 0
Total Purchase Amount: 0
```

> Note: If the `Purchase` table has no records, `COUNT()` returns `0` and `SUM()` is displayed as `0` after handling the `None` value in Python.

---

## Git Commit

```bash
git add .
git commit -m "INV-707 Purchase Report"
```

---

## Story Completion

✅ Purchase Report implemented successfully.

✅ Repository Pattern followed.

✅ Total Purchases displayed successfully.

✅ Total Purchase Amount displayed successfully.

✅ Empty table scenario handled correctly.

✅ Ready for INV-708 – Sprint Testing & Documentation.
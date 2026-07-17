Excellent! 🚀 Let's begin **Sprint 6 – Sales Management**.

This sprint will connect **Products + Customers + Sales**, making your project much closer to a real inventory management system.

---

# Sprint 6

## Sprint Goal

Develop the **Sales Management Module** using Python, SQL Server, and the Repository Pattern.

---

# Sprint Stories

| Story ID | Title                            | Priority | Status         |
| -------- | -------------------------------- | -------- | -------------- |
| INV-601  | Create Sales Table               | High     | 🟡 In Progress |
| INV-602  | Add Sale                         | High     | Pending        |
| INV-603  | View All Sales                   | High     | Pending        |
| INV-604  | Search Sale                      | High     | Pending        |
| INV-605  | Sales Report                     | High     | Pending        |
| INV-606  | Revenue Report                   | High     | Pending        |
| INV-607  | Sales Dashboard                  | High     | Pending        |
| INV-608  | Sprint 6 Testing & Documentation | High     | Pending        |

---

# INV-601

## Title

Create Sales Table

### Status

🟡 In Progress

---

## Step 1: Create `create_sales_table.py`

```python
from db import get_connection

conn = get_connection()
cursor = conn.cursor()

cursor.execute("""
IF OBJECT_ID('Sales', 'U') IS NULL
BEGIN
    CREATE TABLE Sales
    (
        sale_id INT IDENTITY(1,1) PRIMARY KEY,
        product_id INT NOT NULL,
        customer_id INT NOT NULL,
        quantity INT NOT NULL,
        unit_price DECIMAL(10,2) NOT NULL,
        total_amount DECIMAL(10,2) NOT NULL,
        sale_date DATE NOT NULL,

        FOREIGN KEY (product_id) REFERENCES Product(product_id),
        FOREIGN KEY (customer_id) REFERENCES Customer(customer_id)
    )
END
""")

conn.commit()

cursor.close()
conn.close()

print("Sales Table Created Successfully")
```

---

## Step 2: Run

```bash
python create_sales_table.py
```

### Expected Output

```text
Sales Table Created Successfully
```

---

## Step 3: Verify in SQL Server

```sql
SELECT * FROM Sales;
```

You should see an empty table with columns:

| sale_id | product_id | customer_id | quantity | unit_price | total_amount | sale_date |
| ------- | ---------- | ----------- | -------- | ---------- | ------------ | --------- |

---

## Step 4: Git Commit

```bash
git add .
git commit -m "INV-601 Create Sales Table"
```

---

# Sprint 6 Update

## Story ID

### INV-601

**Title:** Create Sales Table

**Priority:** High

**Story Points:** 2

**Status:** 🟡 In Progress

### Tasks

* [ ] Create `create_sales_table.py`
* [ ] Create `Sales` table in SQL Server
* [ ] Add foreign key to `Product`
* [ ] Add foreign key to `Customer`
* [ ] Verify table in SQL Server
* [ ] Commit to Git

---

After **INV-601** is completed, we'll proceed to **INV-602 – Add Sale**, where you'll insert sales records and automatically calculate the total amount. This is a common interview scenario and a valuable feature for your project.
# Story ID

## INV-602

### Title
Add Sale

### Priority
High

### Story Points
3

### Status
✅ Completed

---

## Tasks

- [x] Create Sales Model
- [x] Create Sales Repository
- [x] Create Sales Service
- [x] Create Test File
- [x] Insert Sale into Sales Table
- [x] Resolve Foreign Key Constraint
- [x] Verify Product ID
- [x] Verify Customer ID
- [x] Test Add Sale Functionality

---

## Files Created

- sales_model.py
- sales_repo.py
- sales_service.py
- test_add_sale.py

---

## Database

### Table Used
Sales

---

## Test Result

```
Sale Added Successfully
```

---

## SQL Verification

```sql
SELECT * FROM Sales;
```

Result:
- Sale record inserted successfully.
- Product ID validated.
- Customer ID validated.

---

## Git Commit

```bash
git add .
git commit -m "INV-602 Add Sale"
```

---

## Story Completion

✅ Sale added successfully.

✅ Repository Pattern followed.

✅ SQL Server integration completed.

✅ Ready for INV-603 – View All Sales.

# Story ID

## INV-603

### Title
View All Sales

### Priority
High

### Story Points
2

### Status
✅ Completed

---

## Tasks

- [x] Implement get_all_sales() in Sales Repository
- [x] Implement get_all_sales() in Sales Service
- [x] Create test_get_all_sales.py
- [x] Fetch all sales records from SQL Server
- [x] Display all sales records
- [x] Sort records by Sale ID
- [x] Test View All Sales functionality

---

## Files Updated

- sales_repo.py
- sales_service.py

## Files Created

- test_get_all_sales.py

---

## Database

### Table Used

Sales

---

## SQL Query Used

```sql
SELECT *
FROM Sales
ORDER BY sale_id;
```

---

## Test Result

```text
========================================
        ALL SALES
========================================

(1, 4, 2, 2, 55000.00, 110000.00, 2026-07-17)
```

*(Output may vary based on your database records.)*

---

## Git Commit

```bash
git add .
git commit -m "INV-603 View All Sales"
```

---

## Story Completion

✅ View All Sales implemented successfully.

✅ Repository Pattern followed.

✅ Sales records retrieved from SQL Server.

✅ Data displayed in ascending order by Sale ID.

✅ Ready for INV-604 – Search Sale.

# Story ID

## INV-604

### Title
Search Sale

### Priority
High

### Story Points
2

### Status
✅ Completed

---

## Tasks

- [x] Implement search_sale() in Sales Repository
- [x] Implement search_sale() in Sales Service
- [x] Create test_search_sale.py
- [x] Search Sale by Sale ID
- [x] Display Sale Details
- [x] Handle "Sale Not Found" scenario
- [x] Test Search Sale functionality

---

## Files Updated

- sales_repo.py
- sales_service.py

## Files Created

- test_search_sale.py

---

## Database

### Table Used

Sales

---

## SQL Query Used

```sql
SELECT *
FROM Sales
WHERE sale_id = ?;
```

---

## Test Result

### Existing Sale

```text
Enter Sale ID: 1

========== SEARCH SALE ==========

(1, 4, 2, 2, 55000.00, 110000.00, 2026-07-17)
```

### Non-Existing Sale

```text
Enter Sale ID: 100

========== SEARCH SALE ==========

Sale Not Found
```

---

## Git Commit

```bash
git add .
git commit -m "INV-604 Search Sale"
```

---

## Story Completion

✅ Search Sale implemented successfully.

✅ Repository Pattern followed.

✅ Sale searched using Sale ID.

✅ "Sale Not Found" handled correctly.

✅ Ready for INV-605 – Update Sale.

## INV-605

### Title
Update Sale

### Priority
High

### Story Points
2

### Status
✅ Completed

---

## Tasks

- [x] Implement update_sale() in Sales Repository
- [x] Implement update_sale() in Sales Service
- [x] Create test_update_sales.py
- [x] Update Sale using Sale ID
- [x] Update quantity
- [x] Update total amount
- [x] Handle "Sale Not Found" scenario
- [x] Test Update Sale functionality

---

## Files Updated

- sales_repo.py
- sales_service.py

## Files Created

- test_update_sales.py

---

## Database

### Table Used

Sales

---

## SQL Query Used

```sql
UPDATE Sales
SET quantity = ?,
    total_amount = ?
WHERE sale_id = ?;


---
## INV-606

### Title
Delete Sale

### Priority
High

### Story Points
2

### Status
✅ Completed

---

## Tasks

- [x] Implement delete_sale() in Sales Repository
- [x] Implement delete_sale() in Sales Service
- [x] Create test_delete_sale.py
- [x] Delete Sale using Sale ID
- [x] Handle "Sale Not Found" scenario
- [x] Test Delete Sale functionality

---

## Files Updated

- sales_repo.py
- sales_service.py

## Files Created

- test_delete_sale.py

---

## Database

### Table Used

Sales

---

## SQL Query Used

```sql
DELETE FROM Sales
WHERE sale_id = ?;

# Story ID

## INV-607

### Title
Sales Report

### Priority
High

### Story Points
3

### Status
✅ Completed

---

## Tasks

- [x] Implement sales_report() in Sales Repository
- [x] Implement sales_report() in Sales Service
- [x] Create test_sales_report.py
- [x] Fetch Total Sales Count
- [x] Calculate Total Revenue
- [x] Display Sales Report
- [x] Test Sales Report functionality

---

## Files Updated

- sales_repo.py
- sales_service.py

## Files Created

- test_sales_report.py

---

## Database

### Table Used

Sales

---

## SQL Query Used

```sql
SELECT
    COUNT(sale_id) AS total_sales,
    SUM(total_amount) AS total_revenue
FROM Sales;
```

---

## Test Result

```text
========== SALES REPORT ==========

Total Sales   : 5
Total Revenue : 450000.00
```

---

## Git Commit

```bash
git add .
git commit -m "INV-607 Sales Report"
```

---

## Story Completion

✅ Sales Report implemented successfully.

✅ Repository Pattern followed.

✅ Total Sales Count displayed.

✅ Total Revenue calculated successfully.

✅ Sales Report tested successfully.

✅ Ready for INV-608 – Sprint Testing & Documentation.
# Story ID

## INV-608

### Title
Sprint Testing & Documentation

### Priority
High

### Story Points
2

### Status
✅ Completed

---

## Tasks

- [x] Test Add Sale functionality
- [x] Test View All Sales functionality
- [x] Test Search Sale functionality
- [x] Test Update Sale functionality
- [x] Test Delete Sale functionality
- [x] Test Sales Report functionality
- [x] Verify SQL Server database records
- [x] Verify Repository Pattern implementation
- [x] Update Sprint 6 documentation
- [x] Complete Sprint 6 testing

---

## Files Verified

- create_sales_table.py
- sales_model.py
- sales_repo.py
- sales_service.py
- test_add_sale.py
- test_get_all_sales.py
- test_search_sale.py
- test_update_sales.py
- test_delete_sale.py
- test_sales_report.py
- sprint6.md

---

## Functional Testing

### Add Sale

```text
Status : PASS

Result : Sale Added Successfully
```

### View All Sales

```text
Status : PASS

Result : Sales displayed successfully.
```

### Search Sale

```text
Status : PASS

Result : Existing sale found.
Sale Not Found handled correctly.
```

### Update Sale

```text
Status : PASS

Result : Sale updated successfully.
```

### Delete Sale

```text
Status : PASS

Result : Sale deleted successfully.
Sale Not Found handled correctly.
```

### Sales Report

```text
Status : PASS

Result :
Total Sales displayed successfully.
Total Revenue calculated successfully.
```

---

## Database Verification

### Table Verified

Sales

### Verification

- Records inserted successfully
- Records updated successfully
- Records deleted successfully
- Search operation verified
- Sales Report generated correctly

---

## Repository Pattern Verification

Project Flow

```text
Test File
    │
    ▼
Sales Service
    │
    ▼
Sales Repository
    │
    ▼
SQL Server Database
```

Verified Operations

- Add Sale
- View All Sales
- Search Sale
- Update Sale
- Delete Sale
- Sales Report

Repository Pattern followed successfully.

---

## Sprint Summary

### Sprint Name

Sprint 6 – Sales Management

### Stories Completed

- ✅ INV-601 – Create Sales Table
- ✅ INV-602 – Add Sale
- ✅ INV-603 – View All Sales
- ✅ INV-604 – Search Sale
- ✅ INV-605 – Update Sale
- ✅ INV-606 – Delete Sale
- ✅ INV-607 – Sales Report
- ✅ INV-608 – Sprint Testing & Documentation

---

## Sprint Statistics

- Total Stories : 8
- Completed : 8
- Pending : 0
- Completion : 100%

---

## Git Commit

```bash
git add .
git commit -m "INV-608 Sprint 6 Testing and Documentation"
```

---

## Story Completion

✅ Sprint 6 testing completed successfully.

✅ All Sales module functionalities verified.

✅ SQL Server data validated.

✅ Repository Pattern verified.

✅ Sprint 6 documentation completed.

✅ Sprint 6 completed successfully.
# Story ID

## INV-1101

### Title

Dashboard Summary Report

### Priority

High

### Story Points

2

### Status

✅ Completed

---

## Story Description

As an Admin, I want to view an Inventory Dashboard Summary so that I can quickly monitor the overall status of products, customers, suppliers, and orders.

---

## Tasks

- [x] Create Dashboard Repository
- [x] Create Dashboard Service
- [x] Create Dashboard Summary Method
- [x] Display Product Count
- [x] Display Customer Count
- [x] Display Supplier Count
- [x] Display Order Count
- [x] Test Dashboard Summary

---

## Files Created

```
dashboard_repo.py
dashboard_service.py
test_dashboard_summary.py
```

---

## Repository Method

```
get_dashboard_summary()
```

---

## Service Method

```
get_dashboard_summary()
```

---

## SQL Queries

```sql
SELECT COUNT(*) FROM Product;

SELECT COUNT(*) FROM Customer;

SELECT COUNT(*) FROM Supplier;

SELECT COUNT(*) FROM Orders;
```

---

## Dashboard Output

```text
========== INVENTORY DASHBOARD ==========

Total Products   : 12
Total Customers  : 8
Total Suppliers  : 5
Total Orders     : 4
```

> *(The values depend on the data available in your database.)*

---

## Test Command

```bash
python test_dashboard_summary.py
```

---

## Git Commands

```bash
git add .
git commit -m "INV-1101 Dashboard Summary Report"
```

---

## Story Completion

- ✅ Dashboard Repository implemented
- ✅ Dashboard Service implemented
- ✅ Dashboard Summary generated
- ✅ Product count displayed
- ✅ Customer count displayed
- ✅ Supplier count displayed
- ✅ Order count displayed
- ✅ Repository Pattern followed
- ✅ SQL Server integration completed

---

# Sprint 11 Progress

| Story ID | Title | Status |
|----------|----------------------------|--------|
| INV-1101 | Dashboard Summary Report | ✅ Done |
| INV-1102 | Product Stock Summary | ⏳ Pending |
| INV-1103 | Customer Dashboard | ⏳ Pending |
| INV-1104 | Supplier Dashboard | ⏳ Pending |
| INV-1105 | Sales Dashboard | ⏳ Pending |
| INV-1106 | Purchase Dashboard | ⏳ Pending |
| INV-1107 | Inventory Dashboard Report | ⏳ Pending |
| INV-1108 | Testing & Documentation | ⏳ Pending |

## Sprint Progress

**Completed:** 1 / 8 Stories (**12.5%**)

**Remaining:** INV-1102 to INV-1108
# Story ID

## INV-1102

### Title

Product Stock Summary Dashboard

### Priority

High

### Story Points

2

### Status

✅ Completed

---

## Story Description

As an Admin, I want to view the total number of products and the total stock available in the inventory so that I can easily monitor inventory status.

---

## Tasks

- [x] Create Product Stock Summary Repository Method
- [x] Create Product Stock Summary Service Method
- [x] Create Product Stock Summary Test File
- [x] Display Total Products
- [x] Display Total Stock Quantity
- [x] Verify SQL Output

---

## Files Updated

```
dashboard_repo.py

dashboard_service.py
```

---

## Files Created

```
test_product_stock_summary.py
```

---

## Repository Method

```
get_product_stock_summary()
```

---

## Service Method

```
get_product_stock_summary()
```

---

## SQL Query

```sql
SELECT
    COUNT(*) AS TotalProducts,
    SUM(quantity) AS TotalStock
FROM Product;
```

---

## Test Command

```bash
python test_product_stock_summary.py
```

---

## Expected Output

```text
========== PRODUCT STOCK SUMMARY ==========

Total Products : 12
Total Stock    : 245
```

*(Values depend on the records available in the Product table.)*

---

## SQL Verification

```sql
SELECT
    COUNT(*) AS TotalProducts,
    SUM(quantity) AS TotalStock
FROM Product;
```

---

## Git Commands

```bash
git add .
git commit -m "INV-1102 Product Stock Summary Dashboard"
```

---

## Story Completion

- ✅ Product Stock Summary implemented
- ✅ Dashboard Repository updated
- ✅ Dashboard Service updated
- ✅ Product count displayed
- ✅ Total stock quantity displayed
- ✅ SQL Server verification completed
- ✅ Repository Pattern followed
- ✅ Testing completed

---

# Sprint 11 Progress

| Story ID | Title | Status |
|----------|-------------------------------------|--------|
| INV-1101 | Dashboard Summary Report | ✅ Done |
| INV-1102 | Product Stock Summary Dashboard | ✅ Done |
| INV-1103 | Customer Dashboard Summary | ⏳ Pending |
| INV-1104 | Supplier Dashboard Summary | ⏳ Pending |
| INV-1105 | Sales Dashboard Summary | ⏳ Pending |
| INV-1106 | Purchase Dashboard Summary | ⏳ Pending |
| INV-1107 | Inventory Dashboard Report | ⏳ Pending |
| INV-1108 | Testing & Documentation | ⏳ Pending |

## Sprint Progress

**Completed:** 2 / 8 Stories (**25%**)

**Remaining:** INV-1103 to INV-1108
# Story ID

## INV-1103

### Title

Customer Dashboard Summary

### Priority

High

### Story Points

2

### Status

✅ Completed

---

## Story Description

As an Admin, I want to view the total number of customers on the dashboard so that I can monitor customer records in the Inventory Management System.

---

## Tasks

- [x] Create Customer Dashboard Repository Method
- [x] Create Customer Dashboard Service Method
- [x] Create Customer Dashboard Test File
- [x] Display Total Customers
- [x] Verify SQL Output
- [x] Test Dashboard Summary

---

## Files Updated

```
dashboard_repo.py

dashboard_service.py
```

---

## Files Created

```
test_customer_dashboard.py
```

---

## Repository Method

```
get_customer_summary()
```

---

## Service Method

```
get_customer_summary()
```

---

## SQL Query

```sql
SELECT COUNT(*) AS TotalCustomers
FROM Customer;
```

---

## Test Command

```bash
python test_customer_dashboard.py
```

---

## Expected Output

```text
========== CUSTOMER DASHBOARD ==========

Total Customers : 8
```

> *(The total depends on the number of customer records in the database.)*

---

## SQL Verification

```sql
SELECT COUNT(*) AS TotalCustomers
FROM Customer;
```

---

## Git Commands

```bash
git add .
git commit -m "INV-1103 Customer Dashboard Summary"
```

---

## Story Completion

- ✅ Customer Dashboard Summary implemented
- ✅ Dashboard Repository updated
- ✅ Dashboard Service updated
- ✅ Customer count displayed
- ✅ SQL Server verification completed
- ✅ Repository Pattern followed
- ✅ Testing completed

---

# Sprint 11 Progress

| Story ID | Title | Status |
|----------|--------------------------------------|--------|
| INV-1101 | Dashboard Summary Report | ✅ Done |
| INV-1102 | Product Stock Summary Dashboard | ✅ Done |
| INV-1103 | Customer Dashboard Summary | ✅ Done |
| INV-1104 | Supplier Dashboard Summary | ⏳ Pending |
| INV-1105 | Sales Dashboard Summary | ⏳ Pending |
| INV-1106 | Purchase Dashboard Summary | ⏳ Pending |
| INV-1107 | Inventory Dashboard Report | ⏳ Pending |
| INV-1108 | Testing & Documentation | ⏳ Pending |

## Sprint Progress

**Completed:** 3 / 8 Stories (**37.5%**)
# Story ID

## INV-1104

### Title

Supplier Dashboard Summary

### Priority

High

### Story Points

2

### Status

⏳ In Progress

---

## Story Description

As an Admin, I want to view the total number of suppliers on the dashboard so that I can monitor supplier information.

---

## Tasks

- [ ] Create Supplier Dashboard Repository Method
- [ ] Create Supplier Dashboard Service Method
- [ ] Create Supplier Dashboard Test File
- [ ] Display Total Suppliers
- [ ] Verify SQL Output

---

## Files Updated

dashboard_repo.py

dashboard_service.py

---

## Files Created

test_supplier_dashboard.py

---

## Repository Method

get_supplier_summary()

---

## Service Method

get_supplier_summary()

---

## SQL Query

```sql
SELECT COUNT(*) AS TotalSuppliers
FROM Supplier;
```

---

## Test Command

```bash
python test_supplier_dashboard.py
```

---

## Expected Output

```text
========== SUPPLIER DASHBOARD ==========

Total Suppliers : 5
```

> *(The value depends on the records in the Supplier table.)*

---

## SQL Verification

```sql
SELECT COUNT(*) AS TotalSuppliers
FROM Supplier;
```

---

## Git Commands

```bash
git add .
git commit -m "INV-1104 Supplier Dashboard Summary"
```

---

## Story Completion

- [ ] Supplier Dashboard Repository implemented
- [ ] Supplier Dashboard Service implemented
- [ ] Supplier count displayed
- [ ] SQL Server verification completed
- [ ] Repository Pattern followed
- [ ] Testing completed

---

# Sprint 11 Progress

| Story ID | Title | Status |
|----------|--------------------------------------|--------|
| INV-1101 | Dashboard Summary Report | ✅ Done |
| INV-1102 | Product Stock Summary Dashboard | ✅ Done |
| INV-1103 | Customer Dashboard Summary | ✅ Done |
| INV-1104 | Supplier Dashboard Summary | ⏳ In Progress |
| INV-1105 | Sales Dashboard Summary | ⏳ Pending |
| INV-1106 | Purchase Dashboard Summary | ⏳ Pending |
| INV-1107 | Inventory Dashboard Report | ⏳ Pending |
| INV-1108 | Testing & Documentation | ⏳ Pending |

## Sprint Progress

Completed: **3 / 8 Stories (37.5%)**

Remaining: **INV-1104 to INV-1108**

# Story ID

## INV-1104

### Title

Supplier Dashboard Summary

### Priority

High

### Story Points

2

### Status

✅ Completed

---

## Story Description

As an Admin, I want to view the total number of suppliers on the dashboard so that I can monitor supplier information and inventory resources.

---

## Tasks

- [x] Create Supplier Dashboard Repository Method
- [x] Create Supplier Dashboard Service Method
- [x] Create Supplier Dashboard Test File
- [x] Display Total Suppliers
- [x] Verify SQL Output
- [x] Test Dashboard Summary

---

## Files Updated

```
dashboard_repo.py

dashboard_service.py
```

---

## Files Created

```
test_supplier_dashboard.py
```

---

## Repository Method

```
get_supplier_summary()
```

---

## Service Method

```
get_supplier_summary()
```

---

## SQL Query

```sql
SELECT COUNT(*) AS TotalSuppliers
FROM Supplier;
```

---

## Test Command

```bash
python test_supplier_dashboard.py
```

---

## Expected Output

```text
========== SUPPLIER DASHBOARD ==========

Total Suppliers : 5
```

> *(The value depends on the records available in the Supplier table.)*

---

## SQL Verification

```sql
SELECT COUNT(*) AS TotalSuppliers
FROM Supplier;
```

---

## Git Commands

```bash
git add .
git commit -m "INV-1104 Supplier Dashboard Summary"
```

---

## Story Completion

- ✅ Supplier Dashboard Summary implemented
- ✅ Dashboard Repository updated
- ✅ Dashboard Service updated
- ✅ Supplier count displayed
- ✅ SQL Server verification completed
- ✅ Repository Pattern followed
- ✅ Testing completed

---

# Sprint 11 Progress

| Story ID | Title | Status |
|----------|--------------------------------------|--------|
| INV-1101 | Dashboard Summary Report | ✅ Done |
| INV-1102 | Product Stock Summary Dashboard | ✅ Done |
| INV-1103 | Customer Dashboard Summary | ✅ Done |
| INV-1104 | Supplier Dashboard Summary | ✅ Done |
| INV-1105 | Sales Dashboard Summary | ⏳ Pending |
| INV-1106 | Purchase Dashboard Summary | ⏳ Pending |
| INV-1107 | Inventory Dashboard Report | ⏳ Pending |
| INV-1108 | Testing & Documentation | ⏳ Pending |

## Sprint Progress

**Completed:** 4 / 8 Stories (**50%**)

**Remaining:** INV-1105 to INV-1108

# Story ID

## INV-1105

### Title

Sales Dashboard Summary

### Priority

High

### Story Points

2

### Status

⏳ In Progress

---

## Story Description

As an Admin, I want to view the total number of sales and total sales amount on the dashboard so that I can monitor sales performance.

---

## Tasks

- [ ] Create Sales Dashboard Repository Method
- [ ] Create Sales Dashboard Service Method
- [ ] Create Sales Dashboard Test File
- [ ] Display Total Sales
- [ ] Display Total Sales Amount
- [ ] Verify SQL Output

---

## Files Updated

dashboard_repo.py

dashboard_service.py

---

## Files Created

test_sales_dashboard.py

---

## Repository Method

get_sales_summary()

---

## Service Method

get_sales_summary()

---

## Repository Code

```python
def get_sales_summary(self):

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    SELECT
        COUNT(*) AS TotalSales,
        SUM(total_amount) AS TotalSalesAmount
    FROM Sales
    """

    cursor.execute(query)

    summary = cursor.fetchone()

    cursor.close()
    conn.close()

    return summary
```

---

## Service Code

```python
def get_sales_summary(self):

    return self.repo.get_sales_summary()
```

---

## Test Program

```python
from dashboard_service import DashboardService

service = DashboardService()

summary = service.get_sales_summary()

print("\n========== SALES DASHBOARD ==========\n")

print("Total Sales        :", summary[0])
print("Total Sales Amount :", summary[1])
```

---

## SQL Query

```sql
SELECT
    COUNT(*) AS TotalSales,
    SUM(total_amount) AS TotalSalesAmount
FROM Sales;
```

---

## Test Command

```bash
python test_sales_dashboard.py
```

---

## Expected Output

```text
========== SALES DASHBOARD ==========

Total Sales        : 10
Total Sales Amount : 325000.00
```

> *(Values depend on the records in the Sales table.)*

---

## Git Commands

```bash
git add .
git commit -m "INV-1105 Sales Dashboard Summary"
```

---

## Story Completion

- [ ] Sales Dashboard Repository implemented
- [ ] Sales Dashboard Service implemented
- [ ] Sales count displayed
- [ ] Sales amount displayed
- [ ] SQL Server verification completed
- [ ] Repository Pattern followed
- [ ] Testing completed

---

# Sprint 11 Progress

| Story ID | Title | Status |
|----------|--------------------------------------|--------|
| INV-1101 | Dashboard Summary Report | ✅ Done |
| INV-1102 | Product Stock Summary Dashboard | ✅ Done |
| INV-1103 | Customer Dashboard Summary | ✅ Done |
| INV-1104 | Supplier Dashboard Summary | ✅ Done |
| INV-1105 | Sales Dashboard Summary | ⏳ In Progress |
| INV-1106 | Purchase Dashboard Summary | ⏳ Pending |
| INV-1107 | Inventory Dashboard Report | ⏳ Pending |
| INV-1108 | Testing & Documentation | ⏳ Pending |

## Sprint Progress

Completed: **4 / 8 Stories (50%)**

Remaining: **INV-1105 to INV-1108**
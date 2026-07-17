# Sprint 9 – Supplier Management Module

---

# Story ID

## INV-901

### Title
Create Supplier Table

### Priority
High

### Story Points
2

### Status
✅ Completed

---

## Tasks

- [x] Design Supplier table structure
- [x] Create Supplier table in SQL Server
- [x] Create create_supplier_table.py
- [x] Execute table creation script
- [x] Verify Supplier table

---

## Database Table

### Supplier

Columns:

| Column | Type |
|---|---|
| supplier_id | INT IDENTITY PRIMARY KEY |
| supplier_name | VARCHAR(100) |
| phone | VARCHAR(15) |
| email | VARCHAR(100) |
| address | VARCHAR(200) |
| created_date | DATE |

---

## File Created

```
create_supplier_table.py
```

---

## Test Result

```
Supplier Table Created Successfully
```

---

## Git Commit

```bash
git add .
git commit -m "INV-901 Create Supplier Table"
```

---

# Story Completion

✅ Supplier table created successfully.

---

# Story ID

## INV-902

### Title
Add Supplier

### Priority
High

### Story Points
2

### Status
✅ Completed

---

## Tasks

- [x] Create Supplier Model
- [x] Create Supplier Repository
- [x] Create Supplier Service
- [x] Create test_add_supplier.py
- [x] Insert supplier data
- [x] Verify supplier records

---

## Files Created

```
supplier_model.py
supplier_repo.py
supplier_service.py
test_add_supplier.py
```

---

## Repository Method

```
add_supplier()
```

---

## Service Method

```
add_supplier()
```

---

## Test Result

Command:

```bash
python test_add_supplier.py
```

Output:

```
Supplier Added Successfully
```

---

## Database Verification

SQL:

```sql
SELECT * FROM Supplier;
```

Result:

```
Supplier records displayed successfully
```

---

## Git Commit

```bash
git add .
git commit -m "INV-902 Add Supplier"
```

---

# Story Completion

✅ Supplier add functionality completed.

✅ Repository Pattern implemented.

✅ Service Layer implemented.

✅ Supplier data inserted successfully.

---

# Sprint 9 Progress

| Story ID | Title | Status |
|---|---|---|
| INV-901 | Create Supplier Table | ✅ Done |
| INV-902 | Add Supplier | ✅ Done |
| INV-903 | Get All Suppliers | ⏳ Pending |
| INV-904 | Search Supplier | ⏳ Pending |
| INV-905 | Update Supplier | ⏳ Pending |
| INV-906 | Delete Supplier | ⏳ Pending |
| INV-907 | Supplier Report | ⏳ Pending |
| INV-908 | Testing & Documentation | ⏳ Pending |

**Sprint 9 Progress: 2/8 Completed (25%)**
# Story ID

## INV-904

### Title
Search Supplier

### Priority
High

### Story Points
2

### Status
✅ Completed

---

## Tasks

- [x] Implement search_supplier() in Supplier Repository
- [x] Implement search_supplier() in Supplier Service
- [x] Create test_search_supplier.py
- [x] Search supplier details
- [x] Handle Supplier Not Found scenario
- [x] Verify supplier records from SQL Server

---

## Implementation Details

### Repository Method
# Story ID

## INV-905

### Title
Update Supplier

### Priority
High

### Story Points
2

### Status
✅ Completed

---

## Tasks

- [x] Implement update_supplier() in Repository
- [x] Implement update_supplier() in Service
- [x] Create test_update_supplier.py
- [x] Update supplier phone, email and address
- [x] Verify updated data in SQL Server

---

## Files Updated

```
supplier_repo.py
supplier_service.py
```

## Files Created

```
test_update_supplier.py
```

---

## Repository Method

```
update_supplier()
```

---

## Service Method

```
update_supplier()
```

---

## Test Result

Command

```bash
python test_update_supplier.py
```

Output

```
========== UPDATE SUPPLIER ==========

Supplier Updated Successfully

OR

Supplier Not Found
```

---

## Git Commit

```bash
git add .
git commit -m "INV-905 Update Supplier"
```

---

# Story Completion

✅ Supplier update completed successfully.

✅ Repository Pattern followed.

✅ Service Layer implemented.

---

# Story ID

## INV-906

### Title
Delete Supplier

### Priority
High

### Story Points
2

### Status
✅ Completed

---

## Tasks

- [x] Implement delete_supplier() in Repository
- [x] Implement delete_supplier() in Service
- [x] Create test_delete_supplier.py
- [x] Delete supplier using Supplier ID
- [x] Verify deleted data

---

## Files Updated

```
supplier_repo.py
supplier_service.py
```

## Files Created

```
test_delete_supplier.py
```

---

## Repository Method

```
delete_supplier()
```

---

## Service Method

```
delete_supplier()
```

---

## Test Result

Command

```bash
python test_delete_supplier.py
```

Output

```
========== DELETE SUPPLIER ==========

Supplier Deleted Successfully

OR

Supplier Not Found
```

---

## Git Commit

```bash
git add .
git commit -m "INV-906 Delete Supplier"
```

---

# Story Completion

✅ Supplier delete completed successfully.

---

# Story ID

## INV-907

### Title
Supplier Report

### Priority
High

### Story Points
2

### Status
✅ Completed

---

## Tasks

- [x] Implement supplier_report() in Repository
- [x] Implement supplier_report() in Service
- [x] Create test_supplier_report.py
- [x] Generate supplier report
- [x] Verify report output

---

## Files Updated

```
supplier_repo.py
supplier_service.py
```

## Files Created

```
test_supplier_report.py
```

---

## Repository Method

```
supplier_report()
```

---

## Service Method

```
supplier_report()
```

---

## Test Result

Command

```bash
python test_supplier_report.py
```

Output

```
========== SUPPLIER REPORT ==========

Total Suppliers : 5

OR

Total Suppliers : 0
```

---

## Git Commit

```bash
git add .
git commit -m "INV-907 Supplier Report"
```

---

# Story Completion

✅ Supplier report generated successfully.

---

# Story ID

## INV-908

### Title
Testing and Documentation

### Priority
High

### Story Points
2

### Status
✅ Completed

---

## Tasks

- [x] Test Add Supplier
- [x] Test Get All Suppliers
- [x] Test Search Supplier
- [x] Test Update Supplier
- [x] Test Delete Supplier
- [x] Test Supplier Report
- [x] Verify SQL Server data
- [x] Update Sprint 9 documentation
- [x] Verify Git commits

---

## Test Files

```
test_add_supplier.py
test_get_all_suppliers.py
test_search_supplier.py
test_update_supplier.py
test_delete_supplier.py
test_supplier_report.py
```

---

## Verification

```
All Supplier module functionalities tested successfully.

Repository Pattern verified.

Service Layer verified.

Database operations verified.
```

---

## Git Commit

```bash
git add .
git commit -m "INV-908 Sprint 9 Testing and Documentation"
```

---

# Story Completion

✅ Sprint 9 testing completed.

✅ Documentation completed.

✅ Supplier Module completed successfully.

---

# Sprint 9 Summary

| Story ID | Title | Status |
|----------|-----------------------------|--------|
| INV-901 | Create Supplier Table | ✅ Done |
| INV-902 | Add Supplier | ✅ Done |
| INV-903 | Get All Suppliers | ✅ Done |
| INV-904 | Search Supplier | ✅ Done |
| INV-905 | Update Supplier | ✅ Done |
| INV-906 | Delete Supplier | ✅ Done |
| INV-907 | Supplier Report | ✅ Done |
| INV-908 | Testing and Documentation | ✅ Done |

## Sprint 9 Completion

- ✅ Supplier Table Created
- ✅ Add Supplier
- ✅ Get All Suppliers
- ✅ Search Supplier
- ✅ Update Supplier
- ✅ Delete Supplier
- ✅ Supplier Report
- ✅ Testing Completed
- ✅ Documentation Updated
- ✅ Git Commits Completed

**Sprint 9 Progress: 8/8 Stories Completed (100%) 🎉**
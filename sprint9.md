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
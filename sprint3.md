# Sprint 3

## Sprint Goal
Implement Stock Management Module using Python, SQL Server, and Repository Pattern.

---

# Story ID

## INV-301

### Title
Create StockTransaction Table

### Priority
High

### Story Points
2

### Status
✅ Done

### Tasks

- [x] Create create_stock_table.py
- [x] Create StockTransaction table
- [x] Add Foreign Key with Product table
- [x] Verify table creation in SQL Server

### Result

StockTransaction table created successfully and verified.

# Story ID

## INV-302

### Title
Implement Stock In (Add Stock)

### Priority
High

### Story Points
3

### Status
🟡 In Progress

### Tasks

- [ ] Create stock_in() in repo.py
- [ ] Create stock_in() in service.py
- [ ] Create test_stock_in.py
- [ ] Update product quantity
- [ ] Verify stock update

## INV-303

### Title
Implement Stock Out (Remove Stock)

### Priority
High

### Story Points
3

### Status
🟡 In Progress

### Tasks

- [ ] Create stock_out() in repo.py
- [ ] Create stock_out() in service.py
- [ ] Create test_stock_out.py
- [ ] Verify quantity updated
- [ ] Commit to Git
# Sprint 3

## Sprint Goal

Implement Stock Management Module for the Inventory Management System.

---

# Story ID

## INV-301

### Title

Create StockTransaction Table

### Priority

High

### Story Points

2

### Status

✅ Completed

### Tasks

* [x] Create StockTransaction table
* [x] Add Primary Key
* [x] Add Foreign Key with Product table
* [x] Verify table creation
* [x] Commit to Git

---

# Story ID

## INV-302

### Title

Implement Stock In (Add Stock)

### Priority

High

### Story Points

3

### Status

✅ Completed

### Tasks

* [x] Create stock_in() in repo.py
* [x] Create stock_in() in service.py
* [x] Create test_stock_in.py
* [x] Update product quantity
* [x] Verify in SQL Server
* [x] Commit to Git

---

# Story ID

## INV-303

### Title

Implement Stock Out (Remove Stock)

### Priority

High

### Story Points

3

### Status

✅ Completed

### Tasks

* [x] Create stock_out() in repo.py
* [x] Create stock_out() in service.py
* [x] Create test_stock_out.py
* [x] Reduce product quantity
* [x] Verify in SQL Server
* [x] Commit to Git

---

# Story ID

## INV-304

### Title

Record Stock Transactions

### Priority

High

### Story Points

5

### Status

🟡 In Progress

### Tasks

* [ ] Create stock_model.py
* [ ] Create stock_repo.py
* [ ] Create stock_service.py
* [ ] Create test_stock_transaction.py
* [ ] Insert transaction into StockTransaction table
* [ ] Verify in SQL Server
* [ ] Commit to Git

---

Story ID : INV-305

Title : View Stock Transaction History

Priority : High

Story Points : 3

Status : ✅ Completed

Tasks

[x] Create get_all_transactions() in stock_repo.py
[x] Create get_all_transactions() in stock_service.py
[x] Create test_transaction_history.py
[x] Verify transaction history
[x] Commit to Git
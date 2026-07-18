# Story ID

## INV-1201

### Title

Create Users Table

### Priority

High

### Story Points

2

### Status

✅ Completed

---

## Story Description

As an Admin, I want to create a Users table so that user credentials and roles can be stored for authentication.

---

## Tasks

- [x] Create Users table
- [x] Add Primary Key
- [x] Add Username field
- [x] Add Password field
- [x] Add Role field
- [x] Add Created Date field
- [x] Verify table creation

---

## File Created

```
create_users_table.py
```

---

## SQL Query

```sql
CREATE TABLE Users
(
    user_id INT IDENTITY(1,1) PRIMARY KEY,
    username VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(100) NOT NULL,
    role VARCHAR(50) NOT NULL,
    created_date DATE NOT NULL
);
```

---

## Test Command

```bash
python create_users_table.py
```

---

## Verification

```sql
SELECT * FROM Users;
```

---

## Git Commands

```bash
git add .
git commit -m "INV-1201 Create Users Table"
```

---

## Story Completion

- ✅ Users table created
- ✅ Primary key configured
- ✅ Unique username constraint added
- ✅ SQL Server verification completed
# Sprint 12 Progress

| Story ID | Title | Status |
|----------|----------------------------------|--------|
| INV-1201 | Create Users Table | ✅ Done |
| INV-1202 | Add User Module | ✅ Done |
| INV-1203 | User Login Authentication | ✅ Done |
| INV-1204 | Search User | ✅ Done |
| INV-1205 | Update User | ✅ Done |
| INV-1206 | Delete User | ⏳ Pending |
| INV-1207 | User Report | ⏳ Pending |
| INV-1208 | Testing & Documentation | ⏳ Pending |

---

# Story ID

## INV-1204

### Title

Search User

### Priority

High

### Story Points

2

### Status

✅ Completed

---

## Story Description

As an Admin, I want to search a user by User ID so that I can quickly retrieve user details from the system.

---

## Tasks Completed

- [x] Search User Repository Method
- [x] Search User Service Method
- [x] Test Program Created
- [x] Search by User ID
- [x] Search by Username
- [x] SQL Verification Completed
- [x] Testing Completed

---

## Files Updated

```
user_repo.py

user_service.py
```

---

## Files Created

```
test_search_user.py
```

---

## Repository Methods

```
search_user()

search_user_by_username()
```

---

## Service Methods

```
search_user()

search_user_by_username()
```

---

## SQL Query

```sql
SELECT *
FROM Users
WHERE user_id = ?;
```

---

## Git Commit

```bash
git add .
git commit -m "INV-1204 Search User"
```

---

# Story ID

## INV-1205

### Title

Update User

### Priority

High

### Story Points

2

### Status

✅ Completed

---

## Story Description

As an Admin, I want to update existing user details so that user information remains accurate and up to date.

---

## Tasks Completed

- [x] Update User Repository Method
- [x] Update User Service Method
- [x] Create Update User Test Program
- [x] Update Username
- [x] Update Password
- [x] Update Role
- [x] Verify SQL Data
- [x] Testing Completed

---

## Files Updated

```
user_repo.py

user_service.py
```

---

## Files Created

```
test_update_user.py
```

---

## Repository Method

```
update_user()
```

---

## Service Method

```
update_user()
```

---

## SQL Query

```sql
UPDATE Users
SET
    username = ?,
    password = ?,
    role = ?
WHERE user_id = ?;
```

---

## Git Commit

```bash
git add .
git commit -m "INV-1205 Update User"
```

---

# Sprint Statistics

- **Sprint Number:** 12
- **Total Stories:** 8
- **Completed Stories:** 5
- **Pending Stories:** 3
- **Sprint Completion:** **62.5%**

---

## Sprint Progress

| Story ID | Title | Status |
|----------|----------------------------------|--------|
| INV-1201 | Create Users Table | ✅ Done |
| INV-1202 | Add User Module | ✅ Done |
| INV-1203 | User Login Authentication | ✅ Done |
| INV-1204 | Search User | ✅ Done |
| INV-1205 | Update User | ✅ Done |
| INV-1206 | Delete User | ⏳ Pending |
| INV-1207 | User Report | ⏳ Pending |
| INV-1208 | Testing & Documentation | ⏳ Pending |

## Sprint Status

**Completed:** **5 / 8 Stories (62.5%)**

**Remaining:** **INV-1206 to INV-1208**
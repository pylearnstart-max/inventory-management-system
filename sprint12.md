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
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

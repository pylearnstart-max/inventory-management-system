from db import get_connection

conn = get_connection()
cursor = conn.cursor()

cursor.execute("""
IF OBJECT_ID('Customer', 'U') IS NULL
BEGIN
    CREATE TABLE Customer
    (
        customer_id INT IDENTITY(1,1) PRIMARY KEY,

        customer_name VARCHAR(100) NOT NULL,

        phone VARCHAR(15),

        email VARCHAR(100),

        address VARCHAR(200),

        created_date DATE
    )
END
""")

conn.commit()

cursor.close()
conn.close()

print("Customer Table Created Successfully")
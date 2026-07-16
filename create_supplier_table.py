from db import get_connection

conn = get_connection()
cursor = conn.cursor()

cursor.execute("""
IF OBJECT_ID('Supplier', 'U') IS NULL
BEGIN
    CREATE TABLE Supplier
    (
        supplier_id INT IDENTITY(1,1) PRIMARY KEY,
        supplier_name VARCHAR(100) NOT NULL,
        contact_person VARCHAR(100),
        phone VARCHAR(20),
        email VARCHAR(100),
        address VARCHAR(255),
        created_date DATE
    )
END
""")

conn.commit()

cursor.close()
conn.close()

print("Supplier Table Created Successfully")
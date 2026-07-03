from db import get_connection

conn = get_connection()
cursor = conn.cursor()

cursor.execute("""
IF OBJECT_ID('Product', 'U') IS NULL
BEGIN
    CREATE TABLE Product
    (
        product_id INT IDENTITY(1,1) PRIMARY KEY,
        product_name VARCHAR(100) NOT NULL,
        category VARCHAR(100) NOT NULL,
        brand VARCHAR(100) NOT NULL,
        unit_price DECIMAL(10,2) NOT NULL,
        quantity INT NOT NULL,
        supplier_name VARCHAR(100) NOT NULL,
        created_date DATE NOT NULL
    )
END
""")

conn.commit()

cursor.close()
conn.close()

print("Product table created successfully.")
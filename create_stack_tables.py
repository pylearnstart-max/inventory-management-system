from db import get_connection

conn = get_connection()
cursor = conn.cursor()

cursor.execute("""
IF OBJECT_ID('StockTransaction', 'U') IS NULL
BEGIN
    CREATE TABLE StockTransaction
    (
        transaction_id INT IDENTITY(1,1) PRIMARY KEY,
        product_id INT NOT NULL,
        transaction_type VARCHAR(20) NOT NULL,
        quantity INT NOT NULL,
        transaction_date DATE NOT NULL,
        FOREIGN KEY (product_id) REFERENCES Product(product_id)
    )
END
""")

conn.commit()

cursor.close()
conn.close()

print("StockTransaction Table Created Successfully")
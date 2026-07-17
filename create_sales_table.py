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
from db import get_connection

conn = get_connection()
cursor = conn.cursor()

query = """
IF OBJECT_ID('Orders', 'U') IS NULL
BEGIN
    CREATE TABLE Orders
    (
        order_id INT IDENTITY(1,1) PRIMARY KEY,
        customer_id INT NOT NULL,
        product_id INT NOT NULL,
        quantity INT NOT NULL,
        unit_price DECIMAL(10,2) NOT NULL,
        total_amount DECIMAL(10,2) NOT NULL,
        order_date DATE NOT NULL,

        CONSTRAINT FK_Orders_Customer
            FOREIGN KEY (customer_id)
            REFERENCES Customer(customer_id),

        CONSTRAINT FK_Orders_Product
            FOREIGN KEY (product_id)
            REFERENCES Product(product_id)
    )

    PRINT 'Orders Table Created Successfully'
END
ELSE
BEGIN
    PRINT 'Orders Table Already Exists'
END
"""

cursor.execute(query)
conn.commit()

cursor.close()
conn.close()

print("Process Completed Successfully")
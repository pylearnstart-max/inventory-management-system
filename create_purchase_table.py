from db import get_connection

conn = get_connection()
cursor = conn.cursor()

query = """
IF OBJECT_ID('Purchase', 'U') IS NULL
BEGIN
    CREATE TABLE Purchase
    (
        purchase_id INT IDENTITY(1,1) PRIMARY KEY,
        product_id INT NOT NULL,
        supplier_id INT NOT NULL,
        quantity INT NOT NULL,
        unit_price DECIMAL(10,2) NOT NULL,
        total_amount DECIMAL(10,2) NOT NULL,
        purchase_date DATE NOT NULL,

        CONSTRAINT FK_Purchase_Product
            FOREIGN KEY (product_id)
            REFERENCES Product(product_id),

        CONSTRAINT FK_Purchase_Supplier
            FOREIGN KEY (supplier_id)
            REFERENCES Supplier(supplier_id)
    )

    PRINT 'Purchase Table Created Successfully'
END
ELSE
BEGIN
    PRINT 'Purchase Table Already Exists'
END
"""

cursor.execute(query)
conn.commit()

print("Process Completed Successfully")

cursor.close()
conn.close()
from db import get_connection

conn = get_connection()
cursor = conn.cursor()

query = """
CREATE TABLE CustomerOrder
(
    customer_order_id INT IDENTITY(1,1) PRIMARY KEY,

    customer_id INT NOT NULL,

    order_id INT NOT NULL,

    order_date DATE NOT NULL,

    CONSTRAINT FK_CustomerOrder_Customer
        FOREIGN KEY(customer_id)
        REFERENCES Customer(customer_id),

    CONSTRAINT FK_CustomerOrder_Order
        FOREIGN KEY(order_id)
        REFERENCES Orders(order_id)
)
"""

cursor.execute(query)

conn.commit()

print("CustomerOrder Table Created Successfully")

cursor.close()
conn.close()
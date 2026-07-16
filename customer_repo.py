from db import get_connection

class CustomerRepo:

    def add_customer(self, customer):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO Customer
            (
                customer_name,
                phone,
                email,
                address,
                created_date
            )
            VALUES
            (
                ?, ?, ?, ?, ?
            )
            """,
            (
                customer.customer_name,
                customer.phone,
                customer.email,
                customer.address,
                customer.created_date
            )
        )

        conn.commit()

        cursor.close()
        conn.close()

        print("Customer Added Successfully")

    def get_all_customers(self):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
          """
          SELECT *
          FROM Customer
          ORDER BY customer_id
          """
    )

        customers = cursor.fetchall()

        cursor.close()
        conn.close()

        return customers
from db import get_connection


class CustomerOrderRepo:


    def add_customer_order(self, customer_order):

        conn = get_connection()
        cursor = conn.cursor()

        query = """
        INSERT INTO CustomerOrder
        (
            customer_id,
            order_id,
            order_date
        )
        VALUES
        (
            ?, ?, ?
        )
        """

        cursor.execute(
            query,
            (
                customer_order.customer_id,
                customer_order.order_id,
                customer_order.order_date
            )
        )

        conn.commit()

        cursor.close()
        conn.close()

        print("Customer Order Added Successfully")


    def get_all_customer_orders(self):

        conn = get_connection()
        cursor = conn.cursor()

        query = """
        SELECT
            customer_order_id,
            customer_id,
            order_id,
            order_date
        FROM CustomerOrder
        ORDER BY customer_order_id
        """

        cursor.execute(query)

        customer_orders = cursor.fetchall()

        cursor.close()
        conn.close()

        return customer_orders
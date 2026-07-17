from db import get_connection


class OrderRepo:


    def add_order(self, order):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO Orders
            (
                customer_id,
                product_id,
                quantity,
                unit_price,
                total_amount,
                order_date
            )
            VALUES
            (
                ?, ?, ?, ?, ?, ?
            )
            """,
            (
                order.customer_id,
                order.product_id,
                order.quantity,
                order.unit_price,
                order.total_amount,
                order.order_date
            )
        )

        conn.commit()

        cursor.close()
        conn.close()

        print("Order Added Successfully")



    def get_all_orders(self):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM Orders
            ORDER BY order_id
            """
        )

        orders = cursor.fetchall()

        cursor.close()
        conn.close()

        return orders



    def search_order(self, order_id):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM Orders
            WHERE order_id = ?
            """,
            (order_id,)
        )

        order = cursor.fetchone()

        cursor.close()
        conn.close()

        return order
from db import get_connection


class SalesRepo:

    def add_sale(self, sale):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO Sales
            (
                product_id,
                customer_id,
                quantity,
                unit_price,
                total_amount,
                sale_date
            )
            VALUES
            (
                ?, ?, ?, ?, ?, ?
            )
            """,
            (
                sale.product_id,
                sale.customer_id,
                sale.quantity,
                sale.unit_price,
                sale.total_amount,
                sale.sale_date
            )
        )

        conn.commit()

        cursor.close()
        conn.close()

        print("Sale Added Successfully")


    def get_all_sales(self):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM Sales
            ORDER BY sale_id
            """
        )

        sales = cursor.fetchall()

        cursor.close()
        conn.close()

        return sales


    def search_sale(self, sale_id):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM Sales
            WHERE sale_id = ?
            """,
            (sale_id,)
        )

        sale = cursor.fetchone()

        cursor.close()
        conn.close()

        return sale


    def update_sale(self, sale_id, quantity, total_amount):

        conn = get_connection()
        cursor = conn.cursor()

        query = """
        UPDATE Sales
        SET quantity = ?,
            total_amount = ?
        WHERE sale_id = ?
        """

        cursor.execute(
            query,
            (
                quantity,
                total_amount,
                sale_id
            )
        )

        conn.commit()

        updated = cursor.rowcount

        cursor.close()
        conn.close()

        if updated > 0:
            return True

        return False


    def delete_sale(self, sale_id):

        conn = get_connection()
        cursor = conn.cursor()

        query = """
        DELETE FROM Sales
        WHERE sale_id = ?
        """

        cursor.execute(
            query,
            (sale_id,)
        )

        conn.commit()

        deleted = cursor.rowcount

        cursor.close()
        conn.close()

        if deleted > 0:
            return True

        return False
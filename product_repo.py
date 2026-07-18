from db import get_connection


class ProductRepo:


    def get_low_stock_products(self, limit):

        conn = get_connection()

        cursor = conn.cursor()


        query = """
        SELECT
            product_id,
            product_name,
            category,
            quantity
        FROM Product
        WHERE quantity <= ?
        ORDER BY quantity
        """


        cursor.execute(
            query,
            (limit,)
        )


        products = cursor.fetchall()


        cursor.close()
        conn.close()


        return products
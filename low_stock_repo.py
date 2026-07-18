from db import get_connection



class LowStockRepo:



    def get_low_stock_products(self):


        conn = get_connection()

        cursor = conn.cursor()



        query = """
        SELECT
            product_id,
            product_name,
            quantity
        FROM Product
        WHERE quantity <= 5
        ORDER BY quantity
        """



        cursor.execute(query)



        products = cursor.fetchall()



        cursor.close()

        conn.close()



        return products
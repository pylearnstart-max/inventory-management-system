from db import get_connection


class ProductRepo:


    def add_product(self, product):

        conn = get_connection()
        cursor = conn.cursor()

        query = """
        INSERT INTO Product
        (
            product_name,
            category,
            brand,
            unit_price,
            quantity,
            supplier_name,
            created_date
        )
        VALUES
        (
            ?, ?, ?, ?, ?, ?, ?
        )
        """

        cursor.execute(
            query,
            (
                product.product_name,
                product.category,
                product.brand,
                product.unit_price,
                product.quantity,
                product.supplier_name,
                product.created_date
            )
        )

        conn.commit()

        cursor.close()
        conn.close()

        print("Product Added Successfully")


    def get_all_products(self):

        conn = get_connection()
        cursor = conn.cursor()

        query = """
        SELECT *
        FROM Product
        ORDER BY product_id
        """

        cursor.execute(query)

        products = cursor.fetchall()

        cursor.close()
        conn.close()

        return products


    def search_product(self, product_id):

        conn = get_connection()
        cursor = conn.cursor()

        query = """
        SELECT *
        FROM Product
        WHERE product_id = ?
        """

        cursor.execute(
            query,
            (product_id,)
        )

        product = cursor.fetchone()

        cursor.close()
        conn.close()

        return product


    def update_product(self, product):

        conn = get_connection()
        cursor = conn.cursor()

        query = """
        UPDATE Product
        SET
            product_name = ?,
            category = ?,
            brand = ?,
            unit_price = ?,
            quantity = ?,
            supplier_name = ?
        WHERE product_id = ?
        """

        cursor.execute(
            query,
            (
                product.product_name,
                product.category,
                product.brand,
                product.unit_price,
                product.quantity,
                product.supplier_name,
                product.product_id
            )
        )

        conn.commit()

        updated = cursor.rowcount

        cursor.close()
        conn.close()

        return updated > 0


    def delete_product(self, product_id):

        conn = get_connection()
        cursor = conn.cursor()

        query = """
        DELETE FROM Product
        WHERE product_id = ?
        """

        cursor.execute(
            query,
            (product_id,)
        )

        conn.commit()

        deleted = cursor.rowcount

        cursor.close()
        conn.close()

        return deleted > 0


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


    def inventory_report(self):

        conn = get_connection()
        cursor = conn.cursor()

        query = """
        SELECT
            COUNT(product_id) AS TotalProducts,
            ISNULL(SUM(quantity), 0) AS TotalStock,
            ISNULL(SUM(quantity * unit_price), 0) AS StockValue
        FROM Product
        """

        cursor.execute(query)

        report = cursor.fetchone()

        cursor.close()
        conn.close()

        return report
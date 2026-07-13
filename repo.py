from db import get_connection


class ProductRepo:

    def add_product(self, product):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
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
            """,
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

        cursor.execute(
            """
            SELECT *
            FROM Product
            """
        )

        products = cursor.fetchall()

        cursor.close()
        conn.close()

        return products


    def get_product_by_id(self, product_id):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM Product
            WHERE product_id = ?
            """,
            (product_id,)
        )

        product = cursor.fetchone()

        cursor.close()
        conn.close()

        return product


    def update_product(self, product):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            UPDATE Product
            SET
                product_name = ?,
                category = ?,
                brand = ?,
                unit_price = ?,
                quantity = ?,
                supplier_name = ?,
                created_date = ?
            WHERE product_id = ?
            """,
            (
                product.product_name,
                product.category,
                product.brand,
                product.unit_price,
                product.quantity,
                product.supplier_name,
                product.created_date,
                product.product_id
            )
        )

        conn.commit()

        cursor.close()
        conn.close()

        print("Product Updated Successfully")


    def delete_product(self, product_id):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            DELETE FROM Product
            WHERE product_id = ?
            """,
            (product_id,)
        )

        conn.commit()

        cursor.close()
        conn.close()

        print("Product Deleted Successfully")


    def search_product_by_name(self, product_name):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM Product
            WHERE product_name LIKE ?
            """,
            ('%' + product_name + '%',)
        )

        products = cursor.fetchall()

        cursor.close()
        conn.close()

        return products


    def filter_products_by_category(self, category):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM Product
            WHERE category = ?
            """,
            (category,)
        )

        products = cursor.fetchall()

        cursor.close()
        conn.close()

        return products


    def filter_products_by_brand(self, brand):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM Product
            WHERE brand = ?
            """,
            (brand,)
        )

        products = cursor.fetchall()

        cursor.close()
        conn.close()

        return products


    def filter_products_by_price(self, min_price, max_price):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM Product
            WHERE unit_price BETWEEN ? AND ?
            """,
            (min_price, max_price)
        )

        products = cursor.fetchall()

        cursor.close()
        conn.close()

        return products


    def stock_in(self, product_id, quantity):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            UPDATE Product
            SET quantity = quantity + ?
            WHERE product_id = ?
            """,
            (quantity, product_id)
        )

        conn.commit()

        cursor.close()
        conn.close()

        print("Stock Added Successfully")

    def stock_out(self, product_id, quantity):

      conn = get_connection()
      cursor = conn.cursor()

      cursor.execute(
        """
        UPDATE Product
        SET quantity = quantity - ?
        WHERE product_id = ?
        """,
        (quantity, product_id)
    )

      conn.commit()

      cursor.close()
      conn.close()

    print("Stock Removed Successfully")
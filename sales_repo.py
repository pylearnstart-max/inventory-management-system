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
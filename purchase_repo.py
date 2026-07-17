from db import get_connection


class PurchaseRepo:

    def add_purchase(self, purchase):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO Purchase
            (
                product_id,
                supplier_id,
                quantity,
                unit_price,
                total_amount,
                purchase_date
            )
            VALUES
            (
                ?, ?, ?, ?, ?, ?
            )
            """,
            (
                purchase.product_id,
                purchase.supplier_id,
                purchase.quantity,
                purchase.unit_price,
                purchase.total_amount,
                purchase.purchase_date
            )
        )

        conn.commit()

        cursor.close()
        conn.close()

        print("Purchase Added Successfully")

    def get_all_purchases(self):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
        """
        SELECT *
        FROM Purchase
        ORDER BY purchase_id
        """
    )

        purchases = cursor.fetchall()

        cursor.close()
        conn.close()

        return purchases
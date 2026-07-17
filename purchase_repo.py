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


    def search_purchase(self, purchase_id):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM Purchase
            WHERE purchase_id = ?
            """,
            (purchase_id,)
        )

        purchase = cursor.fetchone()

        cursor.close()
        conn.close()

        return purchase


    def update_purchase(self, purchase_id, quantity, total_amount):

        conn = get_connection()
        cursor = conn.cursor()

        query = """
        UPDATE Purchase
        SET
            quantity = ?,
            total_amount = ?
        WHERE purchase_id = ?
        """

        cursor.execute(
            query,
            (
                quantity,
                total_amount,
                purchase_id
            )
        )

        conn.commit()

        updated = cursor.rowcount

        cursor.close()
        conn.close()

        if updated > 0:
            return True

        return False


    def delete_purchase(self, purchase_id):

        conn = get_connection()
        cursor = conn.cursor()

        query = """
        DELETE FROM Purchase
        WHERE purchase_id = ?
        """

        cursor.execute(
            query,
            (purchase_id,)
        )

        conn.commit()

        deleted = cursor.rowcount

        cursor.close()
        conn.close()

        if deleted > 0:
            return True

        return False


    def purchase_report(self):

        conn = get_connection()
        cursor = conn.cursor()

        query = """
        SELECT
            COUNT(purchase_id) AS total_purchases,
            SUM(total_amount) AS total_purchase_amount
        FROM Purchase
        """

        cursor.execute(query)

        report = cursor.fetchone()

        cursor.close()
        conn.close()

        return report
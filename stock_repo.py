from db import get_connection


class StockRepo:

    def add_transaction(self, transaction):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO StockTransaction
            (
                product_id,
                transaction_type,
                quantity,
                transaction_date
            )

            VALUES
            (
                ?, ?, ?, ?
            )
            """,
            (
                transaction.product_id,
                transaction.transaction_type,
                transaction.quantity,
                transaction.transaction_date
            )
        )

        conn.commit()

        cursor.close()
        conn.close()

        print("Transaction Saved Successfully")


    def get_all_transactions(self):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM StockTransaction
            ORDER BY transaction_id
            """
        )

        transactions = cursor.fetchall()

        cursor.close()
        conn.close()

        return transactions
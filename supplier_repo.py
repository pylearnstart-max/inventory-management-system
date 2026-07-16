from db import get_connection


class SupplierRepo:

    def add_supplier(self, supplier):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO Supplier
            (
                supplier_name,
                contact_person,
                phone,
                email,
                address,
                created_date
            )
            VALUES
            (
                ?, ?, ?, ?, ?, ?
            )
            """,
            (
                supplier.supplier_name,
                supplier.contact_person,
                supplier.phone,
                supplier.email,
                supplier.address,
                supplier.created_date
            )
        )

        conn.commit()

        cursor.close()
        conn.close()

        print("Supplier Added Successfully")


    def get_all_suppliers(self):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM Supplier
            ORDER BY supplier_id
            """
        )

        suppliers = cursor.fetchall()

        cursor.close()
        conn.close()

        return suppliers
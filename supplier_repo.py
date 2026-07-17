from db import get_connection


class SupplierRepo:


    def add_supplier(self, supplier):

        conn = get_connection()
        cursor = conn.cursor()

        query = """
        INSERT INTO Supplier
        (
            supplier_name,
            phone,
            email,
            address,
            created_date
        )
        VALUES
        (
            ?, ?, ?, ?, ?
        )
        """

        cursor.execute(
            query,
            (
                supplier.supplier_name,
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

        query = """
        SELECT *
        FROM Supplier
        ORDER BY supplier_id
        """

        cursor.execute(query)

        suppliers = cursor.fetchall()

        cursor.close()
        conn.close()

        return suppliers


    def search_supplier(self, supplier_id):

        conn = get_connection()
        cursor = conn.cursor()

        query = """
        SELECT *
        FROM Supplier
        WHERE supplier_id = ?
        """

        cursor.execute(
            query,
            (supplier_id,)
        )

        supplier = cursor.fetchone()

        cursor.close()
        conn.close()

        return supplier


    def search_supplier_by_name(self, supplier_name):

        conn = get_connection()
        cursor = conn.cursor()

        query = """
        SELECT *
        FROM Supplier
        WHERE supplier_name LIKE ?
        """

        cursor.execute(
            query,
            ('%' + supplier_name + '%',)
        )

        suppliers = cursor.fetchall()

        cursor.close()
        conn.close()

        return suppliers


    def update_supplier(
            self,
            supplier_id,
            phone,
            email,
            address
    ):

        conn = get_connection()
        cursor = conn.cursor()

        query = """
        UPDATE Supplier
        SET
            phone = ?,
            email = ?,
            address = ?
        WHERE supplier_id = ?
        """

        cursor.execute(
            query,
            (
                phone,
                email,
                address,
                supplier_id
            )
        )

        conn.commit()

        updated = cursor.rowcount

        cursor.close()
        conn.close()

        return updated > 0


    def delete_supplier(self, supplier_id):

        conn = get_connection()
        cursor = conn.cursor()

        query = """
        DELETE FROM Supplier
        WHERE supplier_id = ?
        """

        cursor.execute(
            query,
            (supplier_id,)
        )

        conn.commit()

        deleted = cursor.rowcount

        cursor.close()
        conn.close()

        return deleted > 0


    def supplier_report(self):

        conn = get_connection()
        cursor = conn.cursor()

        query = """
        SELECT
            COUNT(*) AS total_suppliers
        FROM Supplier
        """

        cursor.execute(query)

        report = cursor.fetchone()

        cursor.close()
        conn.close()

        return report
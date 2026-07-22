from db import get_connection

class CustomerRepo:

    def add_customer(self, customer):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO Customer
            (
                customer_name,
                phone,
                email,
                address,
                created_date
            )
            VALUES
            (
                ?, ?, ?, ?, ?
            )
            """,
            (
                customer.customer_name,
                customer.phone,
                customer.email,
                customer.address,
                customer.created_date
            )
        )

        conn.commit()

        cursor.close()
        conn.close()

        print("Customer Added Successfully")

    def get_all_customers(self):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
          """
          SELECT *
          FROM Customer
          ORDER BY customer_id
          """
    )

        customers = cursor.fetchall()

        cursor.close()
        conn.close()

        return customers

    def search_customer(self, customer_name):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
          """
          SELECT *
          FROM Customer
          WHERE customer_name LIKE ?
          """,
          ('%' + customer_name + '%',)
    )

        customers = cursor.fetchall()

        cursor.close()
        conn.close()

        return customers

    def update_customer(self, customer):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
          """
           UPDATE Customer
           SET
             customer_name = ?,
             phone = ?,
             email = ?,
             address = ?,
             created_date = ?
             WHERE customer_id = ?
            """,
            (
              customer.customer_name,
              customer.phone,
              customer.email,
              customer.address,
              customer.created_date,
              customer.customer_id
        )
    )

        conn.commit()

        cursor.close()
        conn.close()

    print("Customer Updated Successfully")

    def delete_customer(self, customer_id):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
          """
          DELETE FROM Customer
          WHERE customer_id = ?
          """,
        (customer_id,)
    )

        conn.commit()

        cursor.close()
        conn.close()

    print("Customer Deleted Successfully")

    def get_customer_report(self):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
          """
            SELECT
            customer_id,
            customer_name,
            phone,
            email,
            address,
            created_date
            FROM Customer
            ORDER BY customer_name
        """
    )

        customers = cursor.fetchall()

        cursor.close()
        conn.close()

        return customers

    # ==========================
# SEARCH CUSTOMER
# ==========================

def search_customer(self, keyword):

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    SELECT *
    FROM Customer
    WHERE customer_name LIKE ?
       OR phone LIKE ?
       OR email LIKE ?
       OR address LIKE ?
    """

    search = f"%{keyword}%"

    cursor.execute(
        query,
        (search, search, search, search)
    )

    customers = cursor.fetchall()

    conn.close()

    return customers
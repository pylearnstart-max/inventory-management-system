from db import get_connection


class DashboardRepo:


    def get_dashboard_summary(self):

        conn = get_connection()
        cursor = conn.cursor()

        dashboard = {}

        # Total Products
        cursor.execute("SELECT COUNT(*) FROM Product")
        dashboard["total_products"] = cursor.fetchone()[0]

        # Total Customers
        cursor.execute("SELECT COUNT(*) FROM Customer")
        dashboard["total_customers"] = cursor.fetchone()[0]

        # Total Suppliers
        cursor.execute("SELECT COUNT(*) FROM Supplier")
        dashboard["total_suppliers"] = cursor.fetchone()[0]

        # Total Orders
        cursor.execute("SELECT COUNT(*) FROM Orders")
        dashboard["total_orders"] = cursor.fetchone()[0]

        # Total Stock
        cursor.execute("SELECT ISNULL(SUM(quantity),0) FROM Product")
        dashboard["total_stock"] = cursor.fetchone()[0]

        # Total Sales
        cursor.execute("SELECT COUNT(*) FROM Sales")
        dashboard["total_sales"] = cursor.fetchone()[0]

        cursor.execute(
            "SELECT ISNULL(SUM(total_amount),0) FROM Sales"
        )
        dashboard["total_sales_amount"] = cursor.fetchone()[0]

        # Total Purchase
        cursor.execute("SELECT COUNT(*) FROM Purchase")
        dashboard["total_purchase"] = cursor.fetchone()[0]

        cursor.execute(
            "SELECT ISNULL(SUM(total_amount),0) FROM Purchase"
        )
        dashboard["total_purchase_amount"] = cursor.fetchone()[0]

        # Stock Value
        cursor.execute("""
        SELECT
        ISNULL(SUM(unit_price * quantity),0)
        FROM Product
        """)
        dashboard["stock_value"] = cursor.fetchone()[0]

        cursor.close()
        conn.close()

        return dashboard


    def get_product_stock_summary(self):

        conn = get_connection()
        cursor = conn.cursor()

        query = """
        SELECT
            COUNT(*) AS TotalProducts,
            ISNULL(SUM(quantity),0) AS TotalStock
        FROM Product
        """

        cursor.execute(query)

        summary = cursor.fetchone()

        cursor.close()
        conn.close()

        return summary


    def get_customer_summary(self):

        conn = get_connection()
        cursor = conn.cursor()

        query = """
        SELECT COUNT(*)
        FROM Customer
        """

        cursor.execute(query)

        summary = cursor.fetchone()

        cursor.close()
        conn.close()

        return summary


    def get_supplier_summary(self):

        conn = get_connection()
        cursor = conn.cursor()

        query = """
        SELECT COUNT(*)
        FROM Supplier
        """

        cursor.execute(query)

        summary = cursor.fetchone()

        cursor.close()
        conn.close()

        return summary


    def get_sales_summary(self):

        conn = get_connection()
        cursor = conn.cursor()

        query = """
        SELECT
            COUNT(*) AS TotalSales,
            ISNULL(SUM(total_amount),0) AS TotalSalesAmount
        FROM Sales
        """

        cursor.execute(query)

        summary = cursor.fetchone()

        cursor.close()
        conn.close()

        return summary


    def get_purchase_summary(self):

        conn = get_connection()
        cursor = conn.cursor()

        query = """
        SELECT
            COUNT(*) AS TotalPurchase,
            ISNULL(SUM(total_amount),0) AS TotalPurchaseAmount
        FROM Purchase
        """

        cursor.execute(query)

        summary = cursor.fetchone()

        cursor.close()
        conn.close()

        return summary


    def get_stock_value(self):

        conn = get_connection()
        cursor = conn.cursor()

        query = """
        SELECT
        ISNULL(SUM(unit_price * quantity),0)
        FROM Product
        """

        cursor.execute(query)

        value = cursor.fetchone()[0]

        cursor.close()
        conn.close()

        return value


    def get_sales_report(self):

        conn = get_connection()
        cursor = conn.cursor()

        query = """
        SELECT
            sale_id,
            product_id,
            customer_id,
            quantity,
            unit_price,
            total_amount,
            sale_date
        FROM Sales
        ORDER BY sale_date DESC
        """

        cursor.execute(query)

        sales = cursor.fetchall()

        cursor.close()
        conn.close()

        return sales
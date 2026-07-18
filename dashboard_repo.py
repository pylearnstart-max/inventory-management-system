from db import get_connection


class DashboardRepo:


    def get_dashboard_summary(self):

        conn = get_connection()
        cursor = conn.cursor()

        dashboard = {}

        # Total Products
        cursor.execute("SELECT COUNT(*) FROM Product")
        dashboard["products"] = cursor.fetchone()[0]

        # Total Customers
        cursor.execute("SELECT COUNT(*) FROM Customer")
        dashboard["customers"] = cursor.fetchone()[0]

        # Total Suppliers
        cursor.execute("SELECT COUNT(*) FROM Supplier")
        dashboard["suppliers"] = cursor.fetchone()[0]

        # Total Orders
        cursor.execute("SELECT COUNT(*) FROM Orders")
        dashboard["orders"] = cursor.fetchone()[0]

        cursor.close()
        conn.close()

        return dashboard

    def get_product_stock_summary(self):

        conn = get_connection()
        cursor = conn.cursor()

        query = """
        SELECT
        COUNT(*) AS TotalProducts,
        SUM(quantity) AS TotalStock
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
        SELECT COUNT(*) AS TotalCustomers
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
        SELECT COUNT(*) AS TotalSuppliers
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
        ISNULL(SUM(total_amount), 0) AS TotalSalesAmount
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
        COUNT(*) AS TotalPurchases,
        ISNULL(SUM(total_amount), 0) AS TotalPurchaseAmount
        FROM Purchase
        """

        cursor.execute(query)

        summary = cursor.fetchone()

        cursor.close()
        conn.close()

        return summary
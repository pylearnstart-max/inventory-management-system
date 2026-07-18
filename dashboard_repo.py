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
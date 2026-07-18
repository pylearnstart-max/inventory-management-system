from dashboard_repo import DashboardRepo


class DashboardService:


    def __init__(self):

        self.repo = DashboardRepo()



    def get_dashboard_summary(self):


        dashboard = {}


        # Basic Dashboard

        summary = self.repo.get_dashboard_summary()


        dashboard["total_products"] = summary["products"]

        dashboard["total_customers"] = summary["customers"]

        dashboard["total_suppliers"] = summary["suppliers"]

        dashboard["total_orders"] = summary["orders"]



        # Stock Summary

        stock = self.repo.get_product_stock_summary()


        dashboard["total_stock"] = stock[1]



        # Sales Summary

        sales = self.repo.get_sales_summary()


        dashboard["total_sales"] = sales[0]

        dashboard["total_sales_amount"] = sales[1]



        # Purchase Summary

        purchase = self.repo.get_purchase_summary()


        dashboard["total_purchase"] = purchase[0]

        dashboard["total_purchase_amount"] = purchase[1]



        # Stock Value

        dashboard["stock_value"] = self.repo.get_stock_value()



        return dashboard




    def get_product_stock_summary(self):

        return self.repo.get_product_stock_summary()



    def get_customer_summary(self):

        return self.repo.get_customer_summary()



    def get_supplier_summary(self):

        return self.repo.get_supplier_summary()



    def get_sales_summary(self):

        return self.repo.get_sales_summary()



    def get_purchase_summary(self):

        return self.repo.get_purchase_summary()
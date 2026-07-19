
from dashboard_repo import DashboardRepo


class DashboardService:


    def __init__(self):

        self.repo = DashboardRepo()


    def get_dashboard_summary(self):

        return self.repo.get_dashboard_summary()


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


    def get_stock_value(self):

        return self.repo.get_stock_value()


    def get_sales_report(self):

        return self.repo.get_sales_report()
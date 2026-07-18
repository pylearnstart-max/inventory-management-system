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
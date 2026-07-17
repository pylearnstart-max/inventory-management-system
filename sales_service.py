from sales_repo import SalesRepo


class SalesService:

    def __init__(self):
        self.repo = SalesRepo()

    def add_sale(self, sale):
        self.repo.add_sale(sale)
    
    def get_all_sales(self):

        return self.repo.get_all_sales()
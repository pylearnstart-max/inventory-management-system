from low_stock_repo import LowStockRepo



class LowStockService:



    def __init__(self):

        self.repo = LowStockRepo()



    def get_low_stock_products(self):


        return self.repo.get_low_stock_products()
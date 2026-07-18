from product_repo import ProductRepo



class ProductService:


    def __init__(self):

        self.repo = ProductRepo()



    def get_low_stock_products(self, limit):

        return self.repo.get_low_stock_products(limit)
from repo import ProductRepo
from validation import ProductValidator


class ProductService:

    def __init__(self):
        self.repo = ProductRepo()

    def add_product(self, product):
        ProductValidator.validate(product)
        self.repo.add_product(product)

    def get_all_products(self):
        return self.repo.get_all_products()

    def get_product_by_id(self, product_id):
        return self.repo.get_product_by_id(product_id)

    def update_product(self, product):
        ProductValidator.validate(product)
        self.repo.update_product(product)

    def delete_product(self, product_id):
        self.repo.delete_product(product_id)
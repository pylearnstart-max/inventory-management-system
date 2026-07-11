from repo import ProductRepo
from validation import ProductValidator
from logger import logger


class ProductService:

    def __init__(self):
        self.repo = ProductRepo()

    def add_product(self, product):
        ProductValidator.validate(product)
        self.repo.add_product(product)
        logger.info(f"Product Added : {product.product_name}")

    def get_all_products(self):
        return self.repo.get_all_products()

    def get_product_by_id(self, product_id):
        return self.repo.get_product_by_id(product_id)

    def update_product(self, product):
        ProductValidator.validate(product)
        self.repo.update_product(product)
        logger.info(f"Product Updated : {product.product_name}")

    def delete_product(self, product_id):
        self.repo.delete_product(product_id)
        logger.info(f"Product Deleted : {product_id}")

    def search_product_by_name(self, product_name):
        return self.repo.search_product_by_name(product_name)
    
    def filter_products_by_category(self, category):
        return self.repo.filter_products_by_category(category)
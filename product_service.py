from product_repo import ProductRepo


class ProductService:


    def __init__(self, repo=None):

        if repo is None:
            self.repo = ProductRepo()
        else:
            self.repo = repo


    def add_product(self, product):

        return self.repo.add_product(product)


    def get_all_products(self):

        return self.repo.get_all_products()


    def search_product(self, product_id):

        product = self.repo.search_product(product_id)

        if product:

            return product

        return "Product Not Found"


    def update_product(self, product):

        result = self.repo.update_product(product)

        if result:

            return "Product Updated Successfully"

        return "Product Not Found"


    def delete_product(self, product_id):

        result = self.repo.delete_product(product_id)

        if result:

            return "Product Deleted Successfully"

        return "Product Not Found"


    def get_low_stock_products(self, limit):

        return self.repo.get_low_stock_products(limit)


    def inventory_report(self):

        report = self.repo.inventory_report()

        if report:

            return report

        return (0, 0, 0)
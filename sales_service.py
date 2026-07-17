from sales_repo import SalesRepo


class SalesService:

    def __init__(self, repo):

        self.repo = repo


    def add_sale(self, sale):

        return self.repo.add_sale(sale)


    def get_all_sales(self):

        return self.repo.get_all_sales()


    def search_sale(self, sale_id):

        sale = self.repo.search_sale(sale_id)

        if sale:
            return sale

        return "Sale Not Found"


    def update_sale(self, sale_id, quantity, total_amount):

        result = self.repo.update_sale(
            sale_id,
            quantity,
            total_amount
        )

        if result:
            return "Sale Updated Successfully"

        return "Sale Not Found"

    def delete_sale(self, sale_id):

        result = self.repo.delete_sale(sale_id)

        if result:
            return "Sale Deleted Successfully"

        return "Sale Not Found"
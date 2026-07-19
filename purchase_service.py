from purchase_repo import PurchaseRepo


class PurchaseService:

    def __init__(self, repo=None):

        if repo is None:
            self.repo = PurchaseRepo()
        else:
            self.repo = repo


    def add_purchase(self, purchase):

        return self.repo.add_purchase(purchase)


    def get_all_purchases(self):

        return self.repo.get_all_purchases()


    def search_purchase(self, purchase_id):

        purchase = self.repo.search_purchase(purchase_id)

        if purchase:

            return purchase

        return "Purchase Not Found"


    def update_purchase(self, purchase_id, quantity, total_amount):

        result = self.repo.update_purchase(
            purchase_id,
            quantity,
            total_amount
        )

        if result:

            return "Purchase Updated Successfully"

        return "Purchase Not Found"


    def delete_purchase(self, purchase_id):

        result = self.repo.delete_purchase(purchase_id)

        if result:

            return "Purchase Deleted Successfully"

        return "Purchase Not Found"


    def purchase_report(self):

        report = self.repo.purchase_report()

        if report:

            return report

        return (0, 0)
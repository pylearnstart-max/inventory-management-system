from purchase_repo import PurchaseRepo


class PurchaseService:

    def __init__(self, repo=None):

        if repo is None:
            repo = PurchaseRepo()

        self.repo = repo


    def add_purchase(self, purchase):

        return self.repo.add_purchase(purchase)


    def get_all_purchases(self):

        return self.repo.get_all_purchases()


    def search_purchase(self, purchase_id):

        return self.repo.search_purchase(purchase_id)


    def update_purchase(self, purchase_id, quantity, total_amount):

        return self.repo.update_purchase(
            purchase_id,
            quantity,
            total_amount
        )
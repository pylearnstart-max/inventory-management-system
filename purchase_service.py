from purchase_repo import PurchaseRepo


class PurchaseService:

    def __init__(self, repo):
        self.repo = repo

    def add_purchase(self, purchase):
        return self.repo.add_purchase(purchase)
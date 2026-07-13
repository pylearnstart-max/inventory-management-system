from stock_repo import StockRepo


class StockService:

    def __init__(self):
        self.repo = StockRepo()

    def add_transaction(self, transaction):
        self.repo.add_transaction(transaction)

    def get_all_transactions(self):
        return self.repo.get_all_transactions()
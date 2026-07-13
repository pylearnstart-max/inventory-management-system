from stock_repo import StockRepo


class StockService:

    def __init__(self):

        self.repo = StockRepo()

    def add_transaction(self, transaction):

        self.repo.add_transaction(transaction)
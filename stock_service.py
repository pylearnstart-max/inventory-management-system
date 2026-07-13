from stock_repo import StockRepo


class StockService:

    def __init__(self):
        self.repo = StockRepo()

    def add_transaction(self, transaction):
        self.repo.add_transaction(transaction)

    def get_all_transactions(self):
        return self.repo.get_all_transactions()

    def get_low_stock_products(self, limit):
        return self.repo.get_low_stock_products(limit)
    def get_inventory_dashboard(self):
        return self.repo.get_inventory_dashboard()
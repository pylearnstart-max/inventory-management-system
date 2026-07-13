from datetime import date


class StockTransaction:

    def __init__(
        self,
        product_id,
        transaction_type,
        quantity,
        transaction_date=None
    ):

        self.product_id = product_id
        self.transaction_type = transaction_type
        self.quantity = quantity

        if transaction_date is None:
            self.transaction_date = date.today()
        else:
            self.transaction_date = transaction_date
from datetime import date

class Sale:

    def __init__(
        self,
        product_id,
        customer_id,
        quantity,
        unit_price,
        total_amount,
        sale_date,
        sale_id=None
    ):
        self.sale_id = sale_id
        self.product_id = product_id
        self.customer_id = customer_id
        self.quantity = quantity
        self.unit_price = unit_price
        self.total_amount = total_amount
        self.sale_date = sale_date
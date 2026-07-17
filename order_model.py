class Order:

    def __init__(
        self,
        customer_id,
        product_id,
        quantity,
        unit_price,
        total_amount,
        order_date
    ):

        self.customer_id = customer_id
        self.product_id = product_id
        self.quantity = quantity
        self.unit_price = unit_price
        self.total_amount = total_amount
        self.order_date = order_date
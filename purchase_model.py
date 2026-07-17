class Purchase:

    def __init__(
        self,
        product_id,
        supplier_id,
        quantity,
        unit_price,
        total_amount,
        purchase_date
    ):
        self.product_id = product_id
        self.supplier_id = supplier_id
        self.quantity = quantity
        self.unit_price = unit_price
        self.total_amount = total_amount
        self.purchase_date = purchase_date
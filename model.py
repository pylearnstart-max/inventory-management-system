class Product:

    def __init__(
            self,
            product_id,
            product_name,
            category,
            brand,
            unit_price,
            quantity,
            supplier_name,
            created_date):

        self.product_id = product_id
        self.product_name = product_name
        self.category = category
        self.brand = brand
        self.unit_price = unit_price
        self.quantity = quantity
        self.supplier_name = supplier_name
        self.created_date = created_date
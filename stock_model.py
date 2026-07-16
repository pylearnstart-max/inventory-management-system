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
class Supplier:

    def __init__(
        self,
        supplier_id,
        supplier_name,
        contact_person,
        phone,
        email,
        address,
        created_date
    ):
        self.supplier_id = supplier_id
        self.supplier_name = supplier_name
        self.contact_person = contact_person
        self.phone = phone
        self.email = email
        self.address = address
        self.created_date = created_date
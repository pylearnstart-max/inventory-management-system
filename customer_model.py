class Customer:

    def __init__(
        self,
        customer_name,
        phone,
        email,
        address,
        created_date,
        customer_id=None
    ):
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.phone = phone
        self.email = email
        self.address = address
        self.created_date = created_date
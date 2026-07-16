from datetime import date

class Customer:

    def __init__(
        self,
        customer_name,
        phone,
        email,
        address,
        created_date
    ):

        self.customer_name = customer_name
        self.phone = phone
        self.email = email
        self.address = address
        self.created_date = created_date

    from datetime import date



    def __init__(
        self,
        customer_id,
        customer_name,
        phone,
        email,
        address,
        created_date
    ):
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.phone = phone
        self.email = email
        self.address = address
        self.created_date = created_date
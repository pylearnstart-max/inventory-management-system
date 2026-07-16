from customer_repo import CustomerRepo

class CustomerService:

    def __init__(self):
        self.repo = CustomerRepo()

    def add_customer(self, customer):
        self.repo.add_customer(customer)
from customer_repo import CustomerRepo

class CustomerService:

    def __init__(self):
        self.repo = CustomerRepo()

    def add_customer(self, customer):
        self.repo.add_customer(customer)

    def get_all_customers(self):

        return self.repo.get_all_customers()

    def search_customer(self, customer_name):

        return self.repo.search_customer(customer_name)
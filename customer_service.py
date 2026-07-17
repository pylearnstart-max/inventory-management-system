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

    def update_customer(self, customer):

        self.repo.update_customer(customer)
    
    def delete_customer(self, customer_id):

        self.repo.delete_customer(customer_id)
    
    def get_customer_report(self):

        return self.repo.get_customer_report()
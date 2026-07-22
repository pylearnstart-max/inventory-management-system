class CustomerService:

    def __init__(self, repo):

        self.repo = repo


    def add_customer(self, customer):

        self.repo.add_customer(customer)


    def get_all_customers(self):

        return self.repo.get_all_customers()


    def get_customer_by_id(self, customer_id):

        return self.repo.get_customer_by_id(customer_id)


    def update_customer(self, customer):

        self.repo.update_customer(customer)


    def delete_customer(self, customer_id):

        self.repo.delete_customer(customer_id)

    def search_customer(self, keyword):

        return self.repo.search_customer(keyword)
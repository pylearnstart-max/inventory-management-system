from customer_order_repo import CustomerOrderRepo


class CustomerOrderService:

    def __init__(self, repo=None):

        if repo is None:
            repo = CustomerOrderRepo()

        self.repo = repo


    def add_customer_order(self, customer_order):

        return self.repo.add_customer_order(customer_order)
    
    def get_all_customer_orders(self):

        return self.repo.get_all_customer_orders()
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


    def search_customer_order(self, customer_order_id):

        return self.repo.search_customer_order(customer_order_id)


    def update_customer_order(
            self,
            customer_order_id,
            customer_id,
            order_id,
            order_date
    ):

        return self.repo.update_customer_order(
            customer_order_id,
            customer_id,
            order_id,
            order_date
        )


    def delete_customer_order(self, customer_order_id):

        return self.repo.delete_customer_order(
            customer_order_id
        )


    def customer_order_report(self):

        return self.repo.customer_order_report()
from order_repo import OrderRepo


class OrderService:


    def __init__(self, repo=None):

        if repo is None:
            repo = OrderRepo()

        self.repo = repo



    def add_order(self, order):

        return self.repo.add_order(order)



    def get_all_orders(self):

        return self.repo.get_all_orders()
    
    def search_order(self, order_id):

        return self.repo.search_order(order_id)
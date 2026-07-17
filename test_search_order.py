from order_repo import OrderRepo
from order_service import OrderService


repo = OrderRepo()
service = OrderService(repo)


order_id = int(input("Enter Order ID: "))


order = service.search_order(order_id)


print("\n========== SEARCH ORDER ==========\n")


if order:

    print(order)

else:

    print("Order Not Found")
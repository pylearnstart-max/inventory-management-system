from order_repo import OrderRepo
from order_service import OrderService


repo = OrderRepo()
service = OrderService(repo)


orders = service.get_all_orders()


print("\n========== ORDER LIST ==========\n")


if orders:

    for order in orders:
        print(order)

else:

    print("No Orders Found")
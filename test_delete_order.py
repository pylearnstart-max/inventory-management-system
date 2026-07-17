from order_repo import OrderRepo
from order_service import OrderService


repo = OrderRepo()
service = OrderService(repo)


order_id = int(input("Enter Order ID: "))


result = service.delete_order(order_id)


print("\n========== DELETE ORDER ==========\n")


if result:

    print("Order Deleted Successfully")

else:

    print("Order Not Found")
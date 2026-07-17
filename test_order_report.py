from order_repo import OrderRepo
from order_service import OrderService


repo = OrderRepo()
service = OrderService(repo)


report = service.order_report()


print("\n========== ORDER REPORT ==========\n")


print("Total Orders       :", report[0])
print("Total Order Amount :", report[1])
from order_repo import OrderRepo
from order_service import OrderService


repo = OrderRepo()
service = OrderService(repo)


order_id = int(input("Enter Order ID: "))
quantity = int(input("Enter New Quantity: "))
total_amount = float(input("Enter New Total Amount: "))


result = service.update_order(
    order_id,
    quantity,
    total_amount
)


print("\n========== UPDATE ORDER ==========\n")


if result:
    print("Order Updated Successfully")

else:
    print("Order Not Found")
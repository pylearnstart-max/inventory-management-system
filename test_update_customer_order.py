from datetime import date
from customer_order_service import CustomerOrderService

service = CustomerOrderService()

customer_order_id = int(input("Enter Customer Order ID: "))
customer_id = int(input("Enter New Customer ID: "))
order_id = int(input("Enter New Order ID: "))

result = service.update_customer_order(
    customer_order_id,
    customer_id,
    order_id,
    date.today()
)

print("\n========== UPDATE CUSTOMER ORDER ==========\n")

if result:
    print("Customer Order Updated Successfully")
else:
    print("Customer Order Not Found")
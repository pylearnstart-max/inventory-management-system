from datetime import date
from customer_order_model import CustomerOrder
from customer_order_service import CustomerOrderService

service = CustomerOrderService()

customer_order = CustomerOrder(
    2,          # Existing customer_id
    4,          # Replace 1 with the actual order_id from Orders table
    date.today()
)

service.add_customer_order(customer_order)
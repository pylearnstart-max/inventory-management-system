from order_model import Order
from order_repo import OrderRepo
from order_service import OrderService


repo = OrderRepo()
service = OrderService(repo)


order = Order(
    customer_id=2,     # existing customer id
    product_id=4,      # existing product id
    quantity=2,
    unit_price=55000,
    total_amount=110000,
    order_date="2026-07-17"
)


service.add_order(order)
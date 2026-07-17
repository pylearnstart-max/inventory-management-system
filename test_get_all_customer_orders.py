from customer_order_service import CustomerOrderService

service = CustomerOrderService()

customer_orders = service.get_all_customer_orders()

print("\n========== CUSTOMER ORDER LIST ==========\n")

if customer_orders:

    for customer_order in customer_orders:
        print(customer_order)

else:

    print("No Customer Orders Found")
from customer_order_service import CustomerOrderService

service = CustomerOrderService()

customer_order_id = int(input("Enter Customer Order ID: "))

customer_order = service.search_customer_order(customer_order_id)

print("\n========== SEARCH CUSTOMER ORDER ==========\n")

if customer_order:

    print(customer_order)

else:

    print("Customer Order Not Found")
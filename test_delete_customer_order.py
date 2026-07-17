from customer_order_service import CustomerOrderService

service = CustomerOrderService()

customer_order_id = input("Enter Customer Order ID to Delete: ").strip()

if customer_order_id == "":
    print("Customer Order ID cannot be empty.")
else:

    result = service.delete_customer_order(
        int(customer_order_id)
    )

    print("\n========== DELETE CUSTOMER ORDER ==========\n")

    if result:
        print("Customer Order Deleted Successfully")
    else:
        print("Customer Order Not Found")
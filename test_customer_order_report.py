from customer_order_service import CustomerOrderService

service = CustomerOrderService()

report = service.customer_order_report()

print("\n========== CUSTOMER ORDER REPORT ==========\n")

if report:

    print("Total Customer Orders :", report[0])

else:

    print("No Customer Orders Found")
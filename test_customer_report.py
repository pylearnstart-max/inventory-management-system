from customer_service import CustomerService

service = CustomerService()

customers = service.get_customer_report()

print("=" * 40)
print("      CUSTOMER REPORT")
print("=" * 40)

if customers:

    for customer in customers:
        print(customer)

else:
    print("No Customers Found")
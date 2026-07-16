from customer_service import CustomerService

service = CustomerService()

customers = service.get_all_customers()

print("\n========== ALL CUSTOMERS ==========\n")

for customer in customers:
    print(customer)
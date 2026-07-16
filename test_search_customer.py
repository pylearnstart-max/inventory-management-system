from customer_service import CustomerService

service = CustomerService()

customer_name = input("Enter Customer Name: ")

customers = service.search_customer(customer_name)

print("\n========== SEARCH CUSTOMER ==========\n")

if customers:

    for customer in customers:
        print(customer)

else:

    print("Customer Not Found")
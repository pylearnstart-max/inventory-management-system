from customer_service import CustomerService

service = CustomerService()

customer_id = int(input("Enter Customer ID to Delete: "))

service.delete_customer(customer_id)
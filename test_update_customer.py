from datetime import date

from customer_model import Customer
from customer_service import CustomerService

service = CustomerService()

customer = Customer(
    1,
    "Rahul Kumar",
    "9876543210",
    "rahulkumar@gmail.com",
    "Hyderabad",
    date.today()
)

service.update_customer(customer)
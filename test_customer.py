from datetime import date

from customer_model import Customer
from customer_service import CustomerService

customer = Customer(
    "Rahul",
    "9876543210",
    "rahul@gmail.com",
    "Hyderabad",
    date.today()
)

service = CustomerService()

service.add_customer(customer)
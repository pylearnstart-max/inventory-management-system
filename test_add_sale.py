from datetime import date

from sales_model import Sale
from sales_service import SalesService

service = SalesService()

sale = Sale(
    4,      # Existing product_id
    2,      # Existing customer_id
    2,
    55000.00,
    110000.00,
    date.today()
)

service.add_sale(sale)

print("Sale Added Successfully")
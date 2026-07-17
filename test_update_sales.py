from sales_repo import SalesRepo
from sales_service import SalesService


repo = SalesRepo()
service = SalesService(repo)


sale_id = int(input("Enter Sale ID: "))
quantity = int(input("Enter New Quantity: "))
total_amount = float(input("Enter New Amount: "))


result = service.update_sale(
    sale_id,
    quantity,
    total_amount
)

print(result)
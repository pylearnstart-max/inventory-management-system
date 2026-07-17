from sales_repo import SalesRepo
from sales_service import SalesService


repo = SalesRepo()
service = SalesService(repo)


sale_id = int(input("Enter Sale ID: "))


result = service.delete_sale(sale_id)

print(result)
from sales_repo import SalesRepo
from sales_service import SalesService


repo = SalesRepo()
service = SalesService(repo)


result = service.sales_report()


print("========== SALES REPORT ==========")

print("Total Sales :", result[0])
print("Total Revenue :", result[1])
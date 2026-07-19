from sales_repo import SalesRepo
from sales_service import SalesService


def show_sales_report():

    repo = SalesRepo()

    service = SalesService(repo)

    report = service.sales_report()

    print("\n====================================")
    print("         SALES REPORT")
    print("====================================")

    print(f"Total Sales   : {report[0]}")
    print(f"Total Revenue : {report[1]}")

    print("====================================")
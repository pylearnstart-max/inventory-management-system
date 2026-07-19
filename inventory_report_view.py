from product_repo import ProductRepo
from product_service import ProductService


def show_inventory_report():

    repo = ProductRepo()

    service = ProductService(repo)

    report = service.inventory_report()

    print("\n========== INVENTORY REPORT ==========\n")

    print("Total Products :", report[0])
    print("Total Stock    :", report[1])
    print("Stock Value    :", report[2])
from purchase_repo import PurchaseRepo
from purchase_service import PurchaseService


def show_purchase_report():

    repo = PurchaseRepo()

    service = PurchaseService(repo)

    report = service.purchase_report()

    print("\n========================================")
    print("          PURCHASE REPORT")
    print("========================================")

    print(f"Total Purchases : {report[0]}")
    print(f"Total Amount    : {report[1]}")

    print("========================================")
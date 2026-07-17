from purchase_repo import PurchaseRepo
from purchase_service import PurchaseService

repo = PurchaseRepo()
service = PurchaseService(repo)

report = service.purchase_report()

total_purchases = report[0]
total_amount = report[1]

if total_amount is None:
    total_amount = 0

print("\n========== PURCHASE REPORT ==========\n")
print(f"Total Purchases      : {total_purchases}")
print(f"Total Purchase Amount: {total_amount}")
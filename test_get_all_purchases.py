from purchase_repo import PurchaseRepo
from purchase_service import PurchaseService

repo = PurchaseRepo()
service = PurchaseService(repo)

purchases = service.get_all_purchases()

print("========== PURCHASE LIST ==========")

if purchases:
    for purchase in purchases:
        print(purchase)
else:
    print("No Purchase Records Found")
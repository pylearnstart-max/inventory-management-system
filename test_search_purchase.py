from purchase_repo import PurchaseRepo
from purchase_service import PurchaseService

repo = PurchaseRepo()
service = PurchaseService(repo)

purchase_id = int(input("Enter Purchase ID: "))

purchase = service.search_purchase(purchase_id)

print("\n========== SEARCH PURCHASE ==========\n")

if purchase:
    print(purchase)
else:
    print("Purchase Not Found")
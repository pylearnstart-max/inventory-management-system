from purchase_repo import PurchaseRepo
from purchase_service import PurchaseService


repo = PurchaseRepo()
service = PurchaseService(repo)


purchase_id = int(input("Enter Purchase ID: "))

result = service.delete_purchase(purchase_id)

print("\n========== DELETE PURCHASE ==========\n")

if result:
    print("Purchase Deleted Successfully")
else:
    print("Purchase Not Found")
from purchase_repo import PurchaseRepo
from purchase_service import PurchaseService


repo = PurchaseRepo()
service = PurchaseService(repo)


purchase_id = int(input("Enter Purchase ID: "))
quantity = int(input("Enter New Quantity: "))
total_amount = float(input("Enter New Total Amount: "))


result = service.update_purchase(
    purchase_id,
    quantity,
    total_amount
)


print("\n========== UPDATE PURCHASE ==========\n")

if result:
    print("Purchase Updated Successfully")
else:
    print("Purchase Not Found")
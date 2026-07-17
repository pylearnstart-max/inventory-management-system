from purchase_model import Purchase
from purchase_repo import PurchaseRepo
from purchase_service import PurchaseService


repo = PurchaseRepo()
service = PurchaseService(repo)


purchase = Purchase(
    product_id=4,
    supplier_id=1,
    quantity=10,
    unit_price=5000,
    total_amount=50000,
    purchase_date="2026-07-17"
)


result = service.add_purchase(purchase)

print(result)
from supplier_model import Supplier
from supplier_repo import SupplierRepo
from supplier_service import SupplierService


repo = SupplierRepo()

service = SupplierService(repo)


supplier = Supplier(
    "ABC Traders",
    "9876543210",
    "abc@gmail.com",
    "Hyderabad",
    "2026-07-17"
)


service.add_supplier(supplier)
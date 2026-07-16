from supplier_model import Supplier
from supplier_service import SupplierService
from datetime import date

service = SupplierService()

supplier = Supplier(
    "ABC Suppliers",
    "Ramesh",
    "9876543210",
    "abc@gmail.com",
    "Hyderabad",
    date.today()
)

service.add_supplier(supplier)
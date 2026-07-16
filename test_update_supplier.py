from supplier_model import Supplier
from supplier_service import SupplierService
from datetime import date

service = SupplierService()

supplier = Supplier(
    1,
    "ABC Suppliers Pvt Ltd",
    "Suresh",
    "9876500000",
    "abcnew@gmail.com",
    "Hyderabad",
    date.today()
)

service.update_supplier(supplier)
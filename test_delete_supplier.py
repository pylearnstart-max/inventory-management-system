from supplier_service import SupplierService

service = SupplierService()

supplier_id = input("Enter Supplier ID to Delete: ").strip()

if supplier_id == "":
    print("Supplier ID cannot be empty.")
else:
    service.delete_supplier(int(supplier_id))
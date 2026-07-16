from supplier_service import SupplierService

service = SupplierService()

supplier_id = int(input("Enter Supplier ID to Delete: "))

service.delete_supplier(supplier_id)
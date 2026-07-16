from supplier_service import SupplierService

service = SupplierService()

suppliers = service.get_all_suppliers()

print("\n========== SUPPLIER LIST ==========\n")

for supplier in suppliers:
    print(supplier)
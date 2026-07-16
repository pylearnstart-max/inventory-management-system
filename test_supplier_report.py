from supplier_service import SupplierService

service = SupplierService()

suppliers = service.get_supplier_report()

print("\n========== SUPPLIER REPORT ==========\n")

if suppliers:

    for supplier in suppliers:
        print(supplier)

else:

    print("No Suppliers Found")
from supplier_service import SupplierService

service = SupplierService()

supplier_name = input("Enter Supplier Name: ")

suppliers = service.search_supplier(supplier_name)

print("\n========== SEARCH SUPPLIER ==========\n")

if suppliers:

    for supplier in suppliers:
        print(supplier)

else:

    print("Supplier Not Found")
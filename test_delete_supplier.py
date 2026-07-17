from supplier_service import SupplierService

service = SupplierService()

supplier_id = input("Enter Supplier ID to Delete: ").strip()

if supplier_id == "":
    print("Supplier ID cannot be empty.")

else:

    result = service.delete_supplier(int(supplier_id))

    print("\n========== DELETE SUPPLIER ==========\n")

    if result:
        print("Supplier Deleted Successfully")

    else:
        print("Supplier Not Found")
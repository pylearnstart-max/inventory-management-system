from supplier_service import SupplierService


service = SupplierService()


supplier_id = int(input("Enter Supplier ID: "))

phone = input("Enter New Phone: ")

email = input("Enter New Email: ")

address = input("Enter New Address: ")


result = service.update_supplier(
    supplier_id,
    phone,
    email,
    address
)


print("\n========== UPDATE SUPPLIER ==========\n")


if result:

    print("Supplier Updated Successfully")

else:

    print("Supplier Not Found")
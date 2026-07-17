from supplier_repo import SupplierRepo
from supplier_service import SupplierService


repo = SupplierRepo()

service = SupplierService(repo)


suppliers = service.get_all_suppliers()


print("\n========== SUPPLIER LIST ==========\n")


if len(suppliers) == 0:

    print("No Suppliers Found")

else:

    for supplier in suppliers:
        print(supplier)
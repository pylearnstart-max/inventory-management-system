from supplier_service import SupplierService

service = SupplierService()

report = service.supplier_report()

print("\n========== SUPPLIER REPORT ==========\n")

print(f"Total Suppliers : {report[0]}")
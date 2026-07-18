from dashboard_service import DashboardService

service = DashboardService()

summary = service.get_supplier_summary()

print("\n========== SUPPLIER DASHBOARD ==========\n")

print("Total Suppliers :", summary[0])
from dashboard_service import DashboardService

service = DashboardService()

dashboard = service.get_dashboard_summary()

print("\n========== INVENTORY DASHBOARD ==========\n")

print("Total Products  :", dashboard["products"])
print("Total Customers :", dashboard["customers"])
print("Total Suppliers :", dashboard["suppliers"])
print("Total Orders    :", dashboard["orders"])
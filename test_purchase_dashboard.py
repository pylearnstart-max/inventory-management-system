from dashboard_service import DashboardService

service = DashboardService()

summary = service.get_purchase_summary()

print("\n========== PURCHASE DASHBOARD ==========\n")

print("Total Purchases      :", summary[0])
print("Total Purchase Amount:", summary[1])
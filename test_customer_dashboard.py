from dashboard_service import DashboardService

service = DashboardService()

summary = service.get_customer_summary()

print("\n========== CUSTOMER DASHBOARD ==========\n")

print("Total Customers :", summary[0])
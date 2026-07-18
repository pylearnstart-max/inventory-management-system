from dashboard_service import DashboardService

service = DashboardService()

summary = service.get_sales_summary()

print("\n========== SALES DASHBOARD ==========\n")

print("Total Sales        :", summary[0])
print("Total Sales Amount :", summary[1])
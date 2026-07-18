from dashboard_service import DashboardService

service = DashboardService()

summary = service.get_product_stock_summary()

print("\n========== PRODUCT STOCK SUMMARY ==========\n")

print("Total Products :", summary[0])
print("Total Stock    :", summary[1])
from dashboard_service import DashboardService


service = DashboardService()


data = service.get_dashboard_summary()


print("\n========= INVENTORY DASHBOARD =========")


for key,value in data.items():

    print(key, ":", value)
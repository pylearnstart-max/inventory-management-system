from dashboard_service import DashboardService

service = DashboardService()

dashboard = service.get_dashboard_summary()
product = service.get_product_stock_summary()
customer = service.get_customer_summary()
supplier = service.get_supplier_summary()
sales = service.get_sales_summary()
purchase = service.get_purchase_summary()

print("\n================= INVENTORY DASHBOARD =================\n")

print("Products")
print("---------------------------------------")
print("Total Products         :", product[0])
print("Total Stock            :", product[1])

print("\nCustomers")
print("---------------------------------------")
print("Total Customers        :", customer[0])

print("\nSuppliers")
print("---------------------------------------")
print("Total Suppliers        :", supplier[0])

print("\nOrders")
print("---------------------------------------")
print("Total Orders           :", dashboard["orders"])

print("\nSales")
print("---------------------------------------")
print("Total Sales            :", sales[0])
print("Total Sales Amount     :", sales[1])

print("\nPurchases")
print("---------------------------------------")
print("Total Purchases        :", purchase[0])
print("Total Purchase Amount  :", purchase[1])

print("\n=======================================================")
from dashboard_service import DashboardService



def show_dashboard():


    service = DashboardService()


    data = service.get_dashboard_summary()



    print("\n====================================")
    print("        INVENTORY DASHBOARD")
    print("====================================")


    print(
        "Total Products       :",
        data["total_products"]
    )


    print(
        "Total Customers      :",
        data["total_customers"]
    )


    print(
        "Total Suppliers      :",
        data["total_suppliers"]
    )


    print(
        "Total Orders         :",
        data["total_orders"]
    )


    print("------------------------------------")


    print(
        "Total Stock          :",
        data["total_stock"]
    )


    print(
        "Stock Value          :",
        data["stock_value"]
    )


    print("------------------------------------")


    print(
        "Total Sales          :",
        data["total_sales"]
    )


    print(
        "Sales Amount         :",
        data["total_sales_amount"]
    )


    print("------------------------------------")


    print(
        "Total Purchase       :",
        data["total_purchase"]
    )


    print(
        "Purchase Amount      :",
        data["total_purchase_amount"]
    )


    print("====================================")
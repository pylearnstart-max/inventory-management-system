from dashboard_view import show_dashboard
from low_stock_view import show_low_stock_alert
from sales_report_view import show_sales_report
from purchase_report import show_purchase_report
from inventory_report_view import show_inventory_report
from logout import logout


def manager_dashboard():

    while True:

        print("\n===================================")
        print("       MANAGER DASHBOARD")
        print("===================================")

        print("1. Product Management")
        print("2. Supplier Management")
        print("3. Customer Management")
        print("4. Purchase Management")
        print("5. Sales Management")
        print("6. Order Management")
        print("7. Dashboard Summary")
        print("8. Sales Report")
        print("9. Purchase Report")
        print("10. Inventory Report")
        print("11. Low Stock Alert")
        print("12. Logout")

        print("===================================")

        choice = input("Enter Your Choice : ")

        if choice == "1":

            print("Product Module")

        elif choice == "2":

            print("Supplier Module")

        elif choice == "3":

            print("Customer Module")

        elif choice == "4":

            print("Purchase Module")

        elif choice == "5":

            print("Sales Module")

        elif choice == "6":

            print("Order Module")

        elif choice == "7":

            show_dashboard()

        elif choice == "8":

            show_sales_report()

        elif choice == "9":

            show_purchase_report()

        elif choice == "10":

            show_inventory_report()

        elif choice == "11":

            limit = int(input("Enter Low Stock Limit : "))
            show_low_stock_alert(limit)

        elif choice == "12":

            logout()
            break

        else:

            print("\nInvalid Choice")
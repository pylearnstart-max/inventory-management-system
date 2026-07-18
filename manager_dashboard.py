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
        print("7. Dashboard")
        print("8. Logout")
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

            print("Dashboard Module")

        elif choice == "8":

            print("\nLogout Successful")
            break

        else:

            print("\nInvalid Choice")
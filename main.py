from user_service import UserService
from admin_dashboard import admin_dashboard

service = UserService()

while True:

    print("\n====================================")
    print(" INVENTORY MANAGEMENT SYSTEM ")
    print("====================================")
    print("1. Login")
    print("2. Exit")
    print("====================================")

    choice = input("Enter Your Choice: ")

    if choice == "1":

        username = input("Username: ")
        password = input("Password: ")

        user = service.login(username, password)

        if user:

            role = user.role.lower()

            if role == "admin":

                admin_dashboard()

            else:

                print("\nDashboard for this role will be implemented in upcoming stories.")

    elif choice == "2":

        print("Application Closed Successfully")
        break

    else:

        print("Invalid Choice")
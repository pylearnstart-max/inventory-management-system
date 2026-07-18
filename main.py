from user_service import UserService

from admin_dashboard import admin_dashboard
from manager_dashboard import manager_dashboard
from employee_dashboard import employee_dashboard


service = UserService()


while True:

    print("\n====================================")
    print("   INVENTORY MANAGEMENT SYSTEM")
    print("====================================")

    print("1. Login")
    print("2. Exit")

    print("====================================")


    choice = input("Enter Your Choice: ")



    if choice == "1":


        print("\n========== LOGIN ==========\n")


        username = input("Username: ")
        password = input("Password: ")



        user = service.login(username, password)



        if user:


            print("\nLogin Successful")


            role = user.role.lower()



            if role == "admin":


                admin_dashboard()



            elif role == "manager":


                manager_dashboard()



            elif role == "employee":


                employee_dashboard()



            else:


                print("\nInvalid User Role")



        else:


            print("\nInvalid Username or Password")




    elif choice == "2":


        print("\nApplication Closed Successfully")

        break




    else:


        print("\nInvalid Choice")
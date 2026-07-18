from user_service import UserService

service = UserService()

while True:

    print("\n======================================")
    print(" INVENTORY MANAGEMENT SYSTEM ")
    print("======================================")
    print("1. Login")
    print("2. Exit")
    print("======================================")

    choice = input("Enter Your Choice: ")

    if choice == "1":

        print("\n========== LOGIN ==========\n")

        username = input("Enter Username: ")
        password = input("Enter Password: ")

        service.login(username, password)

    elif choice == "2":

        print("\nApplication Closed Successfully")
        break

    else:

        print("\nInvalid Choice")
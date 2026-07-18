from user_service import UserService

service = UserService()

username = input("Enter Username: ")
password = input("Enter Password: ")

service.login(username, password)
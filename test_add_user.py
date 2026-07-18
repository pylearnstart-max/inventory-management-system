from datetime import date

from user_model import User
from user_service import UserService

service = UserService()

username = input("Enter Username: ")
password = input("Enter Password: ")
role = input("Enter Role: ")

user = User(
    username=username,
    password=password,
    role=role,
    created_date=date.today()
)

service.add_user(user)
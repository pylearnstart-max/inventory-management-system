from datetime import date

from user_model import User
from user_service import UserService

service = UserService()

user_id = int(input("Enter User ID: "))
username = input("Enter New Username: ")
password = input("Enter New Password: ")
role = input("Enter New Role: ")

user = User(
    username=username,
    password=password,
    role=role,
    created_date=date.today(),
    user_id=user_id
)

service.update_user(user)
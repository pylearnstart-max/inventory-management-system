from datetime import date

from user_model import User
from user_service import UserService

service = UserService()

user = User(
    "admin",
    "admin123",
    "Admin",
    date.today()
)

service.add_user(user)
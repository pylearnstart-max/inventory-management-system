from user_service import UserService

service = UserService()

user_id = int(input("Enter User ID to Delete: "))

print("\n========== DELETE USER ==========\n")

service.delete_user(user_id)
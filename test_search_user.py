from user_service import UserService

service = UserService()

user_id = int(input("Enter User ID: "))

print("\n========== SEARCH USER ==========\n")

user = service.search_user(user_id)

if user:

    print(user)

else:

    print("User Not Found")
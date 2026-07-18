from user_service import UserService

service = UserService()

print("\n========== USER REPORT ==========\n")

users = service.get_all_users()

if users:

    for user in users:
        print(user)

else:

    print("No Users Found")
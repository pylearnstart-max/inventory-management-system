from user_repo import UserRepo


class UserService:


    def __init__(self):

        self.repo = UserRepo()


    def add_user(self, user):

        self.repo.add_user(user)


    def login(self, username, password):

        user = self.repo.login(username, password)

        if user:

            print("\n========== LOGIN ==========\n")
            print("Login Successful")

        else:

            print("\n========== LOGIN ==========\n")
            print("Invalid Username or Password")


    def search_user(self, user_id):

        return self.repo.search_user(user_id)


    def search_user_by_username(self, username):

        return self.repo.search_user_by_username(username)

    def update_user(self, user):

        self.repo.update_user(user)

    def delete_user(self, user_id):

        self.repo.delete_user(user_id)

    def get_all_users(self):

        return self.repo.get_all_users()
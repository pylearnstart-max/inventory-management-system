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
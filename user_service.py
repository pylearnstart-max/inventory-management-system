from user_repo import UserRepo


class UserService:

    def __init__(self):

        self.repo = UserRepo()

    def add_user(self, user):

        self.repo.add_user(user)
import bcrypt

from user_repo import UserRepo


class UserService:

    def __init__(self):

        self.repo = UserRepo()


    # ==========================
    # ADD USER
    # ==========================

    def add_user(self, user):

        hashed_password = bcrypt.hashpw(
            user.password.encode("utf-8"),
            bcrypt.gensalt()
        ).decode("utf-8")

        user.password = hashed_password

        return self.repo.add_user(user)


    # ==========================
    # LOGIN
    # ==========================

    def login(self, username, password):

        user = self.repo.search_user_by_username(username)

        if user is None:

            return None

        stored_password = user[2]

        if bcrypt.checkpw(

            password.encode("utf-8"),
            stored_password.encode("utf-8")

        ):

            return user

        return None


    # ==========================
    # SEARCH USER BY ID
    # ==========================

    def search_user(self, user_id):

        return self.repo.search_user(user_id)


    # ==========================
    # SEARCH USER BY USERNAME
    # ==========================

    def search_user_by_username(self, username):

        return self.repo.search_user_by_username(username)


    # ==========================
    # UPDATE USER
    # ==========================

    def update_user(self, user):

        return self.repo.update_user(user)


    # ==========================
    # DELETE USER
    # ==========================

    def delete_user(self, user_id):

        return self.repo.delete_user(user_id)


    # ==========================
    # GET ALL USERS
    # ==========================

    def get_all_users(self):

        return self.repo.get_all_users()


    # ==========================
    # CHANGE PASSWORD
    # ==========================

    def change_password(

        self,
        username,
        old_password,
        new_password

    ):

        user = self.repo.search_user_by_username(username)

        if user is None:

            return False

        stored_password = user[2]

        if not bcrypt.checkpw(

            old_password.encode("utf-8"),
            stored_password.encode("utf-8")

        ):

            return False

        hashed_password = bcrypt.hashpw(

            new_password.encode("utf-8"),
            bcrypt.gensalt()

        ).decode("utf-8")

        self.repo.change_password(

            username,
            hashed_password

        )

        return True
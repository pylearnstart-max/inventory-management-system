from user_repo import UserRepo


class UserService:


    def __init__(self):

        self.repo = UserRepo()



    # ==========================
    # ADD USER
    # ==========================

    def add_user(self, user):

        return self.repo.add_user(user)



    # ==========================
    # LOGIN
    # ==========================

    def login(self, username, password):

        user = self.repo.login(
            username,
            password
        )

        return user



    # ==========================
    # SEARCH USER BY ID
    # ==========================

    def search_user(self, user_id):

        return self.repo.search_user(
            user_id
        )



    # ==========================
    # SEARCH USER BY USERNAME
    # ==========================

    def search_user_by_username(self, username):

        return self.repo.search_user_by_username(
            username
        )



    # ==========================
    # UPDATE USER
    # ==========================

    def update_user(self, user):

        return self.repo.update_user(
            user
        )



    # ==========================
    # DELETE USER
    # ==========================

    def delete_user(self, user_id):

        return self.repo.delete_user(
            user_id
        )



    # ==========================
    # GET ALL USERS
    # ==========================

    def get_all_users(self):

        return self.repo.get_all_users()



    # ==========================
    # CHANGE PASSWORD
    # INV-1306
    # ==========================

    def change_password(
            self,
            username,
            old_password,
            new_password
        ):


        # Verify old password

        user = self.repo.login(
            username,
            old_password
        )



        if user is None:

            return False



        # Update new password

        self.repo.change_password(
            username,
            new_password
        )



        return True
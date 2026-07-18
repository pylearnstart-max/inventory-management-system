class User:

    def __init__(
        self,
        username,
        password,
        role,
        created_date,
        user_id=None
    ):

        self.user_id = user_id
        self.username = username
        self.password = password
        self.role = role
        self.created_date = created_date
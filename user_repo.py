from db import get_connection


class UserRepo:

    def add_user(self, user):

        conn = get_connection()
        cursor = conn.cursor()

        query = """
        INSERT INTO Users
        (
            username,
            password,
            role,
            created_date
        )
        VALUES
        (
            ?, ?, ?, ?
        )
        """

        cursor.execute(
            query,
            (
                user.username,
                user.password,
                user.role,
                user.created_date
            )
        )

        conn.commit()

        cursor.close()
        conn.close()

        print("User Added Successfully")
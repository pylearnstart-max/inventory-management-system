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


    def login(self, username, password):

        conn = get_connection()
        cursor = conn.cursor()

        query = """
        SELECT *
        FROM Users
        WHERE username = ?
        AND password = ?
        """

        cursor.execute(
            query,
            (
                username,
                password
            )
        )

        user = cursor.fetchone()

        cursor.close()
        conn.close()

        return user


    def search_user(self, user_id):

        conn = get_connection()
        cursor = conn.cursor()

        query = """
        SELECT *
        FROM Users
        WHERE user_id = ?
        """

        cursor.execute(
            query,
            (user_id,)
        )

        user = cursor.fetchone()

        cursor.close()
        conn.close()

        return user


    def search_user_by_username(self, username):

        conn = get_connection()
        cursor = conn.cursor()

        query = """
        SELECT *
        FROM Users
        WHERE username LIKE ?
        """

        cursor.execute(
            query,
            ('%' + username + '%',)
        )

        users = cursor.fetchall()

        cursor.close()
        conn.close()

        return users
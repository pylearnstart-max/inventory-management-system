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
            (
                "%" + username + "%",
            )
        )

        users = cursor.fetchall()

        cursor.close()
        conn.close()

        return users


    def update_user(self, user):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM Users WHERE user_id = ?",
            (user.user_id,)
        )

        existing_user = cursor.fetchone()

        if existing_user is None:

            print("User Not Found")

            cursor.close()
            conn.close()

            return

        query = """
        UPDATE Users
        SET
            username = ?,
            password = ?,
            role = ?
        WHERE user_id = ?
        """

        cursor.execute(
            query,
            (
                user.username,
                user.password,
                user.role,
                user.user_id
            )
        )

        conn.commit()

        print("User Updated Successfully")

        cursor.close()
        conn.close()


    def delete_user(self, user_id):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM Users WHERE user_id = ?",
            (user_id,)
        )

        existing_user = cursor.fetchone()

        if existing_user is None:

            print("User Not Found")

            cursor.close()
            conn.close()

            return

        query = """
        DELETE FROM Users
        WHERE user_id = ?
        """

        cursor.execute(
            query,
            (user_id,)
        )

        conn.commit()

        print("User Deleted Successfully")

        cursor.close()
        conn.close()


    def get_all_users(self):

        conn = get_connection()
        cursor = conn.cursor()

        query = """
        SELECT
            user_id,
            username,
            password,
            role,
            created_date
        FROM Users
        ORDER BY user_id
        """

        cursor.execute(query)

        users = cursor.fetchall()

        cursor.close()
        conn.close()

        return users
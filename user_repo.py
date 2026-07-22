from db import get_connection


class UserRepo:


    # ==========================================
    # ADD USER
    # ==========================================

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

        return True


    # ==========================================
    # LOGIN
    # ==========================================

    def login(self, username):

        conn = get_connection()
        cursor = conn.cursor()

        query = """
        SELECT *
        FROM Users
        WHERE username = ?
        """

        cursor.execute(
            query,
            (username,)
        )

        user = cursor.fetchone()

        cursor.close()
        conn.close()

        return user


    # ==========================================
    # SEARCH USER BY ID
    # ==========================================

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


    # ==========================================
    # SEARCH USER BY USERNAME
    # ==========================================

    def search_user_by_username(self, username):

        conn = get_connection()
        cursor = conn.cursor()

        query = """
        SELECT *
        FROM Users
        WHERE username = ?
        """

        cursor.execute(
            query,
            (username,)
        )

        user = cursor.fetchone()

        cursor.close()
        conn.close()

        return user


    # ==========================================
    # UPDATE USER
    # ==========================================

    def update_user(self, user):

        conn = get_connection()
        cursor = conn.cursor()

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

        updated = cursor.rowcount

        cursor.close()
        conn.close()

        return updated > 0


    # ==========================================
    # DELETE USER
    # ==========================================

    def delete_user(self, user_id):

        conn = get_connection()
        cursor = conn.cursor()

        query = """
        DELETE FROM Users
        WHERE user_id = ?
        """

        cursor.execute(
            query,
            (user_id,)
        )

        conn.commit()

        deleted = cursor.rowcount

        cursor.close()
        conn.close()

        return deleted > 0


    # ==========================================
    # GET ALL USERS
    # ==========================================

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


    # ==========================================
    # CHANGE PASSWORD
    # ==========================================

    def change_password(self, username, new_password):

        conn = get_connection()
        cursor = conn.cursor()

        query = """
        UPDATE Users
        SET password = ?
        WHERE username = ?
        """

        cursor.execute(
            query,
            (
                new_password,
                username
            )
        )

        conn.commit()

        updated = cursor.rowcount

        cursor.close()
        conn.close()

        return updated > 0
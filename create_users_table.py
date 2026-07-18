from db import get_connection

conn = get_connection()
cursor = conn.cursor()

query = """
IF OBJECT_ID('Users', 'U') IS NULL
BEGIN
    CREATE TABLE Users
    (
        user_id INT IDENTITY(1,1) PRIMARY KEY,
        username VARCHAR(100) NOT NULL UNIQUE,
        password VARCHAR(100) NOT NULL,
        role VARCHAR(50) NOT NULL,
        created_date DATE NOT NULL
    )
END
"""

cursor.execute(query)
conn.commit()

cursor.close()
conn.close()

print("Users Table Verified Successfully")
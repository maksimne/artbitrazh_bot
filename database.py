import sqlite3


def get_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


def add_account(email: str, password: str, platform: int, author: str):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
        INSERT INTO accounts (email, password, platform, author)
        VALUES (?, ?, ?, ?)
        """, (email, password, platform, author))
        conn.commit()
    except sqlite3.IntegrityError:
        print("Fail")
    finally:
        conn.close()

def get_account_by_mail(mail: str):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    SELECT * FROM accounts WHERE mail = ?
    """, (mail,))
    acc = cursor.fetchone()
    conn.close()
    return acc


def get_account_by_author(author: str):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    SELECT * FROM accounts WHERE author = ?
    """, (author,))
    acc = cursor.fetchone()
    conn.close()
    return acc



def delete_account(mail: str):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    DELETE FROM users WHERE mail = ?
    """, (mail,))
    conn.commit()
    conn.close()


# def create_tables():
#     conn = get_connection()
#     cursor = conn.cursor()
#
#     cursor.execute("""
#     CREATE TABLE IF NOT EXISTS accounts (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         mail TEXT,
#         password TEXT,
#         full_name TEXT,
#         platform INTEGER,
#         author TEXT
#     )
#     """)
#     conn.commit()
#     conn.close()
#
# create_tables()




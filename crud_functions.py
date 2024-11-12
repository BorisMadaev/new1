import sqlite3


def initiate_db():
    connection = sqlite3.Connection('telegram.db')
    cursor = connection.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL
    )
    """)
#    for i in range(1, 5):
#        cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)",
#                       (f'Продукт {i}', f'Описание {i}', i*100))
    connection.commit()
    connection.close()


def get_all_products():
    connection = sqlite3.Connection('telegram.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Products")
    all_products = cursor.fetchall()
    connection.commit()
    connection.close()
    return all_products


def is_included(username):
    connection = sqlite3.Connection('telegram.db')
    cursor = connection.cursor()
    if not cursor.execute("SELECT username FROM Users WHERE username = ?", (username,)).fetchone() is None:
        connection.commit()
        connection.close()
        return True
    else:
        connection.commit()
        connection.close()
        return False


def add_user(username, email, age):
    connection = sqlite3.Connection('telegram.db')
    cursor = connection.cursor()
    if is_included(username) is False:
        cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
                       (username, email, age, 1000))
    connection.commit()
    connection.close()


initiate_db()

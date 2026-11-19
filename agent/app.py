python
import sqlite3

def login(username, password):
    conn = None
    try:
        conn = sqlite3.connect('users_bank.db')
        cursor = conn.cursor()
        # Placeholders fixam os valores como dados, nunca como SQL
        cursor.execute(
            "SELECT * FROM users WHERE username = ? AND password = ?",
            (username, password)
        )
        result = cursor.fetchone()
        return "Login successful" if result else "Login failed"
    except sqlite3.Error:
        return "Login failed"
    finally:
        if conn is not None:
            conn.close()
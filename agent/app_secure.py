# Versão segura do app.py — corrigida após análise de vulnerabilidade de SQL Injection.
# A correção usa placeholders (?) que separam dados de código SQL,
# impedindo que qualquer entrada do usuário seja interpretada como comando.

import sqlite3

def login(username, password):
    conn = None
    try:
        conn = sqlite3.connect('users_bank.db')
        cursor = conn.cursor()

        # CORREÇÃO: placeholders fixam os valores como dados, nunca como SQL.
        # Mesmo que o usuário digite ' OR '1'='1, isso será tratado como texto literal.
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

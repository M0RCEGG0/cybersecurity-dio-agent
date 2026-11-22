# WARNING: Este arquivo contém uma vulnerabilidade intencional para fins educacionais.
# NÃO use este código em produção. Ele é vulnerável a SQL Injection.
# Veja app_secure.py para a versão corrigida.

import sqlite3

def login(username, password):
    conn = sqlite3.connect('users_bank.db')
    cursor = conn.cursor()

    # VULNERABILIDADE: a query é montada concatenando diretamente os dados do usuário.
    # Um atacante pode digitar: ' OR '1'='1 e ignorar a senha por completo.
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"

    cursor.execute(query)
    result = cursor.fetchone()
    conn.close()

    if result:
        return "Login successful"
    else:
        return "Login failed"

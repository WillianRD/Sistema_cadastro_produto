import sqlite3

def connect_data():
    con = sqlite3.connect('teste.db')
    cursor = con.cursor()
    cursor.close()
    return 'Banco criado', True
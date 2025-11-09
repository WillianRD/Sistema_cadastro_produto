import sqlite3

def create_table():
    con = sqlite3.connect('teste.db')
    cursor = con.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        marketplace TEXT NOT NULL,
        produto TEXT NOT NULL,
        telefone TEXT NOT NULL,
        loja TEXT NOT NULL
    )
    """)
    con.commit()
    con.close()

create_table()
print("Tabela criada com sucesso!")

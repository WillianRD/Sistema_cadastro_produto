import sqlite3

def create_table():
    con = sqlite3.connect('banco.db')
    cursor = con.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS produtos(
            prod_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            prod_name TEXT NOT NULL,
            prod_categoria TEXT,
            prod_descricao TEXT NOT NULL,
            prod_preco REAL NOT NULL,
            prod_qtd_estoque INT NOT NULL,
            prod_data_fabricacao DATE NOT NULL,
            prod_data_vencimento DATE NOT NULL,
            prod_caracter TEXT NOT NULL,
            prod_url TEXT
            )''')
    con.commit()
    cursor.close()
    
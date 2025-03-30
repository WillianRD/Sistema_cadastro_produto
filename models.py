import sqlite3

def createBanco():
    con = sqlite3.connect('banco_de_cadastro.db')
    cursor = con.cursor()

def createTable():
    con = sqlite3.connect('banco_de_cadastro.db')
    cursor = con.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS produto(
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

def inserirDados():
    con = sqlite3.connect('banco_de_cadastro.db')
    cursor = con.cursor()
    
    cursor.execute('''INSERT INTO produto(prod_name, prod_categoria, prod_descricao, prod_preco, prod_qtd_estoque,
                   prod_data_fabricacao, prod_data_vencimento, prod_caracter, prod_url)   
                   VALUES ('Smartphone', 'Tecnologia', 'Celular top de linha', 2999.99, 10, '2024-01-01', '2026-01-01', '128GB, Tela AMOLED', 'https://exemplo.com')
                ''')
    
def mostrarDados():
    con = sqlite3.connect('banco_de_cadastro.db')
    cursor = con.cursor()
    
    cursor.execute('SELECT * FROM produto')
    for exibir in cursor.fetchall():
        print(exibir)
        
mostrarDados()        
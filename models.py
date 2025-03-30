import sqlite3
from sqlite3 import Error
    
def connectDb():
    con = sqlite3.connect('banco_de_cadastro.db')
    cursor = con.cursor()

def createTable():
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
    con.close()
    
def updateDados(nome,categoria,desc,preco,qtd,data_fab,data_ven,caracteres,url):
    con = sqlite3.connect('banco_de_cadastro.db')
    cursor = con.cursor()
    
    sql = '''INSERT INTO produto
        (prod_name, prod_categoria, prod_descricao, prod_preco, prod_qtd_estoque, 
        prod_data_fabricacao, prod_data_vencimento, prod_caracter, prod_url)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)'''
    cursor.execute(sql, (nome, categoria, desc, preco, qtd, data_fab, data_ven, caracteres, url))
    con.commit()
    cursor.close()

    con.commit()
    cursor.close()
    
def ReadDados():
    con = sqlite3.connect('banco_de_cadastro.db')
    cursor = con.cursor()
    
    cursor.execute('SELECT * FROM produto')
    for exibir in cursor.fetchall():
        print(exibir)
        
#inserirDados('Smartphone', 'Tecnologia', 'Celular top de linha', 2999.99, 10, '2024-01-01', '2026-01-01', '128GB, Tela AMOLED', 'https://exemplo.com')     

def deleteProduto(produto_id):
    con = sqlite3.connect('banco_de_cadastro.db')
    cursor = con.cursor()
    
    exe = "DELETE FROM produto WHERE prod_id = ?"
    
    try:
        cursor.execute(exe, (produto_id,))
        con.commit()
        print("✅ Produto deletado com sucesso!")
    except sqlite3.Error as e:
        print(f"❌ Erro ao deletar produto: {e}")
    finally:
        cursor.close()
        con.close()


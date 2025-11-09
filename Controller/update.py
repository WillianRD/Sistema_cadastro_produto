import sqlite3

def insert_data(nome,marketplace, produto, telefone, loja):
    con = sqlite3.connect('teste.db')
    cursor = con.cursor()
    
    sql = '''INSERT INTO clientes
        (name, marketplace, produto, telefone, loja)
        VALUES (?,?,?,?,?)'''
    cursor.execute(sql, (nome, marketplace, produto, telefone, loja))
    con.commit()
    cursor.close()
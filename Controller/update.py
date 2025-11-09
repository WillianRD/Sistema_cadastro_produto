import sqlite3

def insert_data(nome,marketplace, produto, npedido, telefone, loja):
    con = sqlite3.connect('banco.db')
    cursor = con.cursor()
    
    sql = '''INSERT INTO clientes
        (name, marketplace, produto,npedido, telefone, loja)
        VALUES (?,?,?,?,?,?)'''
    cursor.execute(sql, (nome, marketplace, produto, npedido, telefone, loja))
    con.commit()
    cursor.close()
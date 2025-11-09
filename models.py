import sqlite3

def connectDb():
    con = sqlite3.connect('teste.db')
    cursor = con.cursor()
    cursor.close()
    return 'Banco criado', True

def createTable():
    con = sqlite3.connect('teste.db')
    cursor = con.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientes(
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            name TEXT NOT NULL,
            marketplace TEXT NOT NULL,
            produto TEXT NOT NULL,
            telefone TEXT NOT NULL,
            loja TEXT NOT NULL
        )
    ''')
    con.commit()
    cursor.close()
    con.close()

def updateDados(name, marketplace, produto, telefone, loja):
    con = sqlite3.connect('teste.db')
    cursor = con.cursor()
    
    sql = '''INSERT INTO clientes
        (name, marketplace, produto, telefone, loja)
        VALUES (?,?,?,?,?)'''
    
    cursor.execute(sql, (name, marketplace, produto, telefone, loja))
    con.commit()
    cursor.close()
    con.close()
    
def ReadDados():
    con = sqlite3.connect('teste.db')
    cursor = con.cursor()
    
    cursor.execute('SELECT * FROM clientes')
    dados = cursor.fetchall()
    con.close()
    
    # Converter os dados
    listaDeProduto = [{
        "nome": linha[1], 
        "marketplace": linha[2],
        "produto": linha[3],
        "telefone": linha[4],
        "loja": linha[5]
    } for linha in dados]
    
    return listaDeProduto

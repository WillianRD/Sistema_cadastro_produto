import sqlite3
    
def connectDb():
    con = sqlite3.connect('banco.db')
    cursor = con.cursor()
    cursor.close()
    return 'Banco criado', True

def createTable():
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
    
def updateDados(nome,categoria,desc,preco,qtd,data_fab,data_ven,caracteres,url):
    con = sqlite3.connect('banco.db')
    cursor = con.cursor()
    
    sql = '''INSERT INTO produtos
        (prod_name, prod_categoria, prod_descricao, prod_preco, prod_qtd_estoque, 
        prod_data_fabricacao, prod_data_vencimento, prod_caracter, prod_url)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)'''
    cursor.execute(sql, (nome, categoria, desc, preco, qtd, data_fab, data_ven, caracteres, url))
    con.commit()
    cursor.close()
    
def ReadDados():
        
    con = sqlite3.connect('banco.db')
    cursor = con.cursor()
    
    cursor.execute('SELECT * FROM produtos')
    dados = cursor.fetchall()
    print(dados)
    con.close()
    
    # Converter os dados
    listaDeProduto = [{
        "titulo": linha[1], # Na posição 1 do banco de dados
        "categoria": linha[2] , # Na posição 2 do banco de dados
        "descricao": linha[3], # Na posição 3 do banco de dados
        "preco": linha[4], # Na posição 4 do banco de dados
        "imagem_url": linha[9] # Na posição 9 do banco de dados
        } for linha in dados]
    return listaDeProduto

     
# connectDb()
# createTable() 
updateDados("Iphone 16 Pro Max 256GB", "Tecnologia","Celular Apple",7.200,100,"20/02/2025","20/02/2026","Celular com 1 capa\nCarregador","https://a-static.mlcdn.com.br/1500x1500/apple-iphone-15-128gb-preto-61-48mp-ios-5g/magazineluiza/238035600/716d868f4d404bfb6f8189c688a8c74f.jpg")
# ReadDados()
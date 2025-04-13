import sqlite3
from sqlite3 import Error
    
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
    
    # con = sqlite3.connect('sql.db')
    # cursor = con.cursor()
    
    # cursor.execute('SELECT * FROM produto')
    # for exibir in cursor.fetchall():
    #     print(exibir)
        
    con = sqlite3.connect('banco.db')
    cursor = con.cursor()
    
    cursor.execute('SELECT * FROM produtos')
    dados = cursor.fetchall()
    print(dados)
    con.close()
    
    # Converter os dados
    listaDeProduto = [{
        "url_p": linha[8],
        "titulo": linha[1],
        "categoria": linha[2] ,
        "descricao": linha[3],
        "preco": linha[4]
        }  for linha in dados]
    return listaDeProduto
        
    
    for exibir in cursor.fetchall():
        print(exibir)
        

def deleteProduto():
    con = sqlite3.connect('banco.db')
    cursor = con.cursor()
    
    while(True):    
        print('Você deseja deletar qual campo?\n1.ID:\n2.Nome do Produto\n3.Quantidade do Estoque')
    
        campo  =int(input('Digite um digito para deletar um campo'))
    
        print("Mostrando todos os dados da tabela Produto: ",ReadDados())
        id = int(input('Digite o ID do campo: \n'))
        
        if campo == 1:
            sql = '''DELETE FROM produto WHERE prod_id = ? {id}'''
            cursor.execute(sql)
            con.commit()
            print(f"ID {id} foi deletado com sucesso")
        
        if campo == 2:
            sql = f"DELETE FROM produto WHERE prod_name = {id}"
            cursor.execute(sql)
            print(f"Produto nome: {id} foi deletado com sucesso")  
       
        
        if campo == 3:
            sql   = f"DELETE FROM produto WHERE prod_qtd_estoque = {id} " 
            print(f"Produto nome: {id} foi deletado com sucesso")   
            
        if campo == 0:
            sql = f"DELETE FROM produto"    
            cursor.execute(sql)
            con.commit()
            print(f"Todos os produtos foram deletados do banco de dados. Obrigado")
     
# connectDb()
# createTable() 
# updateDados("Celular Iphone 16 Pro Max 256GB", "Tecnologia","Celular Apple",7.200,100,"20/02/2025","20/02/2026","Celular com 1 capa\nCarregador","https://a-static.mlcdn.com.br/1500x1500/apple-iphone-15-128gb-preto-61-48mp-ios-5g/magazineluiza/238035600/716d868f4d404bfb6f8189c688a8c74f.jpg")
ReadDados()
import sqlite3
from sqlite3 import Error
    
def connectDb():
    con = sqlite3.connect('banco-para-testes.db')
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
    con = sqlite3.connect('banco-para-testes.db')
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
    
    # con = sqlite3.connect('sql.db')
    # cursor = con.cursor()
    
    # cursor.execute('SELECT * FROM produto')
    # for exibir in cursor.fetchall():
    #     print(exibir)
        
    con = sqlite3.connect('banco-para-testes.db')
    cursor = con.cursor()
    
    cursor.execute('SELECT * FROM produto')
    dados = cursor.fetchall()
    print(dados)
    con.close()
    
    # Converter os dados
    listaDeProduto = [{"imagem_url": linha[0], "titulo": linha[1],"categoria": linha[2] ,"descricao": linha[3], "preco": linha[4]}  for linha in dados]
    return listaDeProduto
        
    
    for exibir in cursor.fetchall():
        print(exibir)
        

def deleteProduto():
    con = sqlite3.connect('banco-para-testes.db')
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
     
             
updateDados('Smartphone', 'Tecnologia', 'Celular top de linha', 2999.99, 10, '2024-01-01', '2026-01-01', '128GB, Tela AMOLED', 'https://exemplo.com')     
ReadDados()
# deleteProduto()
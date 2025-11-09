import sqlite3

def read_data():
        
    con = sqlite3.connect('teste.db')
    cursor = con.cursor()
    
    cursor.execute('SELECT * FROM clientes')
    dados = cursor.fetchall()
    print(dados)
    con.close()
    
    # Converter os dados
    listaDeProduto = [{
        "nome": linha[1], 
        "marketplce": linha[2] ,
        "produto": linha[3],
        "telefone": linha[4],
        "loja": linha[5]
        } for linha in dados]
    return listaDeProduto

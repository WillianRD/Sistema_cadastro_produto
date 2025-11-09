import sqlite3

def read_data():
        
    con = sqlite3.connect('banco.db')
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
        "npedido": linha[4],
        "telefone": linha[5],
        "loja": linha[6]
        } for linha in dados]
    return listaDeProduto

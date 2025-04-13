import sqlite3

def read_data():
        
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

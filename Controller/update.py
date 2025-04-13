import sqlite3

def insert_data(nome,categoria,desc,preco,qtd,data_fab,data_ven,caracteres,url):
    con = sqlite3.connect('banco.db')
    cursor = con.cursor()
    
    sql = '''INSERT INTO produtos
        (prod_name, prod_categoria, prod_descricao, prod_preco, prod_qtd_estoque, 
        prod_data_fabricacao, prod_data_vencimento, prod_caracter, prod_url)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)'''
    cursor.execute(sql, (nome, categoria, desc, preco, qtd, data_fab, data_ven, caracteres, url))
    con.commit()
    cursor.close()
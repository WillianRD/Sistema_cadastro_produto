from flask import Flask, render_template, request
from Controller import connect_data, read_data, update_data, delete


# Chama a instancia do Flask
app = Flask(__name__)

# Rota criada
@app.route("/", methods=['POST','GET'])
def index():
    if request.method == 'POST':
        produto = request.form['produto'] # Variavel produto recebe requisição do form do atributo produto do index.html
        categoria = request.form['categoria']
        preco = float( request.form['preco'])
        descricao = request.form['descricao']
        qtd = int(request.form['estoque'])
        fornecedor= request.form['fornecedor']
        fabricacao= request.form['fabricacao']
        vencimento= request.form['vencimento']
        caracteristicas= request.form['caracteristicas']
        url_link_page = request.form['urllink']
        update(produto,categoria,descricao,preco,qtd,fabricacao,vencimento,caracteristicas,url_link_page)
    return render_template('index.html')

@app.route("/produtos/read", methods=['GET'])
def get_produto():
    listaDeProdutos = ReadDados()
    return render_template('form_add.html',lista=listaDeProdutos)

if __name__ == '__main__':
    app.run(debug=True)
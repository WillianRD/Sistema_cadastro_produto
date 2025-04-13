from flask import Flask, render_template, request, url_for # type: ignore
from validar_produto.validarProduto import checkSize,checkCategory
from validar_produto.validarProduto import checkPrice, checkDesc, checkSizeEstoque,checkFornecedor
from validar_produto.validarProduto import caracteres, url
from models import updateDados, ReadDados
app = Flask(__name__)

@app.route("/", methods=['GET'])
def main():
    index()
    return 'Página principal --- Em produção'

@app.route("/produtos/insert", methods=['POST','GET'])
def index():
    if request.method == 'POST':
        produto = request.form['produto']
        categoria = request.form['categoria']
        preco = request.form['preco']
        descricao = request.form['descricao']
        qtd = request.form['estoque']
        fornecedor= request.form['fornecedor']
        fabricacao= request.form['fabricacao']
        vencimento= request.form['vencimento']
        caracteristicas= request.form['caracteristicas']
        url_link_page = request.form['url_link_page']
        updateDados(produto,categoria,preco,descricao,qtd,fornecedor,fabricacao,vencimento,caracteristicas,url_link_page)
    return render_template('index.html')

@app.route("/produtos/read", methods=['GET', 'POST'])
def get_produto():
    listaDeProdutos = ReadDados()
    return render_template('produto.html',lista=listaDeProdutos)

@app.route("/produtos/delete", methods=['GET','DELETE'])
def delete_produto():
    return '<h1>Essa rota vai servir para deletar dados --- Em produção </h1>'
    
@app.route('/produtos/update', methods=['GET']) 
def update():
    return 'Atualizar dados --- Em produção'   

if __name__ == '__main__':
    app.run(debug=True)

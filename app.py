from flask import Flask, render_template, request, url_for # type: ignore
from validar_produto.validarProduto import checkSize,checkCategory
from validar_produto.validarProduto import checkPrice, checkDesc, checkSizeEstoque,checkFornecedor
from validar_produto.validarProduto import caracteres, url
from models import updateDados, ReadDados
app = Flask(__name__)

@app.route("/", methods=['GET'])
def main():
    return 'Página principal --- Em produção'

@app.route("/produtos/insert", methods=['POST','GET'])
def index():
    if request.method == 'POST':
        produto = request.form['produto']
        categoria = request.form['categoria']
        preco = float( request.form['preco'])
        descricao = request.form['descricao']
        qtd = int(request.form['estoque'])
        fornecedor= request.form['fornecedor']
        fabricacao= request.form['fabricacao']
        vencimento= request.form['vencimento']
        caracteristicas= request.form['caracteristicas']
        link_image = request.form['page_url']
        updateDados(produto,categoria,descricao,preco,qtd,fabricacao,vencimento,caracteristicas,link_image)
    return render_template('index.html')

@app.route("/produtos/read", methods=['GET', 'POST'])
def get_produto():
    listaDeProdutos = ReadDados()
    return render_template('form_add.html',lista=listaDeProdutos)

@app.route("/produtos/delete", methods=['GET','DELETE'])
def delete_produto():
    return '<h1>Essa rota vai servir para deletar dados --- Em produção </h1>'
    
@app.route('/produtos/update', methods=['GET']) 
def update():
    return 'Atualizar dados --- Em produção'   

if __name__ == '__main__':
    app.run(debug=True)

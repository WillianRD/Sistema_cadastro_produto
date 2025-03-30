from flask import Flask, render_template, request, url_for
from validarProduto import checkSize,checkCategory
from validarProduto import checkPrice, checkDesc, checkSizeEstoque,checkFornecedor
from validarProduto import caracteres, url
from models import createBanco


from models import createBanco
app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        produto = request.form['produto']
        categoria = request.form['categoria']
        preco = request.form['preco']
        descricao = request.form['descricao']
        quantidadeEstoque = request.form['estoque']
        fornecedor= request.form['fornecedor']
        fabricacao= request.form['fabricacao']
        vencimento= request.form['vencimento']
        caracteristicas= request.form['caracteristicas']
        url_link_page = request.form['url_link_page']
           
        print(f'Validação Produto Nome: {checkSize(produto)}')
        print(f'Validação Categoria Produto: {checkCategory(categoria)}')
        print(f'Validação Preço Produto: {checkPrice(preco)}')
        print(f'Validação Descrição Produto: {checkDesc(descricao)}')
        print(f'Validação QTD Estoque Produto: {checkSizeEstoque(quantidadeEstoque)}')
        print(f'Validação Fornecedor Produto: {checkFornecedor(fornecedor)}')
        print(f'Validação Caracteres Produto: {caracteres(caracteristicas)} ')
        print(f'Validação URL Produto: {url(url_link_page)}')
    return render_template('index.html')



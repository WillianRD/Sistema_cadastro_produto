from flask import Flask, render_template, request, url_for
from validarProduto import checkSize, checkPrice, checkDesc

app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        produto = request.form['produto']
        categoria = request.form['categoria']
        descricao = request.form['descricao']
        preco: int = request.form['preco']
        quantidadeEstoque = request.form['estoque']
        fornecedor= request.form['fornecedor']
        fabricacao= request.form['fabricacao']
        vencimento= request.form['vencimento']
        caracteristicas= request.form['caracteristicas']
        url = request.form['url']
        
        print(f'Validação Produto: {checkSize(produto)}')
        print(f'Validação Categoria {checkSize(categoria)}')
        print(f'Validaçaõ Descrição {checkSize(descricao)}')
        print(f'Validação Preço {checkSize(preco)}')
        
    return render_template('index.html')



from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        produto: str = request.form['produto']
        categoria: str = request.form['categoria']
        descricao: str = request.form['descricao']
        preco: str = request.form['preco']
        quantidadeEstoque: int = request.form['estoque']
        fornecedor: str = request.form['fornecedor']
        fabricacao: str = request.form['fabricacao']
        vencimento: str = request.form['vencimento']
        caracteristicas: str = request.form['caracteristicas']
        url: str = request.form['url']
        
        print(f'Produto:{produto}')
        print(f'Categoria{categoria}Descrição{descricao}')
        print(f'Preço{preco}Quantidade Estoque{quantidadeEstoque}Fornecedor{fornecedor}')
        print(f'Fabricação{fabricacao}Vencimento{vencimento}Caracteristicas{caracteristicas}URL:{url}')
    return render_template('index.html')



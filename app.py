from flask import Flask, render_template, request, redirect, url_for
from Controller import insert_data
from models import createTable

app = Flask(__name__)
createTable()

@app.route("/", methods=['POST','GET'])
def index():
    if request.method == 'POST':
        nomeCliente = request.form['name']
        tipoDeMarketplace = request.form['categoria']
        produto = request.form['produto']
        npedido = request.form['idpedido']
        telefone = request.form['telefone']
        fornecedorLoja = request.form['loja']

        insert_data(nomeCliente, tipoDeMarketplace, produto, npedido, telefone, fornecedorLoja)

        # Redireciona e passa o nome do cliente como parâmetro na URL
        return redirect(url_for('sucesso', nome=nomeCliente))

    return render_template('index.html')


@app.route("/sucesso")
def sucesso():
    nome = request.args.get('nome', '')  # pega o nome do cliente passado na URL
    return render_template("sucesso.html", nome=nome)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

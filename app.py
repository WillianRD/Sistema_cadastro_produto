from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        name: str = request.form['name']
        autor: str = request.form['autor']
        temporadas: int = request.form['temporadas']
        imagem: str = request.form['img']

        print(f"Nome:{name}\nAutor:{autor}\nTemporadas:{temporadas}\nimagem:{imagem}")
    return render_template('index.html')



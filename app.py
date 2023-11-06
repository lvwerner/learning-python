from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

def gerar_senha(comprimento=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    return senha

@app.route('/')
def index():
    return render_template('gerador_de_senhas.html', senha_gerada="")

@app.route('/gerar_senha', methods=['POST'])
def gerar_senha_route():
    comprimento_da_senha = int(request.form['comprimento'])
    senha_gerada = gerar_senha(comprimento_da_senha)
    return render_template('gerador_de_senhas.html', senha_gerada=senha_gerada)

if __name__ == '__main__':
    app.run(debug=True)

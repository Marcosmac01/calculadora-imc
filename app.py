from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Mostra o formulário direto na raiz

@app.route('/calcular-imc', methods=['POST'])
def calcular_imc():
    try:
        peso = float(request.form['peso'])
        altura = float(request.form['altura'])
        imc = peso / (altura ** 2)
        return render_template('resultado.html', imc=round(imc, 2))
    except (ValueError, KeyError):
        return "Erro: valores inválidos"

if __name__ == '__main__':
    app.run(debug=True)


from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/resultado', methods=['POST'])
def resultado():
    peso = float(request.form['peso'])
    altura = float(request.form['altura'])
    imc = round(peso / (altura ** 2), 2)

    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif 18.5 <= imc <= 24.9:
        classificacao = "Peso ideal"
    elif 25 <= imc <= 29.9:
        classificacao = "Sobrepeso"
    elif 30 <= imc <= 34.9:
        classificacao = "Obesidade grau 1"
    elif 35 <= imc <= 39.9:
        classificacao = "Obesidade grau 2"
    else:
        classificacao = "Obesidade grau 3"

    return render_template('resultado.html', imc=imc, classificacao=classificacao)

if __name__ == '__main__':
    app.run(debug=True)



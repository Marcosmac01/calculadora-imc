from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calcular', methods=['POST'])
def calcular():
    try:
        peso = float(request.form['peso'])
        altura = float(request.form['altura'])
        imc = peso / (altura ** 2)

        if imc < 18.5:
            classificacao = "Abaixo do peso"
        elif 18.5 <= imc < 25:
            classificacao = "Peso ideal"
        elif 25 <= imc < 30:
            classificacao = "Sobrepeso"
        elif 30 <= imc < 35:
            classificacao = "Obesidade grau 1"
        elif 35 <= imc < 40:
            classificacao = "Obesidade grau 2"
        else:
            classificacao = "Obesidade grau 3"

        return render_template('resultado.html', imc=round(imc, 2), classificacao=classificacao)
    except:
        return "Erro no cálculo. Verifique os valores inseridos."

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/politica')
def politica():
    return render_template('politica.html')

if __name__ == '__main__':
    app.run(debug=True)



from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular', methods=['POST'])
def calcular():
    try:
        peso = float(request.form['peso'])
        altura = float(request.form['altura']) / 100
        imc = peso / (altura ** 2)
        resultado = ""
        if imc < 18.5:
            resultado = "Abaixo do peso"
        elif 18.5 <= imc < 25:
            resultado = "Peso normal"
        elif 25 <= imc < 30:
            resultado = "Sobrepeso"
        else:
            resultado = "Obesidade"
        return render_template('resultado.html', imc=round(imc, 2), resultado=resultado)
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


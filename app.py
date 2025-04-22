from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Mostra o formulário direto na raiz

@app.route('/calcular-imc', methods=['POST'])
def calcular_imc():
    try:
        peso = float(request.form['peso'])
        altura = float(request.form['altura'])
        imc = round(peso / (altura * altura), 2)

        # Classificação do IMC
        if imc < 18.5:
            classificacao = "Abaixo do peso"
        elif imc < 25:
            classificacao = "Peso ideal"
        elif imc < 30:
            classificacao = "Sobrepeso"
        elif imc < 35:
            classificacao = "Obesidade grau 1"
        elif imc < 40:
            classificacao = "Obesidade grau 2"
        else:
            classificacao = "Obesidade grau 3"

        return render_template('resultado.html', imc=imc, classificacao=classificacao)
    except Exception as e:
        return f"Erro no cálculo: {e}"

@app.route('/calculo-imc', methods=['GET'])
def rota_antiga():
    return "API IMC ativa!"



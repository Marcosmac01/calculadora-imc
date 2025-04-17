from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/calculo-imc", methods=["POST"])
def calcular_imc():
    data = request.get_json()
    peso = float(data["peso"])
    altura = float(data["altura"])
    imc = peso / (altura ** 2)
    return jsonify({"imc": round(imc, 2)})

@app.route("/", methods=["GET"])
def home():
    return "API IMC ativa!"

if __name__ == "__main__":
    app.run(debug=True)

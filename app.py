from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Flask está rodando."

@app.route("/disparar", methods=["POST"])
def disparar_bot():
    data = request.get_json()
    numero = data.get("numero")

    if not numero:
        return {"erro": "Número não fornecido"}, 400

    print(f"Recebido número: {numero}")

    # Executa script em Node.js passando o número como argumento
    subprocess.Popen(["node", "zapi-bot.js", numero])

    return {"status": "Bot iniciado"}, 200

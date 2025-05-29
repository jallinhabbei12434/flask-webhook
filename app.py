from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    numero = data.get("phone")
    print(f"Recebido: {numero}")
    return {"status": "ok"}

@app.route('/')
def home():
    return 'Flask está rodando.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)

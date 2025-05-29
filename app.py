from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return 'Flask está rodando.'

@app.route('/webhook', methods=['POST'])
def receber_webhook():
    dados = request.get_json()
    print('📥 Dados recebidos do n8n:')
    print(dados)

    # Aqui você pode salvar, processar ou responder
    return jsonify({'mensagem': 'Recebido com sucesso'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)

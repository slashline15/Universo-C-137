from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('_layouts\home.html')  # Certifique-se de que index.html está na pasta 'templates'


@app.route('/enviar-resposta', methods=['POST'])
def receber_resposta():
    # Recebe os dados enviados pelo formulário
    dados = request.json
    resposta = dados.get('resposta')
    
    # Aqui você pode processar a resposta
    print(f"Resposta recebida: {resposta}")
    
    # Responde para o front-end
    return jsonify({'mensagem': 'Resposta recebida com sucesso!'}), 200

if __name__ == '__main__':
    app.run(debug=True)

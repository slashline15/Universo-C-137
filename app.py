from flask import Flask, request, jsonify
import smtplib

app = Flask(__name__)

@app.route('/enviar-resposta', methods=['POST'])
def enviar_resposta():
    dados = request.json  # Recebe os dados do formulário
    resposta = dados.get('resposta')

    # Configuração do e-mail
    remetente = 'seuemail@gmail.com'
    senha = 'suasenha'
    destinatario = 'emaildestino@gmail.com'

    mensagem = f"Resposta recebida: {resposta}"

    try:
        # Envia o e-mail
        servidor = smtplib.SMTP('smtp.gmail.com', 587)
        servidor.starttls()
        servidor.login(remetente, senha)
        servidor.sendmail(remetente, destinatario, mensagem)
        servidor.quit()
        return jsonify({'mensagem': 'E-mail enviado com sucesso!'}), 200
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")
        return jsonify({'mensagem': 'Erro ao enviar e-mail.'}), 500

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

projeto = {
    "tempo_vermelho_via_1": 2500,
    "tempo_verde_via_1": 3000,
    "amarelo_piscante_via_1" : False,
    "tempo_vermelho_via_2": 3000,
    "tempo_verde_via_2":5000,
    "amarelo_piscante_via_2" : False,
    "iluminacao_ligada" : True,
    "carro_estacionado" : False
  }

@app.route('/')
def main():
    return "Bem vindo a API do Semáforo"

@app.route('/obterDados', methods=['GET'])
def obterProdutos() :
    return jsonify(projeto)

@app.route('/atualizarDados', methods=['PUT'])
def atualizar_dados():
    dados = request.get_json()
    if not dados:
        return jsonify({"error": "Nenhum dado enviado"}), 400

    for chave, valor in dados.items():
        if chave in projeto:
            projeto[chave] = valor
        else:
            return jsonify({"error": f"Chave inválida: {chave}"}), 400

    return jsonify(projeto)


if __name__ == '__main__':
   app.run()
   #app.run( port=5000, host='192.168.0.237', debug=True )

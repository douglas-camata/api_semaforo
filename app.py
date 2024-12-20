from flask import Flask, jsonify, request
from flask_cors import CORS

from flask_swagger_ui import get_swaggerui_blueprint
import os
import json

app = Flask(__name__)
CORS(app)

### Swagger configuration ###
SWAGGER_URL = '/docs'  # URL para acessar a documentação
API_URL = '/swagger.json'  # Caminho para o arquivo JSON de especificação Swagger

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  # Swagger UI URL
    API_URL,  # Swagger arquivo JSON URL
    config={  # Configurações adicionais do Swagger UI
        'app_name': "API Semaforo"
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

@app.route('/swagger.json')
def swagger_json():
    if os.path.exists("swagger_spec.json"):
        with open("swagger_spec.json", 'r') as json_file:
            swagger_spec = json.load(json_file)
            return swagger_spec
    else:
        return {}


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

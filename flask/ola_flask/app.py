from flask import Flask, jsonify, request
import json

app = Flask(__name__)

@app.route('/<int:id>')
def pessoa(id):
    return jsonify({'id': 1, 'nome': 'Rafeal'})

@app.route('/somaOld/<int:valor1>/<int:valor2>')
def somaOld(valor1, valor2):
    return jsonify({'soma': valor1 + valor2 })

@app.route('/soma', methods=['POST', 'GET'])
def soma():
    if request.method == 'POST':
        dados = json.loads(request.data)
        total = sum(dados['valores'])
    elif request.method == 'GET':
        total = 10 + 10
    return jsonify({ 'soma': total })

if __name__ == "__main__":
    app.run(debug=True)
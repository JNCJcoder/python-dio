from flask import Flask, jsonify, request
import json

app = Flask(__name__)

desenvolvedores = [
    {
        'nome': 'Rafaeal',
        'habilidades': ['Python', 'Flask']
    },
    {
        'nome': 'Jorge',
        'habilidades': ['Python', 'Flask', 'Django']
    }
]

@app.route('/dev/<int:id>')
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            dev = desenvolvedores[id]
        except IndexError:
            dev = {'status': 'falha', 'mensagem': 'ID não existe'}
        return jsonify(dev)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({ 'status': 'Sucesso', 'mensagem': 'Registro Excluido'})

@app.route('/dev/', methods=['POST', 'GET'])
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        desenvolvedores.append(dados)
        return jsonify({'status': 'Sucesso', 'mensagem': 'Registro Inserido'})
    elif request.method == 'GET':
        return jsonify(desenvolvedores)

if __name__ == '__main__':
    app.run()
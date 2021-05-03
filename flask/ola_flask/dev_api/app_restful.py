from flask import Flask, request
from flask_restful import Resource, Api
import json

app = Flask(__name__)
api = Api(app)

lista_habilidades = ['Python', 'Java', 'Flask', 'PHP']

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

class Desenvolvedor(Resource):
    def get(self, id):
        try:
            dev = desenvolvedores[id]
        except IndexError:
            dev = {'status': 'falha', 'mensagem': 'ID não existe'}
        return dev
    
    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados

    def delete(self, id):
        desenvolvedores.pop(id)
        return { 'status': 'Sucesso', 'mensagem': 'Registro Excluido'}

class ListaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores
    
    def post(self):
        dados = json.loads(request.data)
        desenvolvedores.append(dados)
        return {'status': 'Sucesso', 'mensagem': 'Registro Inserido'}

class Habilidades(Resource):
    def get(self):
        return lista_habilidades

api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(ListaDesenvolvedores, '/dev/')
api.add_resource(Habilidades, '/habilidades/')

if __name__ == '__main__':
    app.run(debug=True)
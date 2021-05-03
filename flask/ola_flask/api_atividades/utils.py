from models import Pessoas, Usuarios, db_session

def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()

def consulta_todos_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)

def insere_pessoa():
    pessoa = Pessoas(nome='Jorge', idade=21)
    pessoa.save()
    print(pessoa)

def consulta_pessoa():
    pessoa = Pessoas.query.all()
    print(pessoa)

def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Jorge').first() 
    pessoa.nome = 'Joao'
    pessoa.save()

def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Jorge').first()
    pessoa.delete()

if __name__ == '__main__':
    #insere_usuario('jorge', '123')
    #consulta_todos_usuarios()
    #insere_pessoa()
    #altera_pessoa()
    #exclui_pessoa()
    #consulta_pessoa()
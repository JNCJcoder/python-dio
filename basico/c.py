import shutil

def escrever_arquivo(texto):
    arquivo = open('teste.txt', 'w')
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(texto):
    arquivo = open('teste.txt', 'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo():
    arquivo = open('teste.txt', 'r')
    texto = arquivo.read()
    print(texto)


def media_notas(nome_arquivo):
    arquivo = open('teste.txt', 'w')
    texto = arquivo.read()
    aluno_nota = aluno_nota.split('\n')
    for x in aluno_nota:
        lista_notas = x.split(',')
        print(lista_notas[0])
        lista_notas.pop(0)
        print(lista_notas)
        media = lambda notas: sum([int(i) for i in notas]) / 4
        print(media(lista_notas))


def copia_arquivo(nome_arquivo):
    shutil.copy(nome_arquivo, "E:/")

def move_arquivo(nome_arquivo):
    shutil.move(nome_arquivo, "E:/")

if __name__ == "__main__":
    # escrever_arquivo('Primeira Linha. \n')
    # escrever_arquivo('Segunda Linha. \n')
    # atualizar_arquivo('Terceira Linha. \n')
    # media_notas(notas.txt)

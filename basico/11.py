
lista = [1, 10]

try:
    divisao = 10 / 1
    numero = lista[1]
    x = a
except BaseException as error:
    print('Error: {}'.format(error))
else:
    print("Executa quando não ocorre Except")
finally:
    print('Sempre Executa')
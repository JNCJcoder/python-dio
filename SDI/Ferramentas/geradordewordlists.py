import itertools

string = input("String a ser permutada: ")

resultado = itertools.permutations(string, len(string))

for word in resultado:
    print(''.join(word))
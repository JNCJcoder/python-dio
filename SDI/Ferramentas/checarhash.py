import hashlib

def gerarHash(arquivo):
    hash1 = hashlib.new('ripemd160')
    hash1.update(open(arquivo, 'rb').read())  

    return hash1


if __name__ == "__main__":
    Hash1 = gerarHash('a.txt')
    Hash2 = gerarHash('b.txt')

    if Hash1.digest() != Hash2.digest():
        print(f'O Arquivo1 é diferente do Arquivo2')
    else:
        print(f'O Arquivo1 é igual ao Arquivo2')
    
    print('O Hash do Arquivo1 é: ', Hash1.hexdigest())
    print('O Hash do Arquivo2 é: ', Hash2.hexdigest())
import random, string

def gerar_senha():
    TAMANHO = 16
    CHARS = string.ascii_letters + string.digits + 'çÇ!@#$%&()-=+,.;:/?'
    
    rnd = random.SystemRandom()

    senha = ''.join(rnd.choice(CHARS) for chars in range(TAMANHO))

    print(senha)

    return senha


if __name__ == "__main__":
    gerar_senha()
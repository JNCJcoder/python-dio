import socket
import sys

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as ex:
        print("A Conexão falhou")
        print("Erro: {}".format(ex))
        sys.exit()
    
    print("Socket criado com sucesso")

    HostAlvo = input("Digite o Host ou IP a ser conectado: ")
    PortaAlvo = input("Digite a Porta a ser conectada: ")

    try:
        s.connect((HostAlvo, int(PortaAlvo)))
        print("Cliente TCP conectado com Sucesso no host: " + HostAlvo + ":" + PortaAlvo)
    except socket.error as ex:
        print("Não foi possivel conectar no Host: " + HostAlvo + ":" + PortaAlvo)
        print("Erro: {}".format(ex))
        sys.exit()


if __name__ == "__main__":
    main()
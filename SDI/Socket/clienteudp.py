import socket
import sys

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    except socket.error as ex:
        print("A Conexão falhou")
        print("Erro: {}".format(ex))
        sys.exit()


    print("Ciente Socket Criado com Sucesso!!!")

    host = 'localhost'
    porta = 5433
    mensagem = 'Olá servidor firmeza?'

    try:
        print('Cliente: ' + mensagem)
        s.sendto(mensagem.encode(), (host, porta))

        dados, servidor = s.recvfrom(4096)

        dados = dados.decode()
        print('Cliente: ' + dados)
    finally:
        print('Cliente: Fechando a Conexão')
        s.close()

if __name__ == "__main__":
    main()
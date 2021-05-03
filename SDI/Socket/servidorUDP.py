import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Socket Criado com Sucesso')

HOST = 'localHOST'
PORTA = 5432

s.bind((HOST, PORTA))
MENSAGEM = 'Servidor: Oláaa Cliente e ai beleza?'

while True:
    dados, endereco = s.recvfrom(4096)
    
    if dados:
        print('Servidor enviando MENSAGEM...')
        s.sendto(dados + (MENSAGEM.encode()), endereco)


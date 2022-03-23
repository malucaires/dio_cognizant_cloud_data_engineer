import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #AF_INET conexão IP e SOCK_DRAM conexão UDP

print('Socket criado com sucesso!')

host = 'localhost'
port = 5432

s.bind((host, port))
mensagem = 'Servidor: Olá, cliente.'

while 1:
    dados, end = s.recvfrom(4896)

    if dados:
        print('Servidor enviando mensagem...')
        s.sendto(dados + (mensagem.encode()), end)

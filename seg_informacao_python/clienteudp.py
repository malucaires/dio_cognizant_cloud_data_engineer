import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print(f'Cliente Socket criado com sucesso!!!')

host = 'localhost'
porta = 5433
mensagem = 'Olá servidor!'

try:
    print(f'Cliente: {mensagem}')
    s.sendto(mensagem.encode(), (host, 5432))
    dados, servidor = s.recvfrom(5096)
    dados = dados.decode()
    print(f'Cliente: {dados}')
finally:
    print(f'Cliente: Fechando a conexão')
    s.close()
    

#Cria um Cliente TCP para testar uma conexão

import socket #faz o relacionamento com a placa de rede e SO
import sys #fornece acesso a algumas funções do interpretador

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print(f'A conexão falhou! Erro: {e}')
        sys.exit()
    print('Socket criado com sucesso')

    HostAlvo = input(f'Digite o Host ou Ip a ser conectado: ')
    PortaAlvo = input(f'Digite a porta a ser conectada: ')

    try:
        s.connect((HostAlvo, int(PortaAlvo)))
        print(f'Cliente TCP conectado com Sucesso no Host: {HostAlvo} e na Porta: {PortaAlvo}')
        s.shutdown(2) #Aguarda dois segundos para encerrar a conexão
    except socket.error as e:
        print(f'Não foi possível conectar no Host: {HostAlvo} e na Porta {PortaAlvo}')
        print(f'Erro: {e}')
        sys.exit()

if __name__ == '__main__':
    main()
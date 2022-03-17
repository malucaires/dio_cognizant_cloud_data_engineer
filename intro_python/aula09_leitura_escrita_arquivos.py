'''Cria funções para escrever, atualizar e ler um arquivo .txt'''

def escrever_arquivo(texto):
    arquivo = open('aula09.txt','w')
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(texto):
    arquivo = open('aula09.txt','a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo():
    arquivo = open('aula09.txt','r')
    texto = arquivo.read()
    print(texto)
    arquivo.close()

if __name__ == '__main__':
    escrever_arquivo('Primeira linha\n')
    atualizar_arquivo('Segunda linha')
    ler_arquivo()

print('Final do programa!')

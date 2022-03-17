'''Conta quantidade de letras de cada palavra em uma lista'''

def contador_letras(lista_palavras):
    contador = []
    for x in lista_palavras:
        quantidade = len(x)
        contador.append(quantidade)
    return contador
    # Com labda seria: contador_letras = lambda lista: [len(x) for x in lista]

if __name__ == '__main__':
    lista = ['banana','gato']
    print(contador_letras(lista))

print('Final do programa!')

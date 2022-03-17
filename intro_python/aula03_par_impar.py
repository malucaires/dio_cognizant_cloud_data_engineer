'''Recebe um número e retorna se é par ou ímpar'''

numero = int(input('Digite um valor: '))
resto = numero % 2

if resto == 0:
    print(f'O número {numero} é par')
else:
    print(f'O número {numero} é ímpar')

print('Fim do programa!')


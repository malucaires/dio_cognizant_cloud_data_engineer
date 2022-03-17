'''Recebe um valor do usuário e verifica se é primo'''

numero = int(input('Digite um valor: '))
div = 0

for i in range (1, numero+1):
    resto = numero % i
    if resto == 0:
        div += 1

if div == 2:
    print(f'O número {numero} é primo.')
else:
    print(f'O número {numero} não é primo.')

print('Final do programa!')

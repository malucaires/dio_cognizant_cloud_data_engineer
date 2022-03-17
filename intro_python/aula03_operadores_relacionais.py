'''Recebe dois números e verifica qual deles é maior'''

a = int(input(f'Digite o 1º valor: '))
b = int(input(f'Digite o 2º valor: '))

if a > b:
    print(f'O maior número é {a}.')
elif a == b:
    print(f'Os números são iguais e igual a {a}.')
else:
    print(f'O maior número é {b}.')

print('Final do programa!')

'''Recebe um valor N do usuário e retorna todos os números primos de 0 a N'''

numero = int(input('Digite um valor: '))

for num in range (numero):
    div = 0
    for x in range(1, num+1):
        resto = num % x
        if resto == 0:
            div += 1
    if div == 2:
        print(f'O número {num} é primo.')

print('Final do programa!')

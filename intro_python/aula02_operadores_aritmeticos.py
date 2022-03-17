'''Recebe dois números e retorna as operações aritméticas básicas:
soma, subtração, multiplicação, divisão e resto'''

a = int(input('Digite o 1º valor: '))
b = int(input('Digite o 2º valor: '))

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b

print(f'''Soma: {soma}.
Subtração: {subtracao}.
Multiplicação: {multiplicacao:.2f}.
Divisão: {divisao}.
Resto: {resto}.''')

print('Fim do programa!')

'''Calculadora de soma, subtração, multiplicação e divisão
utilizando labda'''

calculadora = {
    'soma': lambda a, b: a +b,
    'subtracao': lambda a,b: a-b,
    'multiplicacao': lambda a,b: a*b,
    'divisao': lambda a,b: a/b,
}

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
soma = calculadora['soma']
subtracao = calculadora['subtracao']
multiplicacao = calculadora['multiplicacao']
divisao = calculadora['divisao']

print(f'A soma é: {soma(n1, n2)}')
print(f'A subtração é: {subtracao(n1, n2)}')
print(f'A multiplicação é: {multiplicacao(n1, n2)}')
print(f'A divisão é: {divisao(n1, n2):.2f}')

print('Final do programa!')

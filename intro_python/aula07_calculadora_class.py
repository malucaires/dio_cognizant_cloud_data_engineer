'''Calculadora que recebe com dois números e retorna funções básicas
 como soma, subtração, multiplicação e divisão utilizando Classe e Função'''

class Calculadora:
    def __init__ (self, num1, num2):
        self.valor_a = num1
        self.valor_b = num2

    def soma(self):
        return self.valor_a + self.valor_b

    def subtracao(self):
        return self.valor_a - self.valor_b

    def multiplicacao(self):
        return self.valor_a * self.valor_b

    def divisao(self):
        return self.valor_a / self.valor_b

if __name__ == '__main__':
    numero1 = int(input('Digite o primeiro número: '))
    numero2 = int(input('Digite o segundo número: '))
    calculadora = Calculadora(numero1, numero2)
    print(f'A soma é: {calculadora.soma()}')
    print(f'A subtração é: {calculadora.subtracao()}')
    print(f'A multiplicação é: {calculadora.multiplicacao()}')
    print(f'A divisão é: {calculadora.divisao():.2f}')

print('Final do programa!')

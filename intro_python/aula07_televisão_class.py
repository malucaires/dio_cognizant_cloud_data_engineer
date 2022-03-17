'''Faz uma classe televisão que liga/desliga a televisão através
de um power e aumenta/diminui o número de um canal inicializado em 5'''

class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 5

    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

    def aumenta_canal(self):
        if self.ligada:
            self.canal += 1

    def diminui_canal(self):
        if self.ligada:
            self.canal -= 1

if __name__ == '__main__':
    televisao = Televisao()
    print(f'Televisão está ligada? {televisao.ligada}')
    televisao.power()
    print('Botão power acionado.')
    print(f'Televisão está ligada? {televisao.ligada}')
    print(f'Canal atual: {televisao.canal}')
    televisao.aumenta_canal()
    print('Botão aumenta canal acionado.')
    print(f'Canal atual: {televisao.canal}')

print('Final do programa!')

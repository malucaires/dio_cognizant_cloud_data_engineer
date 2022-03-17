'''Faz tratamento de erros para verificar se um valor recebido está entre 0 e 10'''

class Error(Exception):
    pass

class InputError(Error):
    def __init__(self, message):
        self.message = message

while True:
    try:
        x = int(input('Entre com uma nota de 0 a 10: '))
        print(x)
        if x > 10:
            raise InputError('Nota não pode ser maior que 10')
        elif x < 0:
            raise InputError('Nota não pode ser menor que 0')
        break
    except ValueError:
        print('Valor inválido. Deve-se digitar um número')
    except InputError as ex:
        print(ex)

print('Final do programa!')

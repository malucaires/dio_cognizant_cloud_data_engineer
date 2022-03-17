'''Retorna os dados de um cep a partir de uma biblioteca'''

import requests

r = requests.get('http://viacep.com.br/ws/01001000/json/')

dados_cep = r.json()
print(f'O CEP é: {dados_cep["cep"]}')
print(f'A cidade é: {dados_cep["localidade"]}')
print(f'O estado é: {dados_cep["uf"]}')

print('Final do programa!')

'''Recebe quatro notas de um aluno, valida se está entre 0 e 10
 e retorna a média. Script feito com while.'''

n1 = int(input('Nota do primeiro bimestre [entre 0 e 10]: '))
while n1 < 0 or n1 > 10:
    n1 = int(input('Valor incorreto. Nota do primeiro bimestre [entre 0 e 10]: '))
n2 = int(input('Nota do segundo bimestre [entre 0 e 10]: '))
while n2 < 0 or n2 > 10:
    n2 = int(input('Valor incorreto. Nota do segundo bimestre [entre 0 e 10]: '))
n3 = int(input('Nota do terceiro bimestre [entre 0 e 10]: '))
while n3 < 0 or n3 > 10:
    n3 = int(input('Valor incorreto. Nota do terceiro bimestre [entre 0 e 10]: '))
n4 = int(input('Nota do quarto bimestre [entre 0 e 10]: '))
while n4 < 0 or n4 > 10:
    n4 = int(input('Valor incorreto. Nota do quarto bimestre [entre 0 e 10]: '))
media = (n1 + n2 + n3 + n4) / 4
print(f'''As notas digitadas foram: {n1}, {n2}, {n3} e {n4}.
A média do aluno é de {media}''')

print('Final do programa!')

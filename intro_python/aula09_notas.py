'''Recebe um arquivo .txt com notas de alunos em uma lista e retorna a média'''

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo,'r')
    aluno_nota = arquivo.read()
    aluno_nota = aluno_nota.split('\n')
    lista_media = []
    for x in aluno_nota:
        lista_notas = x.split(',')
        aluno = lista_notas[0]
        lista_notas.pop(0)
        media = lambda notas: sum([int(i) for i in notas ]) / 3
        lista_media.append({aluno:media(lista_notas)})
    return lista_media

print(media_notas('aula09_notas.txt'))

print('Final do programa!')

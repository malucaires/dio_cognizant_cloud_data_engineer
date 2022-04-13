def fatorial(num, show=False):
    """
    Calcula o fatorial de um número
    :param num: número a ser calculado
    :param show: (opcional) mostra memória de cálculo
    :return: valor faotiral de um número
    """
    fatorial = 1
    for c in range(num, 0, -1):
        fatorial *= c
        if show == True and c != 1:
            print(f'{c} x', end=' ')
        elif show == True and c == 1:
            print(f'{c} =', end=' ')
    return fatorial

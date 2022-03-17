'''Recebe dois conjuntos e faz operações'''

conjuntoa = {1, 2, 3, 4, 5}
conjuntob = {5, 6, 7, 8}
conjuntoc = {6,7}

conjunto_uniao = conjuntoa.union(conjuntob)
print(f'Conjunto União: {conjunto_uniao}')

conjunto_interseccao = conjuntoa.intersection(conjuntob)
print(f'Conjunto Interseção: {conjunto_interseccao}')

conjunto_diferenca1 = conjuntoa.difference(conjuntob)
print(f'Conjunto Diferença (A-B): {conjunto_diferenca1}')

conjunto_diferenca2 = conjuntob.difference(conjuntoa)
print(f'Conjunto Diferença (B-A): {conjunto_diferenca2}')

conjunto_diff_simetrica = conjuntoa.symmetric_difference(conjuntob)
print(f'Diferença Simétrica: {conjunto_diff_simetrica}')

conjunto_subset = conjuntoc.issubset(conjuntob)
print(f'O conjunto C está contido em B? {conjunto_subset}')

conjunto_superset = conjuntob.issuperset(conjuntoc)
print(f'O conjunto B contém C? {conjunto_superset}')

print('Final do programa!')

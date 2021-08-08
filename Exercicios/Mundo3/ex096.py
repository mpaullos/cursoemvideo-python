def area(a,b):
    operação = a*b
    print(f'A area de um terreno de {larg}X{comp} é de {operação}m².')

# PROGRAMA PRINCIPAL
print('Controle de Terrenos')
print('-' *len('Controle de Terrenos'))
larg = float(input('LARGURA (m): '))
comp = float(input('COMPRIMENTO (m): '))
area(larg,comp)

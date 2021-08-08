print('-' * 40)
print('{:^40}'.format('MATERIAIS UFS'))
print('-' * 40)
listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Transferidor', 4.20,
            'Compasso', 9.85,
            'Mochila da Nike', 157.90,
            'Canetas', 3,
            'Visual Studio', 0)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-' * 40)

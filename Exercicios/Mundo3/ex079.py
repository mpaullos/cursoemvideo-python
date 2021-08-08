números = list()
while True:
    num = int(input('Digite um valor:'))
    if num not in números:
        números.append(num)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado não vou adicionar')
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer conitnuar? [S/N]')).strip().upper()[0]
    if continuar == 'N':
        break
print('-' * 30)
números.sort()
print(f'Você digitou os números {números}')

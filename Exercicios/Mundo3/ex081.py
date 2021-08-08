números = list()
contador = 0
while True:
    n = int(input('Digite um número: '))
    números.append(n)
    contador += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if continuar == 'N':
        break
números.sort(reverse=True)
print('=*-'*30)
print('Voce digitou {} números'.format(contador))
print(f'Os valores em ordem descrescente são {números}')
if 5 in números:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não faz parte da lista')
num = list()
pares = list()
impares = list()
while True:
    num.append(int(input('Digite um número: ')))
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar in 'N':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print('=*=' * 30)
print(f'A lista completa é {num}')
print(f'Os números pares são {pares}')
print(f'Os números impares são {impares}')

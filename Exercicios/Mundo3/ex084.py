dados = []
princ = []
cont = 0
maior = menor = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(princ) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        elif dados[1] < menor:
            menor = dados[1]
    princ.append(dados[:])
    dados.clear()
    cont += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'A quantidade de pessoas foi {cont}')
print(f'O maior peso foi {maior} de ', end='')
for p in princ:
    if p[1] == maior:
        print(f'{p[0]}')
print(f'O menor peso foi {menor} de ', end='')
for p in princ:
    if p[1] == menor:
        print(f'{p[0]}')

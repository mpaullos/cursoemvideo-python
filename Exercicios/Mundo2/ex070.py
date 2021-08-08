total = maisqmil = menor = cont = 0
barato = ''
print('-' * 30)
print('{:^30}'.format('LOJA MARCOS EXPRESS'))
print('-' * 30)
while True:
    produto = str(input('Nome do Produto: '))
    preço = float(input('Preço R$'))
    total += preço
    cont += 1
    if preço > 1000:
        maisqmil += 1
    if cont == 1:
        menor = preço
        barato = produto
    else:
        if preço < menor:
            menor = preço
            barato = produto
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if continuar == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {maisqmil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')

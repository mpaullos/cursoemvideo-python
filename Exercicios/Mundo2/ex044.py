print('{:*^40}'.format('\033[0;35mARMARINHO SANTANA\033[m'))
print('{:*^29}'.format('Tudo para o seu artesanato!'))
preço = float(input('\nPreço das compras: R$'))
print('''\nFORMAS DE PAGAMENTO
[ 1 ] à vista no dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual é a opção? '))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print('\nSua compra será parcelada em 2x de {:.2f}'.format(parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totparcela = int(input('Quantas parcelas? '))
    parcela = total / totparcela
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS.'.format(totparcela,parcela))
else:
    total = preço
    print('\033[0;31mOPÇÃO INVALIDA DE PAGAMENTO. Tente novamente\033[m')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço,total))

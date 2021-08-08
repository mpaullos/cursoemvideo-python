import moeda
preco = float(input('Digite o preço: R$'))
print(f'A metade de {preco} é {moeda.metade(preco)}')
print('O dobro de {} é {}'.format(preco, moeda.dobro(preco)))
print(f'Aumentando 10% de {preco} temos {moeda.aumenta(preco)}')
print(f'Reduzindo 13% de {preco} temos {moeda.diminuir(preco)}')

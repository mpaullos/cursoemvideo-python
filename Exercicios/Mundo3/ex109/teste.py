from ex109 import moeda
preco = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.virgula(preco)} é {moeda.metade(preco, True)}')
print('O dobro de {} é {}'.format(moeda.virgula(preco), moeda.dobro(preco, True)))
print(f'Aumentando 10% de {moeda.virgula(preco)} temos {moeda.aumenta(preco, True)}')
print(f'Reduzindo 13% de {moeda.virgula(preco)} temos {moeda.diminuir(preco, True)}')

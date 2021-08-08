from ex108 import moeda
preco = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.virgula(preco)} é {moeda.virgula(moeda.metade(preco))}')
print('O dobro de {} é {}'.format(moeda.virgula(preco), moeda.virgula(moeda.dobro(preco))))
print(f'Aumentando 10% de {moeda.virgula(preco)} temos {moeda.virgula(moeda.aumenta(preco))}')
print(f'Reduzindo 13% de {moeda.virgula(preco)} temos {moeda.virgula(moeda.diminuir(preco))}')

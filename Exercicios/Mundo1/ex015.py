alug= float(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
dia = alug * 60
quilometros = km * 0.15
total = dia + quilometros
print('O total a pagar é de R${:.2f}'.format(total))
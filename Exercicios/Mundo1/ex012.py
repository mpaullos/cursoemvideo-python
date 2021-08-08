produto = float(input('Qual é o preco do produto? R$'))
desconto = produto -(produto * 0.05)
print('O produto que custava R${}, na promoção com desconto de 5% vai custar R$ {:.2f}'.format(produto,desconto))
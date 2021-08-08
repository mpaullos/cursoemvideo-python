casa = float(input('Qual o valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestacao = casa / (anos*12)
min = salario * 30/100
print('Para pegar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(casa,anos,prestacao))
if prestacao >= min:
    print('Emprestimo NEGADO!')
else:
    print('Emprestimo pode ser CONCEDIDO!')
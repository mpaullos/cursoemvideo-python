contagem = 0
soma = 0
for c in range (1,501,2):
    if c % 3 == 0:
        contagem = contagem + 1
        soma = soma + c
print('A soma de todos os {} números resultou em {}'.format(contagem,soma))
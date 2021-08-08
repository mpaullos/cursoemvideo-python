soma = contagem = 0
while True:
    número = int(input('Digite um valor (999 para parar): '))
    if número == 999:
        break
    soma += número
    contagem += 1
print(f'A soma dos {contagem} valores foi {soma}!')

resp = 'S'
soma = quantidade = media = maior = menor = 0
while resp in 'Ss':
    n = int(input('Digite um número: '))
    soma += n
    quantidade += 1
    if quantidade == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
media = soma / quantidade
print('Você digitou {} números e a média foi {}'.format(quantidade, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))

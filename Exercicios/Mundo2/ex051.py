primeiro = int(input('Primeiro termo: '))
razão = int(input('RAZÃO: '))
décimo = primeiro + (10 -1 ) * razão
for c in range (primeiro, décimo + razão, razão):
    print('{}'.format(c),end=' →')
print('ACABOU')
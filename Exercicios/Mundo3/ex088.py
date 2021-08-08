from random import randint
from time import sleep
lista = list()
jogos = list()
print('-' * 40)
print('{:^40}'.format('MEGA SENA PALPITE'))
print('-' * 40)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
total = 1
while total <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
if quant == 1:
    print('-=' * 3, f'SORTEANDO {quant} JOGO ', '-=' * 3)
else:
    print('-=' * 3,f'SORTEANDO {quant} JOGOS ', '-=' * 3)
print(f'Os números sorteados foram:')
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('-=' * 5, '< BOA SORTE!!! >', '-=' *5)
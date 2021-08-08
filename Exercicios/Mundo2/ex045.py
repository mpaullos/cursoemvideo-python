from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''SUAS OPÇÕES
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('Pedra')
sleep(1)
print('Papel')
sleep(1)
print('Tesouraaa')
print('=-'*12)
print('Computador jogou {}'.format(itens[computador]))
if jogador >2:
    print('\033[0;31mOPÇÃO INVALIDA\033[m')
    exit()
print('Jogador jogou {}'.format(itens[jogador]))
print('=-'*12)

if computador == 0: #COMPUTADOR JOGOU PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCEU')
    elif jogador == 2:
       print('COMPUTADOR VENCEU')

elif computador == 1: #COMPUTADOR JOGOU PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCEU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCEU ')
elif computador == 2: #COMPUTADOR JOGOU TESOURA
    if jogador == 0:
        print('JOGADOR VENCEU')
    elif jogador == 1:
        print('COMPUTADOR VENCEU')
    elif jogador == 2:
        print('EMPATE')

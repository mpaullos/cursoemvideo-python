from random import randint
computador = randint(0,5)
design = '=--' * 18
print(design)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print(design)
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
if jogador == computador:
    print('PARABÉNS! Você ganhou!!!')
else:
    print('ERROU! Eu pensei no número {} e não no {}'.format(computador,jogador))

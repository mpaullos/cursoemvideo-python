from random import randint

v = 0
print('=-*' * 10)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-*' * 10)
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
        print('-' * 30)
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total},', end=' ')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    if escolha == 'P':
        if total % 2 == 0:
            v += 1
            print('você VENCEU!')
            print('=-' * 10)
        else:
            print('você PERDEU!')
            break
    elif escolha == 'I':
        if total % 2 != 0:
            v += 1
            print('você VENCEU!')
        else:
            print('você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes')

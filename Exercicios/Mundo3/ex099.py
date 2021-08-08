from time import sleep


def maior(*num):
    cont = maior = 0
    print('-=' * 30)
    print('Analisando os valores passados')
    for valor in num:
        print(f'{valor} ', end='')
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} números ao todo.')
    print(f'O maior valor informado foi {maior}.')


# Programa principal
maior(2, 9, 4, 5, 7, 1)
maior(100, 23, 8, 0, 14, 99, 101)
maior(1, 2)
maior(0)
maior()

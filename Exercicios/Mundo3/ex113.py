def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO: Por favor, digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0;31mERRO: Usuáio preferiu não, digitar um número inteiro válido.\033[m')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            valor = float(input(msg))
        except (ValueError,TypeError):
            print('\033[0;31mERRO: Por favor, digite um número real válido.\033[m')
        except KeyboardInterrupt:
            print('\033[0;31mERRO: Usuário preferiu não digitar um valor.\033[m')
            return 0
        else:
            return valor

n1 = leiaInt('Digite um número inteiro: ')
n2 = leiaFloat ('Digite um número real: ')
print(f'O número inteiro digitado foi {n1} e o número real foi {n2}')

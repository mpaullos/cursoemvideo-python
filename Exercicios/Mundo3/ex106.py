from time import sleep

c = ('\033[m',  # apaga
     '\033[0;30;41m',  # 0  vermelho
     '\033[0;30;42m',  # 1 verde
     '\033[0;30;43m',  # 2 amarelo
     '\033[0;30;44m',  # 3 azul
     '\033[0;30;45m',  # 4 rosa
     '\033[7;30m')     # 5 branco


def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[5], end='')
    help(com)
    print(c[5], end='')
    sleep(2)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('-*-' * tam)
    print(f'  {msg}')
    print('-*-' * tam)
    print(c[0], end='')
    print('-' * tam)
    print(c[0], end='')
    sleep(1)


# Programa Principal
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PYHELP', 2)
    comando = str(input("Função ou Biblioteca > "))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!', 1)

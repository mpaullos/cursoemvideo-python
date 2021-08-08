def metade(n=0, formato=False):
    '''
    -> CALCULA A METADE DE UM DETERMINADO PRECO
    RETORNANDO O RESULTADO FORMATADO
    :param n: O preço que quer registrar
    :param formato: adiciona virgula ou não ao seu preço
    :return: A metade do valor, com ou sem formato.
    '''
    k = n / 2
    return k if not formato else virgula(k)


def dobro(n=0, formato=False):
    res = n * 2
    return res if not formato else virgula(res)


def aumenta(n=0, formato=False):
    dez = (n * 0.10) + n
    return dez if formato is False else virgula(dez)


def diminuir(n=0, formato=False):
    reduz = n - (n * 0.13)
    return reduz if formato is False else virgula(reduz)


def virgula(n=0, virgula='R$'):
    return f'{virgula}{n:.2f}'.replace('.', ',')


def resumo(n=0):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{virgula(n)}')
    print(f'Metade do preco: \t{metade(n, True)}')
    print(f'10% de aumento: \t{aumenta(n, True)}')
    print(f'13% de redução: \t{diminuir(n, True)}')
    print('-' * 30)

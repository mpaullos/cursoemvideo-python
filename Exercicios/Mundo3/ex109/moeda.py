def metade(n=0, formato=False):
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

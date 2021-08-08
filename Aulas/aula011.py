# print('\033[0;35;40mOla Mundo\033[m')
# a = 3
# b = 5
# print('Os valores são \033[1;32m{}\033[m e \033[4;035m{}'.format(a,b))

n1 = 1
n2 = 8
cores = {'limpa': '\033[m', 'azul': '\033[7;30;44m', 'amarelo': '\033[0;033m'}
print('Os valores são {}{}{} e {}{}{}'.format(cores['azul'], n1, cores['limpa'], cores['amarelo'], n2, cores['limpa']))


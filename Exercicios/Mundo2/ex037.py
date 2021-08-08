numero = int(input('\033[1;34mDigite um número inteiro: '))
print('\033[0;33m=-*\033[m'*12)
print('\033[1;31mEscolha uma das bases para coversão:\033[m')
print('\033[2;32m[ 1 ] Converter para BINÁRIO')
print('[ 2 ] Converter para OCTAL')
print('[ 3 ] Converter para HEXADECIMAL\033[m')
print('\033[0;33m=-*\033[m'*12)
opção = int(input('Sua opção: '))
if opção == 1:
    print('\033[0;30;44m{} convertido em BINÁRIO é igual a {}\033[m'.format(numero,bin(numero)[2:]))
elif opção == 2:
    print('\033[0;30;44m{} convertido em OCTAL é igual a {}\033[m'.format(numero,oct(numero)[2:]))
elif opção ==3 :
    print('\033[0;30;44m{} convertido em HEXADECIMAL é igual a {}\033[m'.format(numero,hex(numero)[2:]))
else:
    print('\033[0;31mOPÇÃO INVALIDA!!!\033[m')
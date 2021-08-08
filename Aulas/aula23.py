# try:
#    a = int(input('Numerador: '))
#    b = int(input('Denominador: '))
#    r = a / b
# except Exception as erro:
#    print(f'Infelizmente tivemos um problema :(\nO problema encontrado foi {erro.__class__}')
# else:
#    print(f'O resultado foi {r:.1f}')
# finally:
#    print('Volte sempre! Muito obrigado!')

try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possivel dividir um número por zero!')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__class__}')
else:
    print(f'O resultado foi {r:.1f}')
finally:
    print('Volte sempre! Muito obrigado!')

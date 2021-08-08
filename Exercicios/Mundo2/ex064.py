n = cont = soma = 0
n = int(input('Digite um número, caso queira parar digite 999: '))
while n != 999:
    soma += n
    cont+=1
    n = int(input('Digite um número, caso queira parar digite 999: '))
print('Você digitou {} números e a soma entre eles foi {}'.format(cont,soma))

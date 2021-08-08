from uteis import numeros

# from uteis import fatorial, dobro, triplo
num = int(input('Digite um número para ver o fatorial: '))
fat = numeros.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {numeros.dobro(num)}')
print(f'O triplo de {num} é {numeros.triplo(num)}')

# teste = list()
# teste.append('Marcos')
# teste.append(24)
# galera = list()
# galera.append(teste[:])
# teste[0] = 'Maria'
# teste[1] = 22
# galera.append(teste)
# print(galera)

#galera = [['Marcos', 24], ['Ana', 20], ['Vanessa', 23], ['Ariana', 27]]
#for c in galera:
#    print(f'{c[0]} tem {c[1]} anos de idade')
galera = list()
dado = list()
maior = menor = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        maior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        menor += 1
print(f'Temos {maior} maiores e {menor} menores de idade.')
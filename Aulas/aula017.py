# num = [2, 5, 9, 1]
# num[2] = 3
# num.append(7)
# num.sort(reverse=True)
# num.insert(2, 2)
# num.remove(2)
# if 5 in num:
#    num.remove(5)
# else:
#    print('Não encontrado')
# print(num)
# print(f'Essa lista tem {len(num)} elementos')

valores = list()
valores.append(5)
valores.append(9)
valores.append(9)
valores.append(4)
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista')

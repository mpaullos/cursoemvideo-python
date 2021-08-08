# pessoas ={'nome': 'Marcos', 'Sexo': 'M', 'Idade': 24}
# print(f'O {pessoas["nome"]} tem {pessoas["Idade"]} anos')
# del pessoas ['sexo']
# pessoas['Peso'] = 60
# print(pessoas.keys())
# print(pessoas.values())
# print(pessoas.items())
# for k, v in pessoas.items():
#    print(f'{k} = {v}')

# brasil = []
# estado1 = {'uf': 'Sergipe', 'sigla': 'SE'}
# estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
# brasil.append(estado1)
# brasil.append(estado2)
# print(brasil[0]['uf'])

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()

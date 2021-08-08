#nome = str(input('Digite o seu nome? '))
#if nome == 'Marcos':
    #print('Que nome lindo você tem')
#else:
    #print('Que nome tão normal!')
#print('Bom dia, {}!'.format(nome))


n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
m = (n1+n2)/2
print('A sua média foi {}'.format(m))
if m >= 6.0:
    print('Parabéns!!!')
else:
    print('Estude mais!!!')
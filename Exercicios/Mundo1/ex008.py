distancia = float (input ('Uma distância em metros: '))
km = distancia /1000
hm = distancia /100
dam = distancia /10
dc = distancia *10
cm = distancia *100
mm = distancia * 1000

print('A medida de {:.1f}m corresponde a'.format (distancia))
print('{}km'.format(km))
print('{}hm'.format(hm))
print('{}dam'.format(dam))
print('{:.0f}dc'.format(dc))
print('{:.0f}cm'.format(cm))
print('{:.0f}mm'.format(mm))
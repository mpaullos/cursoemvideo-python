larg = float(input ('Largura da parede: '))
alt= float(input ('Altura da parede: '))
area = larg * alt
mp = (larg * alt)/2

print('Sua parede tem a dimensão de {}x{} e sua área é de {}m²\nPara pintar essa parede você precisará de {}l de tinta. '.format(larg,alt,area,mp))
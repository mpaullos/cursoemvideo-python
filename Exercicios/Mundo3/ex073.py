times = ('Flamengo', 'Internacional', 'Atlético-MG', 'São Paulo',
         'Fluminese', 'Grêmio', 'Palmeiras', 'Santos', 'Athletico-PR',
         'Bragantino', 'Ceará SC', 'Corinthians', 'Atlético-GO', 'Bahia',
         'Sport Recife', 'Fortaleza', 'Vasco da Gama', 'Goiás',
         'Coritiba', 'Botafogo')
print('-=' * 15)
print(f'Lista de Times do Brasileirão: {times}')
print('-=' * 15)
print(f'Os 5 primeiros são {times[0:5]}')
print('-=' * 15)
print(f'Os 4 últimos são {times[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfábetica {sorted(times)}')
print('-=' * 15)
print(f'O Flamengo está na {times.index("Flamengo") + 1}ª posição')

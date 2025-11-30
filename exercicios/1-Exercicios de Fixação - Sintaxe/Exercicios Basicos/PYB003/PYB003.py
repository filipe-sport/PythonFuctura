dist = float(input('Entre com a distância percorrida em km: '))
tempo = float(input('Entre com o tempo gasto para percorrer a distância: '))

velMedia = (dist / tempo) * 3.6

print(f'Logo a velocidade média é em m/s: {velMedia:.2f}')

temp = float(input('Entre com a temperatura atual: '))
umid = float(input('Entre com a umidade atual: '))

if(20 <= temp <= 30 and 30 <= umid <= 60):
    print('Clima agradável')
elif(temp > 30 or umid > 70):
    print('Clima desconfortável')
elif(temp < 15 or umid < 20):
    print('Condições extremas')
else:
    print('Clima neutro')
tempC = float(input('Entre com a temperatura em Celsius: '))
opcao = input('Entre com 1 - Fahrenheit ou 2 - Kelvin: ')

tempF = (tempC *1.8)+32
tempK = tempC + 273.15

if opcao == '1':
    print(f'A temperatura em Fahrenheit é: {tempF}°F')
if opcao == '2':
    print(f'A temperatura em Kelvin é: {tempK}K')


dist = float(input('Entre com a distência a ser pecorrida na viagem: '))
preco = float(input('Entre com o valor do litro da gasolina: '))
consumo = float(input('Entre com o consumo (km/l) do veículo: '))

total = (dist / consumo) * preco

print(f'O valor total a ser gasto com combustível é de: {total} ')
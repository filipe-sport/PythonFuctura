marcaCarro = input('Qual a marca do carro? ')
corCarro = input('Qual a cor do carro? ')
anoCarro = input('Qual o ano do carro? ')
valorCompra = float(input('Por quanto o carro foi comprado? '))
tempoVenda = int(input('Quantos anos pretende ficar com o carro? '))
kmViagem = float(input('Qual a distância que o veículo irá percorrer na viagem? '))
consumoVeiculo = float(input('Qual o consumo médio do veículo? '))

valorDesvalorizado = valorCompra * (0.9) ** tempoVenda
print(f'{valorDesvalorizado:.2f}')
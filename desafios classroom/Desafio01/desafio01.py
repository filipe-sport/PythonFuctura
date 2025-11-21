marcaCarro = input('Qual a marca do carro? ')
corCarro = input('Qual a cor do carro? ')
anoCarro = input('Qual o ano do carro? ')
valorCompra = float(input('Por quanto o carro foi comprado? '))
tempoVenda = int(input('Quantos anos pretende ficar com o carro? '))

valorDesvalorizado = valorCompra * (0.9) ** tempoVenda
print(f'O veículo após {tempoVenda}anos, terá seu valor estimado em R$ {valorDesvalorizado:.2f}')

kmViagem = float(input('Qual a distância que o veículo irá percorrer na próxima viagem? '))
consumoVeiculo = float(input('Qual o consumo médio em km/l atual do veículo? '))

qtdComb = kmViagem/consumoVeiculo
custoComb = qtdComb * 6.50

print(f'Para a viagem de {kmViagem} serão necessários {qtdComb:.2f} totalizando {custoComb:.2f} ')




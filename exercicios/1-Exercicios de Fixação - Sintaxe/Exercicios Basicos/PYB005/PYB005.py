valorEmp = float(input('Qual o valor do empréstimo: '))
taxaJuros = float(input('Entre com a taxa de juros mensal: '))
numMeses = int(input('Entre com o número de meses: '))

valorParcela = (valorEmp + (valorEmp * (taxaJuros/100))) / numMeses

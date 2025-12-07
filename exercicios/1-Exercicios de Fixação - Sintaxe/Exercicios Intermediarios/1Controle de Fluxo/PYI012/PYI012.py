peso = float(input('Entre com seu peso: '))
altura = float(input('Entre com sua altura: '))
imc = peso * (pow(altura))

if imc <= 18.5:
    print('Abaixo do peso!!')
elif 18.5 < imc <= 24.9:
    print('Peso normal!!')
elif 25 <= imc <= 29.9:
    print('Sobrepeso!!')
elif 30 <= imc <= 34.9:
    print('Obesidade grau I')
elif 35 <= imc <= 39.9:
    print('Obesidade grau II')
else:
    print('Obesidade grau III')
      
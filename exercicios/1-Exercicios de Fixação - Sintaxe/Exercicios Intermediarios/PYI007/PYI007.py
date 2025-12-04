n1 = int(input('Entre com o primeiro numero inteiro: '))
n2 = int(input('Entre com o segundo numero inteiro: '))
operador = str(input('Entre com a operação (+ - * /): '))

if operador == '+':
    print(f'A soma de n1 {operador} n2 é: {n1+n2} ')
elif operador == '-':
    print(f'A diferença de n1 {operador} n2 é: {n1-n2} ')
elif operador == '*':
    print(f'A multiplicação de n1 {operador} n2 é: {n1*n2} ')
elif operador == '/':
    print(f'A divisão de n1 {operador} n2 é: {n1/n2} ')
else: 
    print('Operador Inválido')
    
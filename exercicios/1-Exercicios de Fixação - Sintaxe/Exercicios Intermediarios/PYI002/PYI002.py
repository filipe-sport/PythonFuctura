num1 = int(input('Entre com o primeiro numero inteiro'))
num2 = int(input('Entre com o segundo numero inteiro: '))

if num1 > num2:
    print(f'O numero {num1} é o maior')
elif num2 > num1:
    print(f'O numero {num2} é o maior')
else:
    print('Os números são iguais.')
num = int(input('Entre com um número inteiro: '))
num_Max = num
num_Min = num

while num != 0:
    num = int(input('Entre com um numero inteiro: '))
    if num != 0:
        if(num >= num_Max):
            num_Max = num
        if(num <= num_Min):
            num_Min = num
    else:
        print(f'O maior número digitado foi {num_Max}, e o menor foi {num_Min}')

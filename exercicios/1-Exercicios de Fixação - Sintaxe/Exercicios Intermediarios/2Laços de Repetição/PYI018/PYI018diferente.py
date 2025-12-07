num = int(input('Entre com um número inteiro: '))
num_string = str(num)
soma=0
tamanho=len(num_string)
i=0
while ( tamanho > 0):
    soma += int(num_string[i])
    i += 1
    tamanho += -1

print(soma)

soma = 0
cont = 0
while True:
    num = int(input('Entre com um número: '))
    if num < 0:
        break
    else:
        soma +=num
        cont+=1
        media = soma/cont
print(f'A média dos numeros positivos digitados foi {media}')
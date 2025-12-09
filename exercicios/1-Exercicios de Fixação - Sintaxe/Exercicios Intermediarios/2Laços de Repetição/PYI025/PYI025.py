num = int(input('Entre com um número: '))
cont = 0
while num > 0:
    if num > 0:
        num = int(input('Entre com um número: '))
        soma +=num
        cont+=1
        media = soma/cont
    else:
        break
print(f'A média dos numeros positivos digitados foi {media}')
    



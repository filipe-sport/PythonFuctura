idade = int(input('Entre com sua idade: '))

if idade < 16:
    print('Você não pode votar!!!')
elif (16 <= idade < 18) or (idade >= 70):
    print('Seu voto é facultativo!!')
else:
    print('Seu voto é obrigatório!!')
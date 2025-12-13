import random
while True:
    computador = random.randint(1,10)
    usuario = int(input('Entre com o numero sorteado: '))

    if usuario > computador:
        print('O número digitado é Muito Alto!!')
    elif usuario < computador:
        print('O número digitado é Muito Baixo!!')
    else:
        print('Parabéns, você acertou!!')
        break
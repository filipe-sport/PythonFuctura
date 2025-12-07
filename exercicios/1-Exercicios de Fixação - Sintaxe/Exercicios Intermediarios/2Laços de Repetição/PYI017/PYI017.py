import random

computador = random.randint(1,100)

jogador = int(input('Entre com seu palpite entre 1 a 100: '))

while (jogador != computador):
    print('Não foi dessa vez!!!')
    print(f'O computador jogou {computador}')
    jogador = int(input('Entre com um novo palpite: '))

print('Você acertou!!!')
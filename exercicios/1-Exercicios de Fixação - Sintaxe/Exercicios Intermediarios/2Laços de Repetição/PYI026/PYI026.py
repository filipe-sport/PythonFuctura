num = int(input('Entre com um número inteiro: '))

for c in range(1, num + 1):
    if num % c == 0:
        print(c)

tup1 = (1,2,3,4)
tup2 = (5,6,7,8)
tup_total = tup1 + tup2

print(tup_total)

print(len(tup_total))
print(max(tup_total))
print(min(tup_total))

usuario = int(input('Entre com um número inteiro: '))

if usuario in tup_total:
    print(f'O número digitado está na tupla ')
else:
    print('O numero digitado não está na tupla')
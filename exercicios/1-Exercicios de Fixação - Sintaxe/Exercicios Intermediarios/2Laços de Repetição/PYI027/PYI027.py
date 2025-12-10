text = input('Entre com um texto: ')

vogais = ('a','e','i','o','u')
cont = 0
for c in text:
    for i in vogais:
        if c == i:
            cont+=1

print(cont)


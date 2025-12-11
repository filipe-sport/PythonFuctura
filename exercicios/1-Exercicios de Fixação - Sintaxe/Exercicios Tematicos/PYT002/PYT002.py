frutas = []
qtd_Frutas = []
preco_Quilos = []
promocoes =[]

for enter in range (0,4):
    fruta = input('Entre com a fruta: ')
    frutas.append(fruta)
    qtdFruta = float(input('Entre com a quantidade em estoque: '))
    qtd_Frutas.append(qtdFruta)
    precoQuilo = float(input('Entre com o preco/kg: '))
    preco_Quilos.append(precoQuilo)
    promocao = bool(input('Entre True ou False: '))
    promocoes.append(promocao)

for i in range(0,4):
    print(f'Fruta   Quantidade  Preço/Kg    Promoção')
    print(f'{frutas[i]}' f'{qtd_Frutas[i]}' f'{preco_Quilos}' f'{promocoes}')
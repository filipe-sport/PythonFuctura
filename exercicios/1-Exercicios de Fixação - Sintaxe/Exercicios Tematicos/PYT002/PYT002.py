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
    promocao = input('Entre True ou False: ')
    print(promocao.capitalize())
    promocoes.append(promocao)

for i in range(0,4):
    print(f'Fruta\t   Quantidade\t  Preço/Kg\t    Promoção')
    print(f'{frutas[i]}\t' f'{qtd_Frutas[i]}\t' f'{preco_Quilos[i]}\t' f'{promocoes[i]}')
valorCompra = float(input('Entre com o valor da compra: '))
formaPagamento = int(input('1 - À vista, 2 - Cartão ou 3 - Parcelado: '))

if (formaPagamento == 1):
    total = valorCompra * 0.9
    print(f'O valor final da sua compra foi de {total}')
elif(formaPagamento == 2):
    total = valorCompra
    print(f'O valor final da sua compra foi de {total}')
elif(formaPagamento == 3):
    total = valorCompra * 1.10
    print(f'O valor final da sua compra foi de {total:.2f}')
else:
    print('Opção inválida!!')
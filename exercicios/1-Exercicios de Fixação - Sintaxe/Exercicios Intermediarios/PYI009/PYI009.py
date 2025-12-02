preco = float(input('Entre com o preço do produto: '))
formPagamento = input('Entre com a forma de pagamento (1 - à vista, 2 - cartão de crédito, 3 - cartão de débito): ')

if (formPagamento == '1' or formPagamento == '3'):
    total = formPagamento * 0.9
    print(f' Você optou por a vista ou no débito e por isso obteve 10% de desconto, pagando um valor total de: {total} ')
else:
    print('Você não obteve o desconto, pagando o valor total de:', preco)
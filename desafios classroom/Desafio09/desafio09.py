cadastro = {
    'nome': input('Entre com seu nome: '),
    'altura': float(input('Entre com sua altura: ')),
    'peso': float(input('Entre com seu peso: '))
}

print(cadastro)

cadastro['Data de Nascimento'] = '14/06/1984'

print(cadastro)

cadastro['peso'] = float(input('Entre com seu novo peso: '))

print(cadastro)

del cadastro['peso']

print(cadastro)
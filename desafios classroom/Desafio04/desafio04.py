usuario = 'admin'
senha = '1234'

usuario1 = input('Entre com seu usuário: ')
senha1 = input("Entre com sua senha: ")

if(usuario == usuario1 and senha == senha1):
    print('Login autorizado')
elif(usuario == usuario1 or senha == senha1):
    print('Credenciais parcialmenete corretas')
else:
    print('Acesso negado')

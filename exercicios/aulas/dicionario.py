#Criando um dicionário com INPUT
cadastro = {
    'nome': input('Digite seu nome: '),
    'idade' : input('Digite sua idade: '),
    'cidade' : input('Digite sua cidade: ')
}

print('\nCadastro inicial', cadastro)

# Adicionando nova CHAVE e VALOR
nova_chave = input('\n Digite o nome de uma nova chave: ')
novo_valor = input('Digite o valor dessa nova chave: ')
cadastro[nova_chave] = novo_valor

print('\n Cadastro alterado: ', cadastro)

#Alterando valor de uma chave existente
chave_atualizar = input('\nDigite o nome da chave que deseja atualizar: ')

if chave_atualizar in cadastro:
    novo_valor_atualizado = input('Digite o novo valor: ')
else:
    print('Chave não encontrada!! Nenhuma alteração foi feita.')



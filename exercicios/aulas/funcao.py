#Função apresentação
def saudacao(nome):
    print(f'Olá {nome}')
nome ='Filipe'
saudacao(nome)

def apresentar(nome, idade):
    print(f'{nome} tem {idade} anos.')

apresentar('Filipe', 41)

# Calculo IMC
def calcular_imc(peso, altura):
    return peso / (pow(altura,2))

imc = calcular_imc(70, 1.75)
print(f'Seu IMC é de: {imc:.2f}')

#Função soma
def somar(a,b):
    resposta = a+b
resposta = somar(2,3)
print(resposta) #Nada é mostrado

def somar(a, b):
    resposta = a + b
    return resposta

print(somar(10, 5))

# Função calcular pagamento
def calcular_pagamento(horas, valor_por_hora):
    return horas * valor_por_hora
salario = calcular_pagamento(40,25)
print(f'O pagamento será de R$ {salario:.2f}')

#Função calcular desconto
def mostrar_desconto(valor, percentagem):
    preco_com_desconto = valor * ((100 - percentagem)/100)
    print(preco_com_desconto)
mostrar_desconto(100, 10)

def mostrar_desconto_1(valor, percentagem):
    preco_com_desconto = valor * ((100 - percentagem)/100)
    return preco_com_desconto

print(mostrar_desconto_1(100,20))

x = mostrar_desconto_1(100,20)
print(x)

#Funcao dentro de Funcao
def processar_valor(n):
    def dobrar(x):
        return x * 2
    
    resultado = dobrar(n)
    return resultado
print(processar_valor(5))

#Função para validar se ex
def cadastrar_usuario(nome):
    def validar(texto):
        return texto.strip() != ''
    if validar(nome):
        return "Usuário cadastrado"
    else:
        return "Nome inválido"
print(cadastrar_usuario('João'))
print(cadastrar_usuario(''))

convidados = ['Pedro', 'Maria', 'João', 'Carlos', 'José', 'Manoel', 'Teresa', 'Francisca', 'Gustavo', 'Bruno']

novo_convidado = 'Flávio'
convidados.append(novo_convidado)
print(convidados)

remover_convidado = 'Maria'
convidados.remove(remover_convidado)
print(convidados)

quantidade_convidados = len(convidados)
print(quantidade_convidados)

mostrar_primeiro = convidados[0]
print(mostrar_primeiro)

mostrar_ultimo = convidados[-1]
print(mostrar_ultimo)

convidados[1] = 'Yuri'
print(convidados)



animais_nomes = []
animais_especies = []
animais_idade = []
animais_comida = []

qtd_animais = int(input('Entre com a quantidade de animais: '))

for enter in range(0, qtd_animais+1):
    nome_animal = input('Entre com o nome do animal: ')
    animais_nomes.append(nome_animal)
    especie_animal = input('Entre com a espécie do animal: ')
    animais_especies.append(especie_animal)
    idade_animal = int(input('Entre com a idade do animal: '))
    animais_idade.append(idade_animal)
    comida_animal = float(input('Entre com a quantidade de comida que o animal come no dia: '))
    animais_comida.append(comida_animal)

for i in range(0,qtd_animais+1):
    print(f'Animal {animais_nomes[i]}, é da espécie {animais_especies[i]}, tem {animais_idade[i]}, e come {animais_comida[i]}kg por dia. ')
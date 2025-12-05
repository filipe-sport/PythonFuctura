salario = float(input('Entre com o valor do salário: '))

if salario <= 1500 :
    salario_reajust = salario * 1.15
    print(f'O salário sofreu um aumento de 15% e será reajustado para: {salario_reajust}')
elif 1500 < salario <= 2500:
    salario_reajust = salario * 1.10
    print(f'O salário sofreu um aumento de 10% e será reajustado para: {salario_reajust}')
else:
    salario_reajust = salario * 1.05
    print(f'O salário sofreu um aumento de 5% e será reajustado para: {salario_reajust}')
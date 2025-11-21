idade = int(input('Qual a sua idade? '))
if (0 <= idade <= 12):
    categoria = 'criança'
elif (13 <= idade <= 17):
    categoria = 'adolescente'
elif (18 <= idade <= 59):
    categoria = 'adulto'
elif (idade >= 60):
    categoria = 'idoso'

if (categoria == 'criança' or categoria == 'adolescente'):
    print('Você ainda é menor de idade')
elif(categoria == 'adulto' or categoria == 'idoso'):
    print('Pode participar das atividades para maiores de idade')

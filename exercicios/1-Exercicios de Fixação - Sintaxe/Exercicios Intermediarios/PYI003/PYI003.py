nota1 = float('Entre com a primeira nota: ')
nota2 = float('Entre com a segunda nota: ')
nota3 = float('Entre com a terceira nota: ')

media = (nota1 + nota2 + nota3)/3
if (media >=7):
    print('Aluno aprovado')
elif (4 < media < 7):
    print('Aluno em prova final')
else:
    print('Aluno reprovado')

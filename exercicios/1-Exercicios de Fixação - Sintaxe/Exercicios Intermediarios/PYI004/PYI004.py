n1 = float(input('Entre com a primeira nota do aluno: '))
n2 = float(input('Entre com a segunda nota do aluno: '))
n3 = float(input('Entre com a terceira nota do aluno: '))

media = (n1 + n2 + n3)/3

if media >= 7:
    print('O aluno está aprovado!!')
elif (4 <= media < 7):
    print('O aluno está em prova final')
else:
    print('Aluno reprovado!!')
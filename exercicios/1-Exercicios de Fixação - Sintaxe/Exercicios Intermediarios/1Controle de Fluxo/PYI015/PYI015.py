hora = int(input('Entre com uma hora: '))

if (00 <= hora < 12):
    print('Bom dia!!')
elif (12 <= hora < 18):
    print('Boa tarde!!')
elif (18 <= hora < 00):
    print('Boa noite!!')
else:
    print('Hora inválida!!')
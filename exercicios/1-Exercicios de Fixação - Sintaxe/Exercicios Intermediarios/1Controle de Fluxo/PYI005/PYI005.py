mes = int(input('Entre com o numero do mês: '))

if(mes == 2):
    print('O mês têm 28 dias')
    
elif(1<= mes <= 7 ):
    if(mes % 2 == 0):
        print('O mês tem 30 dias')
    else:
        print('O mês tem 31 dias')
elif( 8 <= mes <= 12):
    if(mes % 2 == 0):
        print('O mês tem 31 dias!')
    else:
        print('O mês tem 30 dias!')
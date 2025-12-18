class Lampada:
    def __init__(self, cor):
        self.cor = cor
        self.ligada = False

    def ligar(self):
        self.ligada = True
        print('A almpada está acesa!')
    def desligar(self):
        self.ligada = False
        print('A lampada está desligada!')
    def mostrar_estado(self):
        if self.ligada == True:
            print(f'A lampada {self.cor} está ligada!')
        else:
            print(f'A lampada {self.cor} está desligada!')

lampada1 = Lampada('branca')
lampada1.ligar()
lampada1.desligar()
lampada1.mostrar_estado()



    # def desligar
    # def mostrar_estado
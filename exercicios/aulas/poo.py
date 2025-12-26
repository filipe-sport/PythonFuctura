class Carro:
    # O método __init__ é o construtor da classe.
    # Ele é executado automaticamente quando criamos um novo carro
    def __init__(self, cor, modelo):
        self.cor = cor
        self.modelo = modelo
        self.velocidade = 0 #Todo carro começa parado
        self.ligado = False # Se ligado é True, desligado é false
    
    #Método para ligar o carro
    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print(f"O {self.modelo} está ligado.")
        else:
            print('O carro já está ligado.')
    
    #Método para acelerar o carro:
    def acelerar(self,valor):
        if self.ligado:
            self.velocidade += valor
            print(f"Velocidade atual: {self.velocidade} km/h")
        else:
            print('Você precisa ligar o carro antes de acelerar.')
    
    #Metodo para frear o carro
    def frear(self,valor):
        if self.velocidade > 0:
            self.velocidade -= valor
            if self.velocidade < 0: #Evita velocidade negativa (não existe -10 km/h)
                self.velocidade = 0
            print(f'Freando... Velocidade atual: {self.velocidade} km/h')
        else:
            print('O carro jé está parado')
    

#
carro1 = Carro('bege','Kwid')
carro1.ligar()
carro1.acelerar(20)
carro1.frear(50)

carro2 = Carro('vermelho', 'Corola')
carro2.ligar()
carro2.acelerar(100)
carro2.frear(30)
carro2.buzinar()


class Carro:
    # O método __init__ é o construtor da classe.
    # Ele é executado automaticamente quando criamos um novo carro
    def __init__(self,cor,modelo):
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
    
    #Metodo para frear o carro
    def frear(self,valor):
        pass
    
    #Método para acelerar o carro:
    def acelerar(self,valor):
        if self.ligado:
            self.velocidade += valor
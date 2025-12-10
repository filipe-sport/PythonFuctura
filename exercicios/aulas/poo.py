class Carro:
    # O método __init__ é o construtor da classe.
    # Ele é executado automaticamente quando criamos um novo carro
    def __init__(self,cor,modelo):
        self.cor = cor
        self.modelo = modelo
        self.velocidade = 0
        self.ligado = False
class Carro:
    # O método __init__ é o construtor da classe.
    # Ele é executado automaticamente quando criamos um novo carro
    def __init__(self, cor, modelo):
        self.cor = cor
        self.modelo = modelo
        self.__velocidade = 0 #Todo carro começa parado
        self.__ligado = False # Se ligado é True, desligado é false
    
    #Método para ligar o carro
    def ligar(self):
        if not self.__ligado:
            self.__ligado = True
            print(f"O {self.modelo} está ligado.")
        else:
            print('O carro já está ligado.')
    
    #Método para acelerar o carro:
    def acelerar(self,valor):
        if self.__ligado:
            self.__velocidade += valor
            print(f"Velocidade atual: {self.__velocidade} km/h")
        else:
            print('Você precisa ligar o carro antes de acelerar.')
    
    #Metodo para frear o carro
    def frear(self,valor):
        if self.__velocidade > 0:
            self.__velocidade -= valor
            if self.__velocidade < 0: #Evita velocidade negativa (não existe -10 km/h)
                self.__velocidade = 0
            print(f'Freando... Velocidade atual: {self.__velocidade} km/h')
        else:
            print('O carro jé está parado')
    
    # GETTER (acessar valor)

    def get_velocidade(self):
        return self.__velocidade

    # SETTER (alterar valor)

    def set_velocidade(self,nova_velocidade):
        if nova_velocidade >= 0:
            self.__velocidade = nova_velocidade
        else:
            print('A velocidade não pode ser negativa!')
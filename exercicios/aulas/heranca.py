class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def falar(self):
        return "som de animal: "

class Cachorro(Animal):
    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade)
        self.raca = raca

    def falar(self):
        return "Au au au" 
    
    def buscar_bolinha(self):
        return f'{self.nome} está buscando a bolinha' 

class Gato(Animal):
    def __init__(self, nome, idade, cor_pelo):
        super().__init__(nome, idade)
        self.cor_pelo = cor_pelo #atributo exclusivo do gato
    
    def falar(self):
        return "Miau"
    
    def arranhar(self):
        return f'{self.nome} está arranhando o sofá'
    
cachorro1 = Cachorro('rex', 8, 'pitbull')
gato1 = Gato('Mimi', 2, 'Branco')

print(cachorro1.nome, '-', cachorro1.falar())
print(gato1.nome, '-', gato1.falar())
print(cachorro1.buscar_bolinha())
print(gato1.arranhar())


    

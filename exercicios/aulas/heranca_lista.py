class Animal:
    def __init__(self,nome):
        self.nome = nome
    
    def falar(self):
        return "Som genérico"

class Cachorro(Animal):
    def falar(self):
        return "Au au"
    
class Gato(Animal):
    def falar(self):
        return "Miau"


animais = [
    Cachorro("Rex"),
    Gato('Mimi'),
    Animal('Criatura misteriosa')
]

for animal in animais:
    print(animal.nome, '-', animal.falar())
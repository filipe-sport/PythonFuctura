class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def apresentar(self):
        return f'Olá meu nome é {self.nome} e tenho {self.idade} anos'

class Funcionario(Pessoa):
    def __init__(self, nome, idade, salario, cargo):
        super().__init__(nome, idade)
        self.salario = salario
        self.cargo = cargo
    def detalhar_funcionario(self):
        return f'O nome do funcionário é {self.nome}, tem {self.idade} anos, ocupa o cargo de {self.cargo} e ganha R$ {self.salario}'
    
funcionario = Funcionario('Filipe', 41, 3251.34, 'Analista')
print(funcionario.apresentar())
print(funcionario.detalhar_funcionario())




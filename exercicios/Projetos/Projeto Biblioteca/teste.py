class Pessoa:
    cadastro = {}
    

    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
            
    
    def cadastrar(self, nome, cpf):
        self.cadastro[nome] = {'nome':nome,'cpf' : cpf}
        print(self.cadastro)
        
class Juridico(Pessoa):
    def __init__(self, nome, cpf, cnpj):
        super().__init__(nome, cpf)
        self.cnpj = cnpj
    def cadastrar(self, nome, cpf, cnpj):
        self.cadastro[nome] = {'nome': nome,'cpf' : cpf, 'cnpj' : cnpj}
        print(self.cadastro)


while True:
    
    nome = input('Entre com seu nome: ')
    cpf = input('Entre com seu CPF: ')
    pessoa = Pessoa(nome, cpf)
    pessoa.cadastrar(nome, cpf)
    pj = input('A pessoa é Pessoa Jurídica (S / N)? ').upper()

    if (pj == 'S'):
        cnpj = input('Entre com o CNPJ: ')
        juridico = Juridico(nome, cpf, cnpj)
        juridico.cadastrar(nome, cpf, cnpj)

    



    
       
    
   






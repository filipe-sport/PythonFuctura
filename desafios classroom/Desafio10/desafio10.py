class ContaCorrente:
    def __init__(self,nome,cpf):
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0

    def sacar(self,valor):
        self.saldo -= valor
    
    def depositar(self,valor):
        self.saldo += valor
    
    def transferirEntrada(self,valor):
        self.saldo += valor

conta_pedro = ContaCorrente('Pedro', '123456789-10')
conta_pedro.depositar(500)
conta_pedro.transferirEntrada(200)
conta_pedro.sacar(150)

#Adicionar um novo cliente
conta_antonio = ContaCorrente('Antônio', '987654321-01')
conta_antonio.depositar(1000)
conta_antonio.transferirEntrada(250)
conta_antonio.sacar(100)

print(conta_antonio.saldo)
print(conta_pedro.saldo)
    

    

    
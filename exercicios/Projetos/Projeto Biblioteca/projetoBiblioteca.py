class Midia:
    def __init__(self, titulo, autor, ano, id,):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.id = id
        self.__disponivel = True

    def menu():
        while True:
            opcao = int(input('Digite a opção desejada (1- Cadastrar, 2- Listar, 3- Buscar [Título / Autor / Tipo], 4- Emprestar, 5- Devolver, 6- Remover )'))

            if(opcao == 1):
                Midia.cadastrar()
            elif(opcao == 2):
                Midia.listar()
            elif(opcao == 3):
                Midia.buscar()
            elif(opcao == 4):
                Midia.emprestar()
            elif(opcao == 5):
                Midia.devolver()
            elif(opcao == 6):
                Midia.remover()
            else:
                print('Opção Inválida!!')
    
    
    def cadastrar(self):
            titulo = input('Entre com o Título da mídia: ')
            autor = input('Entre com o autor da mídia: ')
            ano = input('Entre com o ano da mídia: ')
            id = input('Entre com o id da mídia: ')
            
    def listar():
        pass
    def buscar():
        pass
    def emprestar(self):        
        Midia.set_dispor(transacao = 'emprestar')
    def devolver(self):
        Midia.set_dispor(transacao = 'devolver')
    def remover():
        pass
    def get_dispor(self):
        return self.__disponivel
    def set_dispor(self, transacao):
        if transacao == 'emprestar':
            self.__disponivel = False
        elif transacao == 'devolver':
            self.__disponivel = True
        

    
menu = Midia.menu()
class Livro(Midia):
    def __init__(self, titulo, autor, ano, id):
        super().__init__(titulo, autor, ano, id)
    


class Revista(Midia):
    def __init__(self, titulo, autor, ano, id):
        super().__init__(titulo, autor, ano, id)


class Filme(Midia):
    def __init__(self, titulo, autor, ano, id, isbn, edicao, duracao):
        super().__init__(titulo, autor, ano, id)
        self.isbn = isbn
        self.edicao = edicao
        self.duracao = duracao




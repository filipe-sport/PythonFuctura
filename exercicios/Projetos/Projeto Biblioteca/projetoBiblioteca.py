class Midia:
    def __init__(self, titulo, autor, ano, id,):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.id = id
        self.__disponivel = True

      
    def cadastrar(self):
        pass
    def listar(self):
        pass
    def buscar(self):
        pass
    def emprestar(self):        
        Midia.set_dispor(transacao = 'emprestar')
    def devolver(self):
        Midia.set_dispor(transacao = 'devolver')
    def remover(self):
        pass
    def get_dispor(self):
        return self.__disponivel
    def set_dispor(self, transacao):
        if transacao == 'emprestar':
            self.__disponivel = False
        elif transacao == 'devolver':
            self.__disponivel = True


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


from datetime import date

class Midia():
    def __init__(self, titulo, autor, ano, id):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.id = id
        self.__disponibilidade = True
        
    biblioteca = {}
    
    def adicionar():
        titulo = input('Qual midia deseja adicionar: ')
        autor = input('Entre com o autor da midia: ')
        ano = input('Entre com o ano da midia: ')
        id = input('Entre com o id da mídia: ')
        disponivel = True        
        Midia.biblioteca[titulo] = {'titulo' : titulo, 'autor': autor, 'ano': ano, 'id': id, 'disponivel': disponivel}
        print('Livro adicionado com sucesso!')

        print(Midia.biblioteca[titulo]['titulo'])
        print(Midia.biblioteca[titulo]['autor'])
        
    def listar():
        if Midia.biblioteca:
            print('Sua lista de livros: ')
        print('-' * 30)

        for titulo, dados in Midia.biblioteca.items():
            autor = dados['autor']
            ano = dados['ano']
            print(f'{titulo} - {autor} - {ano}')
            print('-' * 30)

    def buscar():
        busca = input('Qual livro, autor ou tipo de midia está buscando? ')
        if busca in Midia.biblioteca:
            #Fazer verificação de metodos para achar um valor dentro de um dicionário e mostrar todo o dicionário
            titulo = Midia.biblioteca[busca]['titulo']
            autor = Midia.biblioteca[busca]['autor']
            print(f'Livro: Título: {titulo} - Autor: {autor}')
            print('-' * 30)
        else:
            print('Livro não encontrado!')
            print('-' * 30)

    def emprestar():
        
        print('-' * 30)
        print("Livros disponíveis: ")
        for titulo, dados in Midia.biblioteca.items():
            autor = dados['autor']
            print(f'{titulo} - {autor}')
            print('-' * 30)
        livro = input('Qual livro vc quer emprestado? ')
        
        if livro in Midia.biblioteca:
            print('Emprestimo feito com sucesso!')
            Midia.biblioteca[livro]['disponivel'] = False                     
        else:
            print('O livro não está disponível!')
    
    def devolver():
        print('-' * 30)
        livro = input('Qual livro vc quer devolver? ')
        
        if (livro in Midia.biblioteca) and (Midia.biblioteca[livro]['disponivel'] == False):
            print('Devolução feita com sucesso!')
            Midia.biblioteca[livro]['disponivel'] = True
        else:
            print('Erro de operação!!')

    def deletar():
        titulo = input('Qual Midia deseja deletar? ')
        if titulo in Midia.biblioteca:
            del Midia.biblioteca[titulo]
            print('-' * 30)
            print('Midia foi deletada com sucesso!')
            print('-' * 30)
        else:
            print('-' * 30)
            print('Midia não foi encontrada!')
            print('-' * 30)
    

    def menu():
        print('1. Para adicionar novos livros. ')
        print('2. Para listar livros. ')
        print('3. Para buscar livros. ')
        print('4. Para emprestar. ')
        print('5. para devolver.')
        print('6. Para deletar. ')
        print('7. Para fechar a biblioteca. ')
    
    def finalizar():
        print('1. Sim')
        print('2. Não')
    
    def loop():
        while True:
            Midia.menu()
            escolha = input('Escolha uma opção: ')
            if escolha == '1':
                Midia.adicionar()
            elif escolha == '2':
                Midia.listar()
            elif escolha == '3':
                Midia.buscar()
            elif escolha == '4':
                Midia.emprestar()
            elif escolha == '5':
                Midia.devolver()
            elif escolha == '6':
                Midia.deletar()
            elif escolha == '7':
                print('Até a proxima!!')
                break
            else:
                print('Opção inválida.')
                continue            
            Midia.finalizar()
            final = input('Deseja mais alguma coisa? ')
            if final == '1':
                continue
            elif final == '2':
                print('Até a próxima!')
                break
            else:
                print('Entrada inválida. Encerrando.')
                break


class Livro(Midia):
    def __init__(self, titulo, autor, ano, id, isbn):
        super().__init__(titulo, autor, ano, id)
        self.isbn = isbn  

class Revista(Midia):
    def __init__(self, titulo, autor, ano, id, edicao):
        super().__init__(titulo, autor, ano, id)
        self.edicao = edicao
          

class Filme(Midia):
    def __init__(self, titulo, autor, ano, id, duracao):
        super().__init__(titulo, autor, ano, id)
        self.duracao = duracao


obtendo_class = input('Entre com a midia Desejada: 1 - Revista, 2 - Livro, 3 - Filme: ')
if obtendo_class == '1':
    Revista.loop()
elif obtendo_class == '2':
    Livro.loop()
elif obtendo_class == '3':
    Filme.loop()
    
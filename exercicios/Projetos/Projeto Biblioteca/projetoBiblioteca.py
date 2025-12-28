from datetime import date

class Midia():
    def __init__(self, titulo, autor, ano, id):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.id = id
        
    biblioteca = {}
    
    def adicionar():
        titulo = input('Qual obra deseja adicionar? ')
        autor = input('Qual o autor da obra? ')
        Midia.biblioteca[titulo] = autor
        print('Livro adicionado com sucesso!')

    def listar():
        if Midia.biblioteca:
            print('Sua estante de livros: ')
        print('-' * 30)
        for titulo, autor in Midia.biblioteca.items():
            print(f'{titulo} - {autor}')
            print('-' * 30)

    def buscar():
        titulo = input('Qual livro está buscando?')
        if titulo in Midia.biblioteca:
            print(f'Livro: {titulo} - Autor: {Midia.biblioteca[titulo]}')
            print('-' * 30)

    def emprestar():
        print('-' * 30)
        print("Livros disponíveis: ")
        for titulo, autor in Midia.biblioteca:
            print(f'{titulo} - {autor}')
            print('-' * 30)
        livro = input('Qual livro vc quer emprestado? ')
        if livro in Midia.biblioteca:
            print('Emprestimo feito com sucesso!')
            dia = date.today().day
            print('Hoje é dia {dia}  e sua devolução é em 10 dias')
        else:
            print('O livro não está disponível!')

    def deletar():
        titulo = input('Qual obra deseja deletar? ')
        if titulo in Midia.biblioteca:
            del Midia.biblioteca[titulo]
            print('-' * 30)
            print('Obra foi deletada com sucesso!')
            print('-' * 30)
        else:
            print('-' * 30)
            print('Obra não foi encontrada!')
            print('-' * 30)
    

    def menu():
        print('1. Para adicionar novos livros. ')
        print('2. Para listar livros. ')
        print('3. Para buscar livros. ')
        print('4. Para emprestar. ')
        print('5. Para deletar. ')
        print('6. Para fechar a biblioteca. ')
    
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
                Midia.deletar()
            elif escolha == '6':
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

Midia.loop()


            
    



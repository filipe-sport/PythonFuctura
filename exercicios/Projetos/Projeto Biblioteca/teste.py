class Midia:
    def __init__(self, titulo, ano):
        
        biblioteca = {
            'filme' : {
                'titulo' : titulo,
                'ano': ano
            }
        }

        for  ano in biblioteca:
            if ano in biblioteca:
                print(f'A chave procurada pertence ao {biblioteca}')


x = Midia('pequeno', '1984')



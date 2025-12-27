class Midia:
    def __init__(self):
        self.cadastro = {}
    
    def cadastrar_midia(self, id, titulo):
        if 'midia' not in self.cadastro:
            self.cadastro['midia'] = {id : titulo}
        else:
            self.cadastro['midia'].update({id : titulo})
    def lista_titulos(self):
        for id, titulo in self.cadastro['midia'].items():
            print(id, titulo)
    def apaga_titulo(self, id):
        del self.cadastro['midia'] [id]

bd = Midia()
bd.cadastrar_midia(1, 'Pequeno Principe')
bd.cadastrar_midia(2, 'Predador')
bd.cadastrar_midia(3, 'Anjos da Noite')
#bd.apaga_titulo(2)
bd.lista_titulos()

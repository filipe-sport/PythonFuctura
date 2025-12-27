class Midia:
    def __init__(self):
        self.dados = {}
    
    def cadastrar_midia(self, id, titulo):
        if 'midia' not in self.dados:
            self.dados['midia'] = {id : titulo}
        else:
            self.dados['midia'].update({id : titulo})
    def lista_titulos(self):
        for id, titulo in self.dados['midia'].items():
            print(id, titulo)
    def apaga_titulo(self, id):
        del self.dados['midia'] [id]

bd = Midia()
bd.cadastrar_midia(1, 'Pequeno Principe')
bd.cadastrar_midia(2, 'Predador')
bd.cadastrar_midia(3, 'Anjos da Noite')
#bd.apaga_titulo(2)
bd.lista_titulos()

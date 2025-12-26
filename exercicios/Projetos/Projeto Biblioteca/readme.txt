1.Simular o funcionamento básico de uma
biblioteca: cadastrar mídias (livros, revistas,
filmes), controlar disponibilidade e empréstimos,
manter histórico e permitir buscas. Aplicação em
camadas (modelo, controle, interface) e menu
interativo.

Deve conter (mínimo obrigatório)
✔ Classe pai Midia com atributos comuns (título, autor, ano, id)
✔ Subclasses Livro, Revista, Filme com atributos específicos (ex.:
ISBN, edição, duração)
✔ Encapsulamento para atributo __disponivel (privado)
✔ Métodos emprestar(contato) e devolver() que atualizam
disponibilidade e histórico básico
✔ Polimorfismo: método obter_tipo() que retorna o tipo da mídia
(implementado diferente nas subclasses)
✔ Lista de mídias cadastradas e lista (ou registro) de empréstimos
ativos
✔ Menu interativo para: cadastrar, listar, buscar (por
título/autor/tipo), emprestar, devolver, remover
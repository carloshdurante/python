# Carlos Henrique Durante da Silva
# (11)96340-9937
# carlos.durante@outlook.com
# https://linkedin.com/in/carloshdurante
# Programação Orientada a Objetos

'''
|------------|          |-----------------|
|   Pessoa   |          |      Livro      |
|------------|          |-----------------|
| nome       |1     0..*| titulo          |
|------------|----------| paginas         |
|            |          | autor           |
|------------|          |-----------------|
                        | exibir_dados()  |
                        |-----------------|
'''


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


class Livro:
    def __init__(self, titulo, paginas, autor):
        self.titulo = titulo
        self.paginas = paginas
        self.autor = autor

    def exibir_dados(self):
        print("Titulo: ", self.titulo)
        print("Paginas ", self.paginas)
        print("Autor: ", self.autor.nome)
        print("Idade do Autor: ", self.autor.idade)


pessoa1 = Pessoa("Nicholas Sparks", 57)
book = Livro("Um porto seguro", 197, pessoa1)
book.exibir_dados()

book2 = Livro("Um amor para recordar", 210, pessoa1)
book.exibir_dados()

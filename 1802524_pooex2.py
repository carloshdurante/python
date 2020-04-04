# Carlos Henrique Durante da Silva
# (11)96340-9937
# carlos.durante@outlook.com
# https://linkedin.com/in/carloshdurante
# Programação Orientada a Objetos

'''
Crie uma classe livro com os atributos:
- titulo
- autor
- preço
Crie o método:
- exibir_dados(exibe o titulo, autor e preço do livro)
'''


class Livro:
    # atributos
    def __init__(self, titulo, autor, preco):               # construtor
        self.titulo = titulo
        self.autor = autor
        self.preco = preco

    # metodos
    def exibir_dados(self):
        print(f"Titulo: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Preço: R${self.preco}")


romance = Livro("Um amor para recordar", "Nicholas Sparks", 30.0)
romance.exibir_dados()

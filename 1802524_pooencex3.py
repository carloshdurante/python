class Filme:
    def __init__(self, titulo, genero):
        self.__titulo = titulo
        self.__gereno = genero

    def get_titulo(self):
        return self.__titulo

    def get_genero(self):
        return self.__gereno

    def set_titulo(self, titulo):
        self.__titulo = titulo

    def set_genero(self, genero):
        self.__genero = genero


filmes = []
for i in range(3):
    titulo = input("Digite o titulo do filme:")
    genero = input("Digite o genero do titulo informado:")
    filme = Filme(titulo, genero)
    filmes.append(filme)

for i in filmes:
    tituto = input("Novo titulo:")
    genero = input("Novo genero:")
    i.set_titulo(titulo)
    i.set_genero(genero)

for i in filmes:
    print("Titulo do Filme:", i.get_titulo())
    print("Genero do Filme:", i.get_genero())

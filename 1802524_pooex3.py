class Aluno:
    def __init__(self, ra, nome):
        self.ra = ra
        self.nome = nome
        self.lista_disciplinas = []

    def adicionar_disciplinas(self, disc):
        self.lista_disciplinas.append(disc)

    def exibir(self):
        print("R.A: ", self.ra)
        print("Nome: ", self.nome)
        print("Disciplinas:", self.lista_disciplinas)


aluno01 = Aluno(1802524, "Carlos")
aluno01.adicionar_disciplinas("Linguagem de Programação II")
aluno01.adicionar_disciplinas("Banco de Dados")
aluno01.exibir()

class Pessoa:
    def __init__(self, nome, idade, cpf, rg):
        self.nome = nome
        self.idade = idade
        self.__cpf = cpf
        self.__rg = rg

    def exibir_dados(self):
        print("Nome:", self.nome)
        print("Idade:", self.idade)
        print("CPF:", self.__cpf)
        print("RG:", self.__rg)

    def get_cpf(self):
        return self.__cpf

    def get_rg(self):
        return self.__rg

    def set_cpf(self, cpf):
        if len(str(cpf)) == 11:
            self.__cpf = cpf
        else:
            print("CPF Inválido")

    def set_rg(self, rg):
        self.__rg = rg


pessoa1 = Pessoa("Carlos", 25, None, 46819146)
pessoa1.nome = "Carlos Durante"
pessoa1.idade = 26

pessoa1.set_rg('46819146x')
pessoa1.set_cpf(42697288848)
print("Nome: ", pessoa1.nome)
print("CPF:", pessoa1.get_cpf())

# Carlos Henrique Durante da Silva
# (11)96340-9937
# carlos.durante@outlook.com
# https://linkedin.com/in/carloshdurante
# Programação Orientada a Objetos


class Emprego:
    def __init__(self, cargo, salario, bonus):
        self.cargo = cargo
        self.salario = salario
        self.bonus = bonus


class Pessoa:
    def __init__(self, nome, fone, email, emprego, dependentes):
        self.nome = nome
        self.fone = fone
        self.email = email
        self.emprego = emprego
        self.dependentes = dependentes

    def calcular_salario(self):
        print(emprego01.salario + (emprego01.salario *
              (pessoa01.dependentes * emprego01.bonus)))


emprego01 = Emprego('Programador', 1000, 0.1)
pessoa01 = Pessoa('Carlos', '11963409937', 'carlos.durante@outlook.com',
                  emprego01, 3)

pessoa01.calcular_salario()

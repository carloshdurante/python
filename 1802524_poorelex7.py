# Carlos Henrique Durante da Silva
# (11)96340-9937
# carlos.durante@outlook.com
# https://linkedin.com/in/carloshdurante
# Programação Orientada a Objetos


class Emprego:
    def __init__(self, cargo, area, salario, bonus):
        self.cargo = cargo
        self.area = area
        self.salario = salario
        self.bonus = bonus


class Pessoa:
    def __init__(self, nome, fone, email, emprego):
        self.nome = nome
        self.fone = fone
        self.email = email
        self.emprego = emprego
        self.dependentes = []

    def calcular_salario(self):
        salario = self.emprego.salario + (self.emprego.salario *
                                          (len(self.dependentes)
                                           * self.emprego.bonus))/100
        return salario


emprego = Emprego("Programador", "TI", 1000, 5)
pessoa1 = Pessoa("Paulo", "11-99999999", "paulo@email.com", emprego)

dep1 = Pessoa("Maria", "", "", None)
dep2 = Pessoa("Joao", "", "", None)

pessoa1.dependentes.append(dep1)
pessoa1.dependentes.append(dep2)

print("Salario: ", pessoa1.calcular_salario())

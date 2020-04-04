# Carlos Henrique Durante da Silva
# (11)96340-9937
# carlos.durante@outlook.com
# https://linkedin.com/in/carloshdurante
# Programação Orientada a Objetos


class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def aumentar_salario(self, perc):
        aumento = self.salario * perc/100
        novo_salario = self.salario + aumento
        print(novo_salario)


nome = input("Digite o nome do funcionário: ")
salario = float(input("Informe o salário do funcionário: "))
func = Funcionario(nome, salario)
perc = float(input("Digite o percentual do aumento: "))
func.aumentar_salario(perc)

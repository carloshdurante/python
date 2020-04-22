class Cliente:
    def __init__(self, nome, cpf, senha):
        self.nome = nome
        self.__cpf = cpf
        self.__senha = senha

    def get_cpf(self):
        return self.__cpf

    def get_senha(self):
        return self.__senha

    def set_cpf(self, cpf):
        self.__cpf = cpf


class ContaBancaria:
    def __init__(self, numero, cliente):
        self.numero = numero
        self.cliente = cliente
        self.__saldo = 0

    def get_saldo(self, senha):
        if senha == self.cliente.get_senha():
            return self.__saldo
        else:
            print("Senha Inválida")

    def depositar(self, valor, senha):
        if senha == self.cliente.get_senha():
            self.__saldo += valor
        else:
            print("Senha Inválida")

    def sacar(self, valor, senha):
        if senha == self.cliente.get_senha():
            self.__saldo -= valor
        else:
            print("Senha Inválida")


cliente1 = Cliente("João", "111111111", "123")
conta = ContaBancaria(1111, cliente1)

conta.depositar(200, "123")
print(conta.get_saldo("123"))            # Imprime 200
conta.sacar(50, "123")
print(conta.get_saldo("123"))            # Imprime 150

conta.depositar(100, "111")         # senha inválida
print(conta.get_saldo("123"))            # Imprime 150
conta.sacar(50, "111")              # senha inválida
print(conta.get_saldo("123"))            # Imprime 150

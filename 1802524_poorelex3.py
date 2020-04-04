# Carlos Henrique Durante da Silva
# (11)96340-9937
# carlos.durante@outlook.com
# https://linkedin.com/in/carloshdurante
# Programação Orientada a Objetos

'''
|------------|         |---------------------|        |-------------|
| Produto    |         | Carrinho            |        | Cliente     |
|------------|         |---------------------|        |-------------|
| descricao  |0..*    1| cliente             |1      1| nome        |
| valor      |---------| produtos            |--------|-------------|
|------------|         |---------------------|        |             |
|            |         | adicionar_produto() |        |-------------|
|------------|         | listar_produtos()   |
                       | calcular_total()    |
                       |---------------------|
'''


class Produto:
    def __init__(self, descricao, valor):
        self.descricao = descricao
        self.valor = valor


class Cliente:
    def __init__(self, nome):
        self.nome = nome


class Carrinho:
    def __init__(self, cliente):
        self.cliente = cliente
        self.produtos = []

    def adicionar_produto(self, prod):
        self.produtos.append(prod)

    def listar_produtos(self):
        for prod in self.produtos:
            print(prod.descricao, prod.valor)

    def calcular_total(self):
        soma = 0
        for prod in self.produtos:
            soma += prod.valor
            return soma


cliente1 = Cliente("Carlos")
prod1 = Produto("Notebook Dell Gaming G5", 6909.0)
prod2 = Produto("Monitor AOC Hero 144hz", 1100.0)

carrinho = Carrinho(cliente1)
carrinho.adicionar_produto(prod1)
carrinho.adicionar_produto(prod2)
carrinho.listar_produtos()
print("Total:", carrinho.calcular_total())

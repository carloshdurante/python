# Carlos Henrique Durante da Silva
# (11)96340-9937
# carlos.durante@outlook.com
# https://linkedin.com/in/carloshdurante
# Programação Orientada a Objetos


class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade


class Pedido:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def calcular_valor(self):
        soma = 0
        for i in self.produtos:
            soma += i.preco * i.quantidade
        return soma


cafe = Produto('Café Solúvel', 5.50, 1)
arroz = Produto('Arroz Integral', 4.90, 2)
feijao = Produto('Feijão Preto', 2.80, 2)
meu_pedido = Pedido()
meu_pedido.adicionar_produto(cafe)
meu_pedido.adicionar_produto(arroz)
meu_pedido.adicionar_produto(feijao)
print('O valor total é: {0:.2f}' .format(meu_pedido.calcular_valor()))

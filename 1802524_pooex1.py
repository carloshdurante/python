'''
Classe Cachorro
- Atributos: nome, idade
- Métodos: andar, comer, latir
'''


class Cachorro:
    # atributos
    def __init__(self, nome, idade):                # construtor
        self.nome = nome
        self.idade = idade

    # metodos
    def andar(self, distancia):
        print("O cachorro andou " + str(distancia) + " metros")

    def comer(self):
        print("O cachorro de nome " + self.nome + " comeu")

    def latir(self):
        print("O cachorro de nome " + self.nome + " latiu: Au Au..,")


dog = Cachorro("Rex", 4)
print("O cachorro de nome " + dog.nome + " possui da idade de "
      + str(dog.idade) + " anos")
dog.andar(2)
dog.latir()
dog.comer()
print("---------------------------------------------------------")

meu_cachorro = Cachorro("Snoopy", 2)
print("O cachorro de nome " + meu_cachorro.nome + " possui da idade de "
      + str(meu_cachorro.idade) + " anos")
meu_cachorro.andar(5)
meu_cachorro.latir()
meu_cachorro.comer()

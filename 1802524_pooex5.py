class Triangulo:
    def __init__(self, lado_a, lado_b, lado_c):
        self.lado_a = lado_a
        self.lado_b = lado_b
        self.lado_c = lado_c

    def calcular_perimetro(self):
        perimetro = lado_a + lado_b + lado_c
        print(f"O perimetro do triangulo é: {perimetro}")

    def maior_lado(self):
        if self.lado_a > self.lado_b and lado_c:
            print(self.lado_a)
        elif self.lado_b > self.lado_a and self.lado_c:
            print(self.lado_b)
        else:
            print(self.lado_c)


lado_a = float(input("Digite o lado A: "))
lado_b = float(input("Digite o lado B: "))
lado_c = float(input("Digite o lado C: "))

tri = Triangulo(lado_a, lado_b, lado_c)
tri.calcular_perimetro()
tri.maior_lado()

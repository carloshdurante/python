# Carlos Henrique Durante da Silva
# (11)96340-9937
# carlos.durante@outlook.com
# https://linkedin.com/in/carloshdurante
# Dicionários x Funções


def calcular_media(alunos, nome):
    if nome in alunos:
        media = sum(alunos[nome]) / len(alunos[nome])
        return media
    else:
        return 0


alunos = {}

for i in range(1):
    nome = input('Nome:')
    nota1 = float(input("Nota 1:"))
    nota2 = float(input("Nota 2:"))
    alunos[nome] = [nota1, nota2]

nome = input('Digite um nome:')
media = calcular_media(alunos, nome)
print("Media do aluno:", media)

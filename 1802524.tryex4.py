# Carlos Henrique Durante da Silva
# (11)96340-9937
# carlos.durante@outlook.com
# https://linkedin.com/in/carloshdurante
# Execeptions x Funções


def InserirAluno(alunos, ra, nome):
    try:
        x = str(ra)
        if len(x) != 7:
            raise TypeError
    except ValueError:
        print("Erro: Digite apenas números inteiros")
    except TypeError:
        print("Permetido apenas 7 digitos")
    try:
        if ra in alunos:
            raise TypeError
    except TypeError:
        print("Aluno já inserido")
    else:
        alunos[ra] = nome
    return


def BuscarAluno(alunos, ra, nome):
    try:
        if ra not in alunos:
            raise KeyError
    except KeyError:
        print("R.A não encontrado")
    else:
        return print(alunos[ra])


alunos = {1234567: 'Carlos'}

nome = input("Digite o nome do aluno:")
ra = int(input("Digite o R.A do aluno:"))

InserirAluno(alunos, ra, nome)

nome = input("Digite o nome do aluno:")
ra = int(input("Digite o R.A do aluno:"))

BuscarAluno(alunos, ra, nome)

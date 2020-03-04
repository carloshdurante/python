# Carlos Henrique Durante da Silva
# (11)96340-9937
# carlos.durante@outlook.com
# https://linkedin.com/in/carloshdurante
# Execeptions x Funções


def InserirNome(lista, nome):
    lista.append(nome)


def ConsultaLista(lista, i):
    try:
        return lista[i]
    except IndexError:
        print('Indice nao encontrado')


lista = []

nome = input("Digite o nome do usuário:")
InserirNome(lista, nome)

i = int(input('Digite o indice:'))
nome = ConsultaLista(lista, i)
if nome is not None:
    print(nome)

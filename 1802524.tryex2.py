# Carlos Henrique Durante da Silva
# (11)96340-9937
# carlos.durante@outlook.com
# https://linkedin.com/in/carloshdurante
# Execeptions x Funções

try:
    def funcao_1():
        print('Início da função 1')
        funcao_2()
        print('Fim da função 1')

    def funcao_2():
        print('Início da função 2')
        lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        for i in range(15):
            print(lista[i])
        print('Fim da função 2')

    print('Início do programa')
    funcao_1()
    print('Fim do programa')
except IndexError:
    print("Indice não encontrado")

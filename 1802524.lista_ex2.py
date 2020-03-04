# Carlos Henrique Durante da Silva
# (11)96340-9937
# carlos.durante@outlook.com
# https://linkedin.com/in/carloshdurante
# Listas

import random

lista = []
for i in range(10):
    lista.append(random.randint(1, 6))

print(lista)

for i in range(1, 7):
    print('Número {} foi sorteado {}'   .format(i, lista.count(i)))

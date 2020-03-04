# Carlos Henrique Durante da Silva
# (11)96340-9937
# carlos.durante@outlook.com
# https://linkedin.com/in/carloshdurante
# Listas

import lista_ex3_modulo

t1 = ()
t2 = ()

for i in range(3):
    t1 += (int(input()),)

for i in range(3):
    t2 += (int(input()),)

print(lista_ex3_modulo.intercala(t1, t2))

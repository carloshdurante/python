# Carlos Henrique Durante da Silva
# (11)96340-9937
# carlos.durante@outlook.com
# https://linkedin.com/in/carloshdurante
# Listas

lista = []
for i in range(10):
    lista.append(int(input()))

print(max(lista))
print(min(lista))
media = sum(lista)/len(lista)
print(media)

for i in lista:
    if i < media:
        print(i)

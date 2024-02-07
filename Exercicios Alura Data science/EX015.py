lista = []

for i in range(1, 6):
    item = int(input('Digite um valor: '))
    lista.append(item)
    i += 1

lista.reverse()
print(lista)
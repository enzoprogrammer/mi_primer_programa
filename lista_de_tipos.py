lista_datos=[False, 1.1, ["a"], "pitito", 2, 3, True]
lista_tipos= []

for dato in lista_datos:
    lista_tipos.append(type(dato))

print(lista_tipos)

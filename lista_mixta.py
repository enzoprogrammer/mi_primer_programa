lista_usuario=[1, 3, "coca", 8, "welcome", 8.2, 4.0]
lista_string=[]
lista_numeros=[]

for dato in lista_usuario:
    tipo_dato=type(dato)
    if tipo_dato==int or tipo_dato==float:
        lista_numeros.append(dato)
    elif tipo_dato==str:
        lista_string.append(dato)
print("Lista numeros {}".format(lista_numeros))
print("Lista string {}".format(lista_string))

lista_usuario= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def pares_en_lista(lista_usuario):
    lista_pares=[]
    for numero in lista_usuario:
        if numero % 2== 0:
            lista_pares.append(numero)
    return lista_pares

print(pares_en_lista(lista_usuario))


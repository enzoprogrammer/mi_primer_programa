def añadir_a_lista_numeros(pregunta):
    operar= True
    lista_usuario=[]
    while operar != False:
        dato_usuario = int(input(pregunta))
        lista_usuario.append(dato_usuario)
        continuar = input("Desea añadir algo mas a la lista? [Si/No]: ").upper()
        if continuar == "NO":
            operar = False
    return lista_usuario

def pares_en_la_lista(lista):
    lista_pares= []
    for numero in lista:
        if numero % 2 == 0:
            lista_pares.append(numero)
    return lista_pares

lista_usuario= añadir_a_lista_numeros("Dime un numero para añadir a la lista: ")
print(lista_usuario)
print(" ")
print(pares_en_la_lista(lista_usuario))








lista_usuario= []
operar= True
cantidad_elementos= 1

while operar != False:
    añadir_lista= input("Añada algo a la lista: ")
    lista_usuario.append(añadir_lista)

    seguir_operando= input("Desea añadir algo mas? Si/ No : ").upper()
    if seguir_operando== "SI":
        cantidad_elementos += 1
    else:
        operar= False

print(" ")
print("Su lista contiene {} elementos".format(cantidad_elementos))
print(" ")





salida= False
fechas= dict()
print("-------------------Bienvenido-------------------")

while not salida:
    opcion_usuario= input("Agregar cumpleaños [A] / Ver fecha de cumpleaños [B] / Salir [S] :").upper()
    print(" ")

    if opcion_usuario== "A":
        print("-----AGRAGANDO CUMPLEAÑOS-----")
        print(" ")
        nombre= input("Escriba el nombre de la persona: ")
        fecha_nacimiento= input("Escriba fecha de nacimiento: ")
        fechas[nombre]= fecha_nacimiento

    elif opcion_usuario== "B":
        print("-----BUSCAR FECHA-----")
        print(" ")
        nombre= input("La fecha de quien desea buscar? :")
        print(fechas[nombre])

    elif opcion_usuario== "S":
        salida = True
        print("----------OFF----------")



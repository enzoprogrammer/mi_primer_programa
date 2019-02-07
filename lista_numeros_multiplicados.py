lista_numeros_usuario= []
operar= "SI"

while operar != "NO":
    numero_usuario= int(input("Dime un numero para agregar a la lista: "))
    lista_numeros_usuario.append(numero_usuario)
    operar=input("Desea agregar mas numeros? Si/No : ").upper()
    if operar!= "SI" and operar!= "NO":
        operar=input("¡¡Por favor, escriba Si o No!! : ").upper()

total= 1
for numero in lista_numeros_usuario:
    total= total*numero

print(" ")
print("----------------------------------------------------------------------------")
print("El total de la multiplicacion entre los numeros de su lista es: {}".format(total))
print("----------------------------------------------------------------------------")



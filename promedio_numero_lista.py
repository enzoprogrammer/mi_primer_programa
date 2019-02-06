lista_usuario=[]
operar= True
total_lista= 0

while operar!= False:
    numero_usuario= int(input("Digite un numero: "))
    lista_usuario.append(numero_usuario)

    seguir_operando= input("Desea añadir nuevos numeros a la lista? Si/No : ").upper()
    if seguir_operando== "NO":
        operar= False

for numero in lista_usuario:
    total_lista += numero

total_lista= total_lista/len(lista_usuario)
print(" ")
print(lista_usuario)
print(" ")
print("El promedio en su lista es: {}".format(total_lista))



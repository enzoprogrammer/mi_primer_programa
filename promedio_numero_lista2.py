lista_usuario = []

numero_iteraciones = int(input("Cuantos elementos quiere agregar a su lista? : "))
iteraciones = 0

while iteraciones < numero_iteraciones:
    numero_usuario=int(input("Digite un numero: "))
    lista_usuario.append(numero_usuario)
    iteraciones += 1

seguir_operando=input("Desea seguir añadiendo elementos a la lista? Si/No :").upper()

while seguir_operando== "SI":
    numero_usuario = int(input("Digite un numero: "))
    lista_usuario.append(numero_usuario)
    seguir_operando=input("Desea continuar añadiendo? Si/No :").upper()

total_numero=0
for numero in lista_usuario:
    total_numero+= numero
total_numero= total_numero/len(lista_usuario)

print(" ")
print("El promedio en su lista es: {}".format(total_numero))
print(" ")
print(lista_usuario)





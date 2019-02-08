lista_numeros=[]
multiplos_dos=[]
multiplos_tres=[]
multiplos_cinco=[]
multiplos_siete=[]

iteraciones= int(input("Cuantos elementos va a cargar a su lista? :"))
print(" ")

n_iteraciones= 0
while n_iteraciones < iteraciones:
    numeros_usuario= int(input("Digite un numero para agregar a la lista: "))
    lista_numeros.append(numeros_usuario)
    print(" ")
    n_iteraciones+=1

operar= "SI"
while operar != "NO":
    print(" ")
    operar=input("Desea añadir mas numeros? Si/No :").upper()
    if operar== "SI":
        numeros_usuario=int(input("Digite un numero para agregar a la lista: "))
        lista_numeros.append(numeros_usuario)

for numero in lista_numeros:
    if numero %2== 0:
        multiplos_dos.append(numero)
    if numero %3== 0:
        multiplos_tres.append(numero)
    if numero %5== 0:
        multiplos_cinco.append(numero)
    if numero %7== 0:
        multiplos_siete.append(numero)

print(" ")
print("-------------------------------------------------------------------")
print("Los multiplos de 2 son: {}".format(multiplos_dos))
print(" ")
print("Los multiplos de 3 son: {}".format(multiplos_tres))
print(" ")
print("Los multiplos de 5 son: {}".format(multiplos_cinco))
print(" ")
print("Los multiplos de 7 son: {}".format(multiplos_siete))
print("-------------------------------------------------------------------")



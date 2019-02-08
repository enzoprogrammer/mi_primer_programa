lista_numeros=[]
operar="SI"

while operar != "NO":
    numero_usuario= int(input("Digite un numero: "))
    lista_numeros.append(numero_usuario)
    print(" ")
    operar= input("Desea seguir cargando numeros a la lista? Si/No: ").upper()
    if operar!= "SI" and operar!="NO":
        print(" ")
        operar=input("¡¡Por favor escriba SI o NO!! :").upper()

maximo=lista_numeros[0]

for numero in lista_numeros:
    if numero > maximo:
        maximo= numero

print(" ")
print(" ")
print("El numero mayor en su lista es: {}".format(maximo))

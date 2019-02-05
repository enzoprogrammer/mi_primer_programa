print(" ")
print("Este programa cuenta las mayusculas dentro de una frase")
print(" ")
operar= True
mayusculas= ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Ñ", "Z", "X", "C", "V", "B", "N", "M"]

while operar != False:
    frase_usuario = input("Escriba una frase: ")
    contador_mayus= 0
    print(" ")

    for letra in frase_usuario:
        if letra in mayusculas:
            contador_mayus+= 1

    print("----------------------------------------------------")
    print("Hay {} mayuscula/s".format(contador_mayus))
    print("----------------------------------------------------")
    print(" ")

    seguir_operando= input("Desea seguir realizando operacioens? Si/No : ").upper()
    print(" ")
    if seguir_operando== "NO":
        operar= False

print(" ")
print("Turning Off...")


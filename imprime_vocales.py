print("")
print("Este programa sirve para imprimir por pantalla todas las vocales que aparecen en una frase...")
print(" ")
vocales=["a", "e", "i", "o", "u"]
operar= True
lista_vocales= []

while operar != False:
    frase_usuario= input("Escriba una frase: ")

    for letra in frase_usuario:
        if letra in vocales:
            lista_vocales.append(letra)

    print("Todas las vocales en su frase son: {}".format(lista_vocales))
    lista_vocales= []

    seguir_operando= input("Desea seguir operando en esta app? Si/No : ").upper()
    if seguir_operando== "NO":
        operar= False


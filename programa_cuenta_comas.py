print("Este programa te podra contar las comas, puntos y espacios de una frase que usted escriba...")
print(" ")
operar=True

while operar != False:
    frase_usuario = input("Escribe un frase: ")
    contador_espacios = 0
    contador_comas = 0
    contador_puntos = 0

    for letra in frase_usuario:
        if letra == " ":
            contador_espacios += 1
        elif letra == ".":
            contador_puntos += 1
        elif letra == ",":
            contador_comas += 1

    print("----------------------------------------------------------------------------------------")
    print(" Hay {} espacios".format(contador_espacios))
    print(" ")
    print(" Hay {} puntos".format(contador_puntos))
    print(" ")
    print(" Hay {} comas".format(contador_comas))
    print("----------------------------------------------------------------------------------------")

    seguir_operando= input("Quieres seguir usando la app? Si/No : ").upper()
    if seguir_operando== "NO":
        operar=False

print(" ")
print("Turning off...")



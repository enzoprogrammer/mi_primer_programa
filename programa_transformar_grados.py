print("Bienvenido al conversor de grados")
print(" ")
operar= True

while operar== True:
    conversion_deseada= input("De que tipo de grado desea convertir? Farenheit / Celsius : ").upper()
    print(" ")
    grados_convertir= int(input("Ingrese los grados {} que desea convertir: " .format(conversion_deseada)))
    print(" ")

    if conversion_deseada== "FARENHEIT":
        resultado= ((grados_convertir - 32)/1.8)
        print("El resultado en Celsius es {}°C" .format(resultado))
    elif conversion_deseada== "CELSIUS":
        resultado= ((grados_convertir * 1.8)+32)
        print("El resultado en Farenheit es {}°F".format(resultado))
    else:
        print("Escriba bien las opciones...")

    continuar= input("Desea seguir operando? Si/ No : ").upper()

    if continuar== "NO":
        operar= False

print(" ")
print("Turning Off...")







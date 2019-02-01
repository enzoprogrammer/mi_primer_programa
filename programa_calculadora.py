print("CALCULADORA... ")
print(" ")
operar= True

while operar !=False:
    operacion_elegida= input("Que operacion quiere hacer? (Suma / Resta / Multiplicacion / Division) :").upper()
    print(" ")
    primer_numero= int(input("Digite el primer numero: "))
    print(" ")
    segundo_numero= int(input("Digite el segundo numero: "))
    print(" ")

    if operacion_elegida== "SUMA":
        resultado= primer_numero + segundo_numero
        print("{} + {} = {}" .format(primer_numero, segundo_numero, resultado))
    elif operacion_elegida == "RESTA":
        resultado= primer_numero - segundo_numero
        print("{} - {} = {}".format(primer_numero, segundo_numero, resultado))
    elif operacion_elegida== "MULTIPLICACION":
        resultado= primer_numero * segundo_numero
        print("{} x {} = {}".format(primer_numero, segundo_numero, resultado))
    elif operacion_elegida== "DIVISION":
        resultado= primer_numero / segundo_numero
        print("{} / {} = {}".format(primer_numero, segundo_numero, resultado))
    else:
        print("Elija bien las opciones...")

    print(" ")
    seguir_operando= input("Desea realizar una nueva operacion? Si / No").upper()

    if seguir_operando== "NO":
        operar= False

print(" ")
print("------------------------POWER OFF-------------------------")
print(" ")





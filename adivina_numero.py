from random import randint, uniform,random

numero_a_adivinar = randint(1,15)

print("")
print("")
print("")
print("Bienvenido al juego de adivinar el numero del 1 al 15")
print("")
print("")
print("Tendras 5 intentos para adivnar el numero")
print("")
print("")


numero_usuario = int(input("Digite un numero: "))

if numero_a_adivinar == numero_usuario:
    print("Acertaste!")
else:
    print("Numero incorrecto")

    numero_usuario = int(input("Digite un numero: "))
    if numero_a_adivinar == numero_usuario:
        print("Acertaste!")
    else:
        print("Numero incorrecto")
        numero_usuario = int(input("Digite un numero: "))

        if numero_a_adivinar == numero_usuario:
            print("Acertaste!")
        else:
            print("Numero incorrecto")
            numero_usuario = int(input("Digite un numero: "))
            if numero_a_adivinar == numero_usuario:
                print("Acertaste!")
            else:
                print("Numero incorrecto")
                numero_usuario = int(input("Digite un numero: "))
                if numero_a_adivinar == numero_usuario:
                    print("Acertaste!")
                else:
                    print("Numero incorrecto, no te quedan mas intentos")
                    print("El numero era: {}".format (numero_a_adivinar))
print("")
print("")
print("")

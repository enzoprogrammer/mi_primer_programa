#Programa tabla de multiplicar que solo imprime multiplos de 2

tabla_multiplicar= int(input("Que tabla de multiplicar desea? : "))
print(" ")

for multiplo in range(1, 11):
    if ((tabla_multiplicar*multiplo)%2) ==0:
        print("{} x {} = {}".format(tabla_multiplicar, multiplo, tabla_multiplicar*multiplo))

